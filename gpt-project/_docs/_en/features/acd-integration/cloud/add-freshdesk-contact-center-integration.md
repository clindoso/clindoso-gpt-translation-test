---
title: Add a Freshdesk Contact Center integration
description: Learn how to connect your Freshdesk Contact Center CRM to injixo to import data.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

A Freshdesk Contact Center integration is a cloud integration that imports call history and real-time adherence data.

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Add a Freshdesk Contact Center integration 

To add a new Freshdesk Contact Center integration in injixo, you need to have a Pro or Enterprise Freshdesk Contact Center account.

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Freshworks** tile, click _Select model_{:.doc-button}.
4. In the **Freshdesk Contact Center** section, click _Add integration_{:.doc-button}.

## Set up your Freshdesk Contact Center integration

1. Enter a unique name for the new integration that identifies the data source.
2. In the **Credentials** section, enter your Freshdesk Contact Center domain name (including the subdomain), e.g. example.freshcaller.com.
3. Go to Freshdesk Contact Center and copy a valid API key of a user with the Account Administrator.
4. Go back to injixo and paste the API key in the **API key** field.
5. Select the [grouping strategy for imported queues](#queue-names-by-grouping-strategy).
6. Click _Save integration_{:.doc-button}. 

After you have saved the configuration, proceed in the **Install the injixo app** section on the page.

## Install the injixo app

1. In the **Install the injixo app** section, generate and copy the **injixo API key**.
2. Set up the required injixo app in your Freshdesk Contact Center account in the [Freshworks marketplace](https://www.freshworks.com/apps/injixo_1).
3. In the injixo app installation page, paste the copied API key.
4. To import data in real time, check the **Export real-time agent status data** checkbox in the injixo app installation page of the Freshworks marketplace.

## Queue names by grouping strategy

When importing data, the grouping strategy affects the names of the queues that are created in injixo:

| Grouping strategy   | Queue name                               | Example           |
| ------------------- | ---------------------------------------- | ----------------- |
| Phone number        | Phone number                             | +49123456789      |
| Routing (team/agent) | Team name                                | Tech Support Team |
| Routing (team/agent) | Agent name (if no team name is assigned) | Agent 1           |

For calls that have no group in Freshdesk Contact Center, the queue name is Undefined_Queue.

## Frequently asked questions

| Question                                                                                                                                                                       | Answer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Suddenly, injixo stops displaying new Freshdesk Contact Center data but the page in **Account > Integrations** still shows the status Operational for my Freshdesk Contact Center integration. What can I do? | The injixo app gets Freshdesk Contact Center data and sends events to injixo. In the event of communication errors between the injixo app and injixo, Freshdesk Contact Center data may no longer be displayed. The Freshdesk Contact Center integration cannot detect such communication errors .<br><br>Check that the injixo API key you entered when setting up the injixo app in your Freshdesk Contact Center account is still valid. If the API key is invalid, update the injixo API key on the injixo app installation page. If the API key is still valid, contact the injixo Support. |
