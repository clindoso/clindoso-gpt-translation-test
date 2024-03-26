from openai import OpenAI
from nl_translation_package.config import OPENAI_API_KEY

class OpenAIClient:
    def __init__(self):
        self.client = self.initialize_client()

    @staticmethod
    def initialize_client():
        if not OPENAI_API_KEY:
            raise EnvironmentError("OPENAI_API_KEY not found.")
        return OpenAI(api_key=OPENAI_API_KEY)
