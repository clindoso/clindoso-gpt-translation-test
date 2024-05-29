---
title: Solve Xlink errors
description: Common Xlink error messages and how to resolve them.
product_label:
  - on-premise
---

Here we have compiled the most common error messages or problems with the Xlink application and
refer to possible solutions.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

## Enterprise Server 1 not available

**The connection between injixo and the Xlink cannot be established correctly.**

Please check the credentials that are stored in the _DB_{:.menu-item} section of the `isps_ul.ini` file and
whether your firewall has enabled the `TCP port 45054` (injixo systems created before 2019 might use port 80).
In addition, please check the hostname which is entered in the `isps.cfg` in the Xlink directory. This should
correspond to the first part of the URL displayed when you are in the WFM section of injixo.

## regsvr32 /s "\*.DLL" failed: 3

**This error message occurs when the Microsoft Visual C++ 2005 SP1 redistributable Package (x86) is not installed.**

The Xlink download contains a folder _Server redistributable_. Install the MSI file for the Microsoft Visual C++ 2005 SP1
redistributable or use the [Download from Microsoft](https://www.microsoft.com/en-ie/download/details.aspx?id=26347) to get
the file.

## Cannot connect to the database

**The credentials of the Xlink user are not correct.**

Give your Xlink user a new password in injixo under _Account_{:.menu-item}. Check whether there is a small lock
next to the user. In this case, the Xlink user was blocked due to too many incorrect logins and you have to unlock
the Xlink user. Store the new password as a coded string (using `passcode.exe`) in `isps_ul.ini` and restart the Xlink
service once.

## The import no longer works and the log does not contain any data.

**The maximum log file size has been reached.**

The maximum Xlink log file size is 4&nbsp;GB. This is because Xlink is a 32-bit application. If the log file reaches 4&nbsp;GB, it can no longer be extended and the import will stop.

Delete the file `isps_ul.log` from the Xlink directory and restart the ISPS Xlink service. To avoid this error in the future, add the parameter LogMaxFileSize to the file `isps_ul.ini` under the section \[General\]. LogMaxFileSize limits the size of file types isps_uls.log und isps_ul.log, e.g. `LogMaxFileSize = 10240` corresponds to a log file size of 10&nbsp;MB.

> Note
>
> The size of interface log files is not limited. Interface log files must be deleted manually. Xlink only generates interface log files if the parameter `Protocol=1` has been configured for external systems in at least one section of the file `isps_ul.ini`. If the protocol is only activated in the \[General\] section, Xlink does not generate interface log files.

## Manual import does not start (progress bar remains at 0&nbsp;%)

The progress bar stalls at 0&nbsp;% during the manual import, and the log file isps_uls.log includes the entries: From Invalid Date Time to Invalid Time.

**If you use Windows terminal services, e.g. server access via 'mstsc', the file 'ixculcmm.dll' must be registered globally.**

1. Move the file **register.exe** from the **support-applications** folder to the Xlink folder.
2. Run the Windows command line as administrator.
3. Navigate to your Xlink folder.
4. Run the following command: `register.exe ixculcmm.dll /system`<br>
   You see the message: ixculcmm.dll registered SYSTEM GLOBAL

If you see an eror message, follow these steps:

1. To remove the write protection for the file **ixculcmm.dll**, right-click on the file > Properties > Uncheck **Write protected**.
2. Close the Windows services window and the Xlink application isps_ul.exe (if open).
3. Reregister the file: `register.exe ixculcmm.dll /system`.

## CSV import moves files but does not import data

**Data is not imported during manual or automatic CSV data import. The CSV file configuration is not correct.**

Check the group names in the parameter `Groups` in the file `isps_ul.ini`. The names must be identical (case-sensitive) to those in your CSV file.
After editing the names, you must adjust the mapping in the file acd_map.ini, and restart the ISPS Xlink service.
