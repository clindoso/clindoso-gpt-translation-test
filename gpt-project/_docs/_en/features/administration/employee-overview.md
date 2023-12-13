---
title: Configure employees
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Create and configure employees to be included in scheduling.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/calculate-a-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/staff-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
---

injixo provides three places where you can create and edit an employee, depending on your use case. The table below gives you an overview of the different places for employee configuration in injixo and describes what you can do where.

| Place                                           | Description              |
| ----------------------------------------------- | ------------------------ |
| _Plan > Configuration > Employees_{:.breadcrumbs}   | {% link_new Configure an employee for scheduling | features/administration/employee-overview.md | #overview-of-employee-settings %}. Employees without assigned planning units will not appear on the list.      |
| _Account > Users_{:.breadcrumbs}                                 | Manage user access rights via {% link_new user roles | getting-started/configure-user-roles.md | #create-new-user-roles %}, {% link_new unlock locked users | getting-started/manage-user-accounts.md | #unlock-users %}, {% link_new set a new password for users | getting-started/manage-user-accounts.md | #set-a-new-user-password %}, and {% link_new check which users are billed | getting-started/how-does-billing-work.md | #view-billed-and-unbilled-users %} and which are not. You can also {% link_new delete users | getting-started/manage-user-accounts.md | #delete-a-user-account %} so that you are no longer billed for them. |
| **People**                                                           | {% link_new Create and manage | features/people/manage-people.md %} a person's account and manage contact and address information. |

In _Plan > Configuration > Employees_{:.breadcrumbs}, users without admin access can only see employees assigned to the planning units they have permissions for. Employees who are not assigned to a planning unit do not appear in the list, even if All is selected in the planning unit and selection drop-down menus. Users with admin access can see all employees.

Employees, users and people are synchronized, so you only have to create an employee once and you will also only be billed once.

> For each employee or user you create in one of the three sections, your organization will be {% link_new billed | getting-started/how-does-billing-work.md %} until you {% link_new deactivate or delete | features/administration/deactivate-employees.md %} them.

## Create an employee

To create an employee with the basic settings, injixo requires you to complete all mandatory fields. Before you can set up the employee for scheduling, you have to [configure](#configure-employee-settings) several other [employee settings](#overview-of-employee-settings).
To create an employee with the basic settings, follow the steps below:

1. Go to _Plan > Configuration > Employees_{:.breadcrumbs}.
2. In the action bar, click the {% icon item-add %}.
3. In the **General** section, add a unique **Personnel number**.
4. In the **Personal data** section, add the **Last name** of the employee.
5. In the **injixo Login (Email)** field, enter the email address the employee is going to use for injixo. A user login for injixo Me is automatically created. 
6. {% link_new Set a password | features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md %} for the employee, so that they can log in to injixo.<br>You can do this after finishing the basic configuration of the employee.
7. Click _OK_{:.doc-button}.<br>The system automatically sets the join date to the current day. You can manually change it later in the [Staff membership section](#other-settings).

When you create an employee, injixo automatically creates a user with the agent role.

<!-- In injixo Enterprise on-premise, you need to set the correct join date for the employee in the Employment Period section manually. To automatically create a linked user in the Users section, you need to add a User name and a Password in the Employee section. The injixo Login (Email) field is called Email 1 here and is not mandatory. --->

## Configure employee settings

After you have created an employee with the mandatory basic settings, you can configure the scheduling-related settings. To do that, follow the steps below:

Prerequisite: You have set up {% link_new all elements required for scheduling | getting-started/set-up-base-configuration.md | #required-configuration-elements %}.

1. Click an employee in the list.<br>
You can use the blue quick links in the upper right to quickly navigate to a section.
2. Click the {% icon item-add %} in a section to add a new setting. To edit an existing setting, click the {% icon item-edit %}.<br>Learn more about the [individual setting options](#overview-of-employee-settings).
3. (Optional) In some sections, you can configure {% link_new Valid From and Valid To dates | features/administration/set-a-validity-period.md %} that limit the validity period for a setting.
4. To save your changes, click _OK_{:.doc-button}.


## Overview of employee settings

In the following sections, you can find information about mandatory and optional scheduling settings for employee configuration.

### Mandatory scheduling settings

The following list shows the mandatory configuration items you need to assign to your employees in order to schedule them. To learn more about each configuration item, follow the links.

> Note
>
> You cannot add assignments with overlapping {% link_new validity periods | features/administration/set-a-validity-period.md %}.
> Past and future assignments are hidden by default. To show them, click the Display all icon {% icon assignment-history | icon-only %}.


- {% link_new Contracts | features/administration/create-contracts.md %}: The drop-down menu shows all available contracts. Choose the right contract for your employee and assign it to them.
- {% link_new Skill levels | features/administration/work-with-skills.md %}: Skill levels reflect how qualified an employee is to work on a certain task. Select one or more skill levels from the drop-down menu.
- {% link_new Activities | features/administration/activities.md %}: Activities are the tasks an employee can work on based on their skills. The activities section is auto-populated after assigning a skill level to an employee. Activities that all employees can work on do not require a skill, e.g. the preset activities Present and Vacation.
- {% link_new Planning units | features/administration/create-and-manage-planning-units.md %}: Planning units group employees. An employee can be assigned to more than one planning unit but needs at least one planning unit with priority 1. Other planning units can be assigned with a value between 1 and 100 for each employee, with 1 being the highest priority.

### Optional scheduling settings

The following settings are not mandatory but can also be used for scheduling. To learn more about each configuration item, follow the links.

- {% link_new Availability | features/administration/availabilities.md %}: Define on which days and at which times an employee is available for scheduling. If you want to always exclude an employee from scheduling on a certain day of the week, set the availability for the respective {% link_new day type | features/administration/day-types.md %} to one minute. To set the same availability for several employees at once, use day models of the {% link_new Availability Period type | features/administration/daymodels/daymodel-creation.md | #availability-period %} in shift sequences. If an employee is available without limitation, you don't need to add any availabilities.

- {% link_new Day models | features/administration/daymodels/daymodel-creation.md %}: By default, injixo uses all day models assigned to the planning unit to create schedules for your employees. If you assign personal day models to an employee, the schedule optimization will only use these specific day models for the employee. If you want injixo to only schedule employees who have been assigned personal day models, you can activate the scheduling rule _2661_{:.id-label} _Day model assignment to employee_.

- {% link_new Shift sequences | features/administration/shift-sequences.md %}: Shift sequences contain day models or activities with a repeating weekly pattern. If you want to use shift sequences to create schedules for your employees, you have to create and [assign shift sequences to an employee](#assign-a-shift-sequence) first. You can also choose to assign more than one shift sequence to an employee, for example, if you want to use a different shift sequence for weekends and weekdays. 

- {% link_new Selections | features/administration/selections.md %}: Selections serve as a type of filter that you can use to display a filtered group of employees in an overview or to perform an action simultaneously for a specific group of employees. You can create one or several selections from the Selections drop-down menu. Examples of selections could be a group of employees who are always scheduled in the same way, have the same contract, work in shift sequences, carpool to work, or who are scheduled first due to their full-time status.

- {% link_new Work time pattern models | features/administration/work-time-pattern-models.md %}: Use work time pattern models to limit the automatic scheduling to a subset of all available day models. You can only assign one work time pattern model per employee. Choose a {% link_new reference date | features/administration/reference-date.md %} to mark the start date for the work time pattern model.


- External systems: Assign {% link_new external user identifiers | features/acd-integration/cloud/import-agent-status-data.md | #map-external-user-identifiers-to-people-in-injixo %} which are needed for the agent status import from your ACD.

### Other settings

The following section provides an overview of the remaining settings in the employee configuration. Most of them are not relevant for scheduling. For further information about these settings, you can also hover over them in the UI to display the setting details.

- Staff membership: When you [create an employee with the basic settings](#create-an-employee), the join date is automatically set. Here, you can edit the join date and set a leave date, if required.

- Personal data: Enter personal data for your employee, e.g. address data, phone number, and country.

- Identification card numbers: Enter the number of your employee's company ID card or other personal ID card.

- Miscellaneous

Some of the settings in the Miscellaneous section are relevant for scheduling and others are not. The following table provides an overview of the setting details.

| Setting        | Relevant for scheduling | Description                |
|----------------| ------------------------|----------------------------|
|Color       | No                      | Pick a color to quickly identify the employee in the schedule.  |
|Date and place of birth  |       No |  Add the employee's date and place of birth.  |
|Schedule position  | Yes | Defines the sorting order for the {% link_new Sort by Schedule Position | features/scheduling/shiftcenter/sort-and-filter-items.md | #sort-the-items-of-a-level %} functionality in Shift Center. The default value is 0 and Shift Center will sort in ascending order.  |
|Shift assignment | Yes | The checkbox is checked by default and is required if you want to schedule employees automatically. If you do not want this, uncheck the checkbox. You can still manually assign shifts and insert shift sequences for this employee.  |

## Use mass update

In injixo Advanced and Enterprise WFM, you can use the {% link_new mass update functionality | features/administration/mass-update.md %} to edit multiple employees at once.

## Assign a shift sequence

A shift sequence is a set of day models or activities that is repeated regularly. Learn how to {% link_new create shift sequences | features/administration/shift-sequences.md %} and how to insert them into your schedule.

To assign a shift sequence, follow the steps below:

1. In the **Shift Sequences** section, click the {% icon item-add %}.
2. Select a shift sequence.
3. From the employee row drop-down menu, select the row of the {% link_new shift sequence | features/administration/shift-sequences.md %} that applies to the employee.
4. Specify the sequence.<br>This setting is only relevant if you need to assign more than one shift sequence to an employee. Shift sequences with lower values are inserted first and can be overwritten by subsequent ones.
5. Set a {% link_new Reference Date | features/administration/reference-date.md %} that marks the start day for the shift sequence.
6. Click _OK_{:.doc-button}.
You can now {% link_new add shift sequences | features/scheduling/capacity/capacity-insert-shift-sequences.md %} to the schedule.

## Delegate employees

If your employees often work in other planning units for a limited amount of time, you can use the Delegate employee functionality to temporarily assign employees to another planning unit.

During the delegation period, the new planning unit automatically takes priority for scheduling. When the defined period ends, the employee is automatically scheduled in their old planning unit again. The Delegate employee functionality saves time compared to manually reassigning the planning unit.

To delegate an employee, follow the steps below.

1. Select an employee.
2. Go to the **Planning units** section.
3. In the section header, click the {% icon delegate-employees %}.
4. Select the planning unit the employee is delegated to.
5. Enter a start date and an end date for the delegation period.
6. Click _OK_{:.doc-button}.

> Note
>
> An employee who is assigned to multiple planning units at the same time, will always be delegated from the planning unit with the highest priority.
