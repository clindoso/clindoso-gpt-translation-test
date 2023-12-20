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

# Function to check if end of sentence is a letter
def ends_with_regex(string):
    # The '$' symbol in regex represents the end of the string
    return re.search('\w$', string) is not None

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

# Define sentence splitter
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

    def split_line(file1_lines, file2_lines):
        etc_pattern = re.compile(r'etc\.\s[a-z()]')
        patterns = {
            "z.&nbsp;B.": "{PLACEHOLDER_ZB}",
            "d.&nbsp;h.": "{PLACEHOLDER_DH}",
            "i.e.": "{PLACEHOLDER_IE}",
            "e.g.": "{PLACEHOLDER_EG}",
            "u.U.": "{PLACEHOLDER_UU}",
            "u.a.": "{PLACEHOLDER_UA}",
            "p.&nbsp;ej.": "{PLACEHOLDER_PEJ}"
        }

        # Define new lists
        processed_file1_lines = []
        processed_file2_lines = []
        
        for i in range(len(file1_lines)):
            # Replace patterns in file1_lines
            line1 = file1_lines[i]
            line1 = etc_pattern.sub("{PLACEHOLDER_ETC}", line1)
            for pattern, placeholder in patterns.items():
                line1 = line1.replace(pattern, placeholder)

            # Replace patterns in file2_lines
            line2 = file2_lines[i]
            line2 = etc_pattern.sub("{PLACEHOLDER_ETC}", line2)
            for pattern, placeholder in patterns.items():
                line2 = line2.replace(pattern, placeholder)

            print(f"Original Line {i} in File1: {file1_lines[i]}")
            print(f"Original Line {i} in File2: {file2_lines[i]}")

            # Split and equalize if necessary
            if line1.count('. ') != line2.count('. '):
                temp_file1_lines = line1.split('. ')
                temp_file2_lines = line2.split('. ')

                for i in range(len(temp_file1_lines)):
                    temp_file1_lines[i] += '.'
                for i in range(len(temp_file2_lines)):
                    temp_file2_lines[i] += '.'

                temp_file1_lines, temp_file2_lines = equalize_list_lengths(temp_file1_lines, temp_file2_lines)

            else:
                temp_file1_lines = line1.split('. ')
                temp_file2_lines = line2.split('. ')

                for i in range(len(temp_file1_lines)):    
                    if ends_with_regex(temp_file1_lines[i]):
                        temp_file1_lines += '.'
                for i in range(len(temp_file2_lines)):
                    if ends_with_regex(temp_file2_lines[i]):
                        temp_file2_lines[i] += '.'
            
            for i in range(len(temp_file1_lines)):
                processed_file1_lines.append(temp_file1_lines[i])
            for i in range(len(temp_file2_lines)):
                processed_file2_lines.append(temp_file2_lines[i])
            
        print(len(processed_file1_lines) == len(processed_file2_lines))
        for i in range(len(processed_file1_lines)):
            print(f"Processed Line {i} in File1: {processed_file1_lines[i]}")
        for i in range(len(processed_file2_lines)):
            print(f"Processed Line {i} in File2: {processed_file2_lines[i]}")

        # Restore placeholders to original patterns
        for i in range(len(processed_file1_lines)):
            line1 = processed_file1_lines[i]
            for placeholder, pattern in patterns.items():
                line1 = line1.replace(placeholder, pattern)
            processed_file1_lines[i] = line1
        for i in range(len(processed_file2_lines)):
            line2 = processed_file2_lines[i]
            for placeholder, pattern in patterns.items():
                line2 = line2.replace(placeholder, pattern)
            processed_file2_lines[i] = line2

        return processed_file1_lines, processed_file2_lines

    
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
print("The following articles might not be aligned:")
for article in not_aligned_articles:
    print(article)
