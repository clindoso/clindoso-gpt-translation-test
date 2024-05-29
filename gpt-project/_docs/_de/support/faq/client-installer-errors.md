---
title: Fehler bei der Client-Installation beheben
toc: false
description: Behebe Fehler, die bei der Ausführung des injixo MSI-Client-Installationsprogramms auftreten können.
product_label:
  - advanced
  - enterprise
  - classic
---

In diesem Artikel lernst Du, wie Du mit Problemen und Fehlermeldungen während der Client-Installation umgehst und diese behebst.

Ein häufiger Grund ist, dass der zuvor installierte Client nicht automatisch deregistriert werden kann.

{{ 1 | image: 'Fehlermeldung im Client Installer', '60%' }}

Dies kann passieren, wenn:

- das ursprüngliche Installationsverzeichnis bereits gelöscht wurde.
- wenn die Datei _unregister.bat_ fehlt.

Das Problem kann auch auftreten, wenn Du versuchst, das Client-Installationsprogramm auf demselben System auszuführen, auf dem die injixo Enterprise on-premise Software mit dem ursprünglichen Installer für Version r4.306 installiert wurde; dann versucht das Installationsprogramm zweimal, den Client zu deregistrieren. In diesem Fall hilft es _nicht_ die Datei _unregister.bat_ neu zu erstellen, starte direkt mit Lösung 3.

## Lösung 1: Verwende die Client-Installer-Reparaturfunktion

Versuche es zuerst über die Reparieren-Funktion des Installers. Diese Installer-Option ist verfügbar, wenn Du den Installer ein zweites Mal auf einem Computer ausführst, auf dem der Client bereits installiert ist. Fahre mit Lösung 2 fort, wenn das Reparieren nicht funktioniert oder diese Option erst gar nicht zur Verfügung steht.

## Lösung 2: Erstellen und Prüfen einer Debug-Logdatei

So erstellt Du eine Debug-Logdatei:

1. Führe den Client Installer mithilfe einer Eingabeaufforderung (CMD) über den Befehl `msiexec /i injixo_client.msi /le error.log` oder `msiexec /i injixo_client.msi /lv debug.log`aus, um ein Logfile zu erzeugen.

2. Aus dem erzeugten Logfile geht dann hervor, was nicht funktioniert.

   Enthält die Datei wie im Beispiel unterhalb _unregisterClient_, eine Fehlernummer `-- Error 1721` und einen Pfad wie `4: C:\Program Files (x86)\InVision WFM\Client\unregister.bat`, konnte die erwartete Datei `unregister.bat` nicht gefunden werden:<br><br>

   ```
     MSI (s) (B0:40) [14:08:31:233]: Note: 1: 1721 2: unregisterClient 3: C:\Program Files (x86)\InVision WFM\Client\ 4: C:\Program Files (x86)\InVision WFM\Client\unregister.bat
     MSI (s) (B0:40) [14:08:34:062]: Product: injixo Client -- Error 1721. There is a problem with this Windows Installer package. A program required for this install to complete could not be run. Contact your support personnel or package vendor. Action: unregisterClient, location: C:\Program Files (x86)\InVision WFM\Client\, command: C:\Program Files (x86)\InVision WFM\Client\unregister.bat
   ```

3. Erstelle in diesem Fall alle Ordner, für den in der Logdatei angezeigten Pfad zur Datei, manuell neu, und im neuen Client Ordner eine neue Datei `unregister.bat` mit dem Inhalt `echo 1`.

4. Führe den Installer erneut aus.

Fahre mit Lösung 3 fort, wenn dies nicht hilft oder Du nicht herausfinden kannst, wie das Problem anders zu lösen ist.

## Lösung 3: Windows-Registrierung bearbeiten

> Hinweis
>
> Das Löschen von Registrierungseinträgen ist der letzte Ausweg und kann zu Problemen mit dem Betriebssystem führen. Bitte erstelle ein Backup der Windows-Registry, bevor Du diesen Schritt ausführst.

Um den Schlüssel für den injixo Client aus der Windows Registrierung zu entfernen, gehe wie folgt vor.

1. Suche in der Windows-Registrierung (`Start > Ausführen > regedit`) nach folgendem Schlüssel:
   `HKEY_CURRENT_USER\Software\Microsoft\Installer\Products\1B19A99FB16314A459325F171A154DCE`
2. Lösche den gesamten Teil `1B19A99FB16314A459325F171A154DCE`.
3. Führe dann den Installer erneut aus.
