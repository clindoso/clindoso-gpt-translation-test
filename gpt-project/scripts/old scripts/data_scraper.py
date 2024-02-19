import os
import json
import csv
import argparse
from term_scraper import extract_terms_from_directory
from sklearn.model_selection import train_test_split

# The script takes one argument, --lang, which selects the target language.
# Use this script to convert training data from TM into prompts OpenAI API

# Create argument parser
argparser = argparse.ArgumentParser(description="Script to process directories")

# Define arguments
argparser.add_argument("--lang")

# Define base directory
base_dir = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/_en"

# Define termbase directory
termbase_directory = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_data/terminology"

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
    raise ValueError(f"This script does not support {args.lang}. Enter one of the supported languages are de (German), es (Spanish), fr (French), it (Italian), nl (Dutch).")

# Extract terms from the TB

terms = extract_terms_from_directory(termbase_directory, args.lang)

# Create empty segment list to collect segments from TM
segments = []

# Extract segments from TM to segment list
with open(tm_path, 'r', encoding='utf-8') as tm:
    reader = csv.DictReader(tm)
    for row in reader:
        segments.append((row['en'], row[args.lang]))

# Split into train and validation sets (80:20 ratio)
train_data, validation_data = train_test_split(segments, test_size=0.2, random_state=42)

# Define train data and validation data file paths
train_data_file_path = os.path.join(output_dir, f'en-{args.lang}_train_data.jsonl')
validation_data_file_path = os.path.join(output_dir, f'en-{args.lang}_validation_data.jsonl')

def write_tuple_into_prompt(data, data_file, language):
    """
    Reads a list of tuples and converts them into ChatGPT prompts for translation.
    
    Parameters:
        data (list): List of tuples.
        data_file (str): JSONL file where prompts will be saved.
        language (str): Target laguage for translation
    
    Returns:
        list: A list of lines from the source file, or None if file not found.
    """
    for segment_pair in data:
        json_entry = {
            "messages": [
                {"role": "system", "content": f"Given a sentence in Markdown format, translate the sentence to {language} keeping the style, tone, formatting, and terminology consistent and provide just the translation in plain language."},
                {"role": "user", "content": segment_pair[0]},
                {"role": "assistant", "content": segment_pair[1]}
            ]
        }
        json.dump(json_entry, data_file, ensure_ascii=False)
        data_file.write('\n')

# Create train data file
with open(train_data_file_path, 'w', encoding='utf-8') as train_data_file:
    # Write terms into train data file
    for term_pair in terms:
        json_entry = {
            "messages": [
                {"role": "system", "content": f"Given a term in English, translate it into {language}. Provide only the term translation."},
                {"role": "user", "content": term_pair[0]},
                {"role": "assistant", "content": term_pair[1]}
            ]
        }
        json.dump(json_entry, train_data_file, ensure_ascii=False)
        train_data_file.write('\n')
    # Write train segment tuple content into train data file
    write_tuple_into_prompt(train_data, train_data_file, language)

# Create validation data file
with open(validation_data_file_path, 'w', encoding='utf-8') as validation_data_file:
    # Write validation segment tuple content into validation data file
    write_tuple_into_prompt(validation_data, validation_data_file, language)

data_directory = os.path.dirname(train_data_file_path)

print(f"The data was written to {data_directory}")
