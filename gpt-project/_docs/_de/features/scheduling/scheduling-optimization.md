---
title: Schichtpläne optimieren
redirect_from: /de/autoscheduler-overview/
redirect_reason: deleted autoscheduler-overview Oct 2020
description: Erfahre mehr über die drei verfügbaren Optimierungsprozesse, die Job-/Pausen- und vollständige Optimierung (SchedulePro).
product_label:
  - classic
promote-service: schedule-optimization-workshop
---

In diesem Artikel lernst Du  
- Welche Optimierungsprozesse zur Verfügung stehen.
- Wie Du diese ausführst.
- Welchen Einfluss sie auf Deine Planung haben.

> In diesem Artikel geht es um *WFM > Scheduling > SchedulePro*{:.breadcrumbs}.
>
> Wenn Du injixo Advanced WFM oder Enterprise WFM verwendest, nutze stattdessen die Funktionen {% link_new Pausenoptimierung | features/scheduling/schedules/break-optimization.md %}, {% link_new Joboptimierung | features/scheduling/schedules/schedules-job-optimization.md %} und {% link_new Volloptimierung | features/scheduling/schedules/schedules-optimized-schedules.md %} unter *Plan > Schedules*{:.breadcrumbs}.  

injixo unterscheidet drei Optimierungsprozesse:  

* **Volloptimierte Planung:** Erstelle automatisiert einen bedarfsorientierten Dienstplan auf Basis von Stammdaten und Mitarbeiterbedarfen.
* **Joboptimierung:** Optimiere einen bereits bestehenden Dienstplan, um ersetzbare Aktivitäten mit planbaren Aktivitäten auszutauschen, um den jeweiligen Bedarf bestmöglich zu decken. Zusätzlich wird eine Pausenoptimierung durchgeführt.
* **Pausenoptimierung:** Optimiere die Pausenpositionen bestmöglich im Hinblick auf die Deckung der übrigen Aktivitäten nach Änderungen an der aktuellen Planung. Pausen können nur innerhalb von {% link_new Korridoren in Tagesmodellen | features/administration/daymodels/daymodel-basics.md | #feste-elemente-vs-korridore %} verschoben werden.

Optimierungen können einige Zeit dauern, abhängig von der Datenmenge und gewähltem Zeitraum. Währenddessen kannst Du in diesem Zeitraum keine Änderungen am Schichtplan vornehmen. injixo speichert das Ergebnis automatisch.

> injixo Enterprise on-premise
>
> Der Menüpunkt *WFM > Scheduling > SchedulePro > Optimierung*{:.breadcrumbs} steht *nicht* zur Verfügung. Die volloptimierte Planung heißt hier *AutoScheduler*{:.menu-item}. Starte Optimierungen direkt aus dem *Schicht Center*{:.menu-item} oder die Joboptimierung über *Planperioden*{:.menu-item}. Sie werden standardmäßig manuell auf Knopfdruck gespeichert und laufen nicht über den JobProcessor. Die AutoScheduler-Benutzeroberfläche zeigt ihren Fortschritt an.  

Die Übersichtsseite in *WFM > Scheduling > SchedulePro > Optimierung*{:.breadcrumbs} zeigt alle Optimierungen. Der angezeigte Verarbeitungsstatus bei laufenden Optimierungen aktualisiert sich automatisch. Abgeschlossene Optimierungen haben den Status *Fertig*.

Betrachte den Fortschritt einer laufenden Optimierung in *Administration > System > JobProcessor*{:.breadcrumbs}. Dort findest Du auch einen Link zum PDF-Report. Erfahre mehr über den {% link_new Planungsreport | best-practices/resolve-optimization-issues.md %}, der Planungsfehler auflistet.

## Was ist die Volloptimierung?

Das Feature *Volloptimierter Plan* (auch AutoScheduler genannt) erstellt automatisch einen kompletten Schichtplan mit der bestmöglichen Deckung für alle Aktivitäten mit der geringstmöglichen Anzahl an Mitarbeitern. Der Schichtplan wird auf der Grundlage des Mitarbeiterbedarfs für die verschiedenen Aktivitäten erstellt.

Um mit dem Feature *Volloptimierter Plan* die besten Ergebnisse zu erzielen, musst Du injixo zuvor korrekt konfigurieren:

* Konfiguriere Deine {% link_new Mitarbeiter | features/administration/employee-overview.md %}.
* Überprüfe die Planungsparameter und AutoScheduler-Parameter Deiner Verträge unter *WFM > Administration > Scheduling > Verträge*{:.breadcrumbs}. Die Optimierung muss sich an diese Einstellungen halten.
* Füge der Planungseinheit alle Tagesmodelle hinzu, die die Optimierung verwenden soll. Die Optimierung berücksichtigt alle Tagesmodelle der Planungseinheit.
* Stelle sicher, dass die Planungseinheit Öffnungszeiten hat und dass die Schichten zu den Öffnungszeiten passen.
* Die Länge der verfügbaren {% link_new Tagesmodelle | features/administration/daymodels/daymodel-creation.md %} muss mit den vertraglichen Arbeitszeiten der Mitarbeiter übereinstimmen.
* Die Aktivitäten, die durch die Optimierung geplant werden, müssen als *Planbar* konfiguriert sein. Diese Aktivitäten ersetzen dann falls nötig als *Ersetzbar* konfigurierte Aktivitäten.
* Verwende {% link_new Planungsmodelle | features/administration/work-time-pattern-models.md %} für Mitarbeiter, wenn Du die möglichen Arbeitszeitkombinationen für die Optimierung einschränken willst.
* Überprüfe die Einstellungen für den {% link_new Stellenwert | best-practices/importance-for-activities.md %} und die {% link_new Priorität | best-practices/priority-for-activities.md %} der Aktivitäten. Sie legen fest, welche Aktivitäten andere Aktivitäten überschreiben können und welche Aktivitäten bei der Optimierung vorrangig behandelt werden.

### Volloptimierung starten

Gehe in *WFM > Scheduling > SchedulePro > Optimierung*{:.breadcrumbs} wie folgt vor, um eine volloptimierte Planung zu starten:

1. Wähle in der Aktionsleiste die Option *Volloptimierter Plan*{:.doc-button}.
2. Lege unter *Zeitraum* das **Startdatum und Enddatum** fest. Maximaler Zeitraum: 10 Wochen.
3. Wähle die **Planungseinheit**.
4. (Optional) Wähle unter *Auswahl* entweder **[Alle]** oder eine **Auswahl** aus dem Dropdown-Menü. Alle Mitarbeiter werden optimiert, aber die Ergebnisse werden nur für die Mitarbeiter in der Auswahl gespeichert.
5. (Optional) Verwende die Option **Erneute Optimierung**, wenn Du für beliebige Mitarbeiter einen Schichtplan neu erstellen möchtest, der Schichten aus Planungsmodellen vom Typ C enthält. In diesem Fall weiß injixo, an welchen Wochentagen die Mitarbeiter mit diesen Planungsmodellen geplant wurden. Wenn Du die Checkbox nicht setzt, werden die gleichen Wochentage wie zuvor verwendet. Du musst zuerst den ursprünglichen Schichtplan löschen.
6. Klicke *Ok*{:.doc-button}, um den Prozess zu starten.

## Was ist die Joboptimierung?

Die Funktion *Joboptimierung* tauscht Aktivitäten in den Schichtplänen Deiner Mitarbeiter aus, ohne die Anfangs- und Endzeiten der Schichten zu ändern. Ziel ist es, die bestmögliche Deckung für alle Aktivitäten zu erreichen, basierend auf den Mitarbeiterbedarfen der Aktivitäten. Auch die Pausen werden optimiert.

Verwende die Joboptimierung:
- Wenn sich die Mitarbeiterbedarfe für eine oder mehrere Aktivitäten geändert haben und Du die Deckung der Aktivitäten entsprechend optimieren möchtest.
- Wenn Du Deinen Mitarbeitern im Schichtwunsch-Verfahren mit den Funktionen *Verlosen* oder *Zuteilen*  Schichten zugewiesen hast. In diesem Fall enthalten die Schichten typischerweise nur die Aktivität *Anwesend*. Diese muss dann durch die tatsächlichen Aktivitäten ersetzt werden, jeweils basierend auf dem Mitarbeiterbedarf.
- Wenn Du Schichtfolgen für Deine Mitarbeiter eingefügt hast, die Schichten mit der Aktivität *Anwesend* oder andere als *Ersetzbar* konfigurierte Aktivitäten verwenden und Du diese Aktivitäten nun basierend auf dem Mitarbeiterbedarf austauschen möchtest.

> Verwende die Aktivität *Anwesend* in Tagesmodellen für Schichtwünsche
>  
> Wenn Du Deinen Mitarbeitern über injixo Me Schichten anbietest, ist es sinnvoll, nur die Standard-Systemaktivität namens *Anwesend* mit der ID 1 als Aktivität in den Tagesmodellen zu verwenden. Auf diese Weise verhinderst Du, dass Mitarbeiter sich zunächst Schichten mit speziellen Aktivitäten wünschen, dann aber durch die Joboptimierung ganz andere Aktivitäten zugewiesen bekommen.  

### Beispiel

Einige Mitarbeiter sind für eine Aktivität namens *Reiseverkauf* qualifiziert. Über das Schichtwunsch-Verfahren haben sie Schichten mit der Basisaktivität *Anwesend* und einer Mittagspause erhalten. Die Aktivität *Anwesend* wurde als ersetzbar definiert. Die Optimierung prüft nun, zu welchen Zeiten ein Mitarbeiterbedarf für die Aktivität *Reiseverkauf* besteht. Für diese Zeiten wird die Aktivität *Anwesend* in den Schichtplänen der Mitarbeiter durch die Aktivität *Reiseverkauf* ersetzt.

## injixo konfigurieren, um optimale Ergebnisse zu erzielen

- Konfiguriere Deine {% link_new Mitarbeiter | features/administration/employee-overview.md %}. Mitarbeiter können nur Aktivitäten erhalten, für die sie qualifiziert sind.
- Die *Job-Optimierung* funktioniert nur mit Aktivitäten, die als *Planbar* konfiguriert wurden. Diese Aktivitäten ersetzen andere Aktivitäten, die als *Ersetzbar* konfiguriert wurden.
- Stelle sicher, dass für alle Aktivitäten, die andere Aktivitäten ersetzen sollen, ein Mitarbeiterbedarf existiert. Aktivitäten ohne Mitarbeiterbedarf werden von der Optimierung nicht berücksichtigt.
- Überprüfe die Einstellungen für den {% link_new Stellenwert | best-practices/importance-for-activities.md %} und die {% link_new Priorität | best-practices/priority-for-activities.md %} der Aktivitäten. Diese legen fest, welche Aktivitäten andere Aktivitäten überschreiben können und welche Aktivitäten bei der Optimierung priorisiert werden.

### Joboptimierung ausführen

Gehe wie folgt vor, um eine Joboptimierung in *WFM > Scheduling > SchedulePro > Optimierung*{:.breadcrumbs} zu starten:

1. Wähle in der Aktionsleiste die Option *Joboptimierung*{:.doc-button}.
2. Lege unter *Zeitraum* das **Startdatum und Enddatum** fest. Maximaler Zeitraum: 10 Wochen.
3. Wähle die **Planungseinheit**.
4. (Optional) Wähle unter *Auswahl* entweder **[Alle]** oder eine **Auswahl** aus dem Dropdown-Menü. Alle Mitarbeiter werden optimiert, aber die Ergebnisse werden nur für die Mitarbeiter in der Auswahl gespeichert.
4. Klicke *Ok*{:.doc-button}, um den Prozess zu starten.

## Was ist die Pausenoptimierung?

Ziel des Features *Pausenoptimierung* ist es, die Pausen innerhalb Deines Schichtplans neu zu verteilen, um die Deckung von Aktivitäten, für die Mitarbeiterbedarf besteht, zu optimieren. Die Zeiten für Schichtbeginn und -ende bleiben dabei unverändert. Das Feature *Pausen optimieren* wandelt bestehende Tagesmodelle im Optimierungszeitraum in Aktivitäten um. Die Pausenkorridore in Tagesmodellen bleiben aber bestehen, so dass Du falls nötig weitere Pausenoptimierungen durchführen kannst.

Beispiel: Zwei Mitarbeiter haben eine Schicht mit einer Pause von 12:00 bis 13:00 Uhr. Die Pause kann alle 30 Minuten zwischen 12:00 und 15:00 Uhr beginnen. Um die niedrige Deckung für die Basisaktivität der Schicht zwischen 12:00 und 13:00 zu verbessern, wird injixo mindestens eine der Pausen auf eine spätere Zeit verschieben.

### Pausenoptimierung ausführen

Gehe wie folgt vor, um eine Pausenoptimierung in *WFM > Scheduling > SchedulePro > Optimierung*{:.breadcrumbs} zu starten:

1. Wähle in der Aktionsleiste die Option *Pausenoptimierung*{:.doc-button}.
2. Lege unter *Zeitraum* das **Startdatum und Enddatum** fest. Maximaler Zeitraum: 10 Wochen.
3. Wähle die **Planungseinheit**.
4. (Optional) Wähle unter *Auswahl* entweder **[Alle]** oder eine **Auswahl** aus dem Dropdown-Menü. Alle Mitarbeiter werden optimiert, aber die Ergebnisse werden nur für die Mitarbeiter in der Auswahl gespeichert.
5. Klicke *Ok*{:.doc-button}, um den Prozess zu starten.
