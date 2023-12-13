---
title: Add a Genesys Cloud integration
description: Learn how to connect your Genesys Cloud CRM to injixo to import data.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

A Genesys Cloud integration is a cloud integration that imports call, email and chat history as well as agent status and real-time adherence data.

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Add a Genesys Cloud integration

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Genesys** tile, click _Select model_{:.doc-button}.
4. In the **Genesys Cloud** section, click _Add integration_{:.doc-button}.

## Set up your Genesys Cloud integration

1. Enter a unique name for the new integration that identifies the data source.
2. In the **API credentials** section, copy and paste your Genesys Cloud API key and API secret.
3. In the **Configuration** section, select your account region.
4. (Optional) Check the checkbox **Import detailed on-queue agent statuses**.<br>The agent status on-queue includes several statuses, e.g. communication, interacting, idle, not responding. When importing agent statuses, injixo will differentiate between the individual statuses summarized under on-queue.
5. Click _Save integration_{:.doc-button}.
