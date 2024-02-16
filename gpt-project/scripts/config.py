import os

# Env variables
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Language models
LANGUAGE_MODELS = {
    "de": {"language": "German", "gpt-model": "", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-de.csv"},
    "es": {"language": "Spanish", "gpt-model": "ft:gpt-3.5-turbo-1106:personal::8SkFElMK", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-es.csv"},
    "fr": {"language": "French", "gpt-model": "", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-fr.csv"},
    "it": {"language": "Italian", "gpt-model": "", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-it.csv"},
    "nl": {"language": "Dutch", "gpt-model": "ft:gpt-3.5-turbo-1106:personal::8f4GFKBA", "tm_path": "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/tm/en-nl.csv"}
}

# Fuzzy matching thresholds
LOWER_THRESHOLD = 0.05
UPPER_THRESHOLD = 0.4

# EN docs directory
docs_directory = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_docs/_en/"

# Termbase directory
termbase_directory = "/Users/caio.lopes/Documents/GitHub/clindoso/gpt-project/_data/terminology"