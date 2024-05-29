---
title: Configure people settings
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn how to unlock people who have locked themselves out, set a new password for people, change a person's role, and grant admin access to an existing person.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/people/configure-people.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-user-accounts.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-2fa.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/configure-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/single-sign-on.md
---

> Note
>
> This article documents the current status of the new **People** app. Until all functionalities described in this article have been completely transferred from existing features, you can still find them there.

People with admin access can access _People_{:.breadcrumbs} by default. Depending on your organization's role preferences, you may need to {% link_new grant permissions for **People** to other people | getting-started/configure-user-roles.md %} in your organization.

New to People? Learn {% link_new the basics | features/people/configure-people.md %} first.

The following sections describe how you can change the settings for a person.

## Activate admin access

1. Go to _People_{:.breadcrumbs}.<br>
2. Use the search field to look for the person for whom you want to activate admin access and click their tile.
3. In the **Access** tab of the configuration panel, click {% icon pencil | icon-only %} **Edit** in the **Roles and admin access** section.
4. Check the **Grant admin access** checkbox at the top.
5. Click _Save_{:.doc-button}.

## Change the role

1. Go to _People_{:.breadcrumbs}.<br>
2. Use the search field to look for the person whose role you want to change and click their tile.
3. In the **Access** tab of the configuration panel, click {% icon pencil | icon-only %} **Edit** in the **Roles and admin access** section.
4. Check the checkbox next to the role(s) you want to assign or unassign.
5. Click _Save_{:.doc-button}.

## Set a new password

1. Go to _People_{:.breadcrumbs}.<br>
2. Use the search field to look for the person for whom you want to set a new password and click their tile.
3. In the **Access** tab of the configuration panel, click {% icon pencil | icon-only %} **Edit** in the **Authentication and password** section.
4. In the **Password** section of the panel, enter a new password and click {% icon check_circle | icon-only %} **Save**.

You need to notify the person of their new password. For security reasons, tell them to change their password and store it in a secure place.

## Unlock a person

People are locked after three failed login attempts with a wrong password. To unlock people, proceed as follows:

1. Go to _People_{:.breadcrumbs}.
2. Look for the person you want to unlock.<br>
   The people list shows a {% icon lock %} next to every locked person's name.
3. Click the tile of the locked person.
4. In the **Access** tab of the configuration panel, click {% icon pencil | icon-only %} **Edit** in the **Authentication and password** section.
5. At the bottom of the panel, click _Restore password_{:.doc-button}.

The person can now log in again with their previous password. If they don't remember it, [set a new password](#set-a-new-password) for that person.

## Activate 2FA

Learn how to {% link_new manage 2FA | getting-started/manage-2fa.md %} for one person at a time or everybody in your organization at once.

## Change user principal name for single sign-on

In _People_{:.breadcrumbs}, you can change the user principal name (UPN) for individual people if the email address for the injixo login differs from the UPN used by the single sign-on identity provider.
Learn how to {% link_new configure single sign-on | getting-started/single-sign-on.md %} for one person at a time or everybody in your organization at once.

1. Go to _People_{:.breadcrumbs}.
2. Look for the person for whom you want to edit the user principal name and click their tile.<br>
3. In the **Access** tab of the configuration panel, click {% icon pencil | icon-only %} **Edit** in the **Single sign-on** section.
4. Enter a new user principal name.
5. Click _Save_{:.doc-button}.

## Change language and time zone

1. Go to _People_{:.breadcrumbs}.
2. Look for the person for whom you want to change the language and/or time zone and click their tile.<br>
3. In the **Profile** tab of the configuration panel, click {% icon pencil | icon-only %} **Edit** in the **Language and time zone** section.
4. From the drop-down menus, select a language and/or time zone.
5. Click _Save_{:.doc-button}.
