---
title: Configure ODBC interfaces
product_label:
  - on-premise
description: Configure Xlink to connect to a database via ODBC to import contact and agent status data.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-mapping-telephony.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-mapping-activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-import-mode.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-log-files.md
  - overwrite_title: Add title for untranslated source
    filepath: support/faq/xlink-frequent-error-messages.md
---

In this article, you will learn how to configure different Xlink ODBC interfaces to import data from database tables or database views into injixo.

Xlink offers various standard interfaces with a fixed logic and the configurable Universal Interface.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

## Requirements

To be able to configure an ODBC interface, you need a proper {% link_new Xlink installation | features/acd-integration/xlink-installation-configuration.md %} and an {% link_new external system for an ODBC interface | features/acd-integration/new-external-system.md %}, e.g. Avaya CMS, Bosch BCC (Avaya CIE) or the Universal interface /(example for Avaya Aura below).

For the connection, you also need a working 32-bit ODBC connection created as a _System DSN_ under _c:\Windows\SysWOW64\\odbcad32.exe_ that is accessible by the user configured in the Xlink service. Note: Do not create a 64-bit ODBC connection by accident and make sure you don't have a User DSN with the same name.

Request any special ODBC drivers which could be required for the connection from your ACD manufacturer. The user which connects to the database needs read access to the tables or views used by the interface.

## Configure a standard interface

1. Double-click the file **isps_ul.exe** to open the Xlink user interface.
2. Right-click the configured _external system_ on the left and select _configuration_{:.menu-item} to open the configuration dialog.
3. Enter the **ODBC connection name**, the database user and the password.
4. Click _Ok_{:.doc-button} to save the settings.

After you have performed these steps, the corresponding configuration section is created in the configuration file _isps_ul.ini_.

The left side of the Xlink application shows a tree structure under the external system if the connection was successful. If not, check the content of the file _call_tree.log_.

## Configure the Universal interface

The Universal interface supports the following database systems: Oracle, Microsoft SQL Server, MySQL, Caché DBMS, Microsoft Access, Informix, and PostgreSQL.

The Universal Interface parameters for call and agent status import are described in the documentation available at [downloads.injixo.com](https://downloads.injixo.com).

This is how you create the initial configuration:

1. Double-click the file **isps_ul.exe** to open the Xlink user interface.
2. Right-click the configured _external system_ on the left and select _configuration_{:.menu-item} to open the configuration dialog.
3. Enter the **ODBC connection name**, the **database user** and the **password**.
4. Click _Ok_{:.doc-button} to save the settings.
5. Open the configuration file **isps_ul.ini** and add the following lines to the existing section _[your external system name]_:

   ```
   QueueSQL = select queue_name from queue_table order by queue_name
   ValueTypes = valuetype_1;valuetype_2;valuetype_3
   TimeStampColumn = start_date_column
   QueueNameColumn = queue_name_column
   CallDataTable = source_table_name

   ActivitySQL = SELECT DISTINCT activiy_name_column, activity_ID_column FROM source table
   ActivityTimeSpanType = 1 ;(start and end time only)
   ActivityColumn = activity_name_column
   AgentColumn = agent_login_id_column
   ActivityStartTimeStampColumn = start_time_column
   ActivityStartTimeStampType = 2 ;(date/time field)
   ActivityEndTimeStampColumn = end_time_column
   ActivityEndTimeStampType = 2 ;(date/time field)
   AgentActivityTable = source table name
   ```

6. Adapt the individual columns and table or view names to your source database. The example above is for illustration only. You must replace the values for the database fields for **queue_name**, **queue_table**, **valuetype\_\***, **start_date_column**, **queue_name_column** and **source_table_name** with the corresponding source database or table. The same applies to the fields of the **Activity\* parameters**.
7. Change the value for the _Protocol_ parameter from 0 to 1.
8. Save the change to the file.
9. Restart the **ISPS XLink** service.
10. Reopen the **isps_ul.exe**.

After you have performed these steps, the corresponding configuration section is created in the configuration file _isps_ul.ini_.

The left side of the Xlink application shows a tree structure under the external system if the connection was successful. If not, check the content of the file _call_tree.log_ for SQL errors.

### Customize the Universal interface configuration

To be able to configure the Universal interface, you need to know the structure or columns and the data types in the table from which the data is read.

You can customize the PhoneLink and TimeLink parameters according to your needs. Information about the parameters can be found in the documentation available at [downloads.injixo.com](https://downloads.injixo.com).

Some additional useful tips:

For the _ActivitySQL_ parameter, Xlink needs both the name and the ID of the activity in the ACD, e.g. _SELECT DISTINCT activiy_name_column, activity_ID_column FROM source_table_. If you ask only the name, the import will not work later. Only activity 0 will appear in the log file.

_ActivityStartTimeStampType_ and _ActivityEndTimeStampType_ define how date and time are interpreted, by default as date/time field (value 2); other possible values are 0 (character string) or 1 (Unix timestamp). If the date is a character string, use value 0 and additionally the parameters _ActivityStartTimeStampFormat_ and _ActivityEndTimeStampFormat_.

_ActivityStartTimeStampColumn_ defines the column containing the start time of an activity to be imported. Depending on what information your database holds, use additionally:

- _ActivityDurationColumn_ and _ActivityTimeSpanType=0_ for the
  the import with start time and duration.
- _ActivityEndTimeStampColumn_ and _ActivityTimeSpanType=1_ for the import with start time and end time.
  _ActivityTimeSpanType=2_ and _LogOffActivities_ for import with start time only. The activity is automatically stopped when a new activity starts. _LogOffActivities_ defines (via a semicolon-separated list of IDs) the activities from the ACD that represent a logout.

### PhoneLink Universal interface example for Avaya Aura

1. Double-click the file **isps_ul.exe** to open the Xlink user interface.
2. Right-click the configured _external system_ on the left and select _configuration_{:.menu-item} to open the configuration dialog.
3. Enter the **ODBC connection name**, the **database user** and the **password**.
4. Click _Ok_{:.doc-button} to save the settings.
5. Open the configuration file **isps_ul.ini** and the following lines to the section _[external system name]_:

   ```
   QueueSQL=select Name from Application order by Name
   QueueMappingSQL=select Name, ApplicationID from Application order by Name
   ValueTypes=CallsOffered;TalkTime;WaitTime;PostCallProcessingTime;CallsAnswered
   TimeStampColumn=""Timestamp""""
   TimeStampType=2
   QueueNameColumn=ApplicationID
   QueueNameType=1
   RetrieveValueTypesUsing=1
   CallDataTable=iApplicationStat
   ```

6. Save your changes.
7. Restart the **ISPS Xlink** service.
8. Open _isps_ul.exe_ again. A tree structure under the configured external system on the left shows queues and value types. If not, check the database connection and the log files.

<!-- misplaced -->
<!-- No tree structure is displayed for TimeLink, check in the Xlink interface under *View > Activities*{:.breadcrumbs} which activities from the external system have been assigned to the injixo activities. -->

Create mappings between your ACD and injixo to import specific data. Check the log files for possible SQL errors caused by an incorrect configuration. Adjust the configuration, restart the service, and run multiple imports to fix all errors and ensure the correct data import.
