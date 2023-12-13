---
title: Configure user roles
redirect_from:
  - /user-and-role-authorization/
redirect_reason: renamed file in June 2021
description: Learn which user roles are available, change their permissions, create new user roles, and assign roles to users.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-user-accounts.md
---

## What are user roles?

A user role defines access rights for a group of users:

- to the products and features in injixo, e.g. _Forecast_{:.menu-item}.
- to the features in WFM, e.g. _WFM > Administration_{:.breadcrumbs}.

injixo has role categories, each with one {% link_new default user role | getting-started/default-user-roles.md | #default-user-roles %} with preset access rights, i.e. permissions. When you add a new user role within a role category, it will have the access rights to the products and features of the default user role.<br>
The Other role category does not have a default user role.

### View and organize user roles

Go to _Account > User roles_{:.breadcrumbs}.  
   User roles are grouped in pre-defined role categories (e.g. the Planner role category). The role categories can help to keep access rights organized. You can also drag and drop a user role from one role category to another or use the search to find user roles by name.
   
   > Permissions for new functionalities are granted based on the role category  
   >   
   >Permissions for new injixo functionalities are assigned to user roles automatically and depending on their role category. For example, a new functionality for planners will be accessible to all user roles in the Planner role category. If you have moved a user role from the Planner role category to another role category, it will no longer automatically receive permissions for the new Planner functionality. If needed, a user with Admin access can add the permissions to the user role manually. The same applies to user roles in the Other role category. Their permissions always need to be added manually.

   {{ 1 | image: "Categories on user roles overview", '80%' }}

### Create new user roles

1. Click the {% icon blue_plus %} in any role category. Hover over the information icons {% icon info_circle | icon-only %} to learn more about each role category.

   - Category Other: Creates a blank user role. There are no default permissions set.
   - {% link_new Default role | getting-started/default-user-roles.md %} categories: Default permissions for injixo components are pre-selected. The access rights to WFM features are not set. 
  > Note
  >
  > When you create a new user role, you need to manually [set access rights to the features in WFM](#set-wfm-permissions).

2. On the **Create user role** page, configure the user role:

   - **Basic information**: Enter a **Name**, an **Abbreviation**, and an optional **Description**.
   - **Role category**: Displays the pre-selected **Role category**.

3. (Optional) Edit the default permissions. In the **Permissions** section, a gray checkmark icon next to a component name indicates that all permissions for this component are granted by default. A gray minus icon indicates that some permissions for this component are not granted by default.  
   - Component: To grant permissions for all features in a component, check the checkbox next to the component name.
   - Feature: To grant permissions for single features, click the arrow pointing down next to a component name. Check the checkbox(es) next to the feature(s).
   - To view all sections, click **Uncollapse all**. To close all sections, click **Collapse all**.
   - To reset any selected permissions to the default user role, click **Reset to default**.
4. To save the new user role, click _Create user role_{:.doc-button}. To [set WFM permissions](#set-wfm-permissions) for the new user role, click _Create & go to Role Authorization_{:.doc-button}.

   {{ 2 | image: "Create user role page", '80%' }}

### Assign user roles to users

1. Go to _Account > Users_{:.breadcrumbs}.
2. Click a **Name**.
3. Under **Assign user role(s)**, check one or more checkboxes. To filter the displayed user roles, use the **Search user roles** input field.
4. Click _Save_{:.doc-button}.

   {{ 6 | image: 'Assign user roles', '80%'}}

## Set WFM permissions

1. Under _Account > User roles_{:.breadcrumbs}, select a user role.
2. In the **Permissions** section, click **Go to Role authorization**.  
   You will be redirected to _WFM > Administration > System > Role authorization_{:.breadcrumbs}.
3. In the **Navigator** section on the right, check or uncheck the checkboxes to add or remove rights.

{{ 4 | image: "Navigator section in WFM role authorization", '60%' }}

We recommend using only role-based permissions. You can change permissions for individual users, if needed. To change individual permissions, go to _WFM > Administration > System > User Authorization_{:.breadcrumbs}.

## Manage team access: Restrict access to configuration data

If your organization includes several teams and you want to restrict access to the teams' data, you can add more than one user role to a user. injixo combines the permissions defined by different user roles. You can restrict access to elements such as planning units, day models, activities, or reports.

**Example**

If all your planners should have access to the schedule but each planner should only be able to edit the data of their own planning unit, you can assign two user roles to each planner.

You can create a new user role with no access to specific planning units, or remove access to all planning units from an existing user role. To remove access to all planning units from an existing user role, proceed as follows:

1. Go to _Account > User roles_{:.breadcrumbs}.
2. Select the user role.
3. Click **Go to Role Authorization**.
4. Scroll to the **Planning Units** section (or use the quick link on top).
5. Click the {% icon item-delete %} next to the [ALL] entry to delete access to all planning units.
6. Click _OK_{:.doc-button}.

Add access to the specific planning unit to other roles as follows:

1. Select the second user role.
2. In the **Planning Units** section, click the {% icon item-add %}.
3. Select the planning unit(s) from the list. Press **CTRL** or **Shift** while clicking to select multiple planning units.
4. Under **Access Authorization**, check one or more checkboxes to set **Read**, **Edit**, and **Delete** rights.
5. Click _OK_{:.doc-button}.

To complete the configuration, go to _Account > Users_{:.breadcrumbs} and [assign the roles to your users](#assign-user-roles-to-users).


## Edit custom or default user roles

1. Go to _Account > User Roles_{:.breadcrumbs}.
2. Select the user role entry to be changed.
3. Make the desired changes to the user role, and click _Save changes_{:.doc-button}.

## Delete custom user roles

1. Go to _Account > User Roles_{:.breadcrumbs}.
2. Select the user role entry.
3. Click _Delete user role_{:.doc-button} on the bottom right. Default user roles cannot be deleted.
