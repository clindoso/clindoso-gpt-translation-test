---
title: Update der Xlink-Installation
product_label:
  - on-premise
redirect_from:
  - support/xlink/xlink-frequent-questions/
  - support/xlink/xlink-update-instruction/
  - /de/xlink-acd-system-update/
toc: false
---

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

Von Zeit zu Zeit stellen wir Updates für den Xlink zur Verfügung. Prüfe regelmäßig, ob Dein Xlink aktualisiert werden muss, um von Fehlerbehebungen und Verbesserungen zu profitieren.

## Aktuell installierte Xlink-Version prüfen

Es gibt zwei Optionen, um die aktuell installierte Xlink-Version herauszufinden:

- Öffne die Datei **version.txt**.
- Klicke mit der rechten Maustaste auf die Datei **isps_ul.exe** und wähle **Eigenschaften**. Klicke auf den Tab **Details**.

Die neueste Versionsnummer findest Du auf der [Downloadseite](https://downloads.injixo.com/de#xlink-software-dokumentation).

## Initiale Hinweise

Die Windows-Dienste öffnest Du wie folgt:

1. Öffne das Windows-Startmenü.
2. Tippe `services.msc` ein (je nach Windows-Version in das Suchfeld).
3. Bestätige Deine Eingabe mit der `Enter`-Taste.

Eine Kommandozeile öffnest Du wie folgt:

1. Öffne das Windows-Startmenü.
2. Tippe `cmd` ein (je nach Windows-Version in das Suchfeld).
3. Wähle nach einem Rechtsklick auf die Datei _Als Administrator ausführen_{:.doc-button}.

## Erforderliche Schritte

1. Sichere die folgende Konfigurationsdateien aus Deiner aktuellen Xlink-Installation:

   - isps.cfg
   - isps_ul.ini
   - isps_ulx.ini (wenn vorhanden)
   - acd_map.ini
   - alle \*.bas Dateien

2. Lade die _Xlink Suite_ von [downloads.injixo.com](https://downloads.injixo.com) herunter und entpacke das Zip-Archiv.

3. Stoppe den Dienst `ISPS Xlink`.

4. Überschreibe Deine aktuelle Installation mit den Dateien aus dem Unterordner `xlink`.

5. Öffne die Windows-Dienste. Führe einen Rechtsklick auf den `ISPS Xlink` Dienst aus und wähle _Eigenschaften_. Prüfe auf dem Tab _Anmeldung_{:.menu-item} bzw. _Logon_{:.menu-item}, ob der Dienst mit dem lokalen Systemkonto oder mit einem speziellen Benutzer/Service-Account konfiguriert ist. Dieses Benutzerkonto geht bei der Deinstallation verloren und muss bei der Neuinstallation des Dienstes wieder eingetragen werden.

   {{ 1 | image: 'Windows Services', '50%' }}

6. Schließe das Fenster mit den Windows-Diensten wieder.

7. Entferne den Dienst in der Kommandozeile mit dem Befehl `sc delete "ISPS Xlink"`.

8. Kopiere nun die in Punkt 1 gesicherten Dateien zurück in den bestehenden Ordner `xlink`, überschreibe ggf. existierende Dateien.

9. Führe nun in der Kommandozeile den Befehl `register.exe ixculcmm.dll /SYSTEM` aus.

   Als Rückmeldung erhältst Du folgende Ausgabe:
   `ixculcmm.dll registered SYSTEM GLOBAL`

   Wenn die Fehlermeldung `Open file failed, rc=5 Error[5]:Access is denied.` erscheint, entferne den Schreibschutz von der Datei `ixculcmm.dll` und schließe die Xlink-Applikation `isps_ul.exe`.

   Die Fehlermeldung `Open file failed, rc=32 Error [32]: The process cannot access the file because it is being used by another process. `
   bedeutet, dass eines der genannten Fenster noch offen ist oder dass Du einfach noch einen kurzen Moment warten musst, um den Befehl erfolgreich ausführen zu können.

10. Installiere den Xlink-Dienst wieder mit dem Befehl `isps_uls.exe -install`.

    Der Dienst wird installiert und automatisch gestartet. Der Xlink steht wieder für Importe zur Verfügung, die Aktualisierung ist abgeschlossen.
