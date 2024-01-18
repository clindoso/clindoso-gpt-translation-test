import os
import yaml

# This funtion will be used within the segment scraper script to include the termbase in the training data set.

# Function to read and return the content of a file
def process_file(file_path, lang, source_lang='en'):
    """
    Process a single YAML file and extract the terms in English and in a target language.
    Returns a list of terms in English and target language as tuples.
    """
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    term_tuple = []
    source_term = data[source_lang]["name"]
    target_term = data.get(lang, {}).get("name", "")
    if target_term:
        term_tuple = (source_term, target_term)
    return term_tuple

def extract_terms(termbase_directory, lang):
    term_tuples = []
    for filename in os.listdir(termbase_directory):
        if filename.endswith('.yml'):
            file_path = os.path.join(termbase_directory, filename)
            term_tuple = process_file(file_path, lang)
            if term_tuple:
                term_tuples.append(term_tuple)
    
    return term_tuples