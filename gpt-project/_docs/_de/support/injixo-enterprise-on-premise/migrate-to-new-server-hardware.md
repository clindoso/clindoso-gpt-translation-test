---
title: Auf neue Server-Hardware migrieren
description: Aktualisiere die Enterprise Server Version, wenn du durch Betriebssystem-Updates auf neue Server-Hardware migrieren musst.
product_label:
  - on-premise
promote-service: general
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: support/injixo-enterprise-on-premise/unicode-migration.md
redirect_from: /de/migration-invision-wfm-server-auf-neue-hardware/
redirect_reason: Renamed article in April 2023
---

Ein Betriebssystem-Update erfordert meist einen Umzug auf einen neuen Server. Ggf. ändert sich auch die aktuelle IP-Adresse. 

Diese Anleitung beschreibt die notwendigen Schritte, um injixo Enterprise on-premise zu migrieren.

Ab Version 9159 findest Du die Build-Nummer nach dem Login oben rechts. In älteren Versionen prüfe eine Datei im Installationsverzeichnis auf dem Server in der Datei version.yaml.


> Führe alle Schritte der Reihenfolge nach aus.

<!-- Versionen älter 2012.3 benötigen einen neuen Lizenz-Schlüssel -->
<!-- Versionen älter 2011.4 benötigen zusätzliche Skripte für das Update der Datenbank. -->

<!-- hardware requirements -->
<!-- copied from deleted file support/injixo-enterprise-on-premise/systemanforderungen.md -->
<!-- ### Datenbank-Server

Microsoft SQL Server (Encoding: UTF-16), Oracle (Encoding: UTF-16, NLS_NCHAR_CHARACTERSET `AL16UTF16`) und PostgreSQL (Encoding: UTF-8) sind die unterstützten Datenbank-Systeme. Verwende mindestens einen Tablespace von 4 GB. Nutze einen separaten oder vorhandenen Datenbank-Server. Achte auf die Auslastung des Servers und den verfügbaren Speicherplatz.

## Hardware

Verwende aktuelle Hardware mit mindestens 8 Gigabyte Arbeitsspeicher und mehreren Prozessoren/Kernen, ausreichend Festplattenplatz für Installationsdateien und Logdateien. Die Virtualisierung des Servers ist möglich. Clients  Clients benötigen aktuelle PCs. injixo lädt nur notwendige Daten in den Speicher. Die Anbindung zum Server sollte ca. 0.5 - 1 MBit betragen. -->

## Voraussetzungen 

Diese Anleitung ist für Versionen größer 9001. Prüfe dein aktuelles Installationsverzeichnis und die Datenbank:

- Du hast nur Datei serinf.txt (und keine version.yaml) im Server-Verzeichnis?
- Es gibt nur die Datei ies64.exe (und keine ies.exe) im Server-Verzeichnis?
- Das Verzeichnis “server\custom” enthält nur den Unterordner "modulation" und zwei saferun\*.rb Dateien?
- Das Ergebnis des folgenden Datenbank-Statements zeigt UTF-8 oder UTF-16?
   `SELECT encoding FROM vs_version;`
- Das Ergebnis des folgenden Datenbank-Statements zeigt 20122001 oder 20130001?  
   `SELECT vs_version_no FROM vs_version;`

> Ist eine der Antworten **Nein**, [erstelle ein Ticket](https://www.injixo.com/support/ticket) mit deiner aktuellen Version, damit wir beim Update unterstützen können.

## 1. Vorbereitung

- Lade den aktuellen [injixo Enterprise Server](https://downloads.injixo.com/en#server-on-premise) herunter.
- Wenn du eine Oracle-Datenbank nutzt, lade einen einen 64-bit Datenbank-Client von der Herstellerseite herunter und installiere diesen auf dem neuen Server.
- Installiere das [Microsoft Visual C++ 2010 Service Pack 1 Redistributable Package](https://www.microsoft.com/en-us/download/details.aspx?id=26999) (64-bit) auf dem neuen Server. 

Ist das VCRedist-Paket nicht installiert, zeigt die Logdatei des Servers (ies64.log) eine Fehlermeldung mit Bezug auf die Datei msvcr100.dll.

## 2. Neues Installationsverzeichnis erstellen

- Erstelle auf dem neuen Server einen neues Installationsverzeichnis, z.&nbsp;B. d:\injixo Enterprise WFM\server.

## 3. Aktuelle Version installieren

- Entpacke das heruntergeladene Archiv ins neue Installationsverzeichnis.

## 4. Aktuelle Konfiguration kopieren

Das Standard-Installationsverzeichnis ist C:\Programme\injixo Enterprise\WFM\Server. Der Pfad oder das Laufwerk können abweichen. Um das richtige Installationsverzeichnis zu finden, prüfe in den Eigenschaften des Dienstes für den Enterprise Server (injixo Enterprise WFM oder InVision Enterprise WFM) auf dem Tab Allgemein den **Pfad zur EXE-Datei**.

- Kopiere folgende Dateien aus dem Installationsverzeichnis vom alten Server ins neue Installationsverzeichnis auf dem neuen Server:
    - isps.cfg
    - license.cfg
    - isps_r4.cfg (oder isps_r464.cfg)
    - esystem.dat (oder esystem64.dat)

## 5. Server-Adresse aktualisieren

Wenn sich die Server-Adresse ändert, musst Du die Datei isps.cfg ändern:

| Abschnitt               | Parameter | Beispiel                   |
| ----------------------- | --------- | -------------------------- |
| [IES System local]      | URL       | iwfm(s)://servername:45054 |
| [InVision JobProcessor] | URL       | iwfm(s)://servername:45054 |

Du kannst einen DNS-Namen oder eine IP-Adresse verwenden.

Hinweis: Sonderentwicklungen wie kundenspezifische Skripte (ggf. auf anderen Servern) benötigen die neue Server-Adresse. Suche daher auch in weiteren Konfigurationsdateien mit der Endung .cfg, .conf oder .config. Erstelle auch eventuell vorhandene geplante Tasks zur Steuerung der Sonderentwicklungen auf dem  neuen Server.

## 6. Dienste stoppen

1. Stoppe die Windows-Dienste auf dem alten Server.

   Hinweis: Dienste können anders benannt sein. Eventuell gibt es sogar mehrere Server mit verschiedenen Diensten. Nicht alle der folgenden Dienste müssen installiert sein:

   - InVision (oder injixo) Enterprise WFM
   - InVision Enterprise Server
   - InVision (oder injixo) HTTP server
   - InVision (oder injixo) JobProcessor
   - InVision (oder injixo) RulesEngine
   - InVision Enterprise WFM AutoScheduler
   - ISPS Xlink<br><br>

   Hinweis: Prüfe ggf. die isps_r464.cfg im Server-Verzeichnis. Die Datei zeigt, welche Prozesse vom InVision Enterprise WFM Dienst gesteuert werden. Standardmäßig der Enterprise Server (ies64.exe), HTTP Server (ihs.exe), sowie JobProcessor (iWFM_ijp.exe) und RulesEngine (iWFM_rul.exe).

2. Um eine erneute Verbindung zur Produktiv-Datenbank zu verhindern, ändere den Starttyp der gestoppten Dienste (von Automatisch) auf Manuell.

## 7. Neue Dienste installieren

1.  Öffne auf dem neuen Server eine Windows-Kommandozeile als Administrator und wechsele ins neue Installationsverzeichnis.
2.  Installiere mit dem Service Manager (nssm.exe) die gleichen Dienste, die du auf dem alten Server gestoppt hast.

    <!-- - War der Dienstname auf dem alten Server *InVision Enterprise WFM* und enthielt der Pfad die Datei isps_r464.exe? Installiere den Dienst wie folgt:
      `isps_r464.exe –install –name “injixo Enterprise WFM” –fullname “injixo Enterprise WFM”` -->

    - `nssm.exe install "injixo Enterprise Server" ies64.exe`
    - `nssm.exe install "injixo HTTP Server" ihs.exe  DependOnService "injixo Enterprise Server"` 
    - `nssm.exe install "injixo JobProcessor" iwfm_jps.exe  DependOnService "injixo Enterprise Server"`
    - `nssm.exe install "injixo RulesEngine" iwfm_rul.exe  DependOnService "injixo Enterprise Server"` (Optional, nur notwendig für die Funktionalität Zeitwirtschaft)

      Hinweis: Die Befehle oberhalb installieren die Dienste. Die DependOnService Option startet einen Dienst, wenn der "injixo Enterprise Server" gestartet ist und stoppt den Dienst, wenn der "injixo Enterprise Server" gestoppt wurde.
      
      Installiere ggf. weitere, auf dem alten Server vorhandene Dienste, z.&nbsp;B. Sonderentwicklungen, die oberhalb nicht aufgeführt sind. Prüfe ggf. deine Dokumentation oder nimm Kontakt mit uns auf. Bei Fragen, [erstelle ein Ticket](https://www.injixo.com/support/ticket).

3.  (Optional) Wenn der AutoScheduler vorher als Dienst installiert war, installiere den Dienst wie folgt:

    `isps_as64.exe --install`

4.  Starte die installierten Dienste. 

Die Meldung "Startup complete" in der Logdatei des Enterprise Servers (ies64.log) zeigt, dass der Enterprise Server gestartet ist.

Bei Fehlermeldungen in der Logdatei des Enterprise Servers (ies64.log), behebe die Ursache des Problems und starte den Dienst neu. Bei Problemen, [erstelle ein Ticket](https://www.injixo.com/support/ticket).
     
> Die neue Server-Adresse ändert die URL für den Planer-Login. 
>  
> Benutzer müssen die neue URL nutzen und vorhandene Lesezeichen im Browser aktualisieren.

Teste den Login im Browser. Prüfe auch die anderen Funktionen der Planung, sowie den Datenimport.

## 8. Xlink aktualisieren und Serveradresse ändern

Migriere Xlink wie folgt auf den neuen Server: 

1. Kopiere das Xlink-Installationsverzeichnis vom alten Server.
2. (Optional) Um Xlink zu aktualisieren, lade die aktuelle Xlink-Version von [downloads.injixo.com](https://downloads.injixo.com) herunter. 
3. Entpacke das Archiv in ein Verzeichnis deiner Wahl. Folge den Anweisungen im Artikel {% link_new Update der Xlink-Installation | support/faq/xlink-update.md %}.
4. Hat sich die Server-Adresse geändert, ändere die Xlink-Konfiguration im Client- oder Xlink-Verzeichnis (standardmäßig im Verzeichnis Programme(x86)):

   | Datei    | Abschnitt        | Parameter | Beispiel                   |
   | -------- | ---------------- | --------- | -------------------------- |
   | isps.cfg | [IES System WFM] | URL       | iwfm(s)://servername:45054 |

5. Wenn sich deine Xlink-Schnittstellen mit einer Datenbank verbinden, musst du auf dem neuen Server eine ODBC-Verbindung erstellen.  
   Erstelle die benötigte ODBC-Verbindung mit dem gleichen Namen wie auf dem alten Server. Die neue ODBC-Verbindung benötigt ggf. zusätzliche ODBC-Treiber.
6. Installiere den Xlink-Dienst auf dem neuen Server mit dem Befehl:
   `isps_uls.exe -install`

## 9. (Optional) Clients aktualisieren

Planer und Administratoren benötigen den injixo Client ([Download](https://downloads.injixo.com/en#client-components)). Der MSI-Installer registriert ActiveX-Komponenten automatisch. Clients mit Versionen größer oder gleich Version 2012.2 (siehe cliinf.txt Datei im Client-Verzeichnis) können sich am aktuellen Server anmelden. Neue Clients enthalten Verbesserungen ([Client Release Notes](https://downloads.injixo.com/release-notes/client.html)). Client-Versionen > 10995 ändern das Schicht Center in eine Windows-App, um Probleme beim Kopieren und Einfügen in Microsoft Edge zu verhindern.

Du kannst den Client lokal auf jedem Computer oder zentral, z.&nbsp;B. auf einem Terminal-Server, installieren. Füge den Einträgen in der `regdll.bat` ggf. den UNC-Pfad oder den Buchstaben des Netzlaufwerks hinzu. Die Registrierung muss im lokalen Benutzerkontext erfolgen. Führe die Datei `register.bat` ggf. manuell aus.


