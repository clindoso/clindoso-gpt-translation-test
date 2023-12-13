---
title: Intraday Adherence
toc: true
product_label:
  - advanced
  - enterprise
description: Erhalte einen Überblick darüber, wie genau sich deine Mitarbeiter im Laufe des Tages an ihre Schichtpläne halten.
archive_ref: 20210422-de-adherence
---

Mit Intraday Adherence kannst du die geplanten Aktivitäten deiner Mitarbeiter mit den tatsächlichen Aktivitäten vergleichen, um im Tagesverlauf Zeiträume mit Planabweichungen zu erkennen.

In Intraday Adherence werden Daten angezeigt, nachdem du den {% link_new Import von Echtzeit-Agentenstatus-Daten | features/acd-integration/cloud/import-agent-status-data.md %} eingerichtet hast.

Neu bei Echtzeit Adherence? Lerne zuerst {% link_new die Grundlagen | features/intraday/real-time-adherence.md %}.

## Daten anzeigen und suchen

1. Gehe zu _Intraday > Intraday Adherence_{:.breadcrumbs}.
2. Um Agentendaten anzuzeigen, wähle eine Planungseinheit und/oder eine Auswahl.
3. Um den angezeigten Tag zu ändern, klicke auf _Heute_{:.doc-button} oder _Gestern_{:.doc-button} oder verwende die Datumsauswahl.

Die Tabelle zeigt die Details zu den Planabweichungen pro Mitarbeiter. Im Tabellenkopf kannst du Zeiträume mit geringer Planeinhaltung erkennen. Du kannst die Tabelle sortieren oder die Suche oben nutzen, um die {% link_new Ansicht zu filtern | features/intraday/real-time-adherence.md | #die-ansicht-filtern-und-sortieren %}.

{{ 1 | image: 'Intraday Adherence','100%' }}

> Begrenze die Ansicht für bestimmte Mitarbeiter auf relevante Benutzer
>
> Konfiguriere Berechtigungen für bestimmte Planungseinheiten oder Auswahlen pro {% link_new Benutzer oder Benutzerrolle | getting-started/configure-user-roles.md | #berechtigungen-für-wfm-konfigurieren %}.

## Adherence Score

Der Adherence Score ist der Zielwert für die Planeinhaltung und zeigt an, ob es Abweichungen zwischen den tatsächlichen und geplanten Aktivitäten der Mitarbeiter gab.

Du kannst die Planeinhaltung im Tagesverlauf anhand der grafischen Darstellung auswerten. Vor dem Tagesende wird der Score bis zum Zeitstempel der letzten Aktualisierung berechnet, der über dem Adherence Score angezeigt wird.

Die gestrichelte Linie zeigt an, wo der Zielwert für die Planeinhaltung liegt. Du kannst den {% link_new Zielwert anpassen | features/intraday/real-time-adherence.md | #zielwert-für-die-planeinhaltung-festlegen %}.

{{ 2 | image: 'Adherence Score','100%' }}

## Tabelle mit Agentendetails

Die Tabelle zeigt die Details zur Planeinhaltung deiner heute geplanten Mitarbeiter. Die Tabelle ist nach Mitarbeitername und Adherence Score sortierbar.

Jede Tabellenzeile enthält eine Zeitreihe eines Mitarbeiters. Du siehst die Unterschiede zwischen den geplanten und den tatsächlich ausgeführten Aktivitäten des Mitarbeiters. Jeder Mitarbeiter hat einen eigenen Adherence Score. Die Einzelwerte ergeben den Gesamtwert für die Planungseinheit (angezeigt im Tabellenkopf). Abweichungen werden hervorgehoben, wenn der Wert unter den {% link_new konfigurierten Zielwert für die Planeinhaltung | features/intraday/real-time-adherence.md | #zielwert-für-die-planeinhaltung-festlegen %} fällt.

Die Farben zeigen die drei Typen der Planabweichung an:

- Nicht Anwesend (rot)
- Falsche Aktivität (gelb)
- Nicht Geplant (blau)

Klicke auf einen Agenten, um dessen {% link_new Agent Intraday Adherence  | features/intraday/adherence-intraday.md | #agent-intraday-adherence %}, also die Planeinhaltung im Tagesverlauf zu sehen. {% link_new Matches | features/intraday/adherence-matches.md %} und {% link_new Toleranzzeiten | features/intraday/real-time-adherence.md | #toleranzzeiten-festlegen %} wirken sich auf Änderungen bei Status und Typen der Planabweichung aus. Erfahre mehr über {% link_new Status und Typen der Planabweichung | features/intraday/real-time-adherence.md | #den-status-verstehen %}.

{{ 3 | image: 'Agentenübersichtstabelle','100%' }}

## Agent Intraday Adherence

Die Ansicht Agent Intraday Adherence zeigt Details zu Planabweichungen. Du siehst, wo Mitarbeiter nicht plankonform waren. Um zu verstehen, was ein Mitarbeiter im Laufe des Tages getan hat, klicke auf einen Eintrag in der Tagesübersicht. In der Ansicht werden einzelne Aktivitäten in den konfigurierten Farben angezeigt.

In der Zeitreihe kannst du die geplanten und tatsächlich ausgeführten Aktivitäten vergleichen und die daraus folgende Planabweichung sehen. Die Tabelle darunter enthält eine Zeile je Zeitraum, der nicht plankonform war.

Um den angezeigten Tag zu ändern, kannst du:

- die Monatsauswahl oben und die Tagesübersicht links nutzen.
- die Navigationspfeile neben dem aktuellen Datum über der Tabelle verwenden.

Die Tagesübersicht zeigt für jeden Tag des ausgewählten Monats den Zielwert für die Planeinhaltung. Oberhalb der Tagesansicht siehst du verschiedene Kennzahlen für den ausgewählten Monat, zum Beispiel den Zielwert für die Planeinhaltung und die geplante Dauer einer Aktivität.

{{ 4 | image: 'Die Ansicht Agent Intraday Adherence im Detail','100%' }}

## Planeinhaltungsreport (CSV-Datei)

Es kann vorkommen, dass du die Daten zur Planeinhaltung bezüglich Arbeitszeit und Aktivitäten für einzelne Mitarbeiter über einen längeren Zeitraum auswerten musst, zum Beispiel für die Berechnung von Bonuszahlungen. Der Planeinhaltungsreport ist eine CSV-Datei, die aggregierte Daten für die Planeinhaltung der Arbeitszeit und der Aktivitäten beinhaltet. Um ihn herunterzuladen, gehe wie folgt vor:

1. Gehe zu _Intraday > Intraday Adherence_{:.breadcrumbs}.
2. Wähle eine Planungseinheit und/oder eine Auswahl.
3. Klicke auf _Report herunterladen_{:.doc-button}.  
   Ein Fenster öffnet sich.
4. Wähle einen Datumsbereich für den Report aus. Du kannst einen Datumsbereich von einem Tag bis zu sechs Monaten in der Vergangenheit wählen.
5. Klicke auf _Report herunterladen_{:.doc-button}.

Die folgende Tabelle erklärt die Report-Spalten:

| Spalte             | Erklärung                                                                     | Berechnung                                                                |
| ------------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Minutes in Adherence | Zeit, die für Aktivitäten aufgewendet wird, die den geplanten Aktivitäten entsprechen      | -- |
| Minutes out of Adherence  | Zeit, die für Aktivitäten aufgewendet wird, die nicht den geplanten Aktivitäten entsprechen        | -- |                  
| Adherence in %   | Prozentualer Anteil der Arbeitszeit, die für Aktivitäten aufgewendet wird, die den geplanten Aktivitäten entsprechen       | Plankonforme Minuten/geplante Minuten * 100% |
| Minutes out of Conformance   | Die Differenz zwischen der tatsächlichen Arbeitszeit und der geplanten Zeit             | Tatsächliche Arbeitszeit in Minuten - geplante Minuten |
| Conformance in % | Prozentualer Anteil der Arbeitszeit, der mit der geplanten Arbeitszeit übereinstimmt | Tatsächliche Zeit/geplante Zeit * 100% |
| Scheduled in %  | Der prozentuale Anteil an geplanter Arbeitszeit für eine Aktivität eines bestimmten Typs | Geplante Zeit für den entsprechenden Aktivitätstyp/insgesamt geplante Zeit * 100%              |
| Actual in %  | Der prozentuale Anteil der tatsächlichen Arbeitszeit, die für eine Aktivität eines bestimmten Typs aufgewendet wurde | Tatsächliche Zeit für den entsprechenden Aktivitätstyp/gesamte tatsächliche Zeit * 100%              |

Jede Datenzeile enthält einen Link, um die entsprechenden Daten in _Intraday > Intraday Adherence_{:.breadcrumbs} anzuzeigen.

## Häufig gestellte Fragen

| Frage                            | Antwort                                                                                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Warum fehlen einige oder alle Mitarbeiter? | Versuche, die Suche zu löschen. Überprüfe, ob die fehlenden Mitarbeiter für den heutigen Tag in der ausgewählten Planungseinheit bzw. Auswahl geplant sind.           |
| Warum kann ich ein bestimmtes Datum nicht auswählen? | Du kannst auf historische Daten zur Planeinhaltung aus den letzten sechs Monaten zugreifen, plus dem aktuellen Monat (wenn z.&nbsp;B. heute der 15.&nbsp;Juli ist, kannst du Daten zwischen dem 1.&nbsp;Januar und dem 15.&nbsp;Juli auswählen). |
