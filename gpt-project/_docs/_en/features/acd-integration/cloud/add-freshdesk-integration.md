---
title: Add a Freshdesk integration
description: Learn how to connect your Freshdesk CRM to injixo to import data.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

A Freshdesk integration is a cloud integration that imports contact volumes for email, web forms, chat, and social messaging.

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Add a Freshdesk integration

To add a new Freshdesk integration in injixo, you need to have a Pro or Enterprise Freshdesk account.

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the **Freshworks** tile, click _Select model_{:.doc-button}.
4. In the **Freshdesk** section, click _Add integration_{:.doc-button}.

## Set up your Freshdesk integration

1. Enter a unique name for the new integration that identifies the data source.
2. In the **Credentials** section, enter your full Freshdesk domain name including the subdomain, e.g. example.freshdesk.com.
3. Go to Freshdesk and copy a valid API key of a user with the Account Administrator role.
4. Go back to injixo and paste the API key in the **API key** field.
5. Click _Save integration_{:.doc-button}.

## Install the injixo app

The Freshdesk integration requires a client application. After you have saved your configuration, you can access the **Install the injixo app** section at the bottom of the page.

To generate and copy the **injixo API key**, click _Generate_{:.doc-button}.

To set up the injixo app in your Freshdesk account, follow the on-screen instructions. For more information, refer to the [Freshworks marketplace](https://www.freshworks.com/apps/freshdesk/injixo_connect).

## Freshdesk data in injixo

injixo imports all ticket data from Freshdesk. Tickets usually contain multiple conversations that take place between your team members and customers.<br>
Note: injixo cannot import ticket durations from Freshdesk. This is why you won't see the AHT graph for workloads with Freshdesk queues in injixo Forecast.

### Tickets and conversations

In injixo, all conversations are grouped by the Freshdesk communication channel (Source). A conversation can be a new ticket or a reply to an existing ticket.

In injixo, the conversations in a Freshdesk ticket are counted separately as an offered contact.

Example: A user creates a ticket by e-mail. The team member replies and closes the ticket. Two days later, the ticket is reopened due to another email, which leads to a new conversation.

The number of offered contacts in injixo will usually be higher than the number of tickets reported in Freshdesk.

### Events from different sources

In a Freshdesk ticket, replies can be tracked in different injixo queues using the channel Cases.

Example: When there is an email reply to a ticket, you will see the contact in an injixo queue that matches the Freshdesk group and source name. A chat in the same ticket will be counted in a separate queue.

### Source queue naming convention

injixo creates source queues from your tickets. The naming convention of these queues depends on the stage of the data import (initial or continuous). During this initial import, the source queue naming will follow this convention:

- "group name + source name + Tickets"
- "group name + source name + Replies"

Examples:

- CustomerService chat Tickets
- CustomerService email Replies
- Unknown group/source Tickets

A new ticket will create a ticket queue. A reply to a ticket will create a replies queue that will also record any other replies. To get all information about a ticket, you need to look at both the ticket and the replies queue.

### Deleted tickets and spam tickets

The group name and source name cannot be determined when a ticket is changed that has already been deleted or marked as spam. The source queues that count such tickets will be labeled Unknown group/source Tickets or Unknown group/source Replies. Typically, these queues are irrelevant for scheduling your agents' workload.

## Frequently asked questions

| Question                                                                                                                                                                       | Answer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Suddenly, injixo stops displaying new Freshdesk data but the page in **Account > Integrations** still shows the status Operational for my Freshdesk integration. What can I do? | The injixo app gets Freshdesk data and sends events to injixo. In the event of communication errors between the injixo app and injixo, Freshdesk data may no longer be displayed. The Freshdesk integration cannot detect such communication errors.<br><br>Check that the injixo API key you entered when setting up the injixo app in your Freshdesk account is still valid. If the API key is invalid, update the injixo API key on the injixo app installation page. If the API key is still valid, contact the injixo Support. |
