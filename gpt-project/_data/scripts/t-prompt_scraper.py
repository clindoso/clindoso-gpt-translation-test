import os
import json
import argparse
import pandas

# The script takes two arguments, --en_dir and --es_dir, which are the respective directories containing the articles.
# Use this script to convert training data from articles into prompts OpenAI API

# Define base directory
base_dir = '/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_data'

# Create argument parser
argparser = argparse.ArgumentParser(description="Script to process directories")

# Define arguments
argparser.add_argument("--lang", default="/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/_de", help="German directory path")

# Define base directory
base_dir = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/_en/"

# Parse arguments
args = argparser.parse_args()

# Function to read and return the content of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Iterate through files in _en and _es directories and write each entry to a JSONL file
scraped_data = os.path.join(base_dir, 'scraped_data.jsonl')

with open(scraped_data, 'w', encoding='utf-8') as scraped_data_file:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):  # Check if the file is a Markdown file
                file_path_en = os.path.join(root, file)
                file_path_es = file_path_en.replace("_en", "_es")

                en_content = read_file(file_path_en).replace('\n', '\\n')
                es_content = ''  # Initialize es_content

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