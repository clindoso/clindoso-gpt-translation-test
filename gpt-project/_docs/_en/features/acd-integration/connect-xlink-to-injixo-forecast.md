---
title: Connect Xlink to injixo Forecast
toc: true
product_label:
  - advanced
  - enterprise
  - classic
description: Learn how to connect Xlink with injixo Forecast to forecast historical data.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-installation-configuration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/forecastpro/administration/queues.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-mapping-telephony.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

In this article, you will learn:

- how to connect Xlink with injixo Forecast.
- the benefits of creating one-to-one mappings.

To learn more about integrations, read the article {% link_new How do integrations work? | features/acd-integration/cloud/how-integrations-work.md %}.

## Connect Xlink to injixo Forecast

To configure the data import, {% link_new install Xlink | features/acd-integration/xlink-overview.md %} if no native integration is available. Xlink requires {% link_new mappings | features/acd-integration/xlink-mapping-telephony.md %} to link data from an external queue to an injixo destination queue. Before you can create Xlink mappings, create all injixo destination queues.

### 1. Create a new integration for Xlink

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. Select type **Universal Interfaces**.
3. Click _Add integration_{:.doc-button} in the _Xlink_ section.

### 2. Create injixo destination queues

1. Go to _WFM > Administration > Forecasting > Queues_{:.breadcrumbs}.
2. Create a new {% link_new destination queue | features/forecast/forecastpro/administration/queues.md | #creating-queues %} for each external queue.
3. Click the {% icon item-add %} to add value types to your destination queue. There are multiple value types for each channel (e.g. calls, emails, social media). Value types are required to create a forecast.
4. Select the **value types** for the channel. For the channel _calls_, add at least:
   - _Calls Average Handling Time_
   - _Calls Answered_
   - _Calls Offered_

### 3. Add mappings and import data

1. Open the Xlink user interface **isps_ul.exe** in your Xlink installation.
2. Create {% link_new mappings | features/acd-integration/xlink-mapping-telephony.md | #create-mappings %} between each external queue and an injixo destination queue.
3. Start the {% link_new Xlink data import | features/acd-integration/xlink-import-mode.md %}.

All destination queues with a mapping will be available in your workloads. You can create [new or edit existing workloads](/manage-workloads) after the first data import has been completed.

## Benefits of creating one-to-one mappings

A one-to-one mapping is a link between an external queue and an injixo destination queue. You can group one-to-one mappings in your {% link_new workloads | features/forecast/injixo-forecast/manage-workloads.md %}.

By creating one-to-one mappings in Xlink, you:

- can add/remove single queues in workloads.
- can see new forecasts when you change your mappings in workloads.

Note: Imported data is stored in injixo per queue. Even if you change mappings, your data will still be available. You don't need to re-import data.

Example for one-to-one mappings:

{{ 1 | image: 'Example of one-to-one mappings from three external queues', '80%'}}
