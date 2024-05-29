---
title: Add a Mitel integration
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to connect your Mitel CRM to injixo to import data.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

A Mitel integration is an on-premise integration that imports call, email, chat and social media history, and agent status data.

The integration uses {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Add a Mitel integration

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Mitel** tile, click _Add integration_{:.doc-button}.

## Set up your new Mitel integration

1. Enter a unique name for the new integration that identifies the data source.
2. Install and connect {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. In the **Regional Settings** section, select your **ACD time zone**.
4. In the **Database credentials** section, set up your integration:

   - Enter your database host and port.
   - Enter your database username and password.

5. If you want to import agent status data, check the checkbox **Import agent status data** in the **Configuration** section.<br>Note: To successfully import agent status data, you first need to {% link_new map external user identifiers and activities | features/acd-integration/cloud/import-agent-status-data.md %}.
6. Click _Save integration_{:.doc-button}.

The integration starts importing data into injixo.

## Edit a Mitel integration

In case any of the integration details change, e.g. database server credentials, you can edit and update the configuration of your integration. The data import will continue using the updated configuration.
