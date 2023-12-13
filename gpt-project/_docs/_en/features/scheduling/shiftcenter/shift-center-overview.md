---
title: What is the Shift Center?
product_label:
  - advanced
  - enterprise
  - classic
description: Learn what the Shift Center is used for and how to customize the display of data.
---

In this article, you will learn:

- what the Shift Center is and what it is used for.
- how the three sections of the Shift Center are structured and what you can do with them.
- how to customize the display of data.
- how to download your schedules as an Excel file.

## What is the Shift Center?

The Shift Center is the central place to view and manually edit the schedules created by the automatic scheduling processes.

You can use the Shift Center to:

- add, edit and move activities, day models, and employee availabilities.
- analyze coverage, requirement, and staffing based on activities and day models.
- find replacement employees for activities and shifts.
- edit employee requirements and generated shifts.

### Two Shift Center versions

In injixo Advanced and injixo Enterprise WFM you can access the Shift Center under _Plan > Shift Center_{:.breadcrumbs}. This ActiveX-free version is usable with all supported browsers.

For real-time updates, allow this Shift Center version to open a {% link_new WebSocket connection | getting-started/system-requirements.md | #share-urls-for-websockets %}. If the Shift Center cannot open the required WebSocket connection or if an open WebSocket connection is closed, a slower fallback mechanism is used to load and update data.

In injixo Classic and injixo Enterprise WFM on-premise, the Shift Center is available under _WFM > Scheduling > SchedulePro > Shift Center_{:.breadcrumbs}. This ActiveX-based version only works in Microsoft Internet Explorer and Edge. This version does not use WebSockets.

The two versions of the Shift Center differ. The articles explain the minor differences for each use case.

> On-premise: injixo build 10995 introduces the Shift Center as a Windows application
>
> To use the new version, you must install build 10995 on the server and all client workstations. injixo falls back to the embedded version when either the clients or server is not using build 10995.
>
> The Windows application resolves crashes that occur when copying and pasting items in Microsoft Edge. Learn more about the [changed handling](#on-premise-shift-center-as-a-windows-application).

## Choose the time range and level(s)

1. Click _Levels_{:.doc-button} in the filter bar.
2. Select one or more **{% link_new Levels | best-practices/tips-on-shift-center-usage.md | #tip-9-working-with-different-levels %}** which you want to display data for.
3. Click the **date button** and choose the date as of which you want to display data.
4. Choose a **time unit** by selecting _days_, _weeks_, _months_ or _years_ from the drop-down menu.
5. Choose a **number** to indicate how many days, weeks, months or years you want to display. You can view data for up to 500 days, 105 weeks, 24 months, or 2 years. If you e.g. select _Months_ as the time unit and _2_ for the time period, the schedule will show 2 months beginning with the start date you selected earlier.
6. Click _Apply_{:.doc-button}.

   {{ 13 | image: 'Filter bar in the Shift Center'}}

If you are using the {% link_new Shift Center with ActiveX | features/scheduling/shiftcenter/shift-center-overview.md | #two-shift-center-versions %} under _WFM > Scheduling > SchedulePro > Shift Center_{:.breadcrumbs}, follow these steps:

1. Click {% icon shift-center-params | icon-only %} on the top left in the action bar.
2. For **Start Date**, choose the date as of which you want to display data.
3. With **Time Unit for Display** and **Time Period Duration**, you specify the date range you want to display.
4. Select one or more **{% link_new Levels | best-practices/tips-on-shift-center-usage.md | #tip-9-working-with-different-levels %}** which you want to display data for. Select one or more levels and click the arrows to move them to the right. Alternatively, use a **double-click**.
5. Click _Ok_{:.doc-button}.

   {{ 14 | image: 'Action bar in the Shift Center'}}

## Schedule window

The schedule window is the upper part of the screen below the action bar. It shows (depending on your user rights) one or more planning units. Click the {% icon plus %} to expand a planning unit.

You now see all employees assigned to the planning unit, their personnel numbers, the level(s), and the schedules of the employees. On the right, you see the contractual working time for each employee, the actual time they have been scheduled, and the time difference between the two.

If elements are assigned to an employee in the schedule, by default, each day cell shows a colored bar with the abbreviation of the first item of the day.

A cell with gray background without any data indicates days without configured opening hours. Day models or activities shown in gray appear when employees have a second planning unit, but scheduling does not take place in there.

{{ 1 | image: 'Schedule Window in Shift Center'}}

> Update Working Time Values (Orange-Colored)
>
> Whenever your schedule changes, the color of the actual time and the difference between the actual time and the contractual time turn orange. This indicates that a manual update is required:
>
> - To update a single planning unit, click {% icon shift-center-update-working-times %} next to the planning unit name.
> - To update all planning units at once, click the **Planning Units column header**.

### Show the actual working hours, start/end times, or time accounts

To show the actual working hours, the start or end time of the shift or the time account <!-- link --> instead of the abbreviation of the first element, right-click a **day cell**, select **Display**, and then choose one of the **options**.

{{ 5 | image: 'Context menu with Display Entry', '50%' }}

In injixo Enterprise WFM, display one or more time management accounts by activating setting _48478_{:.id-label} _Display accounts used in Time Management_.

To select specific time management accounts, click _Account Balances_{:.doc-button} in the filter bar under _Plan > Shift Center_{:.breadcrumbs} or _![Account balances](/assets/img/en/features/shift-center-overview/account-balances.png)_{:.doc-button-icon} under _WFM > Scheduling > SchedulePro > Shift Center_{:.breadcrumbs}.

## Parameter window

The parameter window displays key figures like requirement, staffing, and coverage, based on the elements in the schedule window. You can show aggregated values for the day or zoom in to the interval level.

The _color-coding_ of the key figure values indicates how well the staff requirements are covered. Red shows understaffing, blue shows overstaffing and green signals ideal coverage. The more intense the color, the greater the deviation from the ideal staffing.

At the bottom of the screen, there are _three tabs_ that show key figures for the various elements of your planning unit:

- **Day Models**: Key figures for all day models.
- **Activities**: Key figures for all activities.
- **Activities Overview**: Vertical display of key figures for an activity, key figure and level.

In the parameter window, you can (depending on the tab) also use the context menu to edit your employee requirements for a single day, edit the generated shifts, and find replacement employees for a shift. If you see the message No Data, select at least level Schedule or Actual.

{{ 2 | image: 'Shift Center Parameter Window'}}

## Message window

The message window is the window at the bottom. Use the keyboard shortcut **CTRL + K** to display or hide the message window. It shows scheduling rule violations for rules configured as soft rules (yellow status).

{{ 6 | image: 'Message Window in Shift Center' }}

To delete a message, click it and press **Del** on your keyboard. To delete all messages, click an entry, press **CTRL + A** to select all entries, and hit **Del**.

## Customize the display of data

In the schedule window, parameter window, and message window it is possible to customize the display of data to get a better overview or to look at certain details more closely.

### Resize the areas

To resize one of the areas, hover the mouse over the gray bar separating the schedule window and the parameter window, or the parameter window and the message window. The mouse pointer changes. Click and drag the window up or down.

{{ 7 | image: 'Resize areas', '85%', 'gif' }}

### Expand a day column

To see more details of a day, click a **day column header** to expand it. To contract the day, click the day column header again. By default, an expanded day shows 24 hours.

{{ 3 | image: 'Expanded day in Shift Center' }}

To save some space on the screen, you can limit the timeframe to your opening hours. For this, go to _WFM > Administration > System > Settings_{:.breadcrumbs} and reconfigure the settings _48077_{:.id-label} and _48078_{:.id-label}. Enter values for the start and the end of the timescale there.

### Zoom in and out

Both in the schedule and the parameter window, you can change the resolution of the time scale, e.g. to see values down to 15 minute intervals. To zoom in and out, click the **tiny arrow buttons** pointing right and left.

{{ 4 | image: 'Time scale', '50%' }}

## How are items displayed?

You can identify different elements and states based on special markers, such as dots and (dashed) lines:

- **Activity**: Simple bar with one or more elements

  {{ 12 | image: 'Activity in Schedule Window', '50%' }}

- **Day Model**: Bar with a black line at the bottom. Little dots at the top highlight moveable corridor elements.

  {{ 8 | image: 'Day Model in Schedule Window', '50%' }}

- **Variable Day Model**: Bar with dots at the lower edge before the shift. The dots indicate possible shift positions.

  {{ 9 | image: 'Variable Day Model in Schedule Window', '50%' }}

- **Deleted Day Model**: Bar marked by big black dots at the bottom

  {{ 10 | image: 'Deleted Day Model in Schedule Window', '50%' }}

- **Deleted Activity**: Bar marked by a surrounding dashed line

  {{ 11 | image: 'Deleted Activity in Schedule Window', '50%' }}

## Download your schedules as an excel file

The Shift Center under _Plan > Shift Center_{:.breadcrumbs} does not support the data export to Excel.

In the {% link_new Shift Center with ActiveX | features/scheduling/shiftcenter/shift-center-overview.md | #two-shift-center-versions %} under _WFM > Scheduling > SchedulePro > Shift Center_{:.breadcrumbs}, you can export the schedules for the currently displayed timeframe and levels to an Excel file. Click {% icon shift-center-excel-export | icon-only %} in the action bar.

## On-premise: Shift Center as a Windows application

The Shift Center Windows application replaces the previous embedded version. It also requires Microsoft Internet Explorer or Microsoft Edge; install build 10995 on servers and clients to activate it.

Click an icon in the action bar to open a Shift Center in a new window:

- {% icon item-add | icon-only %}: Start a new instance of the Shift Center with your previously configured view (start date, levels, time period).
- {% icon shift-center-params | icon-only %}: Start a new instance of the Shift Center with modified parameters. This will reset your previously configured view in the new window.

Depending on your user rights, the action bar will contain additional icons:

- {% icon shift-center-time-accounts-balances | icon-only %}: Start a new instance that resets your previous view, with the additional column _Account Balances_ that displays specific time management accounts.
- {% icon shift-center-autoscheduler | icon-only %}: Start the AutoScheduler in a separate window.
- {% icon shift-center-job-optimization | icon-only %}: Start a job optimization in a separate window.
- {% icon shift-center-break-optimization | icon-only %}: Start a break optimization in a separate window.

Note: The following icons have moved from the action bar to the application itself:

- The export to Excel icon
- The icon to change selections
- The icon to change employee filters
- The drop-down menu to select the selection/filter

The action bar no longer links to the page where you can create employee filters. Go to _Administration > Scheduling > Employees_{:.breadcrumbs} to create or edit employee filters.
