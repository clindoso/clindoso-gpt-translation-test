import deepl
import config

def initialize_translator():
    """
    Initialize a DeepL translator instance.

    This function checks if the DeepL API key is set in the configuration file.
    If the API key is not defined, it raises an EnvironmentError with instructions
    on how to set the API key. If the API key is defined, it returns a DeepL 
    Translator instance.

    Raises:
        EnvironmentError: If the DeepL API key is not defined in the config file.

    Returns:
        deepl.Translator: An instance of the DeepL Translator initialized with the API key.
    """
    if not config.DEEPL_API_KEY:
        raise EnvironmentError("DeepL API key is not defined in the config file. Export the DeepL API key using the terminal command `export DEEPL_API_KEY='<DEEPL_API_KEY>'`.")
    else:
        return deepl.Translator(auth_key=config.DEEPL_API_KEY)
    
def translate_with_deepl(translator, segment, previous_segment, lang, source_lang='en'):
    """
    Translates a text segment using the DeepL translator.

    Parameters:
        translator (deepl.Translator): The DeepL translator object.
        segment (str): The current text segment to be translated.
        previous_segment (str): The previous text segment for providing context.
        lang (str): The target language code.
        source_lang (str, optional): The source language code, default is 'en-us'.

    Returns:
        tuple: A tuple containing the translated segment with a DeepL marker and the raw translation.
    """

    result = translator.translate_text(
    segment,
    source_lang=source_lang,
    target_lang=lang,
    split_sentences='nonewlines',
    preserve_formatting=True,
    formality='less',
    glossary=config.GLOSSARY[lang],
    context=previous_segment,
    ignore_tags=''
    )
    
    print(result)
    segment_translation = result.text

    translated_segment = segment_translation + " <!-- DeepL translation -->"

    return translated_segment, segment_translation