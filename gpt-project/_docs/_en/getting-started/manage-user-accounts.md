---
title: Manage user accounts
description: View billed and unbilled users. Create, edit, and delete users. Manage user access by adding user roles.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-2fa.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
redirect_from:
  - /user-administration/
redirect_reason: page used in intercom, updated filename on 06 December 2022
---

Set up user accounts in injixo to manage the people in your organization. 

Under _Account > Users_{:.breadcrumbs} you get a complete overview of all users:
- Billed users: This tab shows all active users in your injixo tenant.
- Unbilled users: This tab shows all {% link_new deactivated users | features/administration/deactivate-employees.md %} who can no longer log in to injixo. Your organization is no longer {% link_new billed | getting-started/how-does-billing-work.md %} for deactivated users.

To find one or more individual users, use the search field on top of the user list. Use commas to separate the entries.
To filter users by user role, click the **User roles** column header. A dialog opens where you can select one or more roles. All users that have at least one of the selected roles are displayed in the user list.

## Create users

Users are also called people. injixo provides three separate places for user creation:
- _Account > Users_{:.breadcrumbs}
- _WFM > Administration > Scheduling > Employees_{:.breadcrumbs}
- {% link_new People | features/people/manage-people.md | #create-a-new-person %}

> Note
> 
> You only need to create a user once in one of these places. injixo will then automatically synchronize this user data in the two other places.

To create a user, follow these steps:

1. Go to _Account > Users_{:.breadcrumbs}.
2. Click _Create user_{:.doc-button}.
3. Fill out the user data and click _Create_{:.doc-button}.

## Edit a user account

injixo provides two places where you can edit a user account, depending on what you want to do. The table below gives you an overview of the different configuration options and where you can find them in injixo. You can also access both of these places from People.

| I want to                                          | Where to go in injixo                                                                             |
| -------------------------------------------------- | ------------------------------------------------------------------------------------- |
| {% link_new Configure scheduling-related settings for a user | features/administration/employee-overview.md | #overview-of-employee-settings %} (e.g. assign activities, add skill levels, define availabilities) | _WFM > Administration > Scheduling > Employees_{:.breadcrumbs} |
| {% link_new Edit staff membership information | getting-started/manage-user-accounts.md | #deactivate-a-user-account %} for a user       | _WFM > Administration > Scheduling > Employees_{:.breadcrumbs} |   
| Edit language and time zone information for a user | _Account > Users_{:.breadcrumbs} |
| {% link_new Assign a user role to a user | getting-started/configure-user-roles.md | #assign-user-roles-to-users %} | _Account > Users_{:.breadcrumbs} |
| {% link_new Enforce two-factor authentication | getting-started/manage-2fa.md %}   | _Account > Users_{:.breadcrumbs} |

If you want to edit a user, e.g. to change their email address, follow these steps:

1. Go to _Account > Users_{:.breadcrumbs}.
2. Click the user name of an existing user.
3. Change the user settings.
4. Click _Save_{:.doc-button}.

### Grant admin access to a user

1. Go to _Account > Users_{:.breadcrumbs}.
2. Click the user name of an existing user.
3. In the **Admin access** section, check the **Grant admin access** checkbox.
4. Click _Save_{:.doc-button}.

### Unlock users

User accounts get locked after three failed login attempts with a wrong password. To unlock locked users, follow these steps:

1. Go to _Account > Users_{:.breadcrumbs}.<br>
The user list shows a yellow {% icon lock %} next to the locked user's name.
2. Click the user name of the locked user.
3. In the **Security** section on the right, click _Unlock user_{:.doc-button}.

When you have unlocked a user, we recommend setting a new password for that user. 

### Set a new user password

If a user has forgotten their password, they can reset it themselves by clicking the **Forgot your Password?** link on the login page. Alternatively, you can set it for them, e.g. after their account was locked.
To set a new password for a user, follow these steps:

> Note
>
> Users are not notified about password changes. You need to inform them about their new password.

1. Go to _Account > Users_{:.breadcrumbs}.
2. Click the user name of an existing user.
3. In the **Security** section on the right, click _Set new password_{:.doc-button}.
4. Enter a new password for the user.
5. Click _Save_{:.doc-button}.



## Deactivate a user account

To understand the consequences of deactivating user accounts, read {% link_new this article | features/administration/deactivate-employees.md %}.

1. Go to _Account > Users_{:.breadcrumbs}.
2. Click the user name of an existing user.
3. Click _Delete_{:.doc-button} on the bottom right.  
   A window opens.
4. To deactivate the user, click _Staff Membership_{:.doc-button} and set a leave date. All scheduling data will be retained. You can still reactivate the user later.

Learn how to {% link_new reactivate a user | features/administration/deactivate-employees.md | #reactivate-employees %}.

## Delete a user account

> Warning
>
> You cannot reactivate a deleted user account. The user account will be deleted from all current and future schedules they were scheduled for.

To permanently delete a user account, follow the steps below:

1. Go to _Account > Users_{:.breadcrumbs}.
2. Click the user name of an existing user.
3. Click _Delete_{:.doc-button} on the bottom right.  
   A window opens.
4. Check the checkbox **I understand that the user record and all scheduling data for \<user name\> will be deleted.**
5. Click _Delete_{:.doc-button}. 

## Export the user list as a CSV file

You can export a full or filtered user list as a CSV file. For example, you can import this CSV file into external databases and tools, such as Data Warehouse databases, SAP and HR systems.

1. Go to _Account > Users_{:.breadcrumbs}.
2. (Optional) To narrow down the list of displayed users, use the search field or the roles filter.
3. Click _Export to CSV_{:.doc-button} on the top right.  
   The CSV file is downloaded to your computer.

The comma-separated CSV file contains the last name, first name, and the users' email address. The export function uses a fixed file format that can't be changed.
