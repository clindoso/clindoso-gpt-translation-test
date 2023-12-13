---
title: Activate business hours
product_label:
  - advanced
  - enterprise
  - classic
toc: false
description: Understand how to activate business hours and how they change the forecast behavior.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

New to injixo Forecast? Learn {% link_new the basics | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} first.

By default, workloads do not observe business hours and forecasts consider all volumes throughout the day.

injixo Classic only supports business hours in Smart workloads.

## How do business hours impact the forecast calculation?

If you activate business hours in a workload, injixo:

- intersects the business hours from the assigned planning unit and activity. Any interval within this period counts as open.
- distributes any volumes outside business hours to a period within the business hours. The total daily volume does not change. The distribution is relative to existing interval values and thus follows the forecasted intraday pattern. Volumes outside business hours become 0.
- sets any forecasted average handling time values outside business hours to 0.

## Activate business hours

To include outside business hours volumes into the forecast calculation, activate business hours separately in each workload.

1. Go to _Forecast_{:.menu-item}.
2. Select a workload, using one of the following options:
   - Select the workload from the drop-down menu on top.
   - Type the workload name in the search field.
   - Click the workload in the list.
3. Click _Edit Workload_{:.doc-button}.
4. Select a **planning unit** and an **activity**.
5. Check the **Forecast within business hours only** checkbox.
6. Click _Save workload_{:.doc-button}.
   injixo will calculate a new forecast. The calculation can take some time.

Important: Configure valid business hours and activities in the selected planning unit for the forecast period to ensure forecast generation. Remove or change the {% link_new Valid from or Valid to entries | features/administration/set-a-validity-period.md %} if necessary.

## How are business hours displayed?

injixo Forecast displays business hours using an orange bar in daily view:

{{ 1 | image: "Orange bar indicating activated business hours in a workload", '80%' }}

Note: Additional {% link_new user rights | getting-started/configure-user-roles.md %} for the planning unit's planning calendar may be required to display the orange bar for opening hours. Go to _WFM > Administration > System > Role Authorization_{:.breadcrumbs} and add rights for the planning calendar to the affected user or user group.
