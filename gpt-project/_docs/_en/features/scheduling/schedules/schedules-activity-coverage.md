---
title: Analyze coverage, staffing, and staff requirements in Schedules
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to analyze the coverage, staffing, and staff requirements for your activities and activity types.
---

In _Plan > Schedules_{:.breadcrumbs}, you can analyze the coverage, staffing, and staff requirements for your scheduled activities and activity types.

## Prerequisites

- You have calculated the {% link_new staff requirements | features/forecast/injixo-forecast/calculate-staff-requirements.md %}.
- You have created a {% link_new schedule | getting-started/create-a-schedule.md %}.

New to Schedules? Learn {% link_new the basics | features/scheduling/schedules/schedules-overview.md %} first.

## Display the activities area

1. In _Plan > Schedules_{:.breadcrumbs}, set the {% link_new filters | features/scheduling/schedules/schedules-overview.md | #filter-data %} and the {% link_new view options | features/scheduling/schedules/schedules-overview.md | #schedule-area %}.
2. In the schedule area, expand the planning unit(s) for which you want to analyze activity data.
3. In the [activities area](#activity-data-table), click a tab:
   - **Activities - Coverage**: The difference between the number of scheduled people and the staff requirements
   - **Activities - Staffing**: The number of scheduled people
   - **Activities - Requirements**: The saved staff requirements<br>
4. To select activities and activity types, use the filter icon {% icon filter | icon-only %} in the header of the **Activity** column.<br>An <em class="multiactivity-icon"></em> icon is displayed next to multiactivities. Subactivities are indented below the multiactivity.<br>If you delete an activity in _Plan > Configuration > Activities_{:.breadcrumbs} and you don't remove it from the planning unit(s) to which it was assigned, the deleted activity is displayed in italics.
   - Check the checkboxes next to the items that you want to display. You can select multiactivities or activities that are not subactivities. You cannot select individual subactivities. Use the search field to search for individual subactivities, multiactivities or other individual activities by their names.
   - (Optional) Use the search field. To search for several terms at once, use commas between the terms.
5. Click anywhere outside the activities area to update the displayed data.

### Activity data table

The table in each tab includes the following columns:

- **Activity**: The activities or activity types for which you want to display data.
- **Level**: The level(s) that you selected in the {% link_new schedule area | features/scheduling/schedules/schedules-overview.md | #schedule-area %}.
- **Sum**: The sum of coverage, staffing, or staff requirements values for the displayed time frame.
- Timeline column: An overview of the selected time frame with coverage, staffing, or staff requirements values per interval.

Hover over any cell to display the coverage, staffing, and staff requirements values for the 15-minute intervals.

If you select one or two days using the date picker in the schedule area, or if you click the day mark in the timeline column, the table displays columns for each hour of the selected day(s).
To display data in 30-minute intervals, hover in between two full-hour marks in the table header. When the {% icon magnifying_glass %} appears, click it.<br>To display 15-minute intervals, hover over the 30-minute mark, and click the {% icon magnifying_glass %} when it appears.<br>To go back to 30-minute intervals, click any 15-minute mark. To go back to displaying full-hour columns, click any full-hour mark at any time.<br>

A cell is empty if either the staff requirements, the staffing values, or both are missing for the interval.<br>
Cells are color-coded as shown in the table below. The more intense the color, the greater the difference between the staff requirements and the staffing.

<!-- left-align table -->
<style>
table {
   margin-left: 0px;
}
</style>

| Color | Coverage       | Description                                                    |
| ----- | -------------- | -------------------------------------------------------------- |
| Red   | Understaffing  | Fewer people scheduled than necessary                          |
| Blue  | Overstaffing   | More people scheduled than necessary                           |
| Green | Ideal coverage | The number of scheduled people matches the staff requirements. |
