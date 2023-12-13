---
title: Create shift sequences
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Use shift sequences to set up repeating schedules.
redirect_from:
  - /shift-sequence-overview/
redirect_reason: filename used in old product onboarding
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/capacity/capacity-insert-shift-sequences.md
---

A shift sequence is a weekly pattern of day models or activities. With shift sequences, you can quickly insert these repeating patterns into your schedule, and let injixo optimize the rest of the schedule.

Shift sequences can save you many hours of work, since you do not have to schedule repeating patterns manually each time.

There are four use cases for shift sequences:

1. Specify days when certain shifts must be scheduled
2. Schedule recurring activities
3. Specify days when people do not work
4. Specify when shifts can be scheduled based on people's availabilities

Shift sequences consist of one or more rows. Each row is an individual pattern that can be inserted into the schedule.<br>
Each row contains cells that represent the days of the week. In the cells, you insert the day models or activities that you want to plan using the shift sequence.<br>
Each row represents a weekly pattern for your schedule, which is why the number of cells in a row must be a multiple of seven. A shift sequence can have a maximum of 53 rows because it cannot run longer than a year.

## Prerequisites

To create shift sequences, you first need to create {% link_new activities | features/administration/activities.md %} or {% link_new day models | features/administration/daymodels/daymodel-creation.md %}.<br>
After you have created shift sequences, you must {% link_new assign them to your people | features/administration/employee-overview.md | #assign-a-shift-sequence %} before you can insert them in your schedule.

>Note
>
>By default, the working week starts on Monday.
>
>You can change the first day of the week with the setting _48420_{:.id-label} _First day of the scheduling week_.

## Create shift sequences

Before you create your first shift sequence, determine how many shift sequences you will need as well as the number of rows and cells in each. This will depend entirely on your organization's needs, e.g. how many different shifts you plan, whether you plan recurring meetings, etc.

To create shift sequences, go to _Plan > Configuration > Shift sequences_{:.breadcrumbs} and follow these steps:

1. Click the New icon {% icon item-add | icon-only %} in the upper left.
2. Configure the settings of the shift sequence:<br>
  **Name**: Enter a unique name (max. 50 characters).<br>
  **Abbreviation**: Enter the name or a shorten version of it (max. 25 characters).<br>
  **Employee row(s)**: Enter the number of rows for the shift sequence (max. 53).<br>Each row will be assigned a number. Double-click on a row to rename it. You will need the row number or name to assign it to a person later.<br>
  **Duration**: Enter a value between 1 and 371 days. The duration must be a multiple of seven.
6. Click _Ok_{:.doc-button}.

>Note
>
>The duration of a shift sequence must always be a multiple of seven, even if your organization only opens five or six days a week. Shift sequences repeat automatically. A shift sequence of 5 days would insert the Monday shift in a Saturday cell, the Tuesday shift in a Sunday cell, etc.
>
>If you want to plan patterns with different durations (e.g. one for weekly meetings, and one for biweekly meetings), you need to create separate shift sequences.

Once you have created a shift sequence, you can set {% link_new validity periods | features/administration/set-a-validity-period.md %} for it:

1. Click the {% icon item-edit %} above the table.
2. Enter or choose the dates in the fields **Valid from** and **Valid to**.
3. Click _OK_{:.doc-button}.

### Insert day models

1. In the **Options** tile, select **Insert day model** from the drop-down menu on the left.
2. Select the day model you want to insert from the **Day model** drop-down menu.
3. Enter a **number**. This will be the amount of consecutive days in which you insert the day model.
4. In the table, click the first cell in which you want to insert the day model.<br>
  If you entered a number higher than one, the day model will be inserted in that cell and in as many cells to the right as needed to reach that number.

The shift sequence is saved automatically.

> Tip
>
> Use activities or fixed day models. If you insert variable day models in a shift sequence, the shift will always start at the earliest possible time.

### Insert activities

1. In the **Options** tile, select **Insert activity** from the drop-down menu on the left.
2. Choose the activity you want to insert from the **Activity** drop-down menu.
3. Enter a **number**. This will be the amount of consecutive days in which you insert the activity.
4. To specify the time when the activity is planned, enter a time period (in 24-hour format) in the fields **from** and **to**, or check the **full-day** checkbox.
5. In the table, click the first cell in which you want to insert the activity.<br>
  If you entered a number higher than one, the activity will be inserted in that cell and in as many cells to the right as needed to reach that number.

> Activities that end after midnight
>
> If you want to insert activities that end past midnight, add 24 to the end time, i.e. if the activity should end at 1 AM on the next day, enter 25:00.

## Edit shift sequences

1. In the **Shift sequences** tile, select a shift sequence from the drop-down menu.
2. Click _Apply_{:.doc-button}.
3. Click the {% icon item-edit %} in the top action bar to edit the name, abbreviation, number of employee rows, or the duration.<br>When you finish editing, click _Ok_{:.doc-button}.
4. Click {% icon item-edit %} in the action bar above the grid to edit the validity periods.<br>When you finish editing, click _Ok_{:.doc-button}.

### Delete elements from a shift sequence

To delete one or a few elements from the shift sequence, follow these steps:
1. In the **Shift sequences** tile, select a shift sequence from the drop-down menu.
2. Click _Apply_{:.doc-button}.
3. In the **Options** tile, select **Delete** from the drop-down menu.
4. Click the cells whose elements you want to delete.<br>
  The elements are deleted automatically.

To delete all elements from a shift sequence, follow these steps:

1. In the **Shift sequences** tile, select a shift sequence from the drop-down menu.
2. Click _Apply_{:.doc-button}.
3. In the **Options** tile, check the **Delete all** checkbox, and click _Apply_{:.doc-button}.

The elements are deleted automatically.

## Delete a shift sequence

1. In the **Shift sequences** tile, select a shift sequence from the drop-down menu.
2. Click _Apply_{:.doc-button}.
3. Click the {% icon item-delete %} in the top action bar.
4. In the confirmation dialog, click _Yes_{:.doc-button}.

## Use cases

You can use shift sequences for various scenarios.

### Use case 1: Specify days when certain shifts must be scheduled

This use case applies, for example, when you need to plan early and late shifts for different groups of people. Or if you have a team member who cannot start working before 11 AM on Mondays, although they are available earlier all other days of the week. 
 
You can learn more about whether this use case applies to you and how to configure shift sequences accordingly in our Academy training video below:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls> 
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-1.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-1.vtt" kind="subtitles" srclang="en" label="English" default>
   </video>
</div>
<br>

### Use case 2: Schedule recurring activities

This use case applies, for example, when you need to plan meetings that take place every week, or if you want to schedule a person to do one-hour slot of back-office work every day at a specific time.

You can learn more about whether this use case applies to you and how to configure shift sequences accordingly in our Academy training video below:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls>
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-2.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-2.vtt" kind="subtitles" srclang="en" label="English" default>
  </video>
</div>
<br>

### Use case 3: Specify days when people do not work

This use case applies, for example, if you need to define specific patterns of days off for individual people. 

You can learn more about whether this use case applies to you and how to configure shift sequences accordingly in our Academy training below:

  <div class="inline-video-container">
    <video class="inline-video-player-v" controls> 
     <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-3.mp4" type="video/mp4">
     <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-3.vtt" kind="subtitles" srclang="en" label="English" default>
    </video>
  </div>
<br>

### Use case 4: Specify when shifts can be scheduled based on people's availabilities

This use case applies when you want to schedule people with varying availability.

You can learn more about whether this use case applies to you and how to configure shift sequences accordingly in our Academy training below:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls>
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-4.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-4.vtt" kind="subtitles" srclang="en" label="English" default>
  </video>
</div>
<br>

## Generate a report

You can generate a report in PDF format that includes all data of a shift sequence. To generate the report, proceed as follows:

1. In the **Shift sequences** tile on the left, select the shift sequence for which you want to generate a report.
2. Click _Apply_{:.doc-button}.
3. Click _Report_{:.doc-button} on top of the table.
4. In the dialog, you can check the checkbox to send the report to the email adress used for your injixo account.

The report shows the start and end times of the activities or day models included in the shift sequence as well as their net duration in hours. The report is structured in weeks.
Additionally, the report shows the following totals and averages of the net duration:

- Row Total: Net duration of all activities or day models in the shift sequence
- Sum column: Total of the net duration of the activities or day models per week
- Row Average: Average value for all values in the column Total
