import os
import json
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
    "de": {"language": "German"},
    "es": {"language": "Spanish"},
    "fr": {"language": "French"},
    "it": {"language": "Italian"},
    "nl": {"language": "Dutch"}
}

# Conditional for language-specific arguments

if args.lang in languages_dict:
    language = languages_dict[args.lang]["language"]
else:
    print(f"This script does not support {args.lang}. Enter one of the following language abbreviations: de, es, fr, it, nl.")

