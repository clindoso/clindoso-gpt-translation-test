---
title: Configure and start data imports
description: Configure the different Xlink import modes.
product_label:
  - on-premise
redirect_from: /xlink-import-modus/
redirect_reason: Renamed file in April 2022
---

In this article, you will learn:

- how to configure the automatic import mode.
- how to start an import manually.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

The import is always carried out for the entire day, i.e. in the case of a historical import for a larger period, several consecutive import processes are always carried out for the respective individual days.  
The import mode is basically configured for all external systems in Xlink. It is not possible to configure different modes only for certain interfaces.

## Automatic import

Import data continuously for the current day or once a day retroactively for the previous day.

The described settings can be made separately for the import of call and employee data. In the Xlink interface, select _Auto-Import_{:.menu-item} from the _Settings_{:.menu-item} menu to configure the automatic import.

{{ 1 | image: 'Xlink Auto-Import Settings', '80%' }}

### Import current data every x minutes

To import the data every X minutes, set the interval at which the import should take place. The selected interval must not be less than the actual duration of the import. The more often data is requested, the higher the network load and the load on the ACD database may be. Therefore, do not set the value lower than necessary.

In addition, the ACD must have already finished writing the data at the time of the import and this must be completely available in the queried table. Since this can take up to a few minutes, you can use the _Reference time_ to specify a time offset when the import should start after the actual end of the interval. For example, a value of 00:05 means that the import will not take place every 15 minutes, but 5 minutes later, i.e. 5, 20, 35 and 50 minutes after every full hour.

### Import previous day's data daily at...

With this option Xlink imports data of the previous day at a fixed time. Use this option if your external system does not provide data for the current day, but only for the previous day. To import data further back, use the [manual import](#manual-import).

### No automatic import

Select this option if you do not want to perform automatic import. Usually you use this option only if you do not have direct access to the ACD database or if CSV files are available only irregularly. In this case use the [manual import](#manual-import).

## Manual import

You can start a manual import via the menu _File > Start Import > Import Call Data_{:.breadcrumbs}. In addition, the menu provides the following buttons:

{{ 2 | image: 'Xlink Manual Import', '25%' }}

For importing call data, select the destination flag, for importing agent activity data select the corresponding option from the menu or the second button with the heads.

A manual import is necessary whenever historical data has to be re-imported, e.g. when new mappings have been created. For the duration of a manual import the auto-import is interrupted, a post-import of not imported current intervals takes place at the next automatic import.

## Write zero values (WriteAlways parameter)

If the _Settings > Write null values_{:.breadcrumbs} option is activated, 0 calls will be accepted for intervals that do not return any values on import. This will cause any existing values in your WFM queues to be overwritten with 0. A change via the Xlink interface updates the _WriteAlways_ parameter in the `isps_ul.ini` file.

This can be the case if, for example, a period is imported for which your ACD has no more data stored, but can be correct if, for example, you have changed a mapping and you actually want to overwrite existing data with 0.

_Write zero values_ can be helpful if data has been imported incorrectly due to a summer/winter time change and you actually need to overwrite the first or last interval of the day with 0.  
However, it is usually advisable not to set the _Write zero values_ option so that existing data is not accidentally overwritten with 0.

## Data import in console mode

To automatically import data that is not available on the same day or from the previous day, e.g. if your service provider only provides you with historical ACD data once a week, use the command line parameters of the Xlink interface _isps_ul.exe_ for the import in a Windows command line, e.g. `ISPS_UL.EXE -t -d MM/DD/YYYY -L 7`.

The following parameters exists (copy from the context help):

- -p = Import of call data (PhoneLink)
- -t = Import of employee activity data (TimeLink)
- -d = start date in the specified format
- -L = import period in days
