---
title: Add a Zendesk integration
description: Learn how to connect your Zendesk CRM to injixo to import data.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

A Zendesk integration is a cloud integration that imports contact volumes for email, web forms, chat, calls, and social messaging from Zendesk Support and Zendesk Talk. 

The integration only imports incoming calls (but no outbound calls). The average handle time (AHT) data is only available for Zendesk Talk.

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## Add a Zendesk integration

In your Zendesk account, create an API token for a user with [Administrative Permissions](https://support.zendesk.com/hc/en-us/articles/4408843355290-Zendesk-for-Salesforce-integration-Required-profile-permissions).

To add a new Zendesk integration in injixo, follow the steps below:

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. If there already is an integration, click _Add integration_{:.doc-button}.
3. In the Zendesk tile, click _Add integration_{:.doc-button}.
4. Enter a unique name for the new integration that identifies the data source.
5. In the **User credentials** section, enter your Zendesk credentials:
   * Enter your full Zendesk domain name including the subdomain, e.g. example.zendesk.com.
   * Enter your Zendesk username.
   * Enter your API token.
6. In the **Configuration** section, select a grouping strategy. Choose either the **IVR** or the **Phone number** option. The strategy determines how injixo [names the resulting source queues](#queue-names-for-zendesk-talk) for Zendesk Talk views. The IVR option uses the destination group. The Phone number option uses the receiving number to generate the source queue name. A call without the relevant information will appear as ungrouped. Source queues for Zendesk Support are not affected.

   > You cannot change the grouping strategy once you have saved the injixo integration configuration.

7. Click _Save integration_{:.doc-button}.

## Zendesk data in injixo

### Tickets vs. contact events

In Zendesk, a ticket usually contains multiple interactions between your team members and your customers through the different communication channels.

Every interaction represents one task that your team members have to handle. An interaction can be a new ticket or a change to an existing ticket.

Example: A user creates a ticket by writing an email. The team member then replies and closes the ticket. Two days later, the user sends another email replying to the team members's email, which reopens the ticket. In injixo, this would be counted as two emails, although happening on a single ticket.

### Views

injixo builds source queues based on your Zendesk views. After the initial data import, you will see a source queue for every supported view that you have created in Zendesk. If a view contains events from different channels (e.g. chat and email), these will appear in separate {% link_new channels | features/forecast/injixo-forecast/manage-workloads.md | #queues-and-channels %} in injixo.

Note: Adding new Zendesk views after you have saved the integration will auto-generate new injixo source queues and related history.

### Unsupported views

Zendesk allows you to create views to group tickets based on certain criteria, e.g. tickets assigned to you. Learn more in the [Zendesk documentation](https://support.zendesk.com/hc/en-us/articles/4408888828570-Creating-views-to-build-customized-lists-of-tickets). 

injixo's Zendesk integration does not support all fields and operators you can select on the Zendesk view configuration page. In parentheses below, you can see the names used in the Zendesk API. To check if your views are supported, you may need to query the raw view configuration using the Zendesk API.

injixo currently does not support views that use the following fields or operators:

- Business Hours (is_business_hours, less_than_business_hours, greater_than_business_hours)
- SLA-related fields (until_sla_next_breach_at, sla_next_breach_at)
- Channel (via_id)
- Skills (skills_match)
- Conditions with user-specific values for fields (assignee_id, via_id, updated_at, ticket_is_public)
- Unsupported operators (changed, value, value_previous, not_changed, not_value, not_value_previous)

injixo does not create source queues for such views with unsupported fields or operators.

### Channel mapping between Zendesk and injixo

Any change event on a Zendesk ticket may be counted within multiple injixo channels.

Example: An email will create a ticket which will show up in an email queue in injixo. If that same ticket enters a chat view, it will also be counted in a chat queue in injixo.

| Zendesk Channel                           | injixo       |
| ----------------------------------------- | ------------ |
| email                                     | email        |
| mobile                                    | email        |
| web                                       | email        |
| chat                                      | chat         |
| native_messaging                          | chat         |
| sms                                       | social_media |
| any_channel                               | social_media |
| facebook                                  | social_media |
| twitter                                   | social_media |
| sunshine_conversations_facebook_messenger | social_media |
| instagram_dm                              | social_media |
| voice                                     | call         |
| api                                       | case         |
| answer_bot_for_web_widget                 | case         |
| chat_transcript                           | case         |
| mobile_sdk                                | case         |

### Queue names for Zendesk Support

The resulting source queue name for Zendesk Support queues will follow this convention:

"view name + (injixo channel)"

Examples:

- Support Tickets (chat)

### Queue names for Zendesk Talk

The resulting source queue name for Zendesk Talk queues will follow this convention:

"Calls Inbound For + grouping strategy"

Examples:

- Calls Inbound For +49123456789 (Phone number)
- Calls Inbound For Senior Agents (IVR)
- Calls Inbound Ungrouped
