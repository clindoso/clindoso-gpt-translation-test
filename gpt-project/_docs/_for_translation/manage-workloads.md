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
    filepath: features/forecast/injixo-forecast/forecast-activate-business-hours.md
---

To create, edit or delete workloads, go to _Forecast_{:.breadcrumbs}.

Workloads map the input channels of your external system, which records the details of your customer interactions. Based on imported contact data stored in queues, injixo Forecast will calculate a forecast for the workload. Configurable events, public holidays, or opening hours influence the forecast result. You can also {% link_new import your forecast | features/forecast/injixo-forecast/import-forecast.md %} into workloads.

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

## Workloads and queues

How many workloads you configure and how many queues you add to each one depends entirely on the needs of your organization. You need to consider if you need separate volume, AHT, and staff requirements calculations for each queue.

Consider the following example:

You have five queues configured in your ACD system: 

- Support Tier 1
- Support Tier 2
- Product Sales North
- Product Sales Central
- Product Sales South

In this example, the three product sales queues refer to different regions of a country with a main language. That means that people skilled to handle sales-related questions can do so regardless of where the contact comes from. It can be relevant to split the sales queues by region to track marketing campaigns or other metrics, but it is not necessary to forecast contact volumes and staff requirements for each region. You can [create one workload](#create-workloads) with the name Product Sales and select all three Product Sales queues in the **Assign queues** section.

The volume and staff requirements for support enquiries, on the other hand, need to be calculated separately. Tier 1 enquiries are more common and easier to handle than tier 2 enquiries. People skilled to handle tier 1 enquiries are not necessarily trained to handle tier 2 enquiries. Additionally, because tier 2 enquiries are less common, you need fewer people to handle them. Here you [create two workloads](#create-workloads), Support Tier 1 and Support Tier 2 and assign the applicable queue to each one. If you want people responsible for tier 2 to also handle tier 1 enquiries with lower priority, keep the two separated workloads, and use a {% link_new multiactivity | features/administration/activity-types-and-properties.md | #subactivities %} for planning.

<!-- anchor for intercom forecast tour -->

## Create workloads

Create one workload for each activity you want to schedule using staff requirements. Multiactivities require one workload for the multiactivity, and one workload for each subactivity.

1. In _Forecast > Workloads_{:.breadcrumbs}, click _New workload_{:.doc-button} on top of the list.
2. Enter the general information for your workload:

   - **Name**: Unique name to identify your workload.
   - **Time zone**: The {% link_new time zone | best-practices/working-with-timezones.md %} for the workload cannot be edited later.

     > Note
     >
     > - To save staff requirements for a planning unit, the time zone of the workload must match the time zone of the planning unit.
     > - If you select a different time zone for your workload than the time zone of the integration used to import data, the imported data will be displayed as shifted in time in the workload. For example, if a CSV integration is set to UTC&nbsp;time and your workload is set to CEST&nbsp;time (UTC&nbsp;+2&nbsp;hours), the imported data marked at 08:00 will be displayed at 10:00 in the workload.

   - (Optional) **Holiday region**: Includes public holidays that may affect your forecast.
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
   When the calculation is completed, reload the page to see the final forecast version.  
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
5. (Optional) Select the **Holiday region** to acknowledge all public holidays that affect your forecast for the year.
6. Select the **Planning unit** and the **Activity**. This is required to calculate staff requirements.
    {{ 4 | image: 'Import Workload basic configuration section' }}
7. Click the tab **Forecast import**.
8. Select your **Interval length** and the **Channel** for the data import. Both must correspond with your import file.
    {{ 5 | image: 'Import Workload parameters' }}
9. Click *Create workload*{:.doc-button}. -->

## Edit workloads

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload from the workloads list or type the workload's name in the search field.
2. To change the workload details, click the {% icon pencil %}.<br>  
   In the **Assign queues** section, you can add or remove queues. If a queue’s interval or channel does not match that of the selected queues, all non-matching queues will be grayed out. If you remove a queue, the imported data is not deleted and the queue can still be added to other workloads.
3. Click _Save workload_{:.doc-button}.  
   The new configuration may update the forecast.

## Delete workloads

1. In _Forecast > Workloads_{:.breadcrumbs}, click the {% icon trash %} next to the workload you want to delete.
2. In the confirmation window, click _Delete workload_{:.doc-button}.  
   injixo stores the associated historical data. To reuse the data, add the queue or queues to another workload.

## Navigate workloads

In _Forecast > Workloads_{:.breadcrumbs}, select a workload to open the workload details page. The page includes the following three sections:

- The volume section
- The **AHT** section
- The **Staff requirements** section

Each section includes a graph and edit functionalities.

By default, the graphs display data from the current week.

- To choose a different time range, use the date picker. Click on a week number to select the whole week, or click any day and drag to select a period shorter or longer than a week.
- Use _<_{:.doc-button} and _>_{:.doc-button} to navigate to the past and to the future of the selected time range.

### The volume section

The graph in the volume section displays contact volume for historical data, imported forecasts, and generated forecasts.
Hover over the graph to see detailed information about volume, AHT, staff requirements, manual adjustments, and added events.<br>
Learn how to {% link_new adjust the volume | features/forecast/injixo-forecast/manual-adjustments.md | #adjust-the-volume%}.

### The AHT section

The AHT section is hidden by default when you open or reload the workload details page. To display the AHT section, click the {% icon eye_slash %}.
The AHT graph is only available for workloads with queues that contain AHT data.<br>
Learn how to {% link_new adjust the AHT | features/forecast/injixo-forecast/manual-adjustments.md | #adjust-the-aht%}.

### The Staff requirements section

The graph in the staff requirements section displays the calculated staff requirements.
Under the graph you can see the configured staff requirements parameters and the total person-hours. Hover over the graph to see detailed information about AHT, volume, staff requirements, any manual adjustments and added events.<br>
Learn how to use {% link_new staff requirements for scheduling | features/forecast/injixo-forecast/calculate-staff-requirements.md | #use-staff-requirements-for-scheduling %}.

## Frequently asked questions

| Question                                     | Answer                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Why are the graphs on a workload page empty? | injixo generates a forecast for 365 days after the last data import. If the graphs on a workload page do not display data for a specific time range in the future, check if your integration is still importing data in _Account > Integrations_{:.breadcrumbs}. Also, check if the right queues are assigned to the workload in the workload configuration. |