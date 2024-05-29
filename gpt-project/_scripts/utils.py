# This file contains functions to process files and strings

import os

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
    joint_translated_text = "\n".join(extracted_segments) + "\n"

    return joint_translated_text


def write_translated_file(language, source, translated_article):
    """
    Saves translated article with the same name of the source file in a subdirectory of the source file
    Parameters:
      language (str): Language for translation
      source (str): Source file path
      translated_article (str): Article in target language
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
