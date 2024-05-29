import config
import argparse
import os
import csv
from config import LANGUAGE_MODELS

# Use this script to create a CSV file as a TM with English as source language
# This script takes one argument, --lang, the target language of the TM

def parse_arguments():
    """
    Parse command-line arguments for language and source file.
    Returns a tuple of (language, source file path).
    """
    parser = argparse.ArgumentParser(description="Script to translate texts using TM and ChatGPT")
    parser.add_argument("--lang", required=True, help="Target language for translation")
    args = parser.parse_args()
    return args.lang

def read_and_split_file(file_path):
    """
    Reads and parses file by code line.
    
    Parameters:
        file_path (str): Path to source file.
        
    Returns:
        list: A list of segments from the source file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            segments = file.readlines()

        # Flag to check if we are inside the frontmatter
        in_frontmatter = False
        segmented_article = []

        # Iterate over the article segments
        for segment in segments:
            stripped_segment = segment.rstrip()

            # Check if the segment is the start or end of the frontmatter
            if stripped_segment == '---':
                in_frontmatter = not in_frontmatter
                continue

            # Exclude segments within the frontmatter or comments
            if in_frontmatter and segment.startswith('title: '):
                stripped_segment = stripped_segment[len('title: '):]
                segmented_article.append(stripped_segment)
            elif in_frontmatter and segment.startswith('description: '):
                stripped_segment = stripped_segment[len('description: '):]
                segmented_article.append(stripped_segment)
            if not in_frontmatter and not (stripped_segment.startswith('<!--') and stripped_segment.endswith('-->')):
                segmented_article.append(stripped_segment)

        # Remove empty strings from the segmented_article list before returning
        return [segment for segment in segmented_article if segment]

    except Exception as e:
        raise Exception(f"Error reading {file_path}: {e}")

def initialize_language_model(lang):
    """
    Initializes language model.
    Returns tm_path
    """
    # Define language model dictionary
    language_models = LANGUAGE_MODELS
    # Initialize language model
    if lang in language_models:
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

    return tm_path

def initialize_tm_file(tm_path, lang):
    """
    Initializes a translation memory (TM) file by clearing its content, or creating it if it doesn't exist.
    The function determines the TM directory based on the provided TM path and ensures the directory exists.

    Parameters:
        tm_path (str): The base path for TM files, used to determine the directory.
        lang (str): The target language code, used to create the specific TM file name.

    The function constructs the TM file name using 'en-' as a prefix followed by the language code and '.csv' extension.
    It then checks if the TM directory exists, creates it if necessary, and clears the content of the TM file.
    """
    # Define tm_directory
    tm_directory = os.path.dirname(tm_path)
    # Define tm file name
    tm_filename = "en-" + lang + ".csv"

    # Check if output directory exists
    os.makedirs(tm_directory, exist_ok=True)
    tm_filepath = os.path.join(tm_directory, tm_filename)

    def clear_csv_content(file_path):
        with open(file_path, 'w') as file:
            pass

    # Delete existing TM
    clear_csv_content(tm_filepath)

    return tm_filepath

# Function to export to CSV
def write_to_csv(file1_segments, file2_segments, lang, source_filename, tm_filepath):
    """
    Appends aligned or marks unaligned text pairs to/from two files into a CSV file.

    Parameters:
        file1_segments (list of str): Segments from the first file.
        file2_segments (list of str): Segments from the second file.
        lang (str): Target language code.
        source_filename (str): Name of the source file.
        tm_filepath (str): Path to the translation memory CSV file.

    Returns:
        tuple: A tuple containing a list of not aligned articles, count of aligned articles, and count of not aligned articles.
    """
    aligned = 0
    not_aligned = 0
    not_aligned_article = []

    with open(tm_filepath, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        if csvfile.tell() == 0:
            writer.writerow(['en', lang, 'article'])

        if len(file1_segments) == len(file2_segments):
            aligned = 1
            for line1, line2 in zip(file1_segments, file2_segments):
                writer.writerow([line1, line2, source_filename])
        else:
            not_aligned = 1
            not_aligned_article.append(source_filename)
        
    return not_aligned_article, aligned, not_aligned
        

# Extract file contents
def extract_file_contents(docs_directory, lang, tm_filepath, file_extension=".md"):
    not_aligned_articles = []  # Initialize list for not aligned articles
    aligned_qtt = 0  # Initialize counter for aligned articles
    not_aligned_qtt = 0  # Initialize counter for not aligned articles
    for root, _, files in os.walk(docs_directory):
        for file in files:
            if file.endswith(file_extension):
                file_path_source = os.path.join(root, file)
                file_path_target = file_path_source.replace("_en", "_" + lang)
                if os.path.exists(file_path_target):
                    source_file_content = read_and_split_file(file_path_source)
                    target_file_content = read_and_split_file(file_path_target)
                    _not_aligned_articles, _aligned_qtt, _not_aligned_qtt = write_to_csv(source_file_content, target_file_content, lang, file, tm_filepath)

                    # Update the results with data from the current file pair
                    not_aligned_articles.extend(_not_aligned_articles)
                    aligned_qtt += _aligned_qtt
                    not_aligned_qtt += _not_aligned_qtt
                else:
                    print(f"{file} has no correspondent article in {lang.upper()}")

    return not_aligned_articles, aligned_qtt, not_aligned_qtt


def main():
    # Initialize docs directory
    if not config.DOCS_DIRECTORY:
        raise EnvironmentError("Source documents directory not defined in the config file.")
    else: docs_directory = config.DOCS_DIRECTORY

    # Initializes target lang
    lang = parse_arguments()

    # Initialize language models
    tm_path = initialize_language_model(lang)

    # Initialize TM file
    tm_filepath = initialize_tm_file(tm_path, lang)

    # Extract segments from articles
    not_aligned_articles, aligned_qtt, not_aligned_qtt = extract_file_contents(docs_directory, lang, tm_filepath)

    print(f"Aligned articles: {aligned_qtt}")
    print(f"Not aligned articles: {not_aligned_qtt}")
    print("The following articles might not be up to date:")
    for article in not_aligned_articles:
        print(article)

if __name__ == "__main__":
    main()
