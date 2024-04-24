---
title: Migrate your database to unicode
product_label:
  - on-premise
description: Learn how to migrate your injixo Enterprise on-premise database to Unicode encoding (utf-16).
---

As of build 9001, Unicode encoding of the database is mandatory. Also older injixo versions may already use Unicode. Check your database encoding before an update and convert the database from ANSI to Unicode if necessary.

## Check database encoding

Run the following SQL statement on your database:

`SELECT vs_version_no, encoding FROM vs_version;`

If the result is `utf-8` or `utf-16`, you are already using Unicode. If an ISO character set appears, e.g. `ISO-8859-1`, migrate the database.

> Important: To avoid losing production data, create a backup before migrating data.

## Preparation

Download the [database scripts](https://downloads.injixo.com/_downloads/db-scripts-and-tools/injixo%20Enterprise%20DB%20scripts.zip). The folder contains all available scripts. You can find out which scripts you need to use below.

### ## Migrate Microsoft SQL Server databases in-place

The in-place migration in SQL Server changes all the _VARCHAR_ fields to _NVARCHAR_ fields:

1. Stop the injixo/InVision services.
2. Run the following script: **mssql/migration/conv_unicode_306.sql**.
3. Restart the services.

### Oracle: Character Set Migration by Export/Import

You can use the Oracle programs exp/expdp or imp/impdb for character set conversion. The import utilities automatically perform the necessary conversions.

> Oracle: Is your National Character Set AL16UTF16?
>
> You will need a new database if the current database does not use AL16UTF16 as National Character Set. This is how you check the National Character Set of your database:  
> `select * from nls_database_parameters where parameter='NLS_CHARACTERSET' or parameter 'NLS_NCHAR_CHARACTERSET';`

This is how you perform the data conversion:

1. Stop the injixo/InVision services.
2. Export your current database using the Oracle export utility (exp/expdp), for example:
   `expdp system/password@db schemas=ISPS directory=TEST_DIR dumpfile=scott_data.dmp logfile=expdp.log content=DATA_ONLY`
3. Create a new Oracle schema, e.g. ISPS2.
4. Run the following script to create the required injixo tables in the new schema: **oracle/create/create-tables.sql**.
5. Import the exported database into the new database using Oracle's impdp, for example:  
   `impdp ISPS2/tiger@db10g schemas=SCOTT directory=TEST_DIR dumpfile=SCOTT.dmp logfile=impdp.log IGNORE=Y`
6. Run the following script for the new schema (ISPS2): `update vs_version set encoding='utf-16';`
7. Restart the services.

<!--

## Use the DBMigrate tool

Using the ODBC drivers installed on your Windows server, DBMigrate can convert an injixo database into the correct Unicode format. It creates tables in the destination database. You can also use DBMigrate to switch your database system.

Note: Depending on the size of the database, this conversion may take several hours.

1. Download [DBMigrate](https://downloads.injixo.com/en#scripts-tools-on-premise).
2. Extract the archive to any folder on the server.
3. Start DBMigrate from a Windows command line.

   Type `dbmigrate --help` to see an example and available options:

   | Parameter | Details                                                                                                                 |
   | --------- | ----------------------------------------------------------------------------------------------------------------------- |
   | --src     | ODBC connection string for the source database                                                                          |
   | --dest    | ODBC connection string for the target database                                                                          |
   | --limit   | Date (m/d/Y) for deleting transaction data (optional),<br> not to be restricted if all data should be kept.             |
   | --history | Number of remaining history layers for scheduling data (optional), <br> not to be limited if no data should be deleted. |

4. Recreate the old tables _sc_user_ and _sc_access_ in the source database. The tables may have already been removed by previous scripts. Use the following scripts:

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

5. Create the new destination database. In Oracle, you may need a new database with an _AL16UTF16_ character set. In Microsoft SQL Server, you can create a new database in the existing instance.

6. Run DBMigrate using the right connection strings to connect to the source database (Parameter --src) and destination database (Parameter --dest), for example:

   **Driver=**

   ```
   dbmigrate.exe --src "DRIVER={SQL Server};SERVER=<server name>\<instance name>;DATABASE=iwfm_db;UID=username;PWD=password"
   --dest "DRIVER={SQL Server};SERVER=<server name>\<instance name>;DATABASE=<database>;UID=<user name>;PWD=<password>"
   ```

   **DSN=**

   ````
   dbmigrate.exe --src "DSN=iwfm_old_ansi;UID=<user name>;PWD=<password>"
   --dest "DSN=new_unicode;UID=username;PWD=password"
   ```
-->

## Change database connection

After the successful Unicode conversion, you may need to connect your Enterprise Server to the new database/schema. To do this, modify the connection string in the **[InVision General Model Settings]** section of the **isps.cfg** file in the installation directory.

```

```
