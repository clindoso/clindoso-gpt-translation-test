---
title: Lizenzdatei
product_label:
  - on-premise
redirect_from: /de/migration-invision-wfm-server-auf-neue-hardware/
redirect_reason: Renamed article in April 2023
---

Der injixo Enterprise Server startet nur mit einer gültigen Lizenzdatei. Die Lizenzdatei befindet sich im Installationsverzeichnis (standardmäßig `C:\Programme\InVision Enterprise WFM\Server`).

Startet der Server nicht, erscheint beim Login in der Benutzeroberfläche folgende Fehlermeldung: Der Enterprise Server konnte nicht gefunden werden. Wenden Sie sich an Ihren Systemadministrator. Nummer 256903-6

Die Logdatei des Servers (ies64.log) zeigt bei einer fehlenden, korrupten oder falsch benannten Lizenz folgende Meldung:

```
[09/Jun/2010T13:14:23:772] - Error - ESYSTEM - can't find valid licence.
[09/Jun/2010T13:14:23:772] - Warning - ESYSTEM - unable to activate.
```

## Lizenzdatei installieren oder aktualisieren

Der Erwerb zusätzlicher Lizenzen, der Ablauf der Gültigkeit einer Lizenzdatei oder ein Update von einer alten Version (2012.2 oder älter) sind Gründe dafür, warum du eine Lizenzdatei austauschen musst. Aktualisiere die Lizenzdatei wie folgt:

1. Sichere die alte Lizenzdatei, z.&nbsp;B. indem du diese in `license.cfg_OLD` umbenennst.
2. Benenne die neue Lizenzdatei in `license.cfg` um und kopiere die Datei ins Server-Verzeichnis.
3. Starte den Dienst **InVision Enterprise WFM** neu.
4. Logge dich ein. Prüfe ggf. die Logdatei ies64.log im Installationsverzeichnis.

> Der Enterprise Server erkennt die Lizenzdatei nur als `license.cfg`.

## Aktive Mitarbeiter prüfen

Du kannst die Anzahl der aktiven, d.&nbsp;h. zur Lizenz zählenden Mitarbeiter jederzeit mit dem Skript _Anzahl aktive Mitarbeiter_ prüfen:

1. [Öffne das Skript im Browser](https://downloads.injixo.com/_downloads/scripts/check-staffs-counting-to-licence.txt) (oder lade es herunter).
2. Kopiere den Skript-Text.
3. Gehe zu _Administration > Prognose > Skripts_{:.breadcrumbs} und erstelle ein neues Skript.
4. Füge den kopierten Inhalt als **Skript-Text** ein.
5. Klicke _Ok_{:.doc-button}.
6. Um das Skript zu starten, klicke _Ausführen_{:.doc-button}.
7. Wähle ein Datum, zu welchem du die aktiven Mitarbeiter prüfen möchtest.
8. Das Ergebnis zeigt Gültigkeitsdatum, Gültigkeitsdatum, den Lizenzumfang und die aktiven Mitarbeiter.

   {{ 1 | image: 'Lizenzgültigkeit', '90%' }}

## Aktive Mitarbeiter überschritten?

injixo zeigt eine Warnung, wenn du neue Mitarbeiter anlegst und die maximal lizenzierte Mitarbeiteranzahl bald erreicht ist.

injixo prüft einmal täglich, ob deine Mitarbeiteranzahl noch mit der Lizenz abgedeckt ist. Gibt es zu viele aktive Mitarbeiter, fährt der Server herunter und bricht danach jeden neuen Startvorgang ab. Die Logdatei `ies64.log` zeigt bei einer Lizenzüberschreitung folgende Meldung:

```
[[01/Sep/2016T06:56:56:957] - Warning - ESYSTEM - licence of 'StaffOption' is depleted - 171 entries found but licence limited to 170.
[01/Sep/2016T06:56:56:957] - Warning - ESYSTEM - unable to activate.
```

Um das Problem zu lösen und eine neue (temporäre) Lizenzerweiterung zu erhalten, [erstelle ein Ticket](https://www.injixo.com/support/ticket) mit deiner aktuellen Version. Aktualisiere deine Lizenz wie oben beschrieben. Verringere dann ggf. die Anzahl der aktiven Mitarbeiter, z.&nbsp;B. durch Setzen eines Austrittsdatums. Installiere danach ggf. wieder die Originaldatei.

## Gültigkeitszeitraum abgelaufen?

Lizenzen verfügen je nach Vertragsart über einen Gültigkeitszeitraum. Ist dieser abgelaufen, fährt sich der Server herunter und bricht auch jeden neuen Startvorgang ab. Die Logdatei `ies64.log` bei einer abgelaufenen Lizenz folgende Meldung:

```
[01/Jul/2014T04:06:43:262] - Error - ESYSTEM64 - licence for "Systemname" expired - contact or InVision Software Support Team for help
[01/Jul/2014T04:06:43:262] - Warning - ESYSTEM64 - unable to activate.
```

Öffne deine Lizenzdatei und prüfe die Gültigkeit (Zeile ValidFrom bzw. ValidTo).

> Die Lizenzdatei ist signiert und darf nicht geändert werden.
