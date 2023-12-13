---
title: Analyze coverage, staffing, and requirement
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Analyze the coverage, staffing, and requirement for your activities and activity types (Schedules feature).
---

In this article, you will learn how to:

- analyze the coverage, staffing, and requirement for your activities and activity types.
- filter by activities and activity types.

New to Schedules? Learn {% link_new the basics | features/scheduling/schedules/schedules-overview.md %} first.

## What is the activities panel?

The _Activities Panel_ is part of _Plan > Schedules_{:.breadcrumbs}. It is located at the bottom of the screen and is retracted by default. The panel allows you to analyze the coverage, staffing, and requirement of activities and activity types for the planning unit(s) you have expanded in the schedule area above.

The following three tabs exist:

- _Activities - Coverage_: the difference between the number of scheduled and required employees
- _Activities - Staffings_: the number of scheduled employees for a certain activity
- _Activities - Requirements_: stored employee requirements per activity

Click _⌃_{:.doc-button} on the left or on one of the tabs to expand the panel.

{{ 1 | image: 'Activities - Coverage Panel' }}

## Check the coverage, staffing, or requirement for an activity or activity type

1. Click one of the three **tabs** of the activity panel, depending on whether you want to analyze coverage, staffing, or requirement.
2. In the header of the first column, click the **filter icon** and pick the activities and activity types you want to analyze. Learn more about [how to filter](#filter-activities-and-activity-types) below.
3. Click **anywhere** outside the selection window to update the view.

You will see a table that consists of:

- _Activity_ column: contains a list of all selected activities and activity types
- _Level_ column: shows the level(s) that you have selected in the schedule area
- _Sum_ column: shows the sum of the coverage, staffing or requirement values for the displayed time range
- _Time or date range_: coverage, staffing or requirement values based on the date range and zoom level you have selected in the schedule area

Provided that you have calculated a requirement and scheduled your employees, you can now check for each activity and interval how good the coverage is. You can also check the staffing and the calculated requirement for each interval. If cells are empty, it means either the requirement or the staffing is missing or both.

{{ 6 | image: 'Activities - Coverage Panel with Multiactvity' }}

When you are viewing the data in hourly intervals, you can hover your mouse over a cell to display the values for the 15-minute intervals.

{{ 2 | image: 'Detail View', '40%' }}

Note: Activities which have been deleted in the _Administration_ section appear in italics. Multiactivities have the _Symbol_{:.multiactivity-icon} next to it. The indented rows below the multiactivity contain the child activities.

### Understand the color-coding

The color coding of the cells immediately shows you how good your coverage is. Red shows understaffing, blue shows overstaffing and green signals ideal coverage (staffing equals requirement). The more intense the color, the greater the deviation from the ideal staffing. <!-- White cells indicated that there is an over- and understaffing within an hour, which sum up to zero. -->

## Filter activities and activity types

You can filter the list of activities and activity types to only show those items for which you want to analyze coverage, staffing, or requirement.

1. Click the **filter icon** _![Filter icon](/assets/img/common/schedules-filter-activities.png)_{:.doc-button-icon} in the header of the Activity column. You will see a list of activities and activity types based on all planning units which are currently expanded in the schedule area.
2. (Optional) Use the **search field**. To search several terms at once, use commas between the terms. You can only select or deselect multiactivities, but you can search for names of their subactivities.
   {{ 5 | image: 'Filter with Multiactivity', '40%' }}

3. Check or uncheck the **checkboxes** in front of the item(s) you want to display or hide. Use **All** to (de)select all items in one go.
4. Click **anywhere** outside the selection window to update the view. You have now filtered your view based on the selected activities and activity types.

   {{ 4 | image: 'Filter activities', '40%'}}
