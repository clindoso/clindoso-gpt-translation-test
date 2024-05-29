---
title: Mitarbeiterfilter konfigurieren
description: Verwende den Mitarbeiterfilter, um Mitarbeiter anhand von gewissen Kriterien zu filtern.
product_label:
  - advanced
  - enterprise
  - classic
---

Mit Mitarbeiterfiltern kannst du Listen von Mitarbeitern anlegen, die bestimmte Kriterien erfüllen. Die Bearbeitungsmöglichkeiten hängen von deinen Berechtigungen ab.

Mitarbeiterfilter funktionieren ähnlich wie {% link_new Auswahlen | features/administration/selections.md %}. So unterscheiden sie sich voneinander:

- Mitarbeiterfilter gruppieren auf Grundlage der Stammdaten wie z.&nbsp;B. Planungseinheit, Qualifikation und Vertrag.
- Bei Auswahlen kannst du die Kriterien für die Gruppierung selbst festlegen.

Mitarbeiterfilter sind nur in injixo Classic, Advanced und Enterprise verfügbar.

1. Um die Bearbeitungsansicht für den Mitarbeiterfilter zu öffnen, gehe zu _Plan > Schicht Center_{:.breadcrumbs}.
2. Falls die Kachel für die Auswahl {% icon selection-filter-s | icon-only %} ausgewählt ist, klicke auf die Kachel für Mitarbeiter {% icon schedules-filter-employees-u | icon-only %} .
3. Klicke auf den Link **Filter-Editor**.

## Filter anlegen

1. Klicke im Abschnitt **Mitarbeiterfilter** auf das Filter-anlegen-Icon {% icon item-add | icon-only %}.
2. Wähle einen **Zeitraumtyp**:<br>
   - **Frei wählbar**: Lege den Zeitraum manuell mit der Datumsauswahl fest. Bestimme das Datum für **vom** und **bis**.<br>
   - **Relativ**: Lege einen Zeitraum für die folgende, aktuelle oder vorherige Woche, den Monat oder das Jahr fest.<br>
   - **Vorgegeben**: Der Zeitraum wird automatisch auf den aktuellen Tag festgelegt.
3. Erstelle eine [**Abfrage**](#abfrage-erstellen).
4. Um die Abfrageergebnisse anzuzeigen, klicke auf _Anzeigen_{:.doc-button}.
5. Um die Abfrage zum Mitarbeiterfilter hinzuzufügen, klicke auf _Anwenden_{:.doc-button}.
6. Um den Filter zu speichern, klicke auf das {% icon save %}.<br>Um einen vorhandenen Filter unter einem anderen Namen zu speichern, klicke auf das {% icon saveas %}.

## Abfrage erstellen

Eine Abfrage ist eine Reihe von Bedingungen, mit denen Daten aus einem größeren Datensatz gefiltert und abgerufen werden. Du kannst Kriterien festlegen und eine Liste von Mitarbeitern erhalten, die diese Kriterien erfüllen.

1. Klicke im Abschnitt **Abfrage** auf das {% icon item-add %}.
2. Wähle im ersten Dropdown-Menü ein Konfigurationselement aus den Stammdaten.
3. Wähle im zweiten Dropdown-Menü eine Bedingung aus.
4. (Optional) Wähle eine [Priorität und Vergleichsoperatoren](#priorität-und-vergleichsoperatoren-verwenden) für Planungseinheiten, Mitarbeiterkategorien oder Qualifikationen.
5. Klicke auf _Anwenden_{:.doc-button}.

Um eine Abfrage zu bearbeiten, klicke auf das {% icon item-edit %}.

## Bedingungen verwenden

### IS IN

Die Bedingung **IS IN** zeigt Ergebnisse, die genau der Abfrage entsprechen.

1. Wähle im ersten Dropdown-Menü ein Konfigurationselement aus den Stammdaten.
2. Wähle im zweiten Dropdown-Menü die Bedingung **IS IN**.
3. Klicke auf _Kriterien_{:.doc-button}, um die verfügbaren Kriterien einzusehen und auszuwählen.
4. Um Kriterien zu deiner Auswahl hinzuzufügen, klicke auf das {% icon right-arrow-blue %}.
5. Klicke im Fenster **Kriterien auswählen** auf _Anwenden_{:.doc-button}.
6. (Optional) Wähle [Optionen und Vergleichsoperatoren](#priorität-und-vergleichsoperatoren-verwenden) für Planungseinheiten, Mitarbeiterkategorien oder Qualifikationen.
7. Klicke auf _Anwenden_{:.doc-button}.

### IS LIKE

Die Bedingung **IS LIKE** zeigt Ergebnisse, die teilweise der Abfrage entsprechen.

1. Wähle im ersten Dropdown-Menü ein Konfigurationselement aus den Stammdaten.
2. Wähle im zweiten Dropdown-Menü die Bedingung **IS LIKE**.
3. Gib im Textfeld den Text ein, der in der Filtersuche verwendet werden soll.
   - Um eine beliebige Anzahl Zeichen zu ersetzen, verwende den Platzhalter \*.
   - Um genau ein Zeichen zu ersetzen, verwende den Platzhalter ?.
4. (Optional) Wähle [Optionen und Vergleichsoperatoren](#priorität-und-vergleichsoperatoren-verwenden) für Planungseinheiten, Mitarbeiterkategorien oder Qualifikationen.
5. Klicke auf _Anwenden_{:.doc-button}.

## Priorität und Vergleichsoperatoren verwenden

Mit der Checkbox Priorität und den Vergleichsoperatoren kannst du nach Mitarbeitern auf Grundlage ihrer Priorität und ihrer Zugehörigkeit zur ausgewählten Planungseinheit bzw. Mitarbeiterkategorie suchen.

1. Wähle **Planungseinheit** oder **Mitarbeiterkategorie** aus dem ersten Dropdown-Menü aus.
2. Aktiviere die Checkbox **Priorität**.
3. Wähle einen Vergleichsoperator aus der Liste aus.
4. Gib im Eingabefeld einen Wert für die Priorität ein.

Du kannst das Konfigurationselement Qualifikation mit Vergleichsoperatoren kombinieren, um nach qualifizierten Mitarbeitern mit einer bestimmten Qualifikationsstufe zu suchen:

1. Wähle die **Qualifikation** aus dem ersten Dropdown-Menü.
2. Aktiviere die Checkbox **Qualifikationsstufe**.
3. Wähle einen Vergleichsoperator aus der Liste aus.
4. Gib im Eingabefeld einen Wert für die Qualifikationsstufe ein.

## Abfragen verknüpfen

Du kannst einzelne Abfragen miteinander verknüpfen:

1. Lege einen [Filter](#filter-anlegen) an oder wähle einen bestehenden aus.
2. Erstelle eine [Abfrage](#abfrage-erstellen).
3. Wähle einen Bedingungsoperator aus:<br>

   - **AND**: Schließt Mitarbeiter ein, die alle Bedingungen erfüllen.
   - **OR**: Schließt Mitarbeiter ein, die mindestens eine der Bedingungen erfüllen.
   - **NOT**: Schließt Mitarbeiter aus, die die Bedingung erfüllen, die auf den Operator NOT folgt.

4. Erstelle eine zweite Abfrage.
5. Klicke auf _Anwenden_{:.doc-button}.

Um eine Gruppe zu erstellen, öffne eine Klammer. Um die Gruppe zu schließen, schließe die Klammer. Mit den Auf- und Ab-Pfeilen kannst du die einzelnen Abfragen jederzeit verschieben und sortieren.

## Beispiel-Abfrage

Um Mitarbeiter aus der Planungseinheit New York zu filtern, die keinen 40-Stunden-Vollzeitvertrag haben und nicht zur Auswahl Überstunden gehören, schreibe die Abfrage wie folgt:

```
Planungseinheit IS IN "New York"
AND
NOT
(
Vertrag IS IN "40h Standard"
AND
Auswahl IS IN "Überstunden"
)
```

Diese Abfrage beinhaltet alle Mitarbeiter aus der Planungseinheit New York ohne die Mitarbeiter, die einen 40-Stunden-Vollzeitvertrag haben und in der Auswahl Überstunden sind:

- **IS IN** legt die Bedingung für die Planungseinheit fest.
- **AND** legt die Bedingungen für die Abfrage fest.
- **NOT** schließt die folgenden Bedingungen aus.
- Die Klammern öffnen und schließen die Gruppe von Bedingungen, die ausgeschlossen werden sollen.
- **IS IN** wählt Mitarbeiter aus, die einen 40-Stunden-Vollzeitvertrag haben.
- **AND** verknüpft die Bedingungen innerhalb der Klammern.
- **IS IN** wählt Mitarbeiter aus, die zur Auswahl Überstunden gehören.

## Filter bearbeiten

1. Wähle im Dropdown-Menü **Mitarbeiterfilter** einen Filter aus.
2. Bearbeite die Informationen, die du ändern möchtest.
3. (Optional) Um deinen Filter umzubenennen, klicke auf das {% icon item-edit %}.
4. Um zu speichern, klicke auf das {% icon save %}.<br>Um einen vorhandenen Filter unter einem anderen Namen zu speichern, klicke auf das {% icon saveas %}.
