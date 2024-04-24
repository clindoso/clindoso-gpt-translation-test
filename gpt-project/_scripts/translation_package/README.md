---
title: Docs
---

Export your OPENAI_API_KEY. Then, use this Python package with the following commands in the `translation_package` directory:

- For translating Help Center articles:

```
python cli.py translate {source article path} --lang {language code}
```

- For aligning a translation memory based on the Help Center articles:

```
python cli.py align --lang {language code}
```

`--lang` is optional. The default value is `nl`, i.e. Dutch.
