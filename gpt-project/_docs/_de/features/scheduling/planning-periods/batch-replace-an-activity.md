---
title: Eine Aktivität im Schichtplan austauschen
product_label:
  - classic
description: Ersetze in einem bestehenden Schichtplan alle Instanzen einer Aktivität durch eine andere Aktivität (SchedulePro).
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/what-are-planning-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/copy-and-back-up-schedules.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/delete-schedules.md
---

In diesem Artikel lernst Du, wie Du in einem bestehenden Schichtplan eine Aktivität komplett durch eine andere Aktivität ersetzt.

Hierfür verwendest Du Planperioden. Lies daher zuerst den Artikel {% link_new Was sind Planperioden? | features/scheduling/planning-periods/what-are-planning-periods.md %}.

> In diesem Artikel geht es um _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> Wenn Du injixo Advanced WFM oder Enterprise WFM verwendest, nutze stattdessen die Funktion {% link_new Aktivitäten ersetzen | features/scheduling/schedules/schedules-replace-activities.md %} unter _Plan > Schedules_{:.breadcrumbs}.

## Eine Planperiode auswählen oder erstellen

1. Gehe zu _WFM > Scheduling > SchedulePro > Planperioden_{:.breadcrumbs}.
2. Wähle eine **Planungseinheit** aus.
3. Wähle den **Typ** _Standard_.
4. Für **Auswahl** wähle **[Alle]**.
5. Klicke auf _Anwenden_{:.doc-button}.
6. Wähle die Planperiode mit dem Datumsbereich aus, für den Du die Aktivität austauschen möchtest. Der Datumsbereich der Planperiode kann auch größer sein als der Datumsbereich, in dem Du die Aktivität ersetzen willst.
7. Klicke auf das {% icon item-edit %}.
8. Setze den **Status** auf _Gesperrt_, damit der Schichtplan im gewählten Zeitraum nicht mehr für Mitarbeiter zugänglich ist.
9. Klicke auf _Ok_{:.doc-button}.

Wenn es keine passende Planperiode in der Liste gibt, erstelle eine neue:

1. Klicke auf das {% icon item-add %} in der Aktionsleiste.
2. Lege mit **Gültig von** und **Gültig bis**, den Zeitraum fest, in dem Du die Aktivität austauschen willst.
3. Setze den **Status** auf _Gesperrt_, damit der Schichtplan im gewählten Zeitraum nicht für Mitarbeiter zugänglich ist.
4. Klicke auf _Ok_{:.doc-button}.

## Eine Aktivität im Schichtplan austauschen

Wähle die Planperiode mit dem Datumsbereich, in dem Du die Aktivität austauschen möchtest:

1. Klicke auf die Planperiode. Es öffnet sich ein Menü auf der rechten Seite.
2. Klicke auf _Austauschen_{:.doc-button} im Bereich _Aktivität_.
3. Optional: Ändere das **Startdatum** und **Enddatum**, um den Zeitrahmen weiter einzugrenzen. Wenn Du nichts änderst, wird der Zeitrahmen der Planperiode verwendet.
4. Optional: Ändere die Methode der **Mitarbeiterauswahl**, um den Prozess nur für bestimmte Mitarbeiter auszuführen. Wähle eine oder mehrere Auswahlen oder Mitarbeiter aus der Liste. Drücke die _Umschalt_- oder _Strg_-Taste, um mehrere Einträge auf einmal auszuwählen.
5. Kreuze bei **Ebenen** ein oder mehrere Kästchen an, um die Planungsebenen auszuwählen, in denen Du die Aktivitätsersetzung durchführen möchtest.
6. Wähle bei **Suchen** die Aktivität aus, die Du ersetzen möchtest.
7. Wähle bei **Ersetzen** die Aktivität aus, mit der Du die andere Aktivität ersetzen möchtest.
8. Um die Ersetzung durchzuführen, klicke auf _Ok_{:.doc-button}.

{{ 2 | image: 'Exchange activities', '50%' }}
