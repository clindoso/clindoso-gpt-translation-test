---
title: Use approval rules and quota settings
description: Set up time-off quotas and approval rules to generate suggestions for time-off approval.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-entitlement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-absences-management.md
---

You can configure approval rules and quotas to generate suggestions for approving time-off requests.

New to Time Off? Learn the {% link_new basics | features/scheduling/time-off/vacation-absences-management.md %} first.

## Configure settings for suggestions

1. Go to _Plan > Time Off_{:.breadcrumbs}
2. Click _Configure Suggestions_{:.doc-button}.
3. (Optional) Check and change the preselected **Planning unit**.

### Configure approval rules

In the **Approval rules** section, you can activate up to three rules for the suggestion process:

- **The agent has enough entitlement left**: Approvals are possible if the agent has enough remaining {% link_new vacation entitlement | features/scheduling/time-off/vacation-entitlement.md %} for the year.
- **The daily average staff requirements for the planning unit are covered (including sickness and other planned absences)**:  Approvals are possible if enough people are working to cover the daily average {% link_new staff requirements | features/scheduling/edit-or-delete-staff-requirements.md %} for all activities in the planning unit.
- **There is enough remaining absence quota for the planning unit left**: Approvals are possible if the configured value for the absence quota is not reached yet.

To save the configuration, click _Save Rules_{:.doc-button}.

## Quota settings

In the **Quota Settings** section, you can set general quota settings. The target quota is the percentage or number of employees that can be absent on a particular day.

### Full-time equivalent

If **Full-Time Equivalent** is deactivated, the quota can be configured to allow a set number or percentage of employees to take time off, regardless of whether they work full time or part time.

If **Full-Time Equivalent** is activated, a request's duration is compared to the defined full-time equivalent (e.g. eight hours). A request with a duration of four hours will count as half a day for full-time employees. The same request would count as a full day for an employee with a contractual working day of four hours.

### Quota unit

Select **Number of Full-Time Employees** or **Percentage** depending on your organisation's needs.

### Base quota

If you selected **Number of employees** as a quota unit, enter a whole number in this field. If you selected **Percentage**, enter a percentage of employees or full-time employees, depending on the **Full-Time Equivalent** settings.

A quota defined in number of employees is independent of the planning unit's size.

Example: When set as a percentage, a base quota of 10% equals 5 employees for a planning unit with 50 available employees. If the number of available employees increases to 55, the base quota of 10% would equal 5.5 employees. In contrast, a base quota of 5 employees would stay the same regardless of the total number of employees.

### Date ranges

A date range specifies a quota for a specified period and can be named individually. Date ranges overwrite the base quota. Furthermore, the order of the date ranges determines which quota is used in case of overlapping date ranges. The topmost date range has priority.

1. Click _+ Add Date Range_{:.doc-button}.
2. Add a **Title** (e.g Christmas Day).
3. Select a start and end date.
4. Enter a value for the quota.
5. Select the option to configure whether the weekly modifiers apply to the date ranges.
6. Press the _Save Quota_{:.doc-button} button.

> Hint
>
> You can drag and drop the date ranges to rearrange them. To delete date ranges click the {% icon trash %}.

### Weekdays

The percentage values in the field next to each weekday are modifiers that are applied to the resulting quota. Modifiers will increase or decrease the quota by the percentage value entered.

A value of 100% will have no effect on the quota, while a value of 120% will increase the quota by 20%. Example: If you set your **Base Quota** as 1 Full-Time Employee, a modifier of 120% to Monday will increase the quota to 1.2 Full-Time Employees on Mondays. A modifier of 80% to Friday will reduce the quota to 0.8 Full-Time Employee on Fridays.

Click _Save Quota_{:.doc-button} when you have finished configuring the quota.

## Calendar

At the bottom of the page, a yearly calendar shows the resulting quota for each day. It is a preview of your current configuration. Color coding indicates adjustments made to the **Weekday** modifiers and any **Date Ranges** added. Click on a day to see the exact quota value. Daily quotas are displayed at the top right of the calendar.

