---
title: Add events and holidays
product_label:
  - advanced
  - enterprise
  - classic
description: Create events and event types to improve the accuracy of your forecast
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

Add events to your historical data and the generated forecast to improve the forecast results. Besides data, events are the second most important driver for forecast quality.

New to injixo Forecast? Learn {% link_new the basics | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} first.

## What are events?

Events allow you to mark past and future days that deviate from the standard. For example:

- Days with unusually low or high volumes or average handle times (AHT) values.
- Days with volume distributions that deviate from a standard day.
- Days with incomplete, faulty, or missing data, e.g. due to an ACD outage.

injixo Forecast analyzes events added to the workload to detect trends, fluctuations in volume, and other patterns to improve the generated forecast.

## Create an event type

Predefined categories group similar event types, e.g. marketing campaigns or newsletters.
All event types you create are available in all workloads. Each category can include up to seven event types.

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. From the three-dots menu _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} at the top right, select **Customize event types**.
3. Select a **Category** from the drop-down menu.
4. Click **+ Add event type** and enter a name.
5. Click _Add event type_{:.doc-button}.
6. Click _Close_{:.doc-button}.


## Delete an event type

Delete obsolete event types or replace an event type with another one, e.g. if you reached the limit of seven event types per category.

> Warning
>
> Deleting an event type will delete all corresponding events from all forecasts.

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. From the three-dots menu _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} at the top right, select **Customize event types**.
3. Select a **Category** from the drop-down menu.
4. Click the **trash can icon** next to the event type you want to delete.
5. Click _Delete event type_{:.doc-button} in the pop-up window.
6. Click _Close_{:.doc-button}.

## Add an event or an outage to a workload

Add all known events to past and future dates. Omit longer periods with uncommon patterns, as these periods and patterns degrade the quality of the forecast over time.

Smart workloads consider an event's impact up to two days before and after the event date. Basic workloads only consider the event's impact on the actual day.

To add an event or an outage, proceed as follows:

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. From the three-dots menu _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} at the top right, select **Manage events**.
3. In the modal window, click **+ Add event** or **+ Add outage** and enter the relevant data:
   - **Date**: Select the date to which you want to add the event.
   - **Category**: Select a category from the drop-down menu.
   - **Event**: Select an event from the drop-down menu.
4. Click _Create event_{:.doc-button} or _Create outage_{:.doc-button}.
5. Click _Close_{:.doc-button}.

> Note
>
> Add an outage to exclude a past day from the forecast calculation.

## Edit your holiday region

Add public holidays from one of the available holiday calendars. injixo Forecast treats public holidays as events, as they may influence the volume of a day. You can select the relevant holiday region while {% link_new creating a workload | features/forecast/injixo-forecast/manage-workloads.md %}. To change the holiday region, proceed as follows:

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Click _Edit_{:.doc-button} at the top right.
3. Select a **Holiday region** from the drop-down menu.
4. Click _Save workload_{:.doc-button}.

## See events and public holidays

You can identify events and public holidays in the graphs. Events, outages, and public holidays are displayed with different colors. The same color is always used for the same event type.

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select a time period from the date picker.
3. Hover over the graphs to see events and public holidays.
  <!-- {{ 3 | image: "Viewing Events", '80%', 'gif' }} -->

## Delete an event

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Select a time period from the date picker.
3. From the three-dots menu _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} at the top right, select **Manage events**.
4. Click the {% icon trash %} next to the event you want to delete.
5. Click _Close_{:.doc-button}.
