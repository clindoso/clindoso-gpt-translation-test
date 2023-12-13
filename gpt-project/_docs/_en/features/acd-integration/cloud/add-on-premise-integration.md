---
title: Add an on-premise integration
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Connect your on-premise database to injixo to import contact volume, AHT, and agent status data.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## What are on-premise integrations?

On-premise integrations use {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} to connect to a system on your local network. Once connected, on-premise integrations will try to import up to three years of historical data.

## Add an on-premise integration

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. Select your external system and click _Add integration_{:.doc-button}. If your external system exists in different models, click _Select model_{:.doc-button} and click _Add integration_{:.doc-button}.
3. Complete the form with the required information. To identify the source of your data later, enter a unique name for your integration.
4. Install the {% link_new injixo Cloud Link client | features/acd-integration/cloud/install-cloud-link.md %}.
5. Click _Save integration_{:.doc-button}.

{{ 1 | image: 'Genesys Engage integration', '85%' }}

The integration now imports contact data into injixo. The first import can take some time. All queues from the connected system will automatically be available for mapping on the {% link_new workload configuration screen | features/forecast/injixo-forecast/manage-workloads.md | #create-workloads %} in injixo Forecast.

If your integration supports the import of agent status data, {% link_new map external user identifiers and activities | features/acd-integration/cloud/import-agent-status-data.md %}. The integration can then import agent status data.
