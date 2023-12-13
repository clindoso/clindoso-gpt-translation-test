---
title: injixo Cloud Link installieren
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Installiere den injixo Cloud Link Client, um Daten zu injixo zu importieren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

In diesem Artikel lernst du:

- wofür injixo Cloud Link verwendet wird.
- wie du den Dienst installierst.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Was ist injixo Cloud Link?

injixo Cloud Link ist eine Client-Software und Teil des Setups von On-Premise- und CSV-Integrationen.

Über einen Dienst importiert injixo Cloud Link in regelmäßigen Abständen Daten zu injixo.

Das Client-Installationsverzeichnis enthält:

- eine ausführbare Datei _injixo-cloud-link_.
- eine oder mehrere Logdateien _injixo-cloud-link.*.log_.
- eine Konfigurationsdatei _injixo-cloud-link.toml_.
- einen Ordner _licenses_ mit den Lizenzen der genutzten Open-Source-Bibliotheken.

## Voraussetzungen

- Der Client verwendet SSL-Verschlüsselung (TCP über Port 443). Stelle sicher, dass dieser Port für ausgehenden Datenverkehr geöffnet ist.
- Bei On-Premise-Integrationen muss injixo Cloud Link Zugriff auf das lokale System haben, von dem du Daten importieren möchtest, z.&nbsp;B. deine ACD, dein CRM, etc. Möglicherweise musst du dafür einen Datenbanktreiber installieren.

## injixo Cloud Link installieren

1. Füge eine {% link_new On-Premise-Integration | features/acd-integration/cloud/add-on-premise-integration.md %} oder eine {% link_new CSV-Integration | features/acd-integration/cloud/add-csv-integration.md %} hinzu.
2. Gib im Abschnitt **Allgemeine Informationen** einen **Namen** für die Integration ein.
3. Lade im Abschnitt **injixo Cloud Link** das Client-Installationsprogramm/-archiv für Windows oder Linux herunter.

   {{ 3 | image: 'Eingabefeld für den Integrationsnamen und Download-Links', '60%' }}

Um die Version und Anleitungen für eine Installation auf MacOS zu erhalten, wende dich an dein Customer-Success-Team.

Fahre mit der Installation je nach Betriebssystem fort.

### Windows-Installation

injixo Cloud Link läuft auf Windows 8 und höher sowie auf Windows Server 2012 und höher. Um eine 32-Bit-Version zu erhalten, wende dich an dein Customer-Success-Team. Das Installationsprogramm erstellt den Windows-Dienst injixo Cloud Link.

1. Klicke auf **Herunterladen für Windows 64-bit**.
2. Führe das Installationsprogramm aus. Ein Konsolenfenster zeigt eine PIN an.

Folge den Anweisungen im Konsolenfenster, um [Cloud Link mit deiner Integration zu verbinden](#cloud-link-mit-deiner-integration-verbinden).

### Linux-Installation

> Vergewissere dich, dass das unixODBC-Paket installiert ist.

1. Klicke auf **Herunterladen für Linux 64-bit**.
2. Extrahiere das Client-Archiv in deinem gewünschten Installationsordner.
3. Öffne ein Terminal.
4. Installiere den injixo Cloud Link-Dienst mit dem Befehl:  
   `sudo ./injixo-cloud-link service install`
5. Starte den installierten Dienst mit dem Befehl:  
   `sudo ./injixo-cloud-link service start`
6. Zeige eine PIN an mit dem Befehl:  
   `sudo ./injixo-cloud-link pin`

Folge den Anweisungen im Konsolenfenster, um [Cloud Link mit deiner Integration zu verbinden](#cloud-link-mit-deiner-integration-verbinden).

## Cloud Link mit deiner Integration verbinden

Während der Cloud Link-Installation wird eine PIN angezeigt:

```
** Before you are able to run the client,
** link it to your injixo account:
**  1) Log in to injixo.com
**  2) Visit https://www.injixo.com/account/integrations
**  3) Select an integration you want to connect the client to
**  4) Enter your pin: 424242 (expires in 5 minutes)
```

1. Gehe zurück zur Ansicht **Neue Integration hinzufügen**.
2. Gib im Abschnitt **injixo Cloud Link** deine PIN in das sechsstellige Eingabefeld ein.
   {{ 1 | image: 'Eingabefeld für die PIN', '60%' }}

3. Klicke auf _Verbinden_{:.doc-button}.
4. Fahre mit der Konfiguration deiner {% link_new On-Premise-Integration | features/acd-integration/cloud/add-on-premise-integration.md %} bzw. {% link_new CSV-Integration | features/acd-integration/cloud/add-csv-integration.md %} fort.

## Mehrere Instanzen von injixo Cloud Link installieren

Du kannst mehrere injixo Cloud Link-Dienste auf einem Computer installieren und ausführen. Jeder Dienst bedient eine separate Integration. Die Dienste können unabhängig gestartet und gestoppt werden.

### Windows-Dienste

Du kannst bis zu neun Instanzen auf Windows installieren.

1. Installiere den ersten Dienst, indem du das Installationsprogramm herunterlädst und startest. Folge den Anweisungen auf dem Bildschirm.
2. Um einen weiteren Dienst zu installieren, starte mit folgendem Befehl ein weiteres Installationsprogramm über die Windows-Eingabeaufforderung (_cmd_):

   ```
   msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS=":instance.1"
   ```

   Jede Installation muss ihren eigenen gültigen Wert für den Parameter TRANSFORMS verwenden:

   - `":instance.1"`
   - `":instance.2"`
   - etc.

   > Installiere jeden Dienst in einem eigenen Verzeichnis. Sonst wird der zuvor installierte Dienst überschrieben.

3. Folge den Anweisungen auf dem Bildschirm, um den neuen Dienst zu installieren.

Das Installationsprogramm erstellt den Windows-Dienst _injixo Cloud Link (Instance {id})_.

### Linux-Dienste

Installiere jeden Dienst in einem eigenen Verzeichnis. Cloud Link benötigt einen eindeutigen App-Namen, um eine interne Referenz im Betriebssystem zu erstellen. Wenn du das Client-Archiv im neuen Verzeichnis extrahiert hast, ändere den App-Namen in der Date _injixo-cloud-link.toml_:

1. Gib einen eindeutigen Namen für deinen neuen Dienst ein:

   ```
   [app]
   name = "com.injixo.cloud-link.instance.1"
   ```

2. Fahre mit dem [Installationsprozess](#linux-installation) fort.

## Über einen Proxy-Server verbinden

Um eine Verbindung über einen Proxy-Server herzustellen, konfiguriere in deinem Betriebssystem eine Umgebungsvariable **HTTPS_PROXY** (oder **https_proxy**).

Füge die Umgebungsvariable im Abschnitt **Systemvariablen** hinzu. Du kannst nur eine Benutzervariable verwenden, wenn du injixo Cloud Link mit einem anderen Benutzer als dem lokalen Systemkonto konfigurieren möchtest.

Der Wert der neuen Umgebungsvariable ist der Hostname oder die IP-Adresse des Proxys im URL-Format. Nutzt der Proxy einen anderen Port als 80, füge die Portnummer hinzu. Erwartet der Proxy eine Authentifizierung, füge Benutzer und Kennwort hinzu.

Beispiel (optionale Angaben in Klammern):

_https_proxy=http[s]://[username:password]@your.proxy.example[:8080]_

Gib folgende URLs im Proxy für automatische Aktualisierungen, PIN-Generierung und Datei-Uploads frei:

- _injixo-*.s3-eu-west-1.amazonaws.com_
- *www.injixo.com*

Hinweis: Eine einzelne IP-Adresse ist nicht möglich. Deployment- und Update-Prozesse ändern regelmäßig die IP-Adresse. Erwäge bei Bedarf eine injixo Cloud Link-Installation in der DMZ. Schlägt die Verbindung zur injixo Cloud fehl, erscheinen [Windows-Socket-Fehlermeldungen](https://docs.microsoft.com/en-us/windows/win32/winsock/windows-sockets-error-codes-2) in der Logdatei.

## Logging

### Rotation der Logdateien

injixo Cloud Link rotiert die Logdateien täglich und nach einem Neustart. Rotierte Logdateien enthalten das Rotationsdatum im Dateinamen, z.&nbsp;B. _injixo-cloud-link.2022-03-10.1.log_.
Die aktuellen Logs befinden sich in _injixo-cloud-link.log_.

injixo Cloud Link löscht keine Logdateien.

### Erweitertes Logging aktivieren

injixo Cloud Link verfügt über einen erweiterten Logging-Modus für Datenbank-Integrationen. Wenn der erweiterte Modus aktiviert ist, zeigt die Logdatei für jede Anfrage die Gesamtzahl der zurückgegebenen Zeilen und die ersten zehn Zeilen der Daten an.

Du kannst das erweiterte Logging wie folgt aktivieren:

1. Stoppe injixo Cloud Link.
   1. Öffne den Task Manager.
   2. Wechsle auf den Dienste-Tab und wähle **injixo Cloud Link**.
   3. Stoppe den **injixo Cloud Link-Dienst**, z.&nbsp;B. über das Kontextmenü.
2. Gehe in das Installationsverzeichnis.
3. Öffne die Datei _injixo-cloud-link.toml_. Wenn die Datei nicht vorhanden ist, erstelle sie im Installationsverzeichnis.
4. Setze **verbose = true** im Abschnitt **[app]** oder kopiere das folgende Beispiel.

   ```
   [app]
   verbose = true
   ```

5. Speichere die Datei.
6. Starte injixo Cloud Link neu.

## Ordner für Import konfigurieren

Bei CSV-Integrationen unterstützt injixo Cloud Link die Konfiguration eines Import-Ordners. injixo Cloud Link lädt standardmäßig Dateien aus dem Installationsordner hoch.

Konfiguriere den Import-Ordner wie folgt:

1. Stoppe injixo Cloud Link.
   1. Öffne den Task Manager.
   2. Wechsle auf den Dienste-Tab und wähle **injixo Cloud Link**.
   3. Stoppe den **injixo Cloud Link-Dienst**, z.&nbsp;B. über das Kontextmenü.
2. Gehe in das Installationsverzeichnis.
3. Öffne die Datei _injixo-cloud-link.toml_. Wenn die Datei nicht vorhanden ist, erstelle sie im Installationsverzeichnis.
4. Konfiguriere im Abschnitt **[app]** **importDirectory = <dein_import_ordner>**, z.&nbsp;B.:

   ```
   [app]
   importDirectory = "c:/dein_import_ordner"
   ```

   Du kannst auch einen relativen Pfad verwenden:

   ```
   [app]
   importDirectory = "../dein_import_ordner"
   ```

5. Speichere die Datei.
6. Starte injixo Cloud Link neu.

> Verwende einen einzelnen Schrägstrich (`/`) als Pfad-Separator auf allen Systemen.
> Falls Windows einen Backslash verlangt, umgehe dies mit einem weiteren Backslash `\\` z.&nbsp;B. `importDirectory = "c:\\dein_import_ordner"`.

## Häufig gestellte Fragen

<style>
table th:first-of-type {
    width: 25%;
}
table th:nth-of-type(2) {
    width: 75%;
}
</style>

| Frage                                                                        | Antwort                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Wie bekomme ich eine neue PIN, wenn die alte abgelaufen ist?                              | Starte injixo Cloud Link neu. Gib die neue PIN aus der Logdatei in das sechsstellige Eingabefeld auf der Konfigurationsseite im Abschnitt _injixo Cloud Link_ ein.                                                                                                                                                                                                                                                    |
| Wie kann ich injixo Cloud Link auf meinem System löschen?                                      | 1\. Führe entweder das injixo Cloud Link-Installationsprogramm erneut aus oder gehe zu _Programme > Programme und Funktionen_{:.breadcrumbs} in Windows.<br>2\. Klicke mit der rechten Maustaste auf den Eintrag **injixo Cloud Link** in der Liste und wähle **Deinstallieren** oder **Deinstallieren/Ändern**.<br>3\. Folge den Anweisungen auf dem Bildschirm.<br><br>Um weitere Instanzen zu deinstallieren, gehe zu _Programme > Programme und Features_{:.breadcrumbs} in Windows und folge den Schritten 2 und 3. |
| Wie kann ich injixo Cloud Link auf einem neuen Server nutzen?                                | 1\. Klicke auf das _![Bleistift-Symbol](/assets/img/common/pen-solid.svg)_{:.doc-button-icon} rechts neben deiner Integration, um sie zu bearbeiten.<br>2\. Klicke auf **Neue Installation von injixo Cloud Link**.<br>3\. Lade injixo Cloud Link bei Bedarf erneut herunter und installiere die Software auf dem neuen Server.                                                                                                                                                                        |
| Wie wechsle ich die Integration für eine bestehende injixo Cloud Link-Installation? | 1\. Gehe in das Installationsverzeichnis und kopiere die PIN aus der Logdatei.<br>2\. Lösche die bestehende Integration und erstelle eine **neue Integration**.<br>3\. Verbinde deinen laufenden injixo Cloud Link mit der neuen Integration, indem du bei der Konfiguration der Integration die PIN aus der Logdatei eingibst.                                                                                                    |
| Was passiert, wenn sich ein Queue-Name in einer CSV-Datei oder in deiner ACD ändert?              | Zwei Dinge können passieren, abhängig von der Integration. 1\. Wenn die Integration die ID der Queue kennt, wird der Name automatisch aktualisiert. 2\. Wenn die Integration nur den Namen kennt, wird eine neue Queue mit dem neuen Queue-Namen erstellt. In diesem Fall musst du die neue Queue zu deinem Workload in injixo Forecast hinzufügen. So stellst du sicher, dass die Daten, die dein Forecast braucht, auch in Zukunft zur Verfügung stehen.    |
