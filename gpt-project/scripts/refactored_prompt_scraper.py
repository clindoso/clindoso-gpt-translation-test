import config
import os
import json
import argparse
from sklearn.model_selection import train_test_split

# The script takes one argument, --lang, which selects the target language.
# Use this script to convert training data from articles into prompts OpenAI API

def parse_arguments():
    """
    Parse command-line arguments for TM target language.
    Returns the string for language.
    """
    parser = argparse.ArgumentParser(description="Script to create a translation memory in EN and a selected target language.")
    parser.add_argument("--lang", required=True, help="TM target language")
    args = parser.parse_args()
    return args.lang

def initialize_language_model(lang):
    """
    Validates and returns the language name based on the provided language code.
    """
    language_models = config.LANGUAGE_MODELS
    if lang not in language_models:
        valid_langs = ", ".join(f'"{code}" for {desc["language"]}' for code, desc in language_models.items())
        raise ValueError(f"Invalid language code. Use one of the following: {valid_langs}")
    return language_models[lang]["language"]

def read_file(file_path):
    """
    Reads and returns the content of a file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_file_paths(docs_directory, lang):
    """
    Generates and validates pairs of source and target file paths for the given language.
    """
    for root, _, files in os.walk(docs_directory):
        for file in files:
            if file.endswith('.md'):
                source_file_path = os.path.join(root, file)
                target_file_path = source_file_path.replace('/_en/', f'/_{lang}/')
                if os.path.exists(target_file_path):
                    yield source_file_path, target_file_path

def scrape_data_to_jsonl(docs_directory, lang, output_dir):
    """
    Scrapes data from documents and writes to a JSONL file.
    """
    language = initialize_language_model(lang)
    scraped_data_file_path = os.path.join(output_dir, 'scraped_data.jsonl')

    with open(scraped_data_file_path, 'w', encoding='utf-8') as file:
        for source_file_path, target_file_path in generate_file_paths(docs_directory, lang):
            source_content = read_file(source_file_path).replace('\n', '\\n')
            target_content = read_file(target_file_path).replace('\n', '\\n')

            json_entry = {
                "messages": [
                    {"role": "system", "content": f"Translate an English Markdown file into {language}, maintaining style, tone, formatting, and terminology."},
                    {"role": "user", "content": source_content},
                    {"role": "assistant", "content": target_content}
                ]
            }
            json.dump(json_entry, file, ensure_ascii=False)
            file.write('\n')
    return scraped_data_file_path

def split_data(scraped_data_file_path, output_dir):
    """
    Splits the data into training and validation sets and writes them to separate files.
    """
    with open(scraped_data_file_path, 'r', encoding='utf-8') as file:
        data = [json.loads(line) for line in file]
    
    train_data, validation_data = train_test_split(data, test_size=0.2, random_state=42)

    train_file_path = os.path.join(output_dir, 'train_data.jsonl')
    validation_file_path = os.path.join(output_dir, 'validation_data.jsonl')

    for dataset, path in zip((train_data, validation_data), (train_file_path, validation_file_path)):
        with open(path, 'w', encoding='utf-8') as file:
            for entry in dataset:
                json.dump(entry, file, ensure_ascii=False)
                file.write('\n')

    print(f"Training data file was created under {train_file_path}")
    print(f"Validation data file was created under {validation_file_path}")

def main():
    # Initialize docs directory
    if not config.docs_directory:
        raise EnvironmentError("Source documents directory not defined in the config file.")
    else: docs_directory = config.docs_directory
    
    # Initialize output_dir
    output_dir = os.path.dirname(docs_directory)

    # Initializes target lang
    lang = parse_arguments()

    # Scrape data from _docs to JSONL file
    scraped_data_file_path = scrape_data_to_jsonl(docs_directory, lang, output_dir)

    # Split scraped data into training and validadtion data
    split_data(scraped_data_file_path, output_dir)

if __name__ == "__main__":
    main()