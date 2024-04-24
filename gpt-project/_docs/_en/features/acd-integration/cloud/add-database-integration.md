---
title: Add a database integration
navigation_title: Database
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Connect your database to injixo to import data.
redirect_from: /add-odbc-integration/
redirect_reason: renamed article in September 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## What is a database integration?

A database integration is a special type of on-premise integration. Use a database integration if your system cannot connect to a cloud or another on-premise integration.

You can define an SQL query to read data from a database. Database integrations use {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

## Add a database integration

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Universal Interfaces** tile, click _Select model_{:.doc-button}.
4. In the **Database** section, click _Add integration_{:.doc-button}.

## Set up your new database integration

1. Enter a unique name for the new integration that identifies the data source.
2. Install and connect {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Select your **Database type**.
4. Enter your credentials, depending on your selection.

   | Database type                                  | Credentials                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | MS&nbsp;SQL&nbsp;Server<br>MySQL<br>PostgreSQL | **Database name**<br>**Host**<br>**Port**: If you use a named instance on an MS SQL Server connection, do not enter a port. Instead, open UDP port 1434 in your firewall to ensure that the SQL Server browser service can determine the port for injixo Cloud Link.<br>**Username**<br>**Password**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | Other (ODBC)                                   | **Connection string**: Connection strings contain parameters required for the integration to connect your database server. You can find a connection string suitable for your database type and ODBC driver at [https://www.connectionstrings.com](https://www.connectionstrings.com).<br><br>Example for an InterSystem Caché database:<br>`DRIVER={InterSystemsODBC};SERVER=myServerAddress;` `PORT=12345;DATABASE=myDataBase;UID=myUsername;PWD=myPassword;` <br><br>SQL identifier in queries will be delimited by double quotes. Add additional options to the connection string if your ODBC driver does not support this by default, e.g. for Informix.<br><br>Example for an IBM Informix database:<br>`DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=myServerAddress;DATABASE=myDatabase;HOST=myHost;SERVICE=myService;UID=myUsername;PWD=myPassword;PROTOCOL=onsoctcp;DELIMIDENT=y;`<br><br>You can also create an ODBC datasource, in which you configure the driver, server, database, etc. This allows you to add the below DSN option as the connection string instead of including the connection details in the connection string. You still need to add the options that cannot be configured in the ODBC datasource, e.g. `DELIMIDENT=y`.<br><br>DSN examples:<br> `DSN=myODBCDatasourceName;`<br>`DSN=myODBCDatasourceName;DELIMIDENT=y;` |

## Configure your import data

1. In the **Configuration** section, select the type of import data that you want to import from your database:
   - **Contact-based** for historical contact data with one row for each contact
   - **Interval-based** for historical contact data which is aggregated into intervals of 15 or 30 minutes (set as Interval length)
   - **Agent status** for agent status data  
    By default, data is imported every 15 minutes but you can control the import behavior with two additional checkboxes:
        - **Import data in real time**: Data is imported every 10 seconds. Available in injixo Advanced and Enterprise WFM only.
        - **Data reconciliation**: Controls which time period of agent status data is imported every 15 minutes. Defaults to data from the last 24 hours.  

2. Select the **Database time zone** from the drop-down menu.
3. Enter the **SQL query** that will be used to import data from your database. Learn more about the [SQL Query](#sql-query).
4. To create the integration, click _Save integration_{:.doc-button}.  
   The integration starts importing data into injixo. The initial import can take a while.  
   All queues imported from the connected database will automatically be available on the {% link_new workload configuration screen | features/forecast/injixo-forecast/create-workloads.md | #create-workloads %} in injixo Forecast.  
   External activities will be available in the Present activity (ID 1). To import agent status data, you need to {% link_new map external user identifiers and activities | features/acd-integration/cloud/import-agent-status-data.md %}.

### Data reconciliation

Sometimes, it may be necessary to manually correct already imported agent status data. An example is when a team member forgot to clock out and you corrected the data in your database to show their actual working time.

By default, the **Data reconciliation** checkbox is activated. injixo re-imports all data

- from the last 24&nbsp;hours
- every 15&nbsp;minutes

You will always have access to the most updated data from the last 24 hours. Only changes to data that is older than 24 hours will not be included in the re-import.

Your database may struggle with the load of continuous data re-import. If you need to deactivate Data reconciliation, injixo only imports the newest data since the last successful import (typically data from the last 15&nbsp;minutes). In this case, you may need to manually update data in injixo that was imported more than 15&nbsp;minutes ago. If possible, keep the checkbox activated, because manual data updates cause significant extra work and can be prone to errors.

When you pause your integration for less than 24&nbsp;hours, injixo re-imports all data as soon as you re-start the integration. This applies regardless of whether the checkbox is checked or unchecked.  
When you pause the integration for a longer time period, all data that is older than 24&nbsp;hours will not be re-imported.

## SQL query

The SQL query for a database integration must contain specific column names. The selected import data type determines the expected columns. You can define the table name. Below, the simplest SQL queries you can run:

<style>
table th:first-of-type {
   width: 20%;
}
table th:nth-of-type(4) {
   width: 50%;
}
</style>

| Import data type | Sample query                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------- |
| Interval-based   | SELECT queueidentifier, queuename, timestamp, offered, answered, handlingtime, channel FROM table |
| Contact-based    | SELECT queueidentifier, queuename, timestamp, answered, duration, channel FROM table              |
| Agent status     | SELECT agentidentifier, starttime, endtime, activity FROM table                                   |

> Note 
> 
> In most cases, your database will not match the expected column names. Get around this by using the required column names as column aliases or create a view in your database.

Extend the sample queries to get and filter data from your custom table:

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

## Column details

The tables below show the details for the expect columns separated by import type.

### Agent status

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

| Column                    | Data type | Required | Details                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| agentidentifier           | String    | Yes      | Unique identifier for the agent                                                                                                                                          |
| starttime                 | Datetime  | Yes      | Start of the agent status activity                                                                                                                                       |
| endtime                   | Datetime  | No       | End of the agent status activity<br>Do not use if the activity is ongoing.                                                                                               |
| activity                  | String    | Yes      | Identifier for the external activity                                                                                                                                     |

### Interval-based

| Column                    | Data type | Required | Details                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| queueidentifier           | String    | Yes      | Unique identifier for the queue<br>You can rename the queue by changing the queuename, but it will keep the same queueidentifier.                                        |
| queuename                 | String    | Yes      | Identifier for the queue                                                                                                                                                 |
| timestamp                 | Datetime  | Yes      | Start of the interval                                                                                                                                                    |
| offered                   | Integer   | Yes      | Amount of contacts (e.g calls or emails) in the interval                                                                                                                 |
| answered                  | Integer   | Yes      | Amount of contacts that have been handled in the interval                                                                                                                |
| handlingtime              | Integer   | Yes      | Total handle time for all contacts in the interval                                                                                                                       |
| channel                   | String    | No       | Identifier for the channel of the injixo source queue<br>Defaults to calls if empty<br>Valid values: calls, chats, emails, social_media, documents, cases. |

### Contact-based

| Column                    | Data type | Required | Details                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| queueidentifier           | String    | Yes      | Unique identifier for the queue<br>You can rename the queue by changing the queuename, but it will keep the same queueidentifier.                                        |
| queuename                 | String    | Yes      | Identifier for the queue                                                                                                                                                 |
| timestamp                 | Datetime  | Yes      | Start of the interval                                                                                                                                                    |                                                                                                       |
| answered                  | Integer   | Yes      | Handled contact (value 1)<br>No handled contact (value 0)                                                                                                                |
| duration                  | Integer   | No       | Total handle time of a single contact                                                                                                                                    |
| channel                   | String    | No       | Identifier for the channel of the injixo source queue<br>Defaults to calls if empty<br>Valid values: calls, chats, emails, social_media, documents, cases. |

## Edit a database integration

When your database details or data structure change, you can edit the configuration of your database integration. The next data import will be done as before. If you need to re-import all available data from the past, create a new integration.

## Known ODBC driver issues

To prevent increasing TCP connections in Cloud Link when querying data from Amazon Athena, make sure to use the [Athena ODBC 2.x driver version](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver.html).
