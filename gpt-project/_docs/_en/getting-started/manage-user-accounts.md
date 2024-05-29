---
title: Manage people for billing
description: Learn how to view active and inactive people and how to deactivate and delete people.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/how-does-billing-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/people/configure-people-settings.md
  - overwrite_title: Add title for untranslated source
    filepath: features/people/configure-people-settings.md
    overwrite_title: Add title for untranslated source
    filepath: features/administration/deactivate-employees.md
redirect_from:
  - /user-administration/
redirect_reason: page used in intercom, updated filename on 06 December 2022
---

> Note
>
> This article documents the current status of the new **People** app. Until all functionalities described in this article have been completely transferred from existing features, you can still find them there.

## View active and inactive people

In _People_{:.breadcrumbs}, you can see for how many people your organization is billed. At the top left of the page, you can choose which information you want to display:

- **Active**: This shows all the people for which your organization is billed.
- **Inactive**: This shows all {% link_new deactivated people | getting-started/manage-user-accounts.md | #deactivate-a-person %}. People that have been deactivated can no longer log in to injixo. Your organization is not {% link_new billed | getting-started/how-does-billing-work.md %} for people that have been deactivated.

To find one or more individual persons, use the search field on top of the people list. Use commas to separate the entries.

To filter people by role, use the drop-down menu next to the search field and select a role.

## Export the person list as a CSV file

You can export a full or filtered person list as a CSV file. For example, you can import this CSV file into external databases and tools, such as Data Warehouse databases, SAP and HR systems.

1. Go to _Account > Users_{:.breadcrumbs}.
2. (Optional) To narrow down the list of displayed people, use the search field or the roles filter.
3. Click _Export to CSV_{:.doc-button} at the top right.  
   The CSV file is downloaded to your computer.

The comma-separated CSV file contains the person's last name, first name, and email address. The export function uses a fixed file format that cannot be changed.

## Deactivate a person

To understand the consequences of deactivating people, read {% link_new this article | features/administration/deactivate-employees.md %}.

1. Go to _Account > Users_{:.breadcrumbs}.
2. Click the user name of an existing user.
3. Click _Delete_{:.doc-button} at the bottom right.  
   A window opens.
4. To deactivate the user, click _Staff Membership_{:.doc-button} and set a leave date. All scheduling data will be retained. You can still reactivate the user later.

Learn how to {% link_new reactivate a user | features/administration/deactivate-employees.md | #reactivate-employees %}.

## Delete a person

> Warning
>
> You cannot reactivate a deleted person. The person will be deleted from all current and future schedules they were scheduled for.

To permanently delete a person, follow the steps below:

1. Go to _People_{:.breadcrumbs}.
2. Search for the person you want to delete and click their tile.
3. In the configuration panel, click _Delete person_{:.doc-button} at the bottom right.
4. In the confirmation window, click _Delete person_{:.doc-button}.
