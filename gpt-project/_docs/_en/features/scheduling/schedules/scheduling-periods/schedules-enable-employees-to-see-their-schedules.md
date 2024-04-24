---
title: Allow employees to see their schedules
toc: false
description: Allow employees to see their schedules in injixo Me (Schedules).
product_label:
  - essential
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/time-off-periods.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/notifications.md
---

In this article, you will learn how to allow employees to see their schedules in injixo Me.

To do this, you will use scheduling periods. Read the article {% link_new What are Scheduling Periods? | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} first.

## Allow employees to see their schedules

1. Go to _Plan > Schedules_{:.breadcrumbs}.
2. Click _Scheduling periods_{:.doc-button}.
3. Choose the **Planning unit** you want to publish schedules for.
4. Choose a **Selection** if you want to limit the publishing of the schedules to a certain group of employees (optional). If you want all employees in the planning unit to see their schedule, leave the field empty.
5. Find an existing scheduling period with the date range for which you want to publish schedules. Click the **drop-down menu** in the Status column and change the status to Published. Note: If the status is preset to Shift bidding enabled, agents can already see their schedules but also participate in shift bidding. If you change it back to Published, shift bidding will not work anymore.

If there is no scheduling period for that date range yet, click _Create scheduling period_{:.doc-button} to create a new one:

1. Set a **Date Range** to define the time period for which you want to publish the schedules.
2. Select the **Status** Published.
3. You do not have to set a **Deadline**. A deadline only affects the shift bidding process.
4. Confirm with _Save_{:.doc-button}.

   {{ 3 | image: 'Configure the Scheduling Period', '40%' }}

### Email and browser push notifications

If you want your employees to see their shifts in injixo Me, you can notify them by email or browser push notification.

Your users need to allow {% link_new browser push notifications | getting-started/notifications.md %} in their browsers.

By default, both email and browser push notifications are allowed. To turn off email or browser push notifications for your tenant, go to _Account > Notifications_{:.breadcrumbs}.
