---
title: Manage availabilities in injixo Me
description: Prevent people from adding or changing their one-time availabilities before a specific date.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: false
---

In injixo, availabilities define when a person is available for scheduling on specific dates and times. As a planner, you can configure availabilities in two ways:
- Using personal {% link_new weekly availabilities | features/administration/availabilities.md | #configure-availabilities %}
- Using {% link_new day models | features/administration/availabilities.md | #rotate-availabilities-across-weeks %}

Additionally, people can add [one-time availabilities in inijxo Me](/add-availabilities-in-me#add-an-availability). If you already configured weekly availabilities, one-time availabilities replace them.

## Give people access to availabilities

To give people access to availabilities in injixo Me, configure their user role:

1. Go to _Account > User roles_{:.breadcrumbs}.
2. Click the relevant user role.
3. In the **Permissions** section, expand the **Me** drop-down menu.
4. Check the **Availabilities** checkbox.
5. Click _Save changes_{:.doc-button}.

Starting from the following day, the person can enter their availabilities in Me.

## Prevent people from editing their availabilities

The availability of your people may vary from day to day and from week to week. If you want to allow people to add their availabilities in injixo Me while avoiding scheduling conflicts, you can prevent people from adding or editing one-time availabilities before a specific date.

Example: You want to create your schedules two weeks in advance. To prevent your people from adding or editing their availabilities during those two weeks, select a date at the end of the scheduled period. If you create a schedule on 2 January for the week starting on 15 January, select 22 January. This prevents your people from adding or editing their availabilities up to 22 January.

To prevent people from editing availabilities in injixo Me before a specific date, proceed as follows:

1. Go to _Plan > Configuration > General_{:.breadcrumbs}.
2. Select a date with the date picker.
3. Click _Save changes_{:.doc-button}.

Before the specified date, people can still see their availabilities but they cannot edit them. If you do not enter any date, people are always allowed to add or edit their one-time availabilities.
