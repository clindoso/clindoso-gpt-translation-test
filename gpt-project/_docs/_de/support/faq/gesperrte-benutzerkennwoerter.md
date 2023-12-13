---
title: Gesperrte Benutzerpasswörter
product_label:
  - on-premise
---

In diesem Artikel lernst Du, wie du mit mit unterschiedlichen Zugriffsproblemen umgehst.

## Benutzer gesperrt

Benutzer der Gruppe *System* können andere Benutzer wieder freischalten:

1. Gehe zu *Administration > System > Benutzerrechte*{:.breadcrumbs}.
2. Aktiviere die Checkbox **Anmeldung** erneut.
3. Klicke *OK*{:.doc-button}.  

Betroffene Benutzer können sich wieder anmelden.

## Benutzerpasswort vergessen

Hat ein Benutzer sein Passwort vergessen, kann jeder Benutzer mit Admin-Rechten den Benutzer wieder freischalten und ein neues Passwort vergeben.

1. Gehe zu *Administration > System > Benutzerrechte*{:.breadcrumbs}.
2. Klicke auf den **Benutzer** in der Liste.
3. Optional: Ist der Benutzer gesperrt, setze aktiviere erneut die Checkbox **Anmeldung**.
4. Gib ein neues **Passwort** ein.
5. Klicke *OK*{:.doc-button}.

## Admin gesperrt

Der Admin-Benutzer wird nach mehrfacher Anmeldung mit einem falschen Passwort gesperrt. Die Logdatei *security.log* im Server-Verzeichnis zeigt die Anmeldeversuche.

Auch externe Anwendungen wie z. B. Xlink oder Skripte können den Admin-Benutzer sperren. Bei einer Passwort-Änderung musst Du das das Passwort ggf. auch in Deiner {% link_new Xlink-Installation | features/acd-integration/xlink-installation-configuration.md | #on-premise-anmeldedaten-konfigurieren %} und in Skript-Konfigurationsdateien anpassen.

Um den Admin-Benutzer (mit der ID 2) freizuschalten, musst Du den *InVision WFM Enterprise*-Dienst neu starten. Wenn der Neustart nicht hilft, führe das folgende Datenbank-Statement auf Deiner injixo-Datenbank aus, um den Admin freizuschalten: `update sm_user set bad_logon = 0 where sm_user_id = 2;`

## Admin-Passwort vergessen

Wenn Du das Passwort für den einzigen Admin-Benutzer (ID 2) vergessen hast und kein weiterer Benutzer der Gruppe *System* (*Administrator*) existiert, kannst Du nur alle Kennwörter in der Datenbank zurückzusetzen.

1. Führe folgendes Statement auf der iWFM Datenbank aus:
`update sm_user set passwd = 'invision';`
2. Lösche die `esystem(64).**dat**` Datei im Server-Verzeichnis.
3. Starte den *InVision Enterprise WFM* Dienst neu.

Die Datei `esystem(64).dat` wird beim Server-Neustart neu erzeugt. Die Datei enthält den Schlüssel für die Kennwörter, die in der Datenbank verschlüsselt sind.

> In diesem Fall muss jeder Benutzer muss nachfolgend sein Passwort ändern.
