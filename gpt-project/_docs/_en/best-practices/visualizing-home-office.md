---
title: View agents working from home
product_label:
  - advanced
  - enterprise
  - classic
description: Learn how to see at a glance which agents are working from home on a given day.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/tips-on-shift-center-usage.md
---

<!-- not sure about essentials -->

Your contact center allows employees to work from home on some days. You want to be able to visualize which employees are working from home on any given day so that you know to contact them by phone or a messaging application rather than looking for them in the office.

injixo offers the following methods to show that employees are working from home:

1. Day status - Schedule an activity for the entire day and display it in the background of other scheduled activities.
2. Schedule levels - Schedule an activity in another scheduling level and display this level next to your schedule.
3. Comments - Add a text for a single day for each person.  

## Home office as day status

To set up home office as day status, {% link_new create a new activity | features/administration/activities.md %} of type Absence. Do not check the **Plannable** checkbox. This prevents the activity from being scheduled automatically.


Check the following checkboxes:

- **Allow as full-day activity** (this activates the day status option)
- **Can be a day status**
- **Exchangeable with shift swap** (optional, makes home office exchangeable between employees)
- **Requestable in Me** (optional, allows agents to request home office days in injixo Me)

> Note
>
> If home office is not exchangeable, shifts can still be exchanged, but not the home office day status.

When you add the home office activity to your schedule, scheduled activities are preserved and home office is inserted in the background:

{{ 2 | image: 'Home office in Shift Center' }}

The home office activity will be displayed in the team calendar in injixo Me. <!-- See https://github.com/ivx/injixo/issues/19396#issuecomment-924892178 -->

## Home office in a second scheduling level

Create an unpaid activity of type Absence and check **Allow as full-day activity**. In Shift Center, you can insert the activity in any unused level, such as Version 1.

When you display this additional level, you can always see the home office activity:

{{ 3 | image: 'Home office in its own level' }}

## Home office as comment

You can use comments in Shift Center or Schedules to indicate that an employee is working from home. However, this is only recommended if you do not use comments for anything else.

To find agents who are working from home, you can look at the comment indicator (thicker black border) on a day cell in Shift Center. Schedules displays a comment icon within the cell.
