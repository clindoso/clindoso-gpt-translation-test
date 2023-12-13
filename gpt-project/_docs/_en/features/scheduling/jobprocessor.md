---
title: Use the JobProcessor
description: Use the JobProcessor to view and cancel running optimization, reporting, and mass update jobs.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

JobProcessor gives you an overview of all the background jobs started in different parts of injixo. You can keep track of currently running jobs as well as view reports on completed jobs. You access JobProcessor from the Navigator, under _WFM > Administration > System > JobProcessor_{:.breadcrumbs}.

JobProcessor runs in the background and processes instructions as jobs from the following features:

- Scheduling
  - SchedulePro
    - Optimization
    - Planning/Scheduling Periods
      - Shifts/Generate
      - Shifts/Lottery
      - Shifts/Assign
      - Target Work Account/Calculate
      - Activity/Exchange
      - Level/Copy
      - Level/Delete
    - Insert Shift Sequences
- Monitoring
  - Reports
- Administration
  - Scheduling
    - Employees
      - Mass Update

Within JobProcessor, you can cancel jobs that are already running (e.g. if you need to stop an Optimization). You can view reports on previously run jobs. You do not start jobs within JobProcessor; instead, you use the relevant features within injixo.

## Running jobs

Once you select an option that requires JobProcessor and confirmed the parameters, the system opens the JobProcessor dialog with information about the job and its current processing status. The settings of the job determine when it is started and whether users can overwrite it or not. Jobs are run in the background, so you can navigate away from the page where you launched the job (e.g. Monitoring/Reports) or close the dialog box without canceling the job.

> Canceling Jobs
>
> Canceling a job only takes effect if the job has not yet started running, e.g. if there are several other jobs in the queue ahead of it. Once a submitted job has started on the server, clicking _Cancel_{:.doc-button} on the JobProcessor dialog does not stop the job. You must cancel running jobs directly from the JobProcessor. Note that many jobs (such as inserting shift sequences or running reports) typically complete within just a few seconds, which makes them difficult to stop once started.

## Jobs overview

Navigate to _WFM > Administration > System > JobProcessor_{:.breadcrumbs}.

The jobs overview provides information about the status of each job that is currently running or recently completed. For each job, it shows the job type, a unique ID number, the user who submitted it, its timeline and an indication of its progress to completion, together with a link to the result, e.g. the report that was produced. Note that the progress indicator does not necessarily indicate the percentage of total processing time that has elapsed; it simply gives a rough idea of activity. You can use the Status Group drop-down menu to filter the list to show all jobs, just processed jobs or just unprocessed jobs. You can use the User drop-down menu to filter the list to jobs submitted by a certain user. The list can be sorted by clicking the column headers, such as the user or the submitted date/time.

> User Rights
>
> Some options or jobs may not be displayed depending on your user rights.

## Job overview functions

In the JobProcessor job overview, the following operations are possible via the action bar, depending on your user role.

Select the job or jobs you want to act upon by checking the corresponding checkboxes in the left-hand column.

- _Submit Job again_{:.doc-button} (Play button)
  - This will run the job with the same settings that you selected previously; if you need to make changes, resubmit the job from the original feature.
- _Cancel Job_{:.doc-button} (Red circle with diagonal line)
  - Stops jobs which are in the `submitted` or `running` state. You can use _Submit Job again_{:.doc-button} later to re-submit the job.
- _Delete Job_{:.doc-button} (Red cross)
  - This removes jobs from the overview, provided that they are not running. The JobProcessor overview automatically cleans up old jobs over time.

The job overview is not automatically updated. The _Refresh Job Overview_{:.doc-button} button (blue circle with arrows) updates the view with new jobs and updates the status of jobs currently running.
