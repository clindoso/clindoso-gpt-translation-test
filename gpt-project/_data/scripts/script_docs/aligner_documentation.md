---
title: Documentation for `aligner.py`
---
## Overview
`aligner.py` is a Python script used for creating Translation Memory (TM) files in CSV format. The script aligns English source text with its translations in a specified target language.

## Requirements
- Python 3.x
- Access to a directory containing English text files

## Usage
To use `aligner.py`, run it from the command line with the required argument:
```
python aligner.py --lang [TARGET_LANGUAGE]
```
Replace `[TARGET_LANGUAGE]` with the desired target language code (e.g., 'es' for Spanish).

## Functionality
- **Argument Parsing**: Parses the command-line argument `--lang` to determine the target language.
- **File Processing**: Reads English text files from a specified source directory.
- **CSV Creation**: Generates a CSV file where each row contains a snippet of English text and its corresponding translation in the target language.

## Example
```
python aligner.py --lang fr
```
This command will process English text files and create a French translation memory in CSV format.
