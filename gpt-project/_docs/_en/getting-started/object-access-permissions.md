---
title: Configure object access
description: Specific injixo objects can be restricted so that users only get to access a subset of e.g. Dashboards.
product_label:
  - advanced
  - enterprise
---

In this article, you will learn:

- what _Object Access Groups_ are and what you do with them.
- how you create a new group and assign it to users.
- how you restrict the default full access to injixo objects, such as Dashboards.

## What are Object Access Groups?

With _Object Access Groups_ you can restrict user access to specific injixo objects, such as Dashboards. By default, the _Full Access_ group is assigned to all users. The _Full Access_ group applies no access restrictions and therefore new users have access to all available injixo objects.

Users with _Admin access_ can create different _Object Access Groups_ and assign them to users to restrict the default access. Each user can only be member of one object access group at a time.

> Manage permissions of WFM objects that are not supported yet by this module, e.g. planning units, under _WFM > Administration > System > Role Authorization_{:.breadcrumbs}.

## Configure Object Access

Navigate to _Account > Object access_{:.breadcrumbs} to view, edit or create _Object Access Groups_.

{{ 0 | image: 'Navigate to object access screen', '80%' }}

### Create a New Object Access Group

1. Go to _Account > Object access_{:.breadcrumbs}
2. Click _Create_{:.doc-button}. The _New object access_ configuration screen opens.
3. Enter a **Name** for the new object group.
4. Enter a **Description** (optional). The description appears in the object access overview.

{{ 1 | image: 'New object access configuration screen', '80%' }}

### Restrict Access In an Object Access Group

By default, any new _Object Access Group_ grants full access to all current and future injixo objects. To restrict the user access, add the objects that the group members will have access to:

1. Check **Restrict access** for the element in the _Accessible objects_ section. This will open the object configuration.
2. Check the **checkboxes** of the elements that should be accessible by the group members. You can also search for elements.
3. Click _Create_{:.doc-button} to save the new object group.

{{ 2 | image: 'Accessible objects with restricted access', '80%' }}

> New objects are automatically accessible
>
> If a user creates a new dashboard, it is automatically added to its object access group. This makes the new dashboard available to all other users with the same object access group.

### Assign an Object Access Group to a User

Under _Account > Users_{:.breadcrumbs} you can assign an _Object Access Group_ to your users:

1. Go to _Account > Users_{:.breadcrumbs}.
2. Select a **User**. Scroll down to the _Manage object access_ section.
3. Select a **group of accessible objects** from the drop-down menu.
4. Click _Save_{:.doc-button} to save the changes. Object access is now restricted according to the configuration of the selected _Object Access Group_.

{{ 3 | image: 'Assign object groups to users', '80%' }}
