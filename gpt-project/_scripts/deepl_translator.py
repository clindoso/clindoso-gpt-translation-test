# This files contains functions related to DeepL's API object Translator

import deepl
import config

def initialize_translator():
    """
    Initializes a DeepL translator instance.

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

def translate_with_deepl(translator, segment, previous_segment, lang, glossary, source_lang='en'):
    """
    Translates a text segment using the DeepL translator.

    This function translates a given text segment into the target language using a provided DeepL
    translator instance. It supports context from a previous segment and the use of a glossary.

    Parameters:
        translator (deepl.Translator): The DeepL translator object.
        segment (str): The current text segment to be translated.
        previous_segment (str): The previous text segment for providing context.
        lang (str): The target language code.
        glossary (deepl.Glossary): The glossary to be used during translation.
        source_lang (str, optional): The source language code, default is 'en'.

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
    glossary=glossary,
    context=previous_segment,
    ignore_tags=''
    )
    
    result_wg = translator.translate_text(
    segment,
    source_lang=source_lang,
    target_lang=lang,
    split_sentences='nonewlines',
    preserve_formatting=True,
    formality='less',
    context=previous_segment,
    ignore_tags=''
    )

    segment_translation = result.text
    segment_translation_wg = result_wg.text

    print(f"------------------\nDeepL comparison\nWith glossary:\n{segment_translation}\n\nWithout glossary:\n{segment_translation_wg}\n\n-----------------")

    translated_segment = segment_translation + " <!-- DeepL translation -->"

    return translated_segment, segment_translation

def initialize_deepl_glossary(translator, lang):
    if not config.GLOSSARY_IDS[lang]:
        raise EnvironmentError("")
    glossary = translator.get_glossary(config.GLOSSARY_IDS[lang])
    return glossary

def retrieve_deepl_glossary(translator, lang):
    """
    Retrieves the specified DeepL glossary for a given language.

    This function lists all available glossaries and retrieves the entries
    for the glossary that matches the specified language pair (en-target language).

    Parameters:
        translator (deepl.Translator): The DeepL translator object.
        lang (str): The target language code.

    Returns:
        str: The ID of the retrieved glossary.
    """
    glossaries = translator.list_glossaries()
    for glossary in glossaries:
        print(glossary.name)
        print(glossary.glossary_id)
        if glossary.name == f"Termbase en-{lang}":
            print(glossary.name)
            print(glossary.glossary_id)
            glossary_id = glossary.glossary_id
            my_glossary = glossary_id
            entries = translator.get_glossary_entries(glossary)
    print(f"Termbase:\n------------------\nEN - {lang.upper()}")
    for k, v in entries.items():
        print(f"{k} - {v}")

    return my_glossary