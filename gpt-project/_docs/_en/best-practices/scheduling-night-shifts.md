---
title: Schedule night shifts
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to schedule night shifts with injixo.
---

injixo offers various options to schedule night shifts.

Note:

- injixo will check compliance with rest periods before and after a night shift. This is why you need to consider the entire week.
- For a 24/7 operation, in your forecast, you must calculate staff requirements for Monday of the following week. Otherwise, your employees will not be scheduled correctly on Monday.
- Essential WFM supports scenario 1 only.

## Scenario 1: Night shifts are distributed fairly among all employees

To make sure that night shifts are distributed equally among all employees, you can use {% link_new shift sequences | features/administration/shift-sequences.md %}.

First, calculate how many night shifts you need and how you can distribute them among all employees as just as possible. Note that you may have to redistribute shift sequences when employees enter and leave the company.

{{ 3 | image: 'Shift sequence with distributed night shifts', '80%' }}

Then you can create optimized schedules to assign the remaining shifts.

**Advantage:**

- Night shifts are always distributed fairly among all employees.

**Disadvantages:**

- High manual effort to keep the shift sequences up to date
- No flexibility
- Manual scheduling required in case of sickness or vacation

## Scenario 2: Night shifts are the exception

You can integrate night shifts into your existing {% link_new work time pattern models | best-practices/fair-shift-distribution.md | #optimized-rotation-work-time-pattern-models %}.

For that, you need a dedicated week time pattern for weeks with night shifts. The week time pattern only contains day models for night shifts. Select the week time pattern as _Week Time Pattern - Exception Days_ in your work time pattern model.

You define the number of possible night shifts in the week time pattern (_maximum number of exception days per week_). This way, you can specify the number of night shifts per week.

Since night shifts are only distributed according to need, some employee can go weeks without a night shift.

{{ 2 | image: 'Possible setup of a work time pattern model with a night shift exception week time pattern', '80%' }}

**Advantage:**

- Because most contact centers are typically understaffed and at the limit of their capacities, what should be optional exception days tend to always be scheduled.

**Disadvantages:**

- Since employees get their night shifts randomly and you cannot set a rotation for night shifts, there may be an unfair distribution.
- If understaffing during the day is disproportionately high, night shifts may also be understaffed.

## Scenario 3: Employees are scheduled on a weekly basis for night shifts

In this scenario, you also integrate your night shifts into your existing {% link_new work time pattern models | best-practices/fair-shift-distribution.md | #optimized-rotation-work-time-pattern-models %}.

Create your own week time pattern for the night shift week. However, only add day models for night shifts.

{{ 1 | image: 'Possible construction of a Work Time Pattern Model with a night shift week', '80%' }}

**Advantage:**

- All agents receive a fair distribution of night shifts.

**Disadvantage:**

- Night shifts can only be scheduled for full weeks.

## Scenario 4: Employees can request night shifts

If you want your employees to choose their own night shifts, use the {% link_new shift request procedure | features/scheduling/shift-bidding.md %}. You can use shift bidding for all shifts as usual or night shifts only.

You can run the shift lottery and assign remaining shifts or combine shift bidding with optimized schedules. In the latter case, however, you cannot work with work time pattern models at the same time.

You can limit the maximum number of night shifts by adjusting the {% link_new shift requirement | features/scheduling/shift-requirement.md %}.

{{ 4 | image: 'Adjust the shift requirements table', '80%'}}

**Advantage:**

- Perceived fairness because employees can request night shifts themselves

**Disadvantages:**

- Night shifts must be scheduled manually if not enough employees requested night shifts.
- Night shifts must be requested before other shifts can be scheduled.

## Night shift-related settings

- _48161_{:.id-label} _Mode for defining night work_
- _48121_{:.id-label} _Earliest start time for night work_
- _48122_{:.id-label} _Night work duration_
- _48162_{:.id-label} _Reference time for night shifts_

## Additional constraints on night shifts in contracts

- _2632_{:.id-label} _Check maximum number of booking days with night work per week as specified in the employee's contract_
- _2633_{:.id-label} _Check maximum number of booking days with night work per month as specified in the employee's contract_
- _2634_{:.id-label} _Check maximum number of successive booking days with night work as specified in the employee's contract_
- _2635_{:.id-label} _Ensure minimum number of days off after night work_
- _2636_{:.id-label} _Ensure rest period after night work_
- _2637_{:.id-label} _Ensure maximum number of working days before night work_
