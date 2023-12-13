---
title: Häufige Fehlermeldungen
product_label:
  - on-premise
---

Hier haben wir die häufigsten Fehlermeldungen bzw. Probleme mit der Xlink-Applikation zusammengetragen und verweisen auf mögliche Lösungen.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

## Enterprise Server 1 not available

**Die Verbindung zwischen injixo und dem Xlink kann nicht korrekt hergestellt werden.**

Bitte prüfe die Zugangsdaten, die in der _DB_{:.menu-item} Sektion der `isps_ul.ini` Datei hinterlegt sind und ob in Deiner Firewall der `TCP Port 45054` (injixo Systeme, die vor 2019 angelegt wurden, nutzen Port 80) freigegeben ist. Zusätzlich prüfe bitte den Hostnamen, welcher in der `isps.cfg` im Xlink-Verzeichnis eingetragen ist. Dieser sollte der dem ersten Teil der URL entsprechen, die angezeigt wird, wenn Du dich im WFM-Teil von injixo befindest.

Nutzt Du injixo Enterprise On-Premise, stelle sicher, dass sich die IP-Adresse zum InVision-Enterprise-Server nicht geändert hat. Andernfalls musst Du diese in der `isps.cfg` anpassen.

## regsvr32 /s "\*.DLL" failed: 3

**Diese Fehlermeldung tritt auf, wenn das Microsoft Visual C++ 2005 SP1 redistributable Package (x86) nicht installiert ist. Der Xlink benötigt bestimmte Microsoft dll-Dateien, welche in dem Package enthalten sind.**

Der Xlink-Download enthält einen Ordner _Server Redistributable_, installiere die dort vorhandene MSI-Datei für das Microsoft Visual C++ 2005 SP1 Redistributable oder nutze den <a href="https://www.microsoft.com/en-gb/download/details.aspx?id=26347" target="_blank">Download von Microsoft.

## Verbindung zur Datenbank kann nicht hergestellt werden

**Die Zugangsdaten vom Xlink-User sind nicht korrekt.**

Gib Deinem Xlink-User in injixo unter _Account_{:.menu-item} ein neues Passwort. Achte darauf, ob neben dem User ein kleines Schloss abgebildet ist. In diesem Fall wurde der Xlink-User aufgrund zu vieler fehlerhafter Anmeldungen gesperrt und Du musst den Xlink-User entsperren.

Nutzt Du injixo Enterprise On-Premise, überprüfe, ob sich die IP-Adresse des Enterprise Servers geändert hat, die in der `isps.cfg` im Xlink hinterlegt ist. Ist das nicht der Fall, teste bitte, ob Du Dich mit dem Benutzer für den Xlink anmelden kannst. Ist das nicht der Fall, muss ein anderer Benutzer das Passwort für den Xlink-Benutzer zurücksetzen.

Hinterlege das neue Passwort als kodierten String (mittels `passcode.exe`) in der `isps_ul.ini` und starte den Xlink-Dienst einmal neu.

## Der Import funktioniert nicht mehr und das Log enthält keine Daten

**Die maximale Log File Größe ist erreicht.**

Durch die 32 bit-Architektur ist standardmäßig die Logfile-Größe im Xlink auf 4 GB begrenzt. Wenn diese Größe erreicht wird, kann das Logfile nicht mehr erweitert werden und der Xlink stoppt den Import. Sichere das `isps_ul.log` an einem anderen Speicherort und lösche dann die Datei aus dem Xlink-Verzeichnis. Zusätzlich kannst Du in der Konfigurationsdatei `isps_ul.ini` die Größe der Logdatei über den Parameter LogMaxFileSize anpassen: `LogMaxFileSize = 10000` (entspricht einer Größe von 10 MB)

## Der Fortschrittsbalken beim Import steht bei 0%, nachdem ein manueller Import gestartet wurde.

**Bei der Nutzung von Windows Terminal-Diensten, z.B. Server-Zugriff per `mstsc` muss die vom Xlink genutzt `ixculcmm.dll` global registriert werden.**

Verschiebe aus dem Ordner `support-applications` die Datei `register.exe` in den Xlink-Ordner. Anschließend öffnest Du die Windows-Kommandozeile und navigierst in Dein Xlink-Verzeichnis. Kopiere den folgenden Befehl:
`register.exe ixculcmm.dll /system`

Drücke die Enter-Taste zum Ausführen. Damit registrierst Du die Datei `ixculcmm.dll` auf Deinem Rechner. Nun sollte die folgende Meldung erscheinen:
`ixculcmm.dll registered SYSTEM GLOBAL`

Hinweis:
Gibt es statt der oberen Meldung eine Fehlermeldung, entferne den Schreibschutz von der Datei `ixculcmm.dll` (Rechtsklick auf die Datei > Eigenschaften > Haken bei “Schreibgeschützt” entfernen). Schließe zudem das Windows Dienste Fenster und die Xlink-Applikation `isps_Ul.exe`.
Warte kurz und führe den Schritt zur Registrierung mit “register.exe ixculcmm.dll /system” erneut aus.

## CSV Import verschiebt Dateien, importiert aber keine Daten

**Du hast den CSV-Import eingerichtet und beim Versuch die Daten zu importieren (manuell oder automatisch), werden die Daten nicht eingelesen. Die Konfiguration für die CSV-Datei stimmt nicht.**

Prüfe die Gruppennamen in der `isps_ul.ini`. Die Bezeichnungen müssen **identisch** zu den Angaben in Deiner CSV-Datei sein, d.h. case-sensitive. Das Mapping muss nach Änderung der Konfiguration angepasst und der Xlink-Dienst neugestartet werden.
