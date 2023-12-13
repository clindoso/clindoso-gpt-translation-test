---
title: Automate recurring jobs with JobManager
product_label:
  - enterprise
description: Automate report generation and more using the JobManager.
promote-service: enhanced-reporting
---

The _JobManager_{:.menu-item} in _Administration > System > JobManager_{:.breadcrumbs} allows injixo Enterprise users with administrator privileges to configure templates for recurring jobs that can run with the privileges of specific users.

The JobProcessor runs activated templates at the specified time. Various job types are available, e.g. to insert shift sequences, create reports, run a lottery, assign shifts, and calculate target work accounts.

## Creating templates

1. Enter a name for the job processing template.
2. Check the _Activated_ box to activate the job for scheduled execution.
3. Define the job type.
4. Specify a value between 1 and 10 for the _Priority_. 1 corresponds to the highest priority.
5. Then select the _user_ that has the required user rights for the specified job type.

Existing templates with the configured parameters can be edited via _JobManager_{:.menu-item} at any time.

## Configure jobs

After saving the general data you can assign the Job Processing Period, the Job Processing Parameters, the Job Processing Dates and the Job Processing Options.

{{ 1 | image: "Job Configuration", '50%' }}

### Periods

Periods define on which days and at what time the activated template is started.

Relative or absolute specifications are possible. For the _type of time entry_ select 'Absolute' for fixed or 'Relative' for variable periods, e.g. 'current week', 'last week', 'current month' or 'last month'. If, for example, a report is to be sent daily at 6:00 a.m. for the previous day, enter 'Relative' as the job processing period _Type of time entry_ and _Reference value from:_ '-1', _Reference value to:_ '-1', 'Day'.Also note the additional information in the _processing date_ for the weekdays.

## Parameter

General and specific parameters are available for each job, which must be specified differently for each job. It is necessary to specify additional parameters using the {% icon item-add %}.

The parameter **lid** (language or language ID) is sent with all job types, so you define that a report will be created in the specific language. Available languages are: English US (1033), German (1031), French (1036), Italian (1040), Spanish modern (3082), Spanish standard (1034), Dutch (1043), Swedish (1053), English UK (2057), Polish (1045).A **level** parameter is available for report generation, which defines the source level from which the data originates.The following levels are supported:1000 (plan), 3000 (current status), 5000 (external system), 4000 (time recording),2000 (request), 2001 (alternative request), 2002 (holiday/absence request), 6000 (availability), 6001 (on-call duty), 4001 (correction), 8000 (version 1), 8001 (version 2), 8002 (version 3).  
The article {% link_new Report names and parameters | features/reporting/jobmanager/jobmanager-examples.md %} lists and explains other specific parameters.

### Processing dates

The following options are available: _Weekday_ (Monday-Sunday), _Day of the Month_ (1-31) and _Last Day of the Month_. When selecting a _Day of the Month_, only select a date that occurs in the months of the processing period. Job processing that is to take place on the 30th day of each month is not executed for the month of February. In addition to each processing date, the desired _Time_ must be specified. For example, if you want a report to be sent daily at 6:00 a.m. for the previous day, use the _Day of the Week_ option and add each individual day with the corresponding time. After saving, the processing date defined by you is stored under the _Job Processing Parameters_ and can be deleted or edited here.It is also possible to store several processing dates for a job.

### Options

As options, you can specify whether a message should be sent to the user after a job has been completed. Alternatively, it is also possible to send the result of the job directly as an attachment. Both is only possible for users who have also assigned employees.
