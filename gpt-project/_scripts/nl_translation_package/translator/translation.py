from nl_translation_package.config import LANGUAGE_MODELS, LOWER_THRESHOLD, UPPER_THRESHOLD, FRONT_MATTER_VARIABLES, GPT_TRANSLATION_MARKER
from .openai_api_client import OpenAIClient
import csv
import re
import Levenshtein as lev
from openai import OpenAI

def initialize_language_model(lang):
    """
    Initializes language model.
    Returns language name, gpt_model, tm_path
    """
    # Define language model dictionary
    language_models = LANGUAGE_MODELS
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
        return (segment, gpt_translation_dict[segment] + " <!-- Repetition of GPT translation -->")
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
        return (segment, gpt_translation_dict[segment] + " <!-- Repetition of GPT translation -->")
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
    lower_threshold = LOWER_THRESHOLD
    upper_threshold = UPPER_THRESHOLD
    
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

def translate_with_gpt(client, segment, language, gpt_model, previous_segment=''):
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
    
    translated_segment = (segment, response.choices[0].message.content + " <!-- GPT translation -->")

    # Tokenize {segment} and check if tokens any of the tokens is in the tokens dictionary
    # If they are, check if the correspondent in the target language is in the {translated segment}
    # If it is not, prompt model to rephrase the {translated segment} based on the target language token

    return translated_segment

def translate_segment(segment, tm_dict, gpt_translation_dict, language, gpt_model, client, previous_segment=''):
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
    tm_translation = check_translation_memory(segment, tm_dict)
    if tm_translation:
        return tm_translation
    
    # Check for existing GPT translation
    gpt_translation = check_gpt_translations(segment, gpt_translation_dict)
    if gpt_translation:
        return gpt_translation
    
    # Handle untranslated segments
    else:
        translated_segment = translate_with_gpt(client, segment, language, gpt_model, previous_segment)
        gpt_translation_dict[segment] = translated_segment[1]
        return translated_segment


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
    frontmatter_variables = FRONT_MATTER_VARIABLES
    gpt_translation_marker = GPT_TRANSLATION_MARKER
    for segment in front_matter_segments:
        for frontmatter_variable in frontmatter_variables:
            if segment[0].startswith(frontmatter_variable):
                # Extract the title text and translate it
                translatable_text = segment[0][len(frontmatter_variable):]
                translated_text = translate_segment(translatable_text, tm_dict, gpt_translation_dict,language, gpt_model, client)
                processed_segment_pair = (segment[0], frontmatter_variable + translated_text[1])
                break
            else:
                # No translation needed; reproduce the segment unchanged
                processed_segment_pair = segment
        processed_front_matter.append(processed_segment_pair)
    processed_front_matter.insert(-1, gpt_translation_marker)

    return processed_front_matter

def translate_article(client, language, source_text, tm_dict, gpt_model):
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
    in_code_quotation = False
    previous_segment = ''

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
        elif re.match(r'^ +\n', segment[0]):
            # Append empty segment
            translated_segments.append((segment, ''))
            continue

        # Check for leading right angle bracket without further content
        elif re.match(r' *> *\n', segment[0]):
            translated_segments.append((segment, segment))
            continue

        # Translate segment using TM or GPT
        else:
            segment, translated_segment = translate_segment(segment, tm_dict, gpt_translation_dict, language, gpt_model, client, previous_segment)
            translated_segments.append((segment, translated_segment))
            previous_segment = segment
            print(f'- Source segment:\n{segment}')
            print(f'- Target segment:\n{translated_segment}\n-------------')
            continue
        
    # Prepends translated front matter segments to translated segments
    translated_segments = translated_front_matter + translated_segments
    
    # Store segment to serve as context for next segment

    # Return list of tuples with source and target segments
    return translated_segments