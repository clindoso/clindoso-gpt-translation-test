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

To import agent status data, you have to {% link_new add an integration | features/acd-integration/cloud/how-integrations-work.md %}. The integration must support agent status data imports.

To see if your integration supports agent status data imports, go to _Account > Integrations_{:.breadcrumbs}. If available, integrations display the Agent Status (historical data) and/or RTA (real time) labels.

After you have added the integration, you need to add external user identifiers to people in injixo. Optionally, you can remap the external system activities to the same activities in injixo.

## External user identifiers

External user identifiers are vendor-specific. They identify the users in the external system by an email address, a username, or an agent ID.

To avoid unsuccessful imports, pay attention to the correct spelling, upper and lower case, and spaces.

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

## Map external user identifiers to people in injixo

To import data, you must add external user identifiers to employees. You can add them to all employees or only to the ones for whom you want to import agent status data.

1. Go to _WFM > Administration > Scheduling > Employees_{:.breadcrumbs} and select an employee.
2. At the top, click **External Systems**, or scroll down to the **External Systems** section.
3. Click the Add icon {% icon item-add | icon-only %} to add an external system.  
   A window opens.
4. In the **External System** drop-down menu, select the integration you have set up before.
5. In the **Employee ID in External System** field, add a unique number for the employee, e.g. the employee's personnel number.
6. In the **Extension** field, enter the external system user identifier for the employee, e.g. the employee's email address.
7. Click _OK_{:.doc-button}.

After you have updated the employees' sections, the next import will import agent status data.


## Remap external system activities

External system activities are the activities that the external system records when people log in, log out, or switch from one activity to another, e.g. from emails to calls.

You can remap external system activities to existing activities. If you decide to {% link_new create new activities | features/administration/activities.md | #create-an-activity %} instead, make sure to add them to your {% link_new planning unit | features/administration/create-and-manage-planning-units.md | #add-activities %} to display them properly later.

By default, integrations store such activities in the activity Present (ID 1) and the agent status will be displayed as Present for all activities. injixo can display the same activities as your external system. To achieve this, you need to remap external system activities to other injixo activities by following the steps below.


To remap activities, you first need to pause the integration:

1. Go to _Account > Integrations_{:.breadcrumbs}.
2. In the list of integrations, click the Suspend importing icon {% icon pause_circle | icon-only %} next to the integration for which you want to remap activities.

Once you have paused your integration, follow these steps:

1. Go to _Plan > Configuration > Activities_{:.breadcrumbs}.
2. Select the activity you want to remap.
3. In the **External Systems** section, click _Edit in WFM_{:.doc-button}. 
4. Go to the **External Systems** section.
5. Click the Add icon {% icon item-add | icon-only %}.
6. In the **External Systems** window:<br>
   - From the **External System** drop-down menu, select your integration.
   - From the **Name from the External System** drop-down menu, select the external system activity you want to map to the currently selected injixo activity.
   - From the **Classification** drop-down menu, select the value 1.
7. Click _OK_{:.doc-button}.

To remap more activities, click the next activity and proceed from the configuration menu on the right.

When you have completed the activity mapping, go to _Account > Integrations_{:.breadcrumbs} and click the Resume importing icon {% icon play_circle | icon-only %} next to your integration to resume the import.
