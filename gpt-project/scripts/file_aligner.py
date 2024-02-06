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

        return stripped_text
    
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

def pattern_replacer(file1_lines, file2_lines):
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

    # Initiate segment lists for list with replaced patterns
    replaced_lines1 = []
    replaced_lines2 = []
    # Iterate over lines in target and source languages
    for line1, line2 in zip(file1_lines, file2_lines):
        # Iterate over patterns in the segment
        for pattern, placeholder in patterns:
            replaced_line1 = line1.replace(pattern, placeholder)
            replaced_line2 = line2.replace(pattern, placeholder)
        replaced_lines1.append(replaced_line1)
        replaced_lines2.append(replaced_line2)

    return replaced_lines1, replaced_lines2

    
def split_line(file1_lines, file2_lines):
    period_pattern = r'(\.\s)'

    # Define new lists for processed lines
    split_file1_lines = []
    split_file2_lines = []
        
    for line1, line2 in zip(file1_lines, file2_lines):

        # Split and equalize if necessary
        if line1.count('. ') != line2.count('. '):
            # Ignore cases in which one language has only one sentence
            if line1.count('. ') == 1 or line2.count('. ') == 1:
                split_file1_lines.append(line1)
                split_file2_lines.append(line2)
            # Process lines with different amount of sentences
            else:
                # Split segments
                split_segment1 = line1.split(period_pattern)
                split_segment2 = line2.split(period_pattern)
                
                # Calculate segment lengths
                lengths1 = [len(sentence) for sentence in split_segment1]
                lengths2 = [len(sentence) for sentence in split_segment2]
                
                # Normalize lenghts
                normalized_lengths1 = [length/sum(lengths1) for length in lengths1]
                normalized_lengths2 = [length/sum(lengths2) for length in lengths2]
                
                # Compare normalized lenghts
                for i in range(max([len(normalized_lengths1), len(normalized_lengths2)])):
                    if normalized_lengths1[i] and normalized_lengths2[i]:
                        if normalized_lengths1[i]/normalized_lengths2[i] < 0.8:
                            split_file1_lines.append(split_segment1[i] + split_segment1[i + 1])
                            split_file2_lines.append(split_segment2[i])
                            for y in range((i+1, max([len(normalized_lengths1), len(normalized_lengths2)]))):
                                split_file1_lines[y] = split_file1_lines[y+1]
                        elif 1.2 > normalized_lengths1[i]/normalized_lengths2[i] > 0.8:
                            split_file1_lines.append(split_segment1[i])
                            split_file2_lines.append(split_segment2[i])
                        else:
                            split_file1_lines.append(split_segment1[i])
                            split_file2_lines.append(split_segment2[i] + split_segment2[i + 1])
                            for y in range((i+1, max([len(normalized_lengths1), len(normalized_lengths2)]))):
                                split_file2_lines[y] = split_file2_lines[y+1]

        else:
            split_file1_lines.append(line1)
            split_file2_lines.append(line2)
        
def pattern_restorer(file1_lines, file2_lines):
    pass
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
