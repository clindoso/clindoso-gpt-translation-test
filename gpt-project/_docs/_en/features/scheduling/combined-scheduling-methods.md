---
title: Combine scheduling methods
product_label:
  - advanced
  - enterprise
  - classic
description: Combine the different scheduling methods to meet your business demands.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/availabilities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-time-pattern-models.md
---

You can combine all {% link_new scheduling methods | features/scheduling/scheduling-methods.md %} in many ways to create schedules that balance the needs of your people and those of your business.

The following examples show some common use cases for combining scheduling methods. You can also use other scheduling methods combinations to best meet the needs of your organization.

## Use case 1: People with flexible shifts plus people with specific working hours or days

For this use case, you can combine fixed scheduling with either rotating flexible shifts, or fully flexible shifts.

To plan your people using this combination, you first need to configure the configuration data shown in the following table, and assign it to the relevant people:

| People with flexible shifts                                  | People with specific working hours or days                                                                                                                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Assign the work time pattern models you want to use to them. | Create specific shift sequences defining the hours or days when they should work, and leave the rest of the week blank.<br>Assign the shift sequence and the relevant work time pattern models to them. |

To schedule your people, follow these steps:

1. Insert your shift sequences.
2. Use the **Create optimized schedule** functionality.<br>injixo will schedule your rotating and fully flexible shifts to complement the coverage provided by the shift sequences.

## Use case 2: People with rotating shifts plus people with flexible shifts

For this use case, you can combine rotating flexible shifts and fully flexible shifts.

To plan your people using this combination, you first need to assign the configuration data to the relevant people, as shown in the following table:

| People with rotating flexible shifts                    | People with fully flexible shifts                  |
| ------------------------------------------------------- | -------------------------------------------------- |
| Assign work time pattern models of type B or D to them. | Assign work time pattern models of type A to them. |

Use the **Create optimized schedule** functionality.<br>People with rotating flexible shifts will be assigned the rotation defined by their work time pattern models, and people with fully flexible shifts will fill up the rest of the schedule.

## Use case 3: People with rotating shifts and restricted availability

This use case refers to people who work rotating shifts but are not available at specific times, e.g. they cannot work past 5 PM on Wednesdays.

For this use case, you can combine availabilities and rotating flexible shifts.

1. Configure {% link_new availabilities | features/administration/availabilities.md %} for your people that define when they cannot work. In this case, they are available on Wednesdays only until 5 PM.
2. Assign to them the relevant work time pattern models.

For weeks when the person works the morning shift, they will be scheduled on Wednesday.<br>For weeks when the person works the evening shift, they will not be scheduled on Wednesday, and they will be planned for other days of the week.

## Use case 4: People with fixed shifts and punctually restricted availability

This use case refers to people who work fixed shifts but have a more restricted availability on some particular days, e.g. they work night shifts, or during the weekend, but only every other week.

For this use case, you can add {% link_new day models of the type Availability period | features/administration/daymodels/daymodel-basics.md | #types-of-day-models %} to {% link_new shift sequences | features/administration/shift-sequences.md %} to influence the scheduling result on particular days.<br>See the two examples below.

To plan people to work shifts every other weekend, follow these steps:

1. Create a day model of type Availability Period with a time range from midnight (0:00) to 0:01 AM as a blocker.
2. Add the day model to one weekend in a shift sequence with 14 days, and leave all other days blank.
3. Assign the shift sequence to the relevant people.
4. Insert the shift sequence into your schedule.
5. Use the **Create optimized schedule** functionality.

injixo does not schedule any shifts every other weekend, and optimizes the remaining days.

To plan people to work night shifts every other week, follow these steps:

1. Create a day model of type Availability Period with a time range from midnight (0:00) to noon (12:00).
2. Add the day model to each day of a week in a shift sequence with 14 days, and leave all other days blank.
3. Assign the shift sequence to the relevant people.
4. Insert the shift sequence into your schedule.
5. Use the **Create optimized schedule** functionality.

injixo schedules the night shift in the weeks when people are available, following the work time pattern model assigned to each person. For other weeks, injixo can schedule any shift that complies with the work time pattern model.
