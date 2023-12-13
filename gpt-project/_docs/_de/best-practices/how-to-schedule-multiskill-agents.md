---
title: Multiskill-Agenten planen
product_label:
  - advanced
  - enterprise
  - classic
description: Plane Multiskill-Agenten mit der optimierten Schichtplanung.
toc: true
---

Contact Center bieten ihren Kunden mehrere Möglichkeiten der Kontaktaufnahme, die mehrere Qualifikationen erfordern, z.&nbsp;B. Telefon für Bestellungen oder E-Mail und Chat für Reklamationen. Nicht jeder Agent ist dabei in allen Bereichen geschult und kann daher nicht in jede Aufgabe übernehmen.

## Abbildung in injixo

Die optimierte Schichtplanung in injixo unterstützt Multiaktivitäten, mit denen du Multiskill- oder Multikanal-Tätigkeiten planen kannst.

Jeder Eingangskanal steht für eine Teilaktivität und jede Qualifikation eines Mitarbeiters entspricht einer Qualifikation in injixo. Während der Schichtplanung werden alle Mitarbeiterqualifikationen gleichzeitig in die Berechnung des Mitarbeiterbedarfs einbezogen. Dies führt zu sogenannten Pooling-Effekten, d.&nbsp;h. der Gesamtbedarf an Agenten wird minimiert, weil alle notwendigen Qualifikationen durch weniger Mitarbeiter abgedeckt werden.

## Empfohlener Ansatz

1. Lege eine {% link_new Multiaktivität | features/administration/activity-types-and-properties.md | #teilaktivitäten %} an.

2. Erstelle einen Forecast. Für Multiaktivitäten benötigst du einen Workload für jeden Eingangskanal.

3. Berechne den Mitarbeiterbedarf für die Multiaktivität mithilfe des Skripts `Calls - Multiactivity`. Für Multikanal gibt es weitere Parameter, z.&nbsp;B. für Chat den Parameter `seq. (%)` und die maximale Anzahl an gleichzeitigen Sessions, siehe {% link_new  | features/forecast/requirement-scripts/requirement-multiactivity.md %} und {% link_new Chat Bedarf | features/forecast/requirement-scripts/requirement-chat.md  %}.

4. Führe die Funktion **Optimierten Plan erstellen** aus.

### Planungsergebnis

In _Schicht Center_{:.menu-item} zeigt der Schichtplan nur die Multiaktivität an. Die Teilaktivitäten werden im Parameterfenster angezeigt:

{{ 2 | image: "Schicht Center mit Kennzahlen zur Multiaktivität" }}

> Hinweis
>
> Es ist nicht möglich, die Werte des Mitarbeiterbedarfs für die einzelnen Teilaktivitäten aufzuaddieren, um so den Mitarbeiterbedarf für die Multiaktivität zu ermitteln.
>
> Der Mitarbeiterbedarf für die Multiaktivität ist immer identisch mit der Anzahl der Personen, die geplant wurden. Das Schicht Center zeigt keine absoluten Zahlen für Teilaktivitäten, sondern wie viele Personen qualifiziert sind, die Aufgabe auszuführen. Wenn Personen für mehrere Teilaktivitäten qualifiziert sind, kann der Mitarbeiterbedarf für die Teilaktivitäten genauso hoch sein wie das Maximum des Mitarbeiterbedarfs für die Multiaktivität. 

Du kannst sehen, welcher Mitarbeiter an welchen Teilaktivitäten arbeitet. Um dir Details zu Multiaktivitäten anzusehen, doppelklicke auf eine Tageszelle in Schicht Center und wähle den Tab **Multiaktivitäten**.

{{ 1 | image: "Teilaktivitäten im Schicht-Center-Dialog", '60%' }}

Für die Tagessteuerung kannst du dir die Deckung und Besetzung für die Teilaktivitäten auf {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %} ansehen. Ziehe die Besetzung für einzelne Teilaktivitäten und die Multiaktivität in das Diagramm.

{{ 3 | image: "Dashboard mit Besetzung für Multiaktivität" }}
