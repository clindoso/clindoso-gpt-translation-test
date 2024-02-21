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
def read_and_split_file(source_file_path):
    try:
        with open(source_file_path, 'r', encoding='utf-8') as file:
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
        raise Exception(f"Error reading {source_file_path}: {e}")
    

# Define output directory and file name
output_directory = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/"
output_filename = f"en-{args.lang}-{file_name}.csv"

# Check if output directory exists
os.makedirs(output_directory, exist_ok=True)
output_filepath = os.path.join(output_directory, output_filename)

def clear_csv_content(file_path):
    with open(file_path, 'w') as file:
        pass

# Patterns to ignore, with their placeholders
patterns_to_replace = {
    re.compile(r'z\.&nbsp;B\.'): "{PLACEHOLDER_ZB}",
    re.compile(r'd\.&nbsp;h\.'): "{PLACEHOLDER_DH}",
    re.compile(r'i\.e\.'): "{PLACEHOLDER_IE}",
    re.compile(r'e\.g\.'): "{PLACEHOLDER_EG}",
    re.compile(r'u\.U\.'): "{PLACEHOLDER_UU}",
    re.compile(r'u\.a\.'): "{PLACEHOLDER_UA}",
    re.compile(r'p\.&nbsp;ej\.'): "{PLACEHOLDER_PEJ}",
    re.compile(r'etc.\s?$'): "{PLACEHOLDER_ETC}"
}

patterns_to_restore = {
    "{PLACEHOLDER_ZB}": 'z.&nbsp;B.',
    "{PLACEHOLDER_DH}": 'd.&nbsp;h.',
    "{PLACEHOLDER_IE}": 'i.e.',
    "{PLACEHOLDER_EG}": 'e.g.',
    "{PLACEHOLDER_UU}": 'u.U.',
    "{PLACEHOLDER_UA}": 'u.a.',
    "{PLACEHOLDER_PEJ}": 'p.&nbsp;ej.',
    "{PLACEHOLDER_ETC}": 'etc. '
}

# Define pattern replacer
def pattern_replacer(file1_lines, file2_lines, patterns_to_replace):

    # Initiate segment lists for list with replaced patterns
    replaced_lines1 = []
    replaced_lines2 = []

    # Iterate over lines in target and source languages
    for line1, line2 in zip(file1_lines, file2_lines):
        # Iterate over patterns in the segment
        for pattern, placeholder in patterns_to_replace.items():
            replaced_line1 = pattern.sub(placeholder, line1)
            replaced_line2 = pattern.sub(placeholder, line2)
            line1 = replaced_line1
            line2 = replaced_line2
        replaced_lines1.append(replaced_line1)
        replaced_lines2.append(replaced_line2)

    return replaced_lines1, replaced_lines2

    
def line_splitter(file1_lines, file2_lines):
    period_pattern = r'\.\s'

    # Define new lists for processed lines
    split_file1_lines = []
    split_file2_lines = []
    
    # Iterate over the segment pair
    for line1, line2 in zip(file1_lines, file2_lines):
        # Check if segments have the same amount of periods
        if line1.count('.') != line2.count('.'):
            # If they have a different amount of periods
            # Ignore cases in which one language has only one sentence
            if line1.count('.') == 1 or line2.count('.') == 1:
                split_file1_lines.append(line1)
                split_file2_lines.append(line2)
                
            # Process lines with different amount of sentences
            else:
                # Use re.split() to split the line
                split_segment1 = re.split(period_pattern, line1)
                split_segment2 = re.split(period_pattern, line2)

                # Exclude the last empty string if any, caused by a period at the end
                if split_segment1[-1] == '':
                    split_segment1 = split_segment1[:-1]
                if split_segment2[-1] == '':
                    split_segment2 = split_segment2[:-1]
                
                # After splitting, delimiters will be included in the list as separate items
                # Here, we recombine sentences with their trailing delimiter
                # Re-combine the split segments with their delimiters
                recombined_segment1 = [split_segment1[i] + '.' if not split_segment1[i].endswith('.') else split_segment1[i] for i in range(len(split_segment1))]
                recombined_segment2 = [split_segment2[i] + '.' if not split_segment2[i].endswith('.') else split_segment2[i] for i in range(len(split_segment2))]

                # Calculate segment lengths
                lengths1 = [len(sentence) for sentence in recombined_segment1]
                lengths2 = [len(sentence) for sentence in recombined_segment2]
                # Calculate total lengths
                total_lengths1 = sum(lengths1)
                total_lengths2 = sum(lengths2)
                # Normalize lenghts
                normalized_lengths1 = [length/total_lengths1 for length in lengths1]
                normalized_lengths2 = [length/total_lengths2 for length in lengths2]
                # Calculate normalized length ratios
                ratios = [normalized_lengths1[i] / normalized_lengths2[i] if normalized_lengths2[i] != 0 else float('inf') for i in range(min(len(normalized_lengths1), len(normalized_lengths2)))]
                
                # Compare normalized lenghts
                i = 0
                while i < len(split_segment1) and i < len(split_segment2):
                    # Check if 'i' is within both lists' bounds
                    if i < len(normalized_lengths1) and i < len(normalized_lengths2):
                        # Handling the case when the ratio is less than 0.8
                        if ratios[i] < 0.8:
                            if i < len(recombined_segment1) - 1:  # Ensure i+1 is within bounds for recombined_segment1
                                split_file1_lines.append(recombined_segment1[i] + recombined_segment1[i + 1])
                                recombined_segment1 = recombined_segment1[:i + 1] + recombined_segment1[i + 2:]
                                # Recalculate normalized lengths
                                lengths1 = [len(sentence) for sentence in recombined_segment1]
                                normalized_lengths1 = [length/total_lengths1 for length in lengths1]
                                ratios = [normalized_lengths1[i] / normalized_lengths2[i] if normalized_lengths2[i] != 0 else float('inf') for i in range(min(len(normalized_lengths1), len(normalized_lengths2)))]
                            else:
                                split_file1_lines.append(recombined_segment1[i])
                            split_file2_lines.append(recombined_segment2[i])
                        # Handling cases when the ratio is between 0.8 and 1.2
                        elif 0.8 <= ratios[i] <= 1.2:
                            split_file1_lines.append(recombined_segment1[i])
                            split_file2_lines.append(recombined_segment2[i])
                        # Handling the case when the ratio is not within the specified ranges
                        else:
                            split_file1_lines.append(recombined_segment1[i])
                            if i < len(recombined_segment2) - 1:  # Ensure i+1 is within bounds for recombined_segment2
                                split_file2_lines.append(recombined_segment2[i] + recombined_segment2[i + 1])
                                recombined_segment2 = recombined_segment2[:i + 1] + recombined_segment2[i + 2:]
                                ratios = [normalized_lengths1[i] / normalized_lengths2[i] if normalized_lengths2[i] != 0 else float('inf') for i in range(min(len(normalized_lengths1), len(normalized_lengths2)))]
                            else:
                                split_file2_lines.append(recombined_segment2[i])
                    
                    i += 1 # Move to the next pair of sentences
        
        # If they have the same amount of periods
        else:
            # Check if they have more than one period
            if line1.count('.') > 1 or line2.count('.') > 1:
                print(f"Non-split: {line1}\n", f"Non-split: {line2}\n")
                # Split segments by period
                split_segment1 = re.split(period_pattern, line1)
                split_segment2 = re.split(period_pattern, line2)
                print(f"Split: {split_segment1}\n", f"Split: {split_segment2}\n")

                # Exclude the last empty string if any, caused by a period at the end
                if split_segment1[-1] == '':
                    split_segment1 = split_segment1[:-1]
                if split_segment2[-1] == '':
                    split_segment2 = split_segment2[:-1]
                
                # After splitting, delimiters will be included in the list as separate items
                # Here, we recombine sentences with their trailing delimiter
                # Re-combine the split segments with their delimiters
                recombined_segment1 = [split_segment1[i] + '.' if not split_segment1[i].endswith('.') else split_segment1[i] for i in range(len(split_segment1))]
                recombined_segment2 = [split_segment2[i] + '.' if not split_segment2[i].endswith('.') else split_segment2[i] for i in range(len(split_segment2))]

                print(f"Recombined: {recombined_segment1}\n", f"Recombined: {recombined_segment2}\n")

                # Append recombined segments separately
                j = 0
                while j < len(recombined_segment1) and j < len(recombined_segment2):
                    split_file1_lines.append(recombined_segment1[j])
                    split_file2_lines.append(recombined_segment2[j])
                    j += 1

            else:
                split_file1_lines.append(line1)
                split_file2_lines.append(line2)

    return split_file1_lines, split_file2_lines
        
def pattern_restorer(file1_lines, file2_lines, patterns_to_restore):

    restored_file1_lines = []
    restored_file2_lines = []

    for line1, line2 in zip(file1_lines, file2_lines):
        for placeholder, pattern in patterns_to_restore.items():
            line1, line2 = line1.replace(placeholder, pattern), line2.replace(placeholder, pattern)
        restored_file1_lines.append(line1)
        restored_file2_lines.append(line2)
    
    return restored_file1_lines, restored_file2_lines

def strip_leading_non_words(file1_lines, file2_lines):
    stripped_lines1 = []
    stripped_lines2 = []
    leading_non_words = r'^\W+\s'

    for line1, line2 in zip(file1_lines, file2_lines):
        line1, line2 = re.sub(leading_non_words, '', line1), re.sub(leading_non_words, '', line2)
        stripped_lines1.append(line1)
        stripped_lines2.append(line2)
    return stripped_lines1, stripped_lines2

# def tag_replacer(file1_lines, file2_lines, tag_dict):
#     tag_patterns = config.tag_patterns
#     stripped_file1_lines = []
#     stripped_file1_lines = []

#     for line1, line2 in zip(file1_lines, file2_lines):
#         i = 1
#         for tag_pattern in tag_patterns:
#             if re.match(line1, tag_pattern):
#                 line1 = line1.replace(tag_pattern, f'{i}')
#                 i += 1
#             if re.match(line2, tag_pattern):
#                 line2 = line2.replace(tag_pattern, f'{i}')
#                 i += 1
            

# Function to export to CSV
def write_to_csv(file1_lines, file2_lines, source_filename, output_filepath):
    """
    Writes lines from two files to a CSV, including the source filename for each line.

    Args:
        file1_lines (list of str): Lines from the first file to be written to the CSV.
        file2_lines (list of str): Lines from the second file to be written to the CSV.
        source_filename (str): The name of the source file.
        output_filepath (str): The path to the CSV file where the data is to be written.

    The function assumes that the two files should have the same number of lines and
    that a series of processing steps (pattern replacing, line splitting, and pattern
    restoring) should be performed before writing the data to the CSV. If the number
    of lines in both files does not match, it prints an error message.
    """

    with open(output_filepath, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Write header row if the CSV file is empty
        if csvfile.tell() == 0:
            writer.writerow(['en', args.lang, 'file'])

        if len(file1_lines) == len(file2_lines):
            # Process lines before writing
            file1_lines, file2_lines = pattern_replacer(file1_lines, file2_lines, patterns_to_replace)
            file1_lines, file2_lines = line_splitter(file1_lines, file2_lines)
            file1_lines, file2_lines = pattern_restorer(file1_lines, file2_lines, patterns_to_restore)
            file1_lines, file2_lines = strip_leading_non_words(file1_lines, file2_lines)
            for line1, line2 in zip(file1_lines, file2_lines):
                writer.writerow([line1, line2, source_filename])
        else:
            print("The source and target files do not have the same amount of code lines. Check if they are up-to-date.")
        

# Define extract file contents
def extract_file_contents(file_path_source, output_filepath, file_name, lang, file_extension=".md"):
    print(lang)
    if file_path_source.endswith(file_extension):
        file_path_target = file_path_source.replace("_en", "_" + lang)
        print(file_path_target)
        if os.path.exists(file_path_target):
            source_file_content = read_and_split_file(file_path_source)
            print(file_path_source)
            target_file_content = read_and_split_file(file_path_target)
            print(file_path_target)
            write_to_csv(source_file_content, target_file_content, file_name, output_filepath)
        else:
            print(f"File does not exist in the {lang}.")

# Delete existing TM
clear_csv_content(output_filepath)
# Extract file contents
extract_file_contents(args.file, output_filepath, file_name, args.lang)
print(args.lang)
print(f"Aligned article is : {output_filepath}")
