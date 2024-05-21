import config
import os
import argparse
import time
import csv
import re
import Levenshtein as lev
from transformers import EncoderDecoderModel, AutoTokenizer
import torch
from term_scraper import extract_terms_from_directory


# Use this script to translate whole articles from English into German, Spanish, French, Italian, or Dutch with ChatGPT.
# The script takes two arguments, --lang and--source, respectively the target language and the source file to be translated.

def load_model(model_path):
    """
    Loads the model and tokenizer based on the given path to the model directory.

    Parameters:
        model_path (str): The file path to the directory where the model and tokenizer are saved. This should
                          be the path to a directory containing model files compatible with Hugging Face transformers.

    Returns:
        tuple: A tuple containing two elements:
               - tokenizer (transformers.PreTrainedTokenizer): The loaded tokenizer ready to process input.
               - model (transformers.PreTrainedModel): The loaded model ready for generating predictions.
    
    Raises:
        OSError: If the model or tokenizer files do not exist at the provided path.
        ValueError: If the loaded model is not compatible with expected use in generation or other tasks.
    """
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = EncoderDecoderModel.from_pretrained(model_path)
        return tokenizer, model
    except Exception as e:
        print(f"Failed to load model with error: {e}")
        raise

def parse_arguments():
    """
    Parse command-line arguments for language and source file.
    Returns a tuple of (language, source file path).
    """
    parser = argparse.ArgumentParser(description="Script to translate texts using TM and ChatGPT")
    parser.add_argument("--source", required=True, help="Source file for translation")
    parser.add_argument("--lang", required=False, help="Target language for translation", default="nl")
    args = parser.parse_args()
    return args.lang, args.source

def load_source_file_segments(source):
    """
    Reads and parses the source file.
    
    Parameters:
        source_path (str): Path to the source file.
    
    Returns:
        list: A list of segments from the source file, or None if file not found.
    """
    # Check if source path exists
    if not os.path.exists(source):
        print("Source file not found. Check the source file path entered.")
        return None

    # Read source file
    with open(source, 'r') as file:
        file_content = file.read()
    
    # Split text into segments
    source_text = file_content.splitlines()

    return source_text

def initialize_language_model(lang):
    """
    Initializes language model.
    Returns language name, gpt_model, tm_path
    """
    # Define language model dictionary
    language_models = config.LANGUAGE_MODELS
    # Initialize language model
    if lang in language_models:
        language = language_models[lang]["language"]
        tm_path = language_models[lang]["tm_path"]
    else:
        raise ValueError("""
              You entered an invalid language code. Use one of the following:
              "de" for German
              "es" for Spanish
              "fr" for French
              "it" for Italian
              "nl" for Dutch
        """)

    return language, tm_path

def initialize_translation_memory(lang, tm_path):
    """
    Initializes the translation memory of the target language
    Parameters:
        lang: Target language code
        tm_path: Translation memory path
    Returns dictionary with the TM
    """
    # Initialize tm dictionary to use TM content in the translation
    tm_dict = {}
    # Read the TM and extract the 'en' and target language column
    with open(tm_path, 'r', encoding='utf-8') as tm:
        reader = csv.DictReader(tm)
        for row in reader:
            tm_dict[row['en']] = row[lang]
    
    return tm_dict

def check_translation_memory(segment, tm_dict):
    """
    Checks if the segment has a translation in the translation memory (TM).

    Parameters:
        segment (str): The current text segment.
        tm_dict (dict): The translation memory dictionary.

    Returns:
        tuple or None: The TM translation if available, else None.
    """
    if segment in tm_dict:
        return tm_dict[segment] + " <!-- TM 100 -->"
    return None

def check_robbert_translations(segment, robbert_translation_dict):
    """
    Checks for existing translations of the segment in GPT translation dictionary.

    Parameters:
        segment (str): The current text segment.
        robbert_translation_dict (dict): Dictionary containing GPT translations.

    Returns:
        tuple or None: The GPT translation if available, else None.
    """
    if segment in robbert_translation_dict:
        return (segment, robbert_translation_dict[segment] + " <!-- Repetition of GPT translation -->")
    return None

def handle_fuzzy_matches(segment, tm_dict, tm_segments_lengths):
    """
    Handles fuzzy matches for the segment using Levenshtein distance.

    Parameters:
        segment (str): The current text segment.
        tm_dict (dict): The translation memory dictionary.
        tm_segments_lengths (dict): Dictionary of lengths of TM segments.

    Returns:
        tuple or None: The best fuzzy match from TM if found, else None.
    """
    # Initialize lower and upper thresholds
    lower_threshold = config.LOWER_THRESHOLD
    upper_threshold = config.UPPER_THRESHOLD
    
    # Initialize closest segment match and min normalized edit distance
    closest_segment, normalized_min_edit_distance = None, 1
    # Calculate source segment length
    segment_length = len(segment)

    # Iterate over TM segment lenghts
    for tm_segment, tm_segment_length in tm_segments_lengths.items():
    # Avoid calculation if length difference is over the upper threshold
        if abs(segment_length - tm_segment_length) / max(segment_length, tm_segment_length) > upper_threshold:
            continue

        # Calculate Levenshtein edit distance and normalize it
        edit_distance = lev.distance(segment, tm_segment)
        normalized_edit_distance = edit_distance / max(segment_length, tm_segment_length)

        # Update closes match if a closer one is found
        if normalized_edit_distance < normalized_min_edit_distance:
            closest_segment, normalized_min_edit_distance = tm_segment, normalized_edit_distance

        # Early exit if a sufficiently close match is found
        if normalized_edit_distance < lower_threshold:
            break

        # If the smallest edit distance is below the threshold, use content of TM
        if normalized_min_edit_distance < upper_threshold:
            fuzzy_match_score = (1 - normalized_min_edit_distance)
            return (segment, tm_dict[closest_segment] + f" <!-- TM {fuzzy_match_score*100:.0f} -->")
    
    # If there is no segment with an edit below the upper threshold, return None
    return None

def translate_with_robbert(segment, tokenizer, model, max_length_factor=1.5, batch_size=8):
    """
    Generates text from a given prompt using the specified tokenizer and model.

    Parameters_
        prompt (str): The input string to generate text from.
        tokenizer (transformers.PreTrainedTokenizer): The tokenizer for encoding the input.
        model (transformers.PreTrainedModel): The model used 
    """    
    
    # Encode the prompt into tensor format
    inputs = tokenizer.encode_plus(segment, return_tensors='pt')
    input_length = inputs['input_ids'].size(1)  # Now you access input_ids from a dictionary
    max_length = int(input_length * max_length_factor) # Set maximum length based on the input length and factor

    # Generate outputs from the model without updating gradients
    with torch.no_grad():
        outputs = model.generate(
            inputs.input_ids,
            max_length=min(max_length, 512),
            num_beams=10,
            num_return_sequences=1,
            temperature=1.0,
            no_repeat_ngram_size=2,
            top_k=50,
            top_p=0.95,
            early_stopping=True
        )

    generated_text = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    generated_text_str = ' '.join(generated_text)
    print(f"Source segment: {segment}")
    print(f"Generated text: {generated_text_str}")
    translated_segment = generated_text_str + " <!-- RobBERT translation -->"

    return translated_segment, generated_text

def translate_segment(segment, tm_dict, robbert_translation_dict, tokenizer, model):
    """
    Translate a single text segment using a translation memory (TM)
    and generative translation

    Parameters:
    - segment: Text segment to be transalted.
    - tm_dict: Dictionary containing existing translations in TM.
    - robbert_translation_dict: Dictionary containing target language segments translated by GPT.
    - language: Target language for translation.
    - gpt_model: GPT model to be used for translation.
    - client: Client object to interact with OpenAI API.

    Returns:
    - A tuple containing the original segment and its translation.
    """

    # Check for existing translation in TM
    tm_translation = check_translation_memory(segment, tm_dict)
    if tm_translation:
        return tm_translation
    
    # Check for existing GPT translation
    robbert_translation = check_robbert_translations(segment, robbert_translation_dict)
    if robbert_translation:
        return robbert_translation
    
    # Handle untranslated segments
    else:
        translated_segment, robbert_translation = translate_with_robbert(segment, tokenizer, model)
        robbert_translation_dict[segment] = robbert_translation
        return translated_segment


def process_front_matter(front_matter_segments, tm_dict, robbert_translation_dict, tokenizer, model):
    """
    Processes the front matter of a document, translating 'title' and 'description'
    fields while leaving their labels and other metadata unchanged.

    Parameters:
    - front matter_segments (list of str): The front matter of the document as a list of strings.
    - language_code (str): The target language code for translation.

    Returns:
    - list of str: The processed front matter segments.
    """
    processed_front_matter = []
    frontmatter_variables = config.front_matter_variables
    gpt_translation_marker = config.gpt_translation_marker
    for segment in front_matter_segments:
        for frontmatter_variable in frontmatter_variables:
            if segment[0].startswith(frontmatter_variable):
                # Extract the title text and translate it
                translatable_text = segment[0][len(frontmatter_variable):]
                translated_text = translate_segment(translatable_text, tm_dict, robbert_translation_dict,tokenizer, model)
                processed_segment_pair = (segment[0], frontmatter_variable + translated_text[1])
                break
            else:
                # No translation needed; reproduce the segment unchanged
                processed_segment_pair = segment
        processed_front_matter.append(processed_segment_pair)
    processed_front_matter.insert(-1, gpt_translation_marker)

    return processed_front_matter

def translate_article(source_text, tm_dict, tokenizer, model):
    """
    Translates the content of the source file using the specified language model.

    Parameters:
        client (OpenAI client object): The OpenAI client for API requests.
        language (str): Target language code.
        source_text (list): List of text segments from the source file.
        tm_dict (dict): The translation memory dictionary.
        gpt_model (str): The GPT model to use for translation.

    Returns:
        list: List of tuples with source and translated segments.
    """ 
    # Initialize empty list to store front matter segments
    front_matter_segments = []

    # Initialize empty list to store translated segments from the article
    translated_segments = []

    # Initialize empty dictionary to store GPT translations for repetitions
    robbert_translation_dict = {}

    # Flag to check front matter
    in_front_matter = False
    front_matter_processed = False
    in_code_quotation = False

    # Iterate over each segment of the source text
    for segment in source_text:
        # Check if segment is the start or end of the front matter
        if segment == '---':
            front_matter_segments.append((segment, segment))
            # Change flag after finding start or end of the front matter
            in_front_matter = not in_front_matter
            continue

        # Reproduce front matter in the target file
        elif in_front_matter:
            front_matter_segments.append((segment, segment))
            continue
        
        if not in_front_matter and not front_matter_processed:
            translated_front_matter = process_front_matter(front_matter_segments, tm_dict, robbert_translation_dict, tokenizer, model)
            front_matter_processed = True
            
        is_in_comment = False  # Flag to track if we are inside a comment block
        # Check if the current segment starts a comment block
        if segment.startswith("<!--"):
            is_in_comment = True
        
        # If inside a comment block, reproduce the segment untranslated
        if is_in_comment:
            translated_segments.append((segment, segment))

            # Check if the current segment ends the comment block
            if segment.endswith("-->"):
                is_in_comment = False

            continue # Skip further processing for this segment
    
        # Handle Markdown table formatting
        elif re.match(r'^\|(\s?)---', segment):
            # Reproduce table formatting
            translated_segments.append((segment, segment))
            continue

        # Handle for code quotation
        elif re.match(r'^ *```', segment):
            # Reproduce quotation segments
            translated_segments.append((segment, segment))
            in_code_quotation = not in_code_quotation
            continue

        elif in_code_quotation:
            translated_segments.append((segment, segment))
            continue

        # Check for empty segments
        elif segment == '':
            # Reproduce empty segments
            translated_segments.append((segment, segment))
            continue

        # Check for segments only with spaces
        elif re.match(r'^ +\n', segment):
            # Append empty segment
            translated_segments.append((segment, ''))
            continue

        # Check for leading right angle bracket without further content
        elif re.match(r'^ *> *$', segment):
            translated_segments.append((segment, segment))
            continue

        # Translate segment using TM or GPT
        else:
            translated_segment = translate_segment(segment, tm_dict, robbert_translation_dict, tokenizer, model)
            translated_segments.append((segment, translated_segment))
            print(f'- Source segment:\n{segment}')
            print(f'- Target segment:\n{translated_segment}\n-------------')
            continue
        
    # Prepends translated front matter segments to translated segments
    translated_segments = translated_front_matter + translated_segments
    
    # Store segment to serve as context for next segment

    # Return list of tuples with source and target segments
    return translated_segments

def join_translated_text(translated_segments):
    """
    Extracts the target text the translated segments list
    Returns text in one string
    """
    # Initialize list to store extracted segments
    extracted_segments = []
    # Iterate over segments
    for _, target_segment in translated_segments:
        # Extract segments from tuples
        extracted_segments.append(target_segment)
    # Join text list in one string 
    joint_translated_text = "\n".join(extracted_segments)

    return joint_translated_text

def write_translated_file(language, source, translated_article):
    """
    Saves translated article with the same name of the source file in a subdirectory of the source file
    Parameters:
      language: Language for translation
      source: Source file path
      translated_article: Article in target language
    """

    # Extract source directory
    source_directory = os.path.dirname(source)
    
    # Define translation file name
    output_filename = source.split('/')[-1]
    
    # Define translation directory
    output_directory = os.path.join(source_directory, f"{language}_translation_output/")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Define translation file path
    output_filepath = os.path.join(output_directory, output_filename)

    # Write the translated article to the output file
    with open(output_filepath, 'w', encoding='utf-8') as output_file:
        output_file.write(translated_article)
        print(f"Translation was written to {output_filepath}")

def main():
    # Start time tracker
    start_time = time.time()

    # Initialize termbase directory from config
    if not config.TERMBASE_DIRECTORY:
        raise EnvironmentError("Termbase directory not defined in the config file.")
    else: termbase_directory = config.TERMBASE_DIRECTORY

    # Initialize source language spaCy model directory from config
    if not config.ROBBERT_MODEL_PATH:
        raise EnvironmentError("RobBERT model path is not defined in the config file.")
    else: model_path = config.ROBBERT_MODEL_PATH

    # Parse command-line arguments
    lang, source = parse_arguments()

    # Initialize language models

    for key, value in config.LANGUAGE_MODELS[lang].items():
        if not value:
            raise EnvironmentError(f"{key} not defined for the target language in the language models in the config file.")
        else: language, tm_path = initialize_language_model(lang)

    # Initialize translation memory dictionary
    tm_dict = initialize_translation_memory(lang, tm_path)

    # Load source file segments
    source_text = load_source_file_segments(source)

    tokenizer, model = load_model(model_path)

    # Perform the translation
    translated_segments = translate_article(source_text, tm_dict, tokenizer, model)

    # Create list with translated text
    translated_text = join_translated_text(translated_segments)

    # Save file in repository
    write_translated_file(language, source, translated_text)

    # Output the result and time taken
    elapsed_time = round((time.time() - start_time), 2)
    print(f"Time taken: {elapsed_time} seconds")

if __name__ == "__main__":
    main()