---
title: Available scheduling methods
promote-service: new-planner-training
description: Learn about the various scheduling methods in injixo.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/combined-scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/set-a-validity-period.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
---

In this article, you will learn:

- which scheduling methods can be used.
- which scheduling method can be used for which use case.

You can either use each scheduling method on its own or {% link_new combine | features/scheduling/combined-scheduling-methods.md %} them.

The scheduling methods consider the information from the {% link_new contracts | features/administration/create-contracts.md %} that are assigned to employees. Contracts contain the number of working days, the working hours per day, week, or month, and other scheduling parameters.

## Fixed scheduling

Fixed scheduling offers the least flexibility. This scheduling method is based on {% link_new shift sequences | features/administration/shift-sequences.md %}.

Shift sequences define:

- the working weekdays of an employee
- the exact start and end time of the shift for each working day

Schedules created from these shift sequences can be the same every week or change in intervals from 2 to 53 weeks.

After the schedule has been created, you can optimize the following elements:

- positions of breaks in [corridors](/daymodel-basics#fixed-elements-vs-corridors)
- {% link_new replaceable activities | features/administration/activity-types-and-properties.md | #activity-properties %}

## Optimized scheduling

Optimized scheduling offers the most flexibility. Use {% link_new Create optimized schedules | features/scheduling/schedules/schedules-optimized-schedules.md %} to automatically create a full schedule. injixo will ensure the best possible coverage for the different activities with the lowest possible number of employees.

To define which shifts are available for scheduling, use {% link_new work time pattern models | features/administration/work-time-pattern-models.md %}.

### Fully flexible shifts

For fully flexible shifts, assign {% link_new type A | features/administration/work-time-pattern-models.md | #types-of-work-time-pattern-models %} work time pattern models to your employees.

Any shift that is available according to the work time pattern model and that complies with the employee's contract can be scheduled on any day.

To increase the employees' acceptance of your schedules, you can exclude certain shifts by adding personal day models to employees or by using [availabilities](#availabilities).

### Rotating flexible shifts

For rotating flexible shifts, assign {% link_new type B, C, or D | features/administration/work-time-pattern-models.md | #types-of-work-time-pattern-models %} work time pattern models to your employees.

Shifts that are available according to the selected work time pattern model, and comply with the employee's contract, are scheduled in a specific order. They can even have the same start time every day.

### Availabilities

{% link_new Availabilities | features/administration/availabilities.md %} can complement optimized scheduling to limit the shift options.

## Shift bidding

In {% link_new shift bidding | features/scheduling/schedules/schedules-shift-bidding.md %}, the final schedule is only created after involving your employees. They can request their preferred shifts in injixo Me beforehand.

Workflow overview:

1. Define how many shifts you need.
2. Generate shifts based on forecasted staff requirements.
3. Set the status of your scheduling period to **Published**. Your employees can request two shifts per day (up to 10 in total).
4. Start a {% link_new shift lottery | features/scheduling/shift-bidding.md | #lottery-of-requested-shifts %} for the requested shifts.
5. Assign the remaining shifts. Employees whose requests were not fulfilled during the lottery will be scheduled in this step.

## Overview of scheduling methods and configuration items

Each scheduling method requires you to set up specific configuration items in _Plan > Configuration_{:.breadcrumbs}. The following table provides an overview of the required and optional configuration items per scheduling method.

|                          | Fixed scheduling  | Optimized scheduling | Shift bidding |
|--------------------------| ----------------  | ---- ----------------| --------------|
| Skills                   | Required          | Required             | Required      |
| Activities               | Required          | Required             | Required      |
| Day models               | Required          | Required             | Required      |
| Planning units           | Required          | Required             | Required      |
| Contracts                | Required          | Required             | Required      |
| Employees                | Required          | Required             | Required      |
| Shift sequences          | Required          | --                   | Optional      |
| Planning calendar        | Optional          | Optional             | Optional      |  
| Selections               | Optional          | Optional             | Optional      | 
| Week time patterns       | --                | Optional             | --            |
| Work time pattern models | --                | Optional             | --            |
