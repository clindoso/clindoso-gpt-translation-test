import json
import csv
from pathlib import Path

# Define the path to your JSON files and the output CSV file
json_files_directory = Path("/path/to/your/json/files")
output_csv_file = Path("/path/to/output/translations.csv")

# Load JSON data
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Extract keys and values with full path
def extract_with_full_path(data, prefix=''):
    for key, value in data.items():
        current_path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            yield from extract_with_full_path(value, current_path)
        else:
            yield (current_path, value)

# Process all JSON files and compile translations
all_translations = {}
languages = []

for file_path in json_files_directory.glob('*.json'):
    lang = file_path.stem  # Assuming file name format is 'en.json', 'fr.json', etc.
    languages.append(lang)
    data = load_json_data(file_path)
    all_translations[lang] = dict(extract_with_full_path(data))

# Ensure 'en' is the second column
languages = sorted(languages)
languages.insert(0, languages.pop(languages.index('en')))

# Collect all unique keys
all_keys = set()
for translations in all_translations.values():
    all_keys.update(translations.keys())

# Write to CSV
with output_csv_file.open('w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow(['key'] + languages)
    # Write rows
    for key in sorted(all_keys):
        row = [key] + [all_translations[lang].get(key, "") for lang in languages]
        writer.writerow(row)

print(f"CSV file has been created at {output_csv_file}")
