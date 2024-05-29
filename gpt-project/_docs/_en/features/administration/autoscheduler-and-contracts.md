---
title: Configure contracts
product_label:
  - advanced
  - enterprise
  - classic
description: Learn how contract settings impact schedule optimization.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/resolve-optimization-issues.md
---

A contract specifies rules about working times and working days that apply to all people with that contract.

The Create optimized schedules functionality can only schedule the expected number of hours per week if there are suitable day models, i.e. the contract must allow the day model duration. Depending on how flexible your daily working hours are, you need to {% link_new create one or more day models | features/administration/daymodels/daymodel-creation.md %} that will provide the corresponding net working times for each available working time combination.

A contractual weekly target working time can be distributed differently over the working days of a week, for example, 20 hours:

- four hours on five days.
- five hours on three days.
- four hours on three days and eight hours on the last day.

{{ 1 | image: 'Contract General', '50%' }}

## Working days per week

To set the maximum working days per week for a person to be scheduled, select a value in the _Working Days/Wk_ field. Create optimized schedules adheres to this value.

## Working time guidelines

Optimized scheduling checks the daily and weekly values of the {% link_new Work Time Guidelines | features/administration/create-contracts.md %}. Monthly values are checked while saving the optimization result. You can only schedule people if there are day models with a corresponding length (net working time).

For contracts with a weekly working time of 40 hours for five working days, a pre-scheduled full-day vacation activity will count as eight hours paid working time. injixo can schedule day models for the remaining 32 hours on the remaining four days.

## Working hours for each day of the week

If you set up {% link_new Working hours for each day of the week | features/administration/create-contracts.md %}, the person's day models, availability, or work time pattern models must allow the values for the single days.

## AutoScheduler parameters

In the **AutoScheduler Parameters** section, you can set special rules for the optimization.

<!-- rework later, I guess that the labels will change with the new contracts UI anyway -->

- **Maximum Number of Successive Workdays**  
   Can be blank for planning units without opening hours on weekends.
- **Minimum Number of Days Off per Week**  
   Can be blank for planning units without opening hours on weekends.
- **Minimum Number of Successive Days Off per Week**  
   Can be blank for planning units without opening hours on weekends.
- **Maximum Number of Consecutive Days Off**  
   The value is checked over several weeks.
- **Minimum Rest Period Between Two Shifts (in Hours)**
- **Minimum Number of Working Days per Week**  
   Specify the minimum number of working days per week. If left blank, injixo will use the general value defined in _Working Days/Wk_. For example, if people can work between two and four days, enter value 2.
- **Target Work Account instead of Weekly Contractual Target**  
   By default, injixo uses the work time guidelines. If you activate this option, you can determine the working time for each week based on calculated {% link_new Target work accounts | features/scheduling/planning-periods/target-work-accounts.md %}.
- **Max. 1 Working Saturday in x No. of Weeks**  
   Set the number of weeks (1-5) in which a person can work on one Saturday at most. For example, a value of 2 means every other Saturday.
- **Assignment of a Workday Following a Full-Day Vacation**  
   Forces Create optimized schedules to schedule a working day after a full-day vacation. If the person has several consecutive days of time off, the working day is scheduled after the last day off.

> The entered values must not contradict each other.
>
> For example, do not enter 4 days off per week and a minimum of 5 working days per week at the same time.

## Scheduling parameters

Create optimized schedules can only schedule one day model per day and ignores scheduling parameter _2613_{:.id-label} _Maximum number of shifts per day_. This parameter only applies for lottery and assignment in shift bidding.

Some scheduling parameters are already checked while optimizing, e.g.:

- _2621_{:.id-label} _Maximum number of Saturdays Worked per Month_
- _2622_{:.id-label} _Maximum number of Sundays Worked per Month_

Other scheduling parameters are only checked while saving the schedule, e.g. _2620_{:.id-label} _Minimum number of weekends off per month_.

## How are parameters considered?

When you manually change the schedule, scheduling rules are considered based on the {% link_new status of the scheduling rules | features/administration/create-contracts.md | #scheduling-rules %}.

Create optimized schedules always interprets the following scheduling rules as set to inviolable (red):

- _2601_{:.id-label} _Check rest period between two working days as specified in the employee's contract_
- _2605_{:.id-label} _Check skills_
- _2607_{:.id-label} _Check whether employees belong to relevant planning unit_
- _2608_{:.id-label} _Check employee's scheduling bar_ <!-- obsolete? : (if defined for a person) -->
- _2609_{:.id-label} _Check company membership_
- _2611_{:.id-label} _Check employee availability_
- _2621_{:.id-label} _Check maximum number of Saturdays scheduled for work per month as specified in the employee's contract_
- _2622_{:.id-label} _Check maximum number of Sundays scheduled for work per month as specified in the employee's contract_
- _2631_{:.id-label} _Check contractual ban on work scheduled for holidays (both day models and activities)_
- _2651_{:.id-label} _Check assignment of day models to planning units_
- _2661_{:.id-label} _Check day model assignment to the employee_

## How to track scheduling errors?

Errors in the {% link_new scheduling report | best-practices/resolve-optimization-issues.md %} appear with the respective scheduling rule ID, e.g.:

```
Saving the activities ...
failed: [2622] 'The employee 'Ashman, Christian' is allowed to have 2 workdays on Sundays. With the assignment from 28.10.2012 the employee has 3 working days on Sundays.''
```
