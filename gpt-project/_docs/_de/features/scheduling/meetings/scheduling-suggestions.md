---
title: Terminvorschläge prüfen und übernehmen
product_label:
  - advanced
  - enterprise
description: Terminvorschläge für Meetings prüfen und in den Schichtplan schreiben.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/meetings/meetings-overview.md
---

In diesem Artikel lernst Du, wie Du:

- überprüfst, ob der Prozess zur Erstellung von Terminvorschlägen für Meetings erfolgreich war.
- die vorgeschlagenen Meeting-Termine sichtest und sie in den Schichtplan überträgst.
- Dir die Planungsergebnisse ansiehst.

Neu im Meetings-Modul? Lerne zuerst {% link_new die Grundlagen | features/scheduling/meetings/meetings-overview.md %}.

## Warten, bis der Prozess beendet ist

Wenn Du den Prozess zur {% link_new Erstellung von Terminvorschlägen für Meetings | features/scheduling/meetings/meetings-overview.md | #vorschläge-für-meeting-termine-generieren %} startest, erscheint ein Eintrag in der Tabelle _Generierte Vorschläge_. Er zeigt an, wann der Prozess gestartet wurde, den Meeting-Typ und die ausgewählte Planungseinheit.

Warte, bis der Prozess abgeschlossen ist. Dies kann einige Zeit dauern, je nach gewähltem Zeitraum.

## Prüfen, ob der Prozess erfolgreich war

Nachdem der Prozess zur Erstellung von Terminvorschlägen für Meetings abgeschlossen ist, zeigt die Spalte _Aktionen_ einen dieser Texte an:

- _Vorschläge anschauen_: Der Prozess wurde erfolgreich beendet.
- _Konflikt anzeigen_: Der Prozess konnte aufgrund von Konflikten mit dem bestehenden Schichtplan nicht beendet werden. Ein Klick auf den Text zeigt die Details an.
- _Nicht möglich_: Der Prozess konnte nicht abgeschlossen werden, da der ausgewählte Gastgeber nicht geplant werden konnte (erscheint nur bei 1:1-Meetings oder Gruppenterminen mit Gastgeber).

Die Spalte _Teilnehmerstatus_ zeigt an, für wie viele Teilnehmer es möglich war, Terminvorschläge zu generieren, und für wie viele dies nicht möglich war, zum Beispiel: _4 verfügbar, 2 nicht verfügbar_. Nachdem Du auf den Link _Vorschläge anschauen_ geklickt hast, erklärt die _Vorschläge_-Seite, warum einigen Mitarbeitern möglicherweise kein Meeting-Termin zugeteilt werden konnte.

## Vorschläge prüfen und übernehmen

Wenn der Prozess erfolgreich Vorschläge generiert hat, kannst Du diese prüfen und übernehmen:

1.  Klicke im Abschnitt _Generierte Vorschläge_ auf _Vorschläge anschauen_{:.doc-button} in der entsprechenden Zeile in der Spalte **Aktionen**. Dadurch gelangst Du auf die Seite _Vorschläge_.
    <!-- Hier fehlt noch das Bild im Assets-Ordner -->

            {{ 5 | image: 'Erstellte Vorschläge - Link zum Anzeigen von Vorschlägen' }}

2.  Auf der Seite _Vorschläge_ siehst Du eine Tabelle mit den folgenden Informationen:

    - _Vorgeschlagener Termin_: der vorgeschlagene Termin für das Meeting
    - _Zu planende Aktivität_: das Meeting, das geplant werden soll
    - _Teilnehmer_: der Name des Mitarbeiters, der am Meeting teilnehmen wird
    - _Ersetzte Aktivität_: die Aktivität, die durch das Meeting ersetzt wird
    - _Geänderte Deckung_: Informationen darüber, wie sich das geplante Meeting auf die Deckung der ersetzten Aktivität auswirken würde; wenn Du mit der Maus über die Deckungswerte fährst, erscheint ein Popover mit Details

    Hinweis: Die Werte für die Deckung werden während der Erstellung von Terminvorschlägen berechnet. Nachträgliche Änderungen am Schichtplan beeinflussen die hier angezeigten Deckungswerte nicht.

    In der Tabelle werden auch Mitarbeiter angezeigt, für die es keine Vorschläge gibt. Sie sind im ausgewählten Zeitraum höchstwahrscheinlich im Urlaub oder krank.

    {{ 2 | image: 'Terminvorschläge - Gruppentermine' }}

3.  Um bestimmte Mitarbeiter nicht für Meetings zu planen, deaktiviere die **Checkbox** auf der linken Seite (optional). Mit der Checkbox oben wählst Du alle Mitarbeiter auf einmal ab. Die Ergebnisseite zeigt abgewählte Mitarbeiter als _Herausgenommen_ an.

4.  Klicke auf _Einzeltermine anlegen_{:.doc-button}, um 1:1 Meetings in den Schichtplan zu schreiben. Bei Self-Learning Sessions heißt der Button _Plane Sessions_{:.doc-button}, bei Gruppenterminen _Gruppentermine anlegen_{:.doc-button}. Klicke auf _Zurück zum Überblick_{:.doc-button}, wenn Du die _Vorschläge_-Seite verlassen möchtest, ohne Vorschläge in den Schichtplan zu schreiben.

## Planungsergebnisse prüfen

Es kann einige Zeit dauern, bis die ausgewählten Vorschläge in den Schichtplan geschrieben wurden. Klicke anschließend auf den Link **Plan anschauen**, um Dir die neuen Meeting-Termine im Schichtplan anzusehen. Im Bereich _Generierte Vorschläge_ auf der Übersichtsseite hat sich der Teilnehmerstatus für den jeweiligen Eintrag geändert. Es wird nun angezeigt, für wie viele Teilnehmer Meetings geplant wurden.

Du kannst jetzt die detaillierten Planungsergebnisse überprüfen:

1. Klicke im Abschnitt _Generierte Vorschläge_ in der jeweiligen Zeile auf den Link **Ergebnis anschauen**. Die Ergebnisseite zeigt die Tabs _Angelegt_, _Fehlgeschlagen_ und _Herausgenommen_. Du findest Deine Mitarbeiter in den jeweiligen Kategorien abhängig davon, ob der Prozess Termin-Vorschläge für Mitarbeiter erstellen konnte und Du diese übernommen hast. Inaktive Tabs bedeuten, dass es keine Mitarbeiter in dieser Kategorie gibt.
2. Klicke auf einen **Tab**, um die Details zu sehen.

   {{ 4 | image: 'Ergebnisseite - Gruppentermine' }}

Du kannst entweder alle Mitarbeiter in den Kategorien _Fehlgeschlagen_ und _Herausgenommen_ ignorieren oder einen neuen Planungsprozess mit anderen Parametern starten, um zu versuchen, auch diese zu planen. Du hast auch die Möglichkeit, manuell Meetings für diese Mitarbeiter unter _Plan > Schedules_{:.breadcrumbs} oder _Plan > Schicht Center_{:.breadcrumbs} hinzuzufügen.
