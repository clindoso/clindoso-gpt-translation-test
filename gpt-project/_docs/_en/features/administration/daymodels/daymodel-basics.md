---
title: Understand day models
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn what day model types there are, what you need to consider before you can create a day model and what impact changing a day model has on the schedule.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
---

Day models are templates for shifts. They represent the working day for the people you schedule and define the start and end times of shifts, as well as how many hours a person works per day and when they are available to work. injixo creates schedules based on your day models.

By default, day models you create are automatically assigned to all planning units in your organization. To change this default, {% link_new edit the planning unit | features/administration/create-and-manage-planning-units.md | #limit-day-models %}. During schedule optimization, injixo will only consider day models assigned to the planning unit.

If the day models configured for your planning unit do not cover some working agreements, you can also add personal day models to individual people. During schedule optimization, injixo will only use those personal day models for that person.

Day models contain presence, absence and break activities of a shift. This is why you need to {% link_new add relevant activities to day models | features/administration/daymodels/daymodel-creation.md | #add-activities-to-day-models %}.

Day models are added to {% link_new shift sequences | features/administration/shift-sequences.md %} and can be grouped in {% link_new week time patterns | features/administration/work-time-pattern-models.md | #create-week-time-patterns %}.


## Types of day models

There are three different types of day models. 

> Note
> 
> - Day models of type Fixed Shift are also called fixed day models.<br> 
> - Day models of type Variable Shift are also called variable day models.


| Type                | Description                                                                                                                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fixed Shift         | Shifts with a fixed day model have a fixed start and end time that cannot be moved. There is always only one possible shift resulting from a fixed day model. Fixed day models are typically added to {% link_new shift sequences | features/administration/shift-sequences.md %}.                                      |
| Variable Shift      | Shifts with a variable day model have a flexible start time within a defined time frame. This results in multiple possible shifts. Variable day models that are added to shift sequences will automatically become fixed day models because they are set to the first possible start position of a shift. |
| Availability Period | This day model type is used to define a time range that is shorter than the planning unit's business hours. After inserting shift sequences that contain this day model type, injixo will select day models that are compatible with this availability range during optimization and in shift bidding. You can also use this type to configure availabilities for several people at once.          |

## When to use which day model in scheduling

There is no single use case for when to use which day model type, but the following list provides some general guidance:

- Fixed Shift: Use fixed day models to schedule people with fixed working times. Their shifts will always start and end at a fixed time and cannot be moved within the schedule.
You can use fixed day models in work time pattern models to {% link_new create optimized schedules | features/scheduling/scheduling-optimization.md %}, to define repeating weekly patterns in {% link_new shift sequences | features/scheduling/schedules/schedules-insert-shift-sequences.md %}, or if you use {% link_new shift bidding | features/scheduling/schedules/schedules-shift-bidding.md %}.
- Variable Shift:  Use variable day models to schedule people with flexible working hours. injixo can schedule a person for different shifts using a single day model of this type. This day model is typically used when {% link_new creating optimized schedules | features/scheduling/scheduling-optimization.md %} or in {% link_new shift bidding | features/scheduling/schedules/schedules-shift-bidding.md %}.
- Availability Period: If your planning unit's business hours span a larger time frame than one working day, you can limit injixo's options to schedule people. To limit the availability for several people at once, use day models of type Availability Period and add them to shift sequences. Alternatively, you can {% link_new configure availabilities for individual people | features/administration/availabilities.md %} in the employee settings. Both are considered during schedule optimization if scheduling rule 2611 is activated.

As an alternative to availabilities, you can use {% link_new shift sequences | features/administration/shift-sequences.md %} or week time patterns in {% link_new work time pattern models | features/administration/work-time-pattern-models.md | #create-week-time-patterns %}. You can also use both to rotate early and late shifts, for example.

We recommend creating a limited set of variable day models (combined with {% link_new availabilities of your people | features/administration/availabilities.md | #create-employee-availabilities %}) instead of creating a large number of fixed day models.

## Base activity and shift duration

For fixed and variable day models, you always need to set up a base activity for each day model to define the total shift duration. In both day model types, you can add more activities that overlay the base activity. The duration of the other activities must not exceed the duration of the base activity.

The base activity covers the total time a scheduled person is present during a shift including breaks and other unpaid activities. It is the first activity that you select when creating a new day model, and you cannot delete it or edit it after saving the day model.

The total time of a scheduled shift including breaks is the gross shift duration. After deducting unpaid activities, such as breaks or set-up times, the resulting working time is the net shift duration. You can see the net shift duration under the name Actual time in Schedules and in Shift Center. Note that contracts also specify net times. 

The length of a day model must comply with the working hours in your {% link_new contracts | features/administration/create-contracts.md %}.
For example, a contract with 40&nbsp;hours of weekly working time distributed over 5&nbsp;days a week requires a day model with a net working time of 8&nbsp;hours per day. A contract with 37.5&nbsp;hours per week needs one with 7.5&nbsp;hours.

Use the Present activity as base activity and make sure it is configured as Replaceable. Then, the Job optimization and Create optimized schedules functionalities can replace the Present activity with other activities, as long as they have {% link_new calculated staff requirements | features/forecast/injixo-forecast/staff-requirement.md %} and are configured as Plannable.

### Fixed elements vs. corridors

You can create a corridor element if you add an activity with a duration shorter than the time between the element's start and end time. Corridor elements overlay all fixed elements in a shift. Optimized scheduling will move corridor elements around to optimize coverage. Corridors as such can overlap, but activities within two corridors cannot.

When you manually insert a day model into the schedule, corridor elements are placed at the earliest possible time of the corridor. You can manually move corridors within their defined intervals.

When the duration of a corridor element exactly matches the configured start and end time of the element, a fixed element is created instead.

