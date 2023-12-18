import Levenshtein
import argparse

# Use this script to calculate the Levenshtein between two articles
# The script takes two arguments, --gpt_tr and --fn_tr,

# Create argument parser
argparser = argparse.ArgumentParser(description="Script to calculate the Levenshtein between two articles")

# Define arguments
argparser.add_argument("--gpt_tr", help="Translation from ChatGPT")
argparser.add_argument("--fn_tr", help="Final file")

# Parse arguments
args = argparser.parse_args()

# Function to read and return the content of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Extract content from file
content_raw = read_file(args.gpt_tr)
content_final = read_file(args.fn_tr)

# Calculate the Levenshtein distance
distance = Levenshtein.distance(content_raw, content_final)
print(f"Levenshtein Distance: {distance}")
