---
title: Edit or delete staff requirements
toc: false
product_label:
  - advanced
  - enterprise
description: Calculate how many employees you need per interval to meet your scheduling goals. Learn how to edit or delete these calculated values.
archive_ref: 20210819-en-employee-requirement
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/calculate-a-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/staff-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
---

Staff requirements define how many people you need for an activity at a specific time. Staff requirements are needed to build or optimize schedules with the Create optimized schedules, Job optimization, or Optimize breaks functionalities.

You generate staff requirements as the last step of the forecasting process. In injixo Forecast, you can use the automatically generated requirement or run a specific staff calculation method. Before you create a schedule, check if your staff requirements have been generated correctly.

## View and edit staff requirements

The easiest way to view and analyze staff requirements for the activities assigned to your planning unit is to use the {% link_new activity panel in Schedules | features/scheduling/schedules/schedules-activity-coverage.md %} or the {% link_new parameter window in Shift Center | features/scheduling/shiftcenter/analyze-coverage-staffing-requirement.md %}. In {% link_new Dashboards | features/monitoring/dashboards/dashboards-examples.md %}, you can create charts with values for different days, activities, and planning units.

In Shift Center, you can also view and edit values for single days in a separate window.

### View staff requirements

1. Go to _Plan > Shift Center_{:.breadcrumbs}.
2. In the parameter window at the bottom, click the **Activities** or **Activity Overview** tab.  
   If you see the message No Data, select at least level Schedule or Actual.
3. Click the {% icon plus %} to open a planning unit.
4. Right-click any cell.
5. In the context menu, click **Edit Employee requirement**.  
   A table displays all activities and staff requirement values for the selected day.  
   The values are displayed in the local time of the planning unit.  
   Multiactivities appear in bold.  
   Deleted activities that are still assigned to the planning unit appear in italics and cannot be edited.

### Edit staff requirements

1. Follow the steps above to [view staff requirements](#view-staff-requirements).
2. In the **Edit Employee Requirement** window, you can edit values for as follows:
   - To change a single value, click a cell and enter a new value.
   - To copy and paste data, you need to copy the row with all values from a spreadsheet first. In the table, click the first cell in which you want to insert data and drag the mouse to the right. Release the mouse and insert the copied values by pressing **CTRL+V**.
3. To save your changes, click _OK_{:.doc-button}.

## Delete staff requirements

To delete staff requirements values for one or more activities in a planning unit, you can run the {% link_new constant requirement script | features/forecast/requirement-scripts/requirement-constant.md %} in _Forecast_{:.breadcrumbs}:

- Ensure that the **Add to Existing Requirement** checkbox is not checked.
- To delete staff requirements for each day in the date range, select 1 from the **Number Of Days With Timestamps** drop-down menu. Enter the value 0 in the **Agents** and **Day 1** fields.
- To define the time period within the day, enter a time in the **Start** and **End** fields.

Example with checkboxes and values with value 0 for the entire day (from midnight to midnight):

{{ 3 | image: 'Constant requirements script example with one activity from 00:00 to 00:00 and 0 requirements', '80%' }}
