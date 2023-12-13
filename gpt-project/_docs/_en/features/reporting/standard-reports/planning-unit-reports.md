---
title: Planning unit reports
product_label:
  - advanced
  - enterprise
  - classic
description: Learn about the standard reports available at a planning unit level.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/intraday/adherence-intraday.md
---

injixo offers different planning unit reports.

> Empty reports or missing data?
> 
> Make sure that the activities you want to display are {% link_new assigned to the correct planning unit | features/administration/create-and-manage-planning-units.md | #add-activities %}. Some reports group data by selections. To display data properly in those "selection-based" reports, add at least {% link_new one selection to each employee | features/administration/selections.md | #assign-people-to-selections %}.

## Frequently used reports

The following reports are widely used:

- **Activities in Hours**  
   Hourly values for paid working time for your employees. Select activities to display the hourly shares (total and individual).
- **Activities in Percent**  
   Hourly values for the paid working time of employees from all activities, the total working time and details of the percentage shares of the selected Activities in these.
- **Time Worked per planning unit**  
   Target work time, the actual worked time, the difference between the two in hours and the percentage of the target work time that has been worked.
- **Exchange Statistics**  
   Processing status of the exchanges (offered, not edited, rejected and exchanged requests).

## Weekly schedules

The following reports provide a weekly overview of assigned paid and unpaid activities, shifts, and the resulting weekly working times:

- **Weekly Schedule I** Sorted by planning unit and employee names.
- **Weekly Schedule I with Filter** Same as Weekly Schedule I, but with additional filter options.
- **Weekly Schedule I (without Full-Day Activities)**
  
- **Weekly Schedule II** As above but selection-based version, sorted by selection name.
- **Weekly Schedule II (without Full-Day Activities)**
- **Weekly Schedule II (without Breaks)**
- **Weekly Schedule II (without Breaks or Full-Day Activities)**

- **Weekly Schedule III** Selection-based report version. Sorted by employee names.
- **Weekly Schedule III (without Full-Day Activities)**

## Daily schedules

Daily reports include information about paid and unpaid activities and shifts, the resulting daily working time, and the start and end times of the working day:

- **Daily Schedule I** Sorted by employee names.
- **Daily Schedule I with Breaks** Same as Daily Schedule I, but with an additional column for break times.
- **Daily Schedule I (without Absences, Illnesses or Vacations)**

- **Daily Schedule II** Sorted by start times.
- **Daily Schedule II with Breaks**
- **Daily Schedule II with Shift Summary**
- **Daily Schedule II with Shift Summary and Breaks**

- **Daily Schedule III** Sorted by activity names.
- **Daily Schedule III with Breaks** Extra column with the break times

- **Daily Schedule IV** Selection-based. Sorted by employee names.
- **Daily Schedule V** Selection-based. Sorted by start times.
- **Daily Schedule VI** Selection-based. Sorted by activity names.

## Absence, vacation, and break schedules

Monthly reports about paid and unpaid non-presence activities. The report name shows which activity type is considered, e.g. Absence Statistics only uses activity of type _Absences_.

- **General Absence Schedule**  
   Activity types _Absence_, _Vacation_, _Illness_ and _Meeting_.
- **Absence Schedule**  
   Only activities of type _Absence_

- **Absence Schedule with Day Status and Full-Day Activities**  
   Displays the day statuses and full-day Activities from the absence planner.

- **Vacation Schedule I**  
   Total number of approved vacation days, the total and remaining vacation entitlement. Only paid activities.
- **Vacation Schedule I with Full-Time Equivalent**  
   Same as Vacation Schedule I, but standardized for a full-time employee.
- **Vacation Schedule II**  
   Total number of approved vacation days showing paid and unpaid activities.

- **Break Schedule I**  
   Daily overview of all break times, individually and in total. One line per employee with start and end time and all breaks.

- **Break Schedule II**  
   Chronologically ordered overview of all breaks. If an Employee has several breaks on the same day, he or she is also listed several times. Selection-based report.

- **Break Schedule III**
  All breaks in the form of a list for each day. Selection-based report.

## Monthly statistics reports

Additional monthly reports can provide information regarding the number of activities like absences, vacation, illness, and breaks in your schedule. These reports consider both paid and unpaid activities. The report name indicates which activity type is included, e.g. Absence Statistics only uses the activity type _Absence_.

- **Activity Statistics**  
   Selection-based report. Number and duration of activities per staff, plus the weekly total values overall. Daily overview for each selection of a planning unit, sorted by activities.

- **Absence Statistics**  
   Total of all absences assigned to each Employee in hours and days for each absence.
- **Absence Statistics with Total Amount Column**  
   As above plus the sum of absent employees.
- **Absence Statistics with Full-Time Equivalent**  
   As above, standardized to a full-time employee.

- **Vacation Statistics**
  Sum of all holidays per employee in hours and days for all activities of type _Vacation_.

- **Vacation Statistics with Total Amount Column**  
   Sum of all holidays per employee in hours and days, both overall and per vacation.
- **Vacation Statistics with Full-Time Equivalent**  
   As above, standardized to a full-time employee.

- **Illness Statistics**  
   Total of all assigned illnesses of each Employee in hours and days, both overall and per illness activity.
- **Illness Statistics with Total Amount Column**  
   As above plus a line showing the sum of sick employees.

## Other reports

Some more reports offering different information depending on the use cases:

- **Activity Analysis**  
   Hourly values for the total employee work time from all activities, the total number of hours for the selected activities, the weekly overrun or underrun in relationship to the control value, and the individual number of hours per activity.

- **Difference in Working Times Between Levels**  
   Weekly overview of the working times as well as their difference per day and Employee for two different levels. In addition to the selected level from the parameter area, you can select a second level in the dialog.

- **Shifts with a Requirement**  
   Shifts created with staff requirements.

- **Capacities According to Contract Type**  
   Gross and net capacity of employees for selected contracts.

- **Scheduling Rules Configuration**  
   Scheduling rule settings valid for every user.

- **Yearly Working Hours Analysis**  
   Selection-based overview containing scheduled working hours of the employees in relation to their target working hours according to their contract.

- **Vacation Overview**  
   Paid and unpaid activities of type _Vacation_, including the ones on weekends and holidays.<!-- , for a maximum of four vacation planning periods.  --><!-- test and reintroduce with time-off periods -->Sorted by activity names.

- **Shift Overview**  
   Selection-based report. Overview of personnel deployment sorted by personnel number. Monthly overview about assigned shifts and all assigned paid and unpaid activities. injixo evaluates and indicates whether the shifts are early, middle, late or night shifts, using activities and shift containing an activity of type _Present_. The report shows number of individual shift types and total number of shifts per day at the end.

## Adherence and conformance

injixo offers a detailed report including adherence and conformance data. {% link_new Learn more about the Adherence report | features/intraday/adherence-intraday.md | #adherence-report-csv-file %}.
