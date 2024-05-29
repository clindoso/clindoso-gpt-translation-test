---
title: Deckung, Besetzung und Mitarbeiterbedarf in Schedules analysieren
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du die Deckung, die Besetzung und den Mitarbeiterbedarf für deine Aktivitäten und Aktivitätstypen analysierst.
---

Unter _Plan > Schedules_{:.breadcrumbs} kannst du die Deckung, die Besetzung und den Mitarbeiterbedarf für deine geplanten Aktivitäten und Aktivitätstypen analysieren.

## Voraussetzungen

- Du hast den {% link_new Mitarbeiterbedarf | features/forecast/injixo-forecast/calculate-staff-requirements.md %} berechnet.
- Du hast einen {% link_new Schichtplan | getting-started/create-a-schedule.md %} erstellt.

Neu bei Schedules? Lerne zuerst {% link_new die Grundlagen | features/scheduling/schedules/schedules-overview.md %}.

## Aktivitäten-Bereich anzeigen

1. Wähle unter _Plan > Schedules_{:.breadcrumbs} deine {% link_new Filter | features/scheduling/schedules/schedules-overview.md | #daten-filtern %} und {% link_new Anzeigeoptionen | features/scheduling/schedules/schedules-overview.md | #schichtplan-bereich %} aus.
2. Klappe im Schichtplan-Bereich die Planungseinheit(en) aus, für die du Aktivitätsdaten analysieren möchtest.
3. Klicke im [Aktivitäten-Bereich](#tabelle-mit-aktivitätsdaten) auf einen Tab:
   - **Aktivitäten - Deckung**: Die Differenz zwischen der Anzahl geplanter Mitarbeiter und dem Mitarbeiterbedarf
   - **Aktivitäten - Besetzung**: Die Anzahl geplanter Mitarbeiter
   - **Aktivitäten - Bedarf**: Der gespeicherte Mitarbeiterbedarf<br>
4. Um Aktivitäten und Aktivitätstypen auszuwählen, verwende das Filter-Icon {% icon filter | icon-only %} im Header der Spalte **Aktivität**.<br>Neben Multiaktivitäten wird ein <em class="multiactivity-icon"></em>-Icon angezeigt. Teilaktivitäten sind unterhalb der Multiaktivität eingerückt.<br>Wenn du unter _Plan > Konfiguration > Aktivitäten_{:.breadcrumbs} eine Aktivität löschst und sie nicht von den Planungseinheiten entfernst, denen sie zugewiesen war, wird die gelöschte Aktivität hier kursiv angezeigt.
   - Aktiviere die Checkboxen neben den Elementen, die du anzeigen möchtest. Du kannst sowohl Multiaktivitäten als auch Einzelaktivitäten auswählen, die keine Teilaktivitäten sind. Du kannst keine einzelnen Teilaktivitäten auswählen. Um nach einzelnen Teilaktivitäten, Multiaktivitäten oder anderen Einzelaktivitäten zu suchen, gib ihren Namen ins Suchfeld ein.
   - (Optional) Verwende das Suchfeld. Um nach mehreren Begriffen gleichzeitig zu suchen, setze Kommas zwischen die Suchbegriffe.
5. Klicke auf eine beliebige Stelle außerhalb des Aktivitäten-Bereichs, um die angezeigten Daten zu aktualisieren.

### Tabelle mit Aktivitätsdaten

Die Tabelle in jedem Tab enthält die folgenden Spalten:

- **Aktivität**: Die Aktivitäten oder Aktivitätstypen, für die du Daten anzeigen möchtest.
- **Ebene**: Die Ebene(n), die du im {% link_new Schichtplan-Bereich | features/scheduling/schedules/schedules-overview.md | #schichtplan-bereich %} ausgewählt hast.
- **Summe**: Die Summe der Werte für Deckung, Besetzung oder Mitarbeiterbedarf für den angezeigten Zeitraum.
- Spalte mit Zeitleiste: Eine Übersicht über den ausgewählten Zeitraum mit den Werten für Deckung, Besetzung und Mitarbeiterbedarf pro Intervall.

Bewege den Mauszeiger auf eine beliebige Zelle, um die Werte für Deckung, Besetzung und Mitarbeiterbedarf für die 15-Minuten-Intervalle anzuzeigen.

Wenn du mit der Datumsauswahl im Schichtplan-Bereich einen oder maximal zwei Tage auswählst oder wenn du auf eine Tagesmarkierung in der Spalte mit der Zeitleiste klickst, zeigt die Tabelle Spalten für jede Stunde des gewählten Zeitraums an.
Um Daten in 30-Minuten-Intervallen anzuzeigen, bewege den Mauszeiger zu der Stelle zwischen zwei Stundenmarkierungen im Tabellenheader. Wenn das {% icon magnifying_glass %} erscheint, klicke darauf.<br>Um 15-Minuten-Intervalle anzuzeigen, bewege den Mauszeiger auf die 30-Minuten-Marke und klicke auf das dann erscheinende {% icon magnifying_glass %}.<br>Um zu der 30-Minuten-Ansicht zurückzukehren, klicke auf eine beliebige 15-Minuten-Markierung. Um zur Stundenansicht zurückzukehren, klicke auf eine beliebige Stundenmarkierung.<br>

Eine Zelle ist leer, wenn für das Intervall entweder der Mitarbeiterbedarf oder die Werte für die Besetzung oder beides gleichzeitig fehlen.<br>
Die Farbcodierung der Zellen wird in der folgenden Tabelle dargestellt. Je intensiver die Farbe, desto größer ist die Differenz zwischen dem Mitarbeiterbedarf und der Besetzung.

<!-- left-align table -->
<style>
table {
   margin-left: 0px;
}
</style>

| Farbe | Deckung        | Beschreibung                                                          |
| ----- | -------------- | --------------------------------------------------------------------- |
| Rot   | Unterbesetzung | Weniger Mitarbeiter geplant als benötigt                              |
| Blau  | Überbesetzung  | Mehr Mitarbeiter geplant als benötigt                                 |
| Grün  | Ideale Deckung | Die Anzahl der geplanten Mitarbeiter entspricht dem Mitarbeiterbedarf |
