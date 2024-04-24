---
title: Use JobProcessor
description: Use JobProcessor to view and cancel running optimization, reporting, and mass update jobs.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

In _WFM > Administration > System > JobProcessor_{:.breadcrumbs}, you can see the key information on jobs started in different parts of injixo. You can keep track of currently running jobs and view reports on completed jobs. Jobs are run in the background. You can close the page from which you launched the job or close the dialog without canceling the job.

Go to JobProcessor to perform the following tasks:

- Cancel jobs that are already running (e.g. if you need to stop an optimization process)
- View reports on previously run jobs
- Restart previously run jobs
- Delete jobs from the list

The following jobs appear in JobProcessor:

- Scheduling actions: insert shift sequences, create optimized schedule, job optimization, replace activities, empty levels, copy level content
- Reports
- Mass update

> Note
>
> You cannot start jobs in JobProcessor. It only gives you an overview of the jobs started in the different parts of injixo.

## Filter by user or status

To filter jobs by status, use the **Status group** drop-down menu.

To filter jobs based on the user who started the job, follow these steps:

1. Click the {% icon select-user %} at the top of the page.
2. Select the user whose jobs you want to display.
3. Click _OK_{:.doc-button}.

## Restart jobs

To restart jobs, follow these steps:

1. Select the jobs you want to restart.
2. Click the {% icon jp-resubmit %} at the top left.

This will restart the jobs with their original settings.

## Cancel jobs

To cancel jobs that are not completed yet, follow these steps:

1. Select the jobs you want to cancel.
2. Click the {% icon jp-cancel %} at the top left.

## Delete jobs

To delete jobs from the list, follow these steps:

1. Select the jobs you want to delete.
2. Click the {% icon jp-delete %} at the top left.

## Refresh the job list

JobProcessor does not automatically update the progress of running jobs. To update the job list, click the {% icon jp-refresh %} at the top left.
