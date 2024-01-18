---
title: Documentation for `prompt_scraper.py`
---

## Overview
`prompt_scraper.py` is designed to process articles and convert them into prompts suitable for OpenAI's language models. It supports specifying a target language for the prompts.

## Requirements
- Python 3.x
- `sklearn` library
- Access to a directory with article data

## Usage
Run the script with the optional `--lang` argument to set the target language:
```
python prompt_scraper.py --lang [LANGUAGE_CODE]
```
If no language is specified, a default may be used.

## Functionality
- **Argument Parsing**: Allows the user to specify the target language for the prompts.
- **Article Reading**: Reads articles from a predefined base directory.
- **Prompt Conversion**: Converts the articles into a format suitable as prompts for OpenAI's API.
- **Data Splitting**: Splits the data into training and testing sets.

## Example
```
python prompt_scraper.py --lang en
```
This command processes articles into English prompts for OpenAI's models.
