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

In _Plan > Meetings_{:.breadcrumbs}, you can schedule 1:1 meetings, group meetings, and self-learning sessions. You don't need to manually shift meetings around to find the optimal place in your existing schedule. Mathematical optimization ensures minimal impact of the meeting time slots on the coverage of existing activities.

## What is the Meetings feature?

_Plan > Meetings_{:.breadcrumbs} can schedule three meeting types:

- {% link_new 1:1 meetings | features/scheduling/meetings/one-on-ones.md %}: one-on-one meetings with a team leader
- {% link_new Schedule group meetings | features/scheduling/meetings/group-meetings.md %}: meetings for groups of people with or without a host
- {% link_new Self-learning sessions | features/scheduling/meetings/self-learning-sessions.md %}: individual training sessions for people

Click a link to see how to set up the specific meeting type.

<!-- {{ 1 | image: 'Overview page' }} -->

## Prerequisites and limitations

- You need to have created at least one planning unit, one activity of type Meeting, a scheduling period, and at least one person. 
- The Schedule level must contain a schedule for the planning unit in which you want to schedule people for meetings.
- Meetings can only be scheduled for time periods in the future.
- Meetings replace {% link_new activities | features/administration/activities.md %} of type Presence configured as Replaceable.
  - Non-replaceable activities are not changed.
  - Activities of types other than Present are not changed, even if they are configured as Replaceable.

## Generate meeting suggestions

After you have decided which meeting type you want to schedule, do the following:

1. Go to _Plan > Meetings_{:.breadcrumbs}.
2. Click the **Set up** button in the card for {% link_new 1:1 meetings | features/scheduling/meetings/one-on-ones.md %}, {% link_new group meetings | features/scheduling/meetings/group-meetings.md %}, or {% link_new self-learning sessions | features/scheduling/meetings/self-learning-sessions.md %}.
3. Configure the required **parameters** for the selected meeting type, which differ depending on the meeting type.
4. Click **Generate suggestions**.  
   The maximum runtime to find the best solution is 10 minutes.  
   Meetings will be scheduled by using the time zone of the planning unit.

## Review and schedule suggestions

When you generate meeting suggestions, injixo will create a new entry in the Generated suggestions table. Each table row shows the start time and the selected meeting type and planning unit. When the process has finished, you can do the following:

1. {% link_new Check the status in the Action column | features/scheduling/meetings/scheduling-suggestions.md | #check-suggestions-generation-results %}.
2. {% link_new Review the suggested meeting time slots | features/scheduling/meetings/scheduling-suggestions.md | #review-and-apply-the-suggestions %} and apply selected or all suggestions to your schedule.
3. {% link_new Check the resulting schedule | features/scheduling/meetings/scheduling-suggestions.md | #review-the-scheduling-results %}.
