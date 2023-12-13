---
title: Datenbank in Unicode konvertieren
description: Ab Build 9001 ist eine Unicode-Kodierung der Datenbank zwingend erforderlich. Prüfe deine Datenbank-Kodierung vor einem Update und migriere ggf. die Datenbank.
product_label:
  - on-premise
---

Ab Build 9001 ist eine Unicode-Kodierung der Datenbank zwingend erforderlich. Auch ältere injixo Versionen verwenden eventuell bereits Unicode. Prüfe deine Datenbank-Kodierung vor einem Update und konvertiere ggf. die Datenbank von ANSI nach Unicode.

## Datenbank-Kodierung prüfen

Führe folgendes SQL-Statement auf deiner Datenbank aus:

`SELECT vs_version_no, encoding FROM vs_version;`

Ist das Ergebnis `utf-8` oder `utf-16`, nutzt du bereits Unicode. Erscheint ein ISO-Zeichensatz, z.&nbsp;B. `ISO-8859-1`, migriere die Datenbank.

> Wichtig: Um den Verlust von Produktionsdaten zu vermeiden, erstelle vor der Datenmigration ein Backup.

## Vorbereitung

Lade die [Datenbank-Skripte](https://downloads.injixo.com/_downloads/db-scripts-and-tools/injixo%20Enterprise%20DB%20scripts.zip) herunter. Der Ordner enthält alle verfügbaren Skripte. Du erfährst unterhalb, welche Skripte Du nutzen musst.

## Microsoft SQL Server-Datenbanken in-place migrieren

Die in-place Migration im SQL-Server ändert alle alle _VARCHAR_-Felder in _NVARCHAR_-Felder:

1. Stoppe die injixo/InVision-Dienste.
2. Führe folgendes Skript aus: **mssql/migration/conv_unicode_306.sql**
3. Starte die Dienste neu.

## Oracle-Datenbanken mit Export/Import migrieren

Du kannst die Oracle-Programme exp/expdp bzw. imp/impdb für die Zeichensatz-Konvertierung nutzen. Die Import-Utilities führen automatisch die erforderlichen Konvertierungen durch.

> Oracle: Ist dein National Character Set AL16UTF16?
>
> Du benötigst eine neue Datenbank, wenn die aktuelle Datenbank nicht AL16UTF16 als National Character Set verwendet. So prüfst du das National Character Set deiner Datenbank:  
> `select * from nls_database_parameters where parameter='NLS_CHARACTERSET' or parameter 'NLS_NCHAR_CHARACTERSET';`

So führst Du die Datenkonvertierung durch:

1. Stoppe die injixo/InVision-Dienste.
2. Exportiere deine aktuelle Datenbank mit dem Oracle's expdp, z. B.:  
   `expdp system/password@db schemas=ISPS directory=TEST_DIR dumpfile=scott_data.dmp logfile=expdp.log content=DATA_ONLY`
3. Erzeuge eine neues Oracle-Schema, z.&nbsp;B. ISPS2.
4. Führe folgendes Skript aus, um die benötigten injixo-Tabellen im neuen Schema zu erstellen: **oracle/create/create-tables.sql**
5. Importiere die exportiere Datenbank mit Oracle's impdp in die neue Datenbank, z. B.:  
   `impdp ISPS2/tiger@db10g schemas=SCOTT directory=TEST_DIR dumpfile=SCOTT.dmp logfile=impdp.log IGNORE=Y`
6. Führe folgendes Skript für das neue Schema (ISPS2) aus: `update vs_version set encoding='utf-16';`
7. Starte die injixo/InVision-Dienste neu.

<!-- ## Datenbanken mit dem DBMigrate-Tool migrieren

Das DBMigrate-Tool kann mit installierten ODBC-Treibern eine injixo-Datenbank konvertieren. DBMigrate erstellt die benötigten Tabellen in der Zieldatenbank.

> Je nach Größe der Datenbank kann diese Konvertierung mehrere Stunden dauern. -->

<!-- ### DBMigrate herunterladen und testen

1. Lade [DBMigrate](https://downloads.injixo.com/de#skripte-tools-on-premise) herunter und entpacke das Archiv in einen beliebigen Ordner auf dem Server.
2. Gib in einer Windows-Kommandozeile `dbmigrate --help` ein.
   Du siehst die verfügbaren Parameter (und ein Beispiel):

   | Parameter | Erläuterung                                                                                                                           |
   | --------- | ------------------------------------------------------------------------------------------------------------------------------------- |
   | --src     | ODBC Connection String für die Quell-Datenbank                                                                                        |
   | --dest    | ODBC Connection String für die Ziel-Datenbank                                                                                         |
   | --limit   | Datum (m/d/Y) für die Löschung von Bewegungsdaten (optional),<br> nicht einzuschränken, wenn keine Daten gelöscht werden sollen.      |
   | --history | Anzahl der verbleibenden Verlaufsstände für Plandaten (optional), <br> nicht einzuschränken, wenn keine Daten gelöscht werden sollen. | -->

<!-- ### Zieldatenbank erstellen

Damit DBMigrate die Daten migrieren kann, benötigst du eine neue Zieldatenbank:

- Oracle: Erstelle ein neues Schema in einer Datenbank mit dem _AL16UTF16_ Zeichensatz.
- Microsoft SQL Server: Erstelle eine neue Datenbank im aktuellen SQL Server. -->

<!-- ### Alte Tabellen in der Quelldatenbank erstellen

Damit DBMigrate funktioniert, musst du zwei alte Tabellen (sc_user und sc_access) in deiner aktuellen (Quell-)Datenbank erstellen:

**Oracle:**

```
CREATE TABLE sc_user
(
   sc_user_id  NUMBER(11,0) NOT NULL,
   is_deleted  NUMBER(1,0) NOT NULL,
   name  VARCHAR2(50) NOT NULL,
   pwd VARCHAR2(25) NOT NULL,
   key_type  NUMBER(11,0) NOT NULL,
   key_id  NUMBER(11,0) NOT NULL,
   num_badlogon  NUMBER(11,0) NOT NULL
);

CREATE TABLE sc_access
(
   sc_access_id  NUMBER(11,0) NOT NULL,
   sc_user_id  NUMBER(11,0) NOT NULL,
   sc_item_type_id NUMBER(11,0) NOT NULL,
   sc_item_id  NUMBER(11,0) NOT NULL,
   access_right  NUMBER(11,0) NOT NULL
);
```

**Microsoft SQL:**

```
CREATE TABLE sc_user
(
   sc_user_id  INT NOT NULL,
   is_deleted  BIT NOT NULL,
   name  NVARCHAR(50) NOT NULL,
   pwd NVARCHAR(25) NOT NULL,
   key_type  INT NOT NULL,
   key_id  INT NOT NULL,
   num_badlogon  INT NOT NULL
);

CREATE TABLE sc_access
(
   sc_access_id  INT NOT NULL,
   sc_user_id  INT NOT NULL,
   sc_item_type_id INT NOT NULL,
   sc_item_id  INT NOT NULL,
   access_right  INT NOT NULL
);
```

### DBMigrate ausführen

1. Führe DBMigrate mit Connection Strings für die Quell- und Zieldatenbank aus (Parameter `--src` und `--dest`):

   | Beispiel               | Befehl                                                                                                                                                                                                                                                                                     |
   | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | SQL Server             | `dbmigrate.exe --src "DRIVER={SQL Server};SERVER=<Servername>\<Instanzname>;DATABASE=iwfm_db;UID=Benutzername;PWD=Passwort" --dest "DRIVER={SQL Server};SERVER=<Servername>\<Instanzname>;DATABASE=<Datenbank>;UID=<Benutzername>;PWD=<Passwort>"`                                         |
   | Oracle                 | `dbmigrate. exe --src "Driver={Oracle in OraClient19Home1};dbq=<Servername>:<PORT>/<Instanzname>;Uid=<Benutzername>;Pwd=XXX;FWC=T;EXC=T;LOB=T;" --dest "Driver={Oracle in OraClient19Home1};dbq=<Servername neu>: <PORT>/<Instanzname neu>;Uid=<Benutzername>;Pwd=XXX;FWC=T;EXC=T;LOB=T;"` |
   | ODBC-Datenquelle (DSN) | `dbmigrate.exe --src "DSN=iwfm_old_ansi_database;UID=<Benutzername> PWD=<Passwort>" --dest "DSN=new_unicode_database;UID=Benutzername;PWD=Passwort"`                                                                                                                                       |

> Hinweise
>
> - In Connection Strings kannst Du die Option `Driver=` oder `DSN=` verwenden. DSN benötigt zusätzlich eine ODBC-Verbindung.
> - Um zusätzlich dein Datenbanksystem zu wechseln, kannst verschiedene Datenbanksysteme als Quelle (`--src`) und Ziel (`--dest`) verwenden. -->

## Datenbank-Verbindung ändern

Nach der erfolgreichen Unicode-Konvertierung, musst du deinen Enterprise Server ggf. noch mit der neuen Datenbank/Schema verbinden. Passe dazu im Installationsverzeichnis in der Datei **isps.cfg** den Connection String im Abschnitt **[InVision General Model Settings]** an.
