---
title: Update from version 2012.3 or later
redirect_from:
  - /update-from-9xxx/
redirect_reason: renamed file in September 2020
product_label:
  - on-premise
description: Learn how to update your injixo Enterprise on-premise server to the latest version if you are currently on version 2012.3 or later.
---

This article explains how to update the injixo Enterprise Server. Depending on the version or builds you are currently using, different steps may be necessary for an update. These are described in detail in the following instructions.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

## Download the current build

Download the current [injixo Enterprise on-premise version](https://downloads.injixo.com/en#server-on-premise).

## Create a backup

It is best to make a backup of the database and the installation folder before you perform the update.

## Stop the services

Stop on your server the _injixo Enterprise_{:.menu-item} service and if necessary _InVision Enterprise WFM AutoScheduler_{:.menu-item} and _ISPS Xlink_{:.menu-item}.

> Important clue!
>
> Under certain circumstances the Windows service is named _InVision Enterprise WFM_{:.menu-item}. In this case you should delete the service with the Windows command `sc delete "InVision Enterprise WFM"`. Then go to the injixo Enterprise Server folder on the command line (by default `C:\Program Files\injixo Enterprise Server\Server`) and run the command `isps_r464.exe -install --name "injixo Enterprise Server" --fullname "injixo Enterprise Server"`.

## Remove old modules

There may still be old modules in your installation. These can lead to the injixo Enterprise Server not starting after the update.
Therefore, if available, delete the file `ivDc64.ivm` in the server directory during the first update.

## Delete calendar templates

This update includes new holiday templates for the planning calendar. If you are using a build older than 9129, you will need to delete the existing calendar templates to avoid duplicate calendar templates.

In the server directory, in the _auxiliary_{:.menu-item} folder, delete the _calendar_{:.menu-item} folder.

Once you have done this step, you can skip it next time. If you are unsure, delete the files if in doubt.

## Copy the new files

Unpack the zip file of the update in the _Server_{:.menu-item} folder in the directory where you installed the injixo Enterprise Server (by default `C:\Program Files\injixo Enterprise Server\Server`). Please overwrite any existing files.

> Note
>
> New Builds (> 9737) require the installation of the _Microsoft Visual C++ 2010 Redistributable Package (x64)_ ([Microsoft download](https://www.microsoft.com/en-us/download/details.aspx?id=26999)).

## Start the services

To complete the update process, start the _injixo Enterprise WFM_{:.menu-item} service on your server and if necessary _InVision Enterprise WFM AutoScheduler_{:.menu-item} and _ISPS Xlink_{:.menu-item}.
