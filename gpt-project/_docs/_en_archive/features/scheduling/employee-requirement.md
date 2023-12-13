---
title: Create and Edit Employee Requirement
toc: false
description: Calculate how many employees you need per interval to meet your scheduling goals. Learn how to edit or delete these calculated values.
archive_ref: 20210819-en-employee-requirement
archived_date: 2021-08-19
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/staff-requirement.md
---

In this article, you will learn:

- what employee requirement is.
- how to view employee requirement.
- how to manually edit employee requirement.

## What Is Employee Requirement?

Employee requirement is the basis for all automatic scheduling processes. It defines how many employees you need for an activity at a specific time in a planning unit.
injixo uses employee requirements for the _Job optimization_, _Optimize breaks_, and _Create optimized schedule_ features to generate or optimize schedules. Employee requirement appears in other parts of injixo as _staff requirement_ or _requirement_.

Employee requirement is generated automatically as the last step of the forecasting process. In injixo Forecast, you can use the automatically generated requirement or run a specific requirement calculation script.

Note: At the beginning of your scheduling process, check whether all employee requirements have been generated correctly. View employee requirement in the {% link_new Shift Center | features/scheduling/shiftcenter/analyze-coverage-staffing-requirement.md %} or in {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %}. In {% link_new Dashboards | features/monitoring/dashboards/dashboards-examples.md %}, you can create charts showing the requirement for different days, activities and planning units.

## View and Edit Employee Requirement (SchedulePro)

1. Go to _WFM > Scheduling > SchedulePro > Employee Requirement_{:.breadcrumbs}.
2. Select a **Planning Unit**.
3. Select a **Date**.
4. Click _Apply_{:.doc-button} to display the table.
   {{ 1 | image: 'Employee Requirement Table', '100%' }}

To enter values:

1. Select a cell.
2. Enter a value.
3. Copy and paste values using **CTRL+C** or **CTRL+V** (optional).
4. Click _Save_{:.doc-button}.

To delete values:

1. Select one or more **cells**.
2. Press the **Del** key on your keyboard.
3. Click _Save_{:.doc-button}.

## View and Edit Employee Requirement in Shift Center

Within the Shift Center, you can check the employee requirement and make manual changes to single days if needed:

1. Go to _Plan > Shift Center_{:.breadcrumbs}.
2. Click the **Activities** or **Activity Overview** tab in the parameter window at the bottom.
3. Click the {% icon plus %} to open a planning unit.
4. Right-click a cell.
5. Select **Edit Employee requirement** in the context menu.

{{ 4 | image: 'Edit employee requirements in context menu', '80%' }}

You will see the requirement values for all activities of the planning unit on the selected date by interval. Multiactivities appear in bold. Deleted activities, which are still assigned to the planning unit, appear in italics; in this case, any input fields are grayed out and inaccessible. The employee requirement is displayed in the local time of the planning unit.

To edit employee requirement:

1. Click on the **interval cell** and enter the **new value**.
2. Copy and paste values using **CTRL+C** or **CTRL+V** (optional).
3. Click _OK_{:.doc-button} to save your changes.

{{ 3 | image: 'Employee Requirement Table', '80%' }}
