---
title: What is the Meetings feature?
product_label:
  - advanced
  - enterprise
permalink: /meetings-overview/
permalink_reason: /meetings-overview/ used in email and in Intercom message
description: Automatically schedule 1:1 meetings, group meetings, and self-learning sessions for your employees with the Meetings feature.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/meetings/scheduling-suggestions.md
---

In this article, you will learn:

- how to schedule 1:1 meetings, group meetings, and self-learning sessions with the _Meetings_ feature.
- which prerequisites must be fulfilled.
- about the limitations of scheduling meetings.

## What is the Meetings feature?

Under _Plan > Meetings_{:.breadcrumbs}, you can schedule three types of meetings for your employees:

- {% link_new 1:1 meetings | features/scheduling/meetings/one-on-ones.md %}: schedule one-on-one meetings between employees and their team leader
- {% link_new Schedule group meetings | features/scheduling/meetings/group-meetings.md %}: schedule meetings for groups of employees with or without a host
- {% link_new Self-learning sessions | features/scheduling/meetings/self-learning-sessions.md %}: schedule individual training sessions for your employees

The _Meetings_ feature will save you precious time, as you don't need to manually shift meetings around to find the optimal place in your schedule. Mathematical optimization ensures that the impact of the meeting time slots on the coverage of existing activities is minimal.

{{ 1 | image: 'Overview page' }}

## Prerequisites and limitations

Some important things to know about the _Meetings_ feature before you start:

- It requires an existing schedule in the _Schedule_ level.
- It can only replace {% link_new activities | features/administration/activities.md %} of type _Presence_ which have been configured as _Replaceable_.
  - It doesn't touch non-replaceable activities at all. They stay as they are.
  - It doesn't touch activities of types other than _Present_, even if they are configured as _Replaceable_.
- It does not generate meeting suggestions for employees that are not part of the planning unit which has been selected during the meeting setup process.
- It uses the time zone of the planning unit.
- It runs for a maximum of 10 minutes and uses the best solution found during this time.

## Generate suggestions for meeting time slots

1. Go to _Plan > Meetings_{:.breadcrumbs}.
2. Decide which meeting type you want to schedule. You can choose between {% link_new 1:1 meetings | features/scheduling/meetings/one-on-ones.md %}, {% link_new group meetings | features/scheduling/meetings/group-meetings.md %}, and {% link_new self-learning sessions | features/scheduling/meetings/self-learning-sessions.md %}. Click the **Set up** button in the respective card.
3. Configure the required **parameters** for the selected meeting type. The parameters differ depending on the meeting type. Click one of the links above to learn more about how to set up the specific meeting type.
4. Click **Generate suggestions**.

## Review suggestions and write them into the schedule

When you have started the process to generate meeting suggestions, an entry appears in the _Generated suggestions_ table. It shows when the process has been initiated, the meeting type, and the selected planning unit. The process can take some time to complete. Afterwards, you

1. {% link_new check if the process was successful | features/scheduling/meetings/scheduling-suggestions.md | #check-if-the-process-was-successful %},
2. {% link_new review the meeting time slot suggestions | features/scheduling/meetings/scheduling-suggestions.md | #review-and-apply-the-suggestions %}, write selected or all suggestions into the schedule, and
3. {% link_new review the scheduling results | features/scheduling/meetings/scheduling-suggestions.md | #review-the-scheduling-results %}.
