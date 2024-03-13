---
title: Availabilities
product_label:
  - advanced
  - enterprise
  - classic
description: Create reusable availabilities to define time frames when employees can be scheduled.
redirect_from:
  - /availability-periods/
redirect_reason: rename article September 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
---

In this article, you will learn:

- what availabilities are.
- how to set up availabilities.

## What are availabilities?

Use availabilities when an employee is not (or only partially) available on a day. Using availabilities, you can further narrow down the restrictions already defined by your planning unit's business hours and contractual limitations.

Only if a shift or activity fits into the configured time frame, it can be inserted into the schedule. Employee with no availability are considered available at any time within your business hours.

## Use cases

You can use availabilities for various purposes. The use cases below are just examples.

| Use case                              | Example                                                                                              |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Fixed working days/times in each week | Employees are only scheduled for morning shifts or earlier end times for childcare purposes.         |
| Block weekends                        | Employees are not scheduled on weekends. Availabilities of one minute block scheduling.              |
| Rotate availabilities across weeks    | 50 % of the team only works until 2pm but the rest works longer due to extended phone support.       |
| Visualize core working hours          | Employees have an availability based on their contract which can be overwritten by a shift sequence. |
| Temporarily (un)available employees   | If employees' availabilities change temporarily, you can overwrite them with shift sequences.        |

<!-- just a test if people read carefully :) What do you think? -->

We are happy to read about your special use cases. Include a comment in the feedback survey for this article.

## Scheduling impact

By default, injixo respects availabilities when creating optimized schedules. Availabilities are not checked while shifts are generated but when the schedule is saved during lottery/assignment.

injixo does not check availabilities if the scheduling rule _2611_{:.id-label} _Check employee availability_ is turned off.

Tip: If you want your employees to be able to request and receive shifts that are longer than their availability, you can turn off the scheduling rule.

## Setting up availabilities

There are two ways to set up availabilities:

| Name                     | Details                                                                                             |
| ------------------------ | --------------------------------------------------------------------------------------------------- |
| Employee availabilities  | Configure temporary or permanent availabilities for single employees in the employee configuration. |
| Day model availabilities | Add availabilities to shift sequences to add the same availability to multiple employees.           |

Note: Day model availabilities overwrite employee availabilities, as well as availabilities that have been manually inserted.

If you allow it, {% link_new employees can enter their own availability | features/injixo-me/use-injixo-me/explore-injixo-me.md | #set-your-availabilities-availability %} in injixo Me. The availabilities are added as employee availabilities (14 at most %}. Employees themselves or planners must regularly delete any obsolete entries from the list. Since this feature does not include an automatic review process, check these availabilities manually before creating the schedule to avoid scheduling errors.

### Tips to set up time periods

You can map your employees’ exact working hours, for example 8 a.m. to 5 p.m.

Or, to be more flexible, extend the time frame of the availabilities (start or end time) to the business hours of your planning unit, for example:

- 12 a.m.-8 p.m.: Employees can work before 8 p.m.
- 4 p.m.-12 a.m.: Employees cannot start before 4 p.m.

To exclude employees from scheduling on certain week days, schedule availabilities of one minute for them, e.g. in the period from 12:00 to 12:01 a.m.

### Create employee availabilities

You can add permanent or temporary availabilities for individual employees in the employee configuration. There is no option to add employee availabilities to several employees at once. Use day model availabilities in shift sequences instead.

1. Go to _WFM > Administration > Scheduling > Employees_{:.breadcrumbs}.
2. Click an **employee** in the list.
3. Scroll to the _Availability_ section on the right (or use the _Availability_ quick link on top).
4. Click the {% icon item-add %} to add a new availability.
5. (Optional) Enter a **Valid from** and **Valid to** date. If the availability is only valid for a certain date range, this limit its {% link_new validity period | features/administration/set-a-validity-period.md %}.
6. To define the weekday, select one or more **Day Types**. Hold CTRL to select multiple entries.
7. Enter a start time into the **From** field and an end time in the **To** field. The times are valid for all selected days.
8. (Optional) If the time frame goes past midnight, e.g. for night shifts, check **Availability Period ends next day**.
9. Click _OK_{:.doc-button}.

The new employee availability is now active.

### Create day model availabilities

You can create day model availabilities and insert them manually or into shift sequences:

1. Go to _WFM > Administration > Scheduling > Day Models_{:.breadcrumbs}.
2. Select the _Availability Period_ type.
3. Enter a unique **Name** and a **Short name**, e.g. _Availability 8:30 AM - 7:00 PM_ and _Avail 830-7pm_.
4. (Optional) Select a **color**. The color can be helpful, e.g. when setting up shift sequences.
5. Enter the **Availability Period Start**. This is the earliest possible time for the shift.
6. Enter the **Availability Period End**. This is the latest possible time for the shift. Alternately, set an **Availability Period Duration**. The maximum value is 48 hours.
7. Click _OK_{:.doc-button}.

You can now manually insert the new day model in the Shift Center or into {% link_new shift sequences | features/administration/shift-sequences.md | #insert-day-models %}.

## Availabilities in Shift Center/Schedules

The Shift Center displays availabilities in each level as `<>` <!-- intentionally code formatted for visibility --> symbol. Hover over the symbol to see a tool tip showing the details.

In the _Availability_ level, you can {% link_new add availabilities | features/scheduling/shiftcenter/add-and-delete-items.md | #add-an-availability %}. In the day cells, you see all availabilities as orange elements. In expanded day cells, employee availabilities appear as white bars underlined in orange.

Note: To show the `<>` symbols in injixo Enterprise WFM on-premise, turn on setting _48188_{:.id-label} _Display of availability information in the Shift Center_.

The Schedules feature can only display availabilities as a _Present_ activity. There is no edit option.

## Editing and deleting availabilities

You can change the start time, end time, or position of manually inserted availabilities (or delete them) in the _Availability_ level in the Shift Center. To open the dialog window, double-click a **day cell**. You can also use the mouse to change an entry.

Learn more about the options on {% link_new how to modify items in the Shift Center | features/scheduling/shiftcenter/modify-items.md %}.

Tip: For temporary changes, you can copy and paste employee and day model availabilities to another (or the same) cell to convert them to manually inserted availabilities.

For permanent changes, edit the shift sequence. To delete day model availabilities from shift sequences, you can also use the {% link_new empty levels feature | features/scheduling/schedules/schedules-empty-levels.md %}. For employee availabilities, go to the _Availability_ section in the [employee configuration](/employee-overview#configure-employee-settings). Instead of deleting the availability entry, you can also terminate the assignment by adding a valid-to date.
