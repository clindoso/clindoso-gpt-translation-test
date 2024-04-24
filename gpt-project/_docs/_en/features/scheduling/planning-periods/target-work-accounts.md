---
title: Calculate target work accounts
product_label:
  - classic
description: Calculate target work accounts to be used as a replacement for contractual working times in shift bidding and full optimization.
---

Under _WFM > Scheduling > Time Manager > Target Work Accounts_{:.breadcrumbs}, you can calculate, view and modify the working time of your Employees for each Planning Period. You can manually update working time values for individual Employees. Moreover, you can add or subtract values to or from several accounts at a time, for example, to compensate for seasonal variations. The displayed Calculated Value represents the target working time of an Employee, which is taken directly from his or her contract.

To show the Calculated Values for selected Planning Periods you can either use the menu option _Target Work Accounts_{:.menu-item} (or you access the same screen via the menu option _WFM > Scheduling > SchedulePro > Planning Periods_{:.breadcrumbs}, and the Target Wok Accounts entry on the right hand side). Once you click the _Target Work Accounts_{:.menu-item} menu item, the main screen appears, allowing you to set various parameters.

## Setting parameters

In the Parameters area, you first decide which Employees you are interested in viewing and/or modifying their Target Work Accounts (this is displayed on the screen as Calculated Value).

| Parameter       | Description                                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Planning Unit   | Select the Planning Unit for which you want to display the Target Work Accounts. The last used Planning Unit is selected by default.                                |
| Selection       | Choose the Selection by which you want to filter the list of Employees. [All] is selected by default.                                                               |
| Planning Period | Select the Planning Period for which you want to display the Target Work Account. All Planning Periods of type 'Standard' are available for the specific Selection. |

Confirm your selection after each change with _Apply_{:.doc-button}, to show or update the Target Work Account overview. Once the job has been submitted, the JobProcessor starts processing the Shift Sequences to calculate the hours the Employees will work (based on the Shift Sequences).

Once the overview appears, you can calculate or edit Target Work Account values. The overview does not contain any values if no target time has been calculated for the specified day.

## Calculating target work accounts

The target working time to be completed by the Employees is normally determined before each new Planning Period. To calculate the target working time for a Planning Period or update existing values, click _Calculate_{:.doc-button} in the Parameters area. As soon as the job has been sent, the JobProcessor starts processing. The updated Target Work Accounts overview is displayed after a short time.

> Note
>
> The Target Work Accounts are only calculated for Employees who have been assigned a contract. This contract must have a Start Date or the Employee must have a Join Date as the time account calculation needs a start date from which to calculate the time account value.

In the overview, you can edit the target work time for each Employee in the selected Planning Period.

| Setting          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Employee         | A list of the Employee names for the selected Planning Unit and Selection.                                                                                                                                                                                                                                                                                                                                                                          |
| Calculated Value | After the calculation, the target working time appears for all Employees. The value is displayed in hours. The calculated target working time itself cannot be changed. Missing values means that no Target Work Account has yet been determined for the Planning Period.                                                                                                                                                                           |
| Modified Value   | For each Employee, you can enter a new target working hours value. The lottery and assignment procedures will first consider the values displayed in this column. To find out which target working hours value was used, refer to the lottery or assignment log. The Calculated Value column and the _Shift Center_{:.menu-item} continue to display the target working time or contractual working that were originally determined by the program. |

## Adjusting target work accounts

To the right of the Parameter section, you see the Adjust Accounts section. This is where you can increase or decrease the calculated target working hours by a value you choose; this can be either a percentage or a number of hours.

| Setting    | Description                                                                                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Percentage | Use this option to increase or decrease the target working time by a percentage value.                                                                        |
| Hours      | Use this option to raise or lower the amount of hours for the selected account.                                                                               |
| Adjustment | Indicate whether you want to add or subtract the Value.                                                                                                       |
| Value      | Enter a numeric value greater than '0'. Valid entries are percentage values up to 100 % (with a maximum of two decimal places) or values up to 9999:00 hours. |

To adjust the Target Work Accounts, click the _Apply_{:.doc-button} button. Once the job has been submitted, the JobProcessor begins to process the shift sequences. The updated target working hours will be displayed in the column Modified Value after a few moments.
