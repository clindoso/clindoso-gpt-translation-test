---
title: Datenbank-Integration hinzufügen
navigation_title: Datenbank
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Verbinde deine Datenbank mit injixo, um Daten zu importieren.
redirect_from: /de/add-odbc-integration/
redirect_reason: Artikel umbenannt im September 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

In diesem Artikel lernst du, wie du eine Datenbank-Integration hinzufügst.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Was ist eine Datenbank-Integration?

Eine Datenbank-Integration ist eine Sonderform einer On-Premise-Integration. Verwende eine Datenbank-Integration, wenn dein System nicht mit einer Cloud-Integration oder einer anderen On-premise-Integration verbunden werden kann.

Du kannst eine SQL-Abfrage definieren, um Daten aus einer Datenbank zu lesen. Datenbank-Integrationen nutzen {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

## Datenbank-Integration hinzufügen

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke im Abschnitt **Universal Interfaces** auf _Modell auswählen_{:.doc-button}.
4. Klicke im Abschnitt **Datenbank** auf _Integration hinzufügen_{:.doc-button}.

## Deine neue Datenbank-Integration konfigurieren

1. Gib einen eindeutigen **Namen** für die neue Integration ein, der die Datenquelle kennzeichnet.
2. Installiere und verbinde {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Wähle deinen **Datenbanktyp**.
4. Gib je nach Auswahl deine Zugangsdaten ein.

   | Datenbanktyp                         | Zugangsdaten                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | MS SQL Server<br>MySQL<br>PostgreSQL | **Datenbankname**<br>**Host**<br>**Port**: Wenn du eine benannte Instanz (named instance) in einer MS SQL Server-Verbindung verwendest, gib keinen Port ein. Erlaube stattdessen Verbindungen über den UDP-Port 1434 in deiner Firewall, um sicherzustellen, dass der SQL Server-Browser-Dienst den Port für injixo Cloud Link ermitteln kann.<br>**Benutzername**<br>**Passwort**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | Andere (ODBC)                        | **Connection String**: Der Connection String enthält die Parameter, die deine Integration benötigt, um sich mit deinem Datenbankserver zu verbinden. Um herauszufinden, welcher String zu deinem Datenbanktyp und deinem ODBC-Treiber passt, sieh unter [https://www.connectionstrings.com](https://www.connectionstrings.com) nach.<br><br>Beispiel für eine InterSystem Caché-Datenbank:<br>`DRIVER={InterSystemsODBC};SERVER=myServerAddress;` `PORT=12345;DATABASE=myDataBase;UID=myUsername;PWD=myPassword;` <br><br>SQL-Bezeichner in Abfragen werden durch doppelte Anführungszeichen abgegrenzt. Füge dem Connection String zusätzliche Optionen hinzu, wenn dein ODBC-Treiber dies nicht standardmäßig unterstützt.<br><br>Beispiel für eine IBM Informix-Datenbank:<br>`DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=myServerAddress;DATABASE=myDatabase;HOST=myHost;SERVICE=myService;UID=myUsername;PWD=myPassword;PROTOCOL=onsoctcp;DELIMIDENT=y;` |

## Importdaten konfigurieren

1. Wähle im Abschnitt **Konfiguration** aus, welchen Datentyp du aus deiner Datenbank importieren möchtest:

   - **Kontaktbasiert** für historische Kontaktdaten mit einer Zeile für jeden Kontakt
   - **Intervallbasiert** für historische Kontaktdaten, die zu Intervallen aggregiert sind<br>Wähle zusätzlich eine Intervalllänge von 15, oder 30 Minuten.
   - **Agentenstatus** für Daten zum Agentenstatus
     - Standardmäßig werden Daten alle 15&nbsp;Minuten importiert.
       Es gibt zwei zusätzliche Checkboxen für Importdaten vom Typ **Agentenstatus**:
       - **Echtzeitdaten importieren**: Daten werden alle 10&nbsp;Sekunden importiert. Nur für injixo Advanced und Enterprise WFM verfügbar.
       - **Datenabgleich**: Bestimmt, welcher Zeitraum von Agentenstatus-Daten alle&nbsp;15 Minuten importiert wird. Standardmäßig werden Daten der letzten 24&nbsp;Stunden importiert (empfohlen). Erfahre mehr über [Datenabgleich](#datenabgleich)

2. Wähle die **Zeitzone** deiner Datenbank aus dem Dropdown-Menü aus.
3. Gib eine **SQL-Query** an, die dazu dient, Daten aus der Datenbank zu importieren. [Beispiel-Abfragen und erwartete Spaltennamen](#beispiel-abfragen-und-erwartete-spaltennamen) findest du im folgenden.
4. Klicke auf _Speichern_{:.doc-button}, um die Integration zu erstellen.

Die Integration beginnt, Daten zu injixo zu importieren. Der erste Import kann eine Weile dauern. Alle aus der Datenbank importierten Queues stehen automatisch für das Mapping auf der {% link_new Workload-Konfigurationsseite | features/forecast/injixo-forecast/manage-workloads.md | #workloads-erstellen %} in injixo Forecast zur Verfügung.

Wenn du Agentenstatus-Daten importieren möchtest, musst du zunächst {% link_new externe Benutzerkennungen und Aktivitäten | features/acd-integration/cloud/import-agent-status-data.md %} zuordnen.

### Datenabgleich:

Manchmal ist es nötig, bereits importierte Agentenstatus-Daten im Nachhinein zu korrigieren. Ein Beispiel ist, wenn ein Teammitglied vergessen hat, sich zum Ende des Arbeitstages abzumelden und du die Daten manuell in deiner Datenbank korrigiert hast, um die tatsächliche Arbeitszeit des Teammitglieds abzubilden.
Wenn die Checkbox aktiviert ist (Standardeinstellung), importiert injixo erneut alle Daten

- der letzten 24 Stunden
- alle 15 Minuten<br>So hast du immer Zugriff auf die aktuellsten Daten.<br>Hinweis: Wenn du Daten änderst, die älter als 24&nbsp;Stunden sind, sind diese Änderungen nicht im erneuten Import enthalten.

Die Checkbox **Datenabgleich** ist standardmäßig aktiviert. Für einige Datenbanken ist die Last kontinuierlicher Datenimporte zu groß. Um die Last zu reduzieren, kannst du die Option deaktivieren.
Wenn die Checkbox deaktiviert ist, importiert injixo ausschließlich die neuesten Daten seit dem letzten erfolgreichen Import. Im Normalfall sind dies die Daten der letzten 15&nbsp;Minuten.<br>Alle Änderungen an Daten, die länger als 15&nbsp;Minuten zurückliegen, sind nicht im erneuten Import enthalten. Deshalb musst du die Daten in injixo manuell aktualisieren.<br>Hinweis: Wir empfehlen, die Checkbox aktiviert zu lassen, da manuelle Datenanpassungen erhebliche Mehrarbeit bedeuten und fehleranfällig sind.

Wenn du deine Integration für weniger als 24&nbsp;Stunden pausierst, importiert injixo alle Daten seit Beginn der Unterbrechung, wenn du den Datenimport erneut startest. Dies gilt unabhängig davon, ob die Checkbox aktiviert ist oder nicht.<br>Hinweis: Wenn du die Integration für einen längeren Zeitraum pausierst, werden alle Daten, die älter sind als 24&nbsp;Stunden, nicht erneut importiert.

## Beispiel-Abfragen und erwartete Spaltennamen

Die Datenbank-Integration erwartet bestimmte Spaltennamen. Der gewählte Importdatentyp bestimmt, welche Spalten abgefragt werden. Du kannst diese Beispiel-Abfragen als Vorlage für komplexere Abfragen verwenden:

<style>
table th:first-of-type {
   width: 20%;
}
table th:nth-of-type(4) {
   width: 50%;
}
</style>

| Importdatentyp   | Beispiel-Query                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------- |
| Intervallbasiert | _SELECT queueidentifier, queuename, timestamp, offered, answered, handlingtime, channel FROM testTable_ |
| Kontaktbasiert   | _SELECT queueidentifier, queuename, timestamp, answered, duration, channel FROM testTable_              |
| Agentenstatus    | _SELECT agentidentifier, starttime, endtime, activity FROM testTable_                                   |

Deine Datenbank verwendet wahrscheinlich andere Spaltennamen. Du hast zwei Optionen:

- Verwende einen Alias, um auf andere Spaltennamen zu verweisen, z.&nbsp;B. YourCustomAgentIdColumn für "agentidentifier".
- Erstelle eine Ansicht in deiner Datenbank, die die erwarteten Spaltennamen verwendet.

Beispiel für komplexere Abfrage mit Alias:

```
SELECT
  "Start" für "timestamp",
  "Id" für queueidentifier,
  "Name" für queuename,
  SUM(CASE "countId" WHEN 1000 THEN "val" ELSE 0 END) für offered,
  SUM(CASE "countId" WHEN 1001 THEN "val" ELSE 0 END) für answered,
  SUM(CASE "countId" WHEN 1002 THEN "val" ELSE 0 END) für handlingtime
FROM "table"
WHERE "countId" IN (1000, 1001, 1002)
GROUP BY "Start", "Name"
```

| Spalte                      | Datentyp | Erforderlich | Erläuterung                                                                                                                                                                                             |
| --------------------------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| agentidentifier             | String   | Ja           | Eindeutige Bezeichnung für den Agenten                                                                                                                                                                  |
| starttime                   | Datetime | Ja           | Beginn der Aktivität des Agenten                                                                                                                                                                        |
| endtime                     | Datetime | Nein         | Ende der Aktivität des Agenten<br>Nutze dieses Feld nicht, wenn die Aktivität andauert.                                                                                                                 |
| activity                    | String   | Ja           | Bezeichnung für die externe Aktivität                                                                                                                                                                   |
| queueidentifier             | String   | Ja           | Eindeutige Bezeichnung für die Queue<br>Du kannst die Queue umbenennen, indem du den queuename änderst. Der queueidentifier bleibt gleich.                                                              |
| queuename                   | String   | Ja           | Bezeichnung für die Queue                                                                                                                                                                               |
| timestamp                   | Datetime | Ja           | Start des Intervalls                                                                                                                                                                                    |
| offered                     | Integer  | Ja           | Anzahl Kontakte (z.&nbsp;B. Anrufe oder E-Mails) im Intervall                                                                                                                                           |
| answered (intervallbasiert) | Integer  | Ja           | Anzahl der Kontakte, die im Intervall bearbeitet wurden.                                                                                                                                                |
| answered (kontaktbasiert)   | Integer  | Ja           | Der Wert 1 bedeutet, dass der Kontakt bearbeitet wurde. Der Wert 0 bedeutet, dass der Kontakt nicht bearbeitet wurde.                                                                                   |
| handlingtime                | Integer  | Ja           | Gesamtbearbeitungszeit für alle Kontakte im Intervall                                                                                                                                                   |
| duration                    | Integer  | Ja           | Gesamtbearbeitungszeit eines einzelnen Kontakts                                                                                                                                                         |
| channel                     | String   | Nein         | Bezeichnung für den Kanal der injixo Quell-Queue<br>Der Standardwert, wenn die Spalte weggelassen wird, ist _calls_<br>Gültige Werte: _calls_, _chats_, _emails_, _social_media_, _documents_, _cases_. |

## Datenbank-Integration bearbeiten

Wenn deine Datenbank-Details oder Datenstruktur sich ändern, kannst du die Konfiguration deiner Datenbank-Integration bearbeiten. Der Import von Daten wird fortgesetzt. Um fehlende Daten zu importieren, erstelle eine neue Integration.
