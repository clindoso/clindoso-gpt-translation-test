---
title: Benutzerkonten verwalten
description: Sieh dir abgerechnete und nicht abgerechnete Benutzer an. Erstelle, bearbeite und lösche Benutzer. Verwalte den Benutzerzugriff über Benutzerrollen.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-2fa.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
redirect_from:
  - /de/user-administration/
redirect_reason: page used in intercom, updated filename on 06 December 2022
---

Richte Benutzerkonten in injixo ein, um die Mitarbeiter in deinem Unternehmen zu verwalten. 

Unter _Account > Benutzer_{:.breadcrumbs} erhältst du eine vollständige Übersicht über alle Benutzer:
- Abgerechnete Benutzer: Dieser Tab zeigt alle aktiven Benutzer auf deinem injixo-Tenant.
- Nicht abgerechnete Benutzer: Dieser Tab zeigt alle {% link_new deaktivierten Benutzer | features/administration/deactivate-employees.md %}, die sich nicht mehr bei injixo anmelden können. Deinem Unternehmen werden deaktivierte Benutzer nicht weiter {% link_new in Rechnung gestellt | getting-started/how-does-billing-work.md %}.

Um einen oder mehrere Benutzer zu finden, benutze das Suchfeld über der Benutzerliste. Benutze Kommata, um die Suchbegriffe voneinander zu trennen.
Um Benutzer nach ihrer Benutzerrolle zu filtern, klicke auf die Spaltenüberschrift **Benutzerrollen**. Ein Dialog öffnet sich, in dem du eine oder mehrere Benutzerrollen auswählen kannst. In der Benutzerliste werden alle Benutzer angezeigt, die mindestens eine der ausgewählten Benutzerrollen haben.

## Benutzer anlegen

Benutzer werden auch Mitarbeiter genannt. In injixo kannst du Benutzer an drei Stellen anlegen:
- _Account > Benutzer_{:.breadcrumbs}
- _WFM > Administration > Scheduling > Mitarbeiter_{:.breadcrumbs}
- {% link_new People | features/people/manage-people.md | #neuen-mitarbeiter-anlegen %}

> Hinweis
> 
> Du musst einen Benutzer nur einmal an einer der drei Stellen anlegen. injixo synchronisiert dann automatisch die Daten des Benutzers an den anderen beiden Stellen.

Um einen Benutzer zu erstellen, führe folgende Schritte aus:

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Klicke auf _Benutzer erstellen_{:.doc-button}.
3. Gib die Daten für den Benutzer ein und klicke auf _Erstellen_{:.doc-button}.

## Benutzerkonto bearbeiten

In injixo gibt es zwei Stellen, an denen du ein Benutzerkonto bearbeiten kannst, je nachdem, was du tun möchtest. In der folgenden Tabelle erhältst du einen Überblick darüber, welche Konfigurationsoptionen es gibt und wo du sie in injixo findest. Du kannst auf beide Stellen auch aus der Ansicht People zugreifen.

| Was ich tun möchte                                          | Wo ich es finde                                                                             |
| -------------------------------------------------- | ------------------------------------------------------------------------------------- |
| {% link_new Planungsbezogene Einstellungen für einen Benutzer konfigurieren | features/administration/employee-overview.md | #übersicht-über-die-mitarbeitereinstellungen %} (z.&nbsp;B. Aktivitäten zuweisen, Qualifikationsstufen hinzufügen, Verfügbarkeiten festlegen) | _WFM > Administration > Scheduling > Mitarbeiter_{:.breadcrumbs} |
| {% link_new Betriebszugehörigkeit eines Benutzers bearbeiten | getting-started/manage-user-accounts.md | #benutzerkonto-deaktivieren %}       | _WFM > Administration > Scheduling > Mitarbeiter_{:.breadcrumbs} |   
| Sprach- und Zeitzoneneinstellungen eines Benutzers bearbeiten | _Account > Benutzer_{:.breadcrumbs} |
| {% link_new Einem Benutzer eine neue Benutzerrolle zuweisen | getting-started/configure-user-roles.md | #benutzerrolle-einem-benutzer-zuweisen %} | _Account > Benutzer_{:.breadcrumbs} |
| {% link_new Zwei-Faktor-Authentifizierung erzwingen | getting-started/manage-2fa.md %}   | _Account > Benutzer_{:.breadcrumbs} |

Wenn du einen Benutzer bearbeiten möchtest, z.&nbsp;B. um dessen E-Mail-Adresse zu ändern, führe folgende Schritte aus:

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Klicke auf den Benutzernamen eines bestehenden Benutzers.
3. Ändere die Benutzereinstellungen.
4. Klicke auf _Speichern_{:.doc-button}.

### Admin-Zugriff gewähren

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Klicke auf den Benutzernamen eines bestehenden Benutzers.
3. Aktiviere im Abschnitt **Admin-Zugriff** die Checkbox **Admin-Zugriff gewähren**.
4. Klicke auf _Speichern_{:.doc-button}.

### Benutzer entsperren

Benutzerkonten werden nach drei fehlgeschlagenen Anmeldeversuchen mit einem falschen Passwort gesperrt. Um einen gesperrten Benutzer zu entsperren, führe folgende Schritte aus:

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.<br>
Die Benutzerliste zeigt ein gelbes {% icon lock %} neben dem Namen des gesperrten Benutzers an.
2. Klicke auf den Benutzernamen des gesperrten Benutzers.
3. Klicke im Abschnitt **Sicherheit** oben rechts auf _Benutzer entsperren_{:.doc-button}.

Wenn du einen Benutzer entsperrt hast, empfehlen wir, für diesen Benutzer ein neues Passwort zu setzen. 

### Neues Benutzerpasswort setzen

Hat ein Benutzer sein Passwort vergessen, kann er es über den Link **Hast Du Dein Passwort vergessen?** auf der Anmeldeseite selbst zurücksetzen. Alternativ kannst du ein neues Passwort für den Benutzer setzen, z.&nbsp;B. nachdem dessen Benutzerkonto gesperrt wurde.
Um ein neues Passwort für einen Benutzer zu setzen, führe folgende Schritte aus:

> Hinweis
>
> Benutzer erhalten keine Benachrichtigung über Passwortänderungen. Du musst ihnen ihr neues Passwort selbst mitteilen.

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Klicke auf den Benutzernamen eines bestehenden Benutzers.
3. Klicke im Abschnitt **Sicherheit** oben rechts auf _Neues Passwort setzen_{:.doc-button}.
4. Gib ein neues Passwort für den Benutzer ein.
5. Klicke auf _Speichern_{:.doc-button}.



## Benutzerkonto deaktivieren

Wenn du wissen möchtest, welche Folgen es hat, Benutzerkonten zu deaktivieren, lies {% link_new diesen Artikel | features/administration/deactivate-employees.md %}.

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Klicke auf den Benutzernamen eines bestehenden Benutzers.
3. Klicke unten rechts auf _Löschen_{:.doc-button}.  
   Ein Fenster öffnet sich.
4. Um einen Benutzer zu deaktivieren, klicke auf _Betriebszugehörigkeit_{:.doc-button} und lege ein Austrittsdatum fest. Alle Planungsdaten bleiben erhalten. Du kannst den Benutzer später reaktivieren.

Erfahre, wie du {% link_new einen Benutzer reaktivierst | features/administration/deactivate-employees.md | #mitarbeiter-reaktivieren %}.

## Benutzerkonto löschen

> Achtung
>
> Gelöschte Benutzerkonten können nicht wiederhergestellt werden. Wenn du ein Benutzerkonto löschst, wird der Benutzer aus allen aktuellen und zukünftigen Schichtplänen entfernt, in denen er geplant war.

Um ein Benutzerkonto dauerhaft zu löschen, führe folgende Schritte aus:

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Klicke auf den Benutzernamen eines bestehenden Benutzers.
3. Klicke unten rechts auf _Löschen_{:.doc-button}.  
   Ein Fenster öffnet sich.
4. Aktiviere die Checkbox **Ich habe verstanden, dass der Benutzer \<Benutzername\> und die dazugehörigen Plandaten gelöscht werden**.
5. Klicke auf _Löschen_{:.doc-button}. 

## Benutzerliste als CSV-Datei exportieren

Du kannst eine komplette oder gefilterte Benutzerliste als CSV-Datei exportieren. Du kannst diese CSV-Datei beispielsweise in externe Datenbanken und Tools importieren, z.&nbsp;B. Data Warehouse oder SAP- und HR-Systeme.

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. (Optional) Um die Liste der angezeigten Benutzer einzugrenzen, verwende das Suchfeld oder den Rollenfilter.
3. Klicke oben rechts auf _Als CSV exportieren_{:.doc-button}.  
   Die CSV-Datei wird auf deinen Computer heruntergeladen.

Die CSV-Datei enthält den Nachnamen, den Vornamen und die E-Mail-Adresse der Benutzer. Die Exportfunktion verwendet ein festes Dateiformat, das nicht geändert werden kann.
