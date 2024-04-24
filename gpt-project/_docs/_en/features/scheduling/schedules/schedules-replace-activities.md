---
title: Batch replace an activity
product_label:
  - advanced
  - enterprise
description: Replace all instances of an activity with another activity in an existing schedule (Schedules feature).
toc: false
---

In _Plan > Schedules_{:.breadcrumbs}, you can batch-replace an activity with another activity in an existing schedule.

## Prerequisite

Make sure that all relevant activities are assigned to the selected {% link_new planning unit | features/administration/create-and-manage-planning-units.md %}.

## Batch replace an activity

1. Under _Plan > Schedules_{:.breadcrumbs}, click _Scheduling actions_{:.doc-button}.
2. Select **Replace activities** from the drop-down menu.<br>The **Replace activities** page opens.
3. Configure the **Settings** section:
   - **Planning unit**
   - **Activity to be replaced**
   - **Replace activity with**
   - **Levels**: Check one or more checkboxes to select the levels in which activities will be replaced.
   - **Date range**: (Optional) Select a different date range. By default, the currently selected period in Schedules is selected for the date range.
4. In the **Employees** section, select the employees you want to replace the activity for. You can also filter the list by a selection or an employee filter.
5. Click _Replace activities_{:.doc-button}.

Before you start the job, you can click the **JobProcessor** link in the lower right to open a separate tab where you can follow the progress. Click _![Back button](/assets/img/common/injixo-ui/back.png)_{:.doc-button-icon} on top or _Cancel_{:.doc-button} at the bottom to return to the Schedules page without running the job.

{{ 1 | image: 'Replace activities', '80%' }}

You are redirected to the Schedules page. Depending on whether the job could be started successfully or not, a success or error message will be displayed.
