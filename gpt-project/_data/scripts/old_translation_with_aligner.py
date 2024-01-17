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
    api_key = os.environ.get("OPENAI_API_KEY")
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

# Check if language is supported

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

# Check if source path exists

if not os.path.exists(args.source):
    print(" This is not a valid source text file.")

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
        {"role": "system", "content": f"Given a sentence in Markdown format, translate the sentence to {language} keeping the style, tone, formatting, and terminology consistent and provide strictly just the translation."},
        {"role": "user", "content": segment}
      ]
    )
    print(segment + " this is the segment")
    translated_segment = response.choices[0].message.content
    return translated_segment


# Text input

source_text = read_file(args.source)

# Split text into segmetns
split_source_text = source_text.splitlines()

# Initialize an empty list to store translated segments
translated_segments = []

# Initialize an empty dictionary to store GPT translations for repetitions
gpt_translation_dict = {}

# Read the TM and extract the 'en' column and the translation
tm_dict = {}
with open(tm_path, 'r', encoding='utf-8') as tm:
    reader = csv.DictReader(tm)
    for row in reader:
        tm_dict[row['en']] = row[args.lang]

# Flag to check if we are inside the frontmatter
in_frontmatter = False
tm_segments_lengths = {tm_segment:len(tm_segment) for tm_segment in tm_dict}

# Loop through each segment of the source text
for segment in split_source_text:

    # Check if segment is the start or end of the frontmatter
    if segment == '---':
        translated_segments.append((segment, segment))
        in_frontmatter = not in_frontmatter
        continue
    
    # Reproduce frontmatter in the translation
    if in_frontmatter:
        translated_segments.append((segment, segment))
        continue

    # Ignore commented out segments
    elif segment.startswith("<!--"):
        translated_segments.append((segment, segment))
        continue
        
    # Check for existing translation in TM
    elif segment in tm_dict:
        translated_segments.append((segment, tm_dict[segment] + " <!-- TM 100 -->"))
        continue

    # Check for existing ChatGPT translation
    elif segment in gpt_translation_dict:
        translated_segments.append((segment, gpt_translation_dict[segment] + " <!-- Repetition of GPT translation -->"))
        continue
    
    elif segment == '':
        translated_segments.append((segment, segment))
        continue

    else:
        # Find closest segment in TM
        lower_threshold = 0.05
        upper_threshold = 0.4
        closest_segment, min_distance = None, float('inf')
        segment_length = len(segment)

        # Iterate through the TM segments
        for tm_segment, tm_segment_length in tm_segments_lengths.items():
            # If the length difference is too large, skip calculation
            if abs(segment_length - tm_segment_length) / max(segment_length, tm_segment_length) > upper_threshold:
                continue

            # Calculate Levenshtein distance and normalize it
            distance = lev.distance(segment, tm_segment)
            normalized_distance = distance / max(segment_length, tm_segment_length)

            # Update closest match if a closer one is found
            if normalized_distance < min_distance:
                closest_segment, min_distance = tm_segment, normalized_distance
            
            # Early exit if a sufficiently closed match is found
            if normalized_distance < lower_threshold:
                break

        # If the smallest distance is below the threshold (0.4 in this case), use content of TM
        if min_distance < upper_threshold:
            fuzzy_match_score = (1 - min_distance)
            translated_segments.append((segment, tm_dict[closest_segment] + f" <!-- TM {fuzzy_match_score*100:.0f} -->"))
        # If the smallest distance is above the threshold (0.4), translate via ChatGPT
        else:
            translated_segment = translate_segment(segment, language, gpt_model)
            print(translated_segment + " this is the translated_segment")
            gpt_translation_dict[segment] = translated_segment
            translated_segments.append((segment, translated_segment + " <!-- GPT translation -->"))
                
    if segment in tm_dict:
        print(tm_dict[segment] + " this is the tm_dict")
    
    # Use existing translation if segment was previously translated by GPT
    elif segment in gpt_translation_dict:
        print(gpt_translation_dict[segment] + " this is the gpt_translation_dict")


# Define function to extract translated frontmatter
def extract_translated_frontmatter(translated_segments):
    # Initialize to track beginning and end of frontmatter
    marker_found = False
    # Iterate through the segments of the translation
    for _, target_segments in translated_segments:
        if target_segments == "---":
            # Yield '---'
            yield target_segments
            if marker_found:
                return # End function when stop condition is met
            else:
                marker_found = True
                continue # Skip to next segment
        # Yield frontmatter content
        elif marker_found:
            yield target_segments

# Create list with translated frontmatter
translated_frontmatter = list(extract_translated_frontmatter(translated_segments))

# Join frontmatter in a string
joint_translated_frontmatter = "\n".join(translated_frontmatter)

# Define function extract translated text
def extract_translated_text(translated_segments):
    # Initialize marker count
    marker_count = 0
    for _, target_segments in translated_segments:
        # Ignore segments while the end of the frontmatter is not found
        if target_segments == "---":
            marker_count += 1
            if marker_count < 2:
                continue # Skip until the second '---' is found
        # Start yielding segments after second '---' is found
        if target_segments == "---" and marker_count >= 2:
            continue
        elif marker_count >= 2:
            yield target_segments

# Create list with translated content
translated_text = list(extract_translated_text(translated_segments))

# Join translated text in a string
joint_translated_text = "\n".join(translated_text)

# Join translated frontmatter and article

joint_translated_article = joint_translated_frontmatter + "\n" + joint_translated_text

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
    output_file_handle.write(joint_translated_article)

# Print elapsed time
print(f"Script time: {elapsed_time} minutes")

# Print output file path
print(f"Translation written to {output_file_path}")