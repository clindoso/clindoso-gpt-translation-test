---
title: 1:1-Meetings planen
product_label:
  - advanced
  - enterprise
toc: false
description: Erzeuge Terminvorschläge für 1:1-Meetings, die die Deckung Deiner anderen Aktivitäten möglichst wenig beeinträchtigen (Meetings-Modul).
---

In diesem Artikel lernst Du, wie Du Terminvorschläge für 1:1-Meetings erzeugst, die die Deckung Deiner anderen Aktivitäten möglichst wenig beeinträchtigen.

Neu im Meetings-Modul? Lerne zuerst {% link_new die Grundlagen | features/scheduling/meetings/meetings-overview.md %}.

## Terminvorschläge für 1:1-Meetings generieren

1:1-Meetings sind Besprechungen zwischen einem Mitarbeiter und einem Gastgeber, der typischerweise ein Teamleiter ist.

1. Gehe zu _Plan > Meetings_{:.breadcrumbs}.
2. Klicke auf _Erstellen_{:.doc-button} in der _1:1-Meetings_-Karte oben auf der Seite.
3. Wähle im Abschnitt _Eckdaten_ die **Planungseinheit** aus, für die Du 1:1-Meetings planen möchtest. Wähle einen Eintrag aus der Liste oder beginne mit der Eingabe des Namens der Planungseinheit, um die Liste zu filtern. Nach der Auswahl einer Planungseinheit erscheint eine Hinweisbox, die Dich darüber informiert, wie viele Aktivitäten vom Typ _Anwesenheit_ in der Planungseinheit nicht als _Ersetzbar_ konfiguriert sind.
4. Wähle bei **Zu planende Aktivität** die 1:1-Meeting-Aktivität aus, die Du planen möchtest. Die Liste enthält alle Aktivitäten vom Typ _Meeting_, die der Planungseinheit zugewiesen sind. Wähle einen Eintrag aus der Liste oder beginne mit der Eingabe des Namens der Aktivität, um die Liste zu filtern. Wenn Du noch keine {% link_new Meeting-Aktivität | features/administration/activities.md %} erstellt hast, tue es jetzt.
5. Wähle den **Zeitraum** aus, in dem Du Meetings planen möchtest. Standardmäßig ist der Datumsbereich auf die nächste Arbeitswoche (Montag - Sonntag) nach dem aktuellen Datum voreingestellt.
6. Lege eine **Meetinglänge** in Minuten fest. Der Standardwert ist 60 Minuten.
   {{ 1 | image: 'Abschnitt Eckdaten', '60%' }}

7. Aktiviere im Abschnitt _Optionale Eckdaten_ die Checkbox **Plane eine Pause zwischen einzelnen Meetings**, wenn Du sicherstellen möchtest, dass für jeden Teilnehmer ein bestimmter Zeitpuffer zwischen zwei Meetings eingehalten wird. Wähle darunter einen passenden **Wert** aus dem Dropdown.
8. Aktiviere die Checkbox **Beschränke die Anzahl der Meetings pro Tag auf maximal**, wenn Du die Anzahl der Meetings pro Tag für jeden Teilnehmer begrenzen möchtest. Gib darunter die maximale **Anzahl** der Meetings pro Tag ein.
9. Aktiviere die Checkbox **Erlaube Termine nur in Zeiträumen mit einer Deckung von mindestens**, wenn Du sicherstellen möchtest, dass die resultierende Deckung nach dem Planen der Meetings nicht unter einen definierten Schwellenwert fällt. Gib einen **Wert für die Deckung** ein. Null und negative Werte sind ebenfalls erlaubt, da die Deckung auch negativ sein kann.

   {{ 5 | image: 'Abschnitt Eckdaten', '60%' }}

10. Im Abschnitt _Gastgeber_ hast Du zwei Optionen, um festzulegen, wann der Gastgeber des Meetings für Termine verfügbar ist:

    - Wenn der Gastgeber nicht in injixo geplant wird, markiere die Option **Manuell eingeben**. Definiere dann Zeitbereiche für einen oder mehrere Tage:

      1. Gib Werte in die Felder **Tag**, **Von** und **Bis** ein.
      2. Klicke auf _+ Zeitspanne_{:.doc-button}, um eine weitere Zeitspanne für den gewählten Tag hinzuzufügen (optional). Wenn sich Zeitspannen überschneiden, verwendet injixo die größtmögliche Zeitspanne aus der Kombination mehrerer Zeitspannen. Um eine Zeitspanne zu entfernen, klicke auf das **X** neben der Zeitspanne.
      3. Wenn Du Zeitspannen für einen weiteren Tag hinzufügen möchtest, klicke auf _Tag und Zeitspanne hinzufügen_{:.doc-button}. Um einzelne Tage zu entfernen, klicke auf _Tag entfernen_{:.doc-button}. Mindestens ein Tag mit einer Zeitspanne ist erforderlich.

      {{ 2 | image: 'Gastgeber - Manuell eingeben', '60%' }}

    - Wenn der Meeting-Gastgeber in injixo geplant wird, markiere die Option **Mitarbeiter auswählen**. injixo entnimmt die Verfügbarkeit des Gastgebers aus dessen Schichtplan. Ist diese Option ausgewählt, werden die geplanten Meetings auch in den Schichtplan des Gastgebers geschrieben.

      1. Wähle eine andere **Planungseinheit** aus, wenn der Gastgeber Teil einer anderen Planungseinheit ist. Hinweis: Die Planungseinheiten des Gastgebers und der Teilnehmer müssen das gleiche Intervall verwenden.
      2. Wähle einen **Mitarbeiter** als Meeting-Gastgeber aus.

      {{ 3 | image: 'Gastgeber - Mitarbeiter auswählen', '70%' }}

11. Im Abschnitt _Teilnehmer_ definierst Du die Liste der Teilnehmer, für die Meetings geplant werden sollen:

    - Optional: Wähle die Option {% link_new **Auswahl** | features/administration/selections.md %} oder **Mitarbeiterfilter** über die Buttons oben aus und wähle rechts ein Element aus dem Dropdown-Menü, um die Liste aller Mitarbeiter zu filtern.
    - Aktiviere die **Checkbox** links neben einem Mitarbeiter, um diesen auszuwählen. Aktiviere die Checkbox oben in der Liste, um alle Mitarbeiter auf einmal aus- oder abzuwählen.

    {{ 4 | image: 'Participants', '60%' }}

12. Um Terminvorschläge für 1:1-Meetings zu erzeugen, klicke auf _Termine vorschlagen_{:.doc-button} unten auf der Seite. Du gelangst zurück zur Übersichtsseite.

Nachdem die Terminvorschläge generiert wurden, musst Du sie {% link_new in den Schichtplan eintragen | features/scheduling/meetings/scheduling-suggestions.md %}.
