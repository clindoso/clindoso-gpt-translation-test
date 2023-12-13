---
title: What is an external system?
toc: false
product_label:
  - on-premise
description: Learn what external systems are and how to create them.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-configuration-import-odbc.md
---

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

In this article, you will learn:

- what an external system is and why you need it.
- how to create an external system.

## What is an external system?

External systems are required to import data using Xlink.

> You don't need an external system to upload data using an {% link_new integration | features/acd-integration/cloud/how-integrations-work.md %}.

External systems define which Xlink (standard) interface is used to retrieve data via ODBC or CSV files. The interfaces behind external systems use a vendor-specific rigid configuration and import logic to connect and to get data from the ACD or file.

The available Universal and CSV interface are more flexible, as you can define a format for files or tables the Xlink reads data from. The corresponding manuals for these interfaces are available at [downloads.injixo.com](https://downloads.injixo.com).

## Create an external system

1. Go to _WFM > Administration > System > External System_{:.breadcrumbs}.
2. Click the {% icon item-add %}.
3. Under _System Description_, select **CSV Files**, **Universal**, or a **specific interface** for your ACD.
4. Enter a **Name** to identity the data source.
5. Check the checkboxes **PhoneLink** (for call data) and **TimeLink** (for agent activity data). Not all interfaces support both options.
6. Click _OK_{:.doc-button}.
