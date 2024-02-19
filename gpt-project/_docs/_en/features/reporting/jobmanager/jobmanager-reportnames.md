---
title: Report names and parameters
product_label:
  - enterprise
description: Learn about the different *cmd* parameters which are needed to generate reports automatically using the JobManager.
---

To create the reports available in the user interface with JobManager, you must configure the **cmd** parameter.

Example: `cmd=shiftplan`

Some reports allow you to change the report output by adding additional text:

- showconsel=1 (Show Contracts And Selections)
- hidefda=1 (Hide Full Day Activities)
- showbreaks=1 (Show Breaks)

Example: `cmd=shiftplan showconsel=1`

The tables below display all the required value for reports that are available under _WFM > Monitoring > Reports_{:.breadcrumbs}.

## Weekly schedule reports

<style>
table {
  width: 100%;
}

table th:first-of-type {
    width: 50%;
}
table th:nth-of-type(2) {
    width: 50%;
}
</style>

| Report name                                                    | Value for the **cmd** parameter     |
| -------------------------------------------------------------- | ----------------------------------- |
| Weekly Schedule I                                              | shiftplan                           |
| Weekly Schedule I with Filter                                  | shiftplan showconsel=1              |
| Weekly Schedule I (without Full-Day Activities)                | shiftplansel hidefda=1              |
| Weekly Schedule II (without Full-Day Activities)               | shiftplansel showbreaks=1 hidefda=1 |
| Weekly Schedule II (without Breaks)                            | shiftplansel                        |
| Weekly Schedule (without Breaks) (without Full-Day Activities) | shiftplansel hidefda=1              |
| Weekly Schedule III                                            | weeklyworkplan                      |
| Weekly Schedule III (without Full-Day Activities)              | weeklyworkplan hidefda=1            |

## Daily schedule reports

| Report name                                                 | Value for the **cmd** parameter |
| ----------------------------------------------------------- | ------------------------------- |
| Daily Schedule I                                            | staffworkpubar                  |
| Daily Schedule I with Breaks                                | staffworkpubarbreaks            |
| Daily Schedule I (without absences, illnesses and vacation) | staffworkpubarabsences          |
| Daily Schedule II                                           | staffworktimebar                |
| Daily Schedule II with Breaks                               | staffworktimebarbreaks          |
| Daily Schedule II with Shift Summary                        | staffworktimebartotal           |
| Daily Schedule II with Shift Summary and Breaks             | staffworktimebartotalbreaks     |
| Daily Schedule III                                          | staffworkactbar                 |
| Daily Schedule III with Breaks                              | staffworkactbarbreaks           |
| Daily Schedule IV                                           | staffworkpubarsel               |
| Daily Schedule V                                            | staffworktimebarsel             |
| Daily Schedule VI                                           | staffworkactbarsel              |

## Vacation and absence schedule

| Report name                                              | Value for the **cmd** parameter |
| -------------------------------------------------------- | ------------------------------- |
| Absence Schedule                                         | absence                         |
| General Absence Schedule                                 | realabsence                     |
| Absence Schedule with Day Status and Full-Day Activities | orgabscalendar                  |
| Vacation Schedule I                                      | holiday                         |
| Vacation Schedule I with Full-Time-Equivalent            | vacation_fte                    |
| Vacation Schedule II                                     | vacationwithunpaid              |

## Absence, illness- and vacation statistics

| Report name                                   | Value for the **cmd** parameter |
| --------------------------------------------- | ------------------------------- |
| Absence Statistics                            | absence_c                       |
| Absence Statistics with Total Amount Column   | absence_t                       |
| Absence Statistics with Full-Time-Equivalent  | absence_fte                     |
| Vacation Statistics                           | holiday_c                       |
| Vacation Statistics with Total Amount Column  | holiday_t                       |
| Vacation Statistics with Full-Time-Equivalent | holiday_fte                     |
| Illness Statistics                            | illness_c                       |
| Illness Statistics with Total Amount Column   | illness_t                       |
| Illness Statistics with Full-Time-Equivalent  | illness_fte                     |

## Work time reports

| Report name                         | Value for the **cmd** parameter |
| ----------------------------------- | ------------------------------- |
| Time Worked Times per Planning Unit | diff_pu                         |
| Activities in Hours                 | activ_st                        |
| Activities in Percent               | activ_per                       |
| Activity Statistics                 | activity_stat                   |
| Net Working Times                   | realized_hours                  |
| Activity Analysis                   | state_train                     |

## Break schedules

| Report name        | Value for the **cmd** parameter |
| ------------------ | ------------------------------- |
| Break Schedule I   | pause                           |
| Break Schedule II  | pausetwo                        |
| Break Schedule III | pausethree                      |

## Other reports

| Report name                                    | Value for the **cmd** parameter |
| ---------------------------------------------- | ------------------------------- |
| Difference in Working Times Between Levels     | worktimes                       |
| Time Accounts Report                           | timeacount                      |
| Shifts with Requirement                        | genshifts                       |
| Days With Night, Weekend und Holiday Schedules | shifttype                       |
| Capacities According To Contract Type          | capacity                        |
| Training Models                                | train_camp_summary              |
| Minimum Staffing                               | minimalcoverage                 |
| Scheduling Rules Configuration                 | schedulingrules                 |
| Vacation Overview                              | vacationoverview                |
| Shift Overview                                 | monthlyshiftplan                |
| Yearly Working Time Analysis                   | work_time_analysis              |
| Conformance Report                             | conformance                     |
| Adherence Report                               | adherence                       |

## Exchange reports

| Report name         | Value for the **cmd** parameter |
| ------------------- | ------------------------------- |
| Exchanges I         | shiftexchdetails                |
| Exchanges II        | shiftexchnodetails              |
| Exchange Statistics | shiftexchstats                  |

## Employee work schedules

| Report name                                         | Value for the **cmd** parameter |
| --------------------------------------------------- | ------------------------------- |
| Employee Work Schedule I (List)                     | staffwork showbreaks=1          |
| Employee Work Schedule I (List) (without Breaks)    | staffwork                       |
| Employee Work Schedule II (List)                    | staffworkabsill                 |
| Employee Work Schedule III (Graph)                  | staffworkbar                    |
| Employee Work Schedule IV (6 Week)                  | staffsixweeksnobreaks           |
| Employee Work Schedule IV (6 Week) (Activities)     | staffsixweeks                   |
| Employee Work Schedule IV (6 Week) (without Breaks) | staffsixweekstwo                |

## Other employee reports

| Report name                                        | Value for the **cmd** parameter |
| -------------------------------------------------- | ------------------------------- |
| Employee Request Schedule I (List)                 | staff_wish                      |
| Working Times per Employee I                       | diff_st                         |
| Working Times per Employee II                      | diff_st_two                     |
| Montly Employees' Journal                          | journal                         |
| Organisational Chart                               | organ                           |
| Weekend Working Hours I                            | weekendwork                     |
| Weekend Working Hours II                           | weekendwork2                    |
| Weekend Working Hours III (Lottery and Assignment) | weekendwork3                    |
| Anniversaries                                      | jubilee                         |
| Vacation Slip                                      | hd_list                         |
| Employees per Contract Type                        | read                            |
| Fluctuation I                                      | fluct                           |
| Fluctuation II                                     | detailfluctuation               |
| Yearly Overview                                    | absencejob_cal                  |
| Compensation Days for Weekend Work                 | comp_week_work                  |
| Employee Shift Sequences                           | staffshiftseq                   |
| Timetable                                          | monthly_work_sched              |
| Workplace                                          | assignedworkplaces              |
| Holiday Work (Lottery And Assignment)              | laaholidaywork                  |
| Minimum Occupance By Sites                         | deskminstaffing                 |
| Work Place Occupancy                               | deskalloc                       |
| Validity Of Master Data                            | masterdatavalidity              |
| Coach/Trainee - Scheduling Difference              | coach_trainee                   |
| Master Data Overview                               | employeemasterdata              |
| Group Authorization                                | group_auth                      |
| Modifying Master Data                              | audit                           |
