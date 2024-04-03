import os

# Env variables
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Language models
LANGUAGE_MODELS = {
    "de": {"language": "German", "gpt-model": "", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-de.csv"},
    "es": {"language": "Spanish", "gpt-model": "ft:gpt-3.5-turbo-1106:personal::8kULYOWh", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-es.csv"},
    "fr": {"language": "French", "gpt-model": "", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-fr.csv"},
    "it": {"language": "Italian", "gpt-model": "", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-it.csv"},
    "nl": {"language": "Dutch", "gpt-model": "ft:gpt-3.5-turbo-0125:personal:nl-29-02-2024:8xZPaq6n", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-nl.csv"}
}

SOURCE_LANGUAGE_SPACY_MODEL = "en_core_news_sm"

# Fuzzy matching thresholds
LOWER_THRESHOLD = 0.05
UPPER_THRESHOLD = 0.4

# EN docs directory
docs_directory = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/_en/"

# Termbase directory
TERMBASE_DIRECTORY = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_data/terminology"

# TM directory
translation_memory_directory = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/"

# Front matter processing variables
front_matter_variables = ['title: ', 'description: ']
gpt_translation_marker = ('gpt_translation: true', 'gpt_translation: true')

# Tag patterns
tag_patterns = [
    r'\*\*',
    r'\_\_',
    r'_\b',
    r'\b_'
]
