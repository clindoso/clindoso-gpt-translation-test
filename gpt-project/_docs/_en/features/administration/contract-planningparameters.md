---
title: Configure scheduling parameters
product_label:
  - advanced
  - enterprise
  - classic
description: Learn what the different scheduling rules in contracts are used for.
toc: false
---

With scheduling rules, you can define criteria that are considered when inserting shifts or activities. A validity check is performed when the corresponding Scheduling Rule is activated.

## Work duration and frequency

**2621 Maximum Number of Saturdays Worked per Month**  
Specify the number of Saturdays per month (0 - 5) on which an Employee can work.

**2622 Maximum Number of Sundays Worked per Month**  
Specify the number of Sundays per month (0 - 5) on which an Employee can work. This value is respected by Scheduling Rules _2622_{:.id-label} and _2643_{:.id-label}.

**2617 Minimum Number of Net Working Hours per Day (Day Models only)**  
Enter the minimum shift duration. This value is respected by scheduling rules _2615_{:.id-label} and _2617_{:.id-label}.

**2616 Maximum Number of Net Working Hours per Day (Day Models only)**  
Enter the maximum shift duration. The net time is the duration of all paid activities of a shift. An employee is only assigned shifts that do not exceed or fall short of the specified net times. This value is respected by the scheduling rules _2614_{:.id-label} and _2616_{:.id-label}.

**2601 Rest Period Between Two Working Days**  
Enter a value for the rest period between the end of the last shift of one working day and the start of the first shift of the following working day.

**2602 Maximum Duration of an Activity**  
Specify a value for the maximum duration of an activity. Full-day activities are **not** checked by this scheduling rule.

Activate the appropriate option within the rule if you want to exclude the check for `Illness` and/or `Vacation` activities in general, for absences check Scheduling Rule _2641_{:.id-label}.

**2613 Maximum Number of Shifts per Day**  
Specify a value for the maximum number of shifts to allow per day.

**2614 Maximum Number of Working Hours per Day (Day Models and Activities)**  
Check one or both checkboxes if the sum of working time from day models and/or activities per day must not exceed the maximum value.

**2623 Maximum Number of Working Days per Week**  
Specify a value for the maximum number of working days per week.

**2624 Maximum Number of Successive Working Days**  
Specify a value for the maximum number of consecutive working days across weeks.

Using the corresponding checkboxes you can exclude the check for paid activities of the type `illness` and/or `holiday`.

**2625 Minimum Number of Successive Days Off per Week**  
Specify a value for the minimum number of consecutive days off per week.

**2626 Maximum Number of Working Hours within 24 Hours**  
Specify a value for the maximum working time from day models and activities within 24 hours.

**2632 Maximum Number of Booking Days with Night Work per Week**  
Specify a value for the maximum number of booking days with night work per week.

**2633 Maximum Number of Booking Days with Night Work per Month**  
Specify a value for the maximum number of booking days with night work per month.

**2634 Maximum Number of Successive Booking Days with Night Work**  
Enter a value for the maximum number of consecutive booking days with night work.

**2659 Maximum Number of Day Models Placed within 24-Hour Period**  
Specify the maximum number of day models (1 - 100) that may start within 24 hours.

injixo checks this for a period of 24 hours before and after each shift starts. The scheduling rule can be used to adhere to a 24-hour period between the start of the shift on the first day and the start of the shift on the following day. If you enter the value 1, an employee with a shift at 20:00 does not receive the next shift until 20:00 of the following day.

**2662 Maximum Permitted Deviation of Working Time from Target Work Account per Planning Period**  
Enter a value for the maximum variance (00:00 - 999:59) that is allowed if the total working time exceeds the working time allowed in the Target Work Account.

## Rest and breaks

**2603 Minimum Time Gap between two Activities on the Same Day**  
Specify a value for the minimum distance between two activities on the same day. The value is only taken into account if activities do not directly follow each other and a distance is entered in the `Shift Center`.

**2604 Maximum Time Gap between two Activities on the Same Day**  
Specify a value for the maximum distance between two activities on the same day.

**2639 Weekly Continuous Rest Period without Guarantee of any Full Day**  
Specify a value for the continuous weekly rest period. If the rest period is less than 48 hours, it is possible that the rest period is spread over two days so that no whole calendar day is included in the rest period.

**2640 Weekly Continuous Rest Period with Guarantee of one Full Day**  
Specify a value for the continuous weekly rest period. For rest periods between 24 and 48 hours, the rest period is always granted in such a way that at least one whole calendar day is included in the rest period.

**2646 Rest Period after Work Done on Holidays without Guarantee of any Full Day**  
Enter a value for the rest period after holiday work. If the rest period is less than 48 hours, it is possible for the rest period to be spread over two days so that the rest period does not include an entire calendar day.

**2647 Rest Period after Work Done on Holidays with Guarantee of one Full Day**  
Enter a value for the rest period after holiday work. The rest period is always granted so that at least one whole calendar day is included in the rest period.

For Scheduling Rules _2646_{:.id-label} and _2647_{:.id-label} the system checks public holidays in the planning unit that are assigned to the employee with the highest priority and for which the 'Public holiday mode' checkbox is checked in the menu option _Day types_{:.menu-item}.

If the rule is activated, an employee must be granted the rest period specified in the contract after each holiday on which he/she executes a shift or activity for which the checkbox "Respect rest period" has been activated in the `Administration` menu item _Activities_{:.menu-item}. Full-day activities are **not** checked by this rule and may violate the rest period.

## Weekends and holidays

**2620 Minimum Number of Weekends off per Month**  
If this rule is activated, an employee must be assigned as many free weekends as specified in the Contract.
The weekends defined in the settings _48421_{:.id-label} and _48449_{:.id-label} are regarded as weekends.

**2627 Minimum Number of Days Off per Week Due to Work Done on a Saturday**  
Specify the minimum number of days off per scheduling week that an employee is to be granted in the following week between Monday and Friday if the employee worked on the Saturday of the previous week or is already scheduled for a shift.

**2628 Minimum Number of Days Off per Week due to Work Done on a Sunday**  
Specify the minimum number of days off per scheduling week that an employee is to be granted in the following week between Monday and Friday if he or she worked on the Sunday of the previous week or is already scheduled for a shift.

The scheduling rules 2627 and 2628 ensure that an employee with this contract who works on a Saturday or Sunday receives the specified number of days off between Monday and Friday. However, they can be assigned another shift on Saturday or Sunday of the current week.

**2631 No Assignments on Holidays (Day Models and Activities)**  
Check the checkbox if the assignment of day models and activities on public holidays should be prevented. The assignment is checked for public holidays in the planning calendar of the planning unit that is assigned to the employee with the highest priority and for which the 'Public holiday mode' checkbox is checked in the menu option _Day types_{:.menu-item}.

**2643 Maximum Number of Scheduled Sundays and Holidays per Month**  
Enter a value for the maximum number of scheduled Sundays and public holidays. Enter the value 3 for an employee who is allowed to work on 2 Sundays per month according to the contract and who is also allowed to work on a public holiday.

**2649 Maximum Number of Successive Sundays Scheduled for Work (across Months)**  
Specify the maximum number of consecutive Sundays on which an employee may work with this contract.

**2650 Maximum Number of Successive Weekends Scheduled for Work (across Months)**  
Specify the maximum number of consecutive weekends on which an employee may work with this contract. The days specified in the settings for configuring the scheduling week are regarded as weekends.

## Special conditions

**2629 Threshold Value for Excess Working Hours in Successive Weeks (Day Models and Activities)**  
Specify a threshold value per week. The default value (168) indicates the time available per week.

The week is the scheduling week configured in the settings. Enter the number of consecutive weeks in which the threshold value may be exceeded in the `Number of weeks` field. An employee can only be assigned as many day models and activities as the number of consecutive weeks in which the threshold value defined in the contract for exceeding the working time per week is exceeded. If, for example, a threshold value of 40 hours per week for three consecutive weeks is defined for a contract, then there must not be four consecutive weeks in which an employee with this contract works more than 40 hours per week. The employee is then allowed to work more than 40 hours per week for a maximum of three consecutive weeks. The check by rule _2629_{:.id-label} _Threshold value for exceeding the working time in consecutive weeks according to the contract (day models and activities)_ to prevent employees from working overtime for an unlimited number of weeks. In this case, the threshold value corresponds to the target per week specified in the contract.

**2641 Maximum Duration for Activities, Exempting Activities of Type 'Absence'**  
Specify a value for the maximum duration of an activity without checking the activity type 'Absence'.

For activities of type `illness` and/or `vacation`, check Scheduling Rule _2641_{:.id-label}.