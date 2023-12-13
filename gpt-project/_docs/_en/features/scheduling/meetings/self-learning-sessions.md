---
title: Schedule self-learning sessions
product_label:
  - advanced
  - enterprise
toc: false
description: Generate time slot suggestions for self-learning sessions that minimize the impact on the coverage of your other activities (Meetings feature).
---

In this article, you will learn how to generate time slot suggestions for self-learning sessions in order to schedule meetings with a minimized impact on the coverage of other existing activities in your schedule.

New to Meetings? Learn {% link_new the basics | features/scheduling/meetings/meetings-overview.md %} first.

## Generate suggestions for self-learning sessions

Self-learning sessions are meetings for single employees without a meeting host.

1. Go to _Plan > Meetings_{:.breadcrumbs}.
2. Click _Set up_{:.doc-button} in the _Self-learning sessions_ card at the top of the page.
3. In the _Settings_ section, select the **Planning unit** for which you want to schedule self-learning sessions. Select an entry from the list, or start typing the planning unit's name to filter the list. After selecting a planning unit, a hint box appears that tells you how many _Presence_ activities in the planning unit are not configured as _Replaceable_.
4. For **Activity to schedule**, select the self-learning session activity you want to schedule. Self-learning sessions are considered as _meetings_ in injixo. Therefore, you now see a list that contains all activities of type _Meeting_ which have been assigned to the planning unit. Select an entry from the list, or start typing the activity's name to filter the list. If you haven't {% link_new created a meeting activity | features/administration/activities.md %} for the self-learning session yet, do it now.
5. Select the **Date range** in which you want to schedule the self-learning sessions. By default, the date range is set to the next working week (Monday - Sunday) following the current date.
6. Set a **Session duration** in minutes. The default value is 60 minutes.
7. Define with **Sessions per participant** how many sessions you want to schedule for each participant.

   {{ 1 | image: 'Settings', '60%' }}

8. In the _Optional settings_ section, Check the checkbox **Limit the number of sessions per day for each participant to maximum** if you want to limit the number of self-learning sessions per day for each participant. Then, enter the maximum **number** of sessions per day below.
9. Check the checkbox **Ensure a buffer between sessions for each participant** if you want to make sure that there is a defined minimum time buffer between self-learning sessions for each participant. Then, choose an appropriate **value** from the drop-down menu below.

   {{ 3 | image: 'Settings', '60%' }}

10. In the _Participants_ section, you define the list of participants for whom self-learning sessions will be scheduled:

    - (Optional) Choose the option {% link_new **selection** | features/administration/selections.md %} or **employee filter** using the buttons on top. Select an item from the corresponding drop-down menu on the right to filter the list of all employees.
    - Check the **checkbox** to the left of a participant to select them. Check the checkbox at the top of the list to (de)select all participants at once.

    {{ 2 | image: 'Participants', '60%' }}

11. To start the generation of time slots for the self-learning sessions, click _Generate suggestions_{:.doc-button} at the bottom of the page. This takes you back to the overview page.

After the time slot suggestions have been generated, you have to {% link_new schedule them | features/scheduling/meetings/scheduling-suggestions.md %}.
