---
title: Activity configuration examples
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: false
description: Set up standard activities with the help of examples.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

To configure how injixo handles activities during scheduling and for reporting, use the {% link_new activity types and properties | features/administration/activity-types-and-properties.md %} under _Plan > Configuration > Activities_{:.breadcrumbs}.

Below, you will find configuration examples for frequently used activities, their type and matching properties.

## Presence, break, illness, and vacation

This table covers setup examples for the activity types Presence, Break, Illness and Vacation.
The Present activity is a pre-configured standard activity in injixo. You can use it for all activities your people work on and that are based on staff requirements, e.g. calls.

<div class="table__wrapper" markdown="1">

<style>
table {
   width: 100%;
}
</style>

| &nbsp;                       |         Present         |       Lunch break       |         Illness         |        Vacation         |
| ---------------------------- | :---------------------: | :---------------------: | :---------------------: | :---------------------: |
| **Type**                     |        Presence         |          Break          |         Illness         |        Vacation         |
| Paid                         | <i class="fa fa-check"> |                         | <i class="fa fa-check"> | <i class="fa fa-check"> |
| Comply with rest period      | <i class="fa fa-check"> |                         |                         |
| Plannable                    | <i class="fa fa-check"> |                         |                         |
| Requestable in Me            |                         | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Replaceable                  | <i class="fa fa-check"> |                         |                         |
| Exchangeable with shift swap | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Allow as full-day activity   |                         |                         | <i class="fa fa-check"> | <i class="fa fa-check"> |

</div>

Depending on your organization's policy, contracts or labor regulations, some breaks may also be unpaid. In this case, uncheck the Paid checkbox.

## Absences and meetings

This table covers setup examples for the activity types Absence and Meeting.
Paid absences are typically used to compensate overtime or as a blocker to {% link_new schedule public holidays | best-practices/scheduling-public-holidays.md %}.
If there are days when an employee cannot work under any circumstances, you can block those days using the configuration setup under Unpaid absence.

<div class="table__wrapper" markdown="1">

| &nbsp;                       |      Paid absence       |     Unpaid absence      |    Full-day meeting     |        Training         |
| ---------------------------- | :---------------------: | :---------------------: | :---------------------: | :---------------------: |
| **Type**                     |         Absence         |         Absence         |         Meeting         |         Meeting         |
| Paid                         | <i class="fa fa-check"> |                         | <i class="fa fa-check"> | <i class="fa fa-check"> |
| Comply with rest period      |                         |                         | <i class="fa fa-check"> |
| Plannable                    |                         |                         |                         |
| Requestable in Me            | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Replaceable                  |                         |                         |                         |
| Exchangeable with shift swap |                         |                         |                         |
| Allow as full-day activity   | <i class="fa fa-check"> | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |

</div>

You can also use paid absences as compensation days for overtime or as paid blocker when {% link_new scheduling public holidays | best-practices/scheduling-public-holidays.md %}.<br>
The Unpaid Absence activity can also be used to flexibly determine on which days an employee will not work under any circumstances.
