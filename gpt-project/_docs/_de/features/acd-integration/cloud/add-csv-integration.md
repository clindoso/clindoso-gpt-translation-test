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
3. Klicke in der Kachel **Universal Interfaces** auf _Modell auswählen_{:.doc-button}.
4. Klicke im Abschnitt **CSV** auf _Integration hinzufügen_{:.doc-button}.

## Neue CSV-Integration konfigurieren

1. Gib einen eindeutigen Namen für die Integration ein, der die Datenquelle kennzeichnet.
2. Installiere im Abschnitt **injixo Cloud Link** {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md | #injixo-cloud-link-installieren %} und stelle die Verbindung her. Wenn du die Daten lieber [manuell hochladen](#manueller-datenimport) möchtest, kannst du diesen Schritt überspringen.
3. Wähle im Abschnitt **CSV-Schema-Konfiguration** den **Datentyp für Import**:
   - **Kontaktdaten**: Die hochgeladenen Daten enthalten alle eingehenden und angenommenen Volumen, die dein externes System aufgezeichnet hat. Dazu gehören Anrufe, Chats, Social Media, Tickets, E-Mails oder Dokumente.
   - **Agentenstatus**: Die hochgeladenen Daten enthalten alle Aktivitäten von Agenten, die dein externes System aufgezeichnet hat. Dazu gehören Anmeldung, Abmeldung, Anruf bearbeiten, Nachbearbeitungszeit, Pause, etc.
4. Klicke auf _Erstelle ein neues CSV-Schema_{:.doc-button}.
5. Konfiguriere die CSV-Schema-Einstellungen. Dazu gehören:
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

1. Lade im Abschnitt **Einrichtung** eine Beispiel-CSV-Datei hoch, die dein externes System erzeugt hat. Dadurch kannst du sehen, wie injixo mit den Dateien deines Systems beim Import umgeht.
2. Konfiguriere die folgenden Parameter: Je nach Importdatentyp können sich die Parameter unterscheiden:<br><br>

   | Parameter                                                     | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Spaltentrennzeichen der CSV-Datei**                              | Trennzeichen, das in der hochgeladenen CSV-Datei verwendet wird, z.&nbsp;B. Semikolon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | **Zeitzone**                                                 | Zeitzone, in der dein externes System die Daten aufzeichnet, z.&nbsp;B. Amerika/Chicago (UTC-05:00).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | **Datenlayout**<br>(Nur für Kontaktdaten)                     | Das Datenlayout hängt davon ab, wie du deine CSV-Datei erstellt hast:<br>**Kontaktbasiert**: Für Datensätze mit Kontaktdaten, die eine Zeile für jeden einzelnen Kontakt enthalten. Da importierte kontaktbasierte Daten in 15-Minuten-Intervallen aggregiert werden, muss das Intervall der Planungseinheit ebenfalls 15&nbsp;Minuten sein. Neue Datenimporte überschreiben die Daten, die zuvor für das Intervall importiert wurden. Wenn deine Datei einen Zeitstempel mehrfach enthält, werden die Daten für das Intervall aufgerechnet.<br><br>**Intervallbasiert**: Für aggregierte Daten, die eine Zeile mit allen Kontaktinformationen pro Intervall enthalten. Wähle zusätzlich die korrekte Intervalllänge aus, die mit der deiner CSV-Datei übereinstimmt. Wenn du ein Intervall auswählst, das größer ist als die Intervalle der hochgeladenen Dateien, siehst du eine Fehlermeldung. Im umgekehrten Fall, d.&nbsp;h., wenn du ein 15-Minuten-Intervall auswählst für eine Datei mit größeren Intervallen (z.&nbsp;B. 30&nbsp;Minuten), wird jedes fehlende (hier: jedes zweite) Intervall mit 0 bzw. mit dem Text no data aufgefüllt. Dies hängt davon ab, welche Option du bei **Fehlende Werte in vorhandenen Intervallen behandeln** gewählt hast. |
   | **Fehlende Werte in vorhandenen Intervallen behandeln**<br>(Nur für Kontaktdaten) | Lege fest, wie fehlende Werte in der Ziel-Queue an anderen Stellen in injixo angezeigt werden sollen:<br>**Mit Null auffüllen**: Fehlende Werte werden mit einer Null ersetzt.<br>**Leer lassen**: Fehlende Werte werden mit folgendem Text ersetzt: no data.<br>**Leer lassen** eignet sich für die meisten Szenarien. injixo überschreibt bestehende Daten während des Imports.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

3. (Optional) Lege im Abschnitt **Vorverarbeitungsoptionen** eine oder mehrere Optionen fest, die für dein CSV-Dateiformat gelten:<br><br>

   | Vorverarbeitungsoption       | Beschreibung                                                                                                                                                                                             |
   | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Spaltenkopfzeile hinzufügen**         | Bei Dateien ohne Kopfzeile beschriftet injixo die Spalten mit A, B, C, usw. auf der [Spaltenzuordnungsseite](#spalten-zuordnen).                                                                        |
   | **Leere Zeilen überspringen**        | injixo ignoriert Zeilen, die nur Trennzeichen enthalten.                                                                                                                                                  |
   | **Überspringe die erste(n) Zeile(n)**        | injixo entfernt zusätzliche Zeilen am Anfang der Datei. Gib die Anzahl der Zeilen ein, die ignoriert werden sollen.                                                                                               |
   | **Überspringe die Zeile(n) mit** | injixo ignoriert Zeilen mit bestimmten Zeichen. Gib eine Zeichenfolge ein (Groß- und Kleinschreibung beachten). injixo ignoriert Zeilen mit dieser Zeichenfolge. Du kannst mehrere Zeichenfolgen hinzufügen, indem du auf _String hinzufügen_{:.doc-button} klickst. |

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

| Feld          | Beschreibung                                                                                                                                                                                                                                          | Erforderlich für intervallbasierte Daten | Erforderlich für kontaktbasierte Daten |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------: | :-----------------------------: |
| **Queue-Name** | Name der Queue, aus der die Daten stammen                                                                                                                                                                                                        |               Ja                |               Ja               |
| **Date**       | Datumswerte und verwendetes Format<br>Standardmäßig kannst du aus dem Dropdown-Menü das Datumsformat auswählen, das deinem CSV-Format entspricht. Um ein [benutzerdefiniertes Datumsformat](#benutzerdefiniertes-datumsformat) zu konfigurieren, klicke auf das {% icon gear %} und gib dein Format in das Textfeld ein. |               Ja                |               Ja               |
| **Time**       | Zeitwerte und verwendetes Format                                                                                                                                                                                                                          |               Ja                |               Ja               |
| **Zeitstempel**  | Zeitstempelwerte mit einem [benutzerdefinierten Zeitstempelformat](#benutzerdefiniertes-zeitstempelformat-mit-datum-und-uhrzeit)<br>Die Spalte erscheint, wenn du **Datum und Uhrzeit in einer Spalte** aktivierst.                                                                              |               Ja                |               Ja               |
| **Offered**    | Eingehende Kontakte (pro Intervall für intervallbasierte Daten)<br>Erlaubt ganze Zahlen oder Dezimalzahlen mit Punkt.                                                                                                                                            |               Ja                |               Ja               |
| **Angenommene**    | Beantwortete Kontakte (pro Intervall für intervallbasierte Daten)<br>Erlaubt ganze Zahlen und Dezimalzahlen mit Punkt.<br>Für kontaktbasierte Daten kann der Wert für bearbeitete Kontakte nur 0 oder 1 (oder Dezimalzahlen) sein.                                              |               Ja                |               Ja               |
| **AHT**        | Durchschnittliche Bearbeitungszeit pro Intervall<br> Unterstützte Formate sind Sekunden (ganze Zahl) oder hh:mm:ss (z.&nbsp;B. 00:05:00).<br>Wenn keine AHT-Spalte vorhanden ist, wähle **Keine Spalte**.<br>Das Feld wird nur für intervallbasierte Daten angezeigt.                           |                Nein                |               Nein                |
| **Dauer**   | Aufgezeichnete Dauer in Sekunden (ganze Zahl).<br>Das Feld wird nur für kontaktbasierte Daten angezeigt.                                                                                                                                             |                Nein                |               Ja               |
| **Kanal**    | Fester Kanalname (erstes Dropdown-Menü) oder auswählbare Spalte, die den Kanalnamen enthält (zweites Dropdown-Menü)<br>Erlaubte Werte: calls, emails, chats, documents, cases, social_media                                                           |               Ja                |               Ja               |

Hinweis: Der Import von AHT für intervallbasierte Daten ist zwar technisch nicht notwendig, aber er ist entscheidend für die genaue Berechnung des Mitarbeiterbedarfs und für das Forecasting.

#### Agentenstatus Dropdown-Menüs

Wenn du **Agentenstatus** als Importdatentyp ausgewählt hast, zeigt die Spaltenzuordnungsseite in der Standardansicht folgende Elemente:

| Feld                   | Beschreibung                                                                                                                                                                                                                                                                          | Erforderlich |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| **Agentenkennung**    | Eindeutiger Bezeichner für den Agenten, z. B. ID oder Name                                                                                                                                                                                                                                     | Ja      |
| **Aktivitätskennung** | Aktivität, an der der Agent gerade arbeitet                                                                                                                                                                                                                                                     | Ja      |
| **Startdatum**          | Datum, an dem der Agent die Aktivität begonnen hat<br>Standardmäßig kannst du aus dem Dropdown-Menü das Datumsformat auswählen, das dem Format deiner CSV-Datei entspricht. Um ein [benutzerdefiniertes Datumsformat](#benutzerdefiniertes-datumsformat) zu konfigurieren, klicke auf das {% icon gear %} und gib dein Format in das Textfeld ein.   | Ja      |
| **Startzeit**          | Zeitpunkt, zu dem der Agent die Aktivität begonnen hat                                                                                                                                                                                                                                         | Ja      |
| **Startzeitstempel**     | [Benutzerdefiniertes Zeitstempelformat](#benutzerdefiniertes-zeitstempelformat-mit-datum-und-uhrzeit) mit Datum und Uhrzeit, zu der der Agent die Aktivität begonnen hat<br>Die Spalte erscheint, wenn du **Datum und Uhrzeit in einer Spalte** aktivierst.                                                                 | Ja      |
| **Enddatum**            | Datum, an dem der Agent die Aktivität beendet hat<br>Wähle aus dem Dropdown-Menü das Datumsformat aus, das deinem Format entspricht. Um ein [benutzerdefiniertes Datumsformat](#benutzerdefiniertes-datumsformat) zu konfigurieren, klicke auf das {% icon gear %} und gib dein benutzerdefiniertes Format in das Textfeld ein. | Nein       |
| **Endzeit**            | Zeitpunkt, zu dem der Agent die Aktivität beendet hat                                                                                                                                                                                                                                         | Nein       |
| **Endzeitstempel**       | [Benutzerdefiniertes Zeitstempelformat](#benutzerdefiniertes-zeitstempelformat-mit-datum-und-uhrzeit) mit Datum und Uhrzeit, zu der der Agent die Aktivität beendet hat<br>Die Spalte erscheint, wenn du **Datum und Uhrzeit in einer Spalte** aktivierst.                                                                 | Nein       |

#### Benutzerdefiniertes Datumsformat

Lege ein benutzerdefiniertes Datumsformat fest, das mit dem Datum in deinen CSV-Dateien übereinstimmt. Benutze die folgenden Zeichen im Feld **Benutzerdefiniertes Datumsformat**:

- für den Tag: **D** (einstellige Ziffern 1-9) oder **DD** (mit führenden Nullen)
- für den Monat: **M** (einstellige Ziffern 1-9) oder **MM** (mit führenden Nullen)
- für das Jahr: **YY** oder **YYYY**

Alle anderen Zeichen werden als Trennzeichen interpretiert.

Beispiele:

| Date     | Benutzerdefiniertes Datumsformat |
| -------- | ------------------ |
| 13/1,22  | D/M,YY             |
| 010122   | DDMMYY             |
| 13012022 | DDMMYYYY           |

#### Benutzerdefiniertes Zeitstempelformat mit Datum und Uhrzeit

Um ein benutzerdefiniertes Format für einen Zeitstempel hinzuzufügen, aktiviere die Option **Datum und Uhrzeit in einer Spalte**.
Zusätzlich zum [benutzerdefinierten Datumsformat](#benutzerdefiniertes-datumsformat) musst du das Zeitformat festlegen (mit Kleinbuchstaben):

- für Stunden: **h** (einstellige Ziffern 1-9) oder **hh** (mit führenden Nullen)
- für Minuten: **m** (einstellige Ziffern 1-9) oder **mm** (mit führenden Nullen)
- (optional) für Sekunden: **s** (einstellige Ziffern 1-9) oder **ss** (mit führenden Nullen)

Beispiele:

| Datum und Uhrzeit  | Zeitstempelformat |
| -------------- | ---------------- |
| 13/1,22 9:15:8 | D/M,YY h:m:s     |
| 010122 09-15   | DDMMYY hh:mm     |

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

> Je nach [WFM-Plan](https://www.injixo.com/de/pricing/) kann es sein, dass dir nicht alle Kanäle für die injixo Quell-Queue zur Verfügung stehen.

| Spaltenname | Datentyp | Erforderlich | Erläuterung                                                                                                                                                                                                  |
| ----------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| queue       | String    | Ja      | Bezeichnung für die Queue                                                                                                                                                                                 |
| timestamp   | Datetime  | Ja      | Start des Intervalls im Format YYYY-MM-DD hh:mm:ss                                                                                                                                                  |
| offered     | Integer   | Ja      | Anzahl Kontakte (z.&nbsp;B. Anrufe oder E-Mails) im Intervall                                                                                                                                                 |
| answered    | Integer   | Ja      | Intervallbasiert: Anzahl der Kontakte, die im Intervall bearbeitet wurden.<br>Kontaktbasiert: Der Wert 1 bedeutet, dass der Kontakt bearbeitet wurde. Der Wert 0 bedeutet, dass der Kontakt nicht bearbeitet wurde. |
| aht         | Float     | Nein       | Durchschnittliche Bearbeitungszeit für alle Kontakte im Intervall                                                                                                                                                   |
| duration    | Integer   | Ja      | Gesamtbearbeitungszeit eines einzelnen Kontakts                                                                                                                                                                  |
| channel     | String    | Ja      | Bezeichnung für den Kanal der injixo Quell-Queue<br>Gültige Werte: calls, chats, emails, social_media, documents, cases                                                                            |

#### Einfache Beispielabfragen

Intervallbasierte Kontaktdaten:

```sql
SELECT
   queue, timestamp,
   offered, handled, aht,
   channel
FROM uploaded_file
```

Kontaktbasierte Kontaktdaten:

```sql
SELECT
   queue, timestamp,
   offered, handled, duration,
   channel
FROM uploaded_file
```

Die folgenden erweiterten Beispiele zeigen, wie du mit mathematischen Operationen und SQLite-Funktionen arbeiten kannst.

#### Erweiterte Beispielabfrage 1

- Teile HandleTime durch HandledCalls, um die durchschnittliche Bearbeitungszeit (AHT) zu erhalten.
- Kombiniere Date und Time mit SUBSTR, um das Zeitstempelformat YYYY-MM-DD HH:MM:SS zu erhalten.

|   Queue    |    Date    | Time  | Received | HandledCalls | Aband | HandleTime | HoldTime |
| :--------: | :--------: | :---: | :------: | :----------: | :---: | :--------: | :------: |
| test queue | 06/03/2023 | 07:30 |    5     |      5       |   -   |   1324.6   |    -     |
| test queue | 06/03/2023 | 08:00 |    2     |      2       |   -   |    1548    |    -     |

```
SELECT
  Queue as queue,
  SUBSTR(Date, 7, 4) || '-'|| SUBSTR(Date, 1, 2) || '-' || SUBSTR(Date, 4,2) || ' ' || Time || ':00' as timestamp,
  Received as offered,
  HandledCalls as handled,
  HandleTime/HandledCalls as aht,
  'chats' as channel
FROM uploaded_file
```

#### Erweiterte Beispielabfrage 2

- Verwende `date('now')` von SQLite, um das aktuelle Datum abzurufen und es mit der Zeit aus der Datei zu kombinieren.
- Entferne Dezimalstellen und wandle sie in Ganzzahlen um.
- Kombiniere Date und Time mit SUBSTR, um das Zeitstempelformat YYYY-MM-DD HH:MM:SS zu erhalten.

In diesem Beispiel enthalten die Spaltenüberschriften Leerzeichen.

| Queue Name | Hour in hh:mm | Offered Calls | Handled Calls | Average Handling Time |
| :--------: | :-----------: | :-----------: | :-----------: | :-------------------: |
| demo queue |     07:00     |      3.4      |      2.9      |       00:05:30        |
| demo queue |     08:30     |      5.7      |      5.2      |       00:10:15        |

Du kannst die Kopfzeile mit den Vorverarbeitungsoptionen der Integration ersetzen:

- Überspringe die ersten 1 Zeile(n): Entfernt die ursprüngliche Kopfzeile
- Spaltenkopfzeile hinzufügen: Fügt Spaltenkopfzeilen mit Buchstaben hinzu

```
 SELECT
   A as queue,
   DATE('now')||' '|| "B"||':00' as timestamp,
   FLOOR(C) as offered,
   FLOOR (D) as handled,
   (CAST(substr(E, 1, 1) AS INTEGER) * 3600) +
   (CAST(substr(E, 3, 2) AS INTEGER) * 60) +
   CAST(substr(E, 6, 2) AS INTEGER) as aht,
   'calls' as channel
FROM uploaded_file
```

Wenn du die Kopfzeile nicht ersetzt, setze die tatsächlichen Spaltennamen in doppelte Anführungszeichen:

```
 SELECT
   "Queue Name" as queue,
   DATE('now')||' '|| "Hour in hh:mm"||':00' as timestamp,
   FLOOR("Offered Calls") as offered,
   FLOOR ("Handled Calls") as handled,
   (CAST(substr("Average Handling Time", 1, 1) AS INTEGER) * 3600) +
   (CAST(substr("Average Handling Time", 3, 2) AS INTEGER) * 60) +
   CAST(substr("Average Handling Time", 6, 2) AS INTEGER) as aht,
   'calls' as channel
FROM uploaded_file
```

#### Erweiterte Beispielabfrage 3

- Berechne die angenommenen Anrufe, indem du AbandonedCalls von OfferedCalls abziehst.
- Wandle den speziell formatierten String Start in das erforderliche Zeitstempelformat YYYY-MM-DD HH:MM:SS um.

|  Name  |       Start       | OfferedCalls | AbandonedCalls | AverageHandlingTime |
| :----: | :---------------: | :----------: | :------------: | :-----------------: |
| queue1 | 20230613 15:30:00 |      10      |       2        |         300         |
| queue2 | 20230613 15:35:00 |      15      |       3        |         450         |
| queue3 | 20230613 15:40:00 |      12      |       2        |         350         |

<!-- notes for database integrations -->
<!-- In this example, the date time format in the Start column is not supported by built-in SQLite `datetime()` and `strftime()` functions. You need to change the string first. -->
<!-- changed the example from datetime(substr(Start, 1, 4) || '-' || to substr(Start, 1, 4) || '-' || -->
<!-- `datetime` is not required here, but in database integrations it would be needed due to the reqiured datetime datatype in the table around line 210 -->

```
SELECT
  Name as queue,
    substr(Start, 1, 4) || '-' ||
    substr(Start, 5, 2) || '-' ||
    substr(Start, 7, 2) || ' ' ||
    substr(Start, 10, 8) as timestamp,
  Offered as offered,
  (Offered - Abandoned) as handled,
  AverageHandlingTime as aht,
  'calls' as channel
FROM uploaded_file
```

#### Erweiterte Beispielabfrage 4

In kontaktbasierten Datensätzen gibt es oft keine Spalte mit der Anzahl der eingehenden und bearbeiteten Anrufe. Stattdessen siehst du Boolesche Werte für den Kontakttyp:

|      Queue       |   DateTimeISO8601   | Offered | Answered | Duration |
| :--------------: | :-----------------: | :-----: | :------: | :------: |
| My Inbound Queue | 2023-01-01T22:59:00 |  true   |   true   |   100    |
| My Inbound Queue | 2023-01-01T23:59:00 |  true   |  false   |   100    |

- Verwende ein CASE Statement für kontaktbasierte Daten mit Booleschen Werten für eingehende und bearbeitete Anrufe.
- Wandle ein Datum, das nach ISO8601 formatiert ist, in das erforderliche Format YYYY-MM-DD HH:MM:SS um.

```
SELECT
   "Queue" as queue,
   substr("DateTimeISO8601", 1, 10) || ' ' || substr("DateTimeISO8601", 12, 8) as timestamp,
   (CASE WHEN "Offered" = 'true' THEN 1 ELSE 0 END) as offered,
   (CASE WHEN "Answered" = 'true' THEN 1 ELSE 0 END) as handled,
   "Duration" as duration,
   'calls' as channel
FROM uploaded_file
```

Diese Abfrage funktioniert auch für echte ISO8601-Zeitstempel, wie Daten in UTC (2023-01-01T22:59:00Z) oder Zeitstempeln mit der Verschiebung deiner Zeitzone (2023-01-01T22:59:00+02:00).

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

| Spalte      | Zugeordnete Spalte/Werte |
| ----------- | ------------------- |
| Queue-Name  | Queue               |
| Datum        | Date                |
| Datumsformat | dd/mm/yyyy          |
| Zeit        | Time                |
| Zeitformat | hh:mm               |
| Eingehende     | IncomingCalls       |
| Angenommene     | AnsweredCalls       |
| AHT         | AHT                 |
| AHT-Format  | Seconds             |

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

| Spalte      | Zugeordnete Spalte/Werte |
| ----------- | ------------------- |
| Queue-Name  | Queue               |
| Datum        | Date                |
| Datumsformat | dd/mm/yyyy          |
| Zeit        | Time                |
| Zeitformat | hh:mm               |
| Eingehende     | Offered             |
| Angenommene     | Answered            |
| Dauer    | Duration            |

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

| Spalte              | Zugeordnete Spalte/Werte |
| ------------------- | ------------------- |
| Agentenkennung    | AgentID             |
| Aktivitätskennung | AgentActivityID     |
| Startdatum          | StartDate           |
| Datumsformat         | yyyy-mm-dd          |
| Startzeit          | StartTime           |
| Zeitformat         | hh:mm:ss            |

## CSV-Dateien importieren

Sobald du deine CSV-Integration gespeichert hast, kannst du CSV-Dateien importieren.
Folgende Dateikodierungen werden unterstützt:

- UTF-8
- ISO-8859-1/Latin-1
- ISO-8859-9
- Windows-1252

Nutze UTF-8, um generische Fehlermeldungen zu vermeiden.

### Automatischer Datenimport

[Konfiguriere eine CSV-Integration](#neue-csv-integration-konfigurieren) und verbinde injixo Cloud Link. injixo Cloud Link lädt dann neue Daten in injixo hoch. Automatisch beginnt jedes Mal ein neuer Upload, wenn du eine neue CSV-Datei im injixo Cloud-Link-Installationsverzeichnis speicherst. Du kannst das Standardinstallationsverzeichnis (C:\\Program Files\\injixo Cloud Link) während der Installation ändern.

Alternativ kannst du einen separaten {% link_new Importordner | features/acd-integration/cloud/install-cloud-link.md | #importordner-konfigurieren %} für Datei-Uploads konfigurieren. Speichere die neuen Dateien stattdessen im Importordner.

Wenn die Daten hochgeladen wurden, kannst du in Forecast {% link_new einem Workload neue Queues hinzufügen | features/forecast/injixo-forecast/manage-workloads.md %} bzw. siehst du die aktualisierten Daten in deinen bestehenden Workloads. Wenn keine Daten hochgeladen wurden, nutze den im folgenden beschriebenen manuellen Datenimport, um festzustellen, ob dein Dateiformat gültig ist.

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

| Frage                                                                  | Antwort                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kann ich die gleiche Datei zweimal importieren?                                         | Ja, wenn du Daten manuell importierst. Nein, wenn du Cloud Link benutzt. Um doppelte Dateien zu erkennen, berechnet injixo während des Imports Prüfsummen. Importierte Dateien mit der gleichen Prüfsumme werden nicht erneut importiert. Wenn die Datei den gleichen Namen, aber einen anderen Inhalt hat, wird sie trotzdem importiert. |
| Löscht injixo automatisch importierte CSV-Dateien nach dem Import? | Nein. Importierte Dateien bleiben im injixo Cloud Link Client-Verzeichnis. Du kannst sie manuell löschen oder selbst eine wiederkehrende Aufgabe einrichten.                                                                                                                                              |
| Kann ich eine CSV-Datei importieren, die zukünftige Daten enthält?                        | Ja, das ist möglich. Beachte aber, dass injixo zukünftige Daten nicht überspringt, sondern sie als historische Daten speichert. Du kannst trotzdem einen Forecast berechnen, aber die Diagramme für Historie und Forecast überschneiden sich.                                               |
