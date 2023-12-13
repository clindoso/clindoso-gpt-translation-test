---
title: Constant requirement
toc: true
description: Set constant values for your employee requirements.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

The script Other - Constant Requirement stores fixed values for staff requirements based on your input. Create new or overwrite existing staff requirements for your activities for a time period.

Use the script before you create a schedule if:

- some activities require a fixed number of people, e.g. two team members to process emails every afternoon.
- you don't have any historical data to calculate staff requirements using a different calculation method.

## Prerequisites

To access Forecast, you need to {% link_new create a workload | features/forecast/injixo-forecast/manage-workloads.md | #create-workloads %} which requires a queue. injixo creates queues when you {% link_new add an integration | features/acd-integration/cloud/how-integrations-work.md %} and import data.

If you do not have historical data but still want to create constant staff requirements using the script, you can also {% link_new import one sample data point | features/forecast/injixo-forecast/import-forecast.md | #create-at-least-one-queue-in-your-injixo-instance %}.

## Select the script

1. Go to _Forecast_{:.menu-item}.
2. On the right, click **Calculations for Multi-Activity, Constant Requirement and Outbound**.
3. Click _Select a requirement script_{:.doc-button}.
4. Select **Other - Constant Requirement** from the drop-down menu.
   A new window opens and displays the iWFM Requirement Script (constant).

Note: In injixo Enterprise on-premise, go to _WFM > Forecast > ForecastPro > Forecast_{:.breadcrumbs} or _WFM > Administration > Forecasting > Scripts_{:.breadcrumbs}. The script name may vary because you can enter a custom name when creating the script.

## Configure the script

1. Configure the following fields:
   - Enter the **Start Date** for the calculation.
   - Enter the **Number of Days** for the calculation. The period usually corresponds with the time frame you want to schedule.
   - **Consider Each Day of the Week**: If you select Yes, the script shows weekday names and the start of the scheduling week is read from the setting _48420_{:.id-label}. If you select No, the specified number in the **Number of Days with Timespans** field appear as 1, 2, 3, 4, etc.
2. (Optional) Adjust how the script behaves using the available checkboxes:
   - **Add to Existing Requirement**: Adds values to an already existing employee requirement. Uncheck this checkbox to overwrite existing requirement values.
   - **Add Up Requirements of Overlapping Timespans**: Adds up values in periods that partially overlap with existing requirements. Uncheck this checkbox to overwrite existing requirement values.
   - **Observe Planning Unit's Business Hours**: Monitors the planning unit's opening hours. When checked, the script will not store any values entered for intervals outside the opening hours.
3. Select values from the following drop-down menus. Your selections will determine the input fields displayed in the Data section.

   - **Number of Days with Timespans**: The number of days for which you can enter staff requirements. Depending on the selected **Consider Each Day of the Week** option, you will see weekday names or Day 1, Day 2, etc.
   - **Timespans per Day**: Number of time periods per day. An input field will be displayed for each period.
   - **Number of Activities**: The number of activities for which you can enter staff requirements. A column will be displayed for each activity.

   > Note
   >
   > When you select a value, the screen may take some time to update.

4. In the **Data** section, select a **Planning Unit** and an **Activity** for each column individually.
5. For each activity and period, enter **Start** and **End** (24h as 00:00 to 00:00), as well as the **value** for the requirement.
6. Check the **checkboxes** next to the days.  
   Now, you can [run the script](#run-the-script).

## The Consider Each Day of the Week option

The script uses the number of days as a date range starting from the first day of the date range.  
If the date range is smaller than 7, injixo will write values only for the number of days included in the date range.  
If the date range is bigger than 7, injixo will write values depending on the Consider Each Day of the Week option:

- Yes: injixo writes values for the selected weekdays until the end of the date range.
- No: injixo writes values repeatedly, starting with day 1 and regardless of the weekday. The data is continuously written until the end of the date range.

## Run the script

After you have configured the script, click _OK_{:.doc-button} to start the calculation. A window will display your input parameters and the script execution results. Learn how to {% link_new see the saved staff requirements | features/scheduling/employee-requirement.md | #view-and-edit-staff-requirements %}.

