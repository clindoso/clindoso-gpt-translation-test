---
title: Schichtpläne löschen
product_label:
  - classic
description: Lösche Schichtpläne in einer oder mehreren Ebenen für einen bestimmten Datumsbereich (SchedulePro).
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/what-are-planning-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/batch-replace-an-activity.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/planning-periods/copy-and-back-up-schedules.md
---

In diesem Artikel lernst Du, wie Du:

- Schichtpläne (Aktivitäten und Tagesmodelle) aus einer oder mehreren Ebenen für einen bestimmten Datumsbereich löschst.
- nur Daten für bestimmte Mitarbeiter löschst.

Hierzu verwendest Du Planperioden. Lies daher zuerst den Artikel {% link_new Was sind Planperioden? | features/scheduling/planning-periods/what-are-planning-periods.md %}.

> In diesem Artikel geht es um _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> Wenn Du injixo Advanced WFM oder Enterprise WFM verwendest, nutze stattdessen die Funktion {% link_new Ebenen leeren | features/scheduling/schedules/schedules-empty-levels.md %} unter _Plan > Schedules_{:.breadcrumbs}.

## Eine Planperiode auswählen oder erstellen

1. Gehe zu _WFM > Scheduling > SchedulePro > Planperioden_{:.breadcrumbs}.
2. Wähle eine **Planungseinheit** aus.
3. Wähle den **Typ** _Standard_.
4. Für **Auswahl** wähle **[Alle]**.
5. Klicke auf _Anwenden_{:.doc-button}.
6. Wähle die Planperiode mit dem Datumsbereich aus, für welchen Du Schichtpläne löschen möchtest. Der Datumsbereich der Planperiode kann auch größer sein als der Datumsbereich, den Du löschen willst.
7. Klicke auf _![edit button](/assets/img/common/item-edit.gif)_{:.doc-button-icon}.
8. Setze den **Status** auf _Gesperrt_, damit der Schichtplan im gewählten Zeitraum nicht für Mitarbeiter zugänglich ist.
9. Klicke auf _Ok_{:.doc-button}.

Wenn es keine passende Planperiode in der Liste gibt, erstelle eine neue:

1. Klicke auf das {% icon item-add %} in der Aktionsleiste.
2. Lege mit **Gültig von** und **Gültig bis** den Zeitraum fest, in dem Du Schichtpläne löschen willst.
3. Setze den **Status** auf _Gesperrt_, damit der Schichtplan im gewählten Zeitraum nicht für Mitarbeiter zugänglich ist.
4. Klicke auf _Ok_{:.doc-button}.

## Schichtpläne löschen

> Sei vorsichtig beim Einstellen der Parameter - die Löschung eines Schichtplans kann nicht rückgängig gemacht werden.

> Lösche keine Urlaubs- und Abwesenheitsanfragen
>
> Genehmigte {% link_new Abwesenheits-Anfragen | features/scheduling/time-off/vacation-absences-management.md %} werden ausschließlich in der Ebene _Plan_ gespeichert. Wenn Du bereits Anfragen genehmigt hast, dann lösche Deinen Schichtplan nicht wie hier beschrieben. Denn dann würdest Du auch die bereits genehmigten Abwesenheitsanfragen im gewählten Zeitraum löschen. Lösche stattdessen die Schichten von Hand.

1. Klicke auf eine **Planperiode** vom Typ _Standard_, die den Datumsbereich umfasst, in dem Du Schichten löschen willst. Ein Menü öffnet sich auf der rechten Seite.
2. Klicke auf _Löschen_{:.doc-button} im Abschnitt _Ebene_.
3. Falls notwendig, ändere das **Startdatum** und das **Enddatum** um den zu löschenden Zeitraum weiter einzugrenzen.
4. Optional: Ändere die Methode der **Mitarbeiterauswahl**, um nur die Schichten von bestimmten Mitarbeitern zu löschen. Wähle eine oder mehrere Auswahlen oder Mitarbeiter aus der Liste. Drücke die _Umschalt_- oder _Strg_-Taste, um mehrere Einträge auf einmal auszuwählen.
5. Wähle die **Ebene** aus, von welcher Du Daten löschen willst.
6. Um die Daten zu löschen, klicke _Ok_{:.doc-button}. Es erfolgt keine weitere Sicherheitsabfrage.

{{ 4 | image: 'Delete level dialog', '50%' }}
