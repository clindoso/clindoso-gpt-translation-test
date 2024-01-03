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

# Function to equalize paragraphs
def equalize_list_lengths(list1, list2):
    # Find the length of the longest string in each list
    max_length1 = max(len(s) for s in list1)
    max_length2 = max(len(s) for s in list2)

    def combine_strings(lst, target_length):
        combined, temp = [], ''
        for s in lst:
            if len(temp) + len(s) <= target_length:
                temp += s + ' '
            else:
                combined.append(temp.strip())
                temp = s + ' '
        if temp:
            combined.append(temp.strip())
        return combined

    # Combine strings in each list
    list1 = combine_strings(list1, max_length2)
    list2 = combine_strings(list2, max_length1)

    return list1, list2

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

# Define sentence splitter

def sentence_splitter(file1_lines, file2_lines):
    # Patterns to ignore, with their placeholders
    # patterns = {
    #     "z.&nbsp;B.": "{PLACEHOLDER_ZB}",
    #     "d.&nbsp;h.": "{PLACEHOLDER_DH}",
    #     "i.e.": "{PLACEHOLDER_IE}",
    #     "e.g.": "{PLACEHOLDER_EG}",
    #     "u.U.": "{PLACEHOLDER_UU}",
    #     "u.a.": "{PLACEHOLDER_UA}",
    #     "p.&nbsp;ej.": "{PLACEHOLDER_PEJ}"
    # }

    # etc_pattern = re.compile(r'etc\.\s[a-z()]')

    def split_line(file1_lines, file2_lines):
        etc_pattern = re.compile(r'etc\.(?=\s[a-z()])')
        etc_placeholder = "{PLACEHOLDER_ETC}"
        etc_string = "etc."
        patterns = {
            "z.&nbsp;B.": "{PLACEHOLDER_ZB}",
            "d.&nbsp;h.": "{PLACEHOLDER_DH}",
            "i.e.": "{PLACEHOLDER_IE}",
            "e.g.": "{PLACEHOLDER_EG}",
            "u.U.": "{PLACEHOLDER_UU}",
            "u.a.": "{PLACEHOLDER_UA}",
            "p.&nbsp;ej.": "{PLACEHOLDER_PEJ}"
        }

        # Define new lists for processed lines
        processed_file1_lines = []
        processed_file2_lines = []
        
        for line1, line2 in zip(file1_lines, file2_lines):
            line1_processed = replace_patterns(etc_pattern, etc_placeholder, patterns, line1)
            line2_processed = replace_patterns(etc_pattern, etc_placeholder, patterns, line2)

            processed_file1_lines.append(line1_processed)
            processed_file2_lines.append(line2_processed)

            # Split and equalize if necessary
            # if line1.count('. ') != line2.count('. '):
            #     temp_file1_lines = line1.split('. ')
            #     temp_file2_lines = line2.split('. ')

            #     for i in range(len(temp_file1_lines)):
            #         temp_file1_lines[i] += '.'
            #     for i in range(len(temp_file2_lines)):
            #         temp_file2_lines[i] += '.'

            #     temp_file1_lines, temp_file2_lines = equalize_list_lengths(temp_file1_lines, temp_file2_lines)

            # else:
            #     temp_file1_lines = line1.split('. ')
            #     temp_file2_lines = line2.split('. ')

                # for i in range(len(temp_file1_lines)):    
                #     if ends_with_regex(temp_file1_lines[i]):
                #         temp_file1_lines += '.'
                # for i in range(len(temp_file2_lines)):
                #     if ends_with_regex(temp_file2_lines[i]):
                #         temp_file2_lines[i] += '.'
            

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
