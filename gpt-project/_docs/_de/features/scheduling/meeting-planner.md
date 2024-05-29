---
title: Meetingplaner
description: Plane Meetings mit dem Meetingplaner (SchedulePro).
product_label:
  - classic
  - on-premise
---

Der Meetingplaner ist der Programmteil zur Planung und Zuordnung von Meetings.

> In diesem Artikel geht es um _WFM > Scheduling > SchedulePro > Meetingplaner_{:.breadcrumbs}.
>
> Wenn du injixo Advanced WFM oder Enterprise WFM verwendest, nutze stattdessen das {% link_new Meetings | features/scheduling/meetings/meetings-overview.md %}-Feature unter _Plan > Meetings_{:.breadcrumbs}.

Anhand der festgelegten Parameter bekommst Du Terminvorschläge für Meetings, die bestimmte Aktivitäten beinhalten. Du hast dann die Möglichkeit, einen oder mehrere Vorschläge auszuwählen und die Daten des Meetings in die Ebene _Plan_ des Schicht Centers einzufügen.

Es werden nur Mitarbeiter in die Suche einbezogen, für die in dieser Zeit schon eine Planung besteht.

## Parameter

Die Parameterauswahl gliedert sich in zwei Teile: Parameter für das Meeting und für die Mitarbeiter.

{{ 1 | image: "Meetingplaner Eingabe-Dialog" }}

### Parameter für das Meeting

Setze die Parameter wie folgt:

1. Wähle die zu planende `Aktivität` für das Meeting aus.

2. Gib die `Dauer` des zu planenden Meetings in Stunden und Minuten an.

3. Wähle ein `Startdatum` und ein `Enddatum` für den Meetingzeitraum aus. Der Suchzeitraum kann maximal ein Jahr lang sein.

4. Aktiviere das Kontrollkästchen `Tägliche Suche`, wenn die eingegebenen Start- und Endzeiten für jeden Tag gelten sollen.

   Beachte, dass mit diesem Kontrollkästchen nur das Verhalten für Zeiträume von mehr als einem Tag geändert wird.

   Bei Aktivierung dieser Option, wird pro Tag geprüft, ob ein Meeting zwischen der Start- und der Endzeit geplant werden kann, z.B. täglich zwischen 09:00 Uhr und 17:00 Uhr. Ansonsten wird geprüft, ob ein Meeting jederzeit zwischen Montag 8:00 Uhr und Freitag 17:00 Uhr stattfinden kann, auch außerhalb des definierten Zeitfensters.

5. Gib den `Wunschuhrzeit Beginn` und das `Wunschuhrzeit Ende` für den Zeitraum ein.
   Wenn die Checkbox **Tägliche Suche** aktiviert ist, kannst du eine Alternativuhrzeit eingeben.

6. Wähle das `Suchzeitintervall` für die Suche nach verfügbaren Mitarbeitern.
   Du kannst zwischen 5, 10, 15, 30 und 60 Minuten wählen. Ein Suchzeitintervall von 10 Minuten bewirkt zum Beispiel, dass bei der Suche innerhalb des angegebenen Zeitraums alle 10 Minuten geprüft wird, ob ein Mitarbeiter an einem Meeting teilnehmen könnte.

7. Aktiviere das Kontrollkästchen `Pausen ignorieren`, um bei der Suche nach einem Termin die Pausen der Mitarbeiter zu ignorieren, andernfalls können die Mitarbeiter innerhalb der Pausenzeit nicht an einem Meeting teilnehmen.

8. Gib jeweils einen Wert für `Mitarbeiteranzahl Minimum` und `Mitarbeiteranzahl Maximum` ein.
   Kein Eintrag bedeutet, dass beliebig viele Mitarbeiter teilnehmen können.

9. Gib einen Wert für `Gleichzeitige Meetings Maximum` ein, wenn du nicht möchtest, dass es beliebig viele Meetings sein können.

10. (Optional) Du kannst einen Kommentar für Mitarbeiter mit einer maximalen Länge von 30 Zeichen eingeben, der dann zusätzlich zum Meeting in injixo Me und im _Schicht Center_{:.menu-item} erscheint.

### Parameter für Mitarbeiter

1. Wähle hier mindestens eine bestimmte Planungseinheit, Auswahlgruppe oder einen Mitarbeiter aus. Die gleichzeitige Auswahl `[Alle]` für alle drei Felder ist nicht gestattet, es erscheint dann eine Fehlermeldung. Drücke zusätzlich die STRG-Taste, um mehrere Items auszuwählen.

2. Aktiviere die Checkbox **Bei der Suche Mitarbeiter ignorieren, denen folgende Aktivitäten im Schichtplan zugeordnet sind**, wenn bei der Suche nach einem Termin für das zu planende Meeting Mitarbeiter ignoriert werden sollen, denen bestimmte Aktivitäten im Schichtplan zugeordnet sind.

3. Aktiviere die Checkbox **Bei der Suche Mitarbeiter ignorieren, denen im nachfolgend angegebenen Zeitraum ein Meeting mit der gleichen Aktivität zugeordnet ist**, wenn bei der Suche nach einem Termin für das zu planende Meeting Mitarbeiter ignoriert werden sollen, denen im angegebenen Zeitraum bereits ein Meeting mit der gleichen Aktivität im Schichtplan zugeordnet ist.

4. Wähle ein `Startdatum` und ein `Enddatum` für den Zeitraum aus, auf ein bereits geplantes Meeting mit der gleichen Aktivität geprüft werden soll.

5. Starte die Suche nach möglichen Terminen für das Meeting. Klicke _Abbrechen_{:.doc-button}, um alle Parameter zurückzusetzen.

## Ergebnisübersicht und Meetingplanung

Die Ergebnisübersicht ist auf maximal 50 Terminvorschläge begrenzt.

Neben dem `Datum` und der `Startuhrzeit` werden zwei weitere Informationen angezeigt:

- In der Spalte _Beeinträchtigte Aktivitäten_ werden alle Aktivitäten angezeigt, deren Deckung durch dieses Meeting beeinträchtigt werden.
- Die Spalte _Deckung_ gibt an, um wie viele Personen geringer die Deckung für die beeinträchtigte Aktivität ist, wenn du diesen Terminvorschlag auswählst.

Die Spalte _Planungsauswahl_ enthält für jeden Terminvorschlag die Schaltfläche _Planen_{:.doc-button}. Klicke _OK_{:.doc-button}, um Meetings in die Ebene _Plan_ zu übertragen. Terminvorschläge, die z.&nbsp;B. gegen bestehende Planungsregeln verstoßen und nicht geplant werden können, verfügen nicht über die Schaltfläche _Planen_. Ist die Planung beendet, siehst Du eine Meldung über die erfolgreiche Planung des Meetings. Klicke _OK_{:.doc-button}, um zum Meeting Planer zurückzukehren.

Das Ergebnis dieser Meetingplanung kannst du Dir im _Schicht Center_{:.menu-item} in der Ebene _Plan_ ansehen. Auf dem Arbeitsblatt Kommentar des Eingabedialoges im _Schicht Center_{:.menu-item} wird Dir der eingegebene Kommentar mit Informationen zu dem Meeting angezeigt.
