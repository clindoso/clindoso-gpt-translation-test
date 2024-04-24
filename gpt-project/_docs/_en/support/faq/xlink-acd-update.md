---
title: Switch to a new ACD
description: Reconfigure Xlink when you switch your ACD to a new version or vendor.
product_label:
  - on-premise
promote-service: acd-integration-support
---

When updating/replacing your ACD you must consider a few things, depending on your current setup.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

## ACD version update

If your ACD version is updated without any changes to the database system or data structure, you only need to change the following information (if they have been changed):

- The server address defined in the ODBC connection
- The username and password used by the ODBC connection

You can find the ODBC connection name in the isps_ul.ini file. Check the value of the `source` parameter for the affected external system.

## Updated database system

If the underlying database system of the ACD changes, e.g. from Informix to Postgresql, create a new ODBC connection (system DSN, based on the new ODBC driver) on the Xlink server.

Update the ODBC connection name, the username and the password in the Xlink configuration file as follows:

1. Open the isps_ul.ini file.
2. In the section for the affected external system, e.g. \[Your ACD name\], change the values for the parameters source, user, and password.
3. To apply the changes, restart the ISPS Xlink service.

Alternatively, make the changes in the Xlink user interface:

1. Open the Xlink user interface isps_ul.exe.
2. Click the external system you want to change on the left.
3. Go to _Settings > ACD_{:.breadcrumbs} in the menu bar, or right-click the selected external system and click **Configuration**.
4. In the configuration dialog, change the ODBC information.
5. Click _OK_{:.doc-button}.  
   The changes will be applied on the next import.

### Is a new mapping required?

When the update introduces new queues or queue IDs, or changes to existing queue names or IDs, this may require a mapping adjustment in the 'isps_ul.exe' user interface. Alternately, you may be able to use a search & replace in the 'acd_map.ini' config file. Learn more about the {% link_new mapping | features/acd-integration/xlink-mapping-telephony.md %}.

## ACD Vendor change

If you are changing to a completely new ACD (typically from a different vendor), check how this manufacturer provides their call data. You can contact your CX team with the name of the new manufacturer and the ACD version for advice.

We provide several standard interfaces besides the fully configurable universal interface and a CSV interface. Using the universal interface you can also consolidate data in a view and select the data from this view.
As an Xlink replacement, the injixo Cloud offers a file-based integration (CSV), as well as native integrations. Learn more about {% link_new how integrations work | features/acd-integration/cloud/how-integrations-work.md %}.

Create a new external system in _Administration > System > External Systems_{:.breadcrumbs} for the new Xlink ACD connection. Then configure it as described for {% link_new ODBC | features/acd-integration/xlink-configuration-import-odbc.md %} or {% link_new CSV | features/acd-integration/xlink-configuration-import-csv.md %}.

## Operating an ACD test system in parallel

If parallel operation of the old and new environment is requested, create the new ACD as another external system in _Administration > System > External Systems_{:.breadcrumbs}. Configure it as described for {% link_new ODBC | features/acd-integration/xlink-configuration-import-odbc.md %} or {% link_new CSV | features/acd-integration/xlink-configuration-import-csv.md %}.

The new ACD appears on the left side of the Xlink as an additional external system. Data should not flow into the existing WFM queues, but into a new _test queue_. Create one or more new WFM queues and create a {% link_new Mapping | features/acd-integration/xlink-mapping-telephony.md %} for the new telephone system. You can create a {% link_new test mapping for activities | features/acd-integration/xlink-mapping-activities.md %} by assigning the external IDs from the new system.

When the new system goes live, remove the old mapping and configuration and then map the new ACD queues to the existing WFM queues.

1. Create a backup of the 'acd_map.ini' and 'isps_ul.ini'.
2. Delete references to the old ACD from `acd_map.ini`.
3. Delete the section for the old external system from `isps_ul.ini`.
4. Delete the old ODBC connection (if it is no longer used)
5. Restart the `ISPS Xlink` service.
6. Create a new mapping for {% link_new Queues | features/acd-integration/xlink-mapping-telephony.md %} or {% link_new Activities | features/acd-integration/xlink-mapping-activities.md %} for the new telephony system.

The whole process is not time-critical, since the ACD usually stores data for several weeks. This allows you to run the initial data import at a later time.
