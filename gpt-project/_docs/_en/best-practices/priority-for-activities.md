---
title: Priority value for activities
product_label:
  - advanced
  - enterprise
  - classic
description: Learn how to protect activities from being overwritten by other activities.
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/importance-for-activities.md
---

You can define a priority value for each activity in _Plan > Configuration > Activities_{:.breadcrumbs}.
The priority value defines which activities can be overwritten by other activities during manual schedule updates or job optimization.

## Why do I need the priority value for activities?

By default, all activities have the same priority. As a consequence, certain activities might be replaced by others if they have different staff requirements. You can ensure that certain activities are never overwritten by using the priority value (default: 1).

An activity with a high priority value (highest value: 1) cannot be replaced by activities that have a lower priority value. You can use this functionality if you want to ensure that an activity is never replaced by another.

## Prerequisites

For prioritizing activities with the priority value, the following must be true:

- The activities that need to be prioritized are configured as {% link_new Replaceable | features/administration/activity-types-and-properties.md | #activity-properties %}.
- If they are of type Present, the activities must have staff requirements.
- Scheduling rule _2660_{:.id-label} _Check activity priority_ is activated.

## Example 1: Activity type Presence <!-- find a better title -->

- There are two activities: B2B hotline and B2C hotline.
- Both activities are of the type {% link_new Presence | features/administration/activity-types-and-properties.md | #activity-types %}.
- B2B hotline is critical and should never be replaced by B2C hotline.

After creating an initial schedule, you recalculate your staff requirements according to current events for both activities to check if your activities are still properly staffed. If the staff requirements for B2C hotline have increased, run a job optimization to ensure that the activities are correctly balanced. However, by doing this, the job optimization might reassign people from B2B hotline to B2C hotline in the schedule.

To ensure that B2B hotline is never replaced by B2C hotline, assign a priority value of 1 to B2B hotline and a lower priority value (a number larger than 1) to B2C hotline.

If there aren't enough people to handle both activities simultaneously, injixo will ensure that B2B hotline is always staffed before B2C hotline.

## Example 2: Illness and Home office

- There are two activities: Illness and Home office.
- Both activities are of type {% link_new Absence | features/administration/activity-types-and-properties.md | #activity-types %}.

Because both activities are of type Absence, they do not have staff requirements. If you insert shift sequences that include Home office without defining a priority, injixo might overwrite Illness with Home office. This could cause problems for people who are ill that day and who are scheduled for Home office.

To prevent that Illness is replaced with Home office, assign a priority value of 1 to Illness and a priority value of 2 (or higher) to Home office. This will ensure that the Illness activity cannot be overwritten by the Home office activity.
