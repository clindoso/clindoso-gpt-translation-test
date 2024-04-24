---
title: Use Xlink log files
product_label:
  - on-premise
description: Activate logging for Xlink and learn about what kind of information is logged.
---

Xlink generates log files, which are important in case of problems with the data import. You may be able to find a problem yourself by taking a look at the files. The log files contain errors and warnings. However, this article does not explain specific error messages. Your Customer Success Team needs them for problem analysis.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

## Activate logging

The configuration file 'isps_ul.ini' contains a parameter **Protocol** in two places:

- Section [General]
- Section [Name of your external system].

To activate logging, change the value from 0 to 1 and restart the 'ISPS Xlink' service after saving the file.

## Xlink log files for service and user interface

A log file is generated after the import of call and agent data.

These log files contain information about

- any starts/stops of the Xlink interface and service
- loaded configuration parameters
- mapping and script changes
- the start and end of each import
- data records read by the interface
- possible error messages, e.g. for connection problems

When logging is activated in the [General] section, Xlink will populate following log files with data:

- isps_uls.log
- isps_ul.log

If the option for agent data import (TimeLink) is activated in the external system, there is another log file:

- external_system_agent_import.log

### Interface-specific logging

Activate logging in the section [Name of your external system] so that the Xlink creates a log file for each mapped queue from the external system.

These log files contain:

- Queries to the data source (database or file)
- Returned values
- Error messages (due to any incorrect configuration, e.g. for universal interface)

From your external system, 'Queue1' and 'Queue2' are linked/mapped with injixo, the Xlink now creates two log files:

- external_system_queue1.log
- external_system_queue1.log

### Specify a custom log directory

Specifically for interface log files, you are able to configure a different target directory. To do this, add the parameter 'LogDir' with an absolute path in the [General] section of the 'isps_ul.ini':

Example:

```
[General]
LogDir="C:\Xlink\Logs"
```

## Maximum file size

Log files can reach a maximum size of 4 GB. Xlink does not delete log files automatically.

As a result, Xlink will no longer import data. There are two possible solutions:

- Switch off logging (Protocol=0).
- Delete the files regularly manually or by using a bat file in a scheduled task.
