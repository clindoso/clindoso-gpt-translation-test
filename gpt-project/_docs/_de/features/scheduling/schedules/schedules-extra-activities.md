---
title: Extra-Aktivitäten planen
product_label:
  - advanced
  - enterprise
permalink: /de/schedules-extra-activities/
permalink_reason: /schedules-extra-activities/ used in email and in Intercom message
description: Plane eine definierte Anzahl an Personenstunden für lagerfähige Aktivitäten wie E-Mail und Backoffice (Schedules-Modul).
---

In diesem Artikel lernst Du:

- was die Funktion _Extra-Aktivitäten planen_ ist.
- wie Du Extra-Aktivitäten planst.
- wie Du Planungsvorschläge für Extra-Aktivitäten generierst, überprüfst und dem Schichtplan hinzufügst.
- wie Du die Planungshistorie bereinigst.

## Was ist die Funktion **Extra-Aktivitäten planen**?

Mit der Funktion _Extra-Aktivitäten planen_ kannst Du eine definierte Anzahl von Personenstunden für eine lagerfähige Aktivität (z. B. Backoffice oder E-Mail) planen. Lagerfähig bedeutet, dass die Tätigkeit zurückgestellt werden kann. Sie wird bearbeitet, wann immer die Zeit dafür vorhanden ist.

Mit der Funktion _Extra-Aktivitäten planen_ wird die lagerfähige Aktivität geplant, indem andere bereits existierende Aktivitäten ersetzt werden. Basierend auf Deinen Eingaben generiert ein Optimierungsprozess Vorschläge für geeignete Zeitfenster, die Du annehmen oder ablehnen kannst. Die Optimierung stellt sicher, dass die Auswirkungen auf die Deckung Deiner anderen Aktivitäten so gering wie möglich sind.

Du kannst die Funktion _Extra-Aktivitäten planen_ auch nutzen, um Aktivitäten zu planen, die nicht lagerfähig sind.

## Voraussetzungen

- Der zu planende Zeitraum muss einen Schichtplan in der Ebene _Schedule_ enthalten.
- Du kannst Extra-Aktivitäten nur in Zeiträumen platzieren, die Aktivitäten vom Typ _Anwesenheit_ enthalten (konfiguriert als _Bezahlt_ und _Ersetzbar_).

## Planungsvorschläge generieren

1. Gehe zu _Plan > Schedules_{:.breadcrumbs}.
2. Klicke auf _Planungsaktionen_{:.doc-button} und wähle **Extra-Aktivitäten planen** aus.
3. Klicke unten auf _Neue Extra-Aktivität einrichten_{:.doc-button}.
   {{ 1 | image: 'Übersichtsseite'}}
4. Wähle im Bereich _Eckdaten_ die **Planungseinheit**, in der Du die Extra-Aktivität planen möchtest. Du kannst auch tippen, um die Liste zu filtern.
   Hast Du einen Eintrag ausgewählt, siehst Du in einem Hinweisfeld, wie viele Aktivitäten vom Typ _Anwesenheit_ in der Planungseinheit aktuell nicht als _Ersetzbar_ konfiguriert sind.
5. Wähle eine **Zu planende Extra-Aktivität**. Die Liste enthält nur _Bezahlte_ Aktivitäten vom Typ _Anwesenheit_.
6. Wähle einen **Zeitraum**, in dem die Extra-Aktivität geplant werden soll. Standardmäßig ist dieser auf die nächste Arbeitswoche von Montag bis Sonntag nach dem aktuellen Datum eingestellt.
7. Wähle die **Mindestdauer der Slots**. Die Dauer kann zwischen 15 und 120 Minuten liegen (der Standardwert ist 30 Minuten). Die genauen Werte hängen von dem definierten Intervall der ausgewählten Planungseinheit ab.
8. Gib bei **Gesamte zu planende Personenstunden** die Anzahl der Personenstunden ein, die für die Extra-Aktivität geplant werden sollen.
9. Um zu erzwingen, dass die Personenstunden möglichst gleichmäßig verteilt werden, aktiviere die Checkbox **Personenstunden gleichmäßig auf Mitarbeiter verteilen**. Dies kann zu einer schlechteren Deckung anderer Aktivitäten führen. Wie gleichmäßig injixo die Stunden verteilen kann, hängt auch von anderen Einschränkungen ab, wie z. B., dass Agenten nicht für eine ersetzbare Aktivität eingeplant sind.

   {{ 2 | image: 'Einstellungen/Eckdaten', '60%' }}

10. Hake unter _Mitarbeiter_ die **Mitarbeiter** an, die mit der Extra-Aktivität geplant werden sollen. Ändere alle auf einmal, indem Du die Checkbox in der Spaltenüberschrift verwendest. Du kannst nur Mitarbeiter der ausgewählten Planungseinheit auswählen, die die erforderliche(n) Qualifikation(en) für die Extra-Aktivität besitzen. Du kannst auch eine Auswahl oder einen Mitarbeiterfilter aus dem Dropdown-Menü oberhalb wählen.
11. Klicke auf _Vorschläge generieren_{:.doc-button} unten auf der Seite.

Du gelangst zurück auf die Übersichtsseite. Die _Planungshistorie_ zeigt einen Eintrag für Deine neue Planungsanfrage. Die Spalte _Status_ zeigt an, dass die Planung läuft.

Das Erzeugen von Planungsvorschlägen kann einige Zeit dauern, abhängig von der Anzahl der Mitarbeiter und dem gewählten Datumsbereich. Warte, bis der Prozess abgeschlossen ist und sich der _Status_ ändert. Lerne unterhalb mehr über die verschiedenen Status.

## Den Status prüfen

Jeder Planungsvorgang erzeugt eine Zeile im Abschnitt _Planungshistorie_ mit folgenden Informationen:

- dem Datum und der Uhrzeit, wann der Prozess gestartet wurde
- dem Benutzer, der den Prozess gestartet hat
- der gewählten Planungseinheit
- der Extra-Aktivität
- dem gewählten Zeitraum

Wenn der Prozess beendet ist, zeigt die Spalte _Status_ einen der folgenden Werte:

- _Vorschläge verfügbar_: Der Prozess war erfolgreich und es wurden Planungsvorschläge für die gewählte Extra-Aktivität erzeugt. Erfahre, wie Du die [Vorschläge prüfst](#planungsvorschläge-prüfen-und-übernehmen).
- _Nicht möglich_: Der Vorgang ist fehlgeschlagen, es wurden keine Vorschläge erzeugt. Gründe dafür können sein, dass die ausgewählten Mitarbeiter nicht genügend _Ersetzbare_ Aktivitäten vom Typ _Anwesenheit_ im Schichtplan haben oder dass der angegebene Wert für _Mindestdauer der Slots_ zu lang ist. In der Statusspalte erscheint außerdem der Text _Konflikt anzeigen_. Klicke darauf, um die Meldung mit dem Grund für den Konflikt anzuzeigen.<sup>1</sup>
- _Die Optimierung ist fehlgeschlagen. Bitte versuche es erneut_: Der Prozess konnte nicht gestartet werden. Versuche, den Prozess erneut zu starten. Wenn das Problem weiterhin besteht, {% link_new erstelle ein Ticket | support/create-ticket.md %}, um Unterstützung zu erhalten.

<sup>1</sup> Beispiel-Meldung: _"Es war nicht möglich, Slots für die ausgewählten Mitarbeiter zu finden. Diese Mitarbeiter haben nicht genügend ersetzbare Aktivitäten vom Typ Anwesenheit in ihrem Plan oder die vorgesehene Mindestdauer der Slots ist zu lang."_ Diese Meldung erscheint, wenn kein Schichtplan oder keine _Ersetzbaren_ Aktivitäten im Schichtplan vorhanden sind; oder aber, wenn gar keine Aktivität als _Ersetzbar_ konfiguriert wurde.

## Planungsvorschläge prüfen und übernehmen

Nachdem die Vorschläge erfolgreich generiert wurden, zeigt die Spalte _Status_ den Text _Vorschläge verfügbar_ und einen Link _Vorschläge anschauen_ an:

1. Um Details zu den erzeugten Vorschlägen zu sehen, klicke auf **Vorschläge anschauen**.
   Eine Tabelle zeigt die folgenden Spalten:
   - _Vorgeschlagener Termin_: der Zeitbereich, in dem die Extra-Aktivität geplant werden könnte
   - _Zu planende Extra-Aktivität_: die Extra-Aktivität, die geplant wird
   - _Mitarbeiter_: der Mitarbeiter, der die Extra-Aktivität in dem vorgeschlagenen Zeitbereich erhalten soll
   - _Ersetzte Aktivität_: die Aktivität, die durch die Extra-Aktivität ersetzt werden soll
   - _Geänderte Deckung_: Informationen darüber, wie sich die Deckung für alle betroffenen Aktivitäten ändern würde, wenn der Planungsvorschlag für die Extra-Aktivität übernommen wird
2. (Optional) Um Vorschläge von der Planung auszuschließen, deaktiviere eine oder mehrere **Checkboxen** auf der linken Seite. Oben siehst Du die Gesamtzahl der Personenstunden, die vorgeschlagen wurden, und die Gesamtzahl der Personenstunden, die basierend auf Deiner Auswahl geplant werden.
3. Um die Vorschläge in den Schichtplan zu schreiben, klicke auf _Extra-Aktivität planen_{:.doc-button} unten auf der Seite. Dies kann einen Moment dauern.

   {{ 3 | image: 'Seite - Vorschläge anschauen'}}

## Ergebnisse ansehen

Nachdem die Vorschläge in den Schichtplan geschrieben wurden, kannst Du auf den Link **Ergebnis anschauen** im Abschnitt _Planungshistorie_ klicken. Mit den Tabs _Geplant_, _Fehlgeschlagen_ und _Ausgeschlossen_ prüfst Du die Planungsergebnisse:

- Der Tab _Geplant_ enthält alle Planungsvorschläge, die Du in den Schichtplan übernommen hast.
- Der Tab _Fehlgeschlagen_ enthält alle Planungsvorschläge, die aufgrund von Fehlern nicht geplant werden konnten.
- Der Tab _Ausgeschlossen_ enthält alle Planungsvorschläge, die Du im vorherigen Schritt nicht ausgewählt hast, und die daher auch nicht in den Schichtplan übertragen werden.

Wenn einer der Tabs deaktiviert ist, gibt es keine Vorschläge in dieser Kategorie.

Mit einem Klick auf den Link **Plan anschauen** auf der linken Seite gelangst Du direkt zum aktuellen Schichtplan.

{{ 4 | image: 'Ergebnisseite'}}

## Alte Einträge entfernen

Du kannst nicht mehr benötigte Einträge aus der _Planungshistorie_ entfernen:

1. Aktiviere die **Checkbox** vor einem Eintrag. Oder aktiviere die oberste Checkbox, um alle Einträge auszuwählen.
2. Klicke auf _Einträge löschen_{:.doc-button}, um die ausgewählten Zeilen zu entfernen. Die Extra-Aktivitäten, die Du bereits in den Schichtplan übertragen hast, werden dabei _nicht_ gelöscht.
