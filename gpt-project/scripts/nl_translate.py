import config
import os
import argparse
import time
import csv
import re
import Levenshtein as lev
from openai import OpenAI

# Use this script to translate whole articles from English into German, Spanish, French, Italian, or Dutch with ChatGPT.
# The script takes two arguments, --lang and--source, respectively the target language and the source file to be translated.

def initialize_open_ai_client():
    """
    Initialize OpenAI client using API key from the config file
    Returns the client object if the key is found, otherwise raises error
    """
    if not config.OPENAI_API_KEY:
        raise EnvironmentError("OPENAI_API_KEY environment variable not found.")
    return OpenAI(api_key=config.OPENAI_API_KEY)

def parse_arguments():
    """
    Parse command-line arguments for language and source file.
    Returns a tuple of (language, source file path).
    """
    parser = argparse.ArgumentParser(description="Script to translate texts using TM and ChatGPT")
    parser.add_argument("--lang", required=True, help="Target language for translation")
    parser.add_argument("--source", required=True, help="Source file for translation")
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
        gpt_model = language_models[lang]["gpt-model"]
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

    return language, gpt_model, tm_path

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
        return (segment, tm_dict[segment] + " <!-- TM 100 -->")
    return None

def check_gpt_translations(segment, gpt_translation_dict):
    """
    Checks for existing translations of the segment in GPT translation dictionary.

    Parameters:
        segment (str): The current text segment.
        gpt_translation_dict (dict): Dictionary containing GPT translations.

    Returns:
        tuple or None: The GPT translation if available, else None.
    """
    if segment in gpt_translation_dict:
        return (segment, gpt_translation_dict[segment] + " <!-- Repetition of GPT translation")
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

def translate_with_gpt(client, segment, previous_segment, language, gpt_model):
    """
    Translates the segment using GPT.

    Parameters:
        client (OpenAI client object): The OpenAI client for API requests.
        segment (str): The current text segment.
        language (str): Target language code.
        gpt_model (str): The GPT model to use for translation.

    Returns:
        str: The translated segment.
    """

    if previous_segment:

        response = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": f"Given a sentence in Markdown format, translate the sentence to {language} keeping the style, tone, formatting, and terminology consistent and provide strictly just the translation in plain language. For context, consider that the sentence preceding the one you will translate is: '{previous_segment}'"},
            {"role": "user", "content": segment}
          ]
        )
    
    else:
        response = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": f"Given a sentence in Markdown format, translate the sentence to {language} keeping the style, tone, formatting, and terminology consistent and provide strictly just the translation in plain language."},
            {"role": "user", "content": segment}
          ]
        )
    
    translated_segment = response.choices[0].message.content
    print(translated_segment)

    return translated_segment

def translate_segment(segment, tm_dict, gpt_translation_dict, language, gpt_model, client):
    """
    Translate a single text segment using a translation memory (TM)
    and generative translation

    Parameters:
    - segment: Text segment to be transalted.
    - tm_dict: Dictionary containing existing translations in TM.
    - gpt_translation_dict: Dictionary containing target language segments translated by GPT.
    - language: Target language for translation.
    - gpt_model: GPT model to be used for translation.
    - client: Client object to interact with OpenAI API.

    Returns:
    - A tuple containing the original segment and its translation.
    """
    # Pre-calculate TM segments lengths for fuzzy match calculation
    previous_segment = ''
    # tm_segments_lengths = {tm_segment:len(tm_segment) for tm_segment in tm_dict}

    # Check for existing translation in TM
    tm_translation = check_translation_memory(segment, tm_dict)
    if tm_translation:
        return tm_translation
    
    # Check for existing GPT translation
    gpt_translation = check_gpt_translations(segment, gpt_translation_dict)
    if gpt_translation:
        return gpt_translation
    
    # Handle untranslated segments
    else:
        translated_segment = translate_with_gpt(client, segment, previous_segment, language, gpt_model)
        gpt_translation_dict[segment] = translated_segment
        return (segment, translated_segment + " <!-- GPT translation -->")


def process_front_matter(front_matter_segments, tm_dict, gpt_translation_dict, language, gpt_model, client):
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
    for line in front_matter_segments:
        if line[0].startswith('title: '):
            # Extract the title text and translate it
            title_text = line[0][len('title: '):]
            translated_title = translate_segment(title_text, tm_dict, gpt_translation_dict,language, gpt_model, client)
            processed_segment_pair = (line[0], 'title: ' + translated_title[1])
        elif line[0].startswith('description: '):
            # Extract the description text and translate it
            description_text = line[0][len('description: '):]
            translated_description = translate_segment(description_text, tm_dict, gpt_translation_dict,language, gpt_model, client)
            processed_segment_pair = (line[0], 'description: ' + translated_description[1])
        else:
            # No translation needed; reproduce the line unchanged
            processed_segment_pair = line
        processed_front_matter.append(processed_segment_pair)

    return processed_front_matter

def translate_article(client, language, source_text, tm_dict, gpt_model, lang):
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
    gpt_translation_dict = {}

    # Flag to check front matter
    in_front_matter = False
    front_matter_processed = False

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
            translated_front_matter = process_front_matter(front_matter_segments, tm_dict, gpt_translation_dict, language, gpt_model, client)
            front_matter_processed = True
            
        # Check commented out segment in English
        if segment.startswith("<!--"):
            # Reproduce untranslated commented out segment
            translated_segments.append((segment, segment))
            continue
        
        # Check for code quotation

        elif re.match(r'^ *```', segment):
                    # Reproduce empty segments
            translated_segments.append((segment, segment))
            continue

        # Check for empty segments
        elif segment == '':
            # Reproduce empty segments
            translated_segments.append((segment, segment))
            continue

        # Translate segment using TM, fuzzy matching, or GPT
        else:
            segment, translated_segment = translate_segment(segment, tm_dict, gpt_translation_dict, language, gpt_model, client)
            previous_segment = segment
            translated_segments.append((segment, translated_segment))
            continue
        
    # Prepends translated front matter segments to translated segments
    translated_segments = translated_front_matter + translated_segments

    # Return list of tuples with source and target segments
    print(translated_segments)
    return translated_segments

def extract_translated_text(translated_segments):
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

    # Initialize OpenAI client
    client = initialize_open_ai_client()

    # Parse command-line arguments
    lang, source = parse_arguments()

    # Initialize language models
    language, gpt_model, tm_path = initialize_language_model(lang)
    
    # Initialize translation memory dictionary
    tm_dict = initialize_translation_memory(lang, tm_path)
    
    # Load source file segments
    source_text = load_source_file_segments(source)

    # Perform the translation
    translated_segments = translate_article(client, language, source_text, tm_dict, gpt_model, lang)

    # Create list with translated text
    translated_text = extract_translated_text(translated_segments)

    # Save file in repository
    write_translated_file(language, source, translated_text)

    # Output the result and time taken
    elapsed_time = round((time.time() - start_time), 2)
    print(f"Time taken: {elapsed_time} seconds")

if __name__ == "__main__":
    main()