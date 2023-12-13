---
title: Schedule group meetings
product_label:
  - advanced
  - enterprise
description: Create and schedule time slot suggestions for group meetings that impact the coverage of your other activities as little as possible (Meetings feature).
toc: false
---

In this article, you will learn how to generate time slot suggestions for group meetings in order to schedule meetings with a minimized impact on the coverage of other existing activities in your schedule.

New to Meetings? Learn {% link_new the basics | features/scheduling/meetings/meetings-overview.md %} first.

## Generate suggestions for group meetings

Group meetings normally take place between a meeting host (typically the team leader) and a group of participants. A meeting host is however not mandatory.

1. Go to _Plan > Meetings_{:.breadcrumbs}.
2. Click _Set up_{:.doc-button} on the _Group meetings_ card at the top of the page.
3. In the _Settings_ section, select the **Planning unit** for which you want to schedule group meetings. Select an entry from the list, or start typing the planning unit's name to filter the list first. After selecting a planning unit, a hint box appears that tells you how many _Presence_ activities in the selected planning unit are not configured as _Replaceable_.
4. Select the **Activity to schedule** the group meeting activity you want to schedule. The list contains all activities of type _Meeting_ which have been assigned to the planning unit. Select an entry from the list, or start typing the activity's name to filter the list first. If you haven't {% link_new created a meeting activity | features/administration/activities.md %} yet, do it now.
5. Select the **Date range** in which you want to schedule meetings. By default, the date range is set to the next working week (Monday - Sunday) following the current date.
6. Set a **Meeting duration**. The default value is 60 minutes.
7. Activate the setting **Set additional availability constraint** if you want to define specific time frames when the meetings should take place.
   1. Choose a **Day**. Then, change the start and end time with the **From** and **To** fields if necessary.
   2. (Optional) Click **+ Time span** to add another time span to the day. To add a time span on another day, click _Add day and time span_{:.doc-button}. To remove individual days, click **Remove day**.
      {{ 1 | image: 'Details', '60%' }}
8. In the _Host_ section, you can choose between three options:

- - **No host**: If you don't choose a host for the group meetings, the time slots of group meetings can overlap.
  - **Internal host**: Select this option if the host is scheduled in injixo. injixo will retrieve the availability of the host from their schedule. You can select a host from a different planning unit, but the planning units of both the host and the participants must be set to the same interval. When you select this option, injixo will write scheduled meetings also to the host's schedule. Choose a **Planning unit** and an **Employee**.
  - **External host**: Select this option if the host is not scheduled in injixo.
    {{ 2 | image: 'No host', '60%' }}

9. In the _Group meetings to be scheduled between_ section, you define the list of participants for whom group meetings will be scheduled.
   - (Optional) Choose the option {% link_new **selection** | features/administration/selections.md %} or **employee filter** using the buttons on top. Select an item from the corresponding drop-down menu on the right to filter the list of all employees.
   - Check the **checkbox** to the left of a participant to select them. Use the **checkbox at the top** of the entire list of participants to (de)select all participants at once.
10. Activate the setting **Split the meeting into several time slots** if you want to split the group of participants into multiple group meetings based on the participants' availabilities. Then, use the drop-down menu **Minimum amount of participants per time slot** to specify the minimum number of participants per meeting.
    {{ 3 | image: 'Participants', '60%' }}
11. To start the meeting generation process, click _Generate suggestions_{:.doc-button} at the bottom of the page. This takes you back to the overview page.

After the group meeting suggestions have been generated, you have to {% link_new schedule them | features/scheduling/meetings/scheduling-suggestions.md %}.
