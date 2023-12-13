---
title: Create workloads
redirect_from:
  - /workloads/
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Create workloads to represent historical and forecasted contact volume and AHT. Learn about the different workload types.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/work-with-workloads.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/forecast-activate-business-hours.md
---

To create, edit or delete workloads, go to _Forecast_{:.breadcrumbs}.

Workloads map the input channels of your external system, which records the details of your customer interactions. Based on imported contact data stored in queues, injixo Forecast will calculate a forecast for the workload. Configurable events, holidays, or opening hours influence the forecast result. You can also {% link_new import your forecast | features/forecast/injixo-forecast/import-forecast.md %} into workloads.

In workloads, you configure the staff requirements calculation. Staff requirements are needed for scheduling.

New to injixo Forecast? Learn {% link_new the basics | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} first.

## Prerequisites

- Add {% link_new a native or CSV integration | features/acd-integration/cloud/how-integrations-work.md %} and import historical data for at least one queue.
- Import offered contacts, average handling time (AHT), and handled contacts. Workloads with multiple queues will need the handled contacts to display the AHT and calculate weighted averages.

injixo creates queues using the data imported by an integration. The data import interval determines the interval of the queues created from that data. You can only add queues with the same interval to a workload.

## Queues and channels

Contact data imported by an integration is stored in queues. These queues are always associated with a channel. When you [create workloads](#create-workloads), you can filter queues by channel to assign them to the workload. Native integrations automatically set the channel for queues. Not all integrations support all channels.
For a CSV integration, you need to set the channel manually. You can add a channel per column or select one channel for the file when you {% link_new map the columns | features/acd-integration/cloud/add-csv-integration.md | #map-the-columns %} of a CSV file.  

Integrations support the following channels:

- Calls
- Chats
- Emails
- Cases
- Documents
- Social media

injixo Forecast groups queues by channel. You can only add queues with the same channel to a workload.

<!-- anchor for intercom forecast tour -->

## Create workloads

We recommend creating one workload for each activity you want to schedule using staff requirements. Multiactivities require one workload for the multiactivity, and one workload for each subactivity.

1. Click _New workload_{:.doc-button} on top of the list.
2. Enter the general information for your workload:
   - **Name**: Unique name to identify your workload.
   - **Time zone**: The {% link_new time zone | best-practices/working-with-timezones.md %} for the workload cannot be edited later.

     > Note
     >
     > - To save staff requirements for a planning unit, the time zone of the workload must match the time zone of the planning unit.
     > - If you select a different time zone for your workload than the time zone of the integration used to import data, the imported data will be displayed as shifted in time in the workload. For example, if a CSV integration is set to UTC&nbsp;time and your workload is set to CEST&nbsp;time (UTC&nbsp;+2&nbsp;hours), the imported data marked at 08:00 will be displayed at 10:00 in the workload.

   - (Optional) **Holiday region**: Includes national holidays that may affect your forecast.
   - (Optional) **Planning unit** and **Activity**: Required to {% link_new activate business hours | features/forecast/injixo-forecast/forecast-activate-business-hours.md %} in the **Business hours** section.

3. (injixo Classic only) Select an option from the **Pricing model** section:

   - **Live mode** (paid): Invoiced monthly. Cannot be reverted to Test mode.
   - **Test mode** (free): You can only view forecasts and not transfer staff requirements for scheduling.

4. In the **Assign queues** section, select the queues for your workload.

   To limit the queues displayed:

   - Filter the queues by channel (Calls, Chats, etc.).
   - Use the checkboxes to show selected, unselected or inactive queues. Inactive queues are those imported by integrations that have been deleted.
   - Use the search field over the table. You can search for queue, integration or workload name.

   Note: If a queue's interval or channel does not match that of the selected queues, all non-matching queues will be grayed out.

5. Click _Create workload_{:.doc-button}.

   The page displays historical data and a preliminary forecast version.  
   When the calculation is completed, refresh the page to see the final forecast version.  
   The new workload is displayed in the workloads list.

If you are using injixo Essential, you can create Basic workloads. Basic workloads require at least two weeks of historical data. Basic workloads do not support business hours.

If you are using injixo Advanced or Enterprise WFM, you can create Smart workloads. Smart workloads generate a forecast based on just one day of historical data. Smart workloads support business hours.

If you are using injixo Classic, you additionally need to select the Forecast model (Smart or Basic) for each workload. For Smart workloads, you must choose between the Live mode and the Test mode. The Test mode is free of charge but it only lets you see the forecast, and you cannot transfer staff requirements for scheduling purposes. The Live mode offers the full functionality and is billed monthly. Smart workloads in Live mode cannot be reverted to Test mode.

<!-- hidden: feature not live yet -->
<!-- ## Create workloads without historical data

You only need an integration and historical data import if you want injixo to create forecasts. To add forecast data by {% link_new importing a forecast | features/forecast/injixo-forecast/import-forecast.md %} that has been generated externally or to {% link_new create constant staff requirements | features/forecast/requirement-scripts/requirement-constant.md %}, you can create a workload using the tab *Forecast Import*:

1. Go to **Forecast**{:.breadcrumbs}.
2. Click _Create Workload_{:.doc-button} in the upper right corner of the forecast page.
3. In the *Basic configuration* section, enter a **Name** for your new workload.
4. Select the **Time zone** to display data. Note: The set time zone must match the planning unit to save staff requirements.
5. (Optional) Select the **Holiday region** to acknowledge all national holidays that affect your forecast for the year.
6. Select the **Planning unit** and the **Activity**. Note: You must select an option to calculate staff requirements.
    {{ 4 | image: 'Import Workload basic configuration section' }}
7. Click the tab **Forecast import**.
8. Select your **Interval length** and the **Channel** for the data import. Both must correspond with your import file.
    {{ 5 | image: 'Import Workload parameters' }}
9. Click *Create workload*{:.doc-button}. -->

## Edit workloads

1. Select a workload from the workloads list or type the workload's name in the search field.
2. To change the workload details, click the {% icon pencil %}.  
   You can add or remove queues without reimporting data. Listed queues are grayed out if their interval or channel does not match that of already assigned queues.
3. Click _Save workload_{:.doc-button}.  
   The new configuration may update the forecast.

## Delete workloads

1. Click the {% icon trash %} next to the workload in the list.
2. In the confirmation window, click _Delete Workload_{:.doc-button}.  
    injixo stores the associated historical data. To reuse the data, add the queue or queues to another workload.
