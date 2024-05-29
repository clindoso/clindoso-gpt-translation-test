import config
import os
import argparse
from utils import load_source_file_segments, join_translated_text, write_translated_file
from tr_utils import initialize_translation_memory, check_translation_memory, check_translations, handle_fuzzy_matches
import re
import time
import csv
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

def translate_with_gpt(client, segment, previous_segment, language, gpt_model, gpt_temperature=1.0):
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
    prompt = config.PROMPT.format(language=language)
    prompt_with_previous_sentence = config.PROMPT_WITH_PREVIOUS_SENTENCE.format(language=language, previous_segment=previous_segment)

    if previous_segment:

        response = client.chat.completions.create(
        model=gpt_model,
        temperature=gpt_temperature, 
        messages=[
            {"role": "system", "content": prompt_with_previous_sentence},
            {"role": "user", "content": segment}
          ]
        )
    
    else:
        response = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": segment}
          ]
        )
    
    gpt_translation = response.choices[0].message.content
    
    translated_segment = gpt_translation + " <!-- GPT translation -->"

    return translated_segment, gpt_translation

def translate_segment(segment, tm_dict, gpt_translation_dict, language, gpt_model, client, tm_segments_lengths, gpt_temperature=1.0, previous_segment=''):
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

    # Check for existing translation in TM
    tm_segment, tm_translation = check_translation_memory(segment, tm_dict)
    if tm_segment is not None:
        return tm_segment, tm_translation
    
    # Check for existing GPT translation
    gpt_segment, gpt_auto_propagation = check_translations(segment, gpt_translation_dict)
    if gpt_segment is not None:
        return gpt_segment, gpt_auto_propagation
    
    # Handle untranslated segments
    else:
        fuzzy_match = handle_fuzzy_matches(segment, tm_dict, tm_segments_lengths)
        if fuzzy_match:
            return fuzzy_match, segment
        else:
            translated_segment, gpt_translation = translate_with_gpt(client, segment, previous_segment, language, gpt_model, gpt_temperature)
            gpt_translation_dict[segment] = gpt_translation
            return translated_segment, gpt_translation


def process_front_matter(front_matter_segments, tm_dict, gpt_translation_dict, language, gpt_model, client, tm_segments_lengths, gpt_temperature=1.0):
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
    frontmatter_variables = config.FRONT_MATTER_VARIABLES
    GPT_TRANSLATION_MARKER = config.GPT_TRANSLATION_MARKER
    for segment in front_matter_segments:
        for frontmatter_variable in frontmatter_variables:
            if segment[0].startswith(frontmatter_variable):
                # Extract the title text and translate it
                translatable_text = segment[0][len(frontmatter_variable):]
                translated_text, _ = translate_segment(translatable_text, tm_dict, gpt_translation_dict,language, gpt_model, client, tm_segments_lengths, gpt_temperature)
                processed_segment_pair = (segment[0], frontmatter_variable + translated_text)
                break
            else:
                # No translation needed; reproduce the segment unchanged
                processed_segment_pair = segment
        processed_front_matter.append(processed_segment_pair)
    processed_front_matter.insert(-1, GPT_TRANSLATION_MARKER)

    return processed_front_matter

def translate_article(client, language, source_text, tm_dict, gpt_model, gpt_temperature):
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

    # Pre-calculate TM segments lengths for fuzzy match calculation
    tm_segments_lengths = {tm_segment:len(tm_segment) for tm_segment in tm_dict}

    # Initialize empty list to store translated segments from the article
    translated_segments = []

    # Initialize empty dictionary to store GPT translations for repetitions
    gpt_translation_dict = {}

    # Flags for formatting issues
    in_front_matter = False
    front_matter_processed = False
    in_code_quotation = False

    # Initialize empty previous segment
    previous_segment=''

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
            translated_front_matter = process_front_matter(front_matter_segments, tm_dict, gpt_translation_dict, language, gpt_model, client, tm_segments_lengths, gpt_temperature)
            front_matter_processed = True
            
        # Check commented out segment in English
        is_in_comment = False  # Flag to track if we are inside a comment block
        # Check if the current segment starts a comment block
        if segment.startswith("\s*<!--"):
            is_in_comment = True

        pattern = r'^\}|^<style>|^<details|^<summary>|^<br>$|^<table>|\s+<thead>|\s+<tr>|\s+</tr>|\s+</thead>|</table>|</details>'
        
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
        
        elif re.match(pattern, segment):
            # Reproduce table formatting
            translated_segments.append((segment, segment))
            continue

        # Handle code quotation
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
            translated_segment.append((segment, ''))
            continue

        # Check for leading right angle bracket without further content
        elif re.match(r' *> *\n', segment):
            translated_segments.append((segment, segment))
            continue

        # Translate segment using TM, fuzzy matching, or GPT
        else:
            translated_segment, previous_segment = translate_segment(segment, tm_dict, gpt_translation_dict, language, gpt_model, client, tm_segments_lengths, gpt_temperature, previous_segment)
            translated_segments.append((segment, translated_segment))
            print(f'- Source segment:\n{segment}')
            print(f'- Target segment:\n{translated_segment}\n-------------------')
            continue
        
    # Prepends translated front matter segments to translated segments
    translated_segments = translated_front_matter + translated_segments

    # Return list of tuples with source and target segments
    return translated_segments

def main():
    # Start time tracker
    start_time = time.time()

    # Initialize OpenAI client
    client = initialize_open_ai_client()

    # Parse command-line arguments
    lang, source = parse_arguments()

    # Initialize language models
    language, gpt_model, tm_path = initialize_language_model(lang)

    # Fetch gpt_temperature
    if not config.GPT_TEMPERATURE:
        print("---\nGPT temperature directory not defined in the config file. The default temperature is 1.0\n---")
    else:
        gpt_temperature = config.GPT_TEMPERATURE
    
    
    # Initialize translation memory dictionary
    tm_dict = initialize_translation_memory(lang, tm_path)
    
    # Load source file segments
    source_text = load_source_file_segments(source)

    # Perform the translation
    translated_segments = translate_article(client, language, source_text, tm_dict, gpt_model, gpt_temperature)

    # Create list with translated text
    translated_text = join_translated_text(translated_segments)

    # Save file in repository
    write_translated_file(language, source, translated_text)

    # Output the result and time taken
    elapsed_time = round((time.time() - start_time), 2)
    print(f"Time taken: {elapsed_time} seconds")

if __name__ == "__main__":
    main()
