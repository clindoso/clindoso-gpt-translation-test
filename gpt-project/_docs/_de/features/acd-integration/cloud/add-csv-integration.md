---
title: CSV-Integration hinzufügen
navigation_title: CSV
description: Importiere historische Daten aus CSV-Dateien in injixo.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /de/csv-format/
redirect_reason: /csv-format/ used on in injixo UI (injixo.com/csv-importer)
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
---

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen | features/acd-integration/cloud/how-integrations-work.md %}.

## Was ist eine CSV-Integration?

Eine CSV-Integration importiert historische Kontakt- oder Agentenstatus-Daten aus CSV-Dateien. Verwende eine CSV-Integration, wenn dein System mit keiner anderen Integration verbunden werden kann.

So sieht der Prozess der CSV-Integration im Überblick aus:

- CSV-Integration in injixo erstellen
- CSV-Schema erstellen
- Spalten zuordnen (über Dropdown-Menü oder SQL-Abfrage)
- CSV-Dateien automatisch oder manuell importieren

## CSV-Integration hinzufügen

Um verschiedene CSV-Dateiformate zu importieren (z.&nbsp;B. mit unterschiedlichen Trennzeichen, Datumsformaten oder Spaltennamen), richte jeweils eine separate Integration ein. Je nachdem, welche CSV-Datei dein externes System erzeugt, kann es sein, dass die Spalten der Datei von denen in injixo abweichen. [Erfahre mehr](#spalten-zuordnen) über die Spalten, die injixo erwartet und wie du Spalten zuordnest, wenn deine CSV-Datei andere Spalten oder Spaltennamen enthält.

Um eine CSV-Integration in injixo hinzuzufügen, gehe wie folgt vor:

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke im Abschnitt **Universal Interfaces** auf _Modell auswählen_{:.doc-button}.
4. Klicke im Abschnitt **CSV** auf _Integration hinzufügen_{:.doc-button}.

## Neue CSV-Integration konfigurieren

1. Gib im Abschnitt **Allgemeine Informationen** einen eindeutigen **Namen** für die Integration ein, der die Datenquelle benennt.
2. Installiere im Abschnitt **injixo Cloud Link** {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md | #injixo-cloud-link-installieren %} und stelle die Verbindung her. Wenn du die Daten lieber [manuell hochladen](#manueller-datenimport) möchtest, kannst du diesen Schritt überspringen.
3. Wähle im Abschnitt **CSV-Schema-Konfiguration** den **Datentyp für Import**:

   - **Kontaktdaten**: Die hochgeladenen Daten enthalten alle eingehenden und angenommenen Volumen, die dein externes System aufgezeichnet hat. Dazu gehören Anrufe, Chats, Social Media, Tickets, E-Mails oder Dokumente.
   - **Agentenstatus**: Die hochgeladenen Daten enthalten alle Aktivitäten von Agenten, die dein externes System aufgezeichnet hat. Dazu gehören Anmeldung, Abmeldung, Rufbereitschaft, Nachbearbeitungszeit, Pause, etc.

4. Klicke auf _Erstelle ein neues CSV-Schema_{:.doc-button}.
5. Konfiguriere die CSV-Schema-Einstellungen.
   Dazu gehören:

- Einrichtung und Vorverarbeitungsoptionen
- Spaltenzuordnung (standardmäßig über [Dropdown-Menüs](#spalten-zuordnen); alternativ über [SQL-Abfrage](#spalten-zuordnen-sql-abfrage))  
   Erfahre mehr darüber, wie ein [CSV-Schema](#csv-schema-erstellen) mit den aufgezählten Konfigurationsoptionen erstellt wird.

6. Klicke auf _Speichern_{:.doc-button}, um die Integration zu erstellen.

Nachdem du die Integration gespeichert hast, kannst du den [manuellen Datenimport](#manueller-datenimport) verwenden oder den [automatischen Datenimport](#automatischer-datenimport) einrichten.

## CSV-Schema erstellen

Jede CSV-Integration hat ihr eigenes CSV-Schema. Das CSV-Schema beschreibt die CSV-Dateiformatierung und die Spaltenzuordnung. Wenn dein externes System CSV-Dateien erzeugt, deren Spaltennamen von denen in injixo abweichen, kannst du sie in injixo zuordnen. Nutze dazu entweder die [Dropdown-Menüs (Standard)](#spalten-zuordnen) oder eine [SQL-Abfrage](#spalten-zuordnen-sql-abfrage).  
[Erfahre mehr](#spalten-zuordnen) über die Spalten, die injixo erwartet und wie du Spalten zuordnest, wenn deine CSV-Datei andere Spalten oder Spaltennamen enthält.

Bevor du ein CSV-Schema erstellen kannst, musst du eine [CSV-Integration hinzufügen](#csv-integration-hinzufügen) und den Datentyp für den Import auswählen. Welche Parameter du für das CSV-Schema konfigurierst, hängt davon ab, welchen Datentyp du für den Import ausgewählt hast (Kontaktdaten oder Agentenstatus).

### Einrichtung und Vorverarbeitungsoptionen

1. Lade im Abschnitt **Einrichtung** eine Beispiel-Datei hoch, die dein externes System erzeugt hat. Dadurch kannst du sehen, wie injixo mit den Dateien deines Systems beim Import umgeht.
2. Konfiguriere die folgenden Parameter: Je nach Importdatentyp können sich die Parameter unterscheiden:<br><br>

   | Parameter                                                                         | Beschreibung                                                                                                                                                                                                                                                                                                                                                                 |
   | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Spaltentrennzeichen der CSV-Datei**                                             | Trennzeichen, das in der hochgeladenen CSV-Datei verwendet wird, z.&nbsp;B. Semikolon.                                                                                                                                                                                                                                                                                       |
   | **Zeitzone**                                                                      | Zeitzone, in der dein externes System die Daten aufzeichnet, z.&nbsp;B. Amerika/Chicago (UTC-05:00).                                                                                                                                                                                                                                                                         |
   | **Datenlayout**<br>(Nur für Kontaktdaten)                                         | Das Datenlayout hängt davon ab, wie du deine CSV-Datei erstellt hast:<br>**Kontaktbasiert**: Für Datensätze mit Kontaktdaten, die eine Zeile für jeden einzelnen Kontakt enthalten.<br>**Intervallbasiert**: Für aggregierte Daten, die eine Zeile mit allen Kontaktinformationen pro Intervall enthalten. Wähle zusätzlich eine Intervalllänge von 15, 30, oder 60 Minuten. |
   | **Fehlende Werte in vorhandenen Intervallen behandeln**<br>(Nur für Kontaktdaten) | Lege fest, wie fehlende Werte in der Ziel-Queue verarbeitet werden und wie Daten in Forecast und Dashboards angezeigt werden:<br>**Mit Null auffüllen**: Fehlende Werte werden mit einer Null ersetzt.<br>**Leer lassen**: Fehlende Werte werden mit folgendem Text ersetzt: no data.<br>injixo überschreibt bestehende Daten während des Imports.                           |

   > Wähle das Intervall, das dem Intervall deiner ACD entspricht
   >
   > Wenn du ein 30-Minuten-Intervall wählst, während deine ACD Daten in 15-Minuten-Intervallen vorhält, überspringt injixo Intervalle beim Import. Dann werden nur für jedes zweite Intervall Daten importiert. <!-- what happens the other way around? -->

3. (Optional) Lege im Abschnitt **Vorverarbeitungsoptionen** eine oder mehrere Optionen fest, die für dein CSV-Dateiformat gelten:<br><br>

   | Vorverarbeitungsoption                | Beschreibung                                                                                                                                                                                                                                                         |
   | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Spaltenkopfzeile hinzufügen**       | Bei Dateien ohne Kopfzeile beschriftet injixo die Spalten mit A, B, C, usw. auf der [Spaltenzuordnungsseite](#spalten-zuordnen).                                                                                                                                     |
   | **Leere Zeilen überspringen**         | injixo ignoriert Zeilen, die nur Trennzeichen enthalten.                                                                                                                                                                                                             |
   | **Überspringe die erste(n) Zeile(n)** | injixo entfernt zusätzliche Zeilen am Anfang der Datei. Gib die Anzahl der Zeilen ein, die ignoriert werden sollen.                                                                                                                                                  |
   | **Überspringe die Zeile(n) mit**      | injixo ignoriert Zeilen mit bestimmten Zeichen. Gib eine Zeichenfolge ein (Groß- und Kleinschreibung beachten). injixo ignoriert Zeilen mit dieser Zeichenfolge. Du kannst mehrere Zeichenfolgen hinzufügen, indem du auf _String hinzufügen_{:.doc-button} klickst. |

4. Um mit der Spaltenzuordnung fortzufahren, klicke auf _Zur Spaltenzuordnung_{:.doc-button}.

### Spalten zuordnen

Standardmäßig kannst du die Dropdown-Menüs im Abschnitt **Spalten zuordnen** nutzen, um festzulegen, wie die Spalten deiner CSV-Dateien den Spalten zugewiesen werden, die injixo erwartet. Bevor du Spalten zuordnen kannst, musst du die [Einrichtung](#einrichtung-und-vorverarbeitungsoptionen) abschließen.
Wenn dein externes System CSV-Dateien mit anderen als den erwarteten Spalten erzeugt, kannst du Spalten auch [über eine SQL-Abfrage zuordnen](#spalten-zuordnen-sql-abfrage).

Die Spaltenzuordnungsseite zeigt eine Vorschau der hochgeladenen CSV-Datei.

1. Nutze die Dropdown-Menüs, um die Spalten und Formate der CSV-Datei zuzuordnen.

2. Fülle jedes Feld aus.  
   Erfahre in den folgenden Tabellen mehr über die Dropdown-Menüs für [Kontaktdaten](#kontaktdaten-dropdown-menüs) und [Agentenstatus](#agentenstatus-dropdown-menüs)-Daten.

3. Um deine Konfiguration zu speichern, klicke auf _Schema speichern_{:.doc-button}.

#### Kontaktdaten Dropdown-Menüs

Wenn du **Kontaktdaten** als Importdatentyp ausgewählt hast, zeigt die Spaltenzuordnungsseite in der Standardansicht folgende Elemente:

| Feld            | Beschreibung                                                                                                                                                                                                                                                                                                             | Erforderlich für intervallbasierte Daten | Erforderlich für kontaktbasierte Daten |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------: | :------------------------------------: |
| **Queue-Name**  | Name der Queue, aus der die Daten stammen                                                                                                                                                                                                                                                                                |                    Ja                    |                   Ja                   |
| **Date**        | Datumswerte und verwendetes Format<br>Standardmäßig kannst du aus dem Dropdown-Menü das Datumsformat auswählen, das deinem CSV-Format entspricht. Um ein [benutzerdefiniertes Datumsformat](#benutzerdefiniertes-datumsformat) zu konfigurieren, klicke auf das {% icon gear %} und gib dein Format in das Textfeld ein. |                    Ja                    |                   Ja                   |
| **Time**        | Zeitwerte und verwendetes Format                                                                                                                                                                                                                                                                                         |                    Ja                    |                   Ja                   |
| **Zeitstempel** | Zeitstempelwerte mit einem [benutzerdefinierten Zeitstempelformat](#benutzerdefiniertes-zeitstempelformat-mit-datum-und-uhrzeit)<br>Die Spalte erscheint, wenn du **Datum und Uhrzeit in einer Spalte** aktivierst.                                                                                                      |                    Ja                    |                   Ja                   |
| **Offered**     | Eingehende Kontakte (pro Intervall für intervallbasierte Daten)<br>Unterstützt ganze Zahlen und Dezimalzahlen mit Punkt (z.&nbsp;B. 15.0).                                                                                                                                                                               |                    Ja                    |                   Ja                   |
| **Angenommene** | Beantwortete Kontakte (pro Intervall für intervallbasierte Daten)<br>Erlaubt ganze Zahlen und Dezimalzahlen mit Punkt (z.&nbsp;B. 1.0).<br>Für kontaktbasierte Daten kann der Wert für bearbeitete Kontakte nur 0 oder 1 (oder Dezimalzahlen) sein.                                                                      |                    Ja                    |                   Ja                   |
| **AHT**         | Durchschnittliche Bearbeitungszeit pro Intervall<br> Unterstützte Formate sind Sekunden (ganze Zahlen) oder hh:mm:ss (z.&nbsp;B. 00:05:00).<br>Wenn keine AHT-Spalte vorhanden ist, wähle **Keine Spalte**.<br>Dieses Feld wird nur für intervallbasierte Daten angezeigt.                                               |                   Nein                   |                  Nein                  |
| **Dauer**       | Dauer für den Eintrag<br>Dieses Feld wird nur für kontaktbasierte Daten angezeigt.                                                                                                                                                                                                                                       |                   Nein                   |                   Ja                   |
| **Kanal**       | Fester Kanalname (erstes Dropdown-Menü) oder auswählbare Spalte, die den Kanalnamen enthält (zweites Dropdown-Menü)<br>Erlaubte Werte: calls, emails, chats, documents, cases, social_media                                                                                                                              |                    Ja                    |                   Ja                   |

#### Agentenstatus Dropdown-Menüs

Wenn du **Agentenstatus** als Importdatentyp ausgewählt hast, zeigt die Spaltenzuordnungsseite in der Standardansicht folgende Elemente:

| Feld                  | Beschreibung                                                                                                                                                                                                                                                                                                                                       | Erforderlich |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Agentenkennung**    | Eindeutiger Bezeichner für den Agenten, z. B. ID oder Name                                                                                                                                                                                                                                                                                         | Ja           |
| **Aktivitätskennung** | Aktivität, an der der Agent gerade arbeitet                                                                                                                                                                                                                                                                                                        | Ja           |
| **Startdatum**        | Datum, an dem der Agent die Aktivität begonnen hat<br>Standardmäßig kannst du aus dem Dropdown-Menü das Datumsformat auswählen, das dem Format deiner CSV-Datei entspricht. Um ein [benutzerdefiniertes Datumsformat](#benutzerdefiniertes-datumsformat) zu konfigurieren, klicke auf das {% icon gear %} und gib dein Format in das Textfeld ein. | Ja           |
| **Startzeit**         | Zeitpunkt, zu dem der Agent die Aktivität begonnen hat                                                                                                                                                                                                                                                                                             | Ja           |
| **Startzeitstempel**  | [Benutzerdefiniertes Zeitstempelformat](#benutzerdefiniertes-zeitstempelformat-mit-datum-und-uhrzeit) mit Datum und Uhrzeit, zu der der Agent die Aktivität begonnen hat<br>Die Spalte erscheint, wenn du **Datum und Uhrzeit in einer Spalte** aktivierst.                                                                                        | Ja           |
| **Enddatum**          | Datum, an dem der Agent die Aktivität beendet hat<br>Wähle aus dem Dropdown-Menü das Datumsformat aus, das deinem Format entspricht. Um ein [benutzerdefiniertes Datumsformat](#benutzerdefiniertes-datumsformat) zu konfigurieren, klicke auf das {% icon gear %} und gib dein benutzerdefiniertes Format in das Textfeld ein.                    | Nein         |
| **Endzeit**           | Zeitpunkt, zu dem der Agent die Aktivität beendet hat                                                                                                                                                                                                                                                                                              | Nein         |
| **Endzeitstempel**    | [Benutzerdefiniertes Zeitstempelformat](#benutzerdefiniertes-zeitstempelformat-mit-datum-und-uhrzeit) mit Datum und Uhrzeit, zu der der Agent die Aktivität beendet hat<br>Die Spalte erscheint, wenn du **Datum und Uhrzeit in einer Spalte** aktivierst.                                                                                         | Nein         |

#### Benutzerdefiniertes Datumsformat

Lege ein benutzerdefiniertes Datumsformat fest, das mit dem Datum in deinen CSV-Dateien übereinstimmt. Benutze die folgenden Zeichen im Feld **Benutzerdefiniertes Datumsformat**:

- für den Tag: **D** (einstellige Ziffern 1-9) oder **DD** (mit führenden Nullen)
- für den Monat: **M** (einstellige Ziffern 1-9) oder **MM** (mit führenden Nullen)
- für das Jahr: **YY** oder **YYYY**

Alle anderen Zeichen werden als Trennzeichen interpretiert.

Examples:

| Date     | Benutzerdefiniertes Datumsformat |
| -------- | -------------------------------- |
| 13/1,22  | D/M,YY                           |
| 010122   | DDMMYY                           |
| 13012022 | DDMMYYYY                         |

#### Benutzerdefiniertes Zeitstempelformat mit Datum und Uhrzeit

Um ein benutzerdefiniertes Format für einen Zeitstempel hinzuzufügen, aktiviere die Option **Datum und Uhrzeit in einer Spalte**.
Zusätzlich zum [benutzerdefinierten Datumsformat](#benutzerdefiniertes-datumsformat) musst du das Zeitformat festlegen (mit Kleinbuchstaben):

- für Stunden: **h** (einstellige Ziffern 1-9) oder **hh** (mit führenden Nullen)
- für Minuten: **m** (einstellige Ziffern 1-9) oder **mm** (mit führenden Nullen)
- (optional) für Sekunden: **s** (einstellige Ziffern 1-9) oder **ss** (mit führenden Nullen)

Examples:

| Datum und Uhrzeit | Zeitstempelformat |
| ----------------- | ----------------- |
| 13/1,22 9:15:8    | D/M,YY h:m:s      |
| 010122 09-15      | DDMMYY hh:mm      |

### Spalten zuordnen (SQL-Abfrage)

Bei den meisten CSV-Dateien kannst du die Spalten standardmäßig über die Dropdown-Menüs zuordnen. Wenn dein externes System CSV-Dateien erzeugt, in denen gewisse Spalten nicht enthalten sind, die das Standardformular erfordert (z.&nbsp;B. wenn weitere Berechnungen nötig sind) oder manche Spaltenformate nicht unterstützt werden, kannst du die [Standardmethode](#spalten-zuordnen) für die Spaltenzuordnung möglicherweise nicht nutzen. In diesem Fall kannst du die Spalten über eine SQL-Abfrage (SQLite) zuordnen. Damit kannst du zum Beispiel Gesamtwerte in Durchschnittswerte umwandeln oder das Anrufvolumen aus mehreren Spalten ermitteln. Diese Zuordnungsmethode ist nur für Kontaktdaten verfügbar. Sie kann nicht für Agentenstatus-Daten verwendet werden.

#### Voraussetzungen

Beachte folgende Voraussetzungen beim Schreiben einer SQL-Abfrage für die Spaltenzuordnung:

- Verwende `uploaded_file` als Tabellennamen.
- Verwende Kleinschreibung für Spaltennamen.
- Verwende datetime als Datentyp für die Zeitstempel-Spalte (formatiert als `YYYY-MM-DD hh:mm:ss`).
- Verwende die Query-Syntax von [SQLite](https://www.sqlite.org).

Die SQL-Abfrage von [SQLite](https://www.sqlite.org) unterstützt mathematische Operationen, Datenumwandlungen und Aliase (um Spalten mit unterschiedlichen Spaltennamen zuzuordnen). Um mehr über die Einschränkungen im einzelnen zu erfahren, sieh dir folgende Links auf sqlite.org an (nur auf Englisch verfügbar):

- [numerische Genauigkeit](https://www.sqlite.org/datatype3.html)
- [mathematische Funktionen](https://www.sqlite.org/lang_mathfunc.html)
- [implizite Datenumwandlungen](https://www.sqlite.org/datatype3.html#affinity)
- [Datums- und Zeitfunktionen](https://www.sqlite.org/lang_datefunc.html)
- [String-Manipulation](https://www.sqlite.org/lang_corefunc.html#string_functions)

Um die Spalten über SQL-Abfrage zuzuordnen, gehe wie folgt vor:

> Ändern der Zuordnungsmethode überschreibt bestehendes CSV-Schema
>
> Wenn du bereits ein CSV-Schema erstellt hast, wird dieses überschrieben, wenn du die Zuordnungsmethode änderst und das neue Schema speicherst. Du kannst ein überschriebenes CSV-Schema nicht wiederherstellen.

1. Aktiviere oben rechts auf der Spaltenzuordnungsseite die Option **Spaltenzuordnung über SQL-Abfrage**.
2. Gib eine SQL-Abfrage (SQLite) in das Textfeld ein. Tipp: Kopiere je nach Bedarf die folgenden Beispielabfragen und füge sie in das Textfeld ein.

Wenn du sowohl intervallbasierte als auch kontaktbasierte Kontaktdaten hochladen möchtest, musst du jeweils eine eigene Integration hinzufügen und eine separate SQL-Abfrage schreiben.

### Erforderliche Spalten in SQL-Abfrage

In der folgenden Tabelle erhältst du einen Überblick über die Spalten, die in der SQL-Abfrage erforderlich sind:

> Je nach [WFM-Plan](https://www.injixo.com/de/pricing/) kann es sein, dass dir nicht alle Kanäle der injixo-Quell-Queue zur Verfügung stehen.

| Spaltenname | Datentyp | Erforderlich | Erläuterung                                                                                                                                                                                                        |
| ----------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| queue       | String   | Ja           | Bezeichnung für die Queue                                                                                                                                                                                          |
| timestamp   | Datetime | Ja           | Start des Intervalls im Format YYYY-MM-DD hh:mm:ss                                                                                                                                                                 |
| offered     | Integer  | Ja           | Anzahl Kontakte (z.&nbsp;B. Anrufe oder E-Mails) im Intervall                                                                                                                                                      |
| answered    | Integer  | Ja           | intervallbasiert: Anzahl der Kontakte, die im Intervall bearbeitet wurden<br>kontaktbasiert: Der Wert 1 bedeutet, dass der Kontakt bearbeitet wurde. Der Wert 0 bedeutet, dass der Kontakt nicht bearbeitet wurde. |
| aht         | Float    | Nein         | Durchschnittliche Bearbeitungszeit für alle Kontakte im Intervall                                                                                                                                                  |
| duration    | Integer  | Ja           | Gesamtbearbeitungszeit eines einzelnen Kontakts                                                                                                                                                                    |
| channel     | String   | Ja           | Bezeichnung für den Kanal der injixo Quell-Queue<br>Gültige Werte: calls, chats, emails, social_media, documents, cases                                                                                            |

#### Beispielabfragen

Beispiel für intervallbasierte Kontaktdaten:

```sql
SELECT
   queue, timestamp,
   offered, handled, aht,
   channel
FROM uploaded_file
```

Beispiel für kontaktbasierte Kontaktdaten:

```sql
SELECT
   queue, timestamp,
   offered, handled, duration,
   channel
FROM uploaded_file
```

Komplexeres Beispiel für intervallbasierte Kontaktdaten:

```sql
SELECT
   Name as queue,
   strftime('%Y-%m-%d %H:%M:%S', Start) as timestamp
   Offered as offered,
   (Offered - Abandoned) as handled,
   AverageHandlingTime as aht,
   'calls' as channel
FROM uploaded_file
```

<!-- do not change the heading, used in the integrations UI -->

## CSV-Schema bearbeiten

Wenn sich die Datenstruktur einer CSV-Datei ändert, musst du das CSV-Schema einer CSV-Integration bearbeiten.

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Klicke auf das {% icon pencil %} neben der Integration, die du bearbeiten möchtest.
3. Klicke auf _CSV-Schema bearbeiten_{:.doc-button}.
   Du kannst die Optionen im Abschnitt **Setup** ändern. Um die Vorverarbeitungsoptionen zu ändern, klicke auf _Datei neu hochladen_{:.doc-button} und lade eine geänderte oder die ursprüngliche CSV-Datei hoch.
4. Klicke auf _Spalten zuordnen_{:.doc-button}. Du kannst deine Spaltenzuordnung bei Bedarf ändern.
5. Klicke auf _Schema speichern_{:.doc-button}.

> Datenlayout kann nicht geändert werden
>
> Wenn du ein CSV-Schema bearbeitest, kannst du das zuvor ausgewählte Datenlayout nicht mehr ändern (d.&nbsp;h. kontaktbasiert bzw. intervallbasiert).

## Beispiel-Zuordnungen

In diesem Abschnitt findest du Beispiele für CSV-Dateien und passende Zuordnungen. Du kannst die Beispiele als Vorlagen für deine eigenen CSV-Dateien verwenden.

### Kontaktdaten (intervallbasiert)

CSV-Datei:

```

Queue;Date;Time;IncomingCalls;AnsweredCalls;AHT
My Inbound Queue;25/05/2020;08:00;15;14;230
My Inbound Queue;25/05/2020;08:15;16;15;210
My Inbound Queue;25/05/2020;08:30;20;18;235
My Inbound Queue;25/05/2020;08:45;18;15;215

```

<!-- left-align all tables -->
<style>
table {
   margin-left: 0px;
}
</style>

Spaltenzuordnung:

| Spalte       | Zugeordnete Spalte/Werte |
| ------------ | ------------------------ |
| Queue-Name   | Queue                    |
| Date         | Date                     |
| Datumsformat | dd/mm/yyyy               |
| Time         | Time                     |
| Zeitformat   | hh:mm                    |
| Offered      | IncomingCalls            |
| Angenommene  | AnsweredCalls            |
| AHT          | AHT                      |
| AHT-Format   | Sekunden                 |

Dieses Beispiel enthält keine Spalte Kanal. Wähle in der Konfiguration des CSV-Schemas die Option **Kanal**. Um den Kanal für z.&nbsp;B. Anrufe festzulegen, wähle **Anrufe** aus dem Dropdown-Menü.

### Kontaktdaten (kontaktbasiert)

CSV-Datei:

```

Queue;Date;Time;Offered;Answered;Duration
My Inbound Queue;25/05/2020;08:00;1;1;100
My Inbound Queue;25/05/2020;08:03;1;0;0
My Inbound Queue;25/05/2020;08:04;1;1;120
My Inbound Queue;25/05/2020;08:07;1;0;0

```

Spaltenzuordnung:

| Spalte       | Zugeordnete Spalte/Werte |
| ------------ | ------------------------ |
| Queue-Name   | Queue                    |
| Date         | Date                     |
| Datumsformat | dd/mm/yyyy               |
| Time         | Time                     |
| Zeitformat   | hh:mm                    |
| Offered      | Offered                  |
| Angenommene  | Answered                 |
| Dauer        | Dauer                    |

Dieses Beispiel enthält keine Spalte Kanal. Wähle in der Konfiguration des CSV-Schemas die Option **Kanal**. Um den Kanal festzulegen, z.&nbsp;B. für Anrufe, wähle **Anrufe** aus dem Dropdown-Menü.

### Agentenstatus

CSV-Datei:

```

StartDate;StartTime;AgentID;AgentActivityID
2022-04-22;08:34:29;816;1013;
2022-04-22;08:34:42;816;1015;
2022-04-22;08:34:48;816;1015;
2022-04-22;08:39:11;816;1015;

```

Spaltenzuordnung:

| Spalte            | Zugeordnete Spalte/Werte |
| ----------------- | ------------------------ |
| Agentenkennung    | AgentID                  |
| Aktivitätskennung | AgentActivityID          |
| Startdatum        | StartDate                |
| Datumsformat      | yyyy-mm-dd               |
| Startzeit         | StartTime                |
| Zeitformat        | hh:mm:ss                 |

## CSV-Dateien importieren

Sobald du deine CSV-Integration gespeichert hast, kannst du CSV-Dateien importieren.
Folgende Dateikodierungen werden unterstützt:

- UTF-8
- ISO-8859-1/Latin-1
- ISO-8859-9
- Windows-1252

Wir empfehlen die Verwendung von UTF-8, um generische Fehlermeldungen zu vermeiden.

### Automatischer Datenimport

Um mit injixo Cloud Link automatisch neue Daten in injixo hochzuladen, [konfiguriere zuerst deine CSV-Integration](#neue-csv-integration-konfigurieren). Jedes Mal, wenn eine neue CSV-Datei im injixo Cloud-Link-Installationsverzeichnis gespeichert wird, startet ein neuer Upload. Du kannst Dateien entweder manuell oder per Skript speichern.

Das Standardinstallationsverzeichnis ist C:\\Program Files\\injixo Cloud Link. Du kannst dies während der Cloud-Installation ändern. Du kannst außerdem einen separaten {% link_new Import-Ordner | features/acd-integration/cloud/install-cloud-link.md | #ordner-für-import-konfigurieren %} für Datei-Uploads konfigurieren.

Du kannst das Installationsverzeichnis für injixo Cloud Link auf zwei verschiedene Arten konfigurieren:

- Speichere neue CSV-Dateien (manuell oder per Skript) im Installationsverzeichnis. Das Standardverzeichnis ist C:\\Program Files\\injixo Cloud Link.
- Wenn du einen {% link_new Import-Ordner | features/acd-integration/cloud/install-cloud-link.md | #ordner-für-import-konfigurieren %} für injixo Cloud Link konfiguriert hast, speichere die Dateien stattdessen dort.

Nachdem die Verarbeitung abgeschlossen ist, kannst du in injixo Forecast die {% link_new Queues zu einem Workload hinzufügen | features/forecast/injixo-forecast/manage-workloads.md %}.

### Manueller Datenimport

Du kannst über eine Webseite manuell Daten in injixo hochladen.

Bevor du Daten manuell hochladen kannst, [füge eine CSV-Integration](#neue-csv-integration-konfigurieren) hinzu (du kannst die Installation von injixo Cloud Link überspringen).

1. Gehe zu [https://www.injixo.com/csv-importer](https://www.injixo.com/csv-importer).
2. Klicke auf den Link **öffne deinen Datei-Explorer** und wähle eine CSV-Datei zum Importieren aus (oder ziehe sie einfach per Drag & Drop in den Browser).
3. Wähle aus dem Dropdown-Menü unten links deine CSV-Integration.
4. Klicke auf _Datei importieren_{:.doc-button}.
   Um Fehlermeldungen zu vermeiden, muss das Dateiformat mit dem [CSV-Schema](#csv-schema-erstellen) übereinstimmen.
5. Um den Import zu starten, klicke auf _Daten übernehmen_{:.doc-button}.

Wenn die Daten verarbeitet wurden, kannst du in injixo Forecast die {% link_new Queues zu einem Workload hinzufügen | features/forecast/injixo-forecast/manage-workloads.md %}. Die maximale Dateigröße ist 7 MB.

## Häufig gestellte Fragen

| Frage                                                              | Antwort                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kann ich die gleiche Datei zweimal importieren?                    | Ja, wenn du Daten manuell importierst. Nein, wenn du Cloud Link benutzt. Um doppelte Dateien zu erkennen, berechnet injixo während des Imports Prüfsummen. Importierte Dateien mit der gleichen Prüfsumme werden nicht erneut importiert. Wenn die Datei den gleichen Namen, aber einen anderen Inhalt hat, wird sie trotzdem importiert. |
| Löscht injixo automatisch importierte CSV-Dateien nach dem Import? | Nein. Importierte Dateien bleiben im injixo Cloud Link Client-Verzeichnis. Du kannst sie manuell löschen oder selbst eine wiederkehrende Aufgabe einrichten.                                                                                                                                                                              |
| Kann ich eine CSV-Datei importieren, die zukünftige Daten enthält? | Ja, aber wir empfehlen, den Import von Dateien zu vermeiden, die zukünftige Daten enthalten. injixo überspringt zukünftige Daten nicht, sondern speichert sie als historische Daten. Du kannst trotzdem einen Forecast berechnen, aber die Diagramme für Historie und Forecast überschneiden sich.                                        |
