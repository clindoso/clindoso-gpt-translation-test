---
title: Analyze coverage, staffing, and requirement
product_label:
  - advanced
  - enterprise
  - classic
description: Analyze the coverage, staffing, and requirement for your activities, properly use the Day Models tab, and more.
---

In this article, you will learn how to:

- analyze the coverage, staffing, and requirement for your activities.
- display requirement and staffing as graphs.
- hide activities of certain activity types.
- use the _Day Models_ tab in the shift bidding process. <!-- break down into use cases -->

New to the Shift Center? Learn {% link_new the basics | features/scheduling/shiftcenter/shift-center-overview.md %} first - in particular what the {% link_new parameter window | features/scheduling/shiftcenter/shift-center-overview.md | #parameter-window %} is and how to {% link_new customize the display of data | features/scheduling/shiftcenter/shift-center-overview.md | #customize-the-display-of-data %}.

## Analyze the coverage

The coverage shows how the current staffing covers the staff requirements for your activity or activity types. It is the difference between the number of scheduled and required employees. You can analyze the coverage (and other metrics) down to 15-minute intervals for each activity assigned to the planning unit and per activity type:

1. Click the **Activities** tab and expand a planning unit by clicking the {% icon plus %}. You will see all activities of the planning unit. Multiactivities are displayed in bold print with their subactivities indented below. The list also shows activity types, e.g. the row _Total Values 'Presence'_ combines all activities of the type _Presence_.
2. Right-click a **day cell** and select **Coverage**. You will see the coverage for the different activities.
3. If you click a **day column header**, it expands to show the detailed coverage for the daily intervals. Zoom in to see the values for even smaller intervals.

The numbers in the cells show you the difference between staff requirements and staffing for the respective time period. If a cell e.g. shows -2, then you are understaffed by two employees.

The color coding of the cells immediately shows you how good your coverage is. Red shows understaffing, blue shows overstaffing and green signals ideal coverage. The more intense the color, the greater the deviation from the ideal staffing.

{{ 2 | image: 'Shift Center Activities Tab' }}

## Analyze the staffing

The staffing shows the number of scheduled employees for a certain activity. Follow the same steps as under [_Check the Coverage_](#analyze-the-coverage) but select the **Staffing** metric at step 2.

## Analyze the requirement

Requirement is the number of employees you need in order to cover the requirement for a given interval and activity. Follow the same steps as under [_Check the Coverage_](#analyze-the-coverage) but select the **Requirement** metric at step 2.

## Analyze an activity over several days and weeks

You can use the tab _Activity Overview_ to analyze the coverage, staffing, and requirement of a single activity or activity type over several days and weeks.

1. Click the **Activity Overview** tab and expand a planning unit by clicking the {% icon plus %}. The intervals will appear in a vertical scrollable view.
2. Right-click a **day cell**, then
   - Click **Activity**, and then on the activity or activity type you want to analyze.
   - Click **Parameters**, and then on the metric you want to analyze.
   - Click **Level**, and then on the level for which you want to analyze the chosen activity and metric.
3. After each selection, the view will update to your filter. Repeat this step 2 if needed.

At the end, you can vertically scroll through the intervals and check the values for the selected activity and metric. You can also expand additional weeks to show more data side by side.

{{ 5 | image: 'Shift Center Activity Overview Tab'}}

## Display requirement and staffing as graphs

On both the _Day Models_ and the _Activities_ tab, you can display the requirement and staffing values as graphs.

1. Right-click a cell and select **Graph Display**. Instead of the cells, a graph is shown. The dashed line represents the requirement values, the solid line the staffing values.
2. To enlarge the graph, hover your mouse over the borders of the cell at the top or the bottom. The cursor changes to a black double arrow pointing up and down. Click, hold, and drag to enlarge the cell and by that also the graph.
3. To downsize the cell back to its original size, double-click the black double arrow.

## Hide activities of certain types

In the _Activities_ tab, the second column on the left shows the activity types. You can hide certain activity types:

1. Right-click the **empty activity types column header** to open a context menu. By default, _All_ is preselected.
2. Click one or more **activity types** to hide all activities of that type from the list.

{{ 4 | image: 'Shift Center Statistics Window'}}

## Day models tab

Use the _Day Models_ tab if you work with {% link_new shift bidding | features/scheduling/schedules/schedules-shift-bidding.md %} and want to see the coverage, staffing, and requirement values for inserted shifts. The numbers are based on the day models in the schedule window.

To the left, you see a list of all your planning units. Click the {% icon plus %} to show all day models of the respective planning unit.

To change the displayed metrics, right-click a **data cell** and choose **Coverage**, **Requests**, **Staffing**, or **Requirement**. Here is what they mean:

| Parameter   | Description                                                                                                                  |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Coverage    | Difference between the number of day models assigned to employees and the number of generated shifts.                        |
| Requests    | Number of shifts requested by employees during the shift bidding process. The values are the same as in the _Request_ level. |
| Staffing    | Shows how many of the generated shift are staffed by employees.                                                              |
| Requirement | Result of the {% link_new Shift Generation process                                                                           | features/scheduling/shift-bidding.md %}. Shows how many shifts are required. |

{{ 3 | image: 'Shift Center Day Models Window'}}

<!-- Separate section for separate use cases?  -->
<!-- Not often used. See how the shift generation covers your requirements before activities have been assigned. Good indicator for the shift generation result.
| Parameter   | Description |
| ----------- | ----------- |
| Net Maximum Capacity | Maximum available number of employees already scheduled and skilled for the activity. Counts only employees with an assigned activity of the type *Present*. |
| Staffing According to Shift Requirement | Number of day models generated by the shift generation to cover the employee requirement for the activity. You can rate how well the Shift Generation worked. |
| Coverage According to Shift Requirement | Difference between the shifts required to cover 100% of the shift requirement and the shifts actually generated during shift generation. | -->
