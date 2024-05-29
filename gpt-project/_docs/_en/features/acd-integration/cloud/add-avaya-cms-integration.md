---
title: Add an Avaya CMS integration
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to connect your Avaya database to injixo to import data.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

An Avaya CMS integration is an on-premise integration that imports call and agent status data.

The integration uses {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Add an Avaya CMS integration

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Avaya CMS** tile, click _Add integration_{:.doc-button}.

## Set up your new Avaya CMS integration

1. Enter a unique name for the new integration.
   The name will help you identify the source of data and determine which queue belongs to which integration.<br>Example: Avaya integration - Customer Support Team
1. Install and connect {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
1. In the **Configuration** section, set up your integration:

   - Enter the [connection string](#connection-string) that defines the parameters required to connect the CMS database.
   - Select your database time zone from the drop-down menu.
   - Check the **Import detailed agent statuses** checkbox to add information about skills (agent profile) and splits (call routing) to imported agent statuses.
   - To import real-time agent status data, check the **Import real-time data** checkbox. In this case, enter a port number in the **Port** field.<br>
     injixo Cloud Link will open a listening TCP socket on the specified port. The Avaya Generic RTA service will connect to this port and start streaming real-time agent status data. The Avaya Generic RTA service is licensed and configured in Avaya.

1. Click _Save integration_{:.doc-button} to create the integration.

The integration starts importing data into injixo. To import agent status data, you need to {% link_new map external user identifiers and activities | features/acd-integration/cloud/import-agent-status-data.md %} once your Avaya integration is set up. If you have activated the **Import real-time data** option before, pause your integration.

## Connection string

The Avaya CMS integration needs the connection string to connect to your Avaya CMS database. Because Avaya CMS typically uses an IBM Informix database, you need to use a special connection string.

Connection string examples that use the IBM Informix ODBC Driver:<br>

- `DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=myServerAddress;DATABASE=myDatabase;HOST=myHost;SERVICE=myService;UID=myUsername;PWD=myPassword;PROTOCOL=onsoctcp;DELIMIDENT=y;` (native access via ODBC driver)
- `DSN=AvayaCMS;DELIMIDENT=y;` (requires an ODBC connection named AvayaCMS)
  If your Avaya CMS does not use an IBM Informix database, you need to obtain the appropriate connection string for your specific database type and ODBC driver. Avaya only supports ODBC connectivity.

## Edit an Avaya CMS integration

In case any of the integration details change, e.g. database server credentials, you can edit and update the configuration of your integration. The data import will continue using the updated configuration.
