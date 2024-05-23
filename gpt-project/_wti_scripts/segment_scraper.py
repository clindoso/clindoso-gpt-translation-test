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

