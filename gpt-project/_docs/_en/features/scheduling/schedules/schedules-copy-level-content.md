---
title: Copy level content
toc: false
product_label:
  - advanced
  - enterprise
toc: true
description: Copy or back up your schedules and other elements in the different scheduling levels of injixo (Schedules feature).
---

In _Plan > Schedules_{:.breadcrumbs}, you can copy or back up your schedules into different levels. You can copy data from a level within the same level or to another level for a time period.

## Levels

For scheduling purposes, injixo stores data in scheduling levels. You can access the levels' content in Schedules and Shift Center. Other features read the data, e.g. Reports or Dashboards.

Scheduling levels can contain activities, day models, and availabilities. Activities and day models can also be shift requests or time off requests.

Depending on your {% link_new permissions | getting-started/configure-user-roles.md %}, you can view and edit the data in a level. To learn more about the available levels, read the article [Tips on Shift Center Usage](/tips-on-shift-center-usage#tip-9-working-with-different-levels).

## Use cases

Use the functionality:

- to create a backup of a complete schedule, e.g. to try out new scheduling methods
- to back up time-off requests, e.g before you re-run the shift generation.
- to speed up your scheduling process.

## Copy or back up a schedule

1. Click _Scheduling actions_{:.doc-button} and select **Copy level content**.
2. Configure the following parameters:

   | **Parameter**                            | **Description**                                                                                                                                                                  |
   | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Planning unit                            | The planning unit for which you want to run the copy job.                                                                                                                        |
   | Source level                             | The level from which you want to copy the data. An empty source level will delete the data in the target level.                                                                  |
   | Target level                             | The level to which you want to copy the data.                                                                                                                                    |
   | Date range                               | The date range for which you want to copy the data. <br> This field is pre-filled with the period that is currently selected in Schedules.                                       |
   | Target start date                        | (Optional) The date at which the copied time period should be inserted. <br> Use it, for example, to copy the data of an old schedule to a future time period on the same level. |
   | Empty source level content after copying | (Optional) Check this checkbox to delete the existing content from the source level.                                                                                             |

   > Warning
   >
   > Make sure you always select the correct source level. injixo will overwrite data in the following cases:
   >
   > - If the source level is empty, injixo will delete data in the target level.
   > - If the source level is wrong, and you selected the **Empty source level content after copying** option, injixo will delete data in the source level.
   >
   > Deleted data cannot be restored for a time frame. You can only {% link_new restore data | features/scheduling/schedules/schedules-edit.md | #see-and-restore-schedule-changes-in-the-history-tab %} for single days and employees from the history in Schedules and Shift Center.

3. (Optional) Click the **JobProcessor** link to open the Job Processor page in a new tab and track the progress of the copy job.
4. Click _Copy level content_{:.doc-button}.<br>
   injixo will redirect to Schedules. You will see a notification whether the copy job could be completed or not.
