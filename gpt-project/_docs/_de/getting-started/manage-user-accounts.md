---
title: Mitarbeiter für Abrechnung verwalten
description: Erfahre, wie du aktive und inaktive Mitarbeiter einsehen kannst und wie du Mitarbeiter deaktivieren und löschen kannst.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/how-does-billing-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/people/configure-people-settings.md
  - overwrite_title: Add title for untranslated source
    filepath: features/people/configure-people-settings.md
    overwrite_title: Add title for untranslated source
    filepath: features/administration/deactivate-employees.md
redirect_from:
  - /de/user-administration/
redirect_reason: page used in intercom, updated filename on 06 December 2022
---

> Hinweis
>
> Dieser Artikel dokumentiert den aktuellen Status der neuen **People**-App. Bis alle hier beschriebenen Funktionalitäten vollständig von bisherigen Features übertragen wurden, findest du sie weiterhin an der gewohnten Stelle.

## Aktive und inaktive Mitarbeiter anzeigen

Unter _People_{:.breadcrumbs} kannst du sehen, welche Mitarbeiter für dein Unternehmen abgerechnet werden. Oben links auf der Seite kannst du auswählen, welche Informationen du anzeigen möchtest:

- **Aktiv**: Dies zeigt alle Mitarbeiter an, die für dein Unternehmen abgerechnet werden.
- **Inaktiv**: Dies zeigt alle {% link_new deaktivierten Mitarbeiter | getting-started/manage-user-accounts.md | #mitarbeiter-deaktivieren %} an. Deaktivierte Mitarbeiter können sich nicht mehr bei injixo anmelden. Deinem Unternehmen werden deaktivierte Mitarbeiter nicht {% link_new in Rechnung gestellt | getting-started/how-does-billing-work.md %}.

Um einen oder mehrere einzelne Mitarbeiter zu finden, verwende das Suchfeld über der Mitarbeiterliste. Verwende Kommas, um die Suchbegriffe voneinander zu trennen.

Um Mitarbeiter nach Rollen zu filtern, verwende das Dropdown-Menü neben dem Suchfeld und wähle eine Rolle aus.

## Mitarbeiterliste als CSV-Datei exportieren

Du kannst eine komplette oder gefilterte Mitarbeiterliste als CSV-Datei exportieren. Du kannst diese CSV-Datei beispielsweise in externe Datenbanken und Tools importieren, z.&nbsp;B. Data Warehouse oder SAP- und HR-Systeme.

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. (Optional) Um die Liste der angezeigten Mitarbeiter einzugrenzen, verwende das Suchfeld oder den Rollenfilter.
3. Klicke oben rechts auf _Als CSV exportieren_{:.doc-button}.  
   Die CSV-Datei wird auf deinen Computer heruntergeladen.

Die durch Kommas getrennte CSV-Datei enthält den Nachnamen, den Vornamen und die E-Mail-Adresse der Mitarbeiter. Die Exportfunktion verwendet ein festes Dateiformat, das nicht geändert werden kann.

## Mitarbeiter deaktivieren

Wenn du wissen möchtest, welche Folgen es hat, Mitarbeiter zu deaktivieren, lies {% link_new diesen Artikel | features/administration/deactivate-employees.md %}.

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Klicke auf den Benutzernamen eines bestehenden Benutzers.
3. Klicke unten rechts auf _Löschen_{:.doc-button}.  
   Ein Fenster öffnet sich.
4. Um einen Benutzer zu deaktivieren, klicke auf _Betriebszugehörigkeit_{:.doc-button} und lege ein Austrittsdatum fest. Alle Planungsdaten bleiben erhalten. Du kannst den Benutzer später reaktivieren.

Erfahre, wie du {% link_new einen Benutzer reaktivierst | features/administration/deactivate-employees.md | #mitarbeiter-reaktivieren %}.

## Mitarbeiter löschen

> Achtung
>
> Gelöschte Mitarbeiter können nicht wiederhergestellt werden. Wenn du einen Mitarbeiter löschst, wird er aus allen aktuellen und zukünftigen Schichtplänen entfernt, in denen er geplant war.

Um einen Mitarbeiter dauerhaft zu löschen, führe folgende Schritte aus:

1. Gehe zu _People_{:.breadcrumbs}.
2. Suche nach dem Mitarbeiter, den du löschen möchtest und klicke auf dessen Kachel.
3. Klicke unten rechts im Konfigurationsfenster auf _Mitarbeiter löschen_{:.doc-button}.
4. Klicke im Bestätigungsdialog auf _Mitarbeiter löschen_{:.doc-button}.
