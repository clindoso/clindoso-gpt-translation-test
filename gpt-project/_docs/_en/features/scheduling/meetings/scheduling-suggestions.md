---
title: Review and apply meeting suggestions
product_label:
  - advanced
  - enterprise
description: Review meeting suggestions and write them into the schedule.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/meetings/meetings-overview.md
---

In this article, you will learn how to:

- check if the process to generate meeting suggestions was successful.
- review the meeting time slot suggestions and apply them to your schedule.
- review the scheduling results.

New to Meetings? Learn {% link_new the basics | features/scheduling/meetings/meetings-overview.md %} first.

## Wait for the process to finish

When you start the process to {% link_new generate meeting slot suggestions | features/scheduling/meetings/meetings-overview.md | #generate-suggestions-for-meeting-time-slots %}, an entry appears in the _Generated suggestions_ table. It shows when the process has been initiated, the meeting type, and the selected planning unit.

Wait until the process has finished. This can take some time, depending on the chosen time period.

## Check if the process was successful

After the meeting suggestions generation process has finished, the _Actions_ column shows one of these texts:

- _View suggestions_: The process finished successfully.
- _View Conflict_: The process could not be finished due to conflicts with the existing schedule. Clicking the text will show the details.
- _Not possible_: The process could not be finished as the selected meeting host could not be scheduled (appears only for 1:1 or group meetings with a host).

The column _Participant status_ shows for how many participants it was possible to generate meeting time slots and for how many this was not possible, for example: _4 available, 2 not available_. After you click the link _View suggestions_, the _Suggestions_ page will explain why some employees may not have been assigned a meeting slot.

## Review and apply the suggestions

If the process has successfully generated suggestions, you can review and apply them:

1. In the _Generated suggestions_ section, click _View suggestions_{:.doc-button} in the respective row in the **Actions** column. This will bring you to the _Suggestions_ page.

   {{ 5 | image: 'Generated suggestions - view suggestions link' }}

2. On the suggestions page, you can see a table with the following information:

   - _Suggested time slot_: the suggested time slot for the meeting
   - _Activity to schedule_: the meeting that will be scheduled
   - _Participant_: the name of the employee who will take part in the meeting
   - _Replaced activity_: the activity that will be replaced by the meeting
   - _Resulting coverage_: how the scheduled meeting would affect the coverage of the replaced activity; if you hover your mouse over the coverage values, a popover with detailed information appears

   Note: The coverage values are calculated during the suggestion generation process. Subsequent changes to the schedule will not change the coverage values displayed here.

   The table also shows employees without any suggestions. They are most likely on vacation or sick leave in the selected period.

   {{ 2 | image: 'Suggestions - Group meetings' }}

3. To exclude employees from getting meetings, uncheck the **checkboxes** on the left (optional). The checkbox on top deselects all employees at once. Deselected employees will appear on the results page as _Excluded_.

4. Click _Schedule meetings_{:.doc-button} to write the meetings into the schedule. For self-learning sessions, the button is called _Schedule sessions_{:.doc-button}. Click _Back to overview_{:.doc-button} if you want to leave the _Suggestions_ page without writing suggestions to the schedule.

## Review the scheduling results

It can take some time to write the selected suggestions into the schedule. Afterwards, you can click the link **View schedule** to check the new meeting slots in the schedule. In the _Generated suggestions_ section on the overview page, the participant status for the respective entry has changed. It now shows for how many participants meetings have been scheduled.

You can now review the detailed scheduling results:

1. In the _Generated suggestions_ section, click the link **View results** in the respective row. The results page shows the tabs _Scheduled_, _Failed_, and _Excluded_. Depending on whether the process could create scheduling suggestions for employees and you accepted them or not, you will find your employees in the respective categories. Inactive tabs mean no employees in this category.
2. Click one of the **tabs** to see the details.

   {{ 4 | image: 'Results - Group meetings' }}

You can either ignore any employees in the _Failed_ and _Excluded_ categories or start a new meeting scheduling process with different parameters to try to schedule them as well. You can also manually add meetings for these employees under _Plan > Schedules_{:.breadcrumbs} or _Plan > Shift Center_{:.breadcrumbs}.
