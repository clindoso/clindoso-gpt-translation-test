---
title: Create work time pattern models
redirect_from:
  - /wtpm_creating/
  - /week_time_patterns/
  - /wtpm_overview.md/
  - /understanding_wtpms/
product_label:
  - advanced
  - enterprise
  - classic
description: Use work time pattern models in your schedule optimization to ensure that employees are not simply given random shifts.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/reference-date.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/scheduling-split-shifts.md
---

A work time pattern model is made up of [week time patterns](#create-week-time-patterns) and defines how {% link_new day models | features/administration/daymodels/daymodel-basics.md %} are assigned to your people.

The following image shows the setup of day models and week time patterns in a work time pattern model.

{{ 1 | image: 'Structure of a work time pattern model' }}

With work time pattern models you can create repeating patterns of shifts, and set scheduling constraints for the **Create optimized schedule** functionality.<br>
Work time pattern models have the following benefits:

- They define which day models can be used to plan a person.
- People are not assigned shifts in random combinations.
- They define starting times for shifts.
- They define an order for the assignment of day models.

As an alternative to work time pattern models, you can use shift sequences or configure {% link_new availabilities | features/administration/availabilities.md %} for your people.

## Prerequisites

To be able to use work time pattern models, make sure the following applies:
- You have created {% link_new day models | features/administration/daymodels/daymodel-creation.md %} and [week time patterns](#create-week-time-patterns), and assigned day models to the week time patterns.
- Each work time pattern model contains at least one week time pattern.
- Each week time pattern contains at least one {% link_new day model | features/administration/daymodels/daymodel-basics.md %}.
- You have assigned work time pattern models to your people.

## Create week time patterns

A week time pattern is a group of day models. You can group day models by any criteria, e.g. shift length, activities involved, starting time, etc.<br>

You can only use week time patterns as part of a work time pattern model. For a working week, injixo will schedule people according to the day models included in the week time pattern. This way, you can ensure that your people have fairer and more consistent working hours.

To create a week time pattern, follow these steps:

1. Go to _Plan > Configuration > Week time patterns_{:.breadcrumbs}.
2. Click the New icon {% icon item-add | icon-only %} in the upper left.
    A configuration panel opens on the right side.
3. Configure the settings of the week time pattern:<br>
  **Name**: Enter a unique name (max. 50 characters).<br>
  **Abbreviation**: Enter the name or a shorter version of it (max. 25 characters).<br>
  **Color**: The color can help you identify the week time pattern in a list.<br>
  **Maximum number of exception days per week**: [Exception days](#exception-days) allow injixo to break the rules of the work time pattern model to better meet staff requirements.
4. Click _OK_{:.doc-button}.

You can now add day models to your week time pattern.

### Add day models to a week time pattern

1. In the configuration panel of the week time pattern, go to the **Day models** section and click the Add icon {% icon item-add | icon-only %}.
2. Select one or more day models from the list.
3. Click _OK_{:.doc-button}.

You can add both {% link_new fixed and variable day models | features/administration/daymodels/daymodel-basics.md | #types-of-day-models %} to a week time pattern. If you use variable day models, the **Create optimized schedule** functionality can determine the optimal starting time of the shifts within the constraints set by the day model.

> Note
>
> injixo can only schedule day models that are assigned to the planning unit to which the person is assigned. If you have {% link_new limited the day models | features/administration/create-and-manage-planning-units.md | #limit-day-models %} in your planning unit, the day models you expect based on your work time pattern model may not be used.
>
> injixo can replace replaceable activities with plannable activities within a shift. For this to work, use variable day models for each shift duration a contract requires, and use the system activity Present (ID: 1) as {% link_new base activity | features/administration/daymodels/daymodel-basics.md | #base-activity-and-shift-duration %}. Do not define day models for each individual activity.

## Create work time pattern models

1. Go to _Plan > Configuration > Work time pattern models_{:.breadcrumbs}.
2. Click the New icon {% icon item-add | icon-only %} in the action bar.
3. Configure the settings of the work time pattern model:<br>
  **Name**: Enter a unique name (max. 50 characters).<br>
  **Abbreviation**: Enter the name or a shorter version of it (max. 25 characters).<br>
  **Color**: The color can help you identify the work time pattern model in a list.<br>
  **Type**: The [type](#types-of-work-time-pattern-models) determines how injixo uses the work time pattern model.<br>
  **Week Time Pattern - Exception Days**: Select the week time pattern that should be planned for [exception days](#exception-days).
4. Click _OK_{:.doc-button}.

You can now add week time patterns to your work time pattern model.

### Add week time patterns to a work time pattern model

1. In the configuration dialog of the work time pattern model, click the Add icon {% icon item-add | icon-only %} in the **Week time patterns** section.
2. Choose a **Week time pattern** from the list.
3. Set a **Position**.<br>
  If you add several week time patterns, click the {% icon down-arrow-blue %} and the {% icon up-arrow-blue %} to change the position.
4. Click _OK_{:.doc-button}.

### Position

The position of week time patterns within work time pattern models is relevant when you use work time pattern models of [type B or D](#types-of-work-time-pattern-models). injixo will assign the week time patterns in the order configured here.

Use the {% icon down-arrow-blue %} and the {% icon up-arrow-blue %} to define the position of the week time patterns.

## Types of work time pattern models

| Type | Name               | Week time pattern use                                                      | Day model assignment | Shift start time              | Effect             |
| ---- | ------------------ | -------------------------------------------------------------------------- | -------------------- | ----------------------------- | --------------------------------- |
| A    | Flexible Selection | injixo can select any day model from any of the week time patterns included for every day of every week. | injixo can use any day model from any of the week time patterns. | Flexible    | Depending on your organization’s opening hours, type A can result in a shift distribution that seems random or stressful to your people. For example, a person could have to work early on Monday, at night on Tuesday, and late on Wednesday, etc. |
| B    | Fixed Rotation     | injixo plans the week time patterns in the order defined by their positions. | For each week, injixo will choose the day model that best covers the staff requirements. | Fixed    | When you assign this type of work time pattern model to people, you must set a {% link_new reference date | features/administration/reference-date.md %}. The reference date defines when the work time pattern model is first used.<br> Each person is assigned the same day model for the entire week, e.g. starting at 9&nbsp;AM from Monday to Friday. This rule can only be broken by defining exception days. This is the most consistent shift assignment of all four types. |
| C    | Variable Rotation  | injixo does not respect the defined position of week time patterns. | injixo chooses one day model for the whole week. | Fixed    | People can be assigned any week time pattern to best meet staff requirements. Since the shifts start at the same time, people have consistent working hours throughout the week. |
| D    | Combined Rotation (A/B) | injixo respects the position defined for the week time patterns. | injixo chooses one day model for the whole week.| Flexible (within a time frame)    |  Based on staff requirements, injixo can schedule people with early shifts to start working between 8&nbsp;AM and 10&nbsp;AM. With type D, injixo can schedule more flexibly to best meet staff requirements, while at the same time assigning fairly consistent schedules to your people. |



## Exception days

Exception days allow injixo to break the rules defined by the [work time pattern model type](#types-of-work-time-pattern-models) in use. For example, you could use exception days to plan one night shift in a week in which the person usually works the morning shift.<br>

Exception days prioritize staff requirements and ensure better coverage. However, they result in less consistent schedules for your people.

To plan exception days, follow these steps:

1. [Create a separate week time pattern](#create-week-time-patterns) and add to it the day models you want to use as exceptions.
2. In the configuration dialog of the week time patterns that you want to use for the standard shift, define the number of exceptions days per week.
3. In the configuration dialog of the work time pattern model, select the week time pattern you want to use for exception days.

When choosing a day model for the week, injixo cannot use the day models defined for exception days. Make sure that all configuration data required for scheduling (i.e. all day models used, as well as the work time pattern model) complies with the {% link_new work time guidelines | features/administration/create-contracts.md | #work-time-guidelines %} defined in the person's contract. If the day model used for the week matches the contract, injixo can substitute the original day model with one defined for exception days, to better meet staff requirements.

## Assign work time pattern models to people

1. Go to _Plan > Configuration > Employees_{:.breadcrumbs}.
2. Select a person from the list.
3. Click the Add icon {% icon item-add | icon-only %} in the **Work Time Pattern Models** section.<br>
   A configuration panel opens on the right side.
4. Configure the settings:<br>
  **Valid from/Valid to**: Set a {% link_new validity period | features/administration/set-a-validity-period.md %}.<br>
  **Work time pattern model**<br>
  **Reference date**: Set a {% link_new reference date | features/administration/reference-date.md %} when the work time pattern model starts to be used.
5. Click _OK_{:.doc-button}.

Use the {% link_new mass update | features/administration/mass-update.md %} functionality to assign a work time pattern model to several people at once.

> Caution when using mass update to assign work time pattern models of type B
>
> If you use the mass update functionality and set the same reference date for everyone, all people will be scheduled with the same week time pattern at the same time.
>
> Instead, select smaller groups for the mass update, and set subsequent Mondays as reference dates for them. This way, each group will start their rotation in a different week.

## Examples

### Example A: Fixed rotation with early and late shifts

Configure a work time pattern model of type B (fixed rotation), and assign three different week time patterns to it. Remember to define the position for the week time patterns.

- Week time pattern 1 (position 1) contains day models for morning shifts (shifts start between 7&nbsp;AM and 9&nbsp;AM).
- Week time pattern 2 (position 2) contains day models for evening shifts (shifts end at 11&nbsp;PM).
- Week time pattern 3 (position 3) contains day models for afternoon shifts (shifts start between 11&nbsp;AM and noon).

With this work time pattern model, people will rotate consistently between one week with morning shifts, one week with evening shifts, and one week with afternoon shifts. 

While this requires certain flexibility, people have very consistent working hours throughout the week.

### Example B: Exception days for night shifts

Configure a work time pattern model with three different week time patterns. Configure a maximum of two exception days per week.

- Week time pattern 1 contains day models for morning shifts.
- Week time pattern 2 contains day models for evening shifts.
- Week time pattern 3 contains day models for night shifts (select this one in the drop-down menu **Week Time Pattern - Exception Days**).

With this work time pattern model, people will alternate between morning shifts in the first week and evening shifts in the following week. However, because you have defined two exception days, people can also be assigned two night shifts per week, if this is the best assignment to meet staff requirements.

<!-- TODO: very special example, add some more context  -->
<!-- ### Example: Performance-Based Scheduling With WTPMs and Preferred Day Models

Use Work Time Pattern Models and preferred day models  for Performance-Based Shift Assignment.

* Within the Week Time Patterns, assign the shifts according to agents' performance.
* Assign the Work Time Pattern Model to an agent with a validity period. Adjust it regularly according to performance scores.

For your high achievers you can pick some of the day models and assign them directly to these employees as personal day models. The AutoScheduler will only use these day models while generating schedules. This ensures that out-of-favor shifts are not assigned to high performing agents. -->

<!-- TODO: Example: normal use case scheduling different hours or working days in different weeks -->
<!-- ### Example: Scheduling Different Number of Working Days or Hours in Different Weeks -->
<!-- There is a bad German article /de/scheduling-different-wtm/ using WTPM Type B with two WTMs 4x10 and 5x8 hour shifts, with Autoscheduler contract parameter. minimum days per week with value 4 and scheduling parameter 2602 with value 10:00 -->
