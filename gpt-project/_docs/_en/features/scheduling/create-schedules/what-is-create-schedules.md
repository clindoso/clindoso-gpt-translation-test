---
title: Create schedules
product_label:
  - advanced
  - enterprise
toc: true
description: Learn about the _Create schedules_ functionality and the current state of development.
beta-feature: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
---

Create schedules automatically generates a full schedule for your people. The schedule considers your configuration and staff requirements for optimal coverage.

Create schedules will eventually replace the {% link_new *Create optimized schedule* | features/scheduling/schedules/schedules-optimized-schedules.md %} (AutoScheduler) functionality in injixo Advanced and Enterprise WFM when development is completed.

## Current development status

Create schedules is in development and not fully implemented yet. Stability issues may occur.

Currently, you can generate a schedule with a length of seven days while the following scheduling constraints are considered:

- People's skills and planning unit membership
- Activities assigned to planning units and their staff requirements
- Worktime guidelines from the contracts
- A subset of scheduling rules

Learn more about [general constraints and (un)supported features ](#supported-and-unsupported-features).

### Join the tests in the Beta phase!

If you are interested in testing Create schedules and in giving us feedback, get in touch with us. We will give your tenant access to Create schedules and the new Productivity level in Schedules.

> Note
> 
> You cannot access the Productivity level from (Virtual) Shift Center. The Productivity level will be removed when the first stable version of Create schedules is released.

## Create a schedule

After the feature has been activated for your tenant, create a schedule as follows:

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click **Scheduling actions**{:.doc-button}.
3. To open the overview page, click **Create schedule [Beta]**.
4. Select the **Planning unit**, **Target level**, and **Time period** for which you want to create a schedule.  
   Note: To avoid interfering with your schedules or workflows in the production environment, use the Test level.
   {{ 1 | image: 'Create schedules overview', '90%' }}

5. Click _Create schedule_{:.doc-button}.  
   injixo starts creating the schedule.  
   This can take up to one hour depending on the number of people, activities, and day models.  
   The **History** section on the page informs you about the status changes.

   > Do not change data in the selected time period and level of your planning unit. Any modifications may be overwritten.

6. Once the schedule has successfully been created, you can access a page summarizing the
   results by clicking **View results**. Here you can see for which people a schedule was created. There are three statuses: 

| Name | Status |
| ------- | ------ |
| Nonscheduled | Schedule could not be created |
| Scheduled despite conflict | The schedule was created but there are conflicts |
| Scheduled | Schedule created successfully |

<!-- What is the way out if the schedule could not be successfully created? What can users do then? Missing, tbd soon -->

   {{ 2 | image: 'Create schedules overview', '90%' }}

7. To see the created schedule, click **See schedule** at the top of the page. You can look at the
   schedule by {% link_new displaying the selected target level | features/scheduling/schedules/schedules-overview.md | #by-level %}.

### Existing activities

> Note
> 
> Create schedules considers some existing activities but overwrites others.

When the schedule is saved, replaceable activities such as meetings are overwritten.

The following activities are considered and not overwritten:

- Illnesses
- Vacation days
- Full-day absences
- Paid intraday activities with a start and end time

Create schedules considers existing activities outside of the person's availability in the following two instances:

| Instance | Example |
|---|---|
| The existing activity overlaps with the person's availability. | The person starts an eight-hour shift at 8 a.m. but the planner has scheduled a meeting from 7-8 a.m. This meeting overlaps with the person's availability by one second. |
| Existing activities that, if added to the person's, availability, will complete their contracted working hours. | A person has a five-hour availability from 11 a.m. to 4 p.m. but the planner schedules a meeting at 5:15 p.m. |

## Supported and unsupported features

Currently, there are some general scheduling constraints:

- You can only create a seven-day schedule.
- On the results page, there is no feedback about why a person could not be scheduled.
- You cannot create schedules on a parent planning unit or based on selections.
- There is only limited support for {% link_new valid from/to fields | features/administration/set-a-validity-period.md %} in related configuration data, e.g. people assigned to planning units. Unless mentioned otherwise below, Create schedules uses the assignments valid for the current date.

Create schedules does not support any type of overnight scheduling yet, as well as target work accounts as a working time guideline.

### Contract rules

The following settings are read from the people's contracts:

- Number of working days per week (Working Days/Wk.)
- Daily and weekly target worktime, incl. min. and max. limits
- 2601 Rest Period Between Two Working Days
- 2624 Maximum Number of Successive Working Days

#### AutoScheduler parameters

Supported AutoScheduler parameters defined in contracts:

- Maximum Number of Successive Workdays
- Minimum Number of Successive Days Off per Week (per week only, not spanning weeks)
- Maximum Number of Consecutive Days Off
- Minimum Number of Days Off per Week
- Minimum Number of Working Days per Week
- Minimum Rest Period Between Two Shifts (in Hours)

#### Work time pattern models

Supported:

- Work time pattern models of type A and type D (exception days settings are ignored)

Not supported:

- Work time pattern models of type B and C

### People

- Skills are always interpreted as capability (one person covers a requirement of 1).
- Person's assignment to the planning unit

The following assignments to people are respected with valid from/to fields:

- Availabilities (always read and respected regardless of scheduling rule 2611)
- Day models directly assigned to people
- Work time pattern models
- Activities a person can perform
- Contract assigned to the person
  - If a contract assignment changes within the week, Create schedules applies the contract which is valid at the first day of the week to the whole week.

### Planning units

The following assignments to planning units are respected with valid from/to fields:

- Business hours defined for a planning unit (date and time fields)
- Planning calendars
- Activities (date and time fields, regardless of setting 48408)

### Activities and coverage

Create schedules reads the activity parameters Paid, Plannable, Replaceable, Importance, Priority, Allow overstaffing if requirements are zero, as well as the type of activity.

You can schedule and optimize all paid activities of type Presence with staff requirements.

Create schedules supports multiactivities.

### Settings

Create schedules supports two settings:

- Setting _48303_{:.id-label} _Minimum duration of activity segments when splitting shifts compatible with multiple activities_
- Setting _48420_{:.id-label} _First day of the scheduling week_
