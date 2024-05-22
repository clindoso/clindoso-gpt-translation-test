import config
import os
import csv
import json

# Use this script to create CSV files as TMs with English as source language

def read_json_file(file_path):
    """
    Reads a JSON file and returns the parsed JSON data.
    
    Parameters:
    file_path (str): The path to the JSON file.
    
    Returns:
    dict_ The parsed JSON data.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except json.JSONDecodeError:
        print("Failed to decode JSON. Check the file content.")
    except Exception as e:
        print(f"An error occurred: {e}")

