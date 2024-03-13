---
title: Add a Freshchat integration
description: Learn how to connect your Freshchat CRM to injixo to import data.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
redirect_from:
  - /add-freshdesk-messaging-integration/
redirect_reason: Updated filename on 15 September 2023
---

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Add a Freshchat integration

To add a new Freshchat integration in injixo, you need to have a Pro or Enterprise Freshchat account.

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Freshworks** tile, click _Select model_{:.doc-button}.
4. In the **Freshchat** section, click _Add integration_{:.doc-button}.

## Set up your Freshchat integration

1. Enter a unique name for the new integration that identifies the data source.
2. In the **Credentials** section, enter your full Freshchat domain name including the subdomain, e.g. example.freshchat.com.
3. Go to Freshchat and copy a valid API key of a user with the Account Administrator role.
4. Go back to injixo and paste the API key in the **API key** field.
5. Click _Save integration_{:.doc-button}.

### Install the injixo app

The Freshchat integration requires a client application. After you have saved your configuration, you can access the **Install the injixo app** section at the bottom of the page.

Generate and copy the **injixo API key** here.

To set up the injixo app in your Freshdesk account, follow the on-screen instructions. For more information, refer to the [Freshworks marketplace](https://www.freshworks.com/apps/freshdesk/injixo_connect).

## Freshchat data in injixo

### Contacts

In Freshchat, a chat usually contains multiple conversations that take place between your team members and your customers. In injixo, each solved chat counts as one contact, independent of the number of conversations.

Example: A customer creates a chat on the website, the team member then responds but solves the issue one day later, due to further information needed. This would be counted as one contact in injixo.

### Source queue naming convention

The source queues that injixo creates from your chats follow this convention:

"group name"

Examples:

- Customer Support
- Undefined_Queue

### Deleted and spam chats

A chat can be deleted or marked as spam when it is updated. In this case, the integration cannot determine the group name. The source queues that count such chats are labeled Undefined_Queue. Typically, these queues are irrelevant for scheduling your people's workload.

## Frequently asked questions

| Question                                                                                                                                                                       | Answer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Suddenly, injixo stops displaying new Freshchat data but the page in **Account > Integrations** still shows the status Operational for my Freshchat integration. What can I do? | The injixo app gets Freshchat data and sends events to injixo. In the event of communication errors between the injixo app and injixo, Freshchat data may no longer be displayed. The Freshchat integration cannot detect such communication errors.<br><br>Check that the injixo API key you entered when setting up the injixo app in your Freshdesk account is still valid. If the API key is invalid, update the injixo API key on the injixo app installation page. If the API key is still valid, contact the injixo Support. |
