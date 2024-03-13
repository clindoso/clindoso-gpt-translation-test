---
title: Manage 2FA
product_label:
  - essential
  - advanced
  - enterprise
description: Learn how to activate and deactivate 2FA for your employees' accounts.
redirect_from:
  - /2fa/
redirect_reason: Updated filename on 14 July 2023
---

> Only users with admin access can manage two-factor authentication (2FA) for other users.

## See other users' 2FA settings

To see other users' current 2FA status, proceed as follows:
1. Go to _Account > Users_{:.breadcrumbs}.
2. In the **2FA** column on the right, a shield icon indicates the 2FA status for each user. Hover over it to see more information.
  - Red icon {% icon 2FA-red | icon-only %}: 2FA is not active.
  - Orange icon with exclamation mark {% icon 2FA-orange | icon-only %}: 2FA was enforced for the user. The user has to activate 2FA upon next login.
  - Green icon with checkmark {% icon 2FA-green | icon-only %}: 2FA is active.

## Enforce 2FA activation for other users
You can make other users activate 2FA. Enforcing 2FA for other users has the following consequences:

- Users will not able to log in if they don't activate 2FA.
- Users will not be able to deactivate 2FA for their personal accounts anymore.

Before you enforce 2FA for other users, make sure that they have access to one of the {% link_new supported authenticator apps | getting-started/use-two-factor-authentication.md | #prerequisite-install-an-authenticator-app %}.

### Enforce 2FA activation for individual users

1. Go to _Account > Users_{:.breadcrumbs}.
2. Click the **name** of the user for whom you want to enforce 2FA activation.  
   The page with the user's details opens.
3. In the **Security** section, check the **Enforce 2FA activation** checkbox.
4. Click _Save_{:.doc-button} to confirm the activation.

### Enforce 2FA activation for all users

1. Go to _Account > Security_{:.breadcrumbs}. On this page, you can see the current distribution of 2FA among your users.
2. Click _Enforce 2FA for all users_{:.doc-button}.  
   You will see a green success message. The button text will change to _Revoke enforcement_{:.doc-button}.

### Deactivate 2FA for individual users

In some cases, you may want to deactivate 2FA temporarily for individual users, or exclude some users from 2FA enforcement.

1. Go to _Account > Users_{:.breadcrumbs}.
2. Click the **name** of the user for whom you want to deactivate 2FA.  
   The page with the user's details opens.
3. In the **Security** section, uncheck the **Enforce 2FA activation** checkbox.
4. Click _Save_{:.doc-button} to confirm the deactivation.
