---
title: Activate business hours
product_label:
  - advanced
  - enterprise
  - classic
toc: true
description: Learn how to activate business hours and how they affect the forecast behavior.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
---

New to injixo Forecast? Learn {% link_new the basics | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} first.

By default, workloads do not take business hours into account, and forecasts are based on the total daily volume. In the workloads configuration, you can configure injixo to take business hours into account and display them in the forecast. Staff requirements always take business hours into account by default.

If you do not configure business hours for your planning unit, the forecast page does not display any staff requirements.

injixo Classic supports business hours only in Smart workloads. 

## Prerequisites

Make sure the following applies:

- You have configured valid {% link_new business hours | features/administration/create-and-manage-planning-units.md | #add-business-hours %} and {% link_new activities | features/administration/activities.md %} for the planning unit for which you want to activate business hours.
- You have checked the {% link_new **Valid from**/**Valid to** | features/administration/set-a-validity-period.md %} entries for the planning unit and activity assigned to the workload and removed or changed them, if necessary.
- You have the necessary permissions to view and edit the relevant planning units.
- If there is a planning calendar assigned to the planning unit, you also have the necessary {% link_new permissions | getting-started/configure-user-roles.md | #set-wfm-permissions %} for the planning calendar to display the business hours.

## Activate business hours

To include volumes outside business hours into the forecast calculation, activate business hours separately for each workload. 

1. In _Forecast > Workloads_{:.breadcrumbs}, select a workload.
2. Click _Edit_{:.doc-button}.
3. In the **Basic configuration** section, select a planning unit and an activity.
4. Check the **Forecast within business hours only** checkbox.
5. Click _Save workload_{:.doc-button}.
   injixo calculates a new forecast. The calculation can take some time.

Once you have activated the business hours, the graph on the **Forecast** page displays periods outside business hours as gray areas. 

## Effects on the forecast

Activating business hours in a workload has the following effects:

- injixo reads business hours from the planning unit and activity assigned to the workload, and only displays the times when both are simultaneously open as business hours. Any interval within this period is considered and displayed as open in the forecast graph.
- injixo redistributes volumes outside of the business hours within the business hours. The total daily volume does not change. The distribution is relative to existing interval values and thus follows the forecasted intraday pattern. Volumes outside of business hours become 0.
- injixo sets any forecasted average handling time values outside business hours to 0.