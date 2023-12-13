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

Wenn Du den Prozess zur {% link_new Erstellung von Terminvorschlägen für Meetings | features/scheduling/meetings/meetings-overview.md | #vorschläge-für-meeting-termine-generieren %} startest, erscheint ein Eintrag in der Tabelle *Generierte Vorschläge*. Er zeigt an, wann der Prozess gestartet wurde, den Meeting-Typ und die ausgewählte Planungseinheit.

Warte, bis der Prozess abgeschlossen ist. Dies kann einige Zeit dauern, je nach gewähltem Zeitraum.

## Prüfen, ob der Prozess erfolgreich war

Nachdem der Prozess zur Erstellung von Terminvorschlägen für Meetings abgeschlossen ist, zeigt die Spalte *Aktionen* einen dieser Texte an:
- *Vorschläge anschauen*: Der Prozess wurde erfolgreich beendet.
- *Konflikt anzeigen*: Der Prozess konnte aufgrund von Konflikten mit dem bestehenden Schichtplan nicht beendet werden. Ein Klick auf den Text zeigt die Details an.
- *Nicht möglich*: Der Prozess konnte nicht abgeschlossen werden, da der ausgewählte Gastgeber nicht geplant werden konnte (erscheint nur bei 1:1-Meetings oder Gruppenterminen mit Gastgeber).

Die Spalte *Teilnehmerstatus* zeigt an, für wie viele Teilnehmer es möglich war, Terminvorschläge zu generieren, und für wie viele dies nicht möglich war, zum Beispiel: *4 verfügbar, 2 nicht verfügbar*. Nachdem Du auf den Link *Vorschläge anschauen* geklickt hast, erklärt die *Vorschläge*-Seite, warum einigen Mitarbeitern möglicherweise kein Meeting-Termin zugeteilt werden konnte.

## Vorschläge prüfen und übernehmen

Wenn der Prozess erfolgreich Vorschläge generiert hat, kannst Du diese prüfen und übernehmen:

1. Klicke im Abschnitt *Generierte Vorschläge* auf *Vorschläge anschauen*{:.doc-button} in der entsprechenden Zeile in der Spalte **Aktionen**. Dadurch gelangst Du auf die Seite *Vorschläge*.
<!-- Hier fehlt noch das Bild im Assets-Ordner -->
        {{ 5 | image: 'Erstellte Vorschläge - Link zum Anzeigen von Vorschlägen' }}

2. Auf der Seite *Vorschläge* siehst Du eine Tabelle mit den folgenden Informationen:

    - *Vorgeschlagener Termin*: der vorgeschlagene Termin für das Meeting
    - *Zu planende Aktivität*: das Meeting, das geplant werden soll
    - *Teilnehmer*: der Name des Mitarbeiters, der am Meeting teilnehmen wird
    - *Ersetzte Aktivität*: die Aktivität, die durch das Meeting ersetzt wird
    - *Geänderte Deckung*: Informationen darüber, wie sich das geplante Meeting auf die Deckung der ersetzten Aktivität auswirken würde; wenn Du mit der Maus über die Deckungswerte fährst, erscheint ein Popover mit Details

    Hinweis: Die Werte für die Deckung werden während der Erstellung von Terminvorschlägen berechnet. Nachträgliche Änderungen am Schichtplan beeinflussen die hier angezeigten Deckungswerte nicht.

    In der Tabelle werden auch Mitarbeiter angezeigt, für die es keine Vorschläge gibt. Sie sind im ausgewählten Zeitraum höchstwahrscheinlich im Urlaub oder krank.

    {{ 2 | image: 'Terminvorschläge - Gruppentermine' }}

3. Um bestimmte Mitarbeiter nicht für Meetings zu planen, deaktiviere die **Checkbox** auf der linken Seite (optional). Mit der Checkbox oben wählst Du alle Mitarbeiter auf einmal ab. Die Ergebnisseite zeigt abgewählte Mitarbeiter als *Herausgenommen* an.

4. Klicke auf *Einzeltermine anlegen*{:.doc-button}, um 1:1 Meetings in den Schichtplan zu schreiben. Bei Self-Learning Sessions heißt der Button *Plane Sessions*{:.doc-button}, bei Gruppenterminen *Gruppentermine anlegen*{:.doc-button}. Klicke auf *Zurück zum Überblick*{:.doc-button}, wenn Du die *Vorschläge*-Seite verlassen möchtest, ohne Vorschläge in den Schichtplan zu schreiben.

## Planungsergebnisse prüfen

Es kann einige Zeit dauern, bis die ausgewählten Vorschläge in den Schichtplan geschrieben wurden. Klicke anschließend auf den Link **Plan anschauen**, um Dir die neuen Meeting-Termine im Schichtplan anzusehen. Im Bereich *Generierte Vorschläge* auf der Übersichtsseite hat sich der Teilnehmerstatus für den jeweiligen Eintrag geändert. Es wird nun angezeigt, für wie viele Teilnehmer Meetings geplant wurden.

Du kannst jetzt die detaillierten Planungsergebnisse überprüfen:

1. Klicke im Abschnitt *Generierte Vorschläge* in der jeweiligen Zeile auf den Link **Ergebnis anschauen**. Die Ergebnisseite zeigt die Tabs *Angelegt*, *Fehlgeschlagen* und *Herausgenommen*. Du findest Deine Mitarbeiter in den jeweiligen Kategorien abhängig davon, ob der Prozess Termin-Vorschläge für Mitarbeiter erstellen konnte und Du diese übernommen hast. Inaktive Tabs bedeuten, dass es keine Mitarbeiter in dieser Kategorie gibt.
2. Klicke auf einen **Tab**, um die Details zu sehen.

    {{ 4 | image: 'Ergebnisseite - Gruppentermine' }}

Du kannst entweder alle Mitarbeiter in den Kategorien *Fehlgeschlagen* und *Herausgenommen* ignorieren oder einen neuen Planungsprozess mit anderen Parametern starten, um zu versuchen, auch diese zu planen. Du hast auch die Möglichkeit, manuell Meetings für diese Mitarbeiter unter *Plan > Schedules*{:.breadcrumbs} oder *Plan > Schicht Center*{:.breadcrumbs} hinzuzufügen.
