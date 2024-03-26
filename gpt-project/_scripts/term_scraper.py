import os
import yaml

# This funtion will be used within the segment scraper script to include the termbase in the training data set.

# Function to read and return the content of a file
def extract_term_from_file(file_path, lang, source_lang='en'):
    """
    Extract terms from a YAML file for specified languages.
    Returns a tuple of terms in the default and target languages if available.
    """
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)

        source_term = data[source_lang]["name"]
        target_term = data.get(lang, {}).get("name", "")
        term_tuple = (source_term, target_term) if target_term else None
        return term_tuple
    
    except Exception as e:
        print(f"{file_path} not found.")
        return None

def extract_terms_from_directory(termbase_directory, lang):
    """
    Extract terms from all YAML files in the specified directory.
    Returns a list of tuples with terms in the default and target languages.
    """
    term_tuples = []
    for file_name in os.listdir(termbase_directory):
        if file_name.endswith('.yml'):
            file_path = os.path.join(termbase_directory, file_name)
            term_tuple = extract_term_from_file(file_path, lang)
            if term_tuple:
                term_tuples.append(term_tuple)
    
    return term_tuples