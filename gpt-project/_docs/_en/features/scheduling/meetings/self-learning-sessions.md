---
title: Schedule self-learning sessions
product_label:
  - advanced
  - enterprise
toc: false
description: Generate time slot suggestions for self-learning sessions that minimize the impact on the coverage of your other activities (Meetings feature).
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/meetings/meetings-overview.md
---

Generate time slot suggestions for self-learning sessions to schedule meetings with a minimized impact on the coverage of other existing activities in your schedule.

New to Meetings? Learn {% link_new the basics | features/scheduling/meetings/meetings-overview.md %} first.

## Generate suggestions for self-learning sessions

Self-learning sessions are meetings for a person without a meeting host.

1. Go to _Plan > Meetings_{:.breadcrumbs}.
2. In the **Self-learning sessions** card, click _Set up_{:.doc-button}.
3. In the **Settings** section, configure the parameters:

   - **Planning unit**: Select a planning unit for which you want to schedule self-learning sessions from the list, or start typing the planning unit's name to filter the list. A box displays how many Presence activities in the planning unit are not replaceable.
   - **Activity to schedule**: List of activities of the meeting type that are assigned to the planning unit. Select an activity from the list, or start typing to filter the list for the activity you want to schedule.
   - **Date range**: Period in which you want to schedule the self-learning sessions. By default, the date range is set to the next working week (Monday - Sunday) following the current date.
   - **Session duration**: Set a session duration in minutes. The default value is 60 minutes.
   - **Sessions per participant**: Define how many sessions you want to schedule for each participant.

   <!-- {{ 1 | image: 'Settings', '60%' }} -->

4. (Optional) To limit the number of self-learning sessions per day for each participant, check the checkbox **Limit the number of sessions per day for each participant to maximum** in the **Optional settings** section. Enter the maximum **number** of sessions per day.
5. (Optional) To take into account a minimum time buffer between self-learning sessions for each participant, check the checkbox **Ensure a buffer between sessions for each participant**. Select the value from the drop-down menu below.

   <!-- {{ 3 | image: 'Settings', '60%' }} -->

6. In the **Participants** section, select participants who will be scheduled for self-learning sessions:

   - (Optional) Choose the option {% link_new **selection** | features/administration/selections.md %} or **employee filter** using the buttons on top. Select an item from the corresponding drop-down menu on the right to filter the list of all people.
   - Check the **checkbox** to the left of a participant to select them. Check the checkbox at the top of the list to (de)select all participants at once.

   <!-- {{ 2 | image: 'Participants', '60%' }} -->

7. Click _Generate suggestions_{:.doc-button}.  
   This takes you back to the overview page.<br>
   Once created, {% link_new schedule the suggestions | features/scheduling/meetings/scheduling-suggestions.md %}.
