import Levenshtein
import argparse

# Use this script to calculate the Levenshtein between two articles
# The script takes two arguments, --t1 and --t2,

# Create argument parser
argparser = argparse.ArgumentParser(description="Script to calculate the Levenshtein between two articles")

# Define arguments
argparser.add_argument("--t1", help="Translation from ChatGPT")
argparser.add_argument("--t2", help="Final file")

# Parse arguments
args = argparser.parse_args()

# Function to read and return the content of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Extract content from file
content_raw = read_file(args.t1)
content_final = read_file(args.t2)

# Calculate the Levenshtein distance
distance = Levenshtein.distance(content_raw, content_final)

# Calculate Levenshtein distance/source character
content_raw_count = len(content_raw)
ld_sc = distance/content_raw_count

print(f"Levenshtein Distance: {distance}")
print(f"Levenshtein Distance/source character: {ld_sc:.1f}%")
