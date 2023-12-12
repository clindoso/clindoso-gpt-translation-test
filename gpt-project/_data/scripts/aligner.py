import os

# Read and return file content
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading {file_path}: {e}"

# Extract file contents
def extract_file_contents(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path_en = os.path.join(root, file)
            file_path_es = file_path_en.replace("_en", "_es")
            if os.path.exists(file_path_es):
                file_content_en = read_file(file_path_en)
                file_content_es = read_file(file_path_es)

extract_file_contents("/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_data")