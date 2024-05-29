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

After you have generated meetings in the Meetings feature, injixo will show generated suggestions with different time slots for the meeting. You can apply the suggestions to your schedule and review the scheduling results.

New to Meetings? Learn {% link_new the basics | features/scheduling/meetings/meetings-overview.md %} first.

## Wait for the process to finish

When you {% link_new generate meeting suggestions | features/scheduling/meetings/meetings-overview.md | #generate-meeting-suggestions %}, injixo will create a new entry in the Generated suggestions section. Each table row shows the start time and the selected meeting type and planning unit.

## Check suggestions generation results

When suggestions have been generated, the Actions column will be updated and shows one of the following statuses:

- View suggestions: The process finished successfully.
- View Conflict: Conflicts with the existing schedule.
- Not possible: 1:1 or group meetings with a host could not be scheduled.

The Participant status column shows how many participants have been scheduled and how many are not available.

## Review and apply the suggestions

Review and apply generated suggestions as follows:

1. In the **Generated suggestions** section, click a **View suggestions** link.

   The Suggestions page opens and shows a table with the following columns:

   | Column               | Details                                                                                                                                                                       |
   | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Suggested time slot  | Suggested time slot for the meeting                                                                                                                                           |
   | Activity to schedule | Meeting activity that will be scheduled                                                                                                                                       |
   | Host/Participant     | Names of people who will be in the meeting                                                                                                                                    |
   | Replaced activity    | Scheduled activity that will be replaced by the meeting                                                                                                                       |
   | Resulting coverage   | Indicator of how the scheduled meeting would affect the coverage of the replaced activity. Hover your mouse over the coverage values for a popover with detailed information. |

   <!-- {{ 2 | image: 'Suggestions - Group meetings' }} -->

   > Notes
   >
   > - The coverage is calculated when suggestions are generated. Subsequent changes to the schedule will not change the displayed coverage.
   > - The table on the Suggestions page shows people without suggestions when they are on vacation or sick leave in the selected period.

2. (Optional) To exclude a person from getting meetings, uncheck the checkbox on the left. The checkbox on top deselects all people at once. Any deselected person will appear on the results page as Excluded.

3. To schedule the meetings, click _Schedule meetings_{:.doc-button} (or **Schedule sessions** for self-learning sessions). To leave the page without applying the suggestions, click _Back to overview_{:.doc-button} .

## Review the scheduling results

When meeting suggestions have been scheduled, the Generated suggestions section shows two links:

- **View schedule**: Allows you to review the new scheduled meetings in _Plan > Schedules_{:.breadcrumbs}.
- **View results**: Opens the results page with details about the suggested meetings on three tabs:

  | Tab       | Details                                                                                                                                                                                                  |
  | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Scheduled | People who got scheduled for a suggested meeting time slot.                                                                                                                                              |
  | Failed    | People who could not be scheduled. The Information column displays the reasons and scheduling rules that block placing the meeting. The tab may be inactive when everyone can be scheduled successfully. |
  | Excluded  | People who have been deselected before to exclude from scheduling. The tab can be inactive when no one was excluded.                                                                                     |

Review people listed in the Failed and Excluded tab. You can ignore or try to reschedule them by using different parameters. In _Plan > Schedules_{:.breadcrumbs} or _Plan > Shift Center_{:.breadcrumbs}, you can also manually add meetings.
