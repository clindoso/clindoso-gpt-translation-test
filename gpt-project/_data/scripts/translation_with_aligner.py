import os
from openai import OpenAI
import argparse
import time
import csv
import Levenshtein as lev

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
    "nl": {"language": "Dutch", "model": "ft:gpt-3.5-turbo-1106:personal::8SkFElMK", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-nl.csv"}
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
        {"role": "system", "content": f"Translate only the sentence after the colon below into {language} keeping the style, tone, formatting, and terminology consistent and provide strictly just the translation."},
        {"role": "user", "content": segment}
      ]
    )
    print(segment)
    translated_segment = response.choices[0].message.content
    return translated_segment


# Text input

source_text = read_file(args.source)

# Split text into lines
split_source_text = source_text.splitlines()

# Initialize an empty list to store translated lines
translated_lines = []
# Initialize an empty dictionary to store GPT translations for repetitions
gpt_translated_dict = {}

# Read the TM and extract the 'en' column and the translation
tm_dict = {}
with open(tm_path, 'r', encoding='utf-8') as tm:
    reader = csv.DictReader(tm)
    for row in reader:
        if args.lang in row:
            tm_dict[row['en']] = row[args.lang]
        else:
            print(f"Column '{args.lang}' does not exist in the TM.")

# Flag to check if we are inside the frontmatter
in_frontmatter = False
tm_lines_lengths = {tm_line:len(tm_line) for tm_line in tm_dict}

# Loop through each line of the source text
for line in split_source_text:

    # Check if line is the start or end of the frontmatter
    if line == '---':
        translated_lines.append((line, line))
        in_frontmatter = not in_frontmatter
        continue
    
    # Reproduce frontmatter in the translation
    if in_frontmatter:
        translated_lines.append((line, line))
        continue
        
    # Check for existing translation in TM
    elif line in tm_dict:
        translated_lines.append((line, tm_dict[line] + " <!-- TM 100 -->"))
        continue

    # Check for existing ChatGPT translation
    elif line in gpt_translated_dict:
        translated_lines.append((line, gpt_translated_dict[line]))
        continue
    else:
        # Find closest line in TM
        lower_threshold = 0.05
        upper_threshold = 0.4
        closest_line, min_distance = None, float('inf')
        line_length = len(line)

        # Iterate through the TM segments
        for tm_line, tm_line_length in tm_lines_lengths.items():
            # If the length difference is too large, skip calculation
            if abs(line_length - tm_line_length) / max(line_length, tm_line_length) > upper_threshold:
                continue

            # Calculate Levenshtein distance and normalize it
            distance = lev.distance(line, tm_line)
            normalized_distance = distance / max(line_length, tm_line_length)

            # Update closest match if a closer one is found
            if normalized_distance < min_distance:
                closest_line, min_distance = tm_line, normalized_distance
            
            # Early exit if a sufficiently closed match is found
            if normalized_distance < lower_threshold:
                break

        # If the smallest distance is below the threshold (0.4 in this case)
        if min_distance < upper_threshold:
            fuzzy_match_score = (1 - min_distance)
            translated_lines.append((line, tm_dict[closest_line] + f" <!-- TM {fuzzy_match_score*100:.0f} -->"))
            

    
    if line in tm_dict:
        print(tm_dict[line])
    
    # Use existing translation if line was previously translated by GPT
    elif line in gpt_translated_dict:
        print(gpt_translated_dict[line])
    
    # Use existing translation if line is not in TM or was not previously translated by GPT
    else:
        translated_line = translate_segment(line, language, gpt_model)
        print(translated_line)
        gpt_translated_dict[line] = translated_line
        translated_lines.append((line, translated_line + " <!-- GPT translation -->"))


# You can change this part if you need the output in a different format (like a list)
translated_text = [target_lines for _, target_lines in translated_lines]
# Join the translated lines into a single string
joint_translated_text = "\n\n".join(translated_text)

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
    output_file_handle.write(joint_translated_text)

# Print elapsed time
print(f"Script time: {elapsed_time} minutes")

# Print output file path
print(f"Translation written to {output_file_path}")