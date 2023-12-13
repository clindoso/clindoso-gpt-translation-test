---
title: Datenbank-Verbindung konfigurieren
product_label:
  - on-premise
promote-service: general
---

Die Verbindung zur Datenbank erfolgt in der Datei isps.cfg im Installationsverzeichnis auf dem Server. Konfiguriere sie im Abschnitt [InVision General Model Settings].

Der Datenbank-Benutzer benötigt mindestens folgende Rechte:

- Microsoft SQL: datareader, datawriter
- Oracle: connect, create, read, edit, delete
- PostgreSQL: connect, create, read, edit, delete

## Datenbank-Verbindung konfigurieren

Alte Versionen (kleiner r4.306) verwenden den Parameter DBServerName, neue Versionen DBConnectString. Beide Parameter können aufgrund früherer Updates parallel vorhanden sein, z.&nbsp;B.:

```
[InVision General Model Settings]
DBServerName = "Driver={SQL Server};
SERVER=myserver\test;DATABASE=iwfm;UID=sa;PWD=mypassword"
DBConnectString = "Driver={SQL Server};
SERVER=myserver\test;DATABASE=iwfm;UID=sa;PWD=mypassword"
```

Hinweis: Es können mehrere Abschnitte [InVision General Model Settings] existieren. Nicht genutzte Abschnitte sind meist durch Semikolon oder X auskommentiert.

## Beispiele für Connection Strings

Der Connection String ist abhängig vom Datenbanksystem. Die folgenden Beispiele nutzen Platzhalter (_<>_):

- Microsoft SQL

  ```
  DBConnectString = "Driver={SQL Server};
  SERVER=<Server Address>\<Instance Name>;DATABASE=<DB Schema Name>;UID=<User Name>;PWD=<Password>"
  ```

- Oracle Admin Client

  ```
  ;admin client
  DBConnectString = "DRIVER={Oracle in <Driver Name>};DBQ=<Oracle Alias>;UID=<User Name>;PWD=<Password>;FWC=T;EXC=T;LOB=T;"
  ```

- Oracle Instant Client

  ```
  DBConnectString	= "DRIVER=(Oracle in XEClient);<User Name>/<Password>@Host:Port/<TNS Name>"
  ```

- PostgreSQL
  ```
  DBConnectString = "Driver={PostgreSQL Unicode};Server=<Server Address>;Port=5432;Database=<DB Schema Name>;Uid=<User Name>;Pwd=<Password>;Encoding=UNICODE;TextAsLongVarchar=1;MaxLongVarcharSize=65536"
  ```

Der Wert für den Eintrag Driver entspricht dem Namen des installierten Windows-Treibers. Den korrekten Wert findest Du im 64-bit ODBC-Datenquellen-Administrator (odbcad32.exe) auf dem Tab Treiber:

{{ 1 | image: 'Dialog ODBC Data Source Administrator', '50%' }}

## Verbindungsprobleme beheben

Wenn die Datei ies64.log nach dem Start des Servers die folgende Fehlermeldung mit errorticket(21) anzeigt, werden SQL Server-Verbindungen mit einem X.509-Zertifikat verschlüsselt:

```
SSL Provider: [error:1416F086:SSL routines:tls_process_server_certificate:certificate verify failed:self signed certificate]
```

Du hast folgende Optionen auf dem injixo-Server:

- Füge den öffentlichen Schlüssel des X.509-Zertifikats vom Server als vertrauenswürdiges Zertifikat im Windows-Zertifikatspeicher hinzu.
- Füge die Option `TrustServerCertificate=yes;` zu deinem Connection String hinzu.

Erfahre auf [learn.microsoft.com](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/connect/error-message-when-you-connect), wie du ein Server-Zertifikat auf dem Datenbank-Client (IES) installierst.

<!--
If the ies64.log file displays the following message with error ticket(21) after starting the server, SQL Server connections are encrypted using an X.509 certificate:

```
SSL Provider: [error:1416F086:SSL routines:tls_process_server_certificate:certificate verify failed:self signed certificate]
```

You have the following options on the injixo server:
- Add the public key of the X.509 certificate from the server as a trusted certificate in the Windows certificate store.
- Add the `TrustServerCertificate=yes;` option to your connection string.

Learn how to add a server certificate on the database client (IES) at [learn.microsoft.com](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/connect/error-message-when-you-connect).
-->
