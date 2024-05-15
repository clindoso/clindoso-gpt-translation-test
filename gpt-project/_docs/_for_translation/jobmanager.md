---
title: Automate recurring jobs with JobManager
product_label:
  - enterprise
description: Automate report generation and more using the JobManager.
promote-service: enhanced-reporting
---

In _WFM > Administration > System > JobManager_{:.breadcrumbs}, users with admin access can set up job templates for recurring jobs, such as inserting shift sequences, creating reports, running the shift lottery or assignment, and calculating target work accounts.

 <!-- that can run with the privileges of other users. -->

<!-- The JobProcessor runs activated templates at the specified time. -->

## Create job templates

1. Click the {% icon item-add %}.
2. Enter a unique name (max. 50 characters).<br>
3. Check the **Enabled** checkbox to activate the scheduled execution.
4. Select a Job Type. This category has no impact but you can sort by job type later on.
5. Set a **Priority**. Value range: 1 to 10 (lowest)
6. (Optional) Select a different **User**. Defaults to the currently logged in user. Can be used to run job types with different permissions.
7. Click _OK_{:.doc-button}.<br>
   Configure the additional information required to run jobs in the sections Time Period for Job Processing, Job Processing Parameters, and Job Processing Dates.

<!-- To edit existing templates, click an item in the list. -->
<!-- Existing templates with the configured parameters can be edited via _JobManager_{:.menu-item} at any time. -->

<!-- outdated for cloud -->
<!-- {{ 1 | image: "Job Configuration", '50%' }} -->

### Set the time period for job processing

Define on which days an active template should be run. Periods can be absolute using a fixed date range or relative for current or previous weeks or months. Periods relative to the current date are useful for recurring jobs.

For example, to create a report every day at 6 AM for the previous day, select the following:

- Unit of Time: Relative
- Reference value until: -1 (Select **day** from the drop-down menu)
- Reference value from: -1 (available after you clicked **OK** to save the other general template properties)

### Set job processing parameters

When you save a job, only the time period for job processing is set. Add other general and job-specific parameters one by one for each job as follows:

1. Click the {% icon item-add %}.<br>
   A dialog window opens.
2. Enter a **Name** for the parameter.
3. Enter a **Value** for the parameter defined as name.

Learn more about available parameters and values in the article {% link_new JobManager examples | features/reporting/jobmanager/jobmanager-examples.md %}.

### Set job processing dates

Define on which days and at what time the JobProcessor runs active templates. You can set one or more processing dates for a job.

Choose from the following options:

- Weekday (Monday-Sunday)
- Day of the Month (1-31): Select a date that occurs in every month of the job processing period. For example, the 30th of February is not executed.
- Last Day of the Month

Each option requires you to set the time in the HH:MM format.

### Set job processing options

You can check the checkbox to delete the job after processing, which is useful to schedule and run jobs only once. <!-- more functionality in on-premise -->
