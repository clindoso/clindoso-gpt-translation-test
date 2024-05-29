---
title: Intraday Adherence verwenden
toc: true
product_label:
  - advanced
  - enterprise
description: Erhalte einen Überblick darüber, wie genau sich deine Mitarbeiter im Laufe des Tages an ihre Schichtpläne halten.
archive_ref: 20210422-de-adherence
---

Unter _Intraday > Intraday Adherence_{:.breadcrumbs} kannst du die geplanten Aktivitäten deiner Mitarbeiter mit ihren tatsächlichen Aktivitäten vergleichen, um historische Zeiträume mit Planabweichungen im Tagesverlauf zu erkennen. Intraday Adherence verwendet {% link_new Echtzeit-Adherence | features/intraday/real-time-adherence.md %}-Daten von deiner ACD. Du kannst auf die Daten zur Planeinhaltung des aktuellen und der vergangenen sechs Monate zugreifen.

## Voraussetzungen

Um Daten zur Planeinhaltung einsehen zu können, stelle sicher, dass folgendes zutrifft:

- Du hast eine {% link_new Integration | features/acd-integration/cloud/how-integrations-work.md %} hinzugefügt, die den Import von Agentenstatus-Daten unterstützt.
- Du hast den {% link_new Import von Agentenstatus-Daten | features/acd-integration/cloud/import-agent-status-data.md %} eingerichtet.

## Daten anzeigen

Um Daten zur Planeinhaltung für einen bestimmten Tag anzuzeigen, gehe wie folgt vor:

1. Wähle eine **Planungseinheit** und/oder eine **Auswahl**.
2. Wähle oben auf der Seite mit der Datumsauswahl ein Datum aus oder klicke stattdessen auf _Heute_{:.doc-button} bzw. _Gestern_{:.doc-button}.

Die Seite zeigt den Gesamt-Adherence-Score, die Adherence Scores je Intervall und eine Tabelle mit den Details zu den Planeinhaltungsdaten pro Mitarbeiter für den ausgewählten Tag an.

### Adherence Score

Die Seite zeigt verschiedene Details zum Adherence Score an:

- **Adherence**: Prozentsatz der Arbeitszeit, die für geplante Aktivitäten aufgewendet wird. Wenn der Arbeitstag noch nicht zu Ende ist, wird der Prozentsatz bis zum zuletzt aktualisierten Zeitstempel ermittelt, der über dem Wert angezeigt wird. Wenn der Wert unter den {% link_new Zielwert für die Planeinhaltung | features/intraday/real-time-adherence.md | #zielwert-für-die-planeinhaltung-festlegen %} fällt, wird er rot hervorgehoben.
- **Adherence Score je Intervall**: Vertikale blaue Balken zeigen die Werte zur Planeinhaltung je Intervall. Wenn Werte unter 100&nbsp;% liegen, bedeutet dies, dass im jeweiligen Intervall die tatsächlichen Aktivitäten der Mitarbeiter von ihren geplanten Aktivitäten abweichen.
- **Zielwert für die Planeinhaltung**: Die gestrichelte Linie im Diagramm zeigt den konfigurierten Zielwert an.

<!-- Adherence in %	Percentage of working time spent in activities that comply with the scheduled activities	Minutes in adherence/scheduled minutes * 100% -->

### Tabelle mit Mitarbeiterdetails

Unter dem Gesamt-Adherence-Score und den Werten pro Intervall zeigt eine Tabelle Details zur Planeinhaltung für den ausgewählten Tag an. Um die Tabelle nach dem Wert für die Planeinhaltung zu sortieren, klicke in der Kopfzeile auf **Adherence**. Um die Tabelle nach den Namen der Mitarbeiter zu sortieren, klicke in der Kopfzeile auf **Name**. Erfahre mehr darüber, wie du die Ansicht {% link_new filtern und sortieren | features/intraday/real-time-adherence.md | #die-ansicht-filtern-und-sortieren %} kannst.
Jede Zeile zeigt den Adherence Score eines Mitarbeiters. Die Unterschiede zwischen den geplanten Aktivitäten der Mitarbeiter und ihren tatsächlichen Aktivitäten werden hervorgehoben.

Wenn der Wert zur Planeinhaltung eines Mitarbeiters unter den konfigurierten Zielwert für die Planeinhaltung fällt, wird dieser Wert rot hervorgehoben. {% link_new Matches | features/intraday/adherence-matches.md %} und {% link_new Toleranzzeiten | features/intraday/real-time-adherence.md | #toleranzzeiten-festlegen %} können sich auf Änderungen bei Status und Typen der Planabweichung auswirken. Erfahre mehr über die {% link_new Status und die Typen der Planabweichung | features/intraday/real-time-adherence.md | #den-status-verstehen %}.

Verschiedene Farben zeigen an, um welchen Typen der Planabweichung es sich handelt:

- Rot: Nicht anwesend
- Gelb: Falsche Aktivität
- Blau: Nicht geplant

## Agent Intraday Adherence

Um die Details zur Planeinhaltung eines Mitarbeiters in einem neuen Fenster anzuzeigen, klicke in der Tabelle auf dessen Zeile. Um das Datum zu ändern, verwende die Monatsauswahl oder die Navigationspfeile links und rechts des Datums.

Auf der linken Seite geben zwei Kästen einen Überblick über den ausgewählten Monat:

- **Name des Mitarbeiters**: Zeigt den Adherence Score des Mitarbeiters an, für wie lange er geplant war und Details zur Planeinhaltung für den ausgewählten Monat. Die Werte basieren auf den Daten bis zum letzten abgeschlossenen Intervall des aktuellen Tages.
- **Tagesübersicht**: Tage, für die Werte zur Planeinhaltung verfügbar sind, sind rot hervorgehoben. Bewege den Mauszeiger über ein Datum, um den Adherence Score für den ausgewählten Mitarbeiter anzuzeigen. Klicke auf ein Datum, um die Details anzuzeigen.

Auf der rechten Seite siehst du im Detail, für welchen Zeitraum der Mitarbeiter geplant war und wo er vom Schichtplan abgewichen ist:

- Wert für **Intraday Adherence**: Dieser Wert berechnet sich aus den Daten bis zum letzten abgeschlossenen Intervall des aktuellen Tages. Er ist identisch mit dem Tageswert für die Planeinhaltung, wenn du im Abschnitt **Tagesübersicht** den Mauszeiger über ein Datum bewegst.
- Dauer für **Geplant** und **Abweichung**: Gesamtdauer aller geplanten Aktivitäten (Aktivitätstypen Anwesend, Meeting, Pause) und Abweichungen im Schichtplan am ausgewählten Datum.
- **Zeitachse**: Farbige Balken markieren geplante Aktivitäten, tatsächliche Aktivitäten und den Status der Planabweichung. In der Zeile **Abweichung** kannst du auf Zeiträume zoomen, die nicht plankonform sind. Klicke zum Hineinzoomen den jeweiligen Zeitraum an und zum Herauszoomen auf _Zoom zurücksetzen_{:.doc-button}.
- **Tabelle**: Jede Zeile zeigt Details zu Zeiträumen in Planabweichung. Klicke auf eine Spaltenüberschrift, um die Daten nach Zeitraum, tatsächlicher Aktivität, Status, geplanter Aktivität oder Abweichungsdauer zu sortieren.

## Planeinhaltungsreport (CSV-Datei)

Wenn du die Daten zur Planeinhaltung bezüglich Arbeitszeit und Aktivitäten für einzelne Mitarbeiter über einen längeren Zeitraum analysieren möchtest, z.&nbsp;B. um Bonuszahlungen zu berechnen, kannst du einen Report als CSV-Datei herunterladen. Dieser enthält aggregierte Daten zur Planeinhaltung. Um den Planeinhaltungsreport herunterzuladen, gehe wie folgt vor:

1. Wähle eine **Planungseinheit** und/oder eine **Auswahl**.
2. Klicke auf _Report herunterladen_{:.doc-button}.
3. Wähle im Bestätigungsfenster einen Datumsbereich für den Report aus. Du kannst einen Datumsbereich von einem Tag bis zu sechs Monaten in der Vergangenheit wählen.
4. Klicke auf _Report herunterladen_{:.doc-button}.

Die folgende Tabelle erklärt die Report-Spalten:

| Spalte                     | Erklärung                                                                                                            | Berechnung                                                                               |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Activity                   | Aktivität, für die die Daten zur Planeinhaltung angezeigt werden                                                     | --                                                                                       |
| Scheduled Minutes          | Für die Aktivität geplante Dauer in Minuten                                                                          | --                                                                                       |
| Actual Minutes             | Für die geplante Aktivität tatsächlich aufgewendete Zeit in Minuten                                                  | --                                                                                       |
| Minutes in Adherence       | Zeit, die für Aktivitäten aufgewendet wird, die den geplanten Aktivitäten entsprechen                                | --                                                                                       |
| Minutes out of Adherence   | Zeit, die für Aktivitäten aufgewendet wird, die nicht den geplanten Aktivitäten entsprechen                          | --                                                                                       |
| Adherence in %             | Prozentualer Anteil der Arbeitszeit, die für Aktivitäten aufgewendet wird, die den geplanten Aktivitäten entsprechen | Plankonforme Minuten/geplante Minuten \* 100%                                            |
| Minutes out of Conformance | Differenz zwischen der tatsächlichen Arbeitszeit und der geplanten Zeit                                              | Tatsächliche Arbeitszeit in Minuten - geplante Minuten                                   |
| Conformance in %           | Prozentualer Anteil der Arbeitszeit, der mit der geplanten Arbeitszeit übereinstimmt                                 | Tatsächliche Zeit/geplante Zeit \* 100%                                                  |
| Scheduled in %             | Prozentualer Anteil an geplanter Arbeitszeit für eine Aktivität eines bestimmten Typs                                | Geplante Zeit für den entsprechenden Aktivitätstyp/insgesamt geplante Zeit \* 100%       |
| Actual in %                | Prozentualer Anteil der tatsächlichen Arbeitszeit, die für eine Aktivität eines bestimmten Typs aufgewendet wurde    | Tatsächliche Zeit für den entsprechenden Aktivitätstyp/gesamte tatsächliche Zeit \* 100% |

Jede Datenzeile enthält einen Link, um die entsprechenden Daten in _Intraday > Intraday Adherence_{:.breadcrumbs} anzuzeigen.

## Häufig gestellte Fragen

| Frage                                                | Antwort                                                                                                                                                                                                                                                            |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Warum fehlen einige oder alle Mitarbeiter?           | Versuche, die Suche zu löschen. Überprüfe, ob die fehlenden Mitarbeiter für den heutigen Tag in der ausgewählten Planungseinheit bzw. Auswahl geplant sind.                                                                                                        |
| Warum kann ich ein bestimmtes Datum nicht auswählen? | Du kannst auf historische Daten zur Planeinhaltung bis zu sechs Monate vor dem aktuellen Datum zugreifen inklusive dem aktuellen Monat (wenn z.&nbsp;B. heute der 15.&nbsp;Juli ist, kannst du Daten zwischen dem 1.&nbsp;Januar und dem 15.&nbsp;Juli auswählen). |
| Welche Zeitzone verwendet Intraday Adherence?        | Intraday Adherence verwendet die Zeitzone der ausgewählten Planungseinheit. Die Zeitzone wird rechts oberhalb der gestrichelten Linie für den Zielwert angezeigt.                                                                                                  |
