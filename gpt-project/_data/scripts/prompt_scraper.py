import os
import json
import argparse
from sklearn.model_selection import train_test_split

# The script takes one argument, --lang, which selects the target language.
# Use this script to convert training data from articles into prompts OpenAI API

# Define base directory
base_dir = '/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_data'

# Create argument parser
argparser = argparse.ArgumentParser(description="Script to process directories")

# Define arguments
argparser.add_argument("--lang")

# Define base directory
base_dir = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/_en/"

# Parse arguments
args = argparser.parse_args()
args.lang = "_" + args.lang

# Function to read and return the content of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Iterate through files in _en and _es directories and write each entry to a JSONL file
scraped_data = os.path.join(os.path.dirname(base_dir), 'scraped_data.jsonl')

with open(scraped_data, 'w', encoding='utf-8') as scraped_data_file:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):  # Check if the file is a Markdown file
                file_path_en = os.path.join(root, file)
                file_path_es = file_path_en.replace("_en", args.lang)

                en_content = read_file(file_path_en).replace('\n', '\\n')

                # Check if the same file exists in _es directory
                if os.path.exists(file_path_es):
                    es_content = read_file(file_path_es).replace('\n', '\\n')

                    # Create a JSON object with the contents
                    json_entry = {
                        "messages": [
                            {"role": "system", "content": "Given a Markdown file in English with Kramdown tags, translate it into Spanish keeping the style, tone, formatting, and terminology consistent. Provide the translation in a Markdown file."},
                            {"role": "user", "content": en_content},
                            {"role": "assistant", "content": es_content}
                        ]
                    }

                    # Write the JSON object to the JSONL file, each object on a new line
                    json.dump(json_entry, scraped_data_file, ensure_ascii=False)
                    scraped_data_file.write('\n')

# Split the scraped data into training and validation sets
with open(scraped_data, 'r', encoding='utf-8') as scraped_data_file:
    data = [json.loads(line) for line in scraped_data_file]

# Splitting into train and validation sets (80:20 ratio)
train_data, validation_data = train_test_split(data, test_size=0.2, random_state=42)

# Write train data to a new file
train_file = os.path.join(base_dir, 'train_data.jsonl')
with open(train_file, 'w', encoding='utf-8') as train_file:
    for entry in train_data:
        json.dump(entry, train_file, ensure_ascii=False)
        train_file.write('\n')

# Write validation data to a new file
validation_file = os.path.join(base_dir, 'validation_data.jsonl')
with open(validation_file, 'w', encoding='utf-8') as validation_file:
    for entry in validation_data:
        json.dump(entry, validation_file, ensure_ascii=False)
        validation_file.write('\n')