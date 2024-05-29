import os

# OpenAI API key
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# DeepL API key
DEEPL_API_KEY = os.environ.get("DEEPL_API_KEY")

# Language models
LANGUAGE_MODELS = {
    "de": {"language": "German", "gpt-model": "", "tm_path": "../_docs/tm/en-de.csv", "target_spacy_model": "de_core_news_sm"},
    "es": {"language": "Spanish", "gpt-model": "ft:gpt-3.5-turbo-1106:personal::8kULYOWh", "tm_path": "../_docs/tm/en-es.csv", "target_spacy_model": "es_core_news_sm"},
    "fr": {"language": "French", "gpt-model": "", "tm_path": "../_docs/tm/en-fr.csv", "target_spacy_model": "fr_core_news_sm"},
    "it": {"language": "Italian", "gpt-model": "ft:gpt-3.5-turbo-0125:personal::9HTP3fRe", "tm_path": "../_docs/tm/en-it.csv", "target_spacy_model": "it_core_news_sm"},
    "nl": {"language": "Dutch", "gpt-model": "ft:gpt-3.5-turbo-0125:personal:nl-29-02-2024:8xZPaq6n", "tm_path": "../_docs/tm/en-nl.csv", "target_spacy_model": "nl_core_news_sm"}
}

# GPT prompts
PROMPT = "As a professional translator, your task is to translate the provided Markdown text to {language} while preserving the style, tone, Markdown format, structure, and terminology. Do not translate the Markdown syntax, file paths, or any text that should remain unchanged. If parts of the text are already in the target language or are global shorthand, keep them without any explanation."
PROMPT_WITH_PREVIOUS_SENTENCE = "As a professional translator, your task is to translate the provided Markdown text to {language} while preserving the style, tone, Markdown format, structure, and terminology. Do not translate the Markdown syntax, file paths, or any text that should remain unchanged. If parts of the text are already in the target language or are global shorthand, keep them without any explanation. For context, consider that the sentence preceding the text you will translate is: '{previous_segment}'"
# Set temperature for GPT text generation
GPT_TEMPERATURE = 1.0

# Fuzzy matching thresholds
LOWER_THRESHOLD = 0.05
UPPER_THRESHOLD = 0.4

# EN docs directory
DOCS_DIRECTORY = "../_docs/_en/"

# Termbase directory
TERMBASE_DIRECTORY = "../_data/terminology"

# TM directory
TRANSLATION_MEMORY_DIRECTORY = "../_docs/tm/"

# Front matter processing variables
FRONT_MATTER_VARIABLES = ['title: ', 'description: ']
GPT_TRANSLATION_MARKER = ('gpt_translation: true', 'gpt_translation: true')
DEEPL_MARKER = ('deepl_translation: true', 'deepl_translation: true')

# Tag patterns
tag_patterns = [
    r'\*\*',
    r'\_\_',
    r'_\b',
    r'\b_'
]
