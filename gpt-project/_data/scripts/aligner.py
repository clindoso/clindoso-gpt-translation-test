import os
import csv
import argparse

# Use this script to create a CSV file as a TM with English as source language
# This script takes one argument, --lang, the target language of the TM

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
            return [line.strip() for line in file 
                    if line.strip() and not (line.strip().startswith('<!--') and line.strip().endswith('-->'))]
    except Exception as e:
        raise Exception(f"Error reading {file_path}: {e}")

output_directory = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/"
output_filename = "en-" + args.lang + ".csv"

# Export to CSV
def write_to_csv(file1_lines, file2_lines, source_filename, output_filename, output_directory):
    os.makedirs(output_directory, exist_ok=True)
    output_filepath = os.path.join(output_directory, output_filename)
    
    with open(output_filepath, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        if csvfile.tell() == 0:
            writer.writerow(['en', args.lang, 'file'])

        if len(file1_lines) == len(file2_lines):
            for line1, line2 in zip(file1_lines, file2_lines):
                writer.writerow([line1, line2, source_filename])
        else:
            print("Files do not have the same amount of lines.")
            print(os.path.abspath(source_filename))

# Extract file contents
def extract_file_contents(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path_en = os.path.join(root, file)
            file_path_tl = file_path_en.replace("_en", "_" + args.lang)
            if os.path.exists(file_path_tl):
                file_content_en = read_and_split_file(file_path_en)
                file_content_tl = read_and_split_file(file_path_tl)
                write_to_csv(file_content_en, file_content_tl, file, output_filename, output_directory)

extract_file_contents("/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/_en/")
