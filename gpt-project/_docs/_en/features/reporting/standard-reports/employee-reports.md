---
title: Employee reports
product_label:
  - advanced
  - enterprise
  - classic
promote-service: enhanced-reporting
description: Learn about the standard reports available at an employee level.
---

injixo offers a whole range of reports for employees, which are listed individually below.

## Employee work schedules

Employee Work Schedules can be used to create work schedules and be sent to your employees.
They show the daily working time of the employees and their paid and unpaid activities and shifts.

- **Employee Work Schedule I (List)**  
   All activity types except `Illness` and all shifts. Displays only days with scheduling data.

- **Employee Work Schedule I (List) (without Breaks)**  
   All activity types except `Break` and `Illness` and all shifts. Displays only days with scheduling data.

- **Employee Work Schedule II (List)**  
   All activity types and all shifts. Displays also days without scheduling data.

- **Employee Work Schedule III (Graph)**
  Diagram version of the schedule with colored bars in a time scale per day. All activity types and shifts.

- **Employee Work Schedule IV (6 Weeks)**  
   Displays all activity types and shifts and the working hours per day. Shows individual activities of shifts but not the name of the shift.

- **Employee Work Schedule IV (6 weeks) (Activities)**  
   In contrast to the previous report, the last 4 weeks of the report period (report weeks 3 to 6) contain all concrete activities of the type `Presence`, and only as many weeks are displayed as are selected in the report period (up to a maximum of 6 weeks).

- **Employee Work Schedule (6 weeks) (no Breaks)**  
   Uses all activity types except `Break` and shows the shifts and the daily working time.

## Hours worked per employee

- **Hours Worked per Employee I**  
   Target work time, actual time worked and the difference in hours and the percentage of the target work time that has been worked.

- **Hours Worked per Employee II**  
   Adjusted target working hours, the actual working hours and the difference in hours and in percent. The report does not contain monthly values. <!-- Anpassungszeiträume are used --> The annual working time is determined from the working times defined in the contract.
    <!-- This annual working time is then distributed to the planning periods by the function for adjustment periods as target time. However, these planning periods have different weightings so that there is no distribution 'x/52'.  -->
    <!-- If these planning periods are in the past and you have already worked with them, the corresponding columns in the report are filled. --> If the planning periods are still in the future, only the adjusted target time is displayed.

## Other reports

- **Modifying Master Data**  
  This report logs users' additions, updates, and deletions to selected configuration data. It provides a comprehensive overview of the changes made to the users' data (e.g., name, address, email, date of birth, ID) within the specified timeframe. The data is automatically removed after 90 days.

- **Master Data Overview**  
   All of your users' available data.

- **Group Authorization**  
   Access rights to navigator with features, menu items and scheduling actions per selected user group.

- **Employee Request Schedule II (List)**  
   Shift and vacation requests (activities and working times) from the _Request_, _Alternative Request_, and _Vacation Request/Absence Request_ levels. <!-- The duration between the start and end time of the workday and for the entire selected period is specified. -->

- **Holiday Work (Lottery and Assignment)**  
   All Activities of the type `Presence` and `Break` and all shifts with these activities that are assigned to employees by lottery and assignment on public holidays and for which shift requests exist. Data originates from the `Request` and `Alternative Request` levels.

- **Fluctuation I**  
   Shows changes in the workforce in chronological order. All employee arrivals and departures are totalled and displayed as percentages. <!-- Employees of one, several or all Planning Units are displayed. A separate page is created for each Planning Unit. -->

- **Fluctuation II**  
   Join and leave dates, the number of days in the company, the selection and the contract for each employee who left the company.

- **Organizational Chart**  
   Employees in a Planning Unit with their skills, resulting activities, assigned contracts and the their selections.

- **Anniversaries**  
   All birthdays and anniversaries of the employees. <!-- In addition, the employees whose probationary period has expired are specified. A separate table is created for each Planning Unit, whose entries are sorted by date within the anniversaries. -->

- **Staff by Contract Type**  
   Number of employees per contract type and the resulting number of working days and hours for the selected planning unit and time period. The total row shows the total values for each column.

- **Staff Shift Sequences**  
   Selection-based report. Assigned Shift Sequences per employee.

- **Employee Absence Schedule with Day Status and Full-Day Activities**  
   Day statuses and full-day activities from the Absence Planner per employee and year.
