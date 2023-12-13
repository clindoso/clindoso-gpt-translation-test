---
title: Delete schedules
product_label:
  - advanced
  - enterprise
description: Delete schedules from one or more scheduling levels for a specific date range (Schedules feature).
toc: false
---

In this article, you will learn how to

- Delete schedules (activities and day models) from one or more scheduling levels for a specific date range.
- Limit the deletion to specific employees.

The instructions refer to _Plan > Schedules_{:.breadcrumbs}.

## Delete schedules for a specific date range

> Be careful when setting your parameters - you cannot undo a schedule deletion.

> Do not delete time-off requests.
>
> Approved {% link_new time-off requests | features/scheduling/time-off/vacation-absences-management.md %} are only stored in the _Schedule_ level. If you have approved time-off requests, don't delete your schedule as explained here. Because this would also delete the approved time-off requests in the chosen date range. Instead, delete the shifts manually.

This is how you delete the contents from a level in _Plan > Schedules_{:.breadcrumbs}:

1. Click _Scheduling actions_{:.doc-button}.
2. Select **Empty levels**.
3. Under _Settings_, select a **Planning unit**.
4. Change the **Date range** (optional). The date range is pre-filled with the time period currently selected in _Schedules_.
5. In **Level(s) to be emptied**, check one or more checkboxes to select the levels in which you want to delete data.
6. Under _Employees_, check the **employees** for whom you want to delete level content. You can also choose a selection or an employee filter from the drop-down menu.
7. To start the deletion job, click _Empty levels_{:.doc-button}. The deletion can take some time. Before you start the job, you can click the **JobProcessor** link on the bottom right to open a separate tab where you can follow the progress. Click _![Back button](/assets/img/common/injixo-ui/back.png)_{:.doc-button-icon} on top or _Cancel_{:.doc-button} at the bottom if you want to return to _Schedules_ without running the job.

{{ 1 | image: 'Empty level dialog', '80%' }}

After starting the deletion job, you are brought back to the _Schedules_ feature. A green or red notification on top indicates whether the job could be started successfully or not.
