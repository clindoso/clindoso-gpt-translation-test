---
title: Tagestypen erstellen und verwenden
description: Erstelle Tagestypen, um Feiertage und andere besondere Tage abzubilden, die sich auf deine Öffnungszeiten auswirken.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/configure-planning-calendars.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/scheduling-public-holidays.md
---

Tagestypen definieren Tage mit den üblichen Öffnungszeiten und Tage mit abweichenden Öffnungszeiten.

Füge deiner {% link_new Planungseinheit | features/administration/create-and-manage-planning-units.md | #öffnungszeiten-hinzufügen %} Tagestypen hinzu, um die Öffnungszeiten für die wöchentlichen Standardtage und für besondere Tage festzulegen, z.&nbsp;B. wenn dein Unternehmen an Feiertagen geöffnet ist. injixo berücksichtigt die festgelegten Öffnungszeiten für diese Tage bei der Schichtplanoptimierung.

In _Plan > Konfiguration > Tagestypen_{:.breadcrumbs} kannst du folgendes tun:

- Die Standard-Tagestypen einsehen.
- Benutzerdefinierte Tagestypen erstellen, bearbeiten und löschen.

## Benutzerdefinierte Tagestypen erstellen

An manchen Tagen kann es sein, dass die Öffnungszeiten deines Unternehmens von den üblichen Öffnungszeiten abweichen, z.&nbsp;B. bei einer besonderen Werbeaktion oder an Feiertagen. Um benutzerdefinierte Tagestypen für diese Tage zu erstellen, gehe wie folgt vor:

1. Klicke oben links in der Aktionsleiste auf das Neu-Icon {% icon item-add | icon-only %}.
2. Gib einen **Namen** ein (max. 50 Zeichen).
3. Gib eine **Kurzbezeichnung** (max. 25 Zeichen) ein.  
   Die Kurzbezeichnung wird im Planungskalender angezeigt.
4. (Optional) Aktiviere die Checkbox **Feiertagsmodus**.<br>[Erfahre mehr](#feiertagsmodus) darüber, wie du Tagestypen für Feiertage konfigurierst.
5. Klicke auf _OK_{:.doc-button}.

## Feiertagsmodus

Um einen Tagestyp als Feiertag zu kennzeichnen, aktiviere die Checkbox **Feiertagsmodus** im Konfigurationsfenster für den Tagestyp.

### Tagestypen für Feiertage erstellen

Es gibt zwei Möglichkeiten, Tagestypen für Feiertage zu erstellen:

- Erstelle Tagestypen mit dem Feiertagsmodus und {% link_new füge sie deinem Planungskalender hinzu | features/administration/configure-planning-calendars.md | #planungskalender-konfigurieren %}.

- Füge deinem Planungskalender eine {% link_new Kalendervorlage | features/administration/configure-planning-calendars.md | #planungskalender-konfigurieren %} hinzu. Damit werden automatisch alle enthaltenen Tagestypen für Feiertage mit aktiviertem Feiertagsmodus erstellt.

Im Feiertagsmodus werden die Arbeitsstunden der Mitarbeiter an diesem Tag entsprechend reduziert. Wenn du diesen Tag als normalen Arbeitstag planen möchtest, kannst du den Feiertagsmodus jederzeit deaktivieren, indem du den {% link_new Tagestyp bearbeitest | features/administration/day-types.md | #tagestypen-bearbeiten %}.

## Tagestypen bearbeiten

> Achtung
>
> Wenn du den Feiertagsmodus eines aktuell verwendeten Tagestyps änderst, musst du die Zeitkonten bzw. {% link_new Richtzeitkonten | features/scheduling/planning-periods/target-work-accounts.md %} neu berechnen.

1. Wähle einen Tagestyp aus der Liste aus.
2. Führe deine Änderungen durch.
3. Klicke auf _OK_{:.doc-button}.

## Tagestypen löschen

> Hinweis
>
> Bevor du einen Tagestyp löschst, {% link_new entferne ihn aus allen Planungskalendern | features/administration/configure-planning-calendars.md | #tagestypen-aus-dem-planungskalender-entfernen %}. Du kannst keine Standard-Tagestypen löschen.

1. Wähle einen Tagestyp aus der Liste aus.
2. Klicke in der Aktionsleiste auf das {% icon item-delete %}.

## Tagestypen in der Schichtplanung

injixo berücksichtigt Tagestypen bei der Schichtplanung.

- Wenn deine Planungseinheit an einem Feiertag regulär geöffnet ist, musst du nur {% link_new die Öffnungszeiten zur Planungseinheit hinzufügen | features/administration/create-and-manage-planning-units.md | #öffnungszeiten-hinzufügen %}.
- Wenn deine Planungseinheit an einem Feiertag geschlossen ist oder die Öffnungszeiten abweichen, lies den Artikel {% link_new Feiertage planen | best-practices/scheduling-public-holidays.md %}.
