# main.py
import argparse
import sys
import time
from .openai_api_client import OpenAIClient
from .translation import translate_article, initialize_translation_memory, initialize_language_model
from .utils import load_source_file_segments, write_translated_file, extract_translated_text
from .config import termbase_directory, LANGUAGE_MODELS

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Script to translate texts using TM and ChatGPT")
    parser.add_argument("--source", required=True, help="Source file for translation")
    parser.add_argument("--lang", required=False, help="Target language for translation", default="nl")
    args = parser.parse_args()
    source, lang = args.source, args.lang

    try:
        # Initialize OpenAI client
        client = OpenAIClient.initialize_client()

        # Load source file segments
        source_text = load_source_file_segments(source)
        if source_text is None:
            print("Source file not found or empty.")
            sys.exit(1)

        # Check for termbase directory in config
        #if not termbase_directory:
        #    print("Termbase directory not defined in the config file.")
        #    sys.exit(1)

        # Initialize language models, translation memory, and termbase
        language, gpt_model, tm_path = initialize_language_model(lang)
        tm_dict = initialize_translation_memory(lang, tm_path)

        # Translate the article
        translated_segments = translate_article(client, language, source_text, tm_dict, gpt_model)
        translated_text = extract_translated_text(translated_segments)

        # Save the translated file
        write_translated_file(lang, source, translated_text)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
