import os

# Config file for WTI segment scraper
LOCALE_REPOS_DIR = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_wti_scripts/repos"

# OpenAI API key
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Prompt for training data
PROMPT = "As a professional translator, your task is to translate the provided Markdown text to {language} while preserving the style, tone, Markdown format, structure, and terminology. Do not translate the Markdown syntax, file paths, or any text that should remain unchanged. If parts of the text are already in the target language or are global shorthand, keep them without any explanation."

LANGUAGE_DATA = {
    "de": {"language": "German", "tm_path": "../_docs/tm/en-de.csv"},
    "es": {"language": "Spanish", "tm_path": "../_docs/tm/en-es.csv"},
    "fr": {"language": "French", "tm_path": "../_docs/tm/en-fr.csv"},
    "it": {"language": "Italian", "tm_path": "../_docs/tm/en-it.csv"},
    "nl": {"language": "Dutch", "tm_path": "../_docs/tm/en-nl.csv"}
}