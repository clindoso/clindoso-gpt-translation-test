---
title: Xlink installieren und konfigurieren
redirect_from:
  - /de/xlink-installation-konfiguration/
description: Erfahre, wie Du Xlink für den Datenimport installierst und konfigurierst.
product_label:
  - on-premise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/system-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-configuration-import-csv.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-configuration-import-odbc.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-log-files.md
  - overwrite_title: Add title for untranslated source
    filepath: support/faq/xlink-frequent-error-messages.md
---

In diesem Artikel lernst Du:

- wie Du einen Xlink-User erstellst.
- wie Du Xlink installierst.
- wie Du die Verbindung zwischen Xlink und dem injixo-Host/Server konfigurierst.
- wie Du Xlink aktualisierst.

Du kannst Xlink verwenden, um Kontakt- oder Agentenstatus-Daten in On-Premise-Installationen und Cloud-Tenants zu importieren.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>
## Voraussetzungen

Xlink benötigt eine Firewall-Ausnahme. Xlink verwendet TCP/IP-Port 45054 für ausgehende Verbindungen zur Cloud. Vor 2019 erstellte Tenants verwenden Port 80. In On-Premise-Installationen ist der Port 45054 voreingestellt. Den Port kannst Du auf dem Server in der Datei isps.cfg mit dem Parameter _IESPort_ konfigurieren.

Um Xlink zu installieren, benötigst Du Windows-Administratorrechte auf dem Computer, auf dem Xlink installiert werden soll.

1. Lade die [Xlink-Anwendung](https://downloads.injixo.com/de#xlink-software-dokumentation) herunter und entpacke das ZIP-Archiv.
2. Kopiere nur den Unterordner **Xlink** in ein beliebiges Verzeichnis, z. B. _C:\\Xlink_, auf dem Computer, auf dem Du Xlink installieren möchtest.

Hinweis: Wenn Du Xlink das erste Mal installierst, kopiere die Konfigurationsdateien **isps_Ul.ini**, **isps.cfg** und **acd_map.ini** aus dem Unterordner _sample-configurations_ in Dein Xlink-Installationsverzeichnis.

## Die Xlink-Verbindung konfigurieren

Um die Anmeldedaten und die Server-Verbindung zu konfigurieren, musst Du einen Benutzer anlegen und zwei Dateien bearbeiten. Sieh Dir abhängig von Deinem WFM-Plan die folgenden Kapitel an.

injixo Advanced und injixo Enterprise WFM:

- [Cloud: Xlink-Benutzer erstellen](#cloud-xlink-benutzer-erstellen)
- [Cloud: Anmeldedaten konfigurieren](#cloud-anmeldedaten-konfigurieren)
- [Cloud: Server-Verbindung konfigurieren](#cloud-server-verbindung-konfigurieren)

injixo Enterprise WFM On-Premise:

- [On-Premise: Xlink-Benutzer erstellen](#on-premise-xlink-benutzer-erstellen)
- [On-Premise: Anmeldedaten konfigurieren](#on-premise-anmeldedaten-konfigurieren)
- [On-Premise: Server-Verbindung konfigurieren](#on-premise-server-verbindung-konfigurieren)

### Cloud: Xlink-Benutzer erstellen

Um Xlink zu installieren, benötigst Du einen Benutzer mit _Admin_-Zugriff.

1. Melde Dich bei injixo an und gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Klicke auf _Neuer Benutzer_{:.doc-button}.
3. Gib eine **E-Mail-Adresse** für den Benutzer ein. Diese muss mit _xlink_ beginnen, z.B. _xlink@deinefirma.com_.
4. Gib einen beliebigen Text für **Vorname** und **Nachname** ein, z. B. _Xlink User_.
5. Aktiviere auf der rechten Seite die Checkbox **Admin-Zugriff gewähren**. Du brauchst keine weitere Rolle hinzuzufügen.
6. Klicke auf _Erstellen_{:.doc-button}.
7. Klicke in der Benutzer-Liste auf den **neuen Benutzer**.
8. Klicke auf _Neues Passwort setzen_{:.doc-button} und gib ein neues Passwort ein. Bewahre dieses Passwort sicher auf.
9. Klicke auf _Speichern_{:.doc-button}.

Xlink nutzt später den Benutzer und das Passwort, um sich mit dem Server zu verbinden.

### Cloud: Anmeldedaten konfigurieren

1. Öffne die Datei **Isps_Ul.ini** im Xlink-Installationsverzeichnis mit einem Texteditor.
2. Gehe zum Abschnitt _[DB]_.
3. Ersetze den Teil **xlink@xxxx.com** mit dem zuvor angelegten Benutzer _xlink@deinefirma.com_.
4. Öffne die Datei **Passcode.exe** im Ordner **support-applications**.
5. Gib im **oberen Feld** das _Passwort des Xlink-Benutzers_ ein.
6. Kopiere das verschlüsselte Passwort aus dem **unteren Feld** in die Zwischenablage für den nächsten Schritt und klicke _OK_{:.doc-button}.
   {{ 2 | image: 'Passcode.exe mit Text-Eingabe', '75%' }}

7. Ersetze die Zeichenkette _\<Passwort vom Generator\>_ (einschließlich < >) mit dem _verschlüsselten Passwort_ aus der Zwischenablage, das Du mit _Passcode.exe_ erstellt hast. Das Ergebnis sollte wie folgt aussehen:

   ```
   [DB]
   1=WFM,0,xlink@deinefirma.com,dein-verschlüsseltes-passwort
   ```

8. Speichere die Änderungen und schließe die **Datei** _isps_ul.ini_.

### Cloud: Server-Verbindung konfigurieren

1.  Öffne die Datei **isps.cfg** im Xlink-Installationsverzeichnis.
2.  Log Dich in injixo ein und klicke oben im Navigator auf **WFM**.
3.  Kopiere den hervorgehobenen Teil der Host-URL aus der URL in der Adresszeile des Browsers (https://**hostname**.injixo.com/iwfm/).
4.  Ersetze in der Datei **isps.cfg** den Teil **iwfm-xxxx** in der Zeile **URL = "iwfms://iwfm-xxxx.injixo.com:45054"** mit dem zuvor kopierten Host-URL-Teil. Das Ergebnis sollte wie folgt aussehen:

        ```
        [IES System WFM]
        Name                    = "WFM"
        Url                     = "iwfms://dein-hostname.injixo.com:45054"
        ```

5.  Speichere die Änderungen und schließe die **Datei** _isps.cfg_.

### On-Premise: Xlink-Benutzer erstellen

Um Xlink zu installieren, benötigst Du einen Benutzer, der zur Benutzergruppe _System_ gehört.

1. Melde Dich bei injixo an und gehe zu _Administration > System > Benutzerrechte_{:.breadcrumbs}.
2. Klicke auf das {% icon item-add %}, um einen neuen Benutzer anzulegen.
3. Gib _xlink_ als **Benutzernamen** ein und füge ein Passwort hinzu.
4. Klicke auf _OK_{:.doc-button}.
5. Klicke in der Benutzer-Liste auf den **neuen Benutzer**.
6. Klicke unter **Zugehörigkeit** auf das {% icon item-add %} und wähle **System**.
7. Klicke zweimal _OK_{:.doc-button}.

Xlink nutzt später den Benutzer und das Passwort, um sich mit dem Server zu verbinden.

### On-Premise: Anmeldedaten konfigurieren

1. Öffne die Datei **Isps_Ul.ini** im Xlink-Installationsverzeichnis mit einem Texteditor.
2. Gehe zum Abschnitt _[DB]_.
3. Ersetze den Teil _xlink@xxxx.com_ mit dem zuvor angelegten Benutzer _xlink_.
4. Öffne die Datei **Passcode.exe** im Ordner **support-applications**.
5. Gib im **oberen Feld** das _Passwort des Xlink-Benutzers_ ein.
6. Kopiere das verschlüsselte Passwort aus dem **unteren Feld** in die Zwischenablage für den nächsten Schritt und klicke _OK_{:.doc-button}.
   {{ 2 | image: 'Passcode.exe mit Text-Eingabe', '75%' }}

7. Ersetze die Zeichenkette _\<Passwort vom Generator\>_ (einschließlich < >) mit dem _verschlüsselten Passwort_ aus der Zwischenablage, das Du mit _Passcode.exe_ erstellt hast. Das Ergebnis sollte wie folgt aussehen:

   ```
   [DB]
   1=WFM,0,xlink,dein-verschlüsseltes-passwort
   ```

8. Speichere und schließe die **Datei** _isps_ul.ini_.

### On-Premise: Server-Verbindung konfigurieren

1. Öffne die Datei **isps.cfg** im Xlink-Installationsverzeichnis.
2. Ersetze in der Datei **isps.cfg** den Teil _iwfm-xxxx.injixo.com_ in der Zeile **URL = "iwfms://iwfm-xxxx.injixo.com:45054"** mit dem Servernamen oder der IP-Adresse Deines lokal installierten injixo-Servers.
3. Ändere den **vorhandenen Eintrag für das Protokoll** von _iwfms_ in _iwfm_, wenn Du **kein** SSL für den Enterprise Server konfiguriert hast (Standard).
4. Ändere den **vorhandenen Port-Eintrag** von 80 auf 45054 (Standard). Wenn in der Serverdatei _isps.cfg_ ein anderer Port konfiguriert ist, verwende diesen. Das Ergebnis sollte wie folgt aussehen (Standardport, kein SSL):

   ```
   [IES System WFM]
   Name                    = "WFM"
   Url                     = "iwfm://dein-servername:45054"
   ```

5. Speichere die Änderungen und schließe die **Datei** _isps.cfg_.

## Xlink-Windows-Dienst installieren

1. Öffne die **Windows-Kommandozeile** als Administrator.
2. Führe den Befehl _isps_uls.exe -install_, um den Windows-Dienst _ISPS Xlink_ zu installieren.

Du bekommst eine Meldung, wenn der ISPS Xlink-Dienst installiert und gestartet wurde.

## Die Server-Verbindung testen

Doppelklicke auf die Datei **isps_Ul.exe**, um die Xlink-Benutzeroberfläche zu öffnen.

Hinweis: Die Standardsprache der Xlink-Benutzeroberfläche ist Englisch. Optional kannst Du die Sprache ändern. Das Installationsverzeichnis enthält mehrere Sprach-Unterordner (z. B. _german_). Kopiere die zwei Dateien aus einem der Unterordner in das Installationsverzeichnis und überschreibe damit die vorhandenen Dateien.

Du siehst rechts einen Ordner-Symbol _WFM_. Klicke **+**, um die in injixo angelegten Queues anzuzeigen. Auf der linken Seite siehst Du die {% link_new externen Systeme | features/acd-integration/new-external-system.md %}, die Du erstellt hast. Es gibt verschiedene Arten von externen Systemen, die Du zusätzlich konfigurieren musst. Lerne mehr über {% link_new ODBC-Schnittstellen | features/acd-integration/xlink-configuration-import-odbc.md %} und die {% link_new CSV-Schnittstelle | features/acd-integration/xlink-configuration-import-csv.md %}.

{{ 1 | image: 'Xlink Benutzeroberfläche in Englisch', '75%' }}

<!-- also in frequent error messages, merge? -->
<!-- frequent error messages needs a rework -- could be an faq or frequent errors sections somewhere -->

## Die Datei ixculcmm.dll registrieren (für manuelle Importe)

Bleibt der Fortschrittsbalken der Xlink-Anwendung beim manuellen Import auf 0 % stehen, führe folgende Schritte durch:

1. Verschiebe die Datei **register.exe** aus dem Ordner **support-applications** in das Xlink-Installationsverzeichnis.
2. Öffne die **Windows-Kommandozeile** als Administrator.
3. Navigiere in Dein Xlink-Installationsverzeichnis.
4. Führe den Befehl _register.exe ixculcmm.dll /system_ aus.

Du bekommst die Erfolgsmeldung _ixculcmm.dll registered SYSTEM GLOBAL_.

Wenn Du eine Fehlermeldung siehst:

- entferne den Schreibschutz von der Datei **ixculcmm.dll**, indem Du mit der rechten Maustaste auf die Datei klickst. Wähle _Eigenschaften_ und entferne den Haken bei **Schreibgeschützt**.
- schließe das **Windows Dienste** Fenster.
- schließe die Xlink-Benutzeroberfläche **isps_Ul.exe**.

Führe erneut den Befehl zur Registrierung der Datei (aus Schritt 3 oben) aus.

> Möglicherweise musst Du diese Schritte nach einem Xlink-Update wiederholen.

<!-- duplicate content - move to linked file? -->

## Xlink aktualisieren

1. Lade die aktuelle Version der [Xlink-Applikation](https://downloads.injixo.com/de#xlink-software-dokumentation) herunter.
2. Stoppe den Dienst **ISPS Xlink**.
3. Erstelle eine **Sicherungskopie** Deines Xlink-Installationsverzeichnisses.
4. Kopiere die **neuen Dateien** in Dein Xlink-Installationsverzeichnis, überschreibe dabei die alten Dateien.
5. Starte den Dienst **ISPS Xlink** neu und kontrolliere die Logdatei **isps_uls.log**, um zu prüfen, dass Xlink eine Server-Verbindung herstellt.

Lerne mehr über die nötigen Befehle und mögliche Fehlermeldungen beim {% link_new Update der Xlink-Installation | support/faq/xlink-update.md %}.
