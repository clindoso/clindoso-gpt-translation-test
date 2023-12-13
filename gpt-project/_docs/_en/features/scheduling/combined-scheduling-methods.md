---
title: Combine scheduling methods
product_label:
  - advanced
  - enterprise
  - classic
description: Combine the various scheduling methods to meet the demands of your business.
---

All available {% link_new single scheduling methods | features/scheduling/scheduling-methods.md %} can be combined in a variety of ways to balance the needs of your agents and your business.

The following examples illustrate a few of the common ways to combine scheduling methods, which you can use as presented or as inspiration to create your own combinations.

## Fixed scheduling and rotating/fully flexible shifts

If you want to have a majority of flexible schedules, you can assign work time pattern models to your flexible employees. If some employees have strict restrictions on their schedule or you want to reward top performers or senior agents, you can define shift sequences for these employees.

During scheduling, insert your shift sequences first, then run scheduling optimization as normal. Your rotating or flexible shifts will be optimized around the coverage provided by your shift sequences.

Alternately, if you have employees who need a certain shift on certain days of the week, you can create a shift sequence defining these days, with the rest of the week blank, and assign the employee a work time pattern model.

When you insert the shift sequence and run a full optimization, the blank days will be filled in by the flexible or rotating shifts, following the rules of the contract to create a complete schedule.

## Rotating flexible and fully flexible shifts

If you want some employees to follow a rotating schedule, while others are more flexible or will always work a flexible shift during a certain time of day, simply assign type B or D work time pattern models to the employees on rotating schedules, and type A work time pattern models to everyone else.
The rotating employees will follow their rotations, and the flexible employees will be optimized to fulfill the rest of your requirements.

## Rotating flexible shifts and availability

If an employee works a rotating shift, but has availability restrictions at certain times (for example, they cannot work past 5 PM on a Wednesday), simply define the availability restriction and assign a work time pattern model as normal.

On weeks where the employee works a morning shift, their availability window will allow them to be scheduled on Wednesday. However, on weeks where the employee works an evening shift, the availability window will block them from being scheduled on Wednesdays, and the schedule optimizer will give them schedules on other days of the week.

## Fixed scheduling and availability

You can add day models of type _Availability Period_ in shift sequences to influence the scheduling result on particular days. See the two examples below.

**Shifts on every other weekend**:

1. Create a day model of type _Availability Period_ with a time frame of 0 a.m. to 00:01 a.m. as a blocker.
2. Add the day model in a shift sequence every other weekend (leave all other days blank).
3. Assign the shift sequence to employees and insert the shift sequence before you create optimized schedules.

injixo does not schedule any shifts for the employee every other weekend and optimizes the other days.

**Night shifts every other week**:

1. Create a day model of type _Availability Period_ with a time frame of 12 p.m. to 12 a.m.
2. Add the day model for each day of a week in a shift sequence (leave all other days blank).
3. Assign the shift sequence to employees and insert the shift sequence before you create optimized schedules.

injixo schedules the night shift for the employee in the weeks with availability (according to the work time pattern model). For other weeks, injixo schedules any shift.
