---
title: IP filtering
product_label:
  - enterprise
  - advanced
description: Learn how to set up IP filtering for your injixo tenant.
toc: true
---

IP filtering is a paid feature. It is not automatically included in your Enterprise or Advanced WFM plan.
If your organization is interested in this feature, get in touch with your consultant.

IP filtering ensures that your users can access your injixo tenant from specific IP address ranges only. Users with other IP addresses will not be able to access injixo. injixo offers a [network access control list](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) (network ACL). Activate the network ACL if you want to allow access to injixo from selected networks only (e.g your organization's network).

## Activate IP filtering

Only users with admin access can activate IP filtering.

> Note
>
> When you activate IP filtering, all active users are logged out. Depending on the product area, the time frame varies:
>
> - Logout can be immediate
> - Logout happens when data is next loaded or stored
> - Logout is timed (only in Shift Center accessible via _Plan > Shift Center_{:.breadcrumbs})
>
> To continue working with injixo, users will have to log in again.

1. Go to _Account > Security_{:.breadcrumbs} and scroll to the **IP filtering** section.
2. In the **IP address range** field(s), enter the IP address ranges in the [CIDR format](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#:~:text=CIDR%20notation%20specifies%20an%20IP,bits). You can add up to three IP address ranges.
3. Click _Activate filtering_{:.doc-button}.

IP filtering only affects UI interactions. The optionally available Shift Center via direct URL is currently not affected by IP filtering.

## Edit the IP address ranges

> Note
>
> If you edit the IP address ranges, all users will be logged out when they next interact with injixo. To continue working with injixo, users will have to log in again.

1. Go to _Account > Security_{:.breadcrumbs} and scroll to the **IP filtering** section.
2. Edit the IP address ranges.
3. Click _Save_{:.doc-button}.

## Deactivate IP filtering

1. Go to _Account > Security_{:.breadcrumbs} and scroll to the **IP filtering** section.
2. Delete the IP address ranges.
3. Click _Deactivate filtering_{:.doc-button}.

After deactivating IP filtering, users will be able to access injixo from any IP address.

> Note
>
> If you deactivate IP filtering, all users will be logged out. To continue working with injixo, users will have to log in again.
