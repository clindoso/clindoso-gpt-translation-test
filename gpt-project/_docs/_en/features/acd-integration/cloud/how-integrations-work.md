---
title: How do integrations work?
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how integrations work, which integrations exist, and how to add and delete them.
promote-service: acd-integration-support
redirect_from: /cloud-overview/
redirect_reason: renamed file in Feb 2021
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

To support your workforce management, injixo needs contact and agent status data from external systems, such as Automatic Call Distribution (ACD) or Customer Relationship Management (CRM) systems. For injixo to receive and process your data, you need to integrate your ACD and/or CRM.

injixo offers native vendor-specific integrations and universal integrations, both for cloud and on-premise systems. Depending on the integration, injixo receives data every 15, 30, or 60 minutes (historical data import), or even within seconds (real-time data import).

## Delivery modes

The delivery mode of an integration determines how injixo connects to the external system:

- Cloud integrations connect to and directly import data from a cloud system, e.g. Five9 or Vonage.
- On-premise integrations use {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} to connect to a system in your local network, e.g. Genesys Engage or Sikom. Once connected, on-premise integrations will start to import up to three years of historical data.

## Vendor-specific and universal integrations

Vendor-specific integrations are tailored to the specific system and should always be the preferred option. If no vendor-specific integration is available, you can also use one of the universal integration options:

- Database: On-premise integration that uses an SQL query to read data from a database.
- CSV: File-based integration to import CSV files with injixo Cloud Link.
- injixo API: Cloud integration required for sending HTTP requests to the injixo API.

## Which data is imported?

Depending on the integration, injixo imports contact data, agent status data or both:

- Contact data (calls, chats, social media, tickets, emails, documents) contains the offered and answered volumes, as well as the average handle time, and is used to generate forecasts.
- Agent status data (login, logout, after-call work, breaks, etc.) contains information about employee activities, such as when they switch from one activity to the next, and it is used for intraday management.

## Add an integration

For details on how to set up your integration, see the following articles:

- {% link_new Add a cloud integration | features/acd-integration/cloud/add-cloud-integration.md %}
- {% link_new Add an on-premise integration | features/acd-integration/cloud/add-on-premise-integration.md %}
- {% link_new Add a CSV integration | features/acd-integration/cloud/add-csv-integration.md %}
- {% link_new Add a database integration | features/acd-integration/cloud/add-database-integration.md %}
- {% link_new Import data with injixo API | features/acd-integration/cloud/import-data-with-injixo-api.md %}

Once you have added an integration, it will start sending data to injixo.

Contact data is automatically imported. To work with contact data, add imported queues to a (new) workload to {% link_new calculate a forecast | getting-started/calculate-a-forecast.md %}. Then calculate staff requirements and create your schedule.

> Prerequisite to display agent status data
>
> To see agent status data in Intraday, {% link_new map external user and activity IDs | features/acd-integration/cloud/import-agent-status-data.md %}. To do this, pause the data import of your integration first.

<!-- add list of articles? or generic steps? -->

## Pause the data import

The activity mapping is overwritten by the running integration. To retain the mapping and to avoid duplicating activities, pause the data import of the integration by clicking the {% icon pause_circle %} next to the integration on the overview page.

To resume the data import when the mapping is done, click the {% icon play_circle %}. Missing data will be reimported.

## Delete an integration

Deleting an integration does not delete the imported data. The queues remain assigned to your workloads. You cannot delete the queues created by an integration.

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. Click the {% icon pencil %} next to the integration that you want to delete.
3. In the bottom right corner, click _Delete integration_{:.doc-button}.
4. In the confirmation window, click _Yes, really delete_{:.doc-button}.
