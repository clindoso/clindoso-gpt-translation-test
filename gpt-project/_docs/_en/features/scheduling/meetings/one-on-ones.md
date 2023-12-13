---
title: Schedule 1:1 meetings
product_label:
  - advanced
  - enterprise
toc: false
description: Generate time slot suggestions for one-on-one meetings that minimize the impact on the coverage of your other activities (Meetings feature).
---

In this article, you will learn how to generate time slot suggestions for one-on-one meetings with a minimized impact on the coverage of other existing activities in your schedule.

New to Meetings? Learn {% link_new the basics | features/scheduling/meetings/meetings-overview.md %} first.

## Generate suggestions for 1:1 meetings

1:1 meetings are meetings between an employee and a meeting host, typically a team leader.

1. Go to _Plan > Meetings_{:.breadcrumbs}.
2. Click _Set up_{:.doc-button} in the _1:1 meetings_ card at the top of the page.
3. In the _Settings_ section, select the **Planning unit** for which you want to schedule 1:1 meetings. Select an entry from the list, or start typing the planning unit's name to filter the list. After selecting a planning unit, a hint box appears that tells you how many _Presence_ activities in the planning unit are not configured as _Replaceable_.
4. For **Activity to schedule**, select the 1:1 meeting activity you want to schedule. The list contains all activities of type _Meeting_ which have been assigned to the planning unit. Select an entry from the list, or start typing the activity's name to filter the list. If you haven't {% link_new created a meeting activity | features/administration/activities.md %} yet, do it now.
5. Select the **Date range** in which you want to schedule meetings. By default, the date range is set to the next working week (Monday - Sunday) following the current date.
6. Set a **Meeting duration** in minutes. The default value is 60 minutes.
   {{ 1 | image: 'Settings section', '60%' }}

7. In the _Optional settings_ section, check the checkbox **Ensure a buffer between meetings** if you want to make sure that there is a defined minimum time buffer between meeting sessions for each participant. Choose an appropriate **value** from the drop-down menu below.
8. Check the checkbox **Limit the number of meetings per day to maximum** if you want to limit the number of meetings per day for each participant. Enter the maximum **number** of meetings per day below.
9. Check the checkbox **Consider only time slots for which the resulting coverage will be at least** if you want to make sure that the resulting coverage after the scheduling of the meetings does not fall below a predefined threshold. Enter a **coverage value**. Zero and negative values are also allowed as coverage can be negative.

   {{ 5 | image: 'Settings section', '60%' }}

10. In the _Meeting host_ section, you have two options to define when the host is available to host the meeting:

    - If the meeting host is not scheduled in injixo, select the **Enter manually** option. Then, define time ranges for one or more days:

      1. Enter values into the **Day**, **From**, and **To** fields.
      2. (Optional) To add another time span for the chosen day, click _+ Time span_{:.doc-button}. If time spans overlap, injixo uses the largest possible time span from the combination of several time spans. To remove a time span again, click the **X** next to it.
      3. If you want to add time spans for another day, click _Add day and time span_{:.doc-button}. To remove individual days, click _Remove day_{:.doc-button}. At least one day with one time span is required.

      {{ 2 | image: 'Enter host availability', '60%' }}

    - If the meeting host is scheduled in injixo, select the **Choose employee** option. injixo will retrieve the availability of the meeting host from the employee's schedule. When this option is selected, scheduled meetings will also be written to the schedule of the meeting host.

      1. Select a different **Planning unit** if the meeting host is part of another planning unit. Note: The planning units of both the meeting host and the participants must be set to the same interval.
      2. Select an **employee** to be the meeting host.

      {{ 3 | image: 'Choose employee as host', '70%' }}

11. In the _Participants_ section, you define the list of participants for whom meetings will be scheduled:

    - (Optional) Choose the option {% link_new **selection** | features/administration/selections.md %} or **employee filter** using the buttons on top. Click an item from the drop-down menu on the right to filter the list of employees.
    - Check the **checkbox** to the left of an employee to select them. Check the checkbox at the top of the list to (de)select all participants at once.

    {{ 4 | image: 'Participants', '60%' }}

12. To start the meeting generation process, click _Generate suggestions_{:.doc-button} at the bottom of the page. This takes you back to the overview page.

After the meeting suggestions have been generated, you have to {% link_new schedule them | features/scheduling/meetings/scheduling-suggestions.md %}.
