import os
import csv
import argparse
import re

# Use this script to create a CSV file as a TM with English as source language
# This script takes one argument, --lang, the target language of the TM

# Define source directory
source_directory = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/_en/"

# Create argument parser
argparser = argparse.ArgumentParser()

# Define argument
argparser.add_argument("--lang", required=True, help="Specify the target language for the translation memory")

# Parse arguments
args = argparser.parse_args()

# Read and return file content in a list
def read_and_split_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Flag to check if we are inside the frontmatter
        in_frontmatter = False
        result = []

        for line in lines:
            stripped_line = line.strip()

            # Check if the line is the start or end of the frontmatter
            if stripped_line == '---':
                in_frontmatter = not in_frontmatter
                continue

            # Exclude lines within the frontmatter or lines that are HTML comments
            if not in_frontmatter and not (stripped_line.startswith('<!--') and stripped_line.endswith('-->')):
                result.append(stripped_line)

        # Remove empty strings from the result list before returning
        return [line for line in result if line]

    except Exception as e:
        raise Exception(f"Error reading {file_path}: {e}")

# Define output directory and file name
output_directory = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/"
output_filename = "en-" + args.lang + ".csv"

# Check if output directory exists
os.makedirs(output_directory, exist_ok=True)
output_filepath = os.path.join(output_directory, output_filename)

def clear_csv_content(file_path):
    with open(file_path, 'w') as file:
        pass

# Delete existing TM
clear_csv_content(output_filepath)

def sentence_splitter(file1_lines, file2_lines):
    """
    Split strings in two lists of lines into sentences by '. ', ignoring specified patterns.

    Args:
    file1_lines (list of str): Lines from the first file.
    file2_lines (list of str): Lines from the second file.

    Returns:
    tuple of list of list of str: Two lists containing the split sentences from each file.
    """
    # Patterns to ignore, with their placeholders
    patterns = {
        "z.&nbsp;B.": "{PLACEHOLDER_ZB}",
        "d.&nbsp;h.": "{PLACEHOLDER_DH}",
        "i.e.": "{PLACEHOLDER_IE}",
        "e.g.": "{PLACEHOLDER_EG}",
        "u.U.": "{PLACEHOLDER_UU}",
        "u.a.": "{PLACEHOLDER_UA}",
        "p.&nbsp;ej.": "{PLACEHOLDER_PEJ}"
    }

    etc_pattern = re.compile(r'etc\.\s[a-z()]')

    def split_line(line):
        # Replace 'etc. ' followed by a capital letter with a placeholder
        line = etc_pattern.sub("{PLACEHOLDER_ETC}", line)

        # Replace other patterns
        for pattern, placeholder in patterns.items():
            line = line.replace(pattern, placeholder)

        # Split sentences by period
        sentences = line.split('. ')

        # Restore 'etc. '
        line = etc_pattern.sub("etc. ", line)

        # Restore other patterns
        for i, sentence in enumerate(sentences):
            for pattern, placeholder in patterns.items():
                sentences[i] = sentence.replace(placeholder, pattern)
        return sentences
    
    # Split files
    split_file1 = [split_line(line) for line in file1_lines]
    split_file2 = [split_line(line) for line in file2_lines]
    
    return split_file1, split_file2

# List for possibly not aligned articles
not_aligned_articles = []
aligned_qtt = 0
not_aligned_qtt = 0

# Export to CSV
def write_to_csv(file1_lines, file2_lines, source_filename, output_filepath):
    global not_aligned_articles
    global aligned_qtt
    global not_aligned_qtt

    with open(output_filepath, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        if csvfile.tell() == 0:
            writer.writerow(['en', args.lang, 'file'])

        if len(file1_lines) == len(file2_lines):
            aligned_qtt += 1
            for line1, line2 in zip(file1_lines, file2_lines):
                writer.writerow([line1, line2, source_filename])
        else:
            not_aligned_qtt += 1
            not_aligned_articles.append(source_filename)
        

# Extract file contents
def extract_file_contents(directory, file_extension=".md"):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                file_path_en = os.path.join(root, file)
                file_path_tl = file_path_en.replace("_en", "_" + args.lang)
                if os.path.exists(file_path_tl):
                    file_content_en = read_and_split_file(file_path_en)
                    file_content_tl = read_and_split_file(file_path_tl)
                    write_to_csv(file_content_en, file_content_tl, file, output_filepath)

extract_file_contents(source_directory)

print(f"Aligned articles: {aligned_qtt}")
print(f"Not aligned articles: {not_aligned_qtt}")
print("The following articles might not be aligned:")
for article in not_aligned_articles:
    print(article)
