---
title: Deckung, Besetzung und Bedarf analysieren
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Analysiere die Deckung, die Besetzung und den Bedarf für Deine Aktivitäten und Aktivitätstypen (Schedules-Modul).
---

In diesem Artikel lernst Du, wie Du:
- die Deckung, die Besetzung und den Bedarf für Deine Aktivitäten und Aktivitätstypen analysierst.
- nach Aktivitäten und Aktivitätstypen filterst.

Neu im Schedules-Modul? Lerne zuerst {% link_new die Grundlagen | features/scheduling/schedules/schedules-overview.md %}.

## Was ist das Aktivitäten-Panel?

Das *Aktivitäten-Panel* ist Teil von _Plan > Schedules_{:.breadcrumbs}. Es befindet sich am unteren Rand des Bildschirms und ist standardmäßig eingeklappt. Das Panel ermöglicht Dir, die Deckung, die Besetzung und den Bedarf an Aktivitäten und Aktivitätstypen für die Planungseinheit(en) zu analysieren, die Du oben im Planungsfenster ausgeklappt hast.

Es gibt die folgenden drei Tabs:

  - *Aktivitäten - Deckung*: die Differenz zwischen der Anzahl der geplanten und der benötigten Mitarbeiter
  - *Aktivitäten - Besetzung*: die Anzahl der geplanten Mitarbeiter für eine bestimmte Aktivität
  - *Aktivitäten - Bedarf*: gespeicherter Mitarbeiterbedarf pro Aktivität  

Klicke auf _⌃_{:.doc-button} auf der linken Seite oder auf einen der Tabs, um das Panel auszuklappen.

{{ 1 | image: 'Der Tab Aktivitäten - Deckung' }}

## Überprüfe die Deckung, Besetzung oder den Bedarf für eine Aktivität oder einen Aktivitätstyp

1. Klicke auf einen der drei **Tabs** im *Aktivitäten-Panel* abhängig davon, ob Du die Deckung, die Besetzung oder den Bedarf analysieren möchtest.
2. Klicke in der Kopfzeile der ersten Spalte auf das **Filtersymbol** und wähle die Aktivitäten und Aktivitätstypen aus, die Du analysieren möchtest. Weitere Informationen zum [Filtern](#aktivitäten-und-aktivitätstypen-filtern) findest Du unten.
3. Klicke an eine **beliebige Stelle** außerhalb des Auswahlfensters, um die Ansicht zu aktualisieren.

Du siehst nun eine Tabelle, die aus folgenden Elementen besteht:

- Spalte *Aktivität*: enthält eine Liste aller ausgewählten Aktivitäten und Aktivitätstypen
- Spalte *Ebene*: zeigt die Ebene(n) an, die im Planungsfenster ausgewählt sind
- Spalte *Summe*: zeigt die Summe der Deckungs-, Besetzungs- oder Bedarfswerte für den angezeigten Zeitraum an
- *Zeit- bzw. Datumsbereich*: Deckungs-, Besetzungs- oder Bedarfswerte basierend auf dem gewählten Zeitbereich und der gewählten Zoomstufe im Planungsfenster

Wenn Du zuvor den Bedarf berechnet und Deine Mitarbeiter geplant hast, kannst Du nun für jede Aktivität und jedes Intervall prüfen, wie gut die Deckung ist. Außerdem kannst Du für jedes Intervall die Besetzung und den berechneten Bedarf überprüfen. Leere Zellen bedeuten, dass der Bedarf oder die Besetzung fehlt oder beides.

{{ 6 | image: 'Der Tab Aktivitäten mit einer Multiaktivität' }}

Wenn Du die Daten in Stunden-Intervallen betrachtest, kannst Du mit der Maus über eine **Zelle** fahren, um die Werte der 15-Minuten-Intervalle anzuzeigen.

{{ 2 | image: 'Detail-Ansicht', '40%' }}

Hinweis: Aktivitäten, die im Bereich *Administration* gelöscht wurden, erscheinen kursiv. Multiaktivitäten werden mit dem _Symbol_{:.multiactivity-icon} dargestellt. Die eingerückten Zeilen unterhalb der Multiaktivität enthalten die Teilaktivitäten.

### Die Farbkodierung verstehen

Die Farbkodierung der Zellen zeigt Dir direkt, wie gut die Deckung ist. Rot zeigt Unterdeckung, Blau zeigt Überdeckung und Grün signalisiert ideale Deckung (Besetzung = Bedarf). Je intensiver die Farbe, desto größer ist die Abweichung von der idealen Besetzung. <!-- Weiße Zellen zeigen an, dass es innerhalb einer Stunde eine Über- und Unterdeckungen gibt, die sich zu Null summieren. -->

## Aktivitäten und Aktivitätstypen filtern

Filtere die Liste der Aktivitäten und Aktivitätstypen, um nur die Elemente anzuzeigen, für die Du die Deckung, die Besetzung oder den Bedarf analysieren möchtest.  

1. Klicke auf das **Filtersymbol** _![Filter icon](/assets/img/common/schedules-filter-activities.png)_{:.doc-button-icon} in der Kopfzeile der Spalte *Aktivität*. Eine Liste von Aktivitäten und Aktivitätstypen erscheint, basierend auf allen Planungseinheiten, die derzeit im Planungsfenster aufgeklappt sind.
2. Verwende optional das **Suchfeld**, um die benötigten Elemente schnell zu finden. Führe mehrere Suchvorgänge auf einmal durch, indem Du die Suchbegriffe mit Kommas trennst. Bei Multiaktivitäten kannst Du auch nach dem Namen von Teilaktivitäten suchen, aber nur die Multiaktivität selbst kann ausgewählt oder abgewählt werden. Alle Teilaktivitäten werden in diesem Fall automatisch hinzugefügt oder entfernt.
    {{ 5 | image: 'Filter mit Multiaktivität', '40%' }}

3. Aktiviere oder deaktiviere die **Checkboxen** vor den Elementen, die Du anzeigen oder ausblenden möchtest. Verwende **Alle**, um alle Elemente auf einmal aus- bzw. abzuwählen.
4. Klicke an eine **beliebige Stelle** außerhalb des Auswahlfensters, um die Ansicht zu aktualisieren. Du hast die Ansicht nun anhand der ausgewählten Aktivitäten und Aktivitätstypen gefiltert.

    {{ 4 | image: 'Aktivitäten filtern', '40%'}}
