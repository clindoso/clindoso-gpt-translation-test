---
title: Add an Interactive Intelligence CIC integration
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to connect your Interactive Intelligence CIC to injixo to import data.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

An Interactive Intelligence CIC integration is an on-premise integration that imports real-time adherence data.

The integration uses {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Add an Interactive Intelligence CIC integration

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Genesys** tile, click _Select model_{:.doc-button}.
4. In the **Interactive Intelligence CIC** section, click _Add integration_{:.doc-button}.

## Set up your Interactive Intelligence CIC integration

1. Enter a unique name for the new integration.
   The name will help you identify the source of data and determine which queue belongs to which integration.<br>Example: CIC - Customer Support Team
2. Install and connect {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. In the **Configuration** section, set up your integration:
 - **Time zone**: Select your ACD time zone from the drop-down menu.
 - **ACD server addresses**: Enter the DNS name or IP address and the port of your ACD, separated by a colon, e.g.: acd.example.com:8080.<br>To enter several ACDs, separate your entries with commas.
4. Click _Save integration_{:.doc-button} to create the integration.

The integration starts importing data into injixo. To import agent status data, you need to {% link_new map external user identifiers and activities | features/acd-integration/cloud/import-agent-status-data.md %} once your Interactive Intelligence CIC integration is set up.

## Edit an Interactive Intelligence CIC integration

In case any of the integration details change, e.g. your ACD port, you can edit and update the configuration of your integration. The data import will continue using the updated configuration.
