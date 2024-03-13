---
title: Intraday Adherence
toc: true
product_label:
  - advanced
  - enterprise
description: Get an overview of how closely people have adhered to their shift schedules throughout the day.
archive_ref: 20210422-de-adherence
---

With Intraday Adherence, you can compare people's scheduled activities with the actual activities to identify out-of-adherence periods throughout the day.

Intraday Adherence will display data after you have set up the {% link_new real-time agent status import | features/acd-integration/cloud/import-agent-status-data.md %}.

New to Real-Time Adherence? Learn {% link_new the basics | features/intraday/real-time-adherence.md %} first.

## Display and search data

1. Go to _Intraday > Intraday Adherence_{:.breadcrumbs}
2. To display agent data, select a **planning unit** and/or **selection**.
3. To change the displayed day, click _Today_{:.doc-button} or _Yesterday_{:.doc-button} or use the **date picker**.

The table displays out-of-adherence details by person. In the table header, you can identify periods with low adherence. You can sort the table or use the search at the top to filter the view, see {% link_new filtering and sorting | features/intraday/real-time-adherence.md | #search-and-filter %}.

{{ 1 | image: 'Intraday Adherence','100%' }}

> Limit the view for specific people to relevant users
>
> Configure rights to specific planning units or selections per {% link_new user or user role | getting-started/configure-user-roles.md | #set-wfm-permissions %}.

## Adherence score

The score shows whether there were deviations between people's scheduled and actual activities.

You can analyze adherence over the course of the day via the graph. If the day has not ended, the score is calculated up to the timestamp of the last update, shown above the adherence score.

The target adherence score is indicated by the dashed line. You can {% link_new adjust the target score | features/intraday/real-time-adherence.md | #define-the-target-adherence-score %}.

{{ 2 | image: 'Adherence score','100%' }}

## Agent adherence table

The table displays adherence details for the people scheduled today. The table is sortable by person name and adherence score.

Each table row contains a timeline of a person. You can see the differences between the person's scheduled and actual activities. Each person has an individual adherence score. The individual scores add up to the overall score of the planning unit (displayed in the table header). Deviations are highlighted when the score drops below the {% link_new configured adherence target score | features/intraday/real-time-adherence.md | #define-the-target-adherence-score %}.

The colors represent three out-of-adherence types:

- Not Present (red)
- Wrong Activity (yellow)
- Not Scheduled (blue)

Click an agent to see the {% link_new agent's intraday adherence | features/intraday/adherence-intraday.md | #agent-intraday-adherence %}. {% link_new Matches | features/intraday/adherence-matches.md %} and {% link_new buffer times | features/intraday/real-time-adherence.md | #buffer-time %} influence changes in status and adherence types. Learn more about the {% link_new status and types | features/intraday/real-time-adherence.md | #status %}.

{{ 3 | image: 'Agent Adherence Table','100%' }}

## Agent intraday adherence

The Agent Intraday Adherence view drills down into adherence incident details. You can see where people have not adhered to their schedule. To understand what a person has done during the day, click a schedule entry. The view will show single activities using the configured colors.

In the timeline, you can compare the scheduled and actual activities and see the resulting out-of-adherence statuses. The table below contains a single row for each out-of-adherence period.

To change the displayed day, you can use:

- the **month selector** on top and the **daily overview** on the left.
- the **navigation arrows** next to the current date above the table.

The daily overview displays the adherence score for each day of a selected month. Above the daily overview, you can see different key metrics for the selected month, for example, the adherence score or the scheduled duration.

{{ 4 | image: 'Agent Intraday Adherence details','100%' }}

## Adherence report (CSV file)

In some cases, you might need to analyze adherence and conformance data for individual people over a longer time frame, e.g. to calculate bonus payments. The Adherence report is a CSV file that includes aggregated adherence and conformance data. To download it, follow these steps:

1. Go to _Intraday > Intraday Adherence_{:.breadcrumbs}.
2. Select at least a planning unit and/or selection.
3. Click _Download report_{:.doc-button}.  
   A window opens.
4. Select a report date range. You can select any date range from one day to up to six months in the past.
5. Click _Download report_{:.doc-button}.

The table below explains the report columns:

| Column             | Explanation                                                                     | Calculation                                                                |
| ------------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Minutes in adherence | Time spent in activities that comply with the scheduled activities      | -- |
| Minutes out of adherence  | Time spent in activities that do not comply with the scheduled activities        | -- |                  
| Adherence in %   | Percentage of working time spent in activities that comply with the scheduled activities       | Minutes in adherence/scheduled minutes * 100% |
| Minutes out of conformance   | The difference between the actual working time and the scheduled time             | Actual working minutes - scheduled minutes |
| Conformance in % | Percentage of working time in compliance with the scheduled working time | Actual time/scheduled time * 100% |
| Scheduled in %  | The percentage of scheduled working time for an activity of a certain type | Scheduled time for the relevant activity type/total scheduled time * 100%              |
| Actual in %  | The percentage of actual working time spent on an activity of a certain type | Actual time for the relevant activity type/total actual time * 100%              |

Each row of data includes a link to display the related data in _Intraday > Intraday Adherence_{:.breadcrumbs}.

## Frequently asked questions

| Question                            | Answer                                                                                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Why are some or all people missing? | Try to clear the search input. Check if the people you are looking for are scheduled today in the selected planning unit or selection.           |
| Why can't I select a specific date? | You can access historical adherence data for the six months prior to the current date, plus the current month (e.g. if today is July 15, you can select dates between January 1 and July 15.) |
