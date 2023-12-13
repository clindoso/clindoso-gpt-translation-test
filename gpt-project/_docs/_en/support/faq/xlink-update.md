---
title: Update Xlink
toc: true
description: Steps to update your Xlink installation with a new version.
product_label:
  - on-premise
---

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

We release new Xlink versions with bug fixes on the [download page](https://downloads.injixo.com/en#xlink-software-documentation). To check your current Xlink version, open the **version.txt** file or right-click the **isps_ul.exe** file and choose Properties. Then, navigate to the Details tab.

## Open Windows services and command line

Open the services window in Windows as follows:

1. Open the Windows start menu.
2. Type in `services.msc` (some Windows versions require to use the search field).
3. Confirm your input with `Enter`.

Open a command line prompt:

1. Open the Windows start menu.
2. Type in `cmd` (some windows versions require you to use the search field).
3. Right click and select _Run as Administrator_{:.doc-button}.

## Prepare the Xlink update

1. Backup the following configuration files from your current Xlink installation:

   - isps.cfg
   - isps_ul.ini
   - isps_ulx.ini (if existing)
   - acd_map.ini
   - all \*.bas files

2. Download the _Xlink Suite_ from [downloads.injixo.com](https://downloads.injixo.com) and unzip the archive.
3. Stop the `ISPS Xlink` service.

## Update Xlink

1. Overwrite your current Xlink installation using the files from the subfolder `xlink`.
2. In the Windows services, right-click the `ISPS Xlink` service and select _Properties_. To see if the service is running with the local system or a special user account, go to the **Login** tab.

   > Note
   >
   > A special user account will be removed while reinstalling the Xlink service. Make sure to set it again after you have reinstalled the ISPS Xlink service.

   {{ 1 | image: 'Windows Services', '50%' }}

3. Close the Windows services window.
4. Remove the service from the command line with the command `sc delete "ISPS Xlink"`.
5. Copy the files that you backed up in step 1 back to the existing Xlink installation directory and overwrite any existing files.
6. Run the command `register.exe ixculcmm.dll /SYSTEM` using the command line.  
   The command line shows the message: ixculcmm.dll registered SYSTEM GLOBAL

   > Note
   >
   > To fix the error messages `Open file failed, rc=5 Error[5]:Access is denied.` or `Open file failed, rc=32 Error [32]: The process cannot access the file because it is being used by another process.`, remove the write protection from the `ixculcmm.dll` file and close the Xlink application `isps_ul.exe`. If you still see the second message, wait for a short time before you can re-run the command successfully.

7. Reinstall the Xlink service using the command `isps_uls.exe -install`.

## Xlink and User Account Control

[User Account Control](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/how-it-works) (UAC) is a key part of Windows security. But due to UAC, Xlink may be unable to update the isps_ul.ini file in the Xlink installation directory. Instead, Windows creates a copy of the isps_ul.ini file in the VirtualStore directory (user/appdata/local/virtualstore).

This can happen when you change the general settings using the isps_ul.exe file. As a consequence, Xlink will not read the correct configuration file.

To fix the problem, take one of the following steps:

- Rename the isps_ul.ini file in the user/appdata/local/virtualstore directory.
- Delete the isps_ul.ini file from the user/appdata/local/virtualstore directory. Or, rename the file to create a backup copy.

After that, you can either run the isps_ul.exe file as admin or [change the folder permissions](#adjust-users-folder-permissions) and apply the configuration changes as usual.

### Run the isps_ul.exe file as Administrator (recommended)

Starting the isps_ul.exe file with elevated privileges allows direct access to the Xlink installation directory, thus bypassing the VirtualStore.

1. Navigate to the Xlink installation directory.
2. Right-click the **isps_ul.exe** file.
3. In the context menu, select **Run as administrator**.
4. If UAC prompts you, select **Yes** or **Continue**.

### Adjust users' folder permissions

Change the permissions of the application's installation folder to give write access to standard Windows users. They can then avoid using the VirtualStore.

1. In the Windows Explorer, go to the Xlink installation directory.
2. Right-click the directory and select **Properties**.
3. In the **Security** tab, click the **Edit...** button to change permissions.
4. From the **Group or user names** list, select **Users**.
5. In the **Permissions for Users** section, check the **Write** checkbox under the **Allow** column.
6. Click **Apply**, then **OK**.
