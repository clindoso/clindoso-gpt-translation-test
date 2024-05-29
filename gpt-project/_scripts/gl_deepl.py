import deepl
import config
from term_scraper import extract_terms_from_directory
from deepl_translator import initialize_translator

def dictify_terms(termbase_directory, lang):
    term_tuples = extract_terms_from_directory(termbase_directory, lang)
    return {term_tuple[1]: term_tuple[2] for term_tuple in term_tuples}

def create_glossary(translator, term_dict, target_lang, source_lang='en'):
    glossary = translator.create_glossary(
        f"Termbase {source_lang}-{target_lang}",
        source_lang=source_lang,
        target_lang=target_lang,
        entries=term_dict
    )
    print(
    f"Created '{glossary.name}' ({glossary.glossary_id}) "
    f"{glossary.source_lang}->{glossary.target_lang} "
    f"containing {glossary.entry_count} entries"
    )

    return glossary

def main():
    # Initialize termbase directory
    if not config.TERMBASE_DIRECTORY:
        raise EnvironmentError("The termbase directory is not set in the config file. Set the termbase directory.")
    else:
        termbase_directory = config.TERMBASE_DIRECTORY

    # Initialize DeepL translator
    translator = initialize_translator()

    # Initialize list with target languages
    target_langs = ['de', 'es', 'fr', 'it', 'nl']

    # Create one glossary per target language
    for lang in target_langs:
        term_dict = dictify_terms(termbase_directory, lang)
        create_glossary(translator, term_dict, lang)
        

if __name__ == "__main__":
    main()