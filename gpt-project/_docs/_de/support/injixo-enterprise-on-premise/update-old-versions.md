---
title: Server-Version aktualisieren
product_label:
  - on-premise
promote-service: general
---

Diese Anleitung beschreibt die Schritte, um deine injixo Enterprise WFM on-premise Version zu aktualisieren. 

Ab Version 9159 findest Du die Build-Nummer nach dem Login oben rechts. In älteren Versionen prüfe eine Datei im Installationsverzeichnis auf dem Server in der Datei version.yaml.

> Führe alle Schritte der Reihenfolge nach aus.

<!-- Versionen älter 2012.3 benötigen einen neuen Lizenz-Schlüssel -->
<!-- Versionen älter 2011.4 benötigen zusätzliche Skripte für das Update der Datenbank. -->
<!-- Versionsnummer in der Datei serinf.txt (Version/PaketNo.) im Server-Verzeichnis. -->

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

## 2. Dienste stoppen

- Stoppe die Windows-Dienste auf dem alten Server.  

   Hinweis: Dienste können anders benannt sein. Eventuell gibt es sogar mehrere Server mit verschiedenen Diensten. Nicht alle der folgenden Dienste müssen installiert sein:

   - InVision (oder injixo) Enterprise WFM
   - InVision Enterprise Server
   - InVision (oder injixo) HTTP server
   - InVision (oder injixo) JobProcessor
   - InVision (oder injixo) RulesEngine
   - InVision Enterprise WFM AutoScheduler
   - ISPS Xlink

## 3. Installationsverzeichnis sichern

Das Standard-Installationsverzeichnis ist C:\Programme\injixo Enterprise\WFM\Server. Der Pfad oder das Laufwerk können abweichen. Um das richtige Installationsverzeichnis zu finden, prüfe in den Eigenschaften des Dienstes für den Enterprise Server (injixo Enterprise WFM oder InVision Enterprise WFM) auf dem Tab Allgemein den **Pfad zur EXE-Datei**.

> Sichere das bestehende Installationsverzeichnis! 
> 
> Kopiere das Installationsverzeichnis in einen anderen Ordner außerhalb des aktuellen Verzeichnisses.

## 4. Inhalt des alten Installationsverzeichnisses löschen

Updates können neue Dateien (wie Kalendervorlagen) enthalten oder es werden alte Module entfernt.

- Lösche den gesamten Inhalt des ursprünglichen Installationsverzeichnisses.

## 5. Aktuelle Version installieren

- Entpacke das heruntergeladene Archiv ins neue Installationsverzeichnis.

## 6. Alte Konfiguration kopieren

Kopiere folgende Dateien aus der Sicherung des Installationsverzeichnisses ins Installationsverzeichnis:

- isps.cfg
- license.cfg
- isps_r4.cfg (oder isps_r464.cfg)
- esystem64.dat

## 7. Dienste neustarten und Abschluss des Updates

- Starte alle gestoppten Dienste wieder. 

Die Meldung "Startup complete" in der Logdatei des Enterprise Servers (ies64.log) zeigt, dass der Enterprise Server gestartet ist.

Bei Fehlermeldungen in der Logdatei des Enterprise Servers (ies64.log), behebe die Ursache des Problems und starte den Dienst neu. Bei Problemen, [erstelle ein Ticket](https://www.injixo.com/support/ticket).
     
Teste den Login im Browser. Prüfe auch die anderen Funktionen der Planung, sowie den Datenimport.

## 8. (Optional) Clients aktualisieren 

Planer und Administratoren benötigen den injixo Client ([Download](https://downloads.injixo.com/en#client-components)). Der MSI-Installer registriert ActiveX-Komponenten automatisch. Clients mit Versionen größer oder gleich Version 2012.2 (siehe cliinf.txt Datei im Client-Verzeichnis) können sich am aktuellen Server anmelden. Neue Clients enthalten Verbesserungen ([Client Release Notes](https://downloads.injixo.com/release-notes/client.html)). Client-Versionen > 10995 ändern das Schicht Center in eine Windows-App, um Probleme beim Kopieren und Einfügen in Microsoft Edge zu verhindern.

Du kannst den Client lokal auf jedem Computer oder zentral, z.&nbsp;B. auf einem Terminal-Server, installieren. Füge den Einträgen in der `regdll.bat` ggf. den UNC-Pfad oder den Buchstaben des Netzlaufwerks hinzu. Die Registrierung muss im lokalen Benutzerkontext erfolgen. Führe die Datei `register.bat` ggf. manuell aus.
## 9. (Optional) Xlink aktualisieren

Folge den Anweisungen im Artikel {% link_new Update der Xlink-Installation | support/faq/xlink-update.md %}.
