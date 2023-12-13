---
title: Optimierten Schichtplan erstellen
description: Lerne, was ein optimierter Schichtplan ist, mit welchen Einstellungen Du injixo auf die Optimierung vorbereitest und wie Du einen optimierten Schichtplan erstellst.
product_label:
  - advanced
  - enterprise
---

In diesem Artikel lernst Du  
* Was ein optimierter Schichtplan ist.
* Wie Du injixo konfigurierst, um die besten Optimierungsergebnisse zu erzielen.
* Wie Du einen optimierten Schichtplan erstellst.

## Was ist ein optimierter Schichtplan?

Das Feature *Optimierten Plan erstellen* (auch Volloptimierung oder AutoScheduler genannt) erstellt automatisch einen kompletten Schichtplan mit der bestmöglichen Deckung für alle Aktivitäten mit der geringstmöglichen Anzahl an Mitarbeitern. Der Schichtplan wird auf der Grundlage des Mitarbeiterbedarfs für die verschiedenen Aktivitäten erstellt.

## injixo konfigurieren, um optimale Ergebnisse zu erzielen

Um mit dem Feature *Optimierten Plan erstellen* die besten Ergebnisse zu erzielen, musst Du injixo zuvor korrekt konfigurieren:

* Konfiguriere Deine {% link_new Mitarbeiter | features/administration/employee-overview.md %}.
* Überprüfe die Planungsparameter und AutoScheduler-Parameter Deiner Verträge unter *WFM > Administration > Scheduling > Verträge*{:.breadcrumbs}. Die Optimierung muss sich an diese Einstellungen halten.
* Füge der Planungseinheit alle Tagesmodelle hinzu, die die Optimierung verwenden soll. Die Optimierung berücksichtigt alle Tagesmodelle der Planungseinheit.
* Stelle sicher, dass die Planungseinheit Öffnungszeiten hat und dass die Schichten zu den Öffnungszeiten passen.
* Die Länge der verfügbaren {% link_new Tagesmodelle | features/administration/daymodels/daymodel-creation.md %} muss mit den vertraglichen Arbeitszeiten der Mitarbeiter übereinstimmen.
* Die Aktivitäten, die durch die Optimierung geplant werden, müssen als *Planbar* konfiguriert sein. Diese Aktivitäten ersetzen dann falls nötig als *Ersetzbar* konfigurierte Aktivitäten.
* Verwende {% link_new Planungsmodelle | features/administration/work-time-pattern-models.md %} für Mitarbeiter, wenn Du die möglichen Arbeitszeitkombinationen für die Optimierung einschränken willst.
* Überprüfe die Einstellungen für den {% link_new Stellenwert | best-practices/importance-for-activities.md %} und die {% link_new Priorität | best-practices/priority-for-activities.md %} der Aktivitäten. Sie legen fest, welche Aktivitäten andere Aktivitäten überschreiben können und welche Aktivitäten bei der Optimierung vorrangig behandelt werden.

## Optimierten Schichtplan erstellen

1. Gehe zu *Plan > Schedules*{:.breadcrumbs}.
2. Klicke auf *Planungsaktionen*{:.doc-button}.
3. Klicke auf **Optimierten Plan erstellen**.
4. Wähle einen **Zeitraum** für die Optimierung. Der Zeitraum ist mit dem aktuell ausgewählten Zeitbereich in Schedules vorausgefüllt.
5. Wähle eine **Planungseinheit**.
6. Wähle eine **Auswahl** (optional), wenn Du die Optimierung nur auf eine bestimmte Auswahl an Mitarbeitern anwenden willst.
7. Aktiviere die Checkbox **Erneute Optimierung**, wenn Du bereits zuvor einen optimierten Schichtplan erstellt hattest, der Planungsmodelle vom Typ C enthält und Du die Reihenfolge der verwendeten Wochenmodelle ändern möchtest. Andernfalls wird injixo die gleiche Reihenfolge der Wochenmodelle verwenden wie zuvor. Bevor Du den Schichtplan neu erstellst, musst Du den bestehenden Schichtplan löschen.
8. Klicke auf *Optimierten Plan erstellen*{:.doc-button}. Du siehst eine grüne Benachrichtigung, wenn die Optimierung erfolgreich gestartet wurde. Eine rote Meldung erscheint, wenn die Optimierung nicht gestartet werden konnte.

{{ 1 | image: 'Dialogfenster zum Erstellen eines optimierten Schichtplanes', '70%' }}

Die Optimierung kann je nach Datenmenge und gewähltem Zeitraum einige Zeit dauern. Währenddessen kannst Du im zu optimierenden Zeitraum keine Änderungen am Schichtplan vornehmen. Wenn der Job beendet ist, speichert injixo das Ergebnis automatisch.

Gehe zu *WFM > Administration > System > JobProcessor*{:.breadcrumbs}, um den Fortschritt einer laufenden Optimierung zu sehen. Dort findest Du auch einen Link zum {% link_new Planungsreport | best-practices/resolve-optimization-issues.md %}, sobald der Prozess beendet ist. Dieser hilft Dir, Planungsfehler zu finden und zu beheben, die während des Optimierungsprozesses aufgetreten sind.
