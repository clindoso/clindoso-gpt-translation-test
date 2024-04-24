---
title: Manage people
product_label:
  - advanced
  - enterprise
description: Learn how to create, view, edit and delete people.
beta-feature: true
redirect_from: /people-overview/
redirect_reason: Renamed from /people-overview/ to /manage-people/ in Jan 2023
---

People allows you to manage data for the people in your company:

- Create, edit and delete person profiles
- Send an injixo invitation to a new person (Welcome email)
- Go to a person's user account settings
- Go to a person's configuration data in WFM

> Users with admin access can access People by default.
>
> To {% link_new grant permissions for People to other users | getting-started/configure-user-roles.md %}, go to _Account > User roles_{:.breadcrumbs}. Select a role and check the checkbox next to **People** in the **Permissions** section under **Products and features**.

## Create a new person

1. Go to _People_{:.breadcrumbs}.
2. Click _+ New person_{:.doc-button}.
3. Under **Basic information**, enter the mandatory information for the person:
   - **First name** and **Last name**, and optionally **Middle name**.
   - **Personnel number**: Unique identifier for the person in your company.
   - **Email (injixo login)**: Enter the email address the person uses to log in to injixo.
4. To invite the person to log in to injixo, check the checkbox **Send welcome email**.  
   You can only send the welcome email while creating a person. The email includes instructions to set a password and a link to the injixo login page. When the person sets a password, their email address will be verified.
5. (Optional) Enter optional information for the person, such as a phone number or further contact information.
   The input in the **Title** field is not used anywhere in injixo. You can use this to address people, for example when distributing newsletters.
6. Click _Create person_{:.doc-button}.  
   If the checkbox **Send welcome email** has been checked, injixo will send the welcome email to the person.

   > Note
   >
   > The person will not automatically get a user role or planning unit. After saving a person, go to the associated WFM employee or user by clicking **WFM** or **Account**.

## Invite a person to log in to injixo

You can only {% link_new invite a person to log in to injixo by welcome email | features/people/manage-people.md | #create-a-new-person %} while you create this person.

## View or edit a person

1. Go to _People_{:.breadcrumbs}.
2. (Optional) To search for a person, use the **Search** field.
3. Click a person in the list.  
   The person's details open on the right. To close the details, you can click _Cancel_{:.doc-button} or press **Esc** on your keyboard.
4. Edit the person's details.

   > Note
   >
   > If you change the email address, the person can no longer log in to injixo with their previous email address. injixo does not inform the person about their changed email address automatically.

5. Click _Save changes_{:.doc-button}.

## Delete a person

> Warning
>
> You cannot reactivate a deleted person. The person will be deleted from all current and future schedules they were scheduled for. Deleting a person does not affect historical adherence data in {% link_new Intraday | features/intraday/adherence-intraday.md %}.

1. Go to _People_{:.breadcrumbs}.
2. Click a person in the list.  
   The data of the person is shown.
3. Click _Delete person_{:.doc-button}.
4. In the confirmation window, click _Delete person_{:.doc-button}.

To ensure your schedule is up to date after deleting a person, run the job optimization.
