import config
import os
import csv
import json

# Use this script to create CSV files as TMs with English as source language

def read_json_file(locale_path):
    """
    Reads a JSON file and returns the parsed JSON data.
    
    Parameters:
    locale_path (str): The path to the JSON file.
    
    Returns:
    dict_ The parsed JSON data.
    """
    try:
        with open(locale_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"The file at {locale_path} was not found.")
    except json.JSONDecodeError:
        print("Failed to decode JSON. Check the file content.")
    except Exception as e:
        print(f"An error occurred: {e}")

def find_json_files(locales_dir):
    """
    Finds and returns a list of JSON files in the given directory and its subdirectory
    
    Parameters:
    directory_path (str): The path to the directory to search for the JSON files 
    
    Returns:
    list: A list of paths to JSON files found in the directory and its subdirectories.
    """

    locales = []

    for root, _, files in os.walk(locales_dir):
        for file in files:
            if file.endswith('.json'):
                locale_path = os.path.join(root, file)
                if is_valid_locale(locale_path):
                    locales.append(locales_dir)
    
    return locales

def is_valid_locale(locale_path):
    """
    Checks if a file contains valid JSON content.
    
    Parameters:
    file_path (str): The path to the JSON file to check.
    
    Returns:
    bool: True if the file contains valid JSON, False otherwise
    """

    try:
        with open(locale_path, 'r', encoding='utf-8') as file:
            json.load(file)
        return True
    except (json.JSONDecodeError, FileNotFoundError):
        return False

def flatten_json(nested_json, parent_key='', separator='.'):
    """
    Flattens a nested JSON object.
    
    Parameters:
    nested_json (dict): The JSON object to flatten.
    parent_key (str): The base key string to use for the flattened keys.
    separator (str): The string used to separate flattened key parts.
    
    Returns:
    dict: A flattened JSON object.
    """

    items = {}
    for k, v in nested_json.items():
        new_key = f"{parent_key}{separator}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, separator))
        else:
            items[new_key] = v
    return items

def create_dict_from_json_files(locale_files):
    """
    Creates a dictionary from a list of JSON files. The key of the dictionary consist of the JSON keys, joined by '.'
    
    Parameters:
    json_files (list): A list of paths to JSON files.
    
    Returns:
    dict: A dictionary with flattened JSON keys and their corresponding values.
    """
    segment_dict = {}

    for locale_path in locale_files:
        locale_data = read_json_file(locale_path)
        flat_json = flatten_json(locale_data)
        segment_dict.update(flat_json)
        
    return segment_dict

def main():
    # Initialize locales directories
    if not config.LOCALE_REPOS_DIR:
        raise EnvironmentError("Locales directory is not configured in the config file.")
    else: locales_dir = config.LOCALE_REPOS_DIR

    # List locales files
    locales_list = find_json_files(locales_dir)

    # Create dictionary from all locales
    locales_dict = create_dict_from_json_files(locales_list)

    print(locales_dict)

if __name__ == "__main__"
