# This file includes functions related to the GPT client
import config
from openai import OpenAI

def initialize_open_ai_client():
    """
    Initializes the OpenAI client using the API key from the config file.

    This function checks if the OpenAI API key is set in the configuration file.
    If the API key is not defined, it raises an EnvironmentError. If the API key is 
    defined, it returns an OpenAI client object.

    Returns:
        OpenAI: The OpenAI client object initialized with the API key.

    Raises:
        EnvironmentError: If the OpenAI API key is not found in the configuration file.
    """
    if not config.OPENAI_API_KEY:
        raise EnvironmentError("OPENAI_API_KEY environment variable not found.")
    return OpenAI(api_key=config.OPENAI_API_KEY)

def translate_with_gpt(client, segment, previous_segment, language, gpt_model, gpt_temperature=1.0):
    """
    Translates the segment using GPT.

    Parameters:
        client (OpenAI client object): The OpenAI client for API requests.
        segment (str): The current text segment.
        previous_segment (str): The previous text segment to help context-based translation.
        language (str): Target language code.
        gpt_model (str): The GPT model to use for translation.
        gpt_temperature (float, optional): The temperature setting for the GPT model, default is 1.0.

    Returns:
        tuple: A tuple containing the translated segment with a GPT marker and the raw GPT translation.
    """
    prompt = config.PROMPT.format(language=language)
    prompt_with_previous_sentence = config.PROMPT_WITH_PREVIOUS_SENTENCE.format(language=language, previous_segment=previous_segment)

    if previous_segment:

        response = client.chat.completions.create(
        model=gpt_model,
        temperature=gpt_temperature, 
        messages=[
            {"role": "system", "content": prompt_with_previous_sentence},
            {"role": "user", "content": segment}
          ]
        )
    
    else:
        response = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": segment}
          ]
        )
    
    gpt_translation = response.choices[0].message.content
    
    translated_segment = gpt_translation + " <!-- GPT translation -->"

    return translated_segment, gpt_translation