---
title: Import agent status data
product_label:
  - advanced
  - enterprise
  - classic
description: Configure injixo to correctly import agent status data.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-on-premise-integration.md
---

External systems, such as ACDs, record when people switch from one activity to the next. injixo can use this data to support Intraday Management.

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Prerequisites

To import agent status data, you first need to {% link_new add an integration | features/acd-integration/cloud/how-integrations-work.md %} that supports agent status data import.

If you need to check whether your integration supports agent status data, go to _Account > Integrations_{:.breadcrumbs} and click _Add an integration_{:.doc-button}. There, you can see the data types that each integration supports (e.g. agent status, call history, etc.). Some vendor-specific integrations are divided into different models. In those cases, click the **Select model** dropdown to see which data types are supported by each model.

After configuring the integration, you need to map the identifiers from your external system (here called external identifiers) to your people in injixo. Optionally, you can map external statuses imported from your external system to activities in injixo.

## External identifiers

External identifiers are vendor-specific. They identify the users in the external system by an email address, a username, or an agent ID.

To avoid unsuccessful imports, pay attention to the correct spelling, the use of upper and lower case, and spaces.

| Vendor                 | Required user identifier              |
| ---------------------- | ------------------------------------- |
| Five9                  | user name from Five9                  |
| Genesys Cloud          | user name from PureCloud              |
| Genesys Engage         | user name from PureEngage             |
| Talkdesk               | email address used in Talkdesk        |
| UJET                   | email address used in UJET            |
| Sikom                  | user name from Sikom                  |
| Mitel MiVoice Business | user name from Mitel MiVoice Business |
| Vonage                 | agent id from Vonage                  |
| Avaya CMS              | user name from Avaya CMS              |

## Map external identifiers to people in injixo

To import agent status data, add external identifiers to all people for whom you want to import data:

1. Go to _People_{:.breadcrumbs} and select a person.
2. On the **Profile** tab, scroll down to the **External identifiers** section and click {% icon pencil | icon-only %} **Edit**.
3. If there is no identifier assigned, click _Assign external identifier_{:.doc-button}.<br>If there already is at least one identifier assigned, click _+ Add external identifier_{:.doc-button}.
4. From the **Integration** drop-down menu, select the integration which imports your agent statuses.
5. In the **Identifier** field, enter the external identifier from your integration for this person.
6. Click _Save_{:.doc-button}.

After you have updated the person's profile section, the next import will include agent status data.

## Map external statuses to activities in injixo

External systems record when people log in, log out, or switch from one task to another. We call this information external statuses.

When you add an integration, injixo maps all external statuses to the activity Present (ID 1). With this configuration, Intraday will show the activity Present for your people whenever there is external status data available.

You can remap external statuses to other activities. You can read more about how to map external statuses and which strategy to follow in {% link_new Map external statuses to activities | features/intraday/map-external-status.md %}.
