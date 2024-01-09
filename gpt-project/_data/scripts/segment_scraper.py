import os
import json
import csv
import argparse
from sklearn.model_selection import train_test_split

# The script takes one argument, --lang, which selects the target language.
# Use this script to convert training data from TM into prompts OpenAI API

# Create argument parser
argparser = argparse.ArgumentParser(description="Script to process directories")

# Define arguments
argparser.add_argument("--lang")

# Define base directory
base_dir = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/_en/"

# Assign parent folder of base directory as output directory
output_dir = os.path.dirname(base_dir)

# Parse arguments
args = argparser.parse_args()

# Define language name and language-specific fine-tuned model
languages_dict = {
    "de": {"language": "German", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-de.csv"},
    "es": {"language": "Spanish", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-es.csv"},
    "fr": {"language": "French", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-fr.csv"},
    "it": {"language": "Italian", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-it.csv"},
    "nl": {"language": "Dutch", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-nl.csv"}
}

# Conditional for language-specific arguments

if args.lang in languages_dict:
    language = languages_dict[args.lang]["language"]
    tm_path = languages_dict[args.lang]["tm_path"]
else:
    print(f"This script does not support {args.lang}. Enter one of the following language abbreviations: de, es, fr, it, nl.")

# Create empty segment list to compile segments from TM
segments = []

# Extract segments from TM to segment list
with open(tm_path, 'r', encoding='utf-8') as tm:
    reader = csv.DictReader(tm)
    for row in reader:
        segments.append((row['en'], row[args.lang]))

print(output_dir)
