---
title: Umgang mit dem ReportServer
redirect_from:
  - /support-report-server/
---

Der ReportServer bietet injixo Enterprise WFM on-premise Kunden Zugriff auf WFM-bezogene Daten. Über verschiedene Endpunkte kannst Du Daten aus dem lokal installierten WFM System abrufen.

Die {% link_new Dokumentation zur injixo API | features/reporting/injixo-api/injixo-api.md %} enthält weitere nützliche, auf den Report-Server anwendbare, Informationen, obwohl sich einige Dinge wie die API-Referenz, Installation/Update und die Authentifizierung unterscheiden.

Die neue {% link_new injixo API | features/reporting/injixo-api/injixo-api.md %} ersetzt den ReportServer für Cloud Kunden. Unsere Empfehlung ist, eine bestehende ReportServer Installation zu ersetzen und die Abfragen und Reports zur injixo API zu migrieren.

## Installation

1. Lade die aktuelle Version unter [downloads.injixo.com](https://downloads.injixo.com) herunter.
2. Entpacke die Dateien in ein Verzeichnis Deiner Wahl.
3. Konfiguriere die `config.cfg` mit der IP oder dem Hostnamen Deines Systems.
4. Lege den Port fest.

Für ein Update tausche nur die Datei `ReportServer.exe` aus.

## ReportServer starten

Du hast zwei Optionen:

- Doppelklicke auf die Datei **reportserver.exe**, um den ReportServer in der Konsole zu starten.
- Installiere den ReportServer mithilfe der Datei nssm.exe als Windows-Dienst.
    1. Kopiere die Datei nssm.exe aus dem injixo-Installationsverzeichnis auf dem Server in das Installationsverzeichnis des ReportServers. Du kannst nssm auch [herunterladen](https://nssm.cc/download).
    2. Öffne eine Windows-Kommandozeile (cmd) als Administrator und wechsele in das ReportServer-Verzeichnis.
    3. Führe den folgenden Befehl aus: `nssm.exe install reportserver`. Lerne mehr auf der Webseite [nssm.cc](https://nssm.cc/usage).

Der ReportServer ist jetzt über `http://servername:port` erreichbar. Zur Vereinfachung zeigen nachfolgende Beispiele nicht diesen ersten URL-Teil.

### API Beschreibung

Die API-Beschreibung ist nach dem Start des ReportServers über folgenden Link erreichbar: `http://dein-report-server-dns-name:report-server-port/v1`

{{ 2 | image: 'ReportServer API Beschreibung', '75%' }}

Wenn Du einen Endpunkt auswählst, gelangst Du in einen Testmodus, mit verfügbaren Parametern und Rückgabewerten pro Endpunkt.

{{ 3 | image: 'ReportServer Endpoint Test Mode', '75%' }}

### Export Formate

Füge der URL nach dem Endpunkt eine Endung hinzu, um das Rückgabe-Format festzulegen, z.B. `/v1/activities.csv`. Ohne Angabe eines Formats, wird JSON zurückgegeben. Akzeptiert werden .csv, .xml oder .json.

### Parameter

Abfrage-Parameter können der URL hinzugefügt werden. Die verfügbaren Parameter pro Endpunkt findest Du in der API Dokumentation des ReportServers.

Nutze **?** für den ersten und **&** für jeden weiteren Parameter. Es gibt Pflichtparameter (Pfadparameter) und optionale Parameter (Abfrageparameter), diese erläutert die {% link_new injixo API Dokumenation | features/reporting/injixo-api/injixo-api.md %}.

## Anmeldung am ReportServer

**Für injixo Cloud** ist eine Anmeldung ausschließlich mit dem Xlink User (xlink@deinefirma.de) möglich. Es stehen mehrere Möglichkeiten zur Verfügung:

### Manuelle Eingabe der Benutzerdaten

Nachdem Du den Request versendet hast, erscheint eine Eingabe-Maske.

{{ 4 | image: 'ReportServer Login Seite', '75%' }}

### Abfrage-Parameter **usr** und **pwd**

Füge die Anmeldedaten der Abfrage als Parameter hinzu:

`/v1/activities.json?usr=DeinUSer&pwd=DeinPasswort`

### Abfrage-Parameter Auth

Der `auth` Parameter akzeptiert einen base64-kodierten String. Kodiere `DeinUser:DeinPassword` mit Hilfe eines Konverters, z.B. [base64.org](https://www.base64encode.org), in base64 und hinterlege es wie folgt in Deiner Abfrage:

`/v1/activities.json?auth=ZG9uYWxkX2R1Y2s6SV9sb3ZlX0RhaXN5IQ==`

> Hinweis
>
> Wenn Du Dich mit einem falschen Passwort einloggst oder Dein Benutzer gesperrt ist, wird keine Fehlermeldung angezeigt. Es erscheint erneut das Anmeldefenster.

## Benutzerrechte

Der Zugriff auf Daten ist abhängig von den Benutzerrechten. Solltest Du also nach erfolgreicher Anmeldung keine oder nicht die gewünschten Daten zurückerhalten, liegt dies entweder an einer falschen Abfrage oder an fehlenden Benutzerrechten für die abgefragten Daten. Wir empfehlen die Nutzung eines Admin Benutzers.

**Für injixo Cloud Kunden**: Der Xlink User (xlink@deinefirma.de) verfügt über alle Benutzerrechte.

## Weiterverarbeitung der Daten

Generierte CSV-Dateien können mit [q.exe](https://harelba.github.io/q), in Excel/Powerquery oder BI-Tools wie PowerBI, außerdem per HTTPClient abgeholt und in einer Programmiersprache Deiner Wahl weiterverarbeitet werden.

## Debug-Modus

Im Debug-Modus werden alle ausgeführten Anfragen mitgeschrieben, die Aktivierung ist einfach:

1. Schließe das ReportServer Konsolen Fenster oder beende den Dienst.
2. Füge in der `config.cfg` `debug: 1` in einer neuen Zeile ein.
3. Starte den ReportServer erneut.

Mit dem folgenden Befehl auf de Kommandozeile kannst Du alle Logausgaben in eine Datei mit dem Namen `debug.log` umleiten:

`ReportServer > debug.log`
