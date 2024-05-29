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

In _Plan > Schedules_{:.breadcrumbs}, you can see and manage your people's shifts. You can notify people of changes in their schedule, create and manage scheduling periods, and perform all available scheduling actions.
The Schedules page consists of an action bar, the schedules area and the activities area. The different sections of this article explain what you can do on each part of the page.

## Prerequisites

To get the most out of the options available in **Schedules**, make sure the following applies:

- You have created at least one {% link_new selection | features/administration/selections.md %}.
- You have configured your firewall to allow {% link_new WebSocket connections | getting-started/system-requirements.md | #share-urls-for-websockets %} for injixo. This is required for real-time updates. If the required WebSocket connection cannot be opened due to firewalls or is closed due to an unstable network connection, you see an error message.

## Action bar

### Filter data

On the left side of the top bar, you have different filtering options:

- Filter by planning unit: Select one or more planning units from the drop-down menu on the left.
- Filter by selection: Click the {% icon selection-filter-u %} and use the drop-down menu on the right to select one.
- Filter by {% link_new employee filter | features/administration/employee-filter.md %}: Click the {% icon schedules-filter-employees-u %} and use the drop-down menu on the right to select a pre-configured employee filter.

### Notify people

Click _Notify people_{:.doc-button} to {% link_new let people know about changes made to their schedule | features/scheduling/schedules/schedules-notify-scheduling-changes.md %} via push notifications or emails.

### Scheduling periods

Click _Scheduling periods_{:.doc-button} to {% link_new configure scheduling periods | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %}.

### Scheduling actions

From the drop-down menu on the far right of the action bar, select one of the following scheduling actions:

- {% link_new Insert shift sequences | features/scheduling/schedules/schedules-insert-shift-sequences.md %}: Insert fixed, recurring sequences of shifts, activities, or availabilities into your schedule.
- {% link_new Job optimization | features/scheduling/schedules/schedules-job-optimization.md %}: Replace activities to improve coverage.
- {% link_new Optimize breaks | features/scheduling/schedules/break-optimization.md %}: Reshuffle the break positions in your schedule to improve coverage.
- {% link_new Replace activities | features/scheduling/schedules/schedules-replace-activities.md %}: Batch replace an activity with another activity in an existing schedule to react to changed needs.
- {% link_new Empty levels | features/scheduling/schedules/schedules-empty-levels.md %}: Delete the contents of a level.
- {% link_new Copy level content | features/scheduling/schedules/schedules-copy-level-content.md %}: Copy or back up your schedules and other elements in a level.
- {% link_new Approve shift swaps | features/scheduling/view-approve-shift-swap-requests.md %}: Approve or reject your people's shift swap requests.

The following scheduling actions are only available in injixo Advanced WFM and Enterprise WFM:

- {% link_new Create optimized schedule | features/scheduling/schedules/schedules-optimized-schedules.md %}: Automatically create a full schedule with the best possible coverage for all activities.
- {% link_new Schedule extra activities | features/scheduling/schedules/schedules-extra-activities.md %}: Schedule storable activities like email and back-office tasks by replacing existing activities.

### Full-screen mode

Click the full screen mode icon _![full-screen mode icon](/assets/img/common/full-screen-mode.png)_{:.doc-button-icon} to switch to full-screen mode. When in full-screen mode, move the cursor to the arrow icon at the top of the screen to see the action bar. Click the {% icon full_screen_exit %} or press the Esc key to leave the full-screen mode.

## Schedule area

The schedule area consists of a table that shows scheduled shifts for the people included in the planning units, selection and/or employee filter that you selected in the action bar.<br>Hover over a shift to see more details. If a shift contains corridors, e.g. for breaks, the detail view shows the corridor as the last item of the list, regardless of its actual position in the schedule.

### Employee name column

The **Employee Name** column is the first column from the left. It displays the planning units according to your filter. Click _>_{:.doc-button} to the left of a planning unit's name to expand it.

Use the search field above the column to search for specific people. Use commas to separate the names if you want to search for more than one person at a time. You can only see a person's row if you expand the planning unit they are assigned to.

Click the column header to sort alphabetically by last name. Click a person's name to open a popover with their contract and skill information. Click the person's name in blue inside the popover to open the person's details in edit mode in a new browser tab.

> Note
>
> If you have configured a join or leave date for a person, the person is only displayed between those dates.
> If the person's planning unit has a validity period, and their assignment to the planning unit ends on the same date, their schedule after that date is not displayed. You can see schedules past that date in Shift Center, where the cells are grayed out for days after the person's leave date.

### Level column

The **Level** column is the second column from the left. You can collapse or expand it using the arrows _<_{:.doc-button} and _>_{:.doc-button} next to the employee name search field. Click the filter icon {% icon filter | icon-only %} to select one or several levels to display their data in the table. The Schedule level is selected by default. In injixo Essential WFM, only the Schedule level is available.

If you select more than one level in the **Level** column, and display [between two and seven days](#multi-day-view-with-day-columns) in the table, each day's column header displays a {% icon ellipsis_v %} that you can click to switch between levels.

### Working hours column

The Working hours column is the third column from the left. You can collapse or expand it using the arrows _<_{:.doc-button} and _>_{:.doc-button}. It contains three sections: Difference, Actual and Contractual. These sections display peoples's contractual and actual working times, plus the difference between those values.<br>The Difference value is color-coded as follows:

- Red: Fewer hours scheduled than contractually required
- Blue: More hours scheduled than contractually required
- Gray: As many hours scheduled as contractually required

To sort the table by people's working time data, click the tags **Difference**, **Actual** or **Contractual**.

### Multi-day view with day columns

Use the date picker at the top right to select the date range displayed in the table. If you select more than one day, the table displays a column for each day in the date range, up to a maximum of 32 days. Each day cell shows the start and end time of the person's shift, displayed in the color of their first activity scheduled for the day.

You can sort the table data by start time of the shifts. To do so, click the {% icon ellipsis_v %} in the header of a day column. If applicable, choose the level whose data you want to use.

Click the header of a day column to switch to the daily view with hour columns.

### Single-day view with hour columns

If you select a single day using the date picker, or if you click the header of a day column, the table displays columns for each hour of the selected day. To change between levels or sort data by shift start in this view, click the {% icon ellipsis_v %} to the right of the date picker and select a new level or click an already selected level to reverse the sorting order.

To display data in 30-minute intervals, hover in between two columns. When the {% icon magnifying_glass %} appears, click it. <br>To see 15-minute intervals, hover over the 30 mark, and click the {% icon magnifying_glass %} when it appears.<br>To go back to displaying hour columns, click any full-hour mark.

## Activities area

Click _^_{:.doc-button} on the bottom left to display a table with activity data that you can use to {% link_new analyze staffing, coverage and staff requirements | features/scheduling/schedules/schedules-activity-coverage.md %}.<br>Click the different tabs to change between them. Click the filter icon {% icon filter | icon-only %} in the **Activity** column to select the activities you want to display.
