---
title: Create contracts
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Create contracts to define the working time per week and other rules for your employees.
redirect_from:
  - /contracts-overview/
  - /contract-creation/
redirect_reason: Updated filename on 08 December 2023
---

In _Plan > Configuration > Contracts_{:.breadcrumbs}, you can enter the contracts for the people you want to schedule. You can create as many contracts as you like. With contracts, you can define time constraints for scheduling:

- The minimum and maximum number of working days per week
- The minimum, target, and maximum number of working hours per day
- The minimum, target, and maximum number of working hours per week
- The maximum number of working hours per months

Contracts also reflect information about work time policies in your organization, for example, the number of rest days between shifts. You can also define scheduling parameters for the **Create optimized schedule** functionality.

## Create a contract

To create a new contract, go to _Plan > Configuration > Contracts_{:.breadcrumbs} and follow the steps below:

1. Click the {% icon item-add %} at the top left.
2. In the **General** section, enter the basic information for the contract:<br>
   - **Name**: Enter a unique name (max. 50 characters).
   - **Abbreviation**: Enter the name or a shorter version of it (max. 25 characters).
   - **Color**: The color can help you identify the contract.
3. In the **Working Days/Wk.** section, enter the number of working days per week.
4. In the **Calculation of the Workdays** section, choose a calculation method: <br>
   - **Standard** respects the order of the days in the scheduling week.<br>
   - **Flexible** freely chooses the working days within the planning unit's business hours.
5. Enter the [**Work Time Guidelines**](#work-time-guidelines) and [**Working Hours for Each Day of the Week**](#working-hours-for-each-day-of-the-week).
6. (Optional) Configure the [**AutoScheduler Parameters**](#autoscheduler-parameters) or [**Scheduling parameters**](#scheduling-rules).
7. To save your contract, click _OK_{:.doc-button}.

## Work time guidelines

Work time guidelines for the minimum, target, and maximum working hours are essential for scheduling. Work time guidelines work in combination with the scheduling parameters and AutoScheduler parameters.

### Day

- **Minimum**: Enter the minimum working hours per day. If you do not enter any value, the target time will be considered as the minimum. This parameter is verified via the scheduling parameter _2615_{:.id-label}.
- **Target**: Enter the target working hours per day. Enter a value between 0 and 24 hours and take into account the standard working times.
- **Maximum**: Enter the maximum working hours per day. If you do not enter any value, the target time will be considered as the maximum. This parameter is verified via the scheduling parameter _2614_{:.id-label}.

### Week

- **Minimum**: Enter the minimum number of working hours per week.
- **Target**: Enter the target working hours per week. This value is required if you do not enter any values in the field **Working Hours for Each day of the Week**.
- **Maximum**: Enter the maximum number of working hours per week. This parameter is verified by the scheduling parameters _2618_{:.id-label} and _2629_{:.id-label}.

> Change start of the week
>
> By default, the start of the week is set to either Sunday or Monday, depending on your region. If you need to set it to another day, contact your consultant.

### Month

- **Maximum**: Enter the maximum working hours per month. This parameter is verified via the scheduling parameter _2619_{:.id-label}.

## Working hours for each day of the week

You can define the number of working hours per day for people with this contract. In the configuration of the **Work time guidelines**, this section is optional. However, it is useful so that injixo can calculate paid absences, such as vacation or illness.

Example:
A person works 40 hours per week and 8 hours per day with days off on Wednesday and Sunday. To ensure the working hours are properly distributed over the week, enter 8:00 in the fields for Monday, Tuesday, Thursday, Friday, and Saturday, and enter 0:00 in the fields for Wednesday and Sunday. If this person calls in sick or takes a paid vacation, their working hours will still be calculated based on the hours you entered here.

Leaving a field blank will default to the formula: [Weekly Target Hours/Number of Working Days]. This can potentially lead to miscalculations because injixo will assume an even distribution of work hours across all working days.

## AutoScheduler parameters

- **Maximum Number of Successive Workdays**: Fill in this field if your planning unit is open 7/7 days. Enter the maximum number of consecutive working days that the **Create optimized schedule** functionality must take into account. For example, if a person works 5 days per week, use this parameter to prevent them from working 10 consecutive days.
- **Minimum Number of Days Off per Week**: Fill in this field if your planning unit is open on the weekends. Enter the minimum number of non-working days that the **Create optimized schedule** functionality must take into account for each scheduling week.
- **Minimum Number of Successive Days Off per Week**: Fill in this field if you want to guarantee that your people have at least one period of consecutive days off per week. Enter the minimum number of consecutive non-working days per week that the **Create optimized schedule** functionality must respect for each scheduling week.
- **Maximum Number of Consecutive Days Off**: Fill in this field if you want to limit the number of consecutive days off for your people to ensure consistent staffing levels and avoid long breaks. Enter the maximum number of consecutive non-working days that the **Create optimized schedule** functionality must take into account. The value is not checked per week but across weeks.
- **Minimum Rest Period Between Two Shifts (in Hours)**: Fill in this field if you need to comply with labor laws regarding rest periods between shifts. Enter the minimum rest period that the **Create optimized schedule** functionality must take into account between two consecutive shifts.
- **Minimum Number of Working Days per Week**: Fill in this field to maintain a minimum level of staffing on a weekly basis in your planning unit, to ensure that there are always enough people to handle the expected call volume. Enter the minimum number of working days to be scheduled per scheduling week.
- **Use Target Work Account instead of Weekly Contractual Target**: Check this checkbox if you want the **Create optimized schedule** functionality to use the values from calculated target work accounts. Learn more about {% link_new target work accounts | features/scheduling/planning-periods/target-work-accounts.md %}.
- **Max. 1 Working Saturday in x No. of Weeks**: Fill in this field if you want to ensure a fair distribution of weekend work among people and prevent the same people from consistently working on Saturdays. Enter the maximum number of weeks (1-5) on which a person can work on a Saturday. For example, a value of 2 means every other Saturday.
- **Assignment of a Workday Following a Full-Day Vacation**: Fill in this field if you want to force the **Create optimized schedule** functionality to schedule a working day after a full-day vacation. If the person has several consecutive days off, the working day is scheduled after the last day off.

## Scheduling rules

Scheduling rules define a general and contract-related set of rules for your scheduling process. In the contract configuration, scheduling rules are called scheduling parameters.

To see a list of all available scheduling rules, go to _WFM > Administration > System > Scheduling rules_{:.breadcrumbs}. To see a description of a rule, click on the respective rule in the list. Scheduling rules are usually configured during your onboarding with your injixo consultant.

Users with Admin access can modify each rule, set exceptions, and even revert user-specific values to default settings.

> Potential risk of scheduling errors
>
> Changes to scheduling rules are complex and can result in scheduling errors if done incorrectly. Do not change them yourself if you are not sure about the consequences. If you need to change a scheduling rule, contact your consultant.

Contract-specific scheduling rules ensure that the conditions of each contract are taken into account during scheduling. For example, if a contract specifies a certain rest period duration or a maximum number of working hours per day, scheduling rules ensure that these conditions are met. Breaching these rules can lead to scheduling conflicts, employee dissatisfaction, and potential contract violations.

### Status indicator

You can see the status of each scheduling rule in the list:

- Gray: The rule is deactivated and won't be considered during scheduling.
- Yellow: The rule is in soft mode. Breaching this rule will generate a warning during scheduling, but the action will still proceed.
- Red: The rule is fully activated. Any violation of the contract will result in an error message detailing the specific rule violation.
