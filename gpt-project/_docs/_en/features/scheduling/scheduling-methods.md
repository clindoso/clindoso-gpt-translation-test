---
title: Scheduling methods
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

injixo offers different scheduling methods, which you can use on their own or as a {% link_new combination | features/scheduling/combined-scheduling-methods.md %}.

The different scheduling methods are designed to fit different use cases. All scheduling methods consider the information configured in your people's {% link_new contracts | features/administration/create-contracts.md %}, such as the number of working days, the working hours per day, week, or month, and other scheduling parameters.

## Prerequisites

Before you start using scheduling methods, make sure that you have set up the following configuration data in _Plan > Configuration_{:.breadcrumbs}:

- Skills
- Activities
- Day models
- Planning units
- Contracts
- Employees

Some scheduling methods might also require that you set up other configuration data, e.g. shift sequences or work time pattern models.

## Fixed scheduling

The fixed scheduling method is based on {% link_new shift sequences | features/administration/shift-sequences.md %}. A shift sequence is a weekly pattern of day models or activities that defines on which days a person works, as well as their exact shift start and end time. As a consequence, fixed scheduling is the most consistent scheduling method, but it offers the least flexibility.

Schedules created using shift sequences can be the same every week, or change in intervals from 2 to 53 weeks.

After the schedule has been created, you can still run {% link_new Optimize breaks | features/scheduling/schedules/break-optimization.md %}, or the {% link_new Job optimization | features/scheduling/schedules/schedules-job-optimization.md %} to further optimize your schedule.

**Optimize breaks** moves planned breaks to the time slot where they have the least impact on your coverage. injixo can only move breaks configured within a {% link_new corridor in a day model | features/administration/daymodels/daymodel-basics.md | #fixed-elements-vs-corridors %}.

**Job optimization** can replace activities configured as replaceable with other plannable activities to achieve the best possible coverage for all activities, based on their staff requirements. The start and end times of shifts remain unchanged. **Job optimization** can also modify break times within a schedule, in the same way **Optimize breaks** does.

## Optimized scheduling

The optimized scheduling method offers the most flexibility. In this method, you use the {% link_new Create optimized schedule | features/scheduling/schedules/schedules-optimized-schedules.md %} functionality to automatically create a full schedule. injixo will ensure the best possible coverage for all activities with as few people as possible.

By default, the **Create optimized schedule** functionality can schedule people using any {% link_new day model | features/administration/daymodels/daymodel-basics.md %} that is assigned to their planning unit and is compatible with their contract. 

Depending on your configuration, using different day models in scheduling can lead to very inconsistent schedules, e.g. people could be scheduled to work the night shift on a Monday, the afternoon shift on a Tuesday, and the morning shift on a Wednesday.

To define which day models can be used to create a schedule, configure {% link_new work time pattern models | features/administration/work-time-pattern-models.md %}. A work time pattern model is made up of {% link_new week time patterns | features/administration/work-time-pattern-models.md | #create-week-time-patterns %}, and defines how day models are assigned to your people. With work time pattern models you can create repeating patterns of shifts, and set scheduling constraints for the **Create optimized schedule** functionality.

To schedule people using work time pattern models, assign one work time pattern model to each person. You cannot assign several work time pattern models to a person for the same validity period.

### Fully flexible shifts

To create schedules with fully flexible shifts, create work time pattern models of {% link_new type A | features/administration/work-time-pattern-models.md | #types-of-work-time-pattern-models %}, and assign them to your people.

With type A, injixo can select any day model included in the work time pattern model for every day of every week, as long as it complies with a person's contract.

This method creates the best schedules to meet your operational needs. At the same time, it can create very inconsistent schedules that negatively impact your people. To reduce this negative impact, you can exclude certain shifts for some people by assigning individual day models to them, or by using [availabilities](#availabilities).

### Rotating flexible shifts

To create schedules with rotating flexible shifts, create work time pattern models of {% link_new type B, C, or D | features/administration/work-time-pattern-models.md | #types-of-work-time-pattern-models %}, and assign them to your people.

With types B, C and D, you define a specific order that injixo follows when selecting the day models from those available in the selected work time pattern model and compatible with people's contract. You can also define a fixed start time for the shifts, or a time frame within which shifts start.

### Availabilities

You can use {% link_new availabilities | features/administration/availabilities.md %} to configure that people are not available to work on a day, or during some hours. Availabilities add further scheduling restrictions to those defined by contracts and planning units' business hours.

When people have availabilities assigned, they can only be scheduled for shifts that fit into the time frames in which they are available.

## Shift bidding

If you use {% link_new shift bidding | features/scheduling/schedules/schedules-shift-bidding.md %}, the final schedule is only created after people have had the chance to request their preferred shifts in injixo Me.

To create a schedule using Shift bidding, follow these steps:

1. Define how many shifts you need for a {% link_new scheduling period | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %}.
2. {% link_new Generate shifts | features/scheduling/schedules/schedules-shift-bidding.md | #generate-shifts %} based on forecasted staff requirements.
3. Set the status of your scheduling period to **Published**. People can request two shifts per day (up to 10 in total).
4. Start a {% link_new shift lottery | features/scheduling/shift-bidding.md | #lottery-of-requested-shifts %} for the shifts that have been requested.
5. Assign the remaining shifts. People whose requests were not fulfilled during the lottery will be scheduled in this step.

After the schedule has been created, you can still run the {% link_new Job optimization | features/scheduling/schedules/schedules-job-optimization.md %} to optimize the scheduled activities and the positions of breaks.

> Use the activity Present if you combine shift bidding and **Job optimization**
>
> If people can request shifts in injixo Me but you want to run **Job optimization** later, only use the default system activity Present (activity ID: 1) as activity in the day models. This way you avoid that people request shifts with specific activities but are then assigned completely different activities by the **Job optimization**.
