---
title: Joboptimierung ausführen
description: Lerne, was die Joboptimierung ist, wann Du sie nutzen solltest und wie Du eine Optimierung ausführst.
product_label:
  - essential
  - advanced
  - enterprise
---

In diesem Artikel lernst Du

- Was die Joboptimierung ist und wann Du sie nutzen solltest.
- Wie Du injixo konfigurierst, um die besten Optimierungsergebnisse zu erzielen.
- Wie Du eine Joboptimierung ausführst.

## Was ist die Joboptimierung?

Die Funktion _Joboptimierung_ tauscht Aktivitäten in den Schichtplänen Deiner Mitarbeiter aus, ohne die Anfangs- und Endzeiten der Schichten zu ändern. Ziel ist es, die bestmögliche Deckung für alle Aktivitäten zu erreichen, basierend auf den Mitarbeiterbedarfen der Aktivitäten. Auch die Pausen werden optimiert.

Verwende die Joboptimierung:

- Wenn sich die Mitarbeiterbedarfe für eine oder mehrere Aktivitäten geändert haben und Du die Deckung der Aktivitäten entsprechend optimieren möchtest.
- Wenn Du Deinen Mitarbeitern im Schichtwunsch-Verfahren mit den Funktionen _Verlosen_ oder _Zuteilen_ Schichten zugewiesen hast. In diesem Fall enthalten die Schichten typischerweise nur die Aktivität _Anwesend_. Diese muss dann durch die tatsächlichen Aktivitäten ersetzt werden, jeweils basierend auf dem Mitarbeiterbedarf.
- Wenn Du Schichtfolgen für Deine Mitarbeiter eingefügt hast, die Schichten mit der Aktivität _Anwesend_ oder andere als _Ersetzbar_ konfigurierte Aktivitäten verwenden und Du diese Aktivitäten nun basierend auf dem Mitarbeiterbedarf austauschen möchtest.

Die Joboptimierung wandelt Tagesmodelle in einzelne Aktivitäten um, Pausenkorridore bleiben hingegen erhalten.

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

## Joboptimierung ausführen

So startest Du eine Joboptimierung in _Plan > Schedules_{:.breadcrumbs}:

1. Klicke auf _Planungsaktionen_{:.doc-button}.
2. Klicke auf **Joboptimierung**.
3. Wähle einen **Zeitraum** für die Optimierung. Der Zeitraum ist mit dem aktuell ausgewählten Zeitbereich in _Schedules_ vorausgefüllt.
4. Wähle eine **Planungseinheit**.
5. Wähle eine **Auswahl** (optional), wenn Du die Optimierung auf eine bestimmte Auswahl an Mitarbeitern beschränken willst.
6. Klicke auf _Joboptimierung starten_{:.doc-button}. Der Hintergrundprozess startet. Du siehst eine grüne Benachrichtigung, wenn die Optimierung erfolgreich gestartet wurde. Eine rote Meldung erscheint, wenn die Optimierung nicht gestartet werden konnte.

{{ 1 | image: 'Dialog für die Joboptimierung', '70%' }}

Die Optimierung kann je nach Datenmenge und gewähltem Zeitraum einige Zeit dauern. Währenddessen kannst Du im zu optimierenden Zeitraum keine Änderungen am Schichtplan vornehmen. Wenn die Optimierung beendet ist, speichert injixo das Ergebnis automatisch.

Gehe zu _WFM > Administration > System > JobProcessor_{:.breadcrumbs}, um den Fortschritt einer laufenden Optimierung zu sehen. Dort findest Du auch einen Link zum {% link_new Planungsreport | best-practices/resolve-optimization-issues.md %}, sobald der Prozess beendet ist. Dieser liefert einige grundlegende Informationen zum Optimierungsprozess.
