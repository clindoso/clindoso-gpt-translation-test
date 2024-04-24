---
title: Constant requirement script
toc: true
description: Set constant values for your staff requirements.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

Use the Constant requirement script to save fixed staff requirements based on your input. Create new staff requirements or overwrite existing staff requirements for your activities for a specific time period.

Use the Constant requirement script in the following cases:

- You do not have any historical data to calculate staff requirements with a different calculation method.
- Some activities require a fixed number of people over a specific time. For example, you need two people to handle emails every afternoon.

## Prerequisites

- Create at least one {% link_new workload | features/forecast/injixo-forecast/create-workloads.md | #create-workloads %}.

Each workload needs at least one queue. There are two ways to create queues:

- {% link_new Add an integration | features/acd-integration/cloud/how-integrations-work.md %} and import data. injixo automatically creates a queue.
- Create a queue by {% link_new importing one sample data point | features/forecast/injixo-forecast/import-forecast.md | #create-a-queue %}. Use this method if you do not have any historical data and you want to create constant staff requirements.

## Configure the script

1. Go to _Forecast > Requirement Scripts_{:.breadcrumbs}.
2. In the **Other - Constant Requirement** tile, click _Open_{:.doc-button}.
3. In the script configuration window, configure the following settings:
    - In the **Date** section:
      - **Start Date**: Enter the start date for the staff requirements calculation.
      - **Number of Days**: Enter the number of days from the start date for which you want to calculate staff requirements.
      - **Consider Each Day of the Week**: If you select **Yes**, the script displays weekday names in the **Data** section and the start of the scheduling week is read from the setting _48420_{:.id-label}.<br> If you select **No**, the script displays days as Day 1, Day 2, Day 3, and so on. Day 1 corresponds to the **Start date**.<br>Learn more about the Consider Each Day of the Week option in the [dedicated section below](#how-does-the-consider-each-day-of-the-week-option-impact-the-calculation).
      - **Add to Existing Requirement**: Checkbox checked: The values you enter below are added to the existing staff requirements. Checkbox unchecked: The values you enter below overwrite the existing staff requirements.
      - **Add Up Requirements of Overlapping Timespans**:  Checkbox checked: The values you enter below are added to the existing staff requirements for periods that partially overlap. Checkbox unchecked: The values you enter below overwrite the existing staff requirements for periods that partially overlap.
      - **Observe Planning Unit's Business Hours**: Check the checkbox if you want to save staff requirements only for the intervals included within the business hours configured for the relevant planning unit.
    - Select values from the following drop-down menus. When you select a value, the script configuration window updates after a few seconds and displays different parameters based on the values you select.
      - **Number of Days with Timespans**: The number of days from the start date for which you can enter staff requirements.
      - **Timespans per Day**: The number of time periods per day for which you can enter staff requirements. In the **Data** section, an input field will be displayed for each period.
      - **Number of Activities**: The number of activities for which you can enter staff requirements. In the **Data** section, a column will be displayed for each activity.
    - In the **Data** section:
      - Select a **Planning Unit** and an **Activity** for each activity column.
      - Enter a **Start** and an **End** time for each time period. Use the 24-hour format.
      - In the **Agents** field, enter the number of people required for each time period.
      - Check the checkboxes next to the days for which you want to calculate staff requirements.

## Run the script

After you have configured the script, click _OK_{:.doc-button} to start the calculation.  
A window displays the planning units and the activities you selected, and the script results. Learn where you can {% link_new see the saved staff requirements | features/scheduling/edit-or-delete-staff-requirements.md | #view-and-edit-staff-requirements %}.

Note: In injixo Enterprise on-premise, go to _WFM > Forecast > ForecastPro > Forecast_{:.breadcrumbs} or _WFM > Administration > Forecasting > Scripts_{:.breadcrumbs}. The script name may vary because you can enter a custom name when creating the script.

## How does the Consider Each Day of the Week option impact the calculation?

The script uses the value entered in the **Number of days** field as a date range starting from the first day of the date range.  
If you enter a value that is smaller than 7 or equal to 7, injixo calculates staff requirements only for the number of days included in the date range.<br>
If you enter a value greater than 7, injixo calculates staff requirements according to the value you selected for the **Consider Each Day of the Week** option:

- Yes: injixo calculates staff requirements for the selected weekdays until the end of the date range.
- No: injixo calculates staff requirements repeatedly, starting with day 1 and regardless of the weekday, until the end of the date range.
