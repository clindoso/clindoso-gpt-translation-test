---
title: Schedule employees at multiple locations
description: Schedule employees from several planning units all at once to handle volume across multiple locations.
product_label:
  - advanced
  - enterprise
  - classic
redirect_from:
  - /best-practice-virtual-planning-units/
---

## Scenario

You operate two contact centers for your business; one in New York and one in Berlin. Calls are routed to any agent who has the appropriate skills, regardless of their physical location. You want to staff agents across both locations to handle this distributed call volume.

In injixo Enterprise on-premise, you have to activate the following settings to use the functionality:

- _48103_{:.id-label} _Consolidate key figures for higher-level planning units_
- _48399_{:.id-label} _Plannability of virtual planning units in AutoScheduler_

## Representation in injixo

Each location is set up as its own {% link_new Planning Unit | features/administration/create-and-manage-planning-units.md %}. In addition, we add two additional planning units:

1. A planning unit that does not have any assigned agents, but which will store the required number of agents to handle your volume.
2. A planning unit which represents your entire business, spread across multiple locations. This is frequently referred to as a 'parent' or 'virtual' planning unit.

You end up with a structure something like this:

- Motibot Technology Co.
  - Berlin
  - New York
  - Requirements

## Recommended approach

### Create a planning unit for the employee requirement

To do this, under _WFM > Administration> Scheduling> Planning Units_{:.breadcrumbs} create a new planning unit with the same interval as your existing planning units. Set the opening hours to encompass the opening hours of all other planning units, and add any activity which is performed by at least one planning unit.

For example:

- Berlin: Mon-Fri from 08:00-18:00
- New York: Mon-Sat from 09:00-18:00
- Requirements: Mon-Sat from 08:00-18:00

> Warning
>
> Do not add anything else to the planning unit (such as employees, day models, or planning calendars).

### Create the parent planning unit

This is created in the same way as the requirement planning unit, however, you do not need to worry about the operating hours; during scheduling, the opening hours of each child planning unit are taken into account individually.

### Structure and assignment of the planning units

During the setup, we set the virtual planning unit as the parent of the location-based planning. To do this, you open the child planning units and, under _General_{:.menu-item} select the virtual planning unit as the _Parent Planning Unit_{:.menu-item}.

{{ 1 | image: 'Create virtual planning unit'}}

### Forecasting and scheduling

Optimized scheduling supports virtual planning units. Shift generation, job, and break optimizations does not.

1. Store the calculated employee requirement for all your activities in the Requirements planning unit.
2. Create optimized schedules on the parent planning unit. Note that this will also create schedules for all planning units under the parent planning unit.

## Scheduling result

Employees in each child planning unit will be scheduled to meet the requirements stored in the Requirements planning unit, optimizing coverage across all sites. You can see the resulting coverage in the heat map in the level of the parent planning unit. This aggregated view only applies to the heat map key figures; it does not show an overview of all employees and their schedule.

> Note
>
> If you would like to schedule an overflow, you only need an additional virtual planning unit and none for the employee requirements. Save the requirements of the individual planning units as usual.
>
> By scheduling the virtual planning unit, you ensure that calls are primarily answered in the corresponding planning unit. If there are not enough employees, appropriately skilled agents from other planning units are considered for the activity.
