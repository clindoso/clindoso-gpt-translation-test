import config
import os
import argparse
import time
import csv
import re
import Levenshtein as lev
import spacy
from openai import OpenAI
from term_scraper import extract_terms_from_directory

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
    parser.add_argument("--segment", required=True, help="Segment for translation")
    args = parser.parse_args()
    return args.lang, args.segment

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

def tokenize(text, model):
    pass

def initialize_tokenized_termbase(termbase_directory, lang):
    """
    Initializes the termbase for the target language
    Parameters:
        termbase_directory (str): Termbase directory path
        lang (str): Target language code
    """
    term_list = extract_terms_from_directory(termbase_directory, lang)
    model = spacy.load(f"{lang}_core_news_sm")
    # tokenized_termbase = {tokenize_with_spacy(source_term): tokenize_with_spacy(target_term) for source_term, target_term in term_list}
    
    # return tokenized_termbase

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
    
    translated_segment = response.choices[0].message.content

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
        gpt_translation_dict[segment] = translated_segment
        return (segment, translated_segment + " <!-- GPT translation -->")

def main():

    # Initialize termbase
    if not config.termbase_directory:
        raise EnvironmentError("Source termbase directory not defined in the config file.")
    else: termbase_directory = config.termbase_directory

    # Initialize OpenAI client
    client = initialize_open_ai_client()

    # Parse command-line arguments
    lang, segment = parse_arguments()

    # Initialize language models
    language, gpt_model, tm_path = initialize_language_model(lang)
    
    # Initialize translation memory dictionary
    tm_dict = initialize_translation_memory(lang, tm_path)

    # Initialize termbase
    # termbase = initialize_termbase(termbase_directory, lang)

    gpt_translation_dict = {}
    # Perform the translation
    translated_segment = translate_segment(segment, tm_dict, gpt_translation_dict, language, gpt_model, client)
    print(f"The source text is:\n\n{translated_segment[0]}\n\nThe target text is:\n\n{translated_segment[1]}")

if __name__ == "__main__":
    main()
