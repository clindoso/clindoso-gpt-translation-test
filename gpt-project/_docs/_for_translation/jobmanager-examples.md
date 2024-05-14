---
title: JobManager examples
product_label:
  - enterprise
description: Learn about important job types in injixo and what they are used for.
---

In _WFM > Administration > System > JobManager_{:.breadcrumbs}, you can automate the start of different jobs, such as creating reports or inserting shift sequences. When you create a job template, you need to {% link_new configure specific parameters | features/reporting/jobmanager/jobmanager.md | #set-job-processing-parameters %}.

This article illustrates how to configure different job types in JobManager.


<style>
table {
  width: 100%;
}

table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

## Create reports

<!-- {{ 1 | image: 'Sending Job Manager Report via Email', '50%' }} -->


| Parameter       | Description                                                          |
| --------------- | -------------------------------------------------------------------- |
| cmd             | Internal report name                                                 |
| p               | Planning unit ID                                                     |
| e               | Employees<br>Values: all, individual IDs delimited by hyphen (-)     |
| c               | Contracts<br>Values: all, individual IDs delimited by hyphen (-)     |
| se              | Selections<br>Values: all, individual IDs delimited by hyphen (-)    |
| level           | [Level ID](#level-id)                                                |
| lid             | [Language ID](#language-id)                                          |
| targethtml      | Output Format<br>Values: 0 (PDF), 1 (HTML)                           |
| targetanonymous | Standard or Anonymous reports<br>Values: 0 (standard), 1 (anonymous) |
| jobnameid       | (Optional) Internal report ID that can be blank                      |


All reports that you automate using JobManager require the cmd parameter. Expand the following list to see what value you need to assign to the cmd parameter for each report type:

<details style="padding-bottom: 20px;">
<summary><strong>Weekly schedule reports</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Report name</th>
      <th>Cmd parameter value</th>
    </tr>
  </thead>
  <tr>
    <td>Weekly Schedule I</td>
    <td>shiftplan</td>
  </tr>
  <tr>
    <td>Weekly Schedule I with Filter</td>
    <td>shiftplan showconsel=1</td>
  </tr>
  <tr>
    <td>Weekly Schedule I (without Full-Day Activities)</td>
    <td>shiftplansel hidefda=1</td>
  </tr>
  <tr>
    <td>Weekly Schedule II (without Full-Day Activities)</td>
    <td>shiftplansel showbreaks=1 hidefda=1</td>
  </tr>
  <tr>
    <td>Weekly Schedule II (without Breaks) (On-premise only)</td>
    <td>shiftplansel</td>
  </tr>
  <tr>
    <td>Weekly Schedule (without Breaks) (without Full-Day Activities)</td>
    <td>shiftplansel hidefda=1</td>
  </tr>
  <tr>
    <td>Weekly Schedule III</td>
    <td>weeklyworkplan</td>
  </tr>
  <tr>
    <td>Weekly Schedule III (without Full-Day Activities)</td>
    <td>weeklyworkplan hidefda=1</td>
  </tr>
</table>
</details>  

<details style="padding-bottom: 20px;">
<summary><strong>Daily schedule reports</strong>
</summary>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Report name</th>
      <th>Cmd parameter value</th>
    </tr>
  </thead>
  <tr>
    <td>Daily Schedule I</td>
    <td>staffworkpubar</td>
  </tr>
  <tr>
    <td>Daily Schedule I with Breaks</td>
    <td>staffworkpubarbreaks</td>
  </tr>
  <tr>
    <td>Daily Schedule I (without absences, illnesses and vacation)</td>
    <td>staffworkpubarabsences</td>
  </tr>
  <tr>
    <td>Daily Schedule II</td>
    <td>staffworktimebar</td>
  </tr>
  <tr>
    <td>Daily Schedule II with Breaks</td>
    <td>staffworktimebarbreaks</td>
  </tr>
  <tr>
    <td>Daily Schedule II with Shift Summary</td>
    <td>staffworktimebartotal</td>
  </tr>
  <tr>
    <td>Daily Schedule II with Shift Summary and Breaks</td>
    <td>staffworktimebartotalbreaks</td>
  </tr>
  <tr>
    <td>Daily Schedule III</td>
    <td>stafffworkactbar</td>
  </tr>
  <tr>
    <td>Daily Schedule III with Breaks</td>
    <td>staffworkactbarbreaks</td>
  </tr>
  <tr>
    <td>Daily Schedule IV</td>
    <td>staffworkpubarsel</td>
  </tr>
  <tr>
    <td>Daily Schedule V</td>
    <td>staffworktimebarsel</td>
  </tr>
  <tr>
    <td>Daily Schedule VI</td>
    <td>staffworkactbarsel</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Vacation and absence schedule</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Report name</th>
      <th>Cmd parameter value</th>
    </tr>
  </thead>
  <tr>
    <td>Absence Schedule</td>
    <td>absence</td>
  </tr>
  <tr>
    <td>General Absence Schedule</td>
    <td>realabsence</td>
  </tr>
  <tr>
    <td>Absence Schedule with Day Status and Full-Day Activities</td>
    <td>orgabscalendar</td>
  </tr>
  <tr>
    <td>Vacation Schedule I</td>
    <td>holiday</td>
  </tr>
  <tr>
    <td>Vacation Schedule I with Full-Time-Equivalent</td>
    <td>vacation_fte</td>
  </tr>
  <tr>
    <td>Vacation Schedule II</td>
    <td>staffworktimebartotal</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Absence, illness- and vacation statistics</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Report name</th>
      <th>Cmd parameter value</th>
    </tr>
  </thead>
  <tr>
    <td>Absence Statistics</td>
    <td>absence_c</td>
  </tr>
  <tr>
    <td>Absence Statistics with Total Amount Column</td>
    <td>absence_t</td>
  </tr>
  <tr>
    <td>Absence Statistics with Full-Time-Equivalent</td>
    <td>absence_fte</td>
  </tr>
  <tr>
    <td>Vacation Statistics</td>
    <td>holiday_c</td>
  </tr>
  <tr>
    <td>Vacation Statistics with Total Amount Column</td>
    <td>holiday_t</td>
  </tr>
  <tr>
    <td>Vacation Statistics with Full-Time-Equivalent</td>
    <td>holiday_fte</td>
  </tr>
  <tr>
    <td>Illness Statistics</td>
    <td>illness_c</td>
  </tr>
  <tr>
    <td>Illness Statistics with Total Amount Column</td>
    <td>illness_t</td>
  </tr>
  <tr>
    <td>Illness Statistics with Full-Time-Equivalent</td>
    <td>illness_fte</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Work time reports</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Report name</th>
      <th>Cmd parameter value</th>
    </tr>
  </thead>
  <tr>
    <td>Time Worked Times per Planning Unit</td>
    <td>diff_pu</td>
  </tr>
  <tr>
    <td>Activities in Hours</td>
    <td>activ_st</td>
  </tr>
  <tr>
    <td>Activities in Percent</td>
    <td>activ_per</td>
  </tr>
  <tr>
    <td>Activity Statistics</td>
    <td>activity_stat</td>
  </tr>
  <tr>
    <td>Net Working Times (On-premise only)</td>
    <td>realized_hours</td>
  </tr>
  <tr>
    <td>Activity Analysis</td>
    <td>state_train</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Break schedules</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Report name</th>
      <th>Cmd parameter value</th>
    </tr>
  </thead>
  <tr>
    <td>Break Schedule I</td>
    <td>pause</td>
  </tr>
  <tr>
    <td>Break Schedule II</td>
    <td>pausetwo</td>
  </tr>
  <tr>
    <td>Break Schedule III</td>
    <td>pausethree</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Other reports</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Report name</th>
      <th>Cmd parameter value</th>
    </tr>
  </thead>
  <tr>
    <td>Difference in Working Times Between Levels</td>
    <td>worktimes</td>
  </tr>
  <tr>
    <td>Time Accounts Reports</td>
    <td>timeacount</td>
  </tr>
  <tr>
    <td>Shifts with a Requirement</td>
    <td>genshifts</td>
  </tr>
  <tr>
    <td>Days With Night, Weekend and Holiday Schedules (On-premise only)</td>
    <td>shifttype</td>
  </tr>
  <tr>
    <td>Capacities According to Contract Type</td>
    <td>capacity</td>
  </tr>
  <tr>
    <td>Training Programs (On-premise only)</td>
    <td>train_camp_summary</td>
  </tr>
  <tr>
    <td>Minimum Staffing (On-premise only)</td>
    <td>minimalcoverage</td>
  </tr>
  <tr>
    <td>Scheduling Rules Configuration</td>
    <td>schedulingrules</td>
  </tr>
  <tr>
    <td>Vacation Overview</td>
    <td>vacationoverview</td>
  </tr>
  <tr>
    <td>Shift Overview</td>
    <td>monthlyshiftplan</td>
  </tr>
  <tr>
    <td>Yearly Working Hours Analysis</td>
    <td>work_time_analysis</td>
  </tr>
  <tr>
    <td>Conformance Report</td>
    <td>conformance</td>
  </tr>
  <tr>
    <td>Adherence Report</td>
    <td>adherence</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Exchange reports</strong>
</summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Report name</th>
      <th>Cmd parameter value</th>
    </tr>
  </thead>
  <tr>
    <td>Exchanges I (On-premise only)</td>
    <td>shiftexchdetails</td>
  </tr>
  <tr>
    <td>Exchanges II (On-premise only)</td>
    <td>shiftexchnodetails</td>
  </tr>
  <tr>
    <td>Exchange Statistics (On-premise only)</td>
    <td>shiftexchstats</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Employee work schedules</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Report name</th>
      <th>Cmd parameter value</th>
    </tr>
  </thead>
  <tr>
    <td>Employee Work Schedule I (List)</td>
    <td>staffwork showbreaks=1</td>
  </tr>
  <tr>
    <td>Employee Work Schedule I (List) (Without Breaks)</td>
    <td>staffwork</td>
  </tr>
  <tr>
    <td>Employee Work schedule II (List)</td>
    <td>staffworkabsill</td>
  </tr>
  <tr>
    <td>Employee Work Schedule III (Graph)</td>
    <td>staffworkbar</td>
  </tr>  
  <tr>
    <td>Employee Work Schedule IV (6 Weeks)</td>
    <td>staffsixweeksnobreaks</td>
  </tr>  
  <tr>
    <td>Employee Work Schedule IV (6 Weeks) (Activities)</td>
    <td>staffsixweeks</td>
  </tr>
  <tr>
    <td>Employee Work Schedule IV (6 Weeks) (No Breaks)</td>
    <td>staffsixweekstwo</td>
  </tr>
</table>
</details>

<details style="padding-bottom: 40px;">
<summary><strong>Other employee reports</strong></summary>
<br>
<table>
  <thead>
    <tr>
      <th>Report name</th>
      <th>Value for the <strong>cmd</strong> parameter</th>
    </tr>
  </thead>
  <tr>
    <td>Employee Request Schedule I (List) (On-premise only)</td>
    <td>staff_wish</td>
  </tr>
  <tr>
    <td>Hours Worked per Employee I</td>
    <td>diff_st</td>
  </tr>
  <tr>
    <td>Hours Worked per Employee II</td>
    <td>diff_st_two</td>
  </tr>
  <tr>
    <td>Monthly Employees' Journal (On-premise only)</td>
    <td>journal</td>
  </tr>
  <tr>
    <td>Organisational Chart</td>
    <td>organ</td>
  </tr>
  <tr>
    <td>Weekend Working Hours I</td>
    <td>weekendwork</td>
  </tr>
  <tr>
    <td>Weekend Working Hours II</td>
    <td>weekendwork2</td>
  </tr>
  <tr>
    <td>Weekend Working Hours III (Lottery and Assignment) (On-premise only)</td>
    <td>weekendwork3</td>
  </tr>
  <tr>
    <td>Anniversaries</td>
    <td>jubilee</td>
  </tr>
  <tr>
    <td>Vacation Slip (On-premise only)</td>
    <td>hd_list</td>
  </tr>
  <tr>
    <td>Staff by Contract Type</td>
    <td>read</td>
  </tr>
  <tr>
    <td>Fluctuation I</td>
    <td>fluct</td>
  </tr>
  <tr>
    <td>Fluctuation II</td>
    <td>detailfluctuation</td>
  </tr>
  <tr>
    <td>Yearly Overview (On-premise only)</td>
    <td>absencejob_cal</td>
  </tr>
  <tr>
    <td>Compensation Days for Weekend Work (On-premise only)</td>
    <td>comp_week_work</td>
  </tr>
  <tr>
    <td>Staff Shift Sequences</td>
    <td>staffshiftseq</td>
  </tr>
  <tr>
    <td>Timetable (On-premise only)</td>
    <td>monthly_work_sched</td>
  </tr>
  <tr>
    <td>Workplace (On-premise only)</td>
    <td>assignedworkplaces</td>
  </tr>
  <tr>
    <td>Holiday Work (Lottery And Assignment)</td>
    <td>laaholidaywork</td>
  </tr>
  <tr>
    <td>Minimum Occupancy By Sites (On-premise only)</td>
    <td>deskminstaffing</td>
  </tr>
  <tr>
    <td>Workplace Occupancy (On-premise only)</td>
    <td>deskalloc</td>
  </tr>
  <tr>
    <td>Validity Of Master Data (On-premise only)</td>
    <td>masterdatavalidity</td>
  </tr>
  <tr>
    <td>Coach/Trainee - Scheduling Differences (On-premise only)</td>
    <td>coach_trainee</td>
  </tr>
  <tr>
    <td>Master Data Overview</td>
    <td>employeemasterdata</td>
  </tr>
  <tr>
    <td>Group Authorization (On-premise only)</td>
    <td>group_auth</td>
  </tr>
  <tr>
    <td>Modifying Master Data</td>
    <td>audit</td>
  </tr>
</table>
</details>


## Insert shift sequences

<!-- {{ 2 | image: 'Insert Shift Sequences', '50%' }} -->

| Parameter    | Description                                                                                                                       |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| delete1      | Delete full-day activities<br>Values: 1 (yes), 0 (no)                                                                             |
| delete2      | Delete availability periods<br>Values: 1 (yes), 0 (no)                                                                            |
| delete3      | Delete all activities and shifts<br>Values: 1 (yes), 0 (no)                                                                       |
| level_id     | [Level ID](#level-id)                                                                                                             |
| lid          | [Language ID](#language-id)                                                                                                       |
| nr_of_seq    | Number of employees with shift sequences<br>Value: all                                                                            |
| option       | Internal ID<br>Value: 2                                                                                                           |
| planunit_id  | Planning unit ID                                                                                                                  |
| selection_id | Selections<br>Values: -1 (all selections), specific IDs delimited by hyphen (-)                                                   |
| shiftseq_id  | IDs of shift sequences assigned to the selected employees delimited by hyphen (-). Required unless type is set.                   |
| type         | (Optional) Selects all shift sequences for the selected employees. If used, the shiftseq_id parameter can be blank.<br>Value: all |

### Lottery and assignment

<!-- {{ 3 | image: 'Lottery or Assignment', '50%' }} -->

| Parameter   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| doreporting | Log file<br>Values: 1 (yes), 0 (no)                                                                                                                                                                                                                                                                                                                                                                                                          |
| e           | Employees<br>Values: all, individual IDs delimited by hyphen (-)                                                                                                                                                                                                                                                                                                                                                                             |
| lid         | [Language ID](#language-id)                                                                                                                                                                                                                                                                                                                                                                                                                  |
| modelcase   | Internal ID<br>Values: 10 (shift assignment), 11 (shift lottery)                                                                                                                                                                                                                                                                                                                                                                             |
| observecorr | Take the tolerance value for the start time into account<br>Values: 0 (no), 1 (yes)                                                                                                                                                                                                                                                                                                                                                          |
| periodid    | Planning period ID or multiple IDs delimited by comma. The correct planning period ID can be found in the source code of the page via dev tools (first part of the value in the data-flip-id element) or by using the [API](https://legacy-api.injixo.com/#tag/Planning-Periods/operation/getV1PlanningPeriodsStartDate). If the time period for job processing is set to relative, only the relevant planning period is taken into account. |
| puid        | Planning unit ID                                                                                                                                                                                                                                                                                                                                                                                                                             |
| staffcount  | Number of people. This parameter is mandatory but its value is always ignored. You can enter any value.                                                                                                                                                                                                                                                                                         |
| tolerance   | Maximum deviation from the average start time<br>Value: Time using format HH:MM), 00:00 (if the observecorr parameter is 0)                                                                                                                                                                                                                                                                                                                  |

### Copy level

The **Copy level content** functionality can be found under _Plan > Schedules > Scheduling actions_{:.breadcrumbs}.

| Parameter     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| copystartdate | Start date for inserting the data in [Julian date format](https://www.onlineconversion.com/julian_date.htm). Data is shifted if the date is not the start date of the planning period. |
| deletesource  | Delete the source level.<br>Values: 0 (Keep source level), 1 (delete source level)                                                                                                                                                                                                                                                                                                                                                           |
| lid           | [Language ID](#language-id) for error messages                                                                                                                                                                                                                                                                                                                                                                                               |
| e             | Employees<br>Values: all, individual IDs delimited by hyphen (-)                                                                                                                                                                                                                                                                                                                                                                             |
| modelcase     | Internal ID.<br>Values: 15 (copy level), 16 (delete level)                                                                                                                                                                                                                                                                                                                                                                                 |
| periodid      | Planning period ID or multiple IDs delimited by comma. The correct planning period ID can be found in the source code of the page via dev tools (first part of the value in the data-flip-id element) or by using the [API](https://legacy-api.injixo.com/#tag/Planning-Periods/operation/getV1PlanningPeriodsStartDate). If the time period for job processing is set to relative, only the relevant planning period is taken into account. |
| puid          | ID of the planning unit. Can be filtered by ID when separated by a delimiter (-).                                                                                                                                                                                                                                                                                                                                                           |
| sourcelevel   | [Level ID](#level-id) (Source)                                                                                                                                                                                                                                                                                                                                                                                                               |
| targetlevel   | [Level ID](#level-id) (Target)                                                                                                                                                                                                                                                                                                                                                                                                               |
| staffcount    | Required but not used. Enter value 0                                                                                                                                                                                                                                                                                     |
| selectionid   | Selection ID<br>Values: -1 (all selections), specific ID delimited by hyphen (-)                                                                                                                                                                                                                                                                                                                                                             |

## Email parameters

Email parameters are optional. If the email parameters are not configured, reports will only be available in the JobProcessor.

| Parameter  | Description                                                                                                                                                                                                                       |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| em         | Employee IDs<br>Values: -1 (all), multiple IDs delimited by hyphen (-)                                                                                                                                                            |
| sendtoall  | Send a single email to the selected employees<br>Values: 1 (yes), 0 (no)                                                                                                                                                          |
| sendperemp | Send an individual email to the selected employee. Not available for all reports <!-- which? --><br>Values: 1 (yes), 0 (no)                                                                                                       |
| email      | Recipient email address. Multiple email recipients not supported. If needed, use an email distribution list that forwards internally to multiple recipients. The email parameter is not used when the em parameter specifies IDs. |
| emailtype  | Employee email address<br>Values: 1 (email 1), 3 (email 2), 2 (both). injixo Cloud versions does not support email 2.                                                                                                             |
| comments   | Optional text for the email message                                                                                                                                                                                               |

## Language ID

The **lid** parameter defines the language ID for the resulting report and supports the following IDs:

English US (1033)<br>
German (1031)<br>
French (1036)<br>
Italian (1040)<br>
Spanish modern (3082)<br>
Spanish standard (1034)<br>
Dutch (1043)<br>
Swedish (1053)<br>
English UK (2057)<br>
Polish (1045)

## Level ID

The **level** parameter defines the level from which data is read and supports the following IDs:

1000 (plan)<br>
3000 (current status)<br>
5000 (external system)<br>
4000 (time recording)<br>
2000 (request)<br>
2001 (alternative request)<br>
2002 (holiday/absence request)<br>
6000 (availability)<br>
6001 (on-call duty)<br>
4001 (correction)<br>
8000 (version 1)<br>
8001 (version 2)<br>
8002 (version 3)
