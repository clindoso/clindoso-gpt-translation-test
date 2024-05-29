---
title: Configure people
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to create, view, edit and delete people.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/people/configure-people-settings.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-user-accounts.md
redirect_from: /people-overview/
redirect_reason: Renamed from /people-overview/ to /manage-people/ in Jan 2023
---

> Note
>
> This article documents the current status of the new **People** app. Until all functionalities described in this article have been completely transferred from existing features, you can still find them there.

People with admin access can access _People_{:.breadcrumbs} by default. Depending on your organization's role preferences, you may need to {% link_new grant permissions for **People** to other people | getting-started/configure-user-roles.md %} in your organization.

## Understand the People page

The **People** page contains an overview of all existing people in your organization. Next to an overview where you can {% link_new see and control | getting-started/manage-user-accounts.md %} for which people your organization is billed, the overview provides the following information on each person at one glance:

- Admin access activated or deactivated: If the person has admin access, an Admin label is displayed next to their name.
- Verification status of email address: If the person hasn't verified their email address yet, a {% icon clock %} next to their email address indicates pending verification.
- {% link_new Two-factor authentication status | getting-started/manage-2fa.md | #see-other-peoples-2fa-settings %}: An icon next to the person's email address indicates whether 2FA is active or inactive for the person.
- Assigned roles: In the top right of each person's tile, the assigned roles are displayed.

Learn how to {% link_new manage a person's account settings | features/people/configure-people-settings.md %}.

## Create a person

> Note
>
> You cannot go back to a previous step during the creation process. Before you click _Next_{:.doc-button} at any step, make sure the information you entered is correct and complete. If you need to change something about the person's configuration from a previous step, you need to complete the creation process first.

1. Go to _People_{:.breadcrumbs}.
2. On the top right, click _+ New person_{:.doc-button}.
3. In the configuration panel, follow the three-step configuration wizard. Click the links to learn how to configure the [basic information](#basic-information), [staff membership](#staff-membership), [roles](#roles), and admin access.
4. Click _Save_{:.doc-button}.
   The creation process is complete. You can now access [further configuration options](#further-configuration-options) on the person.

### Basic information

| Parameter                                    | Description                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **First name**/**Last name**/**Middle name** | The middle name is optional.                                                                                                                                                                                                                                                                                                                                                             |
| **Personnel number**                         | Have injixo automatically generate a unique identifier for the person in your organization or enter one manually.                                                                                                                                                                                                                                                                        |
| **Email (injixo login)**                     | Enter the unique email address the person uses to log in to injixo. To invite the person to log in to injixo, check the checkbox **Send welcome email**.<br>You can only send the welcome email while creating a person. The email includes instructions on how to set a password and a link to the injixo login page. When the person sets a password, their email address is verified. |

> Note
>
> When you click _Next_{:.doc-button} at the bottom of the **Basic information** page, injixo creates the person with an active staff membership right away. If you have opted for the welcome email, the person can log in to injixo. You can no longer cancel the creation process. After completing the creation process, you can [edit](#view-or-edit-a-person) or [delete](#delete-a-person) the person.

### Staff membership

| Parameter      | Description                                                                                                                                                                                                                                                    |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Valid from** | By default, the start date of the staff membership is automatically set to the current date. Your organization is billed for the person from the month of the start date. If you want the person's staff membership to be active later, change the start date. |
| **Valid to**   | By default, the end date of the staff membership is empty. If the person only has a temporary contract, set an end date.                                                                                                                                       |

Learn how to {% link_new edit a person's staff membership | getting-started/manage-user-accounts.md | #deactivate-a-person %} after completing the creation process.

### Roles

| Parameter              | Description                                                                                                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------- |
| **Grant admin access** | Only people with admin access can grant admin access to other people. Learn how to {% link_new grant admin access                                               | features/people/configure-people-settings.md            | #activate-admin-access %}. |
| Roles list             | Use the search field to find a specific role or scroll the list. Check the checkbox for each role that you want to assign to the person. {% link_new Learn more | getting-started/configure-user-roles.md %} about roles. |

## Further configuration options

After creating a person, you can access further configuration options for that person. The following sections provide more details on the additional parameters on each tab of the configuration panel.

### Profile tab

On the **Profile** tab, you can view and edit the parameters you configured on the [**Basic information**](#basic-information) page during the creation process. Additionally, you can now edit further personal information such as marital status or contact data, if necessary.

<!---At the bottom, you can {% link_new add and edit external identifiers | features/acd-integration/cloud/import-agent-status-data.md | #map-external-identifiers-to-people-in-injixo %}.--->

### Access tab

Learn how to {% link_new configure a person's access settings | features/people/configure-people-settings.md %} like enforcing 2FA or setting a new password.

## View or edit a person

1. Go to _People_{:.breadcrumbs}.
2. (Optional) To search for a person, use the search field.
3. Click a person in the list.  
   The person details open on the right. To close the details, you can click _Close_{:.doc-button}.
4. To edit the person details, click {% icon pencil | icon-only %} **Edit** at the top right of the section you want to edit.
   > Note
   >
   > If you change the email address, the person can no longer log in to injixo with their previous email address. injixo does not inform the person about their changed email address automatically.
5. Click _Save_{:.doc-button}.

## Delete a person

> Warning
>
> You cannot reactivate a deleted person. The person will be removed from all current and future schedules they were scheduled for. Deleting a person does not affect historical adherence data in {% link_new Intraday | features/intraday/adherence-intraday.md %}.

1. Go to _People_{:.breadcrumbs}.
2. Click a person in the list.  
   The data of the person is shown.
3. On the bottom right, click _Delete person_{:.doc-button}.
4. In the confirmation panel, click _Delete person_{:.doc-button}.

To ensure your schedule is up to date after deleting a person, run a {% link_new job optimization | features/scheduling/schedules/schedules-job-optimization.md %}.

## Why can I not find a person I am looking for?

People with admin access can always see all people in the organization.

If you do not have admin access, there may be different reasons why you cannot find a person using the search bar. To find out why you cannot see them in the list, check the following:

- The person is assigned to a planning unit for which you have at least read access.
- The person's assignment to the planning unit is still valid. When in doubt, ask a person with admin access to check the start and end date of the person's assignment to the planning unit. If there is no start and end date configured, the person's assignment is always valid.
