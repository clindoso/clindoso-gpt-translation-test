---
title: Manage 2FA
product_label:
  - essential
  - advanced
  - enterprise
description: Learn how to activate and deactivate 2FA for your people.
redirect_from:
  - /2fa/
redirect_reason: Updated filename on 14 July 2023
---

> Only people with admin access can manage two-factor authentication (2FA) for other people.

## See other people's 2FA settings

To see other people's current 2FA status, proceed as follows:

1. Go to _People_{:.breadcrumbs}.
2. A shield icon indicates the 2FA status for each person. Hover over it to see more information.
   - Red icon {% icon 2FA-red | icon-only %}: 2FA is not active.
   - Orange icon with exclamation mark {% icon 2FA-orange | icon-only %}: 2FA was enforced for the person. The person has to activate 2FA on their next login.
   - Orange icon with checkmark {% icon 2FA-activated | icon-only %}: 2FA is active. The person activated 2FA themselves.
   - Green icon with checkmark {% icon 2FA-green | icon-only %}: 2FA is active. The use of 2FA was enforced.

## Enforce 2FA activation for other people

You can make other people activate 2FA. Enforcing 2FA for other people has the following consequences:

- People will not able to log in if they don't activate 2FA.
- People will not be able to deactivate 2FA for themselves anymore.

Before you enforce 2FA for other people, make sure that they have access to one of the {% link_new supported authenticator apps | getting-started/use-two-factor-authentication.md | #prerequisite-install-an-authenticator-app %}.

### Enforce 2FA activation for individual people

1. Go to _People_{:.breadcrumbs}.
2. Use the search field to look for the person for whom you want to enforce 2FA and click their tile.
3. In the **Access** tab of the configuration panel, click {% icon pencil | icon-only %} **Edit** in the **Authentication and password** section.
4. Click {% icon check_circle | icon-only %} **Enforce 2FA**.
5. Click _Save_{:.doc-button}.

### Enforce 2FA activation for everyone

1. Go to _Account > Security_{:.breadcrumbs}. On this page, you can see the current distribution of 2FA among your people.
2. Click _Enforce 2FA for all users_{:.doc-button}.  
   You will see a green success message. The button text will change to _Revoke enforcement_{:.doc-button}.

### Deactivate 2FA for individual people

In some cases, you may want to deactivate 2FA temporarily for individual people, or exclude some people from 2FA enforcement.

1. Go to _People_{:.breadcrumbs}.
2. Use the search field to look for the person for whom you want to deactivate 2FA and click their tile.
3. In the **Access** tab of the configuration panel, click {% icon pencil | icon-only %} **Edit** in the **Authentication and password** section.
4. Click {% icon arrow-rotate-left | icon-only %} **Revoke 2FA enforcement**.
5. Click _Save_{:.doc-button}.
