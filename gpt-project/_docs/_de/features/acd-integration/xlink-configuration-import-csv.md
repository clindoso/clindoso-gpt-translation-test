---
title: CSV-Import
product_label:
  - on-premise
redirect_from:
  - /de/xlink-csv-parameter/
redirect_reason: file remove June 2020
---

Dieser Artikel beschreibt, wie Du eine CSV-Schnittstelle im Xlink einrichtest. Im Vorfeld solltest Du bereits erfolgreich den {% link_new Xlink installiert | features/acd-integration/xlink-installation-configuration.md %} und ein {% link_new externes System | features/acd-integration/new-external-system.md %} für CSV-Dateien angelegt haben. <!-- Richte eine entsprechende Integration in injixo für die Nutzung des injixo Forecasts. -->

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

## Datei-Format

Das Format Deiner CSV-Datei hängt davon ab, welche Daten Du importieren möchtest.

Für den Import von Anrufen, E-Mails, etc. (PhoneLink) benötigst Du in der CSV-Datei mindestens eine Spalte für

- den Namen der Quelle
- das Datum
- die Uhrzeit
- jeden zu importierenden Wert (z.B. je eine Spalte für eingehende Anrufe und AHT)

Die Spalten müssen in jeder Zeile vorhanden sein.

Um Agentenstatus-Daten wie Anmeldung, Abmeldung und Pausen zu importieren (TimeLink), benötigst Du in der CSV-Datei mindestens eine Spalte für

- die Aktivität
- den Agenten
- das Datum
- den Startzeitpunkt der Aktivität
- den Endzeitpunkt der Aktivität

Die Spalten müssen in jeder Zeile vorhanden sein.

Möglich ist auch die Angabe von Startzeitpunkt und Dauer oder nur einem Startzeitpunkt.
Alternativ kannst Du Datum und Uhrzeit für den Startzeitpunkt bzw. Endzeitpunkt auch in einem DateTime-Feld zusammenfassen.

## Unterstützte Zeit- und Datumsformate

Das Format der Uhrzeit erkennt die Schnittstelle automatisch.

Beispiele für erlaubte Formate:

- 9:50 AM, 12:00 PM, 01:34 AM
- 9:50:34 AM, 12:00:00 PM, 01:34:12 AM
- .5, 8.5, 12,7
- 08:48:00, 8:48:00
- 08:48, 8:48
- 084800, 84800
- 0848, 848

Das Format des Datums kann nicht vollautomatisch erkannt werden und erfordert die Konfiguration des Parameters _DateOrder_. Dieser legt die Reihenfolge von Tag, Monat und Jahr fest und wird in der Datei `isps_ul.ini` konfiguriert, in welcher das Datenformat der Quelldatei festgelegt wird. Mögliche Trennzeichen für das Datum sind `.`, `-` oder `/`.

Beispiele für erlaubte Formate (exemplarisch für Parameter _DateOrder_ mit Wert `mdy`):

- 02/09/2019, 02/09/19, 2/9/19, 2/9/2019, 020919, 02092019

Zusätzlich unterstützt werden DateTime-Zeitstempel in einem gemeinsamen Feld für Datum und Uhrzeit.

- 02/09/2019T01:08:40
- 02/09/2019T01:08:40Z
- 02/09/2019T01:08:40+00:00
- 02/09/2019 01:08:40
- 02/09/2019 01:08:40Z
- 02/09/2019 01:08:40+00:00

## Allgemeine Einstellungen

Die Schnittstelle bietet die Möglichkeit, einige wenige allgemeine Einstellungen für den CSV-Import über die Xlink-Oberfläche vorzunehmen.

Allgemeine Einstellungen für PhoneLink und TimeLink im Konfigurationsdialog der Schnittstelle:

{{ 1 | image: 'Konfiguration CSV Schnittstelle', '75%' }}

Gehe wie folgt vor:

1. Öffne die Datei `isps_ul.exe`.
2. Führe einen Rechtsklick auf das externe System aus. Wähle _Konfiguration_{:.menu-item}.
   Klicke alternativ auf _Einstellungen > ACD_{:.breadcrumbs} in der Symbolleiste.
3. Wähle mit _Daten - Verzeichnis_ den Ordner, in dem die CSV-Dateien abgelegt sind.
4. Hinterlege in _Zeitzone - UTC offset_ ggf. den Zeitversatz zwischen der Zeit in der CSV-Datei und der lokalen Zeit.
5. Definiere in _CSV Trennzeichen_ das verwendete CSV-Trennzeichen.
6. Aktiviere unter _Protokoll - Optionen_ ggf. das {% link_new Logging | features/acd-integration/xlink-log-files.md %}.
7. Klicke im Dialog auf _Ok_{:.doc-button}, um die Einstellungen zu speichern.

Nach dem Speichern werden die Werte in Parametern innerhalb der `isps_ul.ini` im Xlink-Verzeichnis gespeichert. Die folgende Tabelle erläutert diese Parameter:

| Parameter                  | Erläuterung                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source                     | Quellverzeichnis für PhoneLink auf dem Xlink Server selbst.                                                                                                                             |
| Destination                | Zielverzeichnis für PhoneLink. Wird nur genutzt, wenn DeleteImportFiles entsprechend konfiguriert ist.                                                                                  |
| SeparatorCharacter         | Trennzeichen für PhoneLink, Wert 2 für Komma, Wert 3 für Semikolon                                                                                                                      |
| DeleteImportFiles          | PhoneLink-Daten bleiben im Verzeichnis (Wert 0), werden verschoben (Wert 1) oder werden gelöscht (Wert 2). Aktionen für 1 und 2 werden in der Datei DeleteImportFiles.log festgehalten. |
| ActivitySource             | Quellverzeichnis für TimeLink auf dem Xlink Server selbst.                                                                                                                              |
| ActivityDestination        | PhoneLink-Zielverzeichnis. Wird nur genutzt, wenn DeleteActivityImportFiles entsprechend konfiguriert ist.                                                                              |
| ActivitySeparatorCharacter | Trennzeichen für TimeLink, Wert 2 für Komma, Wert 3 für Semikolon                                                                                                                       |
| DeleteActivityImportFiles  | TimeLink-Daten bleiben im Verzeichnis (Wert 0), werden verschoben (Wert 1) oder werden gelöscht (Wert 2). Aktionen für 1 und 2 werden in der Datei DeleteImportFiles.log festgehalten.  |
| TimeZone                   | Wert für den Zeitversatz, erlaubte Formate z.B. -2, 2, -3.5, 3.5, -08:00 oder 06:30                                                                                                     |
| Protocol                   | Protokollierung aktiviert (Wert 1 zeigt welche Werte gelesen werden) oder deaktiviert (Wert 0).                                                                                         |

## Import von Anruf-, E-Mail- und Chat-Daten

PhoneLink kann zählbare Daten wie Anrufe, E-Mails, Chats, Dokumente, usw. importieren. Die Schnittstelle erkennt das Format der CSV-Datei über zusätzliche Parameter.

### Erforderliche Parameter

| Parameter       | Erläuterung                                                                                                                                                                            |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HeaderLines     | Anzahl von Kopfzeilen, die nicht gelesen und importiert werden.                                                                                                                        |
| DateColumn      | Spaltenposition der Datum-Spalte, siehe auch TimeStampColumn.                                                                                                                          |
| TimeColumn      | Spaltenposition der Zeit-Spalte.                                                                                                                                                       |
| GroupColumn     | Spaltenposition des Channels/Queue-Namens/der Rufnummer.                                                                                                                               |
| Groups          | Alle in der Datei verfügbaren Queue-Namen, getrennt mit Semikolon.                                                                                                                     |
| ColumnNames     | Alle in der Datei verfügbaren Spalten, getrennt mit Semikolon, frei wählbar. Tip: Nutze die Kopfzeile, wenn verfügbar, z.B. Queue;Date;Time;CallsOffered;CallsHandled;AHT              |
| Interval        | Intervall in Minuten, in dem die ACD Daten zur Verfügung stellt, meist 15, 30 oder 60 Minuten                                                                                          |
| DateOrder       | Reihenfolge von Tag, Monat und Jahr im Datum oder im Datumsteil eines Zeitstempels, automatische Erkennung vorhandener Trennzeichen. Gültige Werte: dmy, mdy und ymd                   |
| AHTColumn       | Spaltenposition für die durchschnittliche Bearbeitungszeit (AHT). Ist dieser Wert nicht definiert, werden die Werte ohne Umrechnung als ganze Zahlen ohne Nachkommastellen importiert. |
| TimeStampColumn | Spaltenposition DateTime Zeitstempel. Überschreibt den Parameter DateColumn, wenn beides konfiguriert ist.                                                                             |

### Optionale Parameter

| Parameter      | Erläuterung                                                                                                                                                                   |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LogFile        | Zusatz für den Standard-Namen der Logdatei                                                                                                                                    |
| SubGroups      | Alle in der Datei verfügbaren Namen für Untergruppen. Notwendig, wenn zwei Spalten für den Namen in der CSV-Datei existieren, z.B. Standort und Queue. Getrennt mit Semikolon |
| SubGroupColumn | Spaltenposition der Untergruppe                                                                                                                                               |

### Erstellung Deiner Konfiguration

Nach dem Speichern der allgemeinen Einstellungen enthält die `isps_ul.ini` eine neue Sektion mit dem definierten Namen für das externe System, z.B. `[CSV]` oder `[Universal]`. Füge die Parameter unterhalb der bereits eingetragenen allgemeinen Parameter manuell hinzu. Die Eingabe erfolgt mit einem Gleichheitszeichen und einem Wert, z.B. `HeaderLines=1`.

Gehe am besten wie folgt vor:

1. Zähle die Spalten Deiner CSV-Datei, beginnend mit 1. Ermittle so die Spaltenpositionen für die Queue-Namen, das Datum und die Uhrzeit. Konfiguriere diese als _GroupColumn_, _DateColumn_ und _TimeColumn_. Bei Nutzung eines DateTime-Feldes, nutze _TimeStampColumn_.
2. Konfiguriere die Parameter _HeaderLines_, _ColumnNames_, _Groups_, _DateOrder_, _AHTColumn_ und _Interval_.
3. Speichere die Konfiguration ab.
4. Starte den `ISPS XLink` Dienst neu, damit die Änderungen wirksam werden.
5. Öffne noch einmal die Xlink-Oberfläche `isps_ul.exe`.

Auf der linken Seite der Benutzeroberfläche erscheint eine Baumstruktur. Diese wird aus den Gruppen und den konfigurierten Spaltenpositionen generiert. Du kannst nun das {% link_new Mapping | features/acd-integration/xlink-mapping-telephony.md %} erstellen, welches für den ersten Import notwendig ist.

## Import von Agentenstatus-Daten

TimeLink importiert Daten zu Agenten wie Anmeldungen und Abmeldungen, Aktivitäten und Pausen. Die Schnittstelle erkennt das Format der CSV-Datei über zusätzliche Parameter.

### Erforderliche Parameter

| Parameter                    | Erläuterung                                                                                                                                                                                                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ActivityIdentifiers          | In der Quelldatei vorkommende Aktivitäten-IDs, getrennt durch Semikolon.                                                                                                                                                                                        |
| ActivityDescriptions         | Anzeigenamen für die in ActivityIdentifiers definierten IDs, getrennt durch Semikolon                                                                                                                                                                           |
| ActivityHeaderLines          | Anzahl von Kopfzeilen, die nicht gelesen und importiert werden.                                                                                                                                                                                                 |
| ActivityTimeSpanType         | Der Import kann mit Startzeit und Dauer (Wert 0), Start- und Endzeit (Wert 1) oder nur mit der Startzeit (Wert 2) erfolgen. Im letzten Fall beendet die nächste Aktivität die vorhergehende. Bei Wert 0 wird der Parameter ActivityDurationColumn erforderlich. |
| ActivityColumn               | Spaltenposition Aktivitäten-ID                                                                                                                                                                                                                                  |
| AgentColumn                  | Spaltenposition Agenten-ID                                                                                                                                                                                                                                      |
| ActivityDateOrder            | Reihenfolge von Tag, Monat und Jahr im Datum oder im Datumsteil eines Zeitstempels. Eventuell vorhandene Trennzeichen wie ".", "-" oder "/" werden automatisch erkannt. Gültige Werte: dmy, mdy und ymd                                                         |
| ActivityStartDateColumn      | Spaltenposition Startdatum (bei getrennten Spalten für Datum und Zeit)                                                                                                                                                                                          |
| ActivityStartTimeColumn      | Spaltenposition Startzeit (bei getrennten Spalten für Datum und Zeit)                                                                                                                                                                                           |
| ActivityEndDateColumn        | Spaltenposition Enddatum (bei getrennten Spalten für Datum und Zeit)                                                                                                                                                                                            |
| ActivityEndTimeColumn        | Spaltenposition Endzeit (bei getrennten Spalten für Datum und Zeit)                                                                                                                                                                                             |
| ActivityStartTimeStampColumn | Spaltenposition Startzeit und Datum (bei gemeinsamem DateTime-Feld)                                                                                                                                                                                             |
| ActivityEndTimeStampColumn   | Spaltenposition Endzeit und Datum (bei gemeinsamem DateTime-Feld)                                                                                                                                                                                               |
| ActivityColumnNames          | Alle in der Datei verfügbaren Spalten, getrennt mit Semikolon, frei wählbar. Tip: Nutze die Kopfzeile, wenn verfügbar, z.B. AgentID;ActivityID;StartDate;StartTime;EndDate;EndTime;AHT                                                                          |

### Erstellung Deiner Konfiguration

Nach dem Speichern der allgemeinen Einstellungen, enthält die `isps_ul.ini` eine neue Sektion mit dem von Dir vergebenen Namen für das externe System , z.B. `[CSV]` oder `[Universal]`. Füge die Parameter unterhalb der bereits eingetragenen allgemeinen Parameter manuell hinzu. Die Eingabe erfolgt mit einem Gleichheitszeichen und einem Wert, z.B. `ActivityHeaderLines=1`.

Gehe am besten wie folgt vor:

1. Zähle die Spalten Deiner CSV-Datei, beginnend mit 1. Ermittle so die Spaltenpositionen für die Aktivität und die Agenten-ID. Konfiguriere diese als _ActivityColumn_ und _AgentColumn_.
2. Konfiguriere _ActivityStartDateColumn_ und _ActivityEndDateColumn_. Bei Nutzung eines DateTime-Feldes, nutze _ActivityStartTimeStampColumn_ und _ActivityEndTimeStampColumn_.
3. Konfiguriere _ActivityDateOrder_, _ActivityColumnNames_, _ActivityIdentifiers_ und _ActivityDescriptions_
4. Prüfe, ob in Deiner Datei eine Spalten für Startzeit und Endzeit, Startzeit und Dauer oder nur Startzeit vorhanden sind.
5. Konfiguriere entsprechend Punkt 4 _ActivityStartTimeColumn_, _ActivityEndTimeColumn_ und/oder _ActivityDurationColumn_. Bei Nutzung von DateTime-Feldern, nutze _ActivityStartTimeStampColumn_ bzw. _ActivityEndTimeStampColumn_.
6. Konfiguriere _ActivityTimeSpanType_.
7. Speichere die Konfiguration ab.
8. Starte den `ISPS XLink`-Dienst neu, damit die Änderungen wirksam werden.

Jetzt prüfe in _WFM > Administration > Scheduling > Aktivitäten_{:.breadcrumbs}, ob neue Zuweisungen für die Aktivität _Anwesend_ in der Kategorie _Externes Systems_ verfügbar sind.
Du kannst nun das {% link_new Mapping | features/acd-integration/xlink-mapping-activities.md %} erstellen, welches für den ersten Import notwendig ist.

## Beispiele

Nachfolgend einige Beispiele für CSV-Dateien und Konfigurationen. Diese zeigen die Daten in festen 15 Minuten Intervallen.

### Anrufdaten (PhoneLink)

```
Queue;Date;Time;CallsOffered;CallsHandled;AHT
UHD_DE_IN;23.12.2014;08:00;1;0;0
UHD_DE_IN;23.12.2014;08:15;1;1;180
UHD_EN_IN;23.12.2014;08:30;1;1;150
UHD_EN_IN;23.12.2014;08:45;1;1;160
```

> Vermeide den Import mehrerer Dateien, die dieselben Daten enthalten
>
> Enthält Deine Datei für jeden Anruf eine einzelne Zeile, z. B. für 08:00, 08:01, 08:05 und 08:14, werden diese Daten in das 08:00-Intervall geschrieben, da Xlink diese Rohdaten zu Intervallen aggregiert. Mehrere Dateien mit denselben Daten in einem einzigen Import führen zu ungewöhnlich hohen Intervallwerten. Um dies zu korrigieren, entferne die Duplikate oder importiere jeweils nur eine Datei, indem Du die Importdatei nach jedem Import mithilfe des Parameters _DeleteImportFiles_ verschiebst oder löschst.

```
GroupColumn=1
DateColumn=2
TimeColumn=3
SubGroupColumn=0
SubGroups =
HeaderLines=1
Interval=15
AHTColumn=6
ColumnNames=Queue;Date;Time;CallsOffered;CallsHandled;AHT
Groups=UHD_DE_IN;UHD_EN_IN;
DateOrder=dmy
```

### Agentendaten (TimeLink) mit DateTime-Feld

```
AgentID;ActivityID;StartDate;StartTime;EndDate;EndTime;AHT
1002;1;29/01/2014 08:00:00;29/01/2009 09:00:00;360
1006;2;29/01/2014 08:00:00;29/01/2009 09:00:00;370
1002;2;29/01/2014 09:00:00;29/01/2009 09:30:00;180
1006;1;29/01/2014 09:00:00;29/01/2009 10:00:00;210
```

```
ActivityHeaderLines=1
ActivityColumn=2
AgentColumn=1
ActivityStartTimeStampColumn=3
ActivityEndTimeStampColumn=4
ActivityTimeSpanType=1
ActivityIdentifiers=1;2
ActivityDescriptions=Aktivität_1;Aktivität_2
ActivityDateOrder=dmy
ActivityColumnNames=AgentID;ActivityID;StartDate;StartTime;EndDate;EndTime;AHT
```

### Agentendaten mit separatem Datum und Uhrzeit

```
AgentID;ActivityID;StartDate;StartTime;EndDate;EndTime;AHT
1002;1;29/01/2014;08:00:00;29/01/2009;09:00:00;360
1006;2;29/01/2014;08:00:00;29/01/2009;09:00:00;370
1002;2;29/01/2014;09:00:00;29/01/2009;09:30:00;180
1006;1;29/01/2014;09:00:00;29/01/2009;10:00:00;210
```

```
ActivityHeaderLines=1
ActivityColumn=2
AgentColumn=1
ActivityStartDateColumn=3
ActivityStartTimeColumn=4
ActivityEndDateColumn=5
ActivityEndTimeColumn=6
ActivityTimeSpanType=1
ActivityIdentifiers=1;2
ActivityDescriptions=Aktivität_1;Aktivität_2
ActivityDateOrder=dmy
ActivityColumnNames=AgentID;ActivityID;StartDate;StartTime;EndDate;EndTime;AHT
```

### Vorlage: Komplette Konfiguration

Zum Abschluss noch einmal die gesamte Konfiguration mit allen allgemeinen Einstellungen und PhoneLink und TimeLink zum Kopieren. Konfiguriere dann die richtigen Werte für Deine CSV-Datei.

```
Source=
Destination=
ActivitySource=
ActivityDestination=
Interval=15
TimeZone=0
Protocol=1
SeparatorCharacter=
ActivitySeparatorCharacter=
DeleteImportFiles=0
DeleteActivityImportFiles=0
HeaderLines=
ActivityHeaderLines=
GroupColumn=
DateColumn=
TimeColumn=
SubGroupColumn=
SubGroups=
HeaderLines=
Interval=
AHTColumn=
ColumnNames=Queue;Date;Time;CallsOffered;CallsHandled;AHT
Groups=
DateOrder=
ActivityColumn=
AgentColumn=
ActivityStartDateColumn=
ActivityStartTimeColumn=
ActivityEndDateColumn=
ActivityEndTimeColumn=
ActivityTimeSpanType=
ActivityIdentifiers=
ActivityDescriptions=
ActivityDateOrder=
ActivityColumnNames=AgentID;ActivityID;StartDate;StartTime;EndDate;EndTime;AHT
```

## Weitere Schritte

Vor dem ersten Daten-Import ist ein weiterer Schritt namens Mapping erforderlich, der in zwei separaten Artikeln beschrieben ist:

- {% link_new PhoneLink Mapping | features/acd-integration/xlink-mapping-telephony.md %}
- {% link_new TimeLink Mapping | features/acd-integration/xlink-mapping-activities.md %}
