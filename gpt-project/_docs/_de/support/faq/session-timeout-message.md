---
title: Timeout-Meldung beim Zugriff auf den WFM-Bereich
toc: false
description: Behebe das Timeout-Problem, das beim Zugriff auf den WFM-Bereich angezeigt wird.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/browser-setup.md
---

In diesem Artikel lernst Du, was Du tun kannst, wenn bei einem Klick auf _WFM_{:.menu-item} in der Navigationsleiste eine Timeout-Meldung erscheint.

{{ 1 | image: 'Session Timeout', '40%' }}

## Ursache 1: Der geschützte Modus im Internet Explorer ist aktiviert

- Konfiguriere die {% link_new vertrauenswürdigen Seiten | getting-started/browser-setup.md %} im Internet Explorer neu.
- Füge **\*.injixo.com** hinzu, nicht nur *www.injixo.com*.

## Ursache 2: Ein altes Internet Explorer-Lesezeichen wird genutzt, um auf injixo zuzugreifen ...

... das auf eine Seite zeigt, die nicht mehr existiert.

1. Verwende ein neues Internet Explorer-Fenster oder einen neuen Tab.
2. Navigiere zu [https://www.injixo.com/login](https://www.injixo.com/login).
3. Gib dort Deine Anmeldedaten ein und navigiere zur gewünschten Seite.

Speichere *https://www.injixo.com/login* bei Bedarf als neues Lesezeichen.
