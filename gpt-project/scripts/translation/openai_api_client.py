from openai import OpenAI
import config

class OpenAIClient:
    def __init__(self):
        self.client = self.initialize_client()

    @staticmethod
    def initialize_client():
        if not config.OPENAI_API_KEY:
            raise EnvironmentError("OPENAI_API_KEY not found.")
        return OpenAI(api_key=config.OPENAI_API_KEY)

    def translate_segment(self, segment, language, gpt_model):
        # Implementation for translating a segment
        pass

def translate_with_gpt(client, segment, language, gpt_model, previous_segment=''):
    """
    Translates the segment using GPT.

    Parameters:
        client (OpenAI client object): The OpenAI client for API requests.
        segment (str): The current text segment.
        language (str): Target language code.
        gpt_model (str): The GPT model to use for translation.

    Returns:
        str: The translated segment.
    """

    if previous_segment:

        response = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": f"Given a sentence in Markdown format, translate the sentence to {language} keeping the style, tone, formatting, and terminology consistent and provide strictly just the translation in plain language. For context, consider that the sentence preceding the one you will translate is: '{previous_segment}'"},
            {"role": "user", "content": segment}
          ]
        )
    
    else:
        response = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": f"Given a sentence in Markdown format, translate the sentence to {language} keeping the style, tone, formatting, and terminology consistent and provide strictly just the translation in plain language."},
            {"role": "user", "content": segment}
          ]
        )
    
    translated_segment = response.choices[0].message.content

    # Tokenize {segment} and check if any of the tokens is in the tokens dictionary
    # If they are, check if the correspondent in the target language is in the {translated segment}
    # If it is not, prompt model to rephrase the {translated segment} based on the target language token

    return translated_segment