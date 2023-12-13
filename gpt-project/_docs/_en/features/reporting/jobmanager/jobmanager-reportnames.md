---
title: Report names and parameters
product_label:
  - enterprise
description: Learn about the different *cmd* parameters which are needed to generate reports automatically using the JobManager.
---

As described in the {% link_new report examples | features/reporting/jobmanager/jobmanager-examples.md | #sending-reports-by-email %} a parameter _cmd_ is required to create reports automatically via the JobManager. Below is a complete list of report names that must be defined as _cmd_ parameter for the corresponding report.

Some reports accept one or two additional parameters _showconsel_ (Show Contracts And Selections), _hidefda_ (Hide Full Day Activities) and _showbreaks_ (Show Breaks) in addition to the name. These are used to show or hide certain things in a report with the same _cmd_ parameter. Not all reports support additional parameters, so we have included them in the second column.

## Weekly schedules

| Report                                                         | CMD Parameter                           |
| -------------------------------------------------------------- | --------------------------------------- | -------------------------- |
| Weekly Schedule I                                              | cmd=shiftplan                           |
| Weekly Schedule I with Filter                                  |                                         | cmd=shiftplan showconsel=1 |
| Weekly Schedule I (without Full-Day Activities)                | cmd=shiftplansel hidefda=1              |
| Weekly Schedule II (without Full-Day Activities)               | cmd=shiftplansel showbreaks=1 hidefda=1 |
| Weekly Schedule II (without Breaks)                            | cmd=shiftplansel                        |
| Weekly Schedule (without Breaks) (without Full-Day Activities) | cmd=shiftplansel hidefda=1              |
| Weekly Schedule III                                            | cmd=weeklyworkplan                      |
| Weekly Schedule III (without Full-Day Activities)              | cmd=weeklyworkplan hidefda=1            |

## Daily schedules

| Report                                                      | CMD Parameter                   |
| ----------------------------------------------------------- | ------------------------------- |
| Daily Schedule I                                            | cmd=staffworkpubar              |
| Daily Schedule I with Breaks                                | cmd=staffworkpubarbreaks        |
| Daily Schedule I (without absences, illnesses and vacation) | cmd=staffworkpubarabsences      |
| Daily Schedule II                                           | cmd=staffworktimebar            |
| Daily Schedule II with Breaks                               | cmd=staffworktimebarbreaks      |
| Daily Schedule II with Shift Summary                        | cmd=staffworktimebartotal       |
| Daily Schedule II with Shift Summary and Breaks             | cmd=staffworktimebartotalbreaks |
| Daily Schedule III                                          | cmd=staffworkactbar             |
| Daily Schedule III with Breaks                              | cmd=staffworkactbarbreaks       |
| Daily Schedule IV                                           | cmd=staffworkpubarsel           |
| Daily Schedule V                                            | cmd=staffworktimebarsel         |
| Daily Schedule VI                                           | cmd=staffworkactbarsel          |

## Vacation and absence schedule

| Report                                                   | CMD Parameter          |
| -------------------------------------------------------- | ---------------------- |
| Absence Schedule                                         | cmd=absence            |
| General Absence Schedule                                 | cmd=realabsence        |
| Absence Schedule with Day Status and Full-Day Activities |  cmd=orgabscalendar    |
| Vacation Schedule I                                      | cmd=holiday            |
| Vacation Schedule I with Full-Time-Equivalent            | cmd=vacation_fte       |
| Vacation Schedule II                                     | cmd=vacationwithunpaid |

## Absence, illness- and vacation statistics

| Report                                        | CMD Parameter   |
| --------------------------------------------- | --------------- |
| Absence Statistics                            | cmd=absence_c   |
| Absence Statistics with Total Amount Column   | cmd=absence_t   |
| Absence Statistics with Full-Time-Equivalent  | cmd=absence_fte |
| Vacation Statistics                           | cmd=holiday_c   |
| Vacation Statistics with Total Amount Column  | cmd=holiday_t   |
| Vacation Statistics with Full-Time-Equivalent | cmd=holiday_fte |
| Illness Statistics                            | cmd=illness_c   |
| Illness Statistics with Total Amount Column   | cmd=illness_t   |
| Illness Statistics with Full-Time-Equivalent  | cmd=illness_fte |

## Work time reports

| Report                              | CMD Parameter      |
| ----------------------------------- | ------------------ |
| Time Worked Times per Planning Unit | cmd=diff_pu        |
| Activities in Hours                 | cmd=activ_st       |
| Activities in Percent               | cmd=activ_per      |
| Activity Statistics                 | cmd=activity_stat  |
| Net Working Times                   | cmd=realized_hours |
| Activity Analysis                   | cmd=state_train    |

## Break schedules

| Report             | CMD Parameter  |
| ------------------ | -------------- |
| Break Schedule I   | cmd=pause      |
| Break Schedule II  | cmd=pausetwo   |
| Break Schedule III | cmd=pausethree |

## Other reports

| Report                                         | CMD Parameter          |
| ---------------------------------------------- | ---------------------- |
| Difference in Working Times Between Levels     | cmd=worktimes          |
| Time Accounts Report                           | cmd=timeacount         |
| Shifts with Requirement                        | cmd=genshifts          |
| Days With Night, Weekend und Holiday Schedules |
| Capacities According To Contract Type          | cmd=capacity           |
| Training Models                                | cmd=train_camp_summary |
| Minimum Staffing                               | cmd=minimalcoverage    |
| Scheduling Rules Configuration                 | cmd=schedulingrules    |
| Vacation Overview                              | cmd=vacationoverview   |
| Shift Overview                                 | cmd=monthlyshiftplan   |
| Yearly Working Time Analysis                   | cmd=work_time_analysis |
| Conformance Report                             | cmd=conformance        |
| Adherence Report                               | cmd=adherence          |

## Exchange reports

| Report              | CMD Parameter          |
| ------------------- | ---------------------- |
| Exchanges I         | cmd=shiftexchdetails   |
| Exchanges II        | cmd=shiftexchnodetails |
| Exchange Statistics | cmd=shiftexchstats     |

## Employee work schedules

| Report                                              | CMD Parameter              |
| --------------------------------------------------- | -------------------------- |
| Employee Work Schedule I (List)                     | cmd=staffwork showbreaks=1 |
| Employee Work Schedule I (List) (without Breaks)    | cmd=staffwork              |
| Employee Work Schedule II (List)                    | cmd=staffworkabsill        |
| Employee Work Schedule III (Graph)                  | cmd=staffworkbar           |
| Employee Work Schedule IV (6 Week)                  | cmd=staffsixweeksnobreaks  |
| Employee Work Schedule IV (6 Week) (Activities)     | cmd=staffsixweeks          |
| Employee Work Schedule IV (6 Week) (without Breaks) | cmd=staffsixweekstwo       |

## Other employee reports

| Report                                             | CMD Parameter          |
| -------------------------------------------------- | ---------------------- |
| Employee Request Schedule I (List)                 | cmd=staff_wish         |
| Working Times per Employee I                       | cmd=diff_st            |
| Working Times per Employee II                      | cmd=diff_st_two        |
| Montly Employees' Journal                          | cmd=journal            |
| Organisational Chart                               | cmd=organ              |
| Weekend Working Hours I                            | cmd=weekendwork        |
| Weekend Working Hours II                           | cmd=weekendwork2       |
| Weekend Working Hours III (Lottery and Assignment) | cmd=weekendwork3       |
| Anniversaries                                      | cmd=jubilee            |
| Vacation Slip                                      | cmd=hd_list            |
| Employees per Contract Type                        | cmd=read               |
| Fluctuation I                                      | cmd=fluct              |
| Fluctuation II                                     | cmd=detailfluctuation  |
| Yearly Overview                                    | cmd=absencejob_cal     |
| Compensation Days for Weekend Work                 | cmd=comp_week_work     |
| Employee Shift Sequences                           | cmd=staffshiftseq      |
| Timetable                                          | cmd=monthly_work_sched |
| Workplace                                          | cmd=assignedworkplaces |
| Holiday Work (Lottery And Assignment)              | cmd=laaholidaywork     |
| Minimum Occupance By Sites                         | cmd=deskminstaffing    |
| Work Place Occupancy                               | cmd=deskalloc          |
| Validity Of Master Data                            | cmd=masterdatavalidity |
| Coach/Trainee - Scheduling Difference              | cmd=coach_trainee      |
| Master Data Overview                               | cmd=employeemasterdata |
| Group Authorization                                | cmd=group_auth         |
| Modifying Master Data                              | cmd=audit              |
