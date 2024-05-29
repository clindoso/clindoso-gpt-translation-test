---
title: Massenbearbeitung
product_label:
  - advanced
  - enterprise
  - classic
---

Mit der Massenbearbeitung kannst du die Zuweisung von Stammdaten für mehrere Mitarbeiter auf einmal ändern.
Du kannst die Funktionalität Massenbearbeitung für folgende Konfigurationselemente verwenden:

- Verträge
- Qualifikationen
- Planungseinheiten
- Auswahl
- Schichtfolgen
- Planungsmodelle

## Voraussetzungen

Bevor du die Funktionalität Massenbearbeitung verwenden kannst, musst du deine {% link_new Grundkonfiguration einrichten | getting-started/set-up-base-configuration.md %}.

## Massenbearbeitung starten

> Hinweis
>
> Du kannst eine Massenbearbeitung nicht zurücksetzen oder rückgängig machen. Starte eine neue Massenbearbeitung, wenn du eine fälschlich durchgeführte Massenbearbeitung überschreiben möchtest oder ändere die Daten für jeden Mitarbeiter einzeln.

Um eine Massenbearbeitung zu starten, gehe wie folgt vor:

1. Gehe zu _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs}.
2. Um die Mitarbeiter auszuwählen, deren Stammdaten du ändern möchtest, wähle eine Auswahl aus oder klicke auf das Mitarbeiterfilter-Icon {% icon employee-filter | icon-only %}.
3. Klicke in der Aktionsleiste auf das Massenbearbeitungs-Icon {% icon mass-update | icon-only %}.<br>Die Seite **Massenbearbeitung** öffnet sich.
4. Verwende im Abschnitt **Parameter** das Dropdown-Menü **Stammdaten**, um das Konfigurationselement auszuwählen, das du für mehrere Mitarbeiter auf einmal ändern möchtest.<br>(Optional): Verwende die Felder **vom** und **bis**, um einzuschränken, für wie lange die Änderung durch die Massenbearbeitung gilt.
5. Wähle eine **Aktion**.
6. Je nach Auswahl erscheinen rechts folgende Abschnitte: **Bisherige Zuordnungen**, **Neue Zuordnung** oder **Neuer Gültigkeitszeitraum**. Wähle in den Abschnitten die Elemente aus, die du hinzufügen, löschen oder ersetzen möchtest.
7. Um die Massenbearbeitung zu starten, klicke auf **OK**.<br>Das Fenster **Jobverarbeitung** öffnet sich.<br>Eine Seite mit dem Ergebnis der Massenbearbeitung öffnet sich.

| Frage                                                                                                            | Antwort                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Warum sind meinen Mitarbeitern nach einer Massenbearbeitung Verträge für eine kürzere Zeit zugewiesen als davor? | Wenn du einem Mitarbeiter ein Konfigurationselement mit einem Zeitraum zuweist, der länger ist als der Gültigkeitszeitraum, kann es zu Zeiträumen ohne Zuweisung kommen.<br>Beispiel: Einem Mitarbeiter ist ein Vertrag zugewiesen. Die Zuweisung ist vom 1.&nbsp;März bis 31.&nbsp;Mai. Du gibst einen neuen Gültigkeitszeitraum vom 1.&nbsp;März bis 15.&nbsp;April ein. Nach der Massenbearbeitung gibt es keine Zuweisung mehr für den Zeitraum vom 16.&nbsp;April bis 31.&nbsp;Mai. |
