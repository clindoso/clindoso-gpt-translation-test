import os
from openai import OpenAI
import argparse
import time

# Use this script to translate whole articles from English to Spanish with ChatGPT.
# The script takes the argument --source_path, i.e. the source file to be translated.

# Set the OpenAI API key from the environment variable
client = OpenAI(
    api_key = os.environ.get("OPEN_API_KEY")
)

# Start time tracker
start_time = time.time()

# Create argument parser
argparser = argparse.ArgumentParser(description="Script to translate texts from English to Spanish using ChatGPT")

# Define arguments
argparser.add_argument("--source_path")

# Parse arguments
args = argparser.parse_args()

# Extract source file path
source_directory = os.path.dirname(args.source_path)

# Function to read and return the content of a file
def read_file(source_path):
    with open(source_path, 'r', encoding='utf-8') as file:
        return file.read()
    

# Text input

text = read_file(args.source_path).replace('\n', '\\n')

# Make a request to the OpenAI API
response = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-1106:personal::8SkFElMK",  # Change to a valid model name
  messages=[
    {"role": "system", "content": "Given a Markdown file in English with Kramdown tags, translate it into Spanish keeping the style, tone, formatting, and terminology consistent. Provide the translation in a Markdown file."},
    {"role": "user", "content": text}
  ]
)

# End time tracker
elapsed_time = round(((time.time() - start_time) / 60), 2)

# Extract response content
translated_content = response.choices[0].message.content
md_translated_content = translated_content.replace("\\n", "\n")

output_file = "translated_output.md"
output_path = os.path.join(os.path.dirname(source_directory), "es/", output_file)

# Write the translated content to the output file
with open(output_path, 'w', encoding='utf-8') as output_path:
    output_path.write(md_translated_content)

# Print elapsed time
print(f"Script time: {elapsed_time} minutes")

# Print output file path
print(f"Translation written to {output_file}")