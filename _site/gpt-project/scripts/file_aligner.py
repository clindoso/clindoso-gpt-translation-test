import os
import csv
import argparse
import re

# Use this script to create a CSV file as a TM with English as source language
# This script takes two arguments, --lang and --file, respectively the target language of the TM and the file path

# Create argument parser
argparser = argparse.ArgumentParser()

# Define argument
argparser.add_argument("--lang", required=True, help="Specify the target language for the translation memory")
argparser.add_argument("--file", required=True, help="Specify the file path of the translated article")

# Parse arguments
args = argparser.parse_args()
# Extract file name
split_file_path = [seg for seg in args.file.split('/') if seg]
file_name = split_file_path[-1]

# Read and return file content in a list
def read_and_split_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Flag to check if we are inside the frontmatter
        in_frontmatter = False
        result = []

        # Iterate over the article lines
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
        stripped_text = [line for line in result if line]
        # Define the complex regex pattern with capturing parentheses to keep the separators
        pattern = (
            r'(\.)'  # Literal period
            r'\s\|\s'  # Space, pipe, space
            r'^\|\s'  # Pipe and space at the beginning of the string
            r'^\d\d?\.'  # Matches start of string, one or two digits and a period
        )
        split_text = [segment for segment in re.split(pattern, stripped_text) if segment]

        return split_text

    except Exception as e:
        raise Exception(f"Error reading {file_path}: {e}")

# Define output directory and file name
output_directory = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/"
output_filename = f"en-{args.lang}-{file_name}.csv"

# Check if output directory exists
os.makedirs(output_directory, exist_ok=True)
output_filepath = os.path.join(output_directory, output_filename)

def clear_csv_content(file_path):
    with open(file_path, 'w') as file:
        pass

# Delete existing TM
clear_csv_content(output_filepath)

# Function to replace patterns
def replace_patterns(etc_pattern, etc_placeholder, patterns, line):
    # Replace specifed patterns in line
    line = etc_pattern.sub(etc_placeholder, line)
    for pattern, placeholder in patterns.items():
        line = line.replace(pattern, placeholder)
    return line

# Function to restore patterns
def restore_patterns(patterns, etc_placeholder, etc_string, line):
    # Restore original patterns
    for pattern, placeholder in patterns.items():
        line = line.replace(placeholder, pattern)
    line = re.sub(etc_placeholder, etc_string, line)
    return line

# Define sentence splitter

def sentence_splitter(file1_lines, file2_lines):
    # Patterns to ignore, with their placeholders
    pattern_zb = re.compile(r'z\.&nbsp;B\.')
    pattern_dh = re.compile(r'd\.&nbsp;h\.')
    pattern_ie = re.compile(r'i\.e\.')
    pattern_eg = re.compile(r'e\.g\.')
    pattern_uu = re.compile(r'u\.U\.')
    pattern_ua = re.compile(r'u\.a\.')
    pattern_pej = re.compile(r'p\.&nbsp;ej\.')
    pattern_etc = re.compile(r'etc.\s?$')
    patterns = {
        pattern_zb: "{PLACEHOLDER_ZB}",
        pattern_dh: "{PLACEHOLDER_DH}",
        pattern_ie: "{PLACEHOLDER_IE}",
        pattern_eg: "{PLACEHOLDER_EG}",
        pattern_uu: "{PLACEHOLDER_UU}",
        pattern_ua: "{PLACEHOLDER_UA}",
        pattern_pej: "{PLACEHOLDER_PEJ}",
        pattern_etc: "{PLACEHOLDER_ETC}"
    }

    def split_line(file1_lines, file2_lines):
        period_pattern = r'(\.\s)'
        placeholders = {
            "{PLACEHOLDER_ZB}": "z.&nbsp;B.",
            "{PLACEHOLDER_DH}": "d.&nbsp;h.",
            "{PLACEHOLDER_IE}": "i.e.",
            "{PLACEHOLDER_EG}": "e.g.",
            "{PLACEHOLDER_UU}": "u.U.",
            "{PLACEHOLDER_UA}": "u.a.",
            "{PLACEHOLDER_PEJ}": "p.&nbsp;ej.",
            "{PLACEHOLDER_ETC}": "etc."
        }

        # Define new lists for processed lines
        processed_file1_lines = []
        processed_file2_lines = []
        
        for line1, line2 in zip(file1_lines, file2_lines):

            processed_file1_lines.append(line1)
            processed_file2_lines.append(line2)

            # Split and equalize if necessary
            if line1.count('. ') != line2.count('. ') and line1.count('. ') > 1 and line2.count('. ') > 1:
                temp_file1_lines = line1.split(period_pattern)
                temp_file2_lines = line2.split(period_pattern)
            
            # Equalize strings

            else:
                temp_file1_lines = line1.split('. ')
                temp_file2_lines = line2.split('. ')

                for i in range(len(temp_file1_lines)):    
                    if ends_with_regex(temp_file1_lines[i]):
                        temp_file1_lines += '.'
                for i in range(len(temp_file2_lines)):
                    if ends_with_regex(temp_file2_lines[i]):
                        temp_file2_lines[i] += '.'
            

        # Restore placeholders to original patterns
        restored_file1_lines = [restore_patterns(patterns, etc_placeholder, etc_string, line) for line in processed_file1_lines]
        restored_file2_lines = [restore_patterns(patterns, etc_placeholder, etc_string, line) for line in processed_file2_lines]
        return restored_file1_lines, restored_file2_lines

    
    # Split files
    split_file1, split_file2 = split_line(file1_lines, file2_lines)
    
    return split_file1, split_file2

# List for possibly not aligned articles
not_aligned_articles = []
aligned_qtt = 0
not_aligned_qtt = 0

# Function to export to CSV
def write_to_csv(file1_lines, file2_lines, source_filename, output_filepath):
    global not_aligned_articles
    global aligned_qtt
    global not_aligned_qtt

    with open(output_filepath, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        if csvfile.tell() == 0:
            writer.writerow(['en', args.lang, 'file'])

        if len(file1_lines) == len(file2_lines):
            file1_lines, file2_lines = sentence_splitter(file1_lines, file2_lines)
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
                file_path_source = os.path.join(root, file)
                file_path_target = file_path_source.replace("_en", "_" + args.lang)
                if os.path.exists(file_path_target):
                    file_content_en = read_and_split_file(file_path_source)
                    file_content_tl = read_and_split_file(file_path_target)
                    write_to_csv(file_content_en, file_content_tl, file, output_filepath)

extract_file_contents(source_directory)

print(f"Aligned articles: {aligned_qtt}")
print(f"Not aligned articles: {not_aligned_qtt}")
print("The following articles might not be up to date:")
for article in not_aligned_articles:
    print(article)
