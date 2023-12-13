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

In this article, you will learn:

- what events are.
- how to create and delete event types.
- how to add events and public holidays to a workload.
- how to remove events.

Add events to your historical data and the generated forecast to improve your forecast. Besides data, events are the second most important driver for forecast quality.

New to injixo Forecast? Learn {% link_new the basics | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} first.

## What are events?

An event is a marker for a day that tells injixo Forecast that this day is special regarding volume or its distribution. There are predefined categories that group similar event types, e.g. promotions or newsletters.

Events allow you to mark days in the past and the future:

- with unusually low or high volumes or average handling times.
- with daily distributions deviating from a standard day.
- with incomplete, faulty, or no data, e.g. due to an ACD outage.

injixo Forecast analyzes events added to the workload to detect trends, fluctuations in volume, and other patterns to improve the generated forecast.

## Create an event type

Any created event type is available in any workload.

1. Go to _Forecast_{:.menu-item}.
2. Select a **workload**.
3. Click _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} in the _Events_ section on the right.
4. Click **Customize Event Types**.
5. Select a pre-defined **Category** from the drop-down menu.
6. In the section _Add new Event Type_, enter a **name** in the field. The event name will appear as a combination of category and event type name.
7. Click _Add Event Type_{:.doc-button}.
8. Click _Close_{:.doc-button}.

   {{ 1 | image: "Configuring event types", '40%' }}

## Delete an event type

Delete obsolete event types or replace an event type with another one, e.g. if you reached the limit of seven event types per category.

> Deleting an event type will delete all corresponding events from all forecasts.

1. Go to _Forecast_{:.menu-item}.
2. Select a **workload**.
3. Click _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} in the _Events_ section on the right.
4. Select **Customize Event Types** from the drop-down menu.
5. Select a **Category** from the drop-down menu.
6. Click the **trash can icon** next to the event type to be removed.
7. Click _Delete_{:.doc-button} in the pop-up window to confirm the deletion or _Cancel_{:.doc-button} to go back.
8. Click _Close_{:.doc-button}.

## Add an event to a workload

Add all known events to past and future dates. Omit longer periods with uncommon patterns, as these periods and patterns degrade the quality of the forecast over time.

Smart workloads consider up to two days before and after the event date. Basic workloads only consider the impact on the actual day.

1. Go to _Forecast_{:.menu-item}.
2. Select a **workload**.
3. Click _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} in the _Events_ section on the right.
4. Select **Assign Event(s)** from the drop-down menu.
   {{ 2 | image: "Adding events", '40%' }}

5. Select an **event type** from the **Select custom event type** drop-down menu.
6. Click the **Select a day** field and select a **day** from the calendar to add the event.
7. Click _Assign Event_{:.doc-button}.
8. Click _Close_{:.doc-button}.

> An _Outage_ event marks a day in the past as invalid and excludes it from the forecast calculation.

## Add your holiday region

Add public holidays from various national holiday calendars. injixo Forecast treats public holidays as events, as they may influence the volume of a normal day. Typically, you select the appropriate holiday region while {% link_new creating a workload | features/forecast/injixo-forecast/manage-workloads.md %}. To change the holiday region:

1. Go to _Forecast_{:.menu-item}.
2. Select a **workload**.
3. Click _Edit Workload_{:.doc-button}. Alternatively, click _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} in the _Events_ section on the right, next click **Edit holiday region**.
4. Select a **Holiday region** from the drop-down menu.
5. Click _Save workload_{:.doc-button}.

## Display events and public holidays

1. Go to _Forecast_{:.menu-item}.
2. Select a **workload**.
3. Go to the **Day**, **Week**, or **Month** to see events for the selected period, or select **Year** to see all events (grouped by month) and public holidays for that year. The graphs highlight events and public holidays in yellow and display them in a list on the right.

   {{ 3 | image: "Viewing Events", '80%', 'gif' }}

## Remove an event

Remove irrelevant events from your workloads, e.g. a canceled mailing or a permanently moved marketing activity.

1. Go to _Forecast_{:.menu-item}.
2. Select a **workload**.
3. Go to the event date. The event populates on the right under _Events_.
4. Click _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} in the _Events_ section on the right.
5. Select **Assign Event(s)** from the drop-down menu.
6. Click the **trash can icon** next to the **Event Type** you want to remove.
7. Click _Close_{:.doc-button}.
