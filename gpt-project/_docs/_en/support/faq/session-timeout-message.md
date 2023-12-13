---
title: Session timeout message when accessing WFM
toc: false
description: Resolve the timeout issue that appears when you access WFM.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/browser-setup.md
---

In this article, you will learn how to resolve the timeout message when clicking the link to _WFM_{:.menu-item} in the navigation bar.

{{ 1 | image: 'Session Timeout', '50%' }}

## Correct your trusted sites configuration

There can be two reasons for this problem:

- The protected mode is activated for the trusted sites.
- The trusted sites entry is misconfigured.

To solve the issue, reconfigure your [trusted sites entry and security zone level](/browser-setup#configure-the-trusted-sites-and-security-zone-settings) in the internet options. Check if you have added the correct **\*.injixo.com** entry to the trusted sites.

## Check your browser bookmarks

Check if you are using an old browser bookmark to access injixo. Your bookmark may point to a page which no longer exists.

To solve this issue:

1. Open a new browser window or tab.
2. Navigate to [https://www.injixo.com/login](https://www.injixo.com/login).
3. Enter your credentials and navigate to the desired page.
4. Store *https://www.injixo.com/login* as a new bookmark.
