import csv
import Levenshtein as lev
import config

# This file contains functions peripheral to translation, e.g. initalizing TM and dicts for saving translations.

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
    Initializes the translation memory for the target language.

    This function reads a translation memory file (CSV) and extracts
    the English and target language translations into a dictionary.

    Parameters:
        lang (str): The target language code (e.g., 'fr' for French).
        tm_path (str): The file path to the translation memory (CSV format).

    Returns:
        dict: A dictionary where the keys are English phrases and the values
              are the corresponding translations in the target language.

    Raises:
        FileNotFoundError: If the specified translation memory file does not exist.
        KeyError: If the specified language code does not exist in the translation memory file.
    """
    # Initialize tm dictionary to use TM content in the translation
    tm_dict = {}
    # Read the TM and extract the 'en' and target language column
    with open(tm_path, 'r', encoding='utf-8') as tm:
        reader = csv.DictReader(tm)
        for row in reader:
            tm_dict[row['en']] = row[lang]
            for key, value in tm_dict.items():
                if key == None:
                    print("Value for None key: {value}")
                if value == None:
                    print("Key for None value: {key}")
    
    return tm_dict

def check_translation_memory(segment, tm_dict):
    """
    Checks if the given segment has a translation in the translation memory (TM).

    This function looks up the provided text segment in the translation memory
    dictionary and returns the corresponding translation and an annotated version
    indicating a 100% match.

    Parameters:
        segment (str): The current text segment to check.
        tm_dict (dict): The translation memory dictionary where keys are source
                        segments and values are translated segments.

    Returns:
        tuple: A tuple containing the annotated translation segment and the plain
            translation if available, otherwise (None, None).
    """
    if segment in tm_dict:
        tm_translation = tm_dict[segment]
        tm_segment = tm_translation + " <!-- TM 100 -->"
        return tm_segment, tm_translation
    else:
        return None, None
    
def check_translations(segment, translation_dict):
    """
    Checks for existing translations of the given segment in the GPT translation dictionary.

    This function looks up the provided text segment in the GPT translation dictionary
    and returns the corresponding translation and an annotated version indicating
    auto-propagation by GPT.

    Parameters:
        segment (str): The current text segment to check.
        translation_dict (dict): Dictionary containing GPT translations where keys
                                are source segments and values are translated segments.

    Returns:
        tuple: A tuple containing the annotated translation segment and the plain
            translation if available, otherwise (None, None).
    """

    if segment in translation_dict:
        gpt_auto_propagation = translation_dict[segment]
        gpt_segment = translation_dict[segment] + " <!-- GPT auto-propagation -->"
        return gpt_segment, gpt_auto_propagation
    return None, None

def handle_fuzzy_matches(segment, tm_dict, tm_segments_lengths):
    """
    Handles fuzzy matches for the given segment using Levenshtein distance.

    This function attempts to find the closest matching segment in the translation memory (TM)
    based on the Levenshtein distance and returns the corresponding translation if a suitable
    fuzzy match is found.

    Parameters:
        segment (str): The current text segment to match.
        tm_dict (dict): The translation memory dictionary where keys are source segments and
                        values are translated segments.
        tm_segments_lengths (dict): Dictionary where keys are TM segments and values are
                                    their lengths.

    Returns:
        str or None: The best fuzzy match from the TM with an annotated fuzzy match score
                    if found within the threshold, otherwise None.
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
            return tm_dict[closest_segment] + f" <!-- TM {fuzzy_match_score*100:.0f} -->"
    
    # If there is no segment with an edit below the upper threshold, return None
    return None
