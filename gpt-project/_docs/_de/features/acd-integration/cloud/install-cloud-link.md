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

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Was ist injixo Cloud Link?

injixo Cloud Link ist eine Client-Software und Teil des Setups von On-premise- und CSV-Integrationen. injixo Cloud Link importiert in regelmäßigen Abständen Daten in injixo. Du kannst injixo Cloud Link auch installieren, wenn du deine CSV-Integrationen konfigurierst, damit sie regelmäßig neue CSV-Dateien aus einem Ordner importieren.

Das Client-Installationsverzeichnis enthält:

- die ausführbare Datei injixo-cloud-link.
- eine oder mehrere Logdateien injixo-cloud-link.\*.log.
- die Konfigurationsdatei injixo-cloud-link.toml.
- einen Ordner licenses mit den Lizenzen der genutzten Open-Source-Bibliotheken.

## Voraussetzungen

- injixo Cloud Link läuft auf Windows 10 und höher sowie auf Windows Server 2016 und höher.
- Linux: Das unixODBC-Paket muss installiert sein.
- Firewall/Proxy: Port&nbsp;443 muss für ausgehenden Datenverkehr geöffnet sein. injixo Cloud Link verwendet TLS-Verschlüsselung mit TCP über Port&nbsp;443.

Hinweis: On-premise-Integrationen greifen auf ein lokales System zu, um Daten abzurufen, z.&nbsp;B. eine ACD oder ein CRM. Je nach Datenbanktyp musst du einen Datenbanktreiber installieren.

## injixo Cloud Link installieren

Wenn du eine {% link_new On-premise-Integration | features/acd-integration/cloud/add-on-premise-integration.md %}, eine {% link_new CSV-Integration | features/acd-integration/cloud/add-csv-integration.md %} oder eine {% link_new Datenbank-Integration | features/acd-integration/cloud/add-database-integration.md %} hinzufügst, findest du im Abschnitt **injixo Cloud Link** Links, um das Client-Installationsprogramm (für Windows) bzw. das Archiv (für Linux) herunterzuladen.

### Windows-Installation

Installiere den ersten Dienst mit dem Windows-Installationsprogramm:

1. Klicke auf **Herunterladen für Windows 64-bit** und führe das Installationsprogramm aus.
2. Klicke auf **Weiter**.
3. (Optional) Ändere das Installationsverzeichnis.
4. Klicke auf **Weiter** und anschließend auf **Installieren**.  
   Ein Konsolenfenster zeigt eine PIN an, die 5&nbsp;Minuten lang gültig ist.  
   Um [Cloud Link mit deiner Integration zu verbinden](#cloud-link-mit-deiner-integration-verbinden), folge den Anweisungen im Konsolenfenster.
5. Klicke im Installationsprogramm auf **Fertigstellen**.  
   Das Installationsprogramm erstellt den Windows-Dienst **injixo Cloud Link**.

### <a name="install-multiple-cloud-link-services-windows">Mehrere Windows-Dienste installieren

Du kannst bis zu acht weitere Dienste für separate Integrationen installieren. Um zu vermeiden, dass frühere Instanzen überschrieben werden, installiere sie in separaten Verzeichnissen.

Um einen zweiten Cloud-Link-Dienst unter Windows zu installieren, füge eine neue Integration hinzu und gehe wie folgt vor:

1. Klicke auf **Herunterladen für Windows 64-bit**.
2. Öffne eine Windows-Eingabeaufforderung (cmd).
3. Führe für die zweite Instanz folgenden Befehl aus:

   ```
   msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS=":instance.1"
   ```

   > Vergib eine höhere ID für die Instanz im Parameter TRANSFORMS, wenn du weitere Instanzen installieren möchtest.
   >
   > Beispielsweise ist für die dritte Instanz die ID `":instance.2"` erforderlich, für die vierte Instanz die ID `":instance.3"` und so weiter.

4. Folge den Anweisungen im Installationsvorgang.  
   Das Installationsprogramm schlägt ein neues Standardinstallationsverzeichnis vor, das die Instanz enthält, z.&nbsp;B. (Instance 1).  
   Tipp: Um zu identifizieren, zu welcher Integration die Installation gehört, kannst du Details zur ACD und zum Importtyp zum Standardinstallationsverzeichnis hinzufügen, z.&nbsp;B. (ACD - Agenten-Import).  
   Du siehst das neue Verzeichnis und einen neuen Windows-Dienst mit dem Namen injixo Cloud Link (Instanz {id}).

### Linux-Installation

Installiere den ersten Dienst wie im folgenden Beispiel beschrieben:

1. Klicke auf **Herunterladen für Linux 64-bit**.
2. Öffne ein Terminal.
3. Installiere den injixo Cloud Link-Dienst:  
   `sudo ./injixo-cloud-link service install`
4. Starte den installierten Dienst:  
   `sudo ./injixo-cloud-link service start`
5. Zeige eine PIN an:  
   `sudo ./injixo-cloud-link pin`  
   Ein Konsolenfenster zeigt eine PIN an, die 5&nbsp;Minuten lang gültig ist.  
   Um [Cloud Link mit deiner Integration zu verbinden](#cloud-link-mit-deiner-integration-verbinden), folge den Anweisungen im Konsolenfenster.

### <a name="install-multiple-cloud-link-services-linux">Mehrere Linux-Dienste installieren

Du kannst mehrere Dienste installieren, die separate Integrationen bedienen. Um zu vermeiden, dass frühere Dienste überschrieben werden, installiere sie in separaten Verzeichnissen.

Um weitere Dienste unter Linux zu installieren, füge eine neue Integration hinzu und gehe wie folgt vor:

1. Erstelle ein neues Verzeichnis und kopiere die Dateien aus dem ursprünglichen Installationsverzeichnis.
2. Öffne die Datei injixo-cloud-link.toml.
3. Passe den Wert für **name** im Abschnitt **[app]** an und verwende eine neue ID:

   ```
   [app]
   name = "com.injixo.cloud-link.instance.1"
   ```

4. Installiere den Dienst und starte ihn im neuen Verzeichnis wie oben beschrieben neu.

## Cloud Link mit deiner Integration verbinden

Die Cloud-Link-Installation zeigt die folgende Nachricht an, einschließlich einer PIN:

```
** Before you are able to run the client,
** link it to your injixo account:
**  1) Log in to injixo.com
**  2) Visit https://www.injixo.com/account/integrations
**  3) Select an integration you want to connect the client to
**  4) Enter your pin: 424242 (expires in 5 minutes)
```

1. Gehe in deinem Browser zurück zur Ansicht **Neue Integration hinzufügen**.
2. Gib im Abschnitt **injixo Cloud Link** deine PIN in das sechsstellige Eingabefeld **PIN, die während der Installation angezeigt wird** ein.
3. Klicke auf _Verbinden_{:.doc-button}.
   Cloud Link verbindet sich mit injixo. Fahre mit der Konfiguration deiner {% link_new On-premise-Integration | features/acd-integration/cloud/add-on-premise-integration.md %} bzw. deiner {% link_new CSV-Integration | features/acd-integration/cloud/add-csv-integration.md %} fort.

## Über einen Proxy-Server verbinden

Um eine Verbindung über einen Proxy-Server herzustellen, füge den Proxy-Hostnamen oder die IP-Adresse der Umgebungsvariable https_proxy hinzu:

- Windows: Füge die Umgebungsvariable zum Abschnitt **Systemvariablen** hinzu. Wenn Dienste nicht mit dem LocalSystem-Konto ausgeführt werden, konfiguriere eine Benutzervariable.
- Linux: Setze die Umgebungsvariable in /etc/environment oder in /etc/profile.d

Beispiel: `https_proxy=http://your.proxy.example`

Falls nötig, kannst du zur Authentifizierung die Portnummer (falls abweichend von Port&nbsp;80) und die Anmeldedaten des Benutzers hinzufügen:

Beispiel: `https_proxy=http://username:password@your.proxy.example:8080`

## Ziel-IP-Adressen für injixo teilen <!-- rethink the name -->

Damit injixo Cloud Link sich mit den injixo-Cloud-Servern verbinden kann, teile die folgenden URLs:

- injixo-\*.s3-eu-west-1.amazonaws.com
- www.injixo.com

Du kannst keine einzelnen IP-Adressen teilen. Deployment- und Update-Prozesse ändern regelmäßig die Server-IP-Adressen. Die Installation von injixo Cloud Link in der DMZ kann nützlich sein. Schlägt die Verbindung zum Server fehl, siehst du [Windows-Socket-Fehlermeldungen](https://docs.microsoft.com/en-us/windows/win32/winsock/windows-sockets-error-codes-2) in der Logdatei.

## Logging

injixo Cloud Link rotiert die Logdateien täglich und nach einem Neustart, allerdings ohne Logdateien zu löschen. Die aktuellen Logs befinden sich in injixo-cloud-link.log. Rotierte Logdateien enthalten das Rotationsdatum im Dateinamen. Um Logdateien zu löschen, musst du eine regelmäßige Löschung aufsetzen oder sie in regelmäßigen Abständen manuell löschen.

### Erweitertes Logging aktivieren

injixo Cloud Link unterstützt einen Verbose-Logging-Modus für Datenbank-Integrationen. Wenn das erweiterte Logging aktiviert ist, zeigt die Logdatei für jede Anfrage die Gesamtzahl der zurückgegebenen Zeilen und die ersten zehn Zeilen der Daten an.

Du kannst das erweiterte Logging wie folgt aktivieren:

1. Stoppe injixo Cloud Link.
2. Öffne im Installationsverzeichnis die Datei injixo-cloud-link.toml.
3. Setze im Abschnitt **[app]** den Wert für **verbose** auf true:

   ```
   [app]
   verbose = true
   ```

4. Speichere die Datei und starte injixo Cloud Link neu.

## Importordner konfigurieren

injixo Cloud Link lädt standardmäßig Dateien aus dem Installationsordner hoch. Für CSV-Integrationen kannst du wie folgt einen benutzerdefinierten Importordner konfigurieren:

1. Stoppe injixo Cloud Link.
2. Öffne im Installationsverzeichnis die Datei injixo-cloud-link.toml.
3. Setze im Abschnitt **[app]** den Wert für **importDirectory** auf deinen Importordner.
   - Verwende relative oder absolute Pfade.
   - Backslashes kannst du mit einem zweiten Backslash maskieren.
4. Speichere die Datei und starte injixo Cloud Link neu.

## Häufig gestellte Fragen

<style>
table th:first-of-type {
    width: 25%;
}
table th:nth-of-type(2) {
    width: 75%;
}
</style>

| Frage                                                                               | Antwort                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Wie bekomme ich eine neue PIN, wenn die alte abgelaufen ist?                        | Starte injixo Cloud Link neu. Gib die neue PIN aus der Logdatei in das sechsstellige Eingabefeld auf der Konfigurationsseite im Abschnitt **injixo Cloud Link** ein.                                                                                                                                                                                                                                                                                                                                                     |
| Wie kann ich injixo Cloud Link von meinem System löschen?                           | 1\. Führe entweder das injixo Cloud Link-Installationsprogramm erneut aus oder gehe zu _Programme > Programme und Funktionen_{:.breadcrumbs} in Windows.<br>2\. Klicke mit der rechten Maustaste auf den Eintrag **injixo Cloud Link** in der Liste und wähle **Deinstallieren** oder **Deinstallieren/Ändern**.<br>3\. Folge den Anweisungen auf dem Bildschirm.<br><br>Um weitere Instanzen zu deinstallieren, gehe zu _Programme > Programme und Features_{:.breadcrumbs} in Windows und folge den Schritten 2 und 3. |
| Wie kann ich injixo Cloud Link auf einem neuen Server nutzen?                       | 1\. Klicke rechts neben deiner Integration auf das {% icon pencil %}, um sie zu bearbeiten.<br>2\. Klicke auf **Neue Installation von injixo Cloud Link**.<br>3\. Lade injixo Cloud Link bei Bedarf erneut herunter und installiere die Software auf dem neuen Server.                                                                                                                                                                                                                                                   |
| Wie wechsle ich die Integration für eine bestehende injixo Cloud Link-Installation? | 1\. Gehe in das Installationsverzeichnis und kopiere die PIN aus der Logdatei.<br>2\. Lösche die bestehende Integration und erstelle eine neue Integration.<br>3\. Verbinde den laufenden injixo Cloud Link-Client mit der neuen Integration. Gib dazu während des Installationsvorgangs der Integration die PIN ein.                                                                                                                                                                                                    |
