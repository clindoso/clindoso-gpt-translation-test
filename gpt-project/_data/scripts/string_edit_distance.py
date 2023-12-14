import Levenshtein
import argparse

# Use this script to calculate the Levenshtein between two articles

# Create argument parser
argparser = argparse.ArgumentParser(description="Script to calculate the Levenshtein between two articles")

# Define arguments
argparser.add_argument("--raw_tr", help="Translation from ChatGPT")
argparser.add_argument("--pe_tr", help="Post-edited file")

# Parse arguments
args = argparser.parse_args()

# Function to read and return the content of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Extract content from file
content_raw = read_file(args.raw_tr)
content_pe = read_file(args.pe_tr)

# Calculate the Levenshtein distance
distance = Levenshtein.distance(content_raw, content_pe)
print(f"Levenshtein Distance: {distance}")
