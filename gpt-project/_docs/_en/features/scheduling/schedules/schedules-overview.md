---
title: What is Schedules?
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: View and edit shifts, activities and other scheduling elements like time-off requests.
promote-service: team-leader-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-activity-coverage.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-edit.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-comments.md
---

Schedules allows you to view and edit shifts, activities and other scheduling elements such as time-off requests. Access Schedules under _Plan > Schedules_{:.breadcrumbs}. It consists of a Filter bar, the Schedule area, and the Activities panel.

## Prerequisites

For the Schedules functionality to work properly, make sure you meet the following prerequisites:

- Create at least one {% link_new selection | features/administration/selections.md %}.
- Allow Schedules to open a {% link_new WebSocket connection | getting-started/system-requirements.md | #share-urls-for-websockets %}. This is required for real-time updates. If the WebSocket connection cannot be opened or needs to be recreated due to firewalls or an unstable network connection, you will see a message when the page tries to reconnect.

### Filter bar

In the filter bar, you can:

- select the planning unit(s) and employees for which you want to display the schedule.
- switch to _full-screen mode_. <sup>1</sup>
- start various _Scheduling actions_ using the drop-down menu on the right.

{{ 2 | image: 'Filter bar' }}

<sup>1</sup> Click the _![full-screen mode icon](/assets/img/common/full-screen-mode.png)_{:.doc-button-icon} icon. When in full-screen mode, move the cursor to the arrow icon at the top of the screen to see the filter bar. You can then change the planning unit, the selection or the employee filter while staying in full-screen mode. Click the icon again or press ESC to leave full-screen mode.

### Scheduling actions

- {% link_new Insert Shift sequences | features/scheduling/capacity/capacity-insert-shift-sequences.md %}: insert fixed, repetitive sequences of shifts, activities, or availabilities into your schedule
- {% link_new Job optimization | features/scheduling/schedules/schedules-job-optimization.md %}: replace activities to improve coverage
- {% link_new Optimize breaks | features/scheduling/schedules/break-optimization.md %}: reshuffle the break positions in your schedule to improve coverage
- {% link_new Empty levels | features/scheduling/schedules/schedules-empty-levels.md %}: delete the contents of a level
- {% link_new Copy level content | features/scheduling/schedules/schedules-copy-level-content.md %}: copy or back up your schedules and other elements in a level
- {% link_new Replace activities | features/scheduling/schedules/schedules-replace-activities.md %}: batch replace an activity with another activity in an existing schedule

Some _Scheduling actions_ are available only in injixo Advanced WFM and Enterprise WFM:

- {% link_new Create optimized schedule | features/scheduling/schedules/schedules-optimized-schedules.md %}: automatically create a full schedule with the best possible coverage for all activities
- {% link_new Schedule extra activities | features/scheduling/schedules/schedules-extra-activities.md %}: schedule "storable" activities like email and backoffice by replacing existing activities

### Schedule area

In the schedule area, you can click a planning unit to expand it. The first column displays the assigned people, the second column the level(s) in which the schedule elements have been saved, and the third column the people's working times. Click the arrow icons in the column headers to expand or collapse the columns.

{{ 8 | image: 'Schedule area' }}

In the working times column, you can see the _Contractual_ and the _Actual_ working time, as well as the _Difference_ between the two. A color scheme helps you to identify whether an employee has reached their contractual hours: red (too few hours), blue (too many hours), and gray (correct number of hours).

To the right of the working times column, you will find each person's schedule. With the exception of the daily view, each day cell shows a bar with the start and end times of the shift. The bar has the same color as the first activity of the day. When you hover over a shift, a tooltip will show the shift details. For shifts that contain corridors, e.g. for breaks, the tooltip always shows the corridor as the last item of the list, regardless of its actual position.

{{ 10 | image: "Weekly view with shift popover" }}

Clicking an **employee's name** opens a popover with contract and skill information for this employee. Click the **blue employee name** inside the popover to open the employee details in a new window.

Note: If you have set a join or leave date for a person, that person is only displayed in periods during which they work for the company. If you also {% link_new set a valid To date | features/administration/set-a-validity-period.md %} in the person's planning unit and the assignment to the planning unit ends on the same date, their schedules will not be visible after that date. You can still see the schedules in the same time period in Shift Center where the cells are grayed out after the person's leave date.

### Activities panel

The bar at the very bottom allows you to {% link_new analyze staffing, coverage and requirement | features/scheduling/schedules/schedules-activity-coverage.md %} for the displayed timeframe.

{{ 7 | image: 'Activities panel', '80%' }}

## Filter data

The Schedules feature allows you to filter data in different places. Learn more about it below.

Note: You can simply use the _back_ function of the browser to go back to your last filter selection or sort order, as Schedules is working with parameters in the URL for filtering and sorting.

### By planning unit

1. Click the _Planning unit_{:.doc-button} button in the filter bar.
2. Check the **checkboxes** to select one or more **Planning units**. You can also filter for a planning unit in the search field or check **All planning units**.

   {{ 6 | image: 'Filter planning units, and selection', '40%' }}

### By employees

- In the filter bar, you can choose an **selection**. In injixo Advanced WFM and Enterprise WFM, you can also select an {% link_new employee filter | features/administration/employee-filter.md %}.
- At the top left of the schedule area, use the **Search Employees** field to filter by individual employees. You can also enter just parts of the name. Separate multiple names by comma.

### By level

In the second column of the schedule area (_Level_), the _Schedule_ level is selected by default. In injixo Advanced WFM and injixo Enterprise WFM, you can display additional levels by clicking the **filter icon** and checking **checkboxes**.

{{ 12 | image: 'Filter for levels', '20%' }}

## Sort data

In the schedule area, you can sort by:

- _Employee Name_: Sort by employee name in ascending or descending order by clicking on the **column header**.
- _Working times_: Sort by _Difference_, _Actual_ and _Contractual_ by clicking on the **column headers**.
- _Start time of shifts_: Click the **three dots** in the column header of a single day. The dots only show up if you have set the view to a date range of seven days or less. Then, choose the **level** in which you want to sort. In injixo Essential WFM, only the _Schedule_ level is available.

To reverse the sort order, perform the steps outlined above again.

Note: If you have selected more than one level in the _Level_ column, you are prompted to click the **level** you want to sort by as an additional step when filtering by working times.

## Customize date range and zoom level

In the schedule area, you can display a maximum of 32 days and zoom down to the 15-minute intervals of a day.

### Choose a date range

The table header in the schedule area shows the selected date range. Use the **arrow fields** right and left to jump to the previous or next period.

To select a new date range:

1. Click the **current date range** in the center. This opens the date range picker.
2. Go to the date range from which you want to pick the start date. Click the **arrow icons** pointing left and right or click the **selected month or year** and choose a **new** one.
3. Click a date to choose the **start date**.
4. Navigate to the **end date** and click it.

To shorten or lengthen your current date range, click the current **start date** or **end date** to deselect it. Then, click a **different date** to choose this date instead.

To select predefined daily, weekly, or monthly views, use the **shortcut links** on the left side.

{{ 4 | image: "Date range picker with short cut links ", '50%' }}

### Switch to daily view

Click any **date** in the table header of the schedule area to see the details of a particular day.

{{ 11 | image: "Switch to daily view", '100%', 'gif' }}

### Zoom in and out in daily view

By default, the data of a day is displayed in one-hour intervals. You can change the interval in the time scale:

1. On the time axis header, hover your mouse over the space between the hours until a **magnifying glass** appears. Click to zoom in to the 30-minute intervals.
2. Hover your mouse over a **30** in the time scale. A magnifying glass appears. Click to zoom into the 15-minute intervals.
3. To zoom back out by one level, click **15**, **30**, or **45** in the time scale.
4. To directly zoom out to the one-hour intervals, click a **full hour**.

{{ 3 | image: 'Time axis' }}

The selected interval size is saved and will be restored on next login.
