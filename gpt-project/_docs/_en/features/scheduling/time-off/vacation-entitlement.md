---
title: Vacation entitlement
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: See and edit vacation entitlement, transfer it to the next year, and export vacation entitlement data as a CSV file.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-absences-management.md
---

Time off entitlement is the basis for planning absences from the workplace with injixo. The entitlement is always valid for a calendar year.

## Check vacation entitlement

1. Go to _Plan > Time Off_{:.breadcrumbs} and click _Edit entitlement_{:.doc-button} to manage people's entitlements.
2. Select a **Planning unit**, optionally a **Selection**, and a **Year**.
3. (Optional) Use **Search** to find specific persons.

{{ 1 | image: 'Vacation entitlement', '100%' }}

Besides the employee number, name, and contract type of your employees, you will see the following columns:

<style>
table th:first-of-type {
    width: 20%;
}
table th:nth-of-type(2) {
    width: 80%;
}
</style>

| Column              | Explanation                                                                                                                                                                                                     |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Remain Current Year | Remaining vacation entitlement for the current year. It is calculated as the remaining vacation days from the previous year plus the entitlement for the current year minus the days taken in the current year. |
| Remain Last Year    | Remaining vacation days from the previous year. You can overwrite this value manually with a negative or positive value.                                                                                        |
| Current Year        | The total number of vacation days the employee is entitled to in the current year. You can overwrite this value manually with a negative or positive value.                                                     |
| Taken Vacation      | Percentage of vacation days already taken of the entitlement for the current year. The column header displays the average percentage value for your current filter settings.                                    |

If employees belong to more than one planning unit throughout a year, the data for the entire year is always displayed, regardless of the filter setting. You only have to enter the data for each employee once.

> injixo Enterprise On-Premise
>
> You find the vacation entitlement menu item under _WFM > Scheduling > SchedulePro > Vacation Entitlement_{:.breadcrumbs}. Field names differ slightly and the functionality is limited (no filter, no download option, not the last two columns in the table). You need to save your changes manually.

### Show remaining vacation entitlement

If you see no values in the **Remain Current Year** column, you need to edit your employees' contracts:

1. Go to _WFM > Administration > Scheduling > Contracts_{:.breadcrumbs}.
2. Click a contract for which you want to show the remaining vacation entitlement.
3. In the **Work Time Guidelines** section, enter a target value for weekly working hours in the **Target** field on the **Week** line.
   {{ 2 | image: 'Add target weekly working hours', '60%' }}

4. Click _Ok_{:.doc-button}.

## Add, edit or delete vacation entitlement

You can add, edit or delete the values in the **Remain Last Year** and **Current Year** columns.

1. Click a field and press Tab to navigate through the list.
2. Type in a value or use the arrows in the field. Press the delete key to remove values. The data will be saved automatically.

You cannot batch-edit values for a contract. You cannot import data.

## Transfer unused vacation entitlement to the next year

You can transfer the remaining vacation entitlement for the current year to the following year.

1. Choose a **Planning unit** and, optionally, a **Selection** to display only the employees whose entitlemens you want to transfer. You can use the **Search** field to select individual employees.
2. Choose the **Year** from which you want to transfer the entitlement to the following year.
3. Make sure that the **Remain Current Year** column displays data. If there is no data, follow the steps to {% link_new show the remaining vacation entitlement | features/scheduling/time-off/vacation-entitlement.md | #show-remaining-vacation-entitlement %}.
4. Click _Transfer Entitlement_{:.doc-button}. This will transfer the vacation entitlement for all displayed employees into the next year. The transferred entitlement will appear in the **Remain Last Year** column.

## Export vacation entitlement as CSV file

To export the displayed data to a CSV file, click the {% icon file-arrow-down %} next to _Transfer Entitlement_{:.doc-button}. The format of the CSV file is as follows:

```
personnelNumber,name,remainingDaysCurrentYear,remainingDaysLastYear,currentYear,percentTaken,year
0001,"Neumann, Günter",105.0,75.0,30.0,0,2019
0003,"Neumann, Moritz",121.0,90.0,31.0,0,2019
...
```

## Subtract taken vacation from the entitlement

Only paid activities of the type Vacation that have been entered in the Schedule level are subtracted from the vacation entitlement for the year.

The working time subtracted from the yearly vacation entitlement for a full-day vacation depends on the person's contract. The formula for the calculation is: Weekly target hours divided by the number of working days per week. Vacation requests for part days are calculated on an exact pro rata basis.

You can manually insert vacation and absences as full-day or regular activities with a start and end time in the Schedule level.

People can only request time off in injixo Me if there is a {% link_new time-off period | features/scheduling/time-off/time-off-periods.md %} published for the time range.  
In injixo Classic, you need a {% link_new valid planning period of the type Vacation | features/scheduling/planning-periods/enable-time-off-and-request-sick-leave.md %}.

In both cases, the activity of type Vacation must be configured as **Requestable in Me**. The activity must be assigned to the same planning unit as the person.
