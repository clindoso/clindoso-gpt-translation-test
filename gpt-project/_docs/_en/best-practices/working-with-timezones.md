---
title: Understand and use time zones
description: Learn how time zones affect the display of data and how to set a user time zone which is right for you.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /best-practice-time zones/
---

In this article you'll learn

- How time zones work in injixo.
- How to set your user time zone.
- How the setting of your user time zone and the time zones of planning units, queues and workloads effects the display of data in injixo.

## Time zones in injixo

injixo supports scheduling across multiple time zones.

Each {% link_new planning unit | features/administration/create-and-manage-planning-units.md %}, {% link_new queue | features/forecast/forecastpro/administration/queues.md %}, and {% link_new workload | features/forecast/injixo-forecast/manage-workloads.md %} has a time zone which you set when creating the item. You cannot change the time zone afterwards. If you need to change it, you have to recreate the item.

The combination of the time zones of the elements as well as the time zone set for your user account determines how injixo displays data in the various features and functionalities.

## Set your user time zone

Your user time zone controls how data is displayed in features like the Shift Center, Schedules, and Dashboards. Change your user time zone to display data from the perspective of any time zone you want:

1. Click your **username** in the upper right.
2. Select a **Time Zone**.
3. Click _Save Profile_{:.doc-button}.

If you re-enter an injixo feature, the data will shift according to your new user time zone.

Example: Your contact center operates in New York, but you work in Berlin. Set your user time zone to Berlin time and the planning unit time zone to New York time to see schedules in your local time. Change your user time zone to New York time to see schedules in the local time of the remote location, in this case New York time.

## Which time zone is used by which feature?

Some injixo features use the user time zone to display data, others the time zone defined for the planning unit or the workload. Some features also show the time offset between the user time zone and the planning unit or workload time zone. Learn which time zone is used in which features and where it is displayed.

### Shift Center

The two main parts of the Shift Center - the schedule window and the parameter window - display data in the user time zone. If there is a time offset between the user time zone and the planning unit time zone, it is displayed in square brackets next to the name of the planning unit.

{{ 3 | image: "Time in Schedule View - Shift Center - Local user time", '90%' }}

If you edit a day, the data is shown in the planning unit time zone during the editing.

{{ 4 | image: "Time in edit menu - planning unit time zone", '80%' }}

### Schedules

The Schedules feature under _Plan > Schedules_{:.breadcrumbs} displays data in the user time zone. If there is a time offset between the time zone of the user and the planning unit, it is displayed next to the name of the planning unit.

{{ 11 | image: "Schedules Time Difference", '80%' }}

If you edit a day, the data is shown in the planning unit time zone during the editing.

### Dashboards

The Dashboards feature under _Analyze > Dashboards_{:.breadcrumbs} displays the data in the user time zone. You can see the current user time zone in the bottom right corner.

If you enter the editing mode by clicking on _![Context menu](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon} and then on **Edit**, the navigator opens to the left. To the right of the elements in the navigator, you can see the time zone of the respective planning unit or workload.

{{ 12 | image: "Dashboards navigator - tree view", '80%' }}

### injixo Me

injixo Me displays shifts and activity times in the user time zone.

### Reports

The reports which you create with the Reports feature under _WFM > Monitoring > Reports_{:.breadcrumbs} display data in the time zone of the planning unit. The report header also displays the time offset between the time zone of the planning unit and the user time zone.

{{ 7 | image: "Planing unit time zone and offset for the user", '60%' }}

### injixo Forecast


The Workload feature under _Forecast_{:.breadcrumbs} shows data in the time zone set for the workload. The time zone of the workload is displayed to the right of the workload name in the drop-down menu.

injixo Forecast displays data using the time zone that is set for the workload. You can see the time zone of the workload in these places: 
- the workloads list
- next to the workload name in the drop-down menu

The values in the volume and AHT graphs in workloads do not default to the time zone set in {% link_new your user profile | getting-started/navigate-injixo.md | #your-user-profile %}. To see values according to your profile's time zone, go to _Analyze > Dashboards_{:.breadcrumbs} and add workload data to a dashboard.

### Requirements calculation window

When you calculate the staff requirements for a workload, you can choose among several staff requirements calculation methods. Learn more about configuring the
{% link_new Multiactivity script | features/forecast/requirement-scripts/requirement-multiactivity.md %}, the {% link_new Outbound script | features/forecast/requirement-scripts/requirement-outbound.md %}, and the {% link_new Constant requirement script | features/forecast/requirement-scripts/requirement-constant.md %}.

Staff requirements are calculated in the time zone of the planning unit. The calculation considers the time offset between queue and planning unit timezone.

{{ 10 | image: "requirement script window", '65%' }}
