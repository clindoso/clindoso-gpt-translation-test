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
    """
    Parse command-line arguments for language and source file.
    Returns a tuple of (language, source file path).
    """
    parser = argparse.ArgumentParser(description="Script to translate texts using TM and ChatGPT")
    parser.add_argument("--lang", required=True, help="Target language for translation")
    parser.add_argument("--source", required=True, help="Source file for translation")
    args = parser.parse_args()
    return args.lang, args.source

def read_and_parse_source(source):
    """
    Reads and parses the source file.
    
    Parameters:
        source_path (str): Path to the source file.
    
    Returns:
        list: A list of lines from the source file, or None if file not found.
    """
    # Check if source path exists
    if not os.path.exists(source):
        print("Source file not found. Check the source file path entered.")

    # Read source file
    with open(source, 'r') as file:
        file_content = file.read()
    
    # Split text into segmetns
    source_text = file_content.splitlines()

    return source_text

def initialize_language_model(lang):
    """
    Initializes language model.
    Returns language name, gpt_model, tm_path
    """
    # Define language model dictionary
    language_models = {
        # "de": {"language": "German", "gpt-model": , "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-de.csv"},
        "es": {"language": "Spanish", "gpt-model": "ft:gpt-3.5-turbo-1106:personal::8SkFElMK", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-fr.csv"},
        # "fr": {"language": "French", "gpt-model": "", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-fr.csv"},
        # "it": {"language": "Italian", "gpt-model": "", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-it.csv"},
        "nl": {"language": "Dutch", "gpt-model": "ft:gpt-3.5-turbo-1106:personal::8f4GFKBA", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-nl.csv"}
    }

    # Initialize language model
    if lang in language_models:
        language = language_models[lang]["language"]
        gpt_model = language_models[lang]["gpt-model"]
        tm_path = language_models[lang]["tm_path"]
    else:
        print("""
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


def translate_with_gpt(client, segment, language, gpt_model):
    """
    Translates a segment using ChatGPT
    Parameters:
      client: OpenAI client object
      segment: Segment to be translated
      lang: Target language code
      gpt_model: ChatGPT model
    Returns the translated segment
    """
    response = client.chat.completions.create(
    model=gpt_model,
    messages=[
        {"role": "system", "content": f"Given a sentence in Markdown format, translate the sentence to {language} keeping the style, tone, formatting, and terminology consistent and provide strictly just the translation."},
        {"role": "user", "content": segment}
      ]
    )
    
    translated_segment = response.choices[0].message.content

    return translated_segment

def handle_frontmatter(segment, in_frontmatter):
    """
    Handles the frontmatter segment of the text.

    Parameters:
        segment (str): The current text segment.
        in_frontmatter (bool): Flag indicating if we are currently processing frontmatter.

    Returns:
        tuple: A tuple containing the processed segment and the updated frontmatter flag.
    """
    if segment == '---':
        return (segment, segment), not in_frontmatter
    return None, in_frontmatter

def handle_commented_out_segment(segment):
    """
    Handles segments that are commented out.

    Parameters:
        segment (str): The current text segment.

    Returns:
        tuple or None: Processed segment if it's a comment, else None.
    """
    if segment.startswith("<!--"):
        return (segment, segment)
    return None

def handle_empty_line(segment):
    """
    Handles empty line segments for maintaining formatting.

    Parameters:
        segment (str): The current text segment.

    Returns:
        tuple or None: Processed segment if it's an empty line, else None.
    """
    if segment == '':
        return (segment, segment)
    return None

def translate_article(client, language, source_text, tm_dict, gpt_model):
    """
    Translate the content of the source file using the specified language model.
    Parameters:
      client: OpenAI client object
      lang: Target language code
      source: Path to the source file
    Returns the translated text.
    """

    # Initialize empty list to store translated segments from the article
    translated_segments = []

    # Initialize empty dictionary to store GPT translations for repetitions
    gpt_translation_dict = {}

    # Flag to check frontmatter
    in_frontmatter = False

    # Pre-calculate lenghts of TM segments
    tm_segments_lengths = {tm_segment:len(tm_segment) for tm_segment in tm_dict}

    # Iterate over each segment of the source text
    for segment in source_text:

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
        elif segment.startswith("<!--"):
            translated_segments.append((segment, segment))
            continue

        # Check for existing translation in TM
        if segment in tm_dict:
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
                if abs(segment_length - tm_segment_length) / max(segment_length, tm_segment_length) > upper_threshold:
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
                translated_segments.append((segment, tm_dict[closest_segment] + f" <!-- TM {fuzzy_match_score*100:.0f} -->"))
            # If the smallest distance is above the lower threshold, translate using ChatGPT
            else:
                translated_segment = translate_with_gpt(client, segment, language, gpt_model)
                gpt_translation_dict[segment] = translated_segment
                translated_segments.append((segment, translated_segment + " <!-- GPT translation -->"))
    
    # Return list of tuples with source and target segments
    return translated_segments

def extract_translated_frontmatter(translated_segments):
    """
    Extracts the target frontmatter the translated segments list
    Returns frontmatter in one string
    """
    # Flag to track beginning and end of frontmatter
    marker_found = False
    # Initialize list to store extracted segments
    extracted_segments = []
    # Iterate over the segments of the translation
    for _, target_segment in translated_segments:
        # Check if the segment is the frontmatter delimiter
        if target_segment == "---":
            # Reproduces delimiter '---'
            extracted_segments.append(target_segment)
            # Check if the flag is true when checking the delimiter
            if marker_found:
                joint_translated_frontmatter = "\n".join(extracted_segments)
                return joint_translated_frontmatter # End function when stop condition is met
            # Skip to next segment
            else:
                marker_found = True
                continue
        # Reproduce frontmatter content
        elif marker_found:
            extracted_segments.append(target_segment)
        # Break out of loop if the end of the list is reached
        if target_segment == translated_segments[-1][1]:
            break
    
    # Join frontmatter in one string
    joint_translated_frontmatter = "\n".join(extracted_segments)

    return joint_translated_frontmatter

def extract_translated_text(translated_segments):
    """
    Extracts the target text the translated segments list
    Returns text in one string
    """
    # Initialize marker count
    marker_count = 0
    # Initialize list to store extracted segments
    extracted_segments = []
    for _, target_segment in translated_segments:
        # Check for frontmatter delimiter
        if target_segment == "---":
            marker_count += 1
            # Skip segments until the second frontmatter delimiter is found
            if marker_count < 2:
                continue

        # Avoid reproducing frontmatter delimiter twice
        if target_segment == "---" and marker_count == 2:
            continue
        # Append segments after second '---'
        elif marker_count == 2:
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
    
    # Read and parse source file
    source_text = read_and_parse_source(source)

    # Perform the translation
    translated_segments = translate_article(client, language, source_text, tm_dict, gpt_model)

    # Create list with translated frontmatter
    translated_frontmatter = extract_translated_frontmatter(translated_segments)

    # Create list with translated text
    translated_text = extract_translated_text(translated_segments)

    # Join translated matter and article
    translated_article = translated_frontmatter + "\n" + translated_text

    # Save file in repository
    write_translated_file(language, source, translated_article)

    # Output the result and time taken
    elapsed_time = round((time.time() - start_time), 2)
    print(f"Time taken: {elapsed_time} seconds")

if __name__ == "__main__":
    main()
