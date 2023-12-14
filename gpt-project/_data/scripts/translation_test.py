import os
from openai import OpenAI
import argparse
import time

# Use this script to translate whole articles from English into German, Spanish, French, Italian, or Dutch with ChatGPT.
# The script takes two arguments, --lang and--source, respectively the target language and the source file to be translated.

# Set the OpenAI API key from the environment variable
client = OpenAI(
    api_key = os.environ.get("OPEN_API_KEY")
)

# Start time tracker
start_time = time.time()

# Create argument parser
argparser = argparse.ArgumentParser(description="Script to translate texts from English to German, Spanish, French, Italian, or Dutch using ChatGPT")

# Define arguments
argparser.add_argument("--lang")
argparser.add_argument("--source")

# Parse arguments
args = argparser.parse_args()

# Define language name and language-specific fine-tuned model
language_models = {
    # "de": {"language": "German", "model": ""},
    "es": {"language": "Spanish", "model": "ft:gpt-3.5-turbo-1106:personal::8SkFElMK"},
    # "fr": {"language": "French", "model": ""},
    # "it": {"language": "Italian", "model": ""},
    "nl": {"language": "Dutch", "model": "ft:gpt-3.5-turbo-1106:personal::8VcQ6Dhp"}
}

# Conditional for language-specific arguments

if args.lang in language_models:
    language = language_models[args.lang]["language"]
    gpt_model = language_models[args.lang].get("model", "")
else:
    print("This is not a valid language")


# Extract source file path
source_directory = os.path.dirname(args.source)

# Function to read and return the content of a file
def read_file(source):
    with open(source, 'r', encoding='utf-8') as file:
        return file.read()
    

# Text input

text = read_file(args.source).replace('\n', '\\n')

# Make a request to the OpenAI API
response = client.chat.completions.create(
  model=gpt_model,
  messages=[
    {"role": "system", "content": f"Given a Markdown file in English with Kramdown tags, translate it into {language} keeping the style, tone, formatting, and terminology consistent. Provide the translation in a Markdown file."},
    {"role": "user", "content": text}
  ]
)

# End time tracker
elapsed_time = round(((time.time() - start_time) / 60), 2)

# Extract response content
translated_content = response.choices[0].message.content
md_translated_content = translated_content.replace("\\n", "\n")

output_file = "translated_output.md"
output_path = os.path.join(os.path.dirname(source_directory), output_file)

# Write the translated content to the output file
with open(output_path, 'w', encoding='utf-8') as output_path:
    output_path.write(md_translated_content)

# Print elapsed time
print(f"Script time: {elapsed_time} minutes")

# Print output file path
print(f"Translation written to {output_path}")