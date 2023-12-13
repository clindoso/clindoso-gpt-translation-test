---
title: Xlink auf neuem Server installieren
product_label:
  - on-premise
---

Wenn Du einen neuen Server aufsetzen oder Deinen Xlink auf einen anderen Server umziehen möchtest, brauchst Du hierfür keine vollständige Neuinstallation durchzuführen. Stattdessen kannst Du bereits bestehende Konfigurationsdateien sichern und als Grundlage für die Migration nutzen.

## Vorbereitende Schritte auf dem altem Server

### Abschaltung Xlink

1\.  Stoppe den `ISPS Xlink`-Dienst
    (Windows Startmenü > Über die Suchmaske `services.msc` aufrufen > `ISPS Xlink` Dienst auswählen und beenden).

2\.  Deinstalliere den `ISPS Xlink`-Dienst mit folgendem Befehl über die Kommandozeile: `sc delete ISPS Xlink`

  Starte die Kommandozeile wie folgt als Administrator:
  Windows Startmenü > Über Suchmaske nach `cmd` suchen > `cmd.exe` via Rechtsklick *Als Administrator ausführen*{:.doc-button}

### Sicherung Konfiguration und Mapping

3\. Sichere die folgenden, relevanten Konfigurationsdateien aus Deiner aktuellen Xlink-Installation:

  - `isps.cfg`
  - `isps_ul.ini`
  - `isps_ulx.ini` (optional)
  - `acd_map.ini`
  - alle `*.bas` Dateien

4\.  Kopiere diese auf den neuen Server.

## Vorbereitende Schritte auf dem neuen Server

### Portfreigabe in möglicher Firewall

Überprüfe, ob der vom Xlink genutzte TCP-Port in einer in vorhandenen Firewall freigegeben ist. Den Port findest Du innerhalb des Parameters URL in der gesicherten Datei `isps.cfg`, für injixo wird TCP-Port 45054 (injixo Systeme, die vor 2019 angelegt wurden, nutzen TCP-Port 80) genutzt.

### VCRedist 2005 SP 1 (x86) Installation

Prüfe, ob das benötigte `Microsoft Visual C++ 2005 SP1 Redistributable Package (x86)` auf dem neuen Server installiert ist.

Außerdem müssen bei der Nutzung des CSV-Imports entsprechende Zugriffsrechte auf die Importdateien vorliegen bzw. die Dateien müssen nun auf dem neuen Server abgelegt werden.
Bei Nutzung der universellen oder einer anderen ODBC-Schnittstelle muss die entsprechende ODBC-Verbindung (System-DSN) in %windir%\SysWOW64\odbcad32.exe angelegt werden.

## Installation der Xlink-Software

1. Lade die *Xlink Suite* von [downloads.injixo.com](https://downloads.injixo.com) herunter und entpacke das Zip-Archiv. Kopiere die Dateien aus dem Unterordner xlink in Deine aktuelle Installation und ersetze dabei vorhandene Dateien.

2.  Kopiere nun die gesicherten Dateien zurück in den bestehenden Ordner xlink, überschreibe ggf. existierende Dateien.

3.  Führe nun folgenden Befehl aus über die Kommandozeile aus `register.exe ixculcmm.dll /SYSTEM`

    Als Rückmeldung erhältst Du folgende Ausgabe:
    `ixculcmm.dll registered SYSTEM GLOBAL`

    Sollte die Fehlermeldung `Open file failed, rc=5 Error[5]:Access is denied.` erscheinen, prüfe und entferne den Schreibschutz von der Datei und schließe das Windows Dienste Fenster und die Xlink-Applikation `isps_ul.exe`. Die Fehlermeldung
    ```
    Open file failed, rc=32 Error [32]:
    The process cannot access the file because it is being used by another process.
    ```
    bedeutet, dass eines der oben genannten Fenster noch offen ist. In manchen Fällen hilft es auch kurz zu warten und den Befehl erneut auszuführen.

4. Installiere den Xlink-Dienst wieder mit dem Befehl `isps_uls.exe -install`
  Ausgabe in der Kommandozeile:
  ```
  ISPS Xlink installed.
  Starting up ISPS Xlink.
  ISPS Xlink started.
  ```

Der Xlink-Dienst wird automatisch gestartet und steht wieder für Importe zur Verfügung, die Migration auf den neuen Server ist abgeschlossen.
