---
title: Configure injixo Me
description: Configure injixo Me to allow employees to participate in shift bidding, exchange shifts with other employees, and request time off.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/use-injixo-me/explore-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md
redirect_from:
  - /injixo-me-administration/
  - /configure-injixo-me/
redirect_reason: Updated filename on 03 July 2023
---

In this article, you will learn how to allow employees to:

- participate in shift bidding.
- swap shifts with other employees.
- book time off.
- see one's own schedule.
- see the schedules of team members.
- set custom availabilities for certain time periods.

As a user with _Admin access_, you can turn injixo Me features on or off. For this, go to **Me** in the main navigation and click the **button** for the respective feature.

> Note
>
> Employees need to get their injixo account to access injixo Me and benefit from the features described. Learn how to {% link_new create an account for them | features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md %}.

## Shift bidding

Employees can request shifts from a pool of shifts which have been created beforehand based on employee requirements and shift requirements. Shifts are then distributed in a lottery and remaining shifts can be assigned manually. Learn more about {% link_new shift bidding | features/scheduling/schedules/schedules-shift-bidding.md %}.

{{ 5 | image: 'Shift bidding', '80%' }}

## Shift swaps

Employees can independently swap their shifts or days off with other employees. The process works as follows:

1. A shift is offered by an employee.
2. Another employee sees the offer and accepts it.
3. The shifts are swapped.

Learn more about {% link_new how to allow your employees to swap shifts | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}. In the [Team Calendar](#team-calendar), employees can see the working hours of their team members. Depending on your injixo configuration, you also need to {% link_new approve pending swap requests | features/scheduling/view-approve-shift-swap-requests.md %}.

{{ 6 | image: 'Shift swap', '50%' }}

## Time-off requests

Employees can request time off for {% link_new activities | features/administration/activity-types-and-properties.md | #activity-types %} of type Absence, Vacation, or Illness for periods ranging from a few hours of a single day up to several weeks. They can also check their annual vacation entitlement and the remaining vacation days.

Learn more about how to {% link_new activate time-off requests for your employees | features/scheduling/time-off/time-off-periods.md %}. Manage the way employees can request time off with {% link_new vacation entitlement settings | features/scheduling/time-off/vacation-entitlement.md %}, {% link_new approval rules | features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md %} and {% link_new quotas | features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md | #quota-settings %}. Approve or reject requests in {% link_new Time Off | features/scheduling/time-off/vacation-absences-management.md %}.

{{ 1 | image: 'Screen to enter a time-off request', '50%' }}

> Only activities of type _vacation_ influence the vacation entitlement.

## Team calendar

Employees can see the working hours of colleagues who are in the same {% link_new selection | features/administration/selections.md %} via the **Team Calendar**. The calendar shows presence times, breaks, and vacation days, but not the actual activity names.

{{ 7 | image: 'Team calendar', '80%' }}

## Availabilities

Employees can use the **Availabilities** menu item to set custom times when they are available or not available to work. They can set time frames of any length, independent from e.g. the hours defined in the contract. Learn more about scheduling using {% link_new availabilities | features/scheduling/scheduling-methods.md | #availabilities %}.

If your employees enter time slots that are too short, parts of the shift schedule may not be created. Therefore, check which availabilities your employees have entered, in the last step before creating the schedule.

{{ 2 | image: 'Set availability', '50%' }}

## Vacation balance in hours

Changes the display of the vacation balance from days to hours. This applies to the requested, remaining and approved time off that is displayed to employees under the menu item **Time Off**.

This switch does not affect the display of daily and hourly values in any other parts of injixo such as **Vacation/Absence Management** or **Vacation Entitlement**.

{{ 4 | image: 'Vacation Balance in Hours', '40%' }}
