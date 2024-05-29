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

> In diesem Artikel geht es um _WFM > Scheduling > SchedulePro_{:.breadcrumbs}.
>
> Wenn Du injixo Advanced WFM oder Enterprise WFM verwendest, nutze stattdessen die Funktionen {% link_new Pausenoptimierung | features/scheduling/schedules/break-optimization.md %}, {% link_new Joboptimierung | features/scheduling/schedules/schedules-job-optimization.md %} und {% link_new Volloptimierung | features/scheduling/schedules/schedules-optimized-schedules.md %} unter _Plan > Schedules_{:.breadcrumbs}.

injixo unterscheidet drei Optimierungsprozesse:

- **Volloptimierte Planung:** Erstelle automatisiert einen bedarfsorientierten Dienstplan auf Basis von Stammdaten und Mitarbeiterbedarfen.
- **Joboptimierung:** Optimiere einen bereits bestehenden Dienstplan, um ersetzbare Aktivitäten mit planbaren Aktivitäten auszutauschen, um den jeweiligen Bedarf bestmöglich zu decken. Zusätzlich wird eine Pausenoptimierung durchgeführt.
- **Pausenoptimierung:** Optimiere die Pausenpositionen bestmöglich im Hinblick auf die Deckung der übrigen Aktivitäten nach Änderungen an der aktuellen Planung. Pausen können nur innerhalb von {% link_new Korridoren in Tagesmodellen | features/administration/daymodels/daymodel-basics.md | #feste-elemente-vs-korridore %} verschoben werden.

Optimierungen können einige Zeit dauern, abhängig von der Datenmenge und gewähltem Zeitraum. Währenddessen kannst Du in diesem Zeitraum keine Änderungen am Schichtplan vornehmen. injixo speichert das Ergebnis automatisch.

> injixo Enterprise on-premise
>
> Der Menüpunkt _WFM > Scheduling > SchedulePro > Optimierung_{:.breadcrumbs} steht _nicht_ zur Verfügung. Die volloptimierte Planung heißt hier _AutoScheduler_{:.menu-item}. Starte Optimierungen direkt aus dem _Schicht Center_{:.menu-item} oder die Joboptimierung über _Planperioden_{:.menu-item}. Sie werden standardmäßig manuell auf Knopfdruck gespeichert und laufen nicht über den JobProcessor. Die AutoScheduler-Benutzeroberfläche zeigt ihren Fortschritt an.

Die Übersichtsseite in _WFM > Scheduling > SchedulePro > Optimierung_{:.breadcrumbs} zeigt alle Optimierungen. Der angezeigte Verarbeitungsstatus bei laufenden Optimierungen aktualisiert sich automatisch. Abgeschlossene Optimierungen haben den Status _Fertig_.

Betrachte den Fortschritt einer laufenden Optimierung in _Administration > System > JobProcessor_{:.breadcrumbs}. Dort findest Du auch einen Link zum PDF-Report. Erfahre mehr über den {% link_new Planungsreport | best-practices/resolve-optimization-issues.md %}, der Planungsfehler auflistet.

## Was ist die Volloptimierung?

Das Feature _Volloptimierter Plan_ (auch AutoScheduler genannt) erstellt automatisch einen kompletten Schichtplan mit der bestmöglichen Deckung für alle Aktivitäten mit der geringstmöglichen Anzahl an Mitarbeitern. Der Schichtplan wird auf der Grundlage des Mitarbeiterbedarfs für die verschiedenen Aktivitäten erstellt.

Um mit dem Feature _Volloptimierter Plan_ die besten Ergebnisse zu erzielen, musst Du injixo zuvor korrekt konfigurieren:

- Konfiguriere Deine {% link_new Mitarbeiter | features/administration/employee-overview.md %}.
- Überprüfe die Planungsparameter und AutoScheduler-Parameter Deiner Verträge unter _WFM > Administration > Scheduling > Verträge_{:.breadcrumbs}. Die Optimierung muss sich an diese Einstellungen halten.
- Füge der Planungseinheit alle Tagesmodelle hinzu, die die Optimierung verwenden soll. Die Optimierung berücksichtigt alle Tagesmodelle der Planungseinheit.
- Stelle sicher, dass die Planungseinheit Öffnungszeiten hat und dass die Schichten zu den Öffnungszeiten passen.
- Die Länge der verfügbaren {% link_new Tagesmodelle | features/administration/daymodels/daymodel-creation.md %} muss mit den vertraglichen Arbeitszeiten der Mitarbeiter übereinstimmen.
- Die Aktivitäten, die durch die Optimierung geplant werden, müssen als _Planbar_ konfiguriert sein. Diese Aktivitäten ersetzen dann falls nötig als _Ersetzbar_ konfigurierte Aktivitäten.
- Verwende {% link_new Planungsmodelle | features/administration/work-time-pattern-models.md %} für Mitarbeiter, wenn Du die möglichen Arbeitszeitkombinationen für die Optimierung einschränken willst.
- Überprüfe die Einstellungen für den {% link_new Stellenwert | best-practices/importance-for-activities.md %} und die {% link_new Priorität | best-practices/priority-for-activities.md %} der Aktivitäten. Sie legen fest, welche Aktivitäten andere Aktivitäten überschreiben können und welche Aktivitäten bei der Optimierung vorrangig behandelt werden.

### Volloptimierung starten

Gehe in _WFM > Scheduling > SchedulePro > Optimierung_{:.breadcrumbs} wie folgt vor, um eine volloptimierte Planung zu starten:

1. Wähle in der Aktionsleiste die Option _Volloptimierter Plan_{:.doc-button}.
2. Lege unter _Zeitraum_ das **Startdatum und Enddatum** fest. Maximaler Zeitraum: 10 Wochen.
3. Wähle die **Planungseinheit**.
4. (Optional) Wähle unter _Auswahl_ entweder **[Alle]** oder eine **Auswahl** aus dem Dropdown-Menü. Alle Mitarbeiter werden optimiert, aber die Ergebnisse werden nur für die Mitarbeiter in der Auswahl gespeichert.
5. (Optional) Verwende die Option **Erneute Optimierung**, wenn Du für beliebige Mitarbeiter einen Schichtplan neu erstellen möchtest, der Schichten aus Planungsmodellen vom Typ C enthält. In diesem Fall weiß injixo, an welchen Wochentagen die Mitarbeiter mit diesen Planungsmodellen geplant wurden. Wenn Du die Checkbox nicht setzt, werden die gleichen Wochentage wie zuvor verwendet. Du musst zuerst den ursprünglichen Schichtplan löschen.
6. Klicke _Ok_{:.doc-button}, um den Prozess zu starten.

## Was ist die Joboptimierung?

Die Funktion _Joboptimierung_ tauscht Aktivitäten in den Schichtplänen Deiner Mitarbeiter aus, ohne die Anfangs- und Endzeiten der Schichten zu ändern. Ziel ist es, die bestmögliche Deckung für alle Aktivitäten zu erreichen, basierend auf den Mitarbeiterbedarfen der Aktivitäten. Auch die Pausen werden optimiert.

Verwende die Joboptimierung:

- Wenn sich die Mitarbeiterbedarfe für eine oder mehrere Aktivitäten geändert haben und Du die Deckung der Aktivitäten entsprechend optimieren möchtest.
- Wenn Du Deinen Mitarbeitern im Schichtwunsch-Verfahren mit den Funktionen _Verlosen_ oder _Zuteilen_ Schichten zugewiesen hast. In diesem Fall enthalten die Schichten typischerweise nur die Aktivität _Anwesend_. Diese muss dann durch die tatsächlichen Aktivitäten ersetzt werden, jeweils basierend auf dem Mitarbeiterbedarf.
- Wenn Du Schichtfolgen für Deine Mitarbeiter eingefügt hast, die Schichten mit der Aktivität _Anwesend_ oder andere als _Ersetzbar_ konfigurierte Aktivitäten verwenden und Du diese Aktivitäten nun basierend auf dem Mitarbeiterbedarf austauschen möchtest.

> Verwende die Aktivität _Anwesend_ in Tagesmodellen für Schichtwünsche
>
> Wenn Du Deinen Mitarbeitern über injixo Me Schichten anbietest, ist es sinnvoll, nur die Standard-Systemaktivität namens _Anwesend_ mit der ID 1 als Aktivität in den Tagesmodellen zu verwenden. Auf diese Weise verhinderst Du, dass Mitarbeiter sich zunächst Schichten mit speziellen Aktivitäten wünschen, dann aber durch die Joboptimierung ganz andere Aktivitäten zugewiesen bekommen.

### Beispiel

Einige Mitarbeiter sind für eine Aktivität namens _Reiseverkauf_ qualifiziert. Über das Schichtwunsch-Verfahren haben sie Schichten mit der Basisaktivität _Anwesend_ und einer Mittagspause erhalten. Die Aktivität _Anwesend_ wurde als ersetzbar definiert. Die Optimierung prüft nun, zu welchen Zeiten ein Mitarbeiterbedarf für die Aktivität _Reiseverkauf_ besteht. Für diese Zeiten wird die Aktivität _Anwesend_ in den Schichtplänen der Mitarbeiter durch die Aktivität _Reiseverkauf_ ersetzt.

## injixo konfigurieren, um optimale Ergebnisse zu erzielen

- Konfiguriere Deine {% link_new Mitarbeiter | features/administration/employee-overview.md %}. Mitarbeiter können nur Aktivitäten erhalten, für die sie qualifiziert sind.
- Die _Job-Optimierung_ funktioniert nur mit Aktivitäten, die als _Planbar_ konfiguriert wurden. Diese Aktivitäten ersetzen andere Aktivitäten, die als _Ersetzbar_ konfiguriert wurden.
- Stelle sicher, dass für alle Aktivitäten, die andere Aktivitäten ersetzen sollen, ein Mitarbeiterbedarf existiert. Aktivitäten ohne Mitarbeiterbedarf werden von der Optimierung nicht berücksichtigt.
- Überprüfe die Einstellungen für den {% link_new Stellenwert | best-practices/importance-for-activities.md %} und die {% link_new Priorität | best-practices/priority-for-activities.md %} der Aktivitäten. Diese legen fest, welche Aktivitäten andere Aktivitäten überschreiben können und welche Aktivitäten bei der Optimierung priorisiert werden.

### Joboptimierung ausführen

Gehe wie folgt vor, um eine Joboptimierung in _WFM > Scheduling > SchedulePro > Optimierung_{:.breadcrumbs} zu starten:

1. Wähle in der Aktionsleiste die Option _Joboptimierung_{:.doc-button}.
2. Lege unter _Zeitraum_ das **Startdatum und Enddatum** fest. Maximaler Zeitraum: 10 Wochen.
3. Wähle die **Planungseinheit**.
4. (Optional) Wähle unter _Auswahl_ entweder **[Alle]** oder eine **Auswahl** aus dem Dropdown-Menü. Alle Mitarbeiter werden optimiert, aber die Ergebnisse werden nur für die Mitarbeiter in der Auswahl gespeichert.
5. Klicke _Ok_{:.doc-button}, um den Prozess zu starten.

## Was ist die Pausenoptimierung?

Ziel des Features _Pausenoptimierung_ ist es, die Pausen innerhalb Deines Schichtplans neu zu verteilen, um die Deckung von Aktivitäten, für die Mitarbeiterbedarf besteht, zu optimieren. Die Zeiten für Schichtbeginn und -ende bleiben dabei unverändert. Das Feature _Pausen optimieren_ wandelt bestehende Tagesmodelle im Optimierungszeitraum in Aktivitäten um. Die Pausenkorridore in Tagesmodellen bleiben aber bestehen, so dass Du falls nötig weitere Pausenoptimierungen durchführen kannst.

Beispiel: Zwei Mitarbeiter haben eine Schicht mit einer Pause von 12:00 bis 13:00 Uhr. Die Pause kann alle 30 Minuten zwischen 12:00 und 15:00 Uhr beginnen. Um die niedrige Deckung für die Basisaktivität der Schicht zwischen 12:00 und 13:00 zu verbessern, wird injixo mindestens eine der Pausen auf eine spätere Zeit verschieben.

### Pausenoptimierung ausführen

Gehe wie folgt vor, um eine Pausenoptimierung in _WFM > Scheduling > SchedulePro > Optimierung_{:.breadcrumbs} zu starten:

1. Wähle in der Aktionsleiste die Option _Pausenoptimierung_{:.doc-button}.
2. Lege unter _Zeitraum_ das **Startdatum und Enddatum** fest. Maximaler Zeitraum: 10 Wochen.
3. Wähle die **Planungseinheit**.
4. (Optional) Wähle unter _Auswahl_ entweder **[Alle]** oder eine **Auswahl** aus dem Dropdown-Menü. Alle Mitarbeiter werden optimiert, aber die Ergebnisse werden nur für die Mitarbeiter in der Auswahl gespeichert.
5. Klicke _Ok_{:.doc-button}, um den Prozess zu starten.
