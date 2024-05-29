---
title: Mitarbeiter konfigurieren
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du Mitarbeiter anlegen, ansehen, bearbeiten und löschen kannst.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/people/configure-people-settings.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-user-accounts.md
redirect_from: /people-overview/
redirect_reason: Renamed from /people-overview/ to /manage-people/ in Jan 2023
---

> Hinweis
>
> Dieser Artikel dokumentiert den aktuellen Status der neuen **People**-App. Bis alle hier beschriebenen Funktionalitäten vollständig von bisherigen Features übertragen wurden, findest du sie weiterhin an der gewohnten Stelle.

Mitarbeiter mit Adminrechten haben standardmäßig Zugriff auf _People_{:.breadcrumbs}. Je nachdem, wie dein Unternehmen Rollen und Adminrechte verwaltet, musst du möglicherweise {% link_new Zugriffsrechte für **People** an andere Mitarbeiter in deinem Unternehmen vergeben | getting-started/configure-user-roles.md %}.

## Überblick über die People-Seite

Die **People**-Seite enthält eine Übersicht aller vorhandenen Mitarbeiter in deinem Unternehmen. Neben der Übersicht, in der du {% link_new sehen und festlegen | getting-started/manage-user-accounts.md %} kannst, welche Mitarbeiter für dein Unternehmen abgerechnet werden, kannst du auf einen Blick folgende Informationen zu jedem Mitarbeiter einsehen:

- Adminrechte: Wenn der Mitarbeiter Adminrechte hat, wird neben dessen Namen ein Admin-Label angezeigt.
- Ausstehende Bestätigung der E-Mail-Adresse: Wenn der Mitarbeiter seine E-Mail-Adresse noch nicht bestätigt hat, signalisiert ein {% icon clock %} neben dessen E-Mail-Adresse, dass die Bestätigung noch aussteht.
- {% link_new Status der Zwei-Faktor-Authentifizierung | getting-started/manage-2fa.md | #2fa-einstellungen-anderer-benutzer-einsehen %}: Ein Icon neben der E-Mail-Adresse des Mitarbeiters zeigt an, ob für den Mitarbeiter 2FA aktiviert ist oder nicht.
- Zugewiesene Rollen: In der rechten oberen Ecke der Kachel jedes Mitarbeiters werden die zugewiesenen Rollen angezeigt.

Erfahre, wie du {% link_new die Mitarbeitereinstellungen verwaltest | features/people/configure-people-settings.md %}.

## Mitarbeiter anlegen

> Hinweis
>
> Du kannst während des Anlegens eines Mitarbeiters nicht zu einem abgeschlossenen Schritt zurückkehren. Bevor du bei einem Schritt auf _Weiter_{:.doc-button} klickst, stelle sicher, dass die eingegebenen Informationen korrekt und vollständig sind. Wenn du während der Mitarbeiterkonfiguration feststellst, dass du etwas bei einem bereits abgeschlossenen Schritt ändern musst, schließe zuerst den Konfigurationsvorgang ab und rufe dann das Mitarbeiterprofil erneut auf.

1. Gehe zu _People_{:.breadcrumbs}.
2. Klicke oben rechts auf _\+ Neuer Mitarbeiter_{:.doc-button}.
3. Folge dem Konfigurationsassistenten durch die drei Schritte der Mitarbeiterkonfiguration. Klicke auf die Links, um zu erfahren, wie du die [allgemeinen Informationen](#allgemeine-informationen), [Betriebszugehörigkeit](#betriebszugehörigkeit), [Rollen](#rollen) und Adminrechte konfigurierst.
4. Klicke auf _Speichern_{:.doc-button}.
   Du hast einen neuen Mitarbeiter angelegt. Jetzt kannst du auf [weitere Konfigurationsoptionen](#weitere-konfigurationsoptionen) für den Mitarbeiter zugreifen.

### Allgemeine Informationen

| Parameter                                    | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Vorname**/**Nachname**/**Zweiter Vorname** | Der zweite Vorname ist optional.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Personalnummer**                           | Lasse von injixo automatisch eine eindeutige Kennung für den Mitarbeiter in deinem Unternehmen erzeugen oder trage selbst eine ein.                                                                                                                                                                                                                                                                                                                                                                |
| **E-Mail (injixo-Anmeldung)**                | Gib die eindeutige E-Mail-Adresse ein, die der Mitarbeiter verwendet, um sich bei injixo anzumelden. Um dem Mitarbeiter die Einladung zur Anmeldung bei injixo zu senden, aktiviere die Checkbox **Begrüßungsmail senden**.<br>Du kannst die Begrüßungsmail nur beim Anlegen eines Mitarbeiters senden. Die E-Mail enthält die Anleitung zum Setzen eines Passworts und einen Link zur Anmeldeseite von injixo. Wenn ein Mitarbeiter ein Passwort festlegt, gilt die E-Mail-Adresse als bestätigt. |

> Hinweis
>
> Wenn du unten auf der Seite **Allgemeine Informationen** auf _Weiter_{:.doc-button} klickst, legt injixo den Mitarbeiter sofort mit einer aktiven Betriebszugehörigkeit an. Wenn du die Option für die Begrüßungsmail ausgewählt hast, kann sich der Mitarbeiter bei injixo anmelden. Du kannst den Anlegevorgang nicht mehr abbrechen. Wenn du den Anlegevorgang abgeschlossen hast, kannst du den Mitarbeiter [bearbeiten](#mitarbeiter-ansehen-oder-bearbeiten) oder [löschen](#mitarbeiter-löschen).

### Betriebszugehörigkeit

| Parameter      | Beschreibung                                                                                                                                                                                                                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gültig von** | Standardmäßig wird das Startdatum der Betriebszugehörigkeit automatisch auf das aktuelle Datum gesetzt. Der Mitarbeiter wird deinem Unternehmen ab dem Monat, in dem das Startdatum liegt, in Rechnung gestellt. Wenn du möchtest, dass der Mitarbeiter später abgerechnet wird, ändere das Startdatum. |
| **Gültig bis** | Standardmäßig ist das Enddatum der Betriebszugehörigkeit leer. Wenn der Mitarbeiter nur einen befristeten Vertrag hat, setze ein Enddatum.                                                                                                                                                              |

Erfahre, wie du die {% link_new Betriebszugehörigkeit eines Mitarbeiters ändern | getting-started/manage-user-accounts.md | #mitarbeiter-deaktivieren %} kannst, nachdem du den Anlegevorgang abgeschlossen hast.

### Rollen

| Parameter                | Beschreibung                                                                                                                                                                                  |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------- |
| **Adminrechte vergeben** | Nur Mitarbeiter mit Adminrechten können anderen Mitarbeitern Adminrechte geben. Erfahre, wie du {% link_new Adminrechte vergeben                                                              | features/people/configure-people-settings.md            | #adminrechte-vergeben %} kannst. |
| Rollenliste              | Verwende das Suchfeld, um eine bestimmte Rolle zu finden oder scrolle in der Liste. Aktiviere die Checkbox für jede Rolle, die du dem Mitarbeiter zuweisen möchtest. {% link_new Erfahre mehr | getting-started/configure-user-roles.md %} über Rollen. |

## Weitere Konfigurationsoptionen

Wenn du einen Mitarbeiter angelegt hast, kannst du auf weitere Konfigurationsoptionen zugreifen. In den folgenden Abschnitten findest du Informationen zu den zusätzlichen Parametern auf den einzelnen Tabs des Konfigurationsfensters.

### Tab Profil

Auf dem Tab **Profil** kannst du die Parameter einsehen und bearbeiten, die du während des Anlegevorgangs auf der Seite [**Allgemeine Informationen**](#allgemeine-informationen) konfiguriert hast. Außerdem kannst du nun bei Bedarf weitere persönliche Daten wie den Familienstand oder Kontaktdaten eintragen.

<!---At the bottom, you can {% link_new add and edit external identifiers | features/acd-integration/cloud/import-agent-status-data.md | #map-external-identifiers-to-people-in-injixo %}.--->

### Tab Zugriffsrechte

Erfahre, wie du die {% link_new Zugriffsrechte für einen Mitarbeiter | features/people/configure-people-settings.md %} konfigurierst. Dazu gehört zum Beispiel das Erzwingen von 2FA oder das Setzen eines neuen Passworts.

## Mitarbeiter ansehen oder bearbeiten

1. Gehe zu _People_{:.breadcrumbs}.
2. (Optional) Um nach einem Mitarbeiter zu suchen, verwende das Suchfeld.
3. Klicke auf einen Mitarbeiter in der Liste.  
   Die Mitarbeiterdetails werden rechts geöffnet. Um die Details zu schließen, klicke auf _Schließen_{:.doc-button}.
4. Um die Mitarbeiterdetails zu bearbeiten, klicke oben rechts in dem Abschnitt, den du bearbeiten möchtest, auf {% icon pencil | icon-only %} **Bearbeiten**.
   > Hinweis
   >
   > Wenn du die E-Mail-Adresse änderst, kann der Mitarbeiter sich nicht mehr mit seiner bisherigen E-Mail-Adresse bei injixo anmelden. Der Mitarbeiter wird nicht automatisch von injixo über die geänderte E-Mail-Adresse informiert.
5. Klicke auf _Speichern_{:.doc-button}.

## Mitarbeiter löschen

> Achtung
>
> Gelöschte Mitarbeiter können nicht wiederhergestellt werden. Wenn du einen Mitarbeiter löschst, wird er aus allen aktuellen und zukünftigen Schichtplänen entfernt, in denen er geplant war. Das Löschen eines Mitarbeiters hat keinen Einfluss auf die historischen Daten zur Planeinhaltung in {% link_new Intraday | features/intraday/adherence-intraday.md %}.

1. Gehe zu _People_{:.breadcrumbs}.
2. Klicke auf einen Mitarbeiter in der Liste.  
   Das Mitarbeiterprofil wird rechts neben der Liste angezeigt.
3. Klicke unten rechts auf _Mitarbeiter löschen_{:.doc-button}.
4. Klicke im Bestätigungsfenster auf _Mitarbeiter löschen_{:.doc-button}.

Um sicherzustellen, dass dein Schichtplan nach dem Löschen eines Mitarbeiters aktuell ist, führe die {% link_new Joboptimierung | features/scheduling/schedules/schedules-job-optimization.md %} aus.

## Warum kann ich einen Mitarbeiter nicht über die Suche finden?

Mitarbeiter mit Adminrechten können immer alle Mitarbeiter im Unternehmen sehen.

Wenn du keine Adminrechte hast, kann es verschiedene Gründe geben, warum du einen Mitarbeiter nicht über die Suche finden kannst. Um herauszufinden, warum du einen Mitarbeiter nicht in der Liste siehst, überprüfe, ob folgendes zutrifft:

- Der Mitarbeiter ist einer Planungseinheit zugewiesen, auf die du mindestens Lesezugriff hast.
- Die Zuweisung des Mitarbeiters zur Planungseinheit ist noch gültig. Wenn du dir nicht sicher bist, bitte einen Mitarbeiter mit Adminrechten, das Start- und Enddatum der Zuweisung zur Planungseinheit für den jeweiligen gesuchten Mitarbeiter zu prüfen. Wenn kein Start- und Enddatum konfiguriert ist, ist die Zuweisung des Mitarbeiters immer gültig.
