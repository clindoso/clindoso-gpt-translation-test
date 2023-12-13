---
title: Autocorrect incorrect mappings
description: Autocorrect mappings after changing parent queue.
toc: true
product_label:
  - on-premise
related_articles:
  - title: Map call data
    filepath: features/acd-integration/xlink-mapping-telephony.md
---

In this article, you will learn how to configure the _AutomaticMappingCorrection_ parameter in Xlink to automatically correct invalid mappings.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

## What Is the _AutomaticMappingCorrection_ Parameter for?

To import call data, you need queue mappings. Existing queue mappings become invalid if you change the parent queue in a queue.
Duplicate mappings may occur if you create new mappings for the queue in the Xlink user interface. These mappings can lead to incorrect or missing data.

## Activate the _AutomaticMappingCorrection_ Parameter

Note: The parameter _AutomaticMappingCorrection_ is part of the Xlink sample configuration and may already be included in the _isps_ul.ini_ file.

1. Stop the **ISPS Xlink** service on the computer where the Xlink is installed.
2. Open the file _isps_ul.ini_ in the Xlink folder.
3. In the section _[GENERAL]_, add the parameter **AutomaticMappingCorrection=1** . If the parameter already exists, change the configured value from 0 to 1 if necessary.
4. Restart the service **ISPS Xlink**
5. Open the Xlink user interface **isps_ul.exe** again.

Xlink checks existing mapping entries in the _acd_map.ini_ file. Xlink detects incorrect mappings and corrects or removes them. The current _acd_map.ini_ file is backed up. A dialog window tells you if wrong mappings have been detected.

## Review Mapping Changes

Any mapping changes are logged to the _isps_ul.log_ file. There are two different messages:

- _Invalid Mapping detected and automatically corrected_: A mapping entry with an invalid parent queue is changed to the correct queue ID.
- _Invalid Mapping(s) detected and automatically removed_: A mapping entry with invalid IDs exists multiple times. The additional entries are removed.

Example:

```
03/17/22 12:15:48 > ** ANALYSING MAPFILE STARTED **

03/17/22 12:15:48 > Invalid Mapping(s) detected and automatically removed:
03/17/22 12:15:48 > 	R4-System:1001:1016:1009=$350.BAS
03/17/22 12:15:48 > 	R4-System:1001:1016:1009=Avaya CMS:1:VDN:123:ACDTIME
03/17/22 12:15:48 > The following valid mapping was identified:
03/17/22 12:15:48 > 	R4-System:1:1016:1009=$473.BAS
03/17/22 12:15:48 > 	R4-System:1:1016:1009=Avaya CMS:1:VDN:123:ACDTIME

03/17/22 12:15:48 > Invalid Mapping detected and automatically corrected:
03/17/22 12:15:48 > 	R4-System:1104:1108:1023=$522.BAS
03/17/22 12:15:48 > 	R4-System:1104:1108:1023=Avaya CMS:1:Split:Test:Holdtime
03/17/22 12:15:48 > Updated to:
03/17/22 12:15:48 > 	R4-System:0:1108:1023=$522.BAS
03/17/22 12:15:48 > 	R4-System:0:1108:1023=Avaya CMS:1:Split:Test:Holdtime

03/17/22 12:16:03 > The file 'C:\Program Files\InVision Enterprise WFM\XLink\Acd_map.ini' has been backed up to the file 'C:\Program Files\InVision Enterprise WFM\XLink\Acd_map220317121603.ini'

03/17/22 12:16:03 > ** ANALYSING MAPFILE COMPLETED **
```
