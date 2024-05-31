import config
import os
import json
import csv
import argparse
from tr_utils import initialize_language_model
from term_scraper import extract_terms_from_directory
from sklearn.model_selection import train_test_split
import random
import string

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

def read_segments_from_tm(tm_path, lang):
    """
    Reads segments from the translation memory.

    Parameters:
        tm_path (str): The file path to the translation memory (CSV format).
        lang (str): The target language code.

    Returns:
        list: A list of tuples where each tuple contains an English segment and its translation in the target language.
    """
    segments = []
    with open(tm_path, 'r', encoding='utf-8') as tm:
        reader = csv.DictReader(tm)
        for row in reader:
            segments.append((row['en'], row[lang]))
    return segments

def generate_random_string(length=4):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def augment_with_tags(data, num_copies=3):
    augmented_data = []

    for tuple in data:
        for _ in range(num_copies):
            tag = f"<{generate_random_string()}>"
            augmented_src = f"{tag}{tuple[0]}{tag}"
            augmented_tgt = f"{tag}{tuple[1]}{tag}"
            augmented_data.append((augmented_src, augmented_tgt))
    return augmented_data

def write_prompts_to_jsonl(data, file_path, language):
    """
    Writes data to a JSONL file in the format of prompts.

    Parameters:
        data (list): A list of tuples where each tuple contains a source segment and its translation.
        file_path (str): The file path to save the JSONL file.
        language (str): The target language for translation.

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
    if not config.TERMBASE_DIRECTORY:
        raise EnvironmentError("Source termbase directory not defined in the config file.")
    else: termbase_directory = config.TERMBASE_DIRECTORY


    lang = parse_arguments()
    language, _, tm_path = initialize_language_model(lang)

    term_tuples = extract_terms_from_directory(termbase_directory, lang)
    terms = [(term_tuple[1], term_tuple[2]) for term_tuple in term_tuples]
    segments = read_segments_from_tm(tm_path, lang)

    # Split segments for training and validation data
    train_data, validation_data = train_test_split(segments, test_size=0.2, random_state=42)
    
    # Add terms to training data
    train_data = train_data + terms

    # Augment data
    train_data = augment_with_tags(train_data)
    
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