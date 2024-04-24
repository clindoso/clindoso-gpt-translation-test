---
title: Map call data
product_label:
  - on-premise
description: Configure Xlink to store data from your ACD queues or skills into the correct injixo queues.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/generate-xlink-scripts.md
---

In this article, you will learn:

- how to create, edit, and delete mappings for call data in Xlink.
- how mappings are saved in your Xlink installation.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

The call data (PhoneLink) import requires a mapping between injixo queues and external key figures.

The available key figures depend on your external system and the injixo import interface. Typically, interfaces provide key figures such as offered and answered calls, as well as average/total handling times. A document (TechDoc) for each interface provide further details. The TechDocs are available in the Xlink section of the [download page](https://www.injixo.com/support/downloads).

## Create mappings

You can map one or more queues from your external system to a queue value type combination in injixo. To take full advantage of injixo Forecast, consider creating one-to-one mappings.

1. Go to your Xlink installation folder and open the Xlink user interface **isps_ul.exe**.
2. Select a **queue** in the _WFM Queue_ section on the right.
3. Click the **plus icon** next to the queue to expand the value types. Select a **value type**.
4. Double-click the **value type** in the _Interface_ section on the left that you want to add to the mapping. It appears in the _Assigned Valuetypes_ section.
5. Double-click the **value type** in the _WFM Queue_ section on the right to create or edit a calculation script. The default script calculates the sum of all added value types. You can use it as template to {% link_new create your own scripts | features/acd-integration/generate-xlink-scripts.md %}.
6. In the new window, click _Create_{:.doc-button} to create a new default script.
7. Click _OK_{:.doc-button} to save the script.

Xlink imports will now execute the calculation script for the related mapping and save the results to the combination of queue, value type, and version within injixo.

### How mappings are saved?

The _acd_map.ini_ file in the Xlink folder contains one line per mapping and one line for the related script (.bas) file. The consecutive .bas file name depends on how many .bas files already exist.

```
iWFM R4 Hamburg:1:1002:1003=InvisionAcd1:Service 1:Calls
iWFM R4 Hamburg:1:1002:1003=InvisionAcd2:Service 2:Calls
iWFM R4 Hamburg:1:1002:1003=$1.BAS
```

The equal sign splits each line into two parts; each part is again separated by colons. The left part contains the name defined in the _[DB]_ section within the _isps_ul.ini_ file, as well as the parent queue, queue, and value type ID from injixo. The right side displays the names from the external system tree view, or (in case of a .bas file) the corresponding file name.

Note: The order of the lines depends on the order in which you have executed the steps to create mappings. Avoid changing the file manually, as this may result in incorrect values or even break the import process.

## Edit and remove mappings

1. Go to your Xlink installation folder and open the Xlink user interface **isps_ul.exe**.
2. Select a **queue** in the _WFM Queue_ section on the right.
3. Click the **plus icon** next to the queue to expand the value types. Select a **value type**.
4. Double-click a **mapping entry** in the _Assigned Valuetypes_ section to remove it.
5. Double-click the **value type** in the _WFM Queue_ section on the right to remove/edit the existing script.
6. Delete the script content completely, or edit it if the number/order of assigned parameters changes.
7. Click _OK_{:.doc-button} to save the script.
