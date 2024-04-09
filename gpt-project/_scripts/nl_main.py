import config
import os
import argparse
import time
import csv
import re
import Levenshtein as lev
import spacy
from spacy.matcher import PhraseMatcher
from openai import OpenAI
from term_scraper import extract_terms_from_directory
from langdetect import detect_langs


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
        gpt_model = language_models[lang]["gpt-model"]
        tm_path = language_models[lang]["tm_path"]
        target_spacy_model = language_models[lang]["target_spacy_model"]
    else:
        raise ValueError("""
              You entered an invalid language code. Use one of the following:
              "de" for German
              "es" for Spanish
              "fr" for French
              "it" for Italian
              "nl" for Dutch
        """)

    return language, gpt_model, tm_path, target_spacy_model

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

def initialize_termbase(termbase_directory, lang):
    termbase = extract_terms_from_directory(termbase_directory, lang)

    return termbase

def split_termbase(termbase):
    source_terms = [term_tuple[0] for term_tuple in termbase]
    target_terms = [term_tuple[1] for term_tuple in termbase]

    return source_terms, target_terms

def lemmatize_term(model, term):
    """
    Lemmatize a list of terms using a spaCy model.

    Parameters:
    - model (spaCy model): The spaCy language model.
    - terms (list of str): The terms to lemmatize.

    Returns:
    - dict: A dictionary with original terms as keys and their lemmatized forms as values.
    """
    doc = model(term)
    lemmatized_term = ' '.join([token.lemma_ for token in doc])
    return lemmatized_term

def detect_language(text, lang, source_lang='en'):
    detections = detect_langs(text)
    # Convert detections to a dictionary {language_code: confidence}
    detection_dict = {str(detection.lang): detection.prob for detection in detections}

    # Get confidence scores for the source and target languages, defaulting to 0 if not detected
    source_confidence = detection_dict.get(source_lang, 0)
    target_confidence = detection_dict.get(lang, 0)

    # Determine which languages has a higher confidence score, defaulting to the source language if equal
    if source_confidence <= target_confidence:
        return source_lang
    else:
        return lang


def lemmatize_termbase(source_model, target_model, termbase, lang):
    source_terms = [term_tuple[1] for term_tuple in termbase]
    target_terms = [term_tuple[2] for term_tuple in termbase]

    lemmatized_source_terms = []
    for source_term in source_terms:
        lemmatized_source_term = lemmatize_term(source_model, source_term)
        lemmatized_source_terms.append(lemmatized_source_term)
    lemmatized_target_terms = []
    for target_term in target_terms:
        language = detect_language(target_term, lang)
        print(f"\nTerm: {target_term}\n")
        print(f"Language: {language}\n---------------------")
        if language == lang:
            lemmatized_target_term = lemmatize_term(target_model, target_term)
        else:
            lemmatized_target_term = lemmatize_term(source_model, target_term)
        
        lemmatized_target_terms.append(lemmatized_target_term)
    lemmatized_termbase = [(term_tuple[0], lemmatized_source_terms[i], lemmatized_target_terms[i]) for i, term_tuple  in enumerate(termbase)]

    return lemmatized_termbase

def initialize_spacy_models(target_spacy_model, source_spacy_model):
    source_model = spacy.load(source_spacy_model)
    target_model = spacy.load(target_spacy_model)

    return source_model, target_model

def setup_phrase_matcher(model, terms):
    # target_model = spacy.load(f"{lang}_core_news_sm")
    phrase_matcher = PhraseMatcher(model.vocab, attr='LEMMA')
    add_terms_to_matcher(phrase_matcher, model, terms)
    
    return phrase_matcher

def add_terms_to_matcher(matcher, model, terms):
    # Convert each term into a Doc object and add it to the matcher
    for term in terms:
        doc = model(term)  # Process the term to create a Doc
        matcher.add("TermbaseTerms", [doc])

def filter_matches(phrase_matcher, doc):
    # Find matches
    matches = phrase_matcher(doc)
    # Sort matches
    matches = sorted(matches, key=lambda x: x[2] - x[1], reverse=True)
    # Filter overlapping matches, keeping only longest match
    filtered_matches = []
    seen_ranges = set()
    for match_id, start, end in matches:
        if not any(start >= existing_start and end <= existing_end for existing_start, existing_end in seen_ranges):
            filtered_matches.append((match_id, start, end))
            seen_ranges.add((start, end))

    return filtered_matches

def index_matches_by_lemma(doc, matches):
    """
    Index matches by their lemma form.
    
    Üarameters:
    - doc (spaCy Doc): The processed document.
    - matches (list): The list of matches from the PhraseMatcher.
    
    Returns:
    - dict: A dictionary with lemmas as keys and lists of match positions.
    """
    lemma_matches = {}
    for _, start, end in matches:
        # Extract the match span
        span = doc[start:end]
        lemma = ' '.join([token.lemma_ for token in span])
        if lemma not in lemma_matches:
            lemma_matches[lemma] = []
        lemma_matches[lemma].append((start, end))
    return lemma_matches

def match_terms_in_text(model, matcher, text):
    """
    Identifies if the terms from the PhraseMatcher are present in the given text.
    
    Parameters:
        model (spacy.language.Language): The spaCy language model for processing the text.
        matcher (PhraseMatcher): The PhraseMatcher object with the terms to match.
        text (str): The text to search for the terms.
    
    Returns:
        bool: True if any of the terms are found in the text, False otherwise.
    """
    doc = model(text)
    matches = matcher(doc)
    return matches

def verify_termbase_compliance(source_lemma_matches, target_lemma_matches, lemmatized_termbase):
    term_not_found = False
    for _, source_term, target_term in lemmatized_termbase:
        # Check if lemmatized source term is in source lemma matches

        if source_term not in source_lemma_matches:
            continue # Source term not found
        if target_term not in target_lemma_matches:
            print(f"Term not translated: {source_term} -> {target_term}")
            term_not_found = True
            continue
        if term_not_found:
            return False
        else: 
            return True


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

def translate_with_gpt(client, segment, language, gpt_model, source_model, target_model, source_phrase_matcher, target_phrase_matcher, lemmatized_termbase, previous_segment=''):
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
    
    gpt_translation = response.choices[0].message.content

    # Create Doc out of segment and translation
    segment_doc = source_model(segment)
    gpt_translation_doc = target_model(gpt_translation)
    # Lemmatize segment and translation
    lemmatized_segment = " ".join([token.lemma_ for token in segment_doc])
    lemmatized_gpt_translation = " ".join([token.lemma_ for token in gpt_translation_doc])

    # Find matches
    source_matches = filter_matches(source_phrase_matcher, segment_doc)
    target_matches = filter_matches(target_phrase_matcher, gpt_translation_doc)
    
    # Index matches by lemma
    source_lemma_matches = index_matches_by_lemma(segment_doc, source_matches)
    target_lemma_matches = index_matches_by_lemma(gpt_translation_doc, target_matches)

    compliance = verify_termbase_compliance(source_lemma_matches, target_lemma_matches, lemmatized_termbase)

    if compliance:
        print("No term missalignment.")
    translated_segment = (segment, gpt_translation + " <!-- GPT translation -->")

    return translated_segment, gpt_translation

def translate_segment(segment, tm_dict, gpt_translation_dict, language, gpt_model, client, source_model, target_model, source_phrase_matcher, target_phrase_matcher, lemmatized_termbase,  previous_segment=''):
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
        translated_segment, gpt_translation = translate_with_gpt(client, segment, language, gpt_model, source_model, target_model, source_phrase_matcher, target_phrase_matcher, lemmatized_termbase,  previous_segment)
        gpt_translation_dict[segment] = gpt_translation
        return translated_segment


def process_front_matter(front_matter_segments, tm_dict, gpt_translation_dict, language, gpt_model, client, source_model, target_model, source_phrase_matcher, target_phrase_matcher, lemmatized_termbase):
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
                translated_text = translate_segment(translatable_text, tm_dict, gpt_translation_dict,language, gpt_model, client, source_model, target_model, source_phrase_matcher, target_phrase_matcher, lemmatized_termbase)
                processed_segment_pair = (segment[0], frontmatter_variable + translated_text[1])
                break
            else:
                # No translation needed; reproduce the segment unchanged
                processed_segment_pair = segment
        processed_front_matter.append(processed_segment_pair)
    processed_front_matter.insert(-1, gpt_translation_marker)

    return processed_front_matter

def translate_article(client, language, source_text, tm_dict, gpt_model, source_model, target_model, source_phrase_matcher, target_phrase_matcher, lemmatized_termbase):
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
            translated_front_matter = process_front_matter(front_matter_segments, tm_dict, gpt_translation_dict, language, gpt_model, client, source_model, target_model, source_phrase_matcher, target_phrase_matcher, lemmatized_termbase)
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
            segment, translated_segment = translate_segment(segment, tm_dict, gpt_translation_dict, language, gpt_model, client, source_model, target_model, source_phrase_matcher, target_phrase_matcher, lemmatized_termbase,  previous_segment)
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
    if not config.SOURCE_LANGUAGE_SPACY_MODEL:
        raise EnvironmentError("Source language spaCy model not defined in the config file.")
    else: source_lang_spacy_model = config.SOURCE_LANGUAGE_SPACY_MODEL

    # Initialize OpenAI client
    client = initialize_open_ai_client()

    # Parse command-line arguments
    lang, source = parse_arguments()

    # Initialize language models

    for key, value in config.LANGUAGE_MODELS[lang].items():
        if not value:
            raise EnvironmentError(f"{key} not defined for the target language in the language models in the config file.")
        else: language, gpt_model, tm_path, target_spacy_model = initialize_language_model(lang)

    # Initialize translation memory dictionary
    tm_dict = initialize_translation_memory(lang, tm_path)

    # Initialize termbase
    termbase = initialize_termbase(termbase_directory, lang)
    source_terms = [term_tuple[1] for term_tuple in termbase]
    target_terms = [term_tuple[2] for term_tuple in termbase]
    
    # Split termbase
    # source_terms, target_terms = split_termbase(termbase)

    # Initialize spaCy models
    source_model, target_model = initialize_spacy_models(target_spacy_model, source_lang_spacy_model)
    
    # Lemmatize termbase
    lemmatized_termbase = lemmatize_termbase(source_model, target_model, termbase, lang)

    # Setup source PhraseMatcher
    source_phrase_matcher = setup_phrase_matcher(source_model, source_terms)

    # Setup target PhraseMatcher
    target_phrase_matcher = setup_phrase_matcher(target_model, target_terms)

    # Load source file segments
    source_text = load_source_file_segments(source)

    # Perform the translation
    translated_segments = translate_article(client, language, source_text, tm_dict, gpt_model, source_model, target_model, source_phrase_matcher, target_phrase_matcher, lemmatized_termbase)

    # Create list with translated text
    translated_text = join_translated_text(translated_segments)

    # Save file in repository
    write_translated_file(language, source, translated_text)

    # Output the result and time taken
    elapsed_time = round((time.time() - start_time), 2)
    print(f"Time taken: {elapsed_time} seconds")

if __name__ == "__main__":
    main()
