---
title: Schichtbedarf nutzen
product_label:
  - advanced
  - enterprise
description: Nutze Schichtbedarf im Schichtwunsch-Verfahren, um zu definieren, wie viele Schichten erzeugt werden. Diese stehen dann in injixo Me zum Wünschen zur Verfügung.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-basics.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/day-types.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/edit-or-delete-staff-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
---

In diesem Artikel lernst Du:

- was Schichtbedarf ist und wie Du diesen verwendest.
- wie Du die Werte richtig in die Schichtbedarfstabelle eingibst.
- wie Du das Ergebnis der Schichterzeugung überprüfen kannst.

Der Schichtbedarf wird für das {% link_new Schichtwunsch-Verfahren | features/scheduling/schedules/schedules-shift-bidding.md %} benötigt. Der Schichtbedarf gibt vor, wie viele Schichten durch die Schichterzeugung minimal erzeugt werden müssen bzw. maximal erzeugt werden können. Das Ergebnis der Schichterzeugung sind die Schichten, die den Mitarbeitenden in injixo _Me_{:.menu-item} als Wünsche zur Verfügung stehen.

## Schichtbedarf anzeigen

Überprüfe oder bearbeite den Schichtbedarf in _Plan > Schedules_{:.breadcrumbs}.

1. Klicke auf _Planperioden_{:.doc-button}.
2. Bewege den Mauszeiger in der Übersicht über eine **Planperiode** und klicke auf _![Kontextmenü Icon](/assets/img/common/injixo-ui/context-menu.svg)_{:.doc-button-icon} auf der rechten Seite.
3. Wähle _Schichterzeugung anpassen_{:.doc-button} im Overflow-Menü. Die Planungseinheit der Planperiode ist vorausgewählt.
4. Klicke auf _Speichern_{:.doc-button}.

Die Tabelle zeigt fixe und variable Tagesmodelle. Die Tagesmodelle und die darin enthaltenen Aktivitäten müssen der Planungseinheit zugeordnet sein.

{{ 1 | image: 'Tabelle für den Schichtbedarf', '100%' }}

Füge der Planungseinheit weitere {% link_new Tagestypen | features/administration/day-types.md %} hinzu, um neben den Standard-Wochentagen besondere Ereignisse wie Feiertage in weiteren Spalten anzuzeigen.

> Schichtbedarf für gelöschte Tagestypen oder Tagesmodelle
>
> Elemente, die der Planungseinheit noch zugeordnet sind, werden kursiv dargestellt und sind nicht mehr änderbar. Entferne die Zuordnung von alten Tagesmodellen oder Tagestypen zur Planungseinheit, um sie aus der Tabelle zu entfernen.

## Schichtbedarf bearbeiten

1. Wähle eine **Planungseinheit**.
2. Editiere die **Min/Max-Werte** für ein oder mehrere Tagesmodelle.
3. Klicke auf _Speichern_{:.doc-button}.

## Bedeutung der Minimal- und Maximalwerte

Die einzelnen Einträge definieren pro Tagesmodell und Tagestyp, wie viele Schichten von der Schichterzeugung minimal bzw. maximal erzeugt werden können. Die Anzahl der Mitarbeiter und deren mögliche Schichten werden nicht berücksichtigt. injixo zielt nur auf die bestmögliche Deckung ab.

Wenn Du nicht nur mit Minimalwerten arbeitest, ist der {% link_new Mitarbeiterbedarf | features/scheduling/edit-or-delete-staff-requirements.md %} relevant. Es werden (bis zum eingetragenen Maximum) die Anzahl Schichten erzeugt, die zur Deckung des Mitarbeiterbedarfs notwendig sind.

## Benötigte Schichten in die Tabelle eintragen

Nutze den Wert 0 für das Minimum und Maximum eines Tagesmodells, um dafür keine Schichten zu erzeugen, z.B. an Tagen, an denen die Planungseinheit geschlossen ist oder wenn Du bestimmte Schichten nicht im Schichtwunsch-Verfahren verwenden willst.

Nutze den gleichen Wert für Minimum und Maximum, um eine fixe Anzahl Schichten zu erzeugen, z.B. für Tagesmodelle, die unabhängig vom Mitarbeiterbedarf immer gleich besetzt werden sollen.

Für die übrigen Tagesmodelle gehe vor jeder Planung wie folgt vor, um die richtigen Werte pro Tagesmodell zu ermitteln und einzutragen:

1. Ermittle, welche Mitarbeiter Vollzeit arbeiten und welche Teilzeit. Zähle jeweils die Mitarbeiter. Idealerweise hast Du eine {% link_new Auswahl | features/administration/selections.md %} für Vollzeit- und Teilzeit-Mitarbeiter.
2. Überlege Dir, wie die verfügbaren Tagesmodelle verteilt sein sollen. Es kann z.B. sinnvoll sein, mehr kurze Teilzeit-Schichten am Vormittag und mehr Vollzeit-Schichten am Nachmittag zu erzeugen.
3. Überlege, wie viele Schichten Du jeweils zum Wünschen anbieten möchtest. Alle Mitarbeiter sollten sich eine Schicht wünschen können, wenn Du für die Planerstellung nur das Schichtwunsch-Verfahren nutzt.
4. Ziehe ggf. Krankheiten und andere Abwesenheiten von der Gesamtzahl der benötigten Schichten ab.
5. Trage Werte für Minimum und Maximum pro Tagesmodell in die Tabelle ein.

> Hinweise
>
> **Schichten in Schichtfolgen**
>
> Wird ein Tagesmodell bereits zweimal in Schichtfolgen verwendet und Du benötigst mindestens drei weitere Schichten eines Tagesmodells, erhöhe den Wert entsprechend und trage als Minimum einen Wert von fünf ein.
>
> **Interpretation von fehlenden Einträgen**
>
> Gibst Du in der Tabelle keine Werte vor, erzeugt die Schichterzeugung beliebig viele Schichten zur Deckung des Mitarbeiterbedarfs. In injixo Enterprise on-premise definiert Einstellung _48128_{:.id-label} _Interpretation von fehlenden Einträgen für Schichtbedarf_, ob für leere Felder keine (Wert 0) oder beliebig viele Schichten (Wert 1) erzeugt werden.

## Kennzahlen im Schicht Center

Das _Schicht Center_{:.menu-item} zeigt die erzeugten Schichten für jedes einzelne Tagesmodell. Du findest die Kennzahl _Bedarf_ im Kennzahlenfenster auf dem Arbeitsblatt _Tagesmodelle_.
Darüber hinaus findest Du weitere Kennzahlen auf dem Arbeitsblatt _Aktivitäten_, indem Du einen Rechtsklick im Kennzahlenfenster ausführst ({% link_new Screenshot | features/scheduling/shiftcenter/shift-center-overview.md | #kennzahlenfenster %}:

| Kennzahl                    | Bedeutung                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Besetzung lt. Schichtbedarf | Die Kennzahl gibt an, wie viele Schichten mit der ausgewählten Aktivität im angezeigten Zeitintervall durch die Schichterzeugung erzeugt wurden, um den Mitarbeiterbedarf für diese Aktivität zu decken. Sie zeigt die Qualität einer Schichterzeugung, denn hier ist abzulesen, wie der Mitarbeiterbedarf gedeckt werden würde, wenn alle erzeugten Schichten besetzt würden. |
| Deckung lt. Schichtbedarf   | Die Kennzahl zeigt die Differenz zwischen den Schichten, die im angezeigten Zeitintervall benötigt werden, und den bei der Schichterzeugung tatsächlich erzeugten Schichten.                                                                                                                                                                                                   |

## Kennzahlen in Dashboards

{% link_new Dashboards | features/monitoring/dashboards/manage-dashboards.md %} zeigt folgende Kennzahlen für Schichten:

| Kennzahl              | Bedeutung                                                                         |
| --------------------- | --------------------------------------------------------------------------------- |
| Bedarf                | Anzahl der benötigten Schichten.                                                  |
| Besetzung             | Anzahl der tatsächlichen Schichten.                                               |
| Wünsche               | Anzahl der gewünschten Schichten.                                                 |
| Deckung               | Differenz zwischen benötigten und tatsächlichen Schichten.                        |
| Deckung inkl. Wünsche | Differenz zwischen benötigten und tatsächlichen Schichten, inklusive der Wünsche. |
