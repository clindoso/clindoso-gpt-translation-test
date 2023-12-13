---
title: Map Xlink agent activity data
toc: false
product_label:
  - on-premise
description: Map agent statuses and external activities from your ACD to injixo activities.
---

In this article, you will learn how to map the external login IDs from external systems with injixo. We call this process Mapping.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

> This article refers to Xlink. Read the article {% link_new Import agent status data | features/acd-integration/cloud/import-agent-status-data.md %} if you want to configure an integration.

An activity in an external system represents an activity or skill that an employee logs on to, for example, by entering a code in the external system. Depending on the interface, different activities from the external system are available. The specific interface documentation with further information is available at [downloads.injixo.com](https://downloads.injixo.com).

## Map external user identifiers to employees

By default, Xlink stores all external activities from your system in the activity _Present_ with the ID 1. Therefore, the agent status will be displayed as _Present_ for all activities. To display the actual activities instead, follow these steps:

Create a separate new activity for each activity which has been stored in _Present_.

1. Go to _Plan > Configuration_{:.breadcrumbs} and select **Activities**.
2. Click **Present** in the list of activities, then click **External System**. You will see a list of all activities which have been imported by Xlink.
3. For each of these activities, {% link_new create a new activity | features/administration/activities.md | #create-an-activity %} if it doesn't exist already.
4. Click the **Present** activity, then click **External System**.
5. Click _![remove button](/assets/img/common/item-delete.gif)_{:.doc-button-icon} on every **activity** to remove it from the **Present** activity.
6. Click _OK_{:.doc-button}.

Now, you can map the activities from the external system with the newly created activities:

1. Click one of the **activities** which you have just created, then click **External System**.
2. Click the {% icon item-add %}.
3. For **External System**, select your external system.
4. For **External Activity**, select the external activity you want to connect with the current activity.
5. Select _1_ for **Classification**.
6. Click _OK_{:.doc-button}.
7. Modify all activities you created in the same way.

> To properly display your newly created activities, add them to your {% link_new planning unit | features/administration/create-and-manage-planning-units.md | #add-activities %} under _WFM > Administration > Scheduling > Planning Units_{:.breadcrumbs}.

Several external activities can be assigned to one WFM activity. Conversely, however, only exactly one WFM activity can be assigned to an external activity.

## Add external login IDs to employees

Your employees have a unique ID in the external system with which they log in. Go to _WFM > Administration > Scheduling > Employees_{:.breadcrumbs} and assign the correct external user identifier to each employee.

1. Click an **Employee**.
2. At the top, find the **External System** link and click it. The page will scroll down to the External System section.
3. Click the {% icon item-add %} to add an external system. A new window opens.
4. For **External System**, select the external system you have set up in advance.
5. For **Employee ID in External System**, add the ACD login ID for the employee. The ID may only contain numbers.
6. Click _OK_{:.doc-button}.

Repeat the process for all employees. A missing or wrong user identifier will lead to no data import. After you have added the external user identifier for all employees, you can import data.

{{ 1 | image: 'Employees External Systems', '50%' }}

{{ 2 | image: 'External Systems Dialog', '50%' }}

You can assign several external employee IDs to a single employee in WFM, but you only can assign an external employee ID to a single WFM employee.
