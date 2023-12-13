---
title: Configure employee filters
description: Use the employee filter editor to filter employees using a combination of criteria.
product_label:
  - advanced
  - enterprise
  - classic
---

With employee filters, you can create lists of employees who match several criteria. The editing options depend on your user rights.

Employee filters work similarly to {% link_new selections | features/administration/selections.md %}. The difference between them is:

- For employee filters, the grouping criteria are based on configuration elements, e.g. planning unit, skill, and contract.
- For selections, you can create your own grouping criteria.

Employee filters are available only in injixo Classic, Advanced, and Enterprise.
  
1. To access the filter editor, go to _Plan > Shift Center_{:.breadcrumbs}.
2. If the Selection tile {% icon selection-filter-s | icon-only %} is selected: Select the Employee tile {% icon schedules-filter-employees-u | icon-only %}.
3. Click the **Filter editor** link.

## Create a filter

1. In the **Employee Filter** section, click the Create filter icon {% icon item-add | icon-only %}.
2. Select a **Time Period Type**:<br>
    - **User-Defined**: Specify the time period manually using the date picker. Select a **From** and **To** date.<br>
    - **Relative**: Specify a period for the next, current or previous week, month or year.<br>
    - **Context-Defined**: The date period is automatically set to the current day.
3. Create a [**Query**](#create-a-query).
4. To show the query results, click _Display_{:.doc-button}.
5. To add the query to the employee filter, click _Apply_{:.doc-button}.
6. To save the filter, click the {% icon save %}.<br>To save an existing filter under a different name, click the {% icon saveas %}.

## Create a query

A query is a set of conditions to filter and retrieve data from a larger dataset. You can define criteria and retrieve a list of employees who meet those criteria.

1. In the **Query** section, click the {% icon item-add %}.
2. In the first drop-down menu, select a configuration data type.
3. In the second drop-down menu, select a condition.
4. (Optional) Select a [priority and relational operators](#use-priority-and-relational-operators) for planning units, employee categories or skills.
5. Click _Apply_{:.doc-button}.

To edit a query, click {% icon item-edit %}.

## Use conditions

### IS IN

The **IS IN** condition shows results that match the query exactly.
 
1. Select a configuration data type from the first drop-down menu.
2. Select **IS IN** from the second drop-down menu.
3. Click _Criteria_{:.doc-button} to see the available criteria and select one from the list.
4. To add criteria to your selection, click the {% icon right-arrow-blue %}.
5. In the **Select criteria** window, click _Apply_{:.doc-button}.
6. (Optional) Select [options and relational operators](#use-priority-and-relational-operators) for planning units, employee categories or skills.
7. Click _Apply_{:.doc-button}.

### IS LIKE

The **IS LIKE** condition shows results that match the query partially.

1. Select a configuration data type from the first drop-down menu.
2. Select **IS LIKE** from the second drop-down menu.
3. Enter the text you want to match in the text field.
    - To replace any number of characters, use the * placeholder.
    - To replace exactly one character, use the ? placeholder.
4. (Optional) Select [options and relational operators](#use-priority-and-relational-operators) for planning units, employee categories or skills.
5. Click _Apply_{:.doc-button}.

## Use priority and relational operators

With the Priority checkbox and the relational operators, you can include employees based on their priority and assignment to the selected planning unit/employee category:  

1. Select **Planning unit** or **Employee category** from the first drop-down menu.
2. Check the **Priority** checkbox.
3. Select a relational operator from the list.
4. Enter a priority value in the input field.

With the Skill configuration element, you can use relational operators to include only skilled employees with a certain skill level:  

1. Select **Skill** from the first drop-down menu.
2. Check the **Skill level** checkbox.
3. Choose a relational operator from the list.
4. Enter the value of the skill level in the input field.

## Link queries

You can link individual queries with each other:

1. Create or select a [filter](#create-a-filter).
2. Create a [query](#create-a-query).
3. Select a conditional operator:<br>
  - **AND**: Include people who meet all the conditions.  
  - **OR**: Include people who meet at least one of the conditions.  
  - **NOT**: Exclude people who meet the condition following NOT.
4. Create a second query.
5. Click _Apply_{:.doc-button}.

To create a group, open a parenthesis. To close it, close the parenthesis. Use the up and down arrows to move and sort the individual queries at any time.

## Example query

To filter people from the New York planning unit who do not have a Full Time 40h contract and are not part of the Extra Hours selection, the query should follow this structure:


```
Planning Unit IS IN "New York"
AND
NOT
(
Contract IS IN "Full Time 40h"
AND
Selection IS IN "Extra Hours"
)
```

This query selects all people from the New York planning unit and then excludes people who have a Full Time 40h contract and are in the Extra Hours selection:

- **IS IN** defines the condition for the planning unit.
- **AND** combines the query's conditions.
- **NOT** excludes the following conditions.
- The parentheses open and close the group of conditions to exclude.
- **IS IN** selects people who have a Full Time 40h contract.
- **AND** combines the conditions within the parentheses.
- **IS IN** selects people who are part of the Extra Hours selection.

## Edit filters

1. In the **Employee filter** drop-down menu, select a filter.
2. Edit the information you want to change.
3. (Optional) To rename your filter, click the {% icon item-edit %}.
4. To save, click the {% icon save %}.<br>To save an existing filter under a different name, click the {% icon saveas %}.
