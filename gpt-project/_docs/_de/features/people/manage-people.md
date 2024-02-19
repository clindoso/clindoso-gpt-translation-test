---
title: Mitarbeiter verwalten
product_label:
  - advanced
  - enterprise
description: Erfahre, wie du Mitarbeiter anlegen, ansehen, bearbeiten und löschen kannst.
beta-feature: true
---

Unter People kannst du die wichtigsten Daten für die Mitarbeiter in deinem Unternehmen verwalten:
- Profile für Mitarbeiter erstellen, bearbeiten und löschen
- Eine injixo-Einladung an einen neuen Mitarbeiter senden (Begrüßungsmail)
- Zu den Benutzerkontoeinstellungen eines Mitarbeiters gehen
- Zu den Stammdaten eines Mitarbeiters in WFM gehen

 > Benutzer mit Admin-Zugriff haben standardmäßig Zugriff auf People. 
 > 
 > Um anderen Benutzern {% link_new Zugriff auf People zu gewähren | getting-started/configure-user-roles.md %}, gehe zu _Account > Rollen_{:.breadcrumbs}. 

## Neuen Mitarbeiter anlegen

1. Gehe zu _People_{:.breadcrumbs}.
2. Klicke auf _\+ Neuer Mitarbeiter_{:.doc-button}.
3. Fülle die Allgemeinen Informationen (Pflichtfelder) aus:
   - **Vorname** und **Nachname**, und optional **Zweiter Vorname** 
   - **Personalnummer**: Eindeutige Kennung für den Mitarbeiter in deinem Unternehmen.
   - **E-Mail (injixo-Anmeldung)**: Gib die E-Mail-Adresse an, mit der sich der Mitarbeiter bei injixo anmeldet.
4. Um den Mitarbeiter zur Anmeldung bei injixo einzuladen, aktiviere die Checkbox **Begrüßungsmail senden**.  
    Du kannst die Begrüßungsmail nur beim Anlegen eines Mitarbeiters senden. Die E-Mail enthält die Anleitung zum Setzen eines Passworts und einen Link zur Anmeldeseite von injixo.
5. (Optional) Du kannst auch die Telefonnummer und weitere Kontaktdaten des Mitarbeiters angeben. 
Die Eingabe im Feld **Anrede** wird in injixo nirgendwo verwendet. Du kannst die Anrede des Mitarbeiters z.&nbsp;B. in Newslettern zur Ansprache verwenden.
7. Klicke auf _Mitarbeiter anlegen_{:.doc-button}.   
   Wenn die Checkbox **Begrüßungsmail senden** aktiviert ist, sendet injixo dem Mitarbeiter eine Begrüßungsmail.

## Einen Mitarbeiter zur Anmeldung bei injixo einladen

Du kannst {% link_new einen Mitarbeiter nur dann per Begrüßungsmail zur Anmeldung bei injixo einladen | features/people/manage-people.md | #neuen-mitarbeiter-anlegen %}, wenn du einen neuen Mitarbeiter anlegst.

## Einen Mitarbeiter ansehen oder bearbeiten

1. Gehe zu _People_{:.breadcrumbs}.
2. (Optional) Um nach einem Mitarbeiter zu suchen, verwende das Feld **Suche**.
3. Klicke auf einen Mitarbeiter in der Liste.  
   Das Mitarbeiterprofil wird rechts neben der Liste angezeigt. Um das Mitarbeiterprofil zu schließen, klicke auf _Abbrechen_{:.doc-button} oder drücke die **Esc**-Taste auf deiner Tastatur.
4. Bearbeite das Mitarbeiterprofil.

   > Hinweis
   > 
   > Wenn du die E-Mail-Adresse eines Mitarbeiters änderst, kann sich der Mitarbeiter unter der zuletzt verwendeten E-Mail-Adresse nicht mehr bei injixo anmelden. Stelle sicher, dass du dem Mitarbeiter die neue E-Mail-Adresse mitteilst. injixo versendet keine Mitteilung über die geänderte E-Mail-Adresse an die Mitarbeiter.

5. Klicke auf _Änderungen speichern_{:.doc-button}.

## Einen Mitarbeiter löschen

 > Achtung
   > 
   > Gelöschte Mitarbeiter können nicht wiederhergestellt werden. Wenn du einen Mitarbeiter löschst, wird sie aus allen aktuellen und zukünftigen Schichtplänen entfernt, in denen sie geplant war. Das Löschen eines Mitarbeiters hat keinen Einfluss auf die historischen Daten zur Planeinhaltung in {% link_new Intraday | features/intraday/adherence-intraday.md %}.
   
1. Gehe zu _People_{:.breadcrumbs}.
2. Klicke auf einen Mitarbeiter in der Liste.  
   Das Mitarbeiterprofil wird rechts neben der Liste angezeigt.
2. Klicke auf _Mitarbeiter löschen_{:.doc-button}.
3. Klicke im Bestätigungsdialog auf _Mitarbeiter löschen_{:.doc-button}.

Um sicherzustellen, dass dein Schichtplan nach dem Löschen eines Mitarbeiters aktuell ist, führe die Joboptimierung aus.
