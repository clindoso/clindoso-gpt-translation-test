---
title: Verfügbarkeiten in injixo Me verwalten
description: Verhindere, dass Mitarbeiter vor einem bestimmten Datum einmalige Verfügbarkeiten hinzufügen oder ändern können.
product_label:
  - essential
  - advanced
  - enterprise
toc: true
---

In injixo legen Verfügbarkeiten bestimmte Tage und Zeiten fest, zu denen ein Mitarbeiter für die Schichtplanung verfügbar ist. Für Planer gibt es zwei Möglichkeiten, Verfügbarkeiten zu konfigurieren.

- Persönliche {% link_new wöchentliche Verfügbarkeiten | features/administration/availabilities.md | #verfügbarkeiten-konfigurieren %} verwenden
- {% link_new Tagesmodelle | features/administration/availabilities.md | #verfügbarkeiten-über-wochen-hinweg-wechseln %} verwenden

Zusätzlich können Mitarbeiter [einmalige Verfügbarkeiten](/de/add-availabilities-in-me#verfügbarkeit-hinzufügen) in injixo Me hinzufügen. Falls du bereits wöchentliche Verfügbarkeiten konfiguriert hast, werden diese durch einmalige Verfügbarkeiten überschrieben.

## Mitarbeitern Zugriff auf Verfügbarkeiten geben

Um Mitarbeitern Zugriff auf Verfügbarkeiten in injixo Me zu geben, konfiguriere deren Rolle:

1. Gehe zu _Account > Rollen_{:.breadcrumbs}.
2. Klicke auf die entsprechende Rolle.
3. Klappe im Abschnitt **Berechtigungen** das Dropdown-Menü **Me** aus.
4. Aktiviere die Checkbox **Verfügbarkeiten**.
5. Klicke auf _Änderungen speichern_{:.doc-button}.

Ab dem nächsten Tag kann der Mitarbeiter seine Verfügbarkeiten in Me eintragen.

## Verhindern, dass Mitarbeiter Verfügbarkeiten ändern

Die Verfügbarkeit deiner Mitarbeiter kann von Tag zu Tag und von Woche zu Woche variieren. Wenn du möchtest, dass Mitarbeiter ihre Verfügbarkeiten in injixo Me eintragen können, ohne dass es zu Planungskonflikten kommt, kannst du verhindern, dass Mitarbeiter einmalige Verfügbarkeiten vor einem bestimmten Datum hinzufügen bzw. bearbeiten.

Beispiel: Du möchtest deine Schichtpläne mit einem Vorlauf von zwei Wochen erstellen. Um zu verhindern, dass deine Mitarbeiter ihre Verfügbarkeiten in diesen zwei Wochen hinzufügen oder bearbeiten, wähle ein Datum am Ende des geplanten Zeitraums aus. Wenn du am 2.&nbsp;Januar einen Schichtplan für die Woche ab dem 15.&nbsp;Januar erstellen möchtest, wähle den 22.&nbsp;Januar aus. Dies verhindert, dass deine Mitarbeiter ihre Verfügbarkeiten bis einschließlich 22.&nbsp;Januar hinzufügen bzw. bearbeiten können.

Um zu verhindern, dass Mitarbeiter Verfügbarkeiten in injixo Me vor einem bestimmten Datum ändern können, gehe wie folgt vor:

1. Gehe zu _Plan > Konfiguration > Allgemein_{:.breadcrumbs}.
2. Wähle mit der Datumsauswahl ein Datum aus.
3. Klicke auf _Änderungen speichern_{:.doc-button}.

Vor dem ausgewählten Datum können Mitarbeiter ihre Verfügbarkeiten sehen, sie können sie jedoch nicht bearbeiten. Wenn du kein Datum angibst, können Mitarbeiter jederzeit einmalige Verfügbarkeiten hinzufügen bzw. ändern.
