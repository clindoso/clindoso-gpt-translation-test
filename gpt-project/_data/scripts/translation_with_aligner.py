import os
from openai import OpenAI
import argparse
import time
import csv

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
    # "de": {"language": "German", "model": "", "tm": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-de.csv"},
    "es": {"language": "Spanish", "model": "ft:gpt-3.5-turbo-1106:personal::8SkFElMK", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-es.csv"},
    # "fr": {"language": "French", "model": "", "tm": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-fr.csv"},
    # "it": {"language": "Italian", "model": "", "tm": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-it.csv"},
    "nl": {"language": "Dutch", "model": "ft:gpt-3.5-turbo-1106:personal::8VcQ6Dhp", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-nl.csv"}
}

# Conditional for language-specific arguments

if args.lang in language_models:
    language = language_models[args.lang]["language"]
    gpt_model = language_models[args.lang].get("model", "")
    tm_path = language_models[args.lang]["tm_path"]
else:
    print("""
          You typed an invalid language abbreviation. Use the following:
          "de" for German
          "es" for Spanish
          "fr" for French
          "it" for Italian
          "nl" for Dutch
    """)

# Conditional for source path

if not os.path.exists(args.source):
    print("This is not a valid source text file.")

# Extract source file path
source_directory = os.path.dirname(args.source)

# Function to read and return the content of a file
def read_file(source):
    with open(source, 'r', encoding='utf-8') as file:
        return file.read()
    
# Function to translate segment
def translate_segment(segment, language, gpt_model):
    response = client.chat.completions.create(
      model=gpt_model,
      messages=[
        {"role": "system", "content": f"Given a Markdown file in English with Kramdown tags, translate it into {language} keeping the style, tone, formatting, and terminology consistent. Provide the translation in a Markdown file."},
        {"role": "user", "content": segment}
      ]
    )

    translated_segment = response.choices[0].message.content
    return translated_segment


# Text input

text = read_file(args.source)

# Split text into lines
lines = text.splitlines()

# Initialize an empty list to store translated lines
translated_lines = []

# Read the TM and extract the 'en' column and the translation
tm_dict = {}
with open(tm_path, 'r', encoding='utf-8') as tm:
    reader = csv.DictReader(tm)
    for row in reader:
        if args.lang in row:
            tm_dict[row['en']] = row[args.lang]
        else:
            print(f"Column '{args,lang}' does not exist in the TM.")

# Iterate over each line and translate
for line in lines:
    if line in tm_dict:
        # Use TM suggestion
        translated_lines.append(tm_dict[line])
    else:
        translated_line = translate_segment(line, language, gpt_model)
        translated_lines.append(translated_line)

# Join the translated lines into a single string
# You can change this part if you need the output in a different format (like a list)
translated_text = "\n".join(translated_lines)

# Now `translated_text` contains the whole translated content

# End time tracker
elapsed_time = round(((time.time() - start_time) / 60), 2)

# Define output file name and path
output_file = args.source.split('/')[-1]
output_directory = os.path.join(source_directory, f"{language}_translation_output/")
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
output_file_path = os.path.join(output_directory, output_file)

# Write the translated content to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file_handle:
    output_file_handle.write(translated_text)

# Print elapsed time
print(f"Script time: {elapsed_time} minutes")

# Print output file path
print(f"Translation written to {output_file_path}")