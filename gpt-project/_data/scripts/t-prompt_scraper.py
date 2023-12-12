import os
import json
import argparse

# The script takes two arguments, --en_dir and --es_dir, which are the respective directories containing the articles.
# Use this script to convert training data from articles into prompts OpenAI API

# Define base directory
base_dir = '/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_data'

# Create argument parser
argparser = argparse.ArgumentParser(description="Script to process directories")

# Define arguments
argparser.add_argument("--en_dir", default='/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_en/training', help="English directory path")
argparser.add_argument("--es_dir", default='/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_es/training', help="Spanish directory path")

# Parse arguments
args = argparser.parse_args()

# Function to read and return the content of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Iterate through files in _en and _es directories and write each entry to a JSONL file
scraped_data_file_path = os.path.join(base_dir, 'md_training_data.jsonl')

with open(scraped_data_file_path, 'w', encoding='utf-8') as scraped_data_file:
    for en_file in os.listdir(args.en_dir):
        if en_file.endswith('.md'):  # Check if the file is a Markdown file
            en_file_path = os.path.join(args.en_dir, en_file)
            es_file_path = os.path.join(args.es_dir, en_file)

            # Check if the same file exists in _es directory
            if os.path.exists(es_file_path):
                en_content = read_file(en_file_path).replace('\n', '\\n')
                es_content = read_file(es_file_path).replace('\n', '\\n')

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
