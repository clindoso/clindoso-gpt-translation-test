---
title: Sort and filter items
product_label:
  - advanced
  - enterprise
  - classic
description: Sort and filter items of a level on a given day.
redirect_from: /displayed-items/
redirect_reason: renamed file in March 2021
---

In this article, you will learn how to:

- sort the items of a level by start time, schedule position, and activity.
- filter the items of a level by activity and time of the day.

New to the Shift Center? Learn {% link_new the basics | features/scheduling/shiftcenter/shift-center-overview.md %} first.

## Sort the items of a level

You can sort the items of a level on a given day:

1. Click a **column header of a day** in the schedule window to expand the day. An hour-scale appears.
2. Right-click the **hour scale** and select **Sort by Start Time**, **Sort by Schedule Position**, or **Sort by Activity**.
3. Select the **level** for which you want to sort the items.
4. To reverse the sort order, click the little **black arrow pointing down** in the hour scale.

{{ 9 | image: 'Context menu in the hour-scale of an expanded day', '70%' }}

## Filter the items of a level

You can filter the items of a level on a given day:

1. Right-click the **column header of a day** or click the day to expand it and then right-click the **hour-scale**.
   - In the hour-scale of the expanded day, select **Filter by Activity and Time**, then click **Define Filter**.
   - In the day column, click **Define filter**.
2. The following dialog appears. Select a value for **Level**, **Activity Type**, **Activity**, and **Time**. With _Time_, you restrict the filter to only show items that contain the selected time.

   {{ 10 | image: 'Dialog: Filter by Activity and Time', '40%' }}

3. Click _Ok_{:.doc-button}. The schedule view will update to only show the items that match your filter. If no data matches the filter, the schedule view will be empty.

To remove the filter, right-click the **hour scale**, select **Filter by Activity and Time** and then **Delete Filter**. You can also right click the **column header of a day** and choose **Delete Filter**.

To reactivate your last filter, follow the steps above but choose **Activate Filter** instead.
