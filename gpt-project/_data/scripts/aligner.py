import os
import csv

# Read and return file content in a list
def read_and_split_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        return f"Error reading {file_path}: {e}"

# Export to CSV
def write_to_csv(file1_lines, file2_lines, base_directory_en, output_filename):
    os.makedirs(base_directory_en, exist_ok=True)
    output_filepath = os.path.join(base_directory_en, output_filename)
    
    with open(output_filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['EN', 'DE', 'File'])

        if len(file1_lines) == len(file2_lines):
            for line1, line2 in zip(file1_lines, file2_lines):
                writer.writerow([line1, line2, output_filename])
                print(output_filepath)
        else:
            print("Files do not have the same amount of lines.")

# Extract file contents
def extract_file_contents(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path_en = os.path.join(root, file)
            file_path_es = file_path_en.replace("_en", "_es")
            if os.path.exists(file_path_es):
                file_content_en = read_and_split_file(file_path_en)
                file_content_es = read_and_split_file(file_path_es)
                write_to_csv(file_content_en, file_content_es, root, file)

extract_file_contents("/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/_en/")
