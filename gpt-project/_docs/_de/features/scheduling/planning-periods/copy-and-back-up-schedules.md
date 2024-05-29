---
title: Schichtpläne kopieren oder sichern
product_label:
  - classic
description: Kopiere oder sichere Schichtpläne und andere Elemente in den verschiedenen Planungsebenen von injixo (SchedulePro).
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/what-are-planning-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/delete-schedules.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/batch-replace-an-activity.md
---

In diesem Artikel lernst Du, wie Du Schichtpläne und andere Elemente in den verschiedenen Planungsebenen von injixo kopierst oder sicherst.

Hierfür verwendest Du Planperioden. Lies daher zuerst den Artikel {% link_new Was sind Planperioden? | features/scheduling/planning-periods/what-are-planning-periods.md %}.

> In diesem Artikel geht es um _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> Wenn Du injixo Advanced WFM oder Enterprise WFM verwendest, nutze stattdessen die Funktion {% link_new Ebeneninhalte kopieren | features/scheduling/schedules/schedules-copy-level-content.md %} unter _Plan > Schedules_{:.breadcrumbs}.

## Ebenen in injixo

In injixo kannst Du verschiedene Ebenen für Planungszwecke nutzen. Ebenen enthalten - unter anderem - Tagesmodelle oder Aktivitäten für die Schichtplanung, Schichtwünsche oder Daten zur Verfügbarkeit von Agenten. Du kannst die Daten einer Ebene innerhalb derselben Ebene oder in eine andere Ebene kopieren, z.B. Deinen kompletten Schichtplan oder Teile davon. Das kann hilfreich sein, um Deine Planung zu beschleunigen.

Du kannst ein Backup anlegen, indem Du den kompletten Schichtplan in eine neue Ebene kopierst. Backups sind von Zeit zu Zeit empfehlenswert, besonders bevor du neue Planungsmethoden ausprobierst.

## Eine Planperiode auswählen oder erstellen

1. Gehe zu _WFM > Scheduling > SchedulePro > Planperioden_{:.breadcrumbs}.
2. Wähle eine **Planungseinheit** aus.
3. Wähle den **Typ** _Standard_.
4. Für **Auswahl** wähle **[Alle]**.
5. Klicke auf _Anwenden_{:.doc-button}.
6. Wähle die Planperiode mit dem Datumsbereich aus, für welchen Du Schichtpläne kopieren oder sichern möchtest. Der Datumsbereich der Planperiode kann auch größer sein als der Datumsbereich, den Du kopieren willst.
7. Klicke auf das {% icon item-edit %}.
8. Setze den **Status** auf _Gesperrt_, damit der Schichtplan im gewählten Zeitraum nicht für Mitarbeiter zugänglich ist.
9. Klicke auf _Ok_{:.doc-button}.

Wenn es keine passende Planperiode in der Liste gibt, erstelle eine neue:

1. Klicke auf das {% icon item-add %} in der Aktionsleiste.
2. Lege mit **Gültig von** und **Gültig bis**, den Zeitraum fest, den Du kopieren willst.
3. Setze den **Status** auf _Gesperrt_, damit der Schichtplan im gewählten Zeitraum nicht für Mitarbeiter zugänglich ist.
4. Klicke auf _Ok_{:.doc-button}.

## Den Schichtplan kopieren

Wähle eine Planperiode mit dem Datumsbereich, für welchen Du Schichtpläne kopieren oder sichern möchtest:

1. Klicke auf die Planperiode. Es öffnet sich ein Menü auf der rechten Seite.
2. Klicke auf _Kopieren_{:.doc-button} im Abschnitt _Ebene_.
3. Optional: Ändere das **Startdatum** und **Enddatum**, um den Zeitrahmen weiter einzugrenzen. Wenn Du nichts änderst, wird der Zeitrahmen der Planperiode verwendet.
4. Optional: Ändere die Methode der **Mitarbeiterauswahl**, um den Prozess nur für bestimmte Mitarbeiter auszuführen. Wähle eine oder mehrere Auswahlen oder Mitarbeiter aus der Liste. Drücke die _Umschalt_- oder _Strg_-Taste, um mehrere Einträge auf einmal auszuwählen.
5. Als **Quellebene**, wählst Du die Ebene, aus welcher Du Aktivitäten kopieren möchtest.
6. Optional: Das Setzen der Option **Nach dem Kopieren leeren** löscht den vorhandenen Inhalt aus der Quellebene.
7. Als **Zielebene**, wählst Du die Ebene, in welche Du die Daten kopieren möchtest.
8. Ändere das **Startdatum** für die _Zielebene_, um Daten in einen anderen Zeitraum zu kopieren. Kopiere so z.B. die Daten eines alten Schichtplans in einen zukünftigen Zeitraum auf derselben Ebene. In diesem Fall sind _Quellebene_ und _Zielebene_ gleich.
9. Um den Schichtplan zu kopieren, klicke auf _Ok_{:.doc-button}.

{{ 3 | image: 'Level copy dialog', '50%' }}
