---
title: Universal-Schnittstelle mit Datenbank-Views
product_label:
  - on-premise
---

injixo bietet mit dem Xlink die Möglichkeit, Daten aus Deiner ACD-Datenbank oder einem Data-Warehouse-System zu importieren.

Der einfachste Weg Daten, unabhängig der Datenstruktur in der Quelldatenbank, für den Import bereitzustellen sind Views.
Möglich sind ein oder mehrere Views, die einerseits eine eindeutige ID und den Namen der Queue, andererseits Information zu den dazugehörigen Anruf-Daten enthalten müssen, so dass eine Zuordnung von Anruf zu Queue hergestellt werden kann.

Der Xlink kann sowohl Rohdaten importieren, d.&nbsp;h. es existiert ein Datensatz pro Anruf, als auch auf 15 oder 30 Minuten aggregierte Daten.

In den folgenden Beispielen gehen wir von zwei getrennten Views aus.

## Phonelink

Die Views im Beispiel heißen `Queues` und `CallData`.

Der View `Queues` enthält die IDs und Namen aller aktiven Queues in Deiner ACD. Queues können auch auf ACD-Ebene mehrere Telefonnummern zu einer Gruppe zusammenfassen. Es können nur die Queues importiert werden, die hier vorkommen.

| QueueID | QueueName |
| ------- | ------- |
| 1001 | Zentrale |
| 1002 | Hotline |
| 1003 | Support |

{{ 0 | image: 'Baumstruktur mit Queues im Xlink', '50%' }}

Der View `CallData` enthält alle notwendigen Kennzahlen, um die Anrufe für den injixo Forecast auswerten zu können. Dazu sind die Kennzahlen “Angebotene Anrufe”, “Angenommene Anrufe” und die “Durchschnittliche Bearbeitungszeit”.

{{ 1 | image: "Inhalt des Views in der Datenbank Ansicht" }}

|QueueID | XlinkDateTime | CallsOffered | AHT | CallsHandled |
| ------- | ------- | ------- | ------- | ------- |
|1001 | 2018-02-21 17:34:30.000 | 27 | 241 | 25 |
|1001 | 2018-02-21 17:37:30.000 | 22 | 235 | 20 |
|1001 | 2018-02-21 17:41:30.000 | 29 | 253 | 26 |

{{ 2 | image: "Ansicht der Datentypen-Definition", '50%' }}

Du kannst die Views gern anders benennen, wobei Du dann in den folgenden Beispielen für die Parameter `CallDataTable` bzw. `QueueSQL` und `QueueMappingSQL` Deine View-Namen verwenden musst.

### Konfigurationsvorlage

Nachfolgend findest Du eine Vorlage für die `isps_ul.ini`. Wir gehen hier davon aus, dass Du bereits ein {% link_new externes System vom Typ Universal | features/acd-integration/new-external-system.md %} angelegt und die {% link_new Basis-Konfiguration | features/acd-integration/xlink-configuration-import-odbc.md %} erstellt hast. Öffne in Deinem Xlink-Ordner die Datei `isps_ul.ini` mit einem beliebigen Texteditor, suche hier den Abschnitt, den Du weiter oben mittels externem System angelegt hast.

Füge dort unterhalb des entsprechenden Abschnitts folgendes ein:

```
Interval = 15
QueueSQL = select distinct QueueName from Queues order by QueueName
QueueMappingSQL = select QueueName, QueueID from Queues order by QueueName
ValueTypes = CallsOffered;AHT;CallsHandled
TimeStampColumn = XlinkDateTime
TimeStampType = 2
QueueNameColumn = QueueName
QueueNameType = 0
RetrieveValueTypesUsing = 1
CallDataTable = CallData
```

Prüfe den Eintrag `Interval = 15`. Dieser ist abhängig davon, wie die Daten in Deiner ACD tatsächlich aggregiert werden. In der Regel sind dies entweder 15, 30 oder 60 Minuten. Passe die Intervall-Einstellung bei Bedarf an und speichere anschließend die Datei und starte den Windows Dienst `ISPS Xlink` neu, damit diese Änderungen aktiv werden.

Wenn Du jetzt die Xlink Oberfläche erneut öffnest, siehst Du auf der linken Seite die hierarchische Struktur Deiner ACD-Queues. Wie Du die ACD-Queues mit den injixo-Queues verbindest, erfährst Du in {% link_new Mapping für den Import von Telefoniedaten | features/acd-integration/xlink-mapping-telephony.md %}.

## Timelink

Sobald ein Agent in der ACD seinen Status, z.B. von Bereit in Nachbearbeitung, ändert, wird dazu ein Eintrag in der ACD-Datenbank hinterlegt. Diese Datenbank können wir abfragen und die Daten importieren.

Die Views im Beispiel heißen `Status` und `AgentStatus`.

Der View `Status` enthält die IDs und Namen aller Status in Deiner ACD.

StatusID | StatusName
------- | -------
1001 | Ready
1002 | OnHold
1003 | AfterCall
1004 | NotReady

Spaltenname | Datentyp
------- | -------
StatusID | integer
StatusName | character

Der View `AgentStatus` enthält alle Information zu Zeitpunkt, Dauer zum Statuswechsel der Agenten.

AgentID | StatusID | StatusDateTime | StatusDuration
------- | ------- | ------- | -------
90142 | 1001 | 2017-05-22 08:01:32.000 | 281
90142 | 1002 | 2017-05-22 08:05:00.000 | 180
90142 | 1001 | 2017-05-22 08:08:00.000 | 150
90142 | 1002 | 2017-05-22 08:10:30.000 | 60
90142 | 1002 | 2017-05-22 08:11:30.000 | 230

Spaltenname | Datentyp
------- | -------
AgentID | integer
StatusID | integer
StatusDateTime | datetime
StatusDuration | integer

Du kannst die Views gern anders benennen, wobei Du dann in den folgenden Beispielen für die Parameter `AgentActivityTable` bzw. `ActivitiySQL` Deine View-Namen verwenden musst.

### Konfigurationsvorlage

Nachfolgend findest Du eine Vorlage für die `isps_ul.ini`. Auch hier gehen hier davon aus, dass Du bereits ein {% link_new externes System vom Typ Universal | features/acd-integration/new-external-system.md %} angelegt und die {% link_new Basis-Konfiguration | features/acd-integration/xlink-configuration-import-odbc.md %} erstellt hast. Öffne in Deinem Xlink-Ordner die Datei `isps_ul.ini` mit einem beliebigen Texteditor, suche hier den Abschnitt, den Du weiter oben mittels externem System angelegt hast, füge dort unterhalb des entsprechenden Abschnitts folgendes ein:

```
ActivitySQL = select StatusName, StatusID from Status order by StatusName
ActivityTimeSpanType = 0
ActivityColumn = StatusID
AgentColumn = AgentID
ActivityStartTimeStampColumn = StatusDateTime
ActivityStartTimeStampType = 2
ActivityDurationColumn = StatusDuration
AgentActivityTable = AgentStatus
```

Speichere Deine Änderungen und starte den **ISPS Xlink** Dienst neu, damit diese Änderungen aktiv werden.
Wie Du den ACD-Status mit den injixo-Aktivitäten verbinden kannst, erklärt das Dokument {% link_new Mapping für den Import von Anmelde-/Abmeldedaten | features/acd-integration/xlink-mapping-activities.md %}.
