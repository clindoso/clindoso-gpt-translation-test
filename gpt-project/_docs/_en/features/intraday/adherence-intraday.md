---
title: Intraday Adherence
toc: true
product_label:
  - advanced
  - enterprise
description: Get an overview of how closely people have adhered to their shift schedules throughout the day.
archive_ref: 20210422-de-adherence
---

In _Intraday > Intraday Adherence_{:.breadcrumbs}, you can compare people's scheduled activities with the actual activities to identify out-of-adherence periods throughout the day. You can access the adherence data for the last six months and the current month.

## Prerequisites

To be able to see adherence data, make sure the following applies:
- You have added an {% link_new integration | features/acd-integration/cloud/how-integrations-work.md %} that supports agent status data import.
- You have set up the {% link_new agent status data import | features/acd-integration/cloud/import-agent-status-data.md %}.

## Display data

1. Select a **Planning unit** and, optionally, a **Selection**.
2. Select a date by using the date picker, or click _Today_{:.doc-button} or _Yesterday_{:.doc-button}.<br>
   The page shows the total Adherence percentage for the selected day.<br>
   A table displays individual scores and details about out-of-adherence statuses. Learn more about the [table](#agent-overview-table).


> Tip
>
> To show relevant people only, limit permissions to specific planning units or selections by configuring {% link_new user roles | getting-started/configure-user-roles.md | #set-wfm-permissions %}.

### Adherence score

The page shows different Adherence score details:

- Adherence in %: Percentage of working time spent on scheduled activities. If the day has not ended, the score is calculated up to the last updated timestamp, which is displayed above the score.
- Scores by interval: Blue bars represent scores by interval. Scores lower than 100&nbsp;% represent intervals during which people’s actual activities deviate from their scheduled activities.
- Target adherence score: The dashed line in the graph shows the configured target score. You can {% link_new adjust the target score | features/intraday/real-time-adherence.md | #define-the-target-adherence-score %}.

<!-- Adherence in %	Percentage of working time spent in activities that comply with the scheduled activities	Minutes in adherence/scheduled minutes * 100% -->

{{ 2 | image: 'Adherence score','100%' }}

### Agent overview table

A table displays adherence details on the selected day. You can sort the table by person's name or adherence score, or use the search at the top to filter the view, see {% link_new filtering and sorting | features/intraday/real-time-adherence.md | #search-and-filter %}.
Each row shows a person's adherence score. Differences between the person's scheduled activities and their actual activities are highlighted. To see the {% link_new person's intraday adherence | features/intraday/adherence-intraday.md | #agent-intraday-adherence %}, click their name.

When the score drops below the {% link_new configured adherence target score | features/intraday/real-time-adherence.md | #define-the-target-adherence-score %}, the score is highlighted in red. {% link_new Matches | features/intraday/adherence-matches.md %} and {% link_new buffer times | features/intraday/real-time-adherence.md | #buffer-time %} may influence changes in status and adherence types. Learn more about the {% link_new status and types | features/intraday/real-time-adherence.md | #status %}.

Different colors identify the three out-of-adherence types:

- Red: Not present
- Yellow: Wrong Activity
- Blue: Not scheduled

{{ 3 | image: 'Agent Adherence Table','100%' }}

## Agent intraday adherence

To see adherence details for a single person, click an agent's row. To change dates, use the month selector or the navigation arrows next to the dates.

The two boxes on the left give you an overview of the selected month:

- Agent name: Shows the person's adherence score, how long they were scheduled, and out of adherence details for the selected month. The values include the data up to the last completed interval of the current day. The values do not contain future data.
- Daily overview: Hover over it to see adherence scores for each day. Click it to change dates.

On the right, you can see in detail when this person was scheduled and where they did not adhere to the schedule:

- Intraday adherence score and durations for Scheduled and Out of Adherence:
  - Intraday adherence score: Calculated using data up to the last completed interval of the current day. Identical to the score for the day when you hover a date in the calendar on the left.
  - Scheduled and Out of Adherence durations: Sum of durations for all scheduled activities (activity types present, meeting, break) and deviations in the schedule on the selected date.
- Timeline: Colored bars help you compare the scheduled and actual activities and see the resulting out-of-adherence statuses.
- Table: Each row shows details for an out-of-adherence period.

## Adherence report (CSV file)

In some cases, you might need to analyze adherence and conformance data for individual people over a longer time frame, e.g. to calculate bonus payments. The Adherence report is a CSV file that includes aggregated adherence and conformance data. To download it, follow these steps:

1. Go to _Intraday > Intraday Adherence_{:.breadcrumbs}.
2. Select at least a planning unit and/or selection.
3. Click _Download report_{:.doc-button}.  
   A window opens.
4. Select a report date range. You can select any date range from one day to up to six months in the past.
5. Click _Download report_{:.doc-button}.

The table below explains the report columns:

| Column                     | Explanation                                                                              | Calculation                                                                |
| -------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Minutes in adherence       | Time spent in activities that comply with the scheduled activities                       | --                                                                         |
| Minutes out of adherence   | Time spent in activities that do not comply with the scheduled activities                | --                                                                         |
| Adherence in %             | Percentage of working time spent in activities that comply with the scheduled activities | Minutes in adherence/scheduled minutes \* 100%                             |
| Minutes out of conformance | The difference between the actual working time and the scheduled time                    | Actual working minutes - scheduled minutes                                 |
| Conformance in %           | Percentage of working time in compliance with the scheduled working time                 | Actual time/scheduled time \* 100%                                         |
| Scheduled in %             | The percentage of scheduled working time for an activity of a certain type               | Scheduled time for the relevant activity type/total scheduled time \* 100% |
| Actual in %                | The percentage of actual working time spent on an activity of a certain type             | Actual time for the relevant activity type/total actual time \* 100%       |

Each row of data includes a link to display the related data in _Intraday > Intraday Adherence_{:.breadcrumbs}.

## Frequently asked questions

| Question                            | Answer                                                                                                                                                                                        |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Why are some or all people missing? | Try to clear the search input. Check if the people you are looking for are scheduled today in the selected planning unit or selection.                                                        |
| Why can't I select a specific date? | You can access historical adherence data for the six months prior to the current date, plus the current month (e.g. if today is July 15, you can select dates between January 1 and July 15.) |
