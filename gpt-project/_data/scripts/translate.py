import os
import argparse
import time
import csv
import Levenshtein as lev
from openai import OpenAI

# Use this script to translate whole articles from English into German, Spanish, French, Italian, or Dutch with ChatGPT.
# The script takes two arguments, --lang and--source, respectively the target language and the source file to be translated.

def initialize_open_ai_client():
    # Initialize OpenAI client using API key
    # Returns the client object if the key is found, otherwise raises error
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not found.")
    return OpenAI(api_key=api_key)

def parse_arguments():
    # Parse command-line arguments for language and source file.
    # Returns a tuple of (language, source file path).
    parser = argparse.ArgumentParser(description="Script to translate texts using TM and ChatGPT")
    parser.add_argument("--lang", required=True, help="Target language for translation")
    parser.add_argument("--source", required=True, help="Source file for translation")
    args = parser.parse_args()
    return args.lang, args.source

def translate_segment(client, segment, language, gpt_model):
    # Translates a segment using ChatGPT
    # Parameters:
    #   client: OpenAI client object
    #   segment: Segment to be translated
    #   language_code: Target language code
    #   gpt_model: ChatGPT model
    # Returns the translated segment
    response = client.chat.completions.create(
    model=gpt_model,
    messages=[
        {"role": "system", "content": f"Given a sentence in Markdown format, translate the sentence to {language} keeping the style, tone, formatting, and terminology consistent and provide strictly just the translation."},
        {"role": "user", "content": segment}
      ]
    )
    print(segment + " This is the segment")
    translated_segment = response.choices[0].message.content
    return translated_segment

def translate_article(client, language_code, source_file):
    # Translate the content of the source file using the specified language model.
    # Parameters:
    #   client: OpenAI client object
    #   language_code: Target language code
    #   source_file: Path to the source file
    # Returns the translated text.

    # Define language models
    language_models = {
        # "de": {"language": "German", "model": , "tm": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-de.csv"},
        "es": {"language": "Spanish", "model": "ft:gpt-3.5-turbo-1106:personal::8SkFElMK", "tm": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-fr.csv"},
        # "fr": {"language": "French", "model": "", "tm": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-fr.csv"},
        # "it": {"language": "Italian", "model": "", "tm": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-it.csv"},
        "nl": {"language": "Dutch", "model": "ft:gpt-3.5-turbo-1106:personal::8f4GFKBA", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-nl.csv"}
    }

    # Initialize language model
    if language_code in language_models:
        language = language_models[language_code]["language"]
        gpt_model = language_models[language_code]["model"]
        tm_path = language_models[language_code]["tm_path"]
    else:
        print("""
              You entered an invalid language code. Use one of the following:
              "de" for German
              "es" for Spanish
              "fr" for French
              "it" for Italian
              "nl" for Dutch
        """)
    
    # Check if source path exists
    if not os.path.exists(source_file):
        print("Source file not found. Check the source file path entered.")
    
    # Extract source file directory
    source_directory = os.path.dirname(source_file)

    # Read source file
    with open(source_file, 'r') as file:
        source_text = file.read()
    
    # Split text into segmetns
    split_source_text = source_text.splitlines()

    # Initialize empty list to store translated segments from the article
    translated_segments = []

    # Initialize empty dictionary to store GPT translations for repetitions
    gpt_translation_dict = {}

    # Initialize tm dictionary to use TM content in the translation
    tm_dict = {}

    # Read the TM and extract the 'en' and target language column
    with open(tm_path, 'read', encoding='utf-8') as tm:
        reader = csv.DictReader(tm)
        for row in reader:
            tm_dict[row['en']] = row[language_code]

    # Flag to check frontmatter
    in_frontmatter = False

    # Pre-calculate lenghts of TM segments
    tm_segments_lengths = {tm_segment:len(tm_segment) for tm_segment in tm_dict}

    # Iterate over each segment of the source text
    for segment in split_source_text:

        # Check if segment is the start or end of the frontmatter
        if segment == '---':
            translated_segments.append((segment, segment))
            # Change flag after finding start or end of the frontmatter
            in_frontmatter = not in_frontmatter
            continue

        # Reproduce frontmatter in the target file - THIS PART NEEDS TO BE CHANGED FOR FRONTMATTER TRANSLATION
        elif in_frontmatter:
            translated_segments.append((segment, segment))
            continue

        # Keep commented out segment in English
        elif segment.startswith(">!--"):
            translated_segments.append((segment, segment))
            continue

        # Check for existing translation in TM
        if segment in tm_dict():
            translated_segments.append((segment, tm_dict[segment] + " <!-- TM 100 -->"))
            continue
        
        # Check for for existing GPT translation
        elif segment in gpt_translation_dict:
            translated_segments.append((segment, gpt_translation_dict[segment] + " <!-- Repetition of GPT translation"))
            continue
        
        # Reproduce empty lines to keep article formatting
        elif segment == '':
            translated_segments.append((segment, segment))
            continue
        
        # Check for fuzzy matches
        else:
            # Define upper and lower normalized edit distance
            lower_threshold = 0.05
            upper_threshold = 0.4
            # Initialize closest segment match and max normalized edit distance
            closest_segment, normalized_min_distance = None, 1
            # Calculate source segment length
            segment_length = len(segment)

            # Iterate over TM segment lenghts
            for tm_segment, tm_segment_length in tm_segments_lengths.items():
                # Avoid calculation if length difference is over the upper threshold
                if abs(segment_length - tm_segment_length) / max(segment_length, tm_segment_length) > upper_threshold
                    continue

                # Calculate Levenshtein distance and normalize it
                distance = lev.distance(segment, tm_segment)
                normalized_distance = distance / max(segment_length, tm_segment_length)

                # Update closes match if a closer one is found
                if normalized_distance < normalized_min_distance:
                    closest_segment, normalized_min_distance = tm_segment, normalized_distance

                # Early exit if a sufficiently close match is found
                if normalized_distance < lower_threshold:
                    break

            # If the smallest distance is below the threshold, use content of TM
            if normalized_min_distance < upper_threshold:
                fuzzy_match_score = (1 - normalized_min_distance)
                translated_segments.append((segment, tm_dict[closest_segment] + f" <!-- TM {fuzzy_match_score} -->"))
            # If the smallest distance is above the lower threshold, translate using ChatGPT
            else:
                translated_segment = translate_segment(client, segment, language, gpt_model)
                gpt_translation_dict[segment] = translated_segment
                translated_segments.append((segment, translated_segment + " <!-- GPT translation -->"))
    
    # Return list of tuples with source and target segments
    return translated_segments

def extract_translated_frontmatter(translated_segments):
    # Flag to track beginning and end of frontmatter
    marker_found = False
    # Iterate over the segments of the translation
    for _, target_segment in translated_segments:
        # If the segment is the frontmatter delimiter
        if target_segment == "---":
            # Reproduces delimiter '---'
            yield target_segment
            # Check if the flag is true when checking the delimiter
            if marker_found:
                return # End function when stop condition is met
            else:
                marker_found = True
                continue # Skip to next segment
        # Reproduce frontmatter content
        elif marker_found:
            yield target_segment

def extract_translated_text(translated_segments):
    # Initialize marker count
    marker_count = 0
    for _, target_segments in translated_segments:
        # Check for frontmatter delimiter
        if target_segments == "---":
            marker_count += 1
            # Skip segments until the second frontmatter delimiter is found
            if marker_count < 2:
                continue
            # Start yielding segments after second
    







# Create list with translated content
translated_text = list(extract_translated_text(translated_segments))

# Join translated text in a string
joint_translated_text = "\n".join(translated_text)

# Join translated frontmatter and article

joint_translated_article = joint_translated_frontmatter + "\n" + joint_translated_text
