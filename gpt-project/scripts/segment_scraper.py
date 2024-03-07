import config
import os
import json
import csv
import argparse
from term_scraper import extract_terms_from_directory
from sklearn.model_selection import train_test_split

# The script takes one argument, --lang, which selects the target language.
# Use this script to segment articles and convert them into training data as OpenAI API prompts

def parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Convert training data from TM into prompts for OpenAI API.")
    parser.add_argument("--lang", required=True, help="Target language code")
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
    return language_models[lang]["language"], language_models[lang]["tm_path"]

def read_segments_from_tm(tm_path, lang):
    """
    Read segments from translation memory.
    """
    segments = []
    with open(tm_path, 'r', encoding='utf-8') as tm:
        reader = csv.DictReader(tm)
        for row in reader:
            segments.append((row['en'], row[lang]))
    return segments

def write_prompts_to_jsonl(data, file_path, language):
    """
    Write data to a JSONL file in the format of prompts.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        for segment_pair in data:
            json_entry = {
                "messages": [
                    {"role": "system", "content": f"Translate the sentence to {language} keeping style, tone, formatting consistent."},
                    {"role": "user", "content": segment_pair[0]},
                    {"role": "assistant", "content": segment_pair[1]}
                ]
            }
            json.dump(json_entry, file, ensure_ascii=False)
            file.write('\n')

def main():

    # Initialize termbase directory
    if not config.termbase_directory:
        raise EnvironmentError("Source termbase directory not defined in the config file.")
    else: termbase_directory = config.termbase_directory


    lang = parse_arguments()
    language, tm_path = initialize_language_model(lang)

    terms = extract_terms_from_directory(termbase_directory, lang)
    segments = read_segments_from_tm(tm_path, lang)

    # Combine terms and segments for training data
    combined_data = terms + segments
    train_data, validation_data = train_test_split(combined_data, test_size=0.2, random_state=42)

    # Assign output_dir
    output_dir = os.path.dirname(os.path.dirname(tm_path))

    # Append /data to the output_dir path
    output_dir = os.path.join(output_dir, 'gpt-data')

    # Now, create the directory including the /data subdirectory
    os.makedirs(output_dir, exist_ok=True)
    train_file_path = os.path.join(output_dir, f'{lang}_train_data.jsonl')
    validation_file_path = os.path.join(output_dir, f'{lang}_validation_data.jsonl')

    write_prompts_to_jsonl(train_data, train_file_path, language)
    write_prompts_to_jsonl(validation_data, validation_file_path, language)

    print(f"Training and validation data written to {output_dir}")

if __name__ == "__main__":
    main()
