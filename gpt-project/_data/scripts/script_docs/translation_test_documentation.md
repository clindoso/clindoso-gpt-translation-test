---
title: Documentation for `translation_test.py`
---

## Overview
`translation_test.py` is a script for translating entire articles from English to a specified target language using OpenAI's ChatGPT.

## Requirements
- Python 3.x
- `openai` Python package
- An OpenAI API key set as an environment variable

## Usage
The script requires two command-line arguments: `--lang` for the target language and `--source` for the source file path.
```
python translation_test.py --lang [TARGET_LANGUAGE] --source [FILE_PATH]
```

## Functionality
- **OpenAI API Integration**: Uses the OpenAI API for translation tasks.
- **Argument Parsing**: Parses `--lang` and `--source` arguments for language selection and source file specification.
- **Translation**: Translates the content of the specified file from English to the target language.
- **Time Tracking**: Measures the duration of the translation process.

## Example
```
python translation_test.py --lang de --source ./example.txt
```
This command translates the content of `example.txt` from English to German.
