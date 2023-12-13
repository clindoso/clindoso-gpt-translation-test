---
title: Set a reference date
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how the reference date is used by shift sequences and work time pattern models to represent repeating schedule patterns.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-time-pattern-models.md
---

When you assign {% link_new shift sequences | features/administration/shift-sequences.md %} and {% link_new work time pattern models | features/administration/work-time-pattern-models.md %} to an employee, you need to set a starting point (reference date) for the rotation. In this article, we explain how to use reference dates.

## Fixed point for scheduling

You may have noticed that Shift Sequences refer to "Week 1", "Week 2", and so forth. Similarly, Week Time Patterns within Work Time Pattern Models are listed in Position 1, Position 2, etc.

In both cases, you will typically only specify a small number of weeks, equal to the length of the pattern you want to repeat, rather than specifying a pattern for the entire year.

In order to create a schedule, injixo needs to know for any day of the week whether it should use the pattern for Week 1, Week 2, etc. The reference date provides a fixed point which allows injixo to answer this question.

> Reference Date vs Valid From/Valid To Date
>
> Note that the Valid From/To Dates and the reference date have completely different purposes. The reference date is always mandatory, and is used to define which week of a Shift Sequences or which Week Time Pattern of a Work Time Pattern Model is used. Meanwhile, Valid From/To Dates are always optional, and are used to specify when a given configuration element is associated with an Employee or Planning Unit.

## Example: Shift sequences

When inserting Shift Sequences, injixo treats the reference date as the first day of the full shift sequence pattern. So, if the reference date is January 1, and the shift sequence is 14 days, January 1-7 will be week 1, and January 8-14 will be week 2.

To visualize this, imagine you had a calendar which was long strip of paper, with a square for each day of the year laid out in order from left to right. You can think of your shift sequence as a long stamp, with each shift printed in a square on the stamp (including blank days). You start by placing the stamp with the first square over the reference date, and stamp the schedules into place. Then, on the first day that you didn't stamp, you press the stamp down again.

This allows you to repeat your Shift Sequence forever, just by using one _date_ as your initial _reference_ point.

## Example: Work time pattern models

Just like with Shift Sequences, Work Time Pattern Models treat the reference date as the first day of the weekly rotation.  
So, if the reference date is January 1, and the Work Time Pattern Model is two weeks long, the first Week Time Pattern is used in week 1 (January 1-7) and the second Week Time Pattern is used in week two (January 8-14).
The fixed order of the Week Time Patterns only applies to Work Time Pattern Models of type **B - Fixed Rotation** and **D - Combined Rotation (A/B)**.

## Always use the first day of the Week

The reference date must always be set to the first day of the week, as defined in setting _48420_{:.id-label} _First day of the scheduling week_. If the reference date is set to any other day of the week, the Shift Sequence or Work Time Pattern Model will switch to a new week after 7 days (or the end of the Shift Sequence, if it is less than 7 days).

For example, if March 1st is a Wednesday, and is set as the reference date, then a Shift Sequence will treat Wednesday the 1st through Tuesday the 7th as Week 1, and Wednesday the 8th through Tuesday the 14th as Week 2. This will also insert the schedule specified for Monday in the Shift Sequence into Wednesday.

In this scenario, a type B or D Work Time Pattern Model will use the Week Time Pattern defined in position 1 for week 1 (Wednesday to Tuesday), and the Week Time Pattern defined in position 2 for week 2, starting on Wednesday, March 8.

## Best practice: The same reference date for multiple employees

As a best practice, we recommend setting the same reference date (including the year) for all employees in injixo, regardless of when they are hired. This ensures that injixo uses the same pattern for employees with the same shift sequence or Work Time Pattern Model for any day of the year.

Although it is possible to set reference dates as different dates to offset the patterns between employees, this can be difficult to keep track of and can cause errors down the line if not well documented. Although using the same reference date for all employees will require more rows in a Shift Sequence or more Work Time Pattern Models, it will be far easier to troubleshoot in the future.
