---
title: Add a Sikom integration
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to connect your Sikom CRM to injixo to import data.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

A Sikom integration is an on-premise integration that imports call history, agent status and real-time adherence data.

The integration uses {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Add a Sikom integration

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Sikom** tile, click _Add integration_{:.doc-button}.

## Set up your new Sikom integration

1. Enter a unique name for the new integration that identifies the data source.
2. Install and connect {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. In the **Database credentials** section, set up your integration:

   - Select your database time zone.
   - Enter your database host and port.
   - Enter your database username and password.

4. If you want to import agent status data, check the checkbox **Import agent status data** in the **Configuration** section.<br>Note: To successfully import agent status data, you first need to {% link_new map external user identifiers and activities | features/acd-integration/cloud/import-agent-status-data.md %}.
5. Click _Save integration_{:.doc-button}.

The integration starts importing data into injixo.

## Edit a Sikom integration

In case any of the integration details change, e.g. database server credentials, you can edit and update the configuration of your integration. The data import will continue using the updated configuration.
