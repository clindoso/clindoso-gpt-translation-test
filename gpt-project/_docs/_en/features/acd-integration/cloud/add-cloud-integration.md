---
title: Add a cloud integration
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: false
description: Connect your cloud ACD to injixo to import data.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-five9-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## What are cloud integrations?

Cloud integrations fetch data directly from a cloud system. injixo supports a variety of cloud integrations.

## Add a cloud integration

1. Go to *Account > Integrations*{:.breadcrumbs}. The page shows all available integrations.
2. Click *Add integration*{:.doc-button} and enter the required information. In this example, we're setting up the Five9 integration, but the process for setting up other cloud integrations is similar.
3. Choose a unique name for your integration. The name should reflect the source of the data.
4. Enter the **username** and **password** for a user that has an administrator role in your Five9 account.
5. Configure further integration-specific details (i.e. the region of your Five9 account and how you would like to group the queues).
6. Click _Save_{:.doc-button} to create the integration with the provided information.

{{ 1 | image: 'Five9 integration', '80%' }}

The integration now imports data into injixo. The initial import can take up to 15 minutes. All queues from the connected system will automatically be available for mapping on the {% link_new workload configuration screen | features/forecast/injixo-forecast/create-workloads.md | #create-workloads %} in injixo Forecast.

If your integration supports the import of agent status data, you need to {% link_new map external user identifiers and activities | features/acd-integration/cloud/import-agent-status-data.md %} before agent status data can be imported.
