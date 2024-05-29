---
title: Datenbank-Integration hinzufügen
navigation_title: Datenbank
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Verbinde deine Datenbank mit injixo, um Daten zu importieren.
redirect_from:
  - de/add-odbc-integration/
redirect_reason: Artikel umbenannt im September 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Was ist eine Datenbank-Integration?

Eine Datenbank-Integration ist eine Sonderform einer On-Premise-Integration. Verwende eine Datenbank-Integration, wenn dein System nicht mit einer Cloud-Integration oder einer anderen On-premise-Integration verbunden werden kann.

Du kannst eine SQL-Abfrage definieren, um Daten aus einer Datenbank zu lesen. Datenbank-Integrationen nutzen {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

## Datenbank-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der Kachel **Universal Interfaces** auf _Modell auswählen_{:.doc-button}.
4. Klicke im Abschnitt **Datenbank** auf _Integration hinzufügen_{:.doc-button}.

## Deine neue Datenbank-Integration konfigurieren

1. Gib einen eindeutigen Namen für die neue Integration ein, der die Datenquelle kennzeichnet.
2. Installiere und verbinde {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Wähle deinen **Datenbanktyp**.
4. Gib je nach Auswahl deine Zugangsdaten ein.

   | Datenbanktyp                         | Zugangsdaten                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | MS SQL Server<br>MySQL<br>PostgreSQL | **Datenbankname**<br>**Host**<br>**Port**: Wenn du eine bereits benannte Instanz (named instance) in einer MS SQL Server-Verbindung verwendest, gib keinen Port ein. Öffne stattdessen den UDP-Port 1434 in deiner Firewall, um sicherzustellen, dass der SQL Server-Browser-Dienst den Port für injixo Cloud Link ermitteln kann.<br>**Benutzername**<br>**Passwort**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | Andere (ODBC)                        | **Connection String**: Connection Strings enthalten Parameter zur Verbindung deiner Integration mit deinem Datenbankserver. Um einen String zu finden, der zu deinem Datenbanktyp und deinem ODBC-Treiber passt, gehe zu [https://www.connectionstrings.com](https://www.connectionstrings.com).<br><br>Beispiel für eine InterSystem Caché-Datenbank:<br>`DRIVER={InterSystemsODBC};SERVER=myServerAddress;` `PORT=12345;DATABASE=myDataBase;UID=myUsername;PWD=myPassword;` <br><br>In Abfragen werden SQL-Identifier durch doppelte Anführungszeichen abgegrenzt. Füge dem Connection String weitere Optionen hinzu, wenn dein ODBC-Treiber dies nicht standardmäßig unterstützt, z.&nbsp;B. für Informix.<br><br>Beispiel für eine IBM Informix-Datenbank:<br>`DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=myServerAddress;DATABASE=myDatabase;HOST=myHost;SERVICE=myService;UID=myUsername;PWD=myPassword;PROTOCOL=onsoctcp;DELIMIDENT=y;`<br><br>Du kannst auch eine ODBC-Datenquelle erstellen, in der du den Treiber, den Server, die Datenbank usw. konfigurierst. Damit kannst du die folgende DSN-Option als Connection String hinzufügen statt die Verbindungsdetails in den Connection String einzufügen. Zusätzlich musst du noch die Optionen hinzufügen, die nicht in der ODBC-Datenquelle konfiguriert werden können, z.&nbsp;B. `DELIMIDENT=y`.<br><br>DSN-Beispiele:<br> `DSN=myODBCDatasourceName;`<br>`DSN=myODBCDatasourceName;DELIMIDENT=y;` |

## Importdaten konfigurieren

1. Wähle im Abschnitt **Konfiguration** aus, welchen Datentyp du aus deiner Datenbank importieren möchtest:

   - **Kontaktbasiert** für historische Kontaktdaten mit einer Zeile für jeden Kontakt
   - **Intervallbasiert** für historische Kontaktdaten, die zu Intervallen von 15&nbsp;bzw. 30&nbsp;Minuten (je nach konfigurierter Intervalllänge) aggregiert sind
   - **Agentenstatus** für Agentenstatus-Daten  
     Standardmäßig werden alle 15&nbsp;Minuten Daten importiert. Mit diesen beiden Checkboxen kannst du das Importverhalten anpassen: - **Echtzeitdaten importieren**: Daten werden alle 10&nbsp;Sekunden importiert. Nur für injixo Advanced und Enterprise WFM verfügbar. - **Datenabgleich**: Bestimmt, welcher Zeitraum von Agentenstatus-Daten alle&nbsp;15 Minuten importiert wird. Standardmäßig werden Daten der letzten 24&nbsp;Stunden importiert.

2. Wähle die **Zeitzone** deiner Datenbank aus dem Dropdown-Menü aus.
3. Gib eine **SQL-Abfrage** an, die dazu dient, Daten aus der Datenbank zu importieren. Erfahre mehr über die [SQL-Abfrage](#sql-abfrage).
4. Um die Integration zu erstellen, klicke auf _Integration speichern_{:.doc-button}.  
   Die Integration beginnt, Daten zu injixo zu importieren. Der erste Import kann eine Weile dauern.  
   Alle aus der Datenbank importierten Queues stehen automatisch für das Mapping auf der {% link_new Workload-Konfigurationsseite | features/forecast/injixo-forecast/create-workloads.md | #workloads-erstellen %} in injixo Forecast zur Verfügung.  
   Externe Aktivitäten sind in der Aktivität Anwesend (ID 1) verfügbar. Um Agentenstatus-Daten zu importieren, musst du {% link_new externe Benutzerkennungen und Aktivitäten | features/acd-integration/cloud/import-agent-status-data.md %} zuordnen.

### Datenabgleich

Manchmal ist es nötig, bereits importierte Agentenstatus-Daten im Nachhinein zu korrigieren. Ein Beispiel ist, wenn ein Mitarbeiter vergessen hat, sich zum Ende des Arbeitstages abzumelden und du die Daten manuell in deiner Datenbank korrigiert hast, um die tatsächliche Arbeitszeit des Mitarbeiters abzubilden.

Die Checkbox **Datenabgleich** ist standardmäßig aktiviert. injixo importiert alle Daten neu:

- aus den letzten 24 Stunden
- in Intervallen von 15 Minuten

Du hast also immer Zugriff auf die aktuellsten Daten der letzten 24&nbsp;Stunden. Der erneute Import enthält keine Datenänderungen, die älter als 24&nbsp;Stunden sind.

Möglicherweise ist für deine Datenbank die Last kontinuierlicher Datenimporte zu groß. Wenn du die Funktionalität Datenabgleich deaktivieren musst, importiert injixo nur die neuesten Daten seit dem letzten erfolgreichen Import (in der Regel Daten aus den letzten 15&nbsp;Minuten). Wenn dies der Fall ist, musst du eventuell Daten manuell in injixo aktualisieren, wenn diese vor über 15&nbsp;Minuten importiert wurden. Wenn möglich, lasse die Checkbox aktiviert, da manuelle Datenanpassungen erhebliche Mehrarbeit bedeuten und fehleranfällig sind.

Wenn du deine Integration für weniger als 24&nbsp;Stunden pausierst, importiert injixo alle Daten seit Beginn der Unterbrechung, wenn du den Datenimport erneut startest. Dies gilt unabhängig davon, ob die Checkbox aktiviert ist oder nicht.  
Wenn du die Integration für einen längeren Zeitraum pausierst, werden alle Daten, die älter sind als 24&nbsp;Stunden, nicht erneut importiert.

## SQL-Abfrage

Die SQL-Abfrage für eine Datenbank-Integration muss bestimmte Spaltennamen enthalten. Der gewählte Importdatentyp legt die erwarteten Spalten fest. Du kannst den Tabellennamen festlegen. Im folgenden findest du die einfachsten SQL-Abfragen, die du ausführen kannst:

<style>
table th:first-of-type {
   width: 20%;
}
table th:nth-of-type(4) {
   width: 50%;
}
</style>

| Importdatentyp   | Beispiel-Query                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------- |
| Intervallbasiert | SELECT queueidentifier, queuename, timestamp, offered, answered, handlingtime, channel FROM table |
| Kontaktbasiert   | SELECT queueidentifier, queuename, timestamp, answered, duration, channel FROM table              |
| Agentenstatus    | SELECT agentidentifier, starttime, endtime, activity FROM table                                   |

> Hinweis
>
> In der Regel entsprechen die Spalten deiner Datenbank nicht den erwarteten Spaltennamen. Um dies zu umgehen, verwende die erforderlichen Spaltennamen als Spaltenalias oder erstelle eine entsprechende Ansicht in deiner Datenbank.

Erweitere die Beispielabfragen, um Daten aus deiner benutzerdefinierten Tabelle abzurufen und zu filtern.

```
SELECT
  Start as "timestamp",
  Id as queueidentifier,
  Name as queuename,
  SUM(CASE countId WHEN 1000 THEN val ELSE 0 END) as offered,
  SUM(CASE countId WHEN 1001 THEN val ELSE 0 END) as answered,
  SUM(CASE countId WHEN 1002 THEN val ELSE 0 END) as handlingtime,
  calls as channel
FROM table
WHERE countId IN (1000, 1001, 1002)
GROUP BY Start, Name
```

## Erläuterungen zu den Spalten

Die folgenden Tabellen enthalten Erläuterungen für die erwarteten Spalten für jeden Importtyp.

### Agentenstatus

<style>

table {
   width: 100%;
}  
table th:first-of-type {
   width: 20%;
}
table th:nth-of-type(4) {
   width: 50%;
}
</style>

| Spalte          | Datentyp | Erforderlich | Erläuterung                                                                             |
| --------------- | -------- | ------------ | --------------------------------------------------------------------------------------- |
| agentidentifier | String   | Ja           | Eindeutige Bezeichnung für den Agenten                                                  |
| starttime       | Datetime | Ja           | Beginn der Aktivität des Agenten                                                        |
| endtime         | Datetime | Nein         | Ende der Aktivität des Agenten<br>Nutze dieses Feld nicht, wenn die Aktivität andauert. |
| activity        | String   | Ja           | Kennung für die externe Aktivität                                                       |

### Intervallbasiert

| Spalte          | Datentyp | Erforderlich | Erläuterung                                                                                                                                                              |
| --------------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| queueidentifier | String   | Ja           | Eindeutige Bezeichnung für die Queue<br>Du kannst die Queue umbenennen, indem du den queuename änderst. Der queueidentifier bleibt gleich.                               |
| queuename       | String   | Ja           | Bezeichnung für die Queue                                                                                                                                                |
| timestamp       | Datetime | Ja           | Start des Intervalls                                                                                                                                                     |
| offered         | Integer  | Ja           | Anzahl Kontakte (z.&nbsp;B. Anrufe oder E-Mails) im Intervall                                                                                                            |
| answered        | Integer  | Ja           | Anzahl der Kontakte, die im Intervall bearbeitet wurden                                                                                                                  |
| handlingtime    | Integer  | Ja           | Gesamtbearbeitungszeit für alle Kontakte im Intervall                                                                                                                    |
| channel         | String   | Nein         | Bezeichnung für den Kanal der injixo Quell-Queue<br>Bei leerer Spalte standardmäßiger Wert calls<br>Gültige Werte: calls, chats, emails, social_media, documents, cases. |

### Kontaktbasiert

| Spalte          | Datentyp | Erforderlich | Erläuterung                                                                                                                                                              |
| --------------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
| queueidentifier | String   | Ja           | Eindeutige Bezeichnung für die Queue<br>Du kannst die Queue umbenennen, indem du den queuename änderst. Der queueidentifier bleibt gleich.                               |
| queuename       | String   | Ja           | Bezeichnung für die Queue                                                                                                                                                |
| timestamp       | Datetime | Ja           | Start des Intervalls                                                                                                                                                     |     |
| answered        | Integer  | Ja           | Bearbeiteter Kontakt (Wert 1)<br>Kein bearbeiteter Kontakt (Wert 0)                                                                                                      |
| duration        | Integer  | Nein         | Gesamtbearbeitungszeit eines einzelnen Kontakts                                                                                                                          |
| channel         | String   | Nein         | Bezeichnung für den Kanal der injixo Quell-Queue<br>Bei leerer Spalte standardmäßiger Wert calls<br>Gültige Werte: calls, chats, emails, social_media, documents, cases. |

## Datenbank-Integration bearbeiten

Wenn deine Datenbank-Details oder Datenstruktur sich ändern, kannst du die Konfiguration deiner Datenbank-Integration bearbeiten. Der nächste Datenimport wird wie zuvor durchgeführt. Wenn du alle aus der Vergangenheit verfügbaren Daten erneut importieren musst, erstelle eine neue Integration.

## Bekannte Probleme mit dem ODBC-Treiber

Um eine Zunahme der TCP-Verbindungen in Cloud Link bei der Abfrage von Daten von Amazon Athena zu verhindern, stelle sicher, dass du die [Treiberversion Athena ODBC 2.x](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver.html) verwendest.
