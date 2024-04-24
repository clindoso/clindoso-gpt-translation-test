---
title: Resolve client installer errors
toc: false
description: Resolve errors that can appear during the execution of the injixo MSI client installer.
product_label:
  - enterprise
  - classic
---

When you run the injixo client installer, you may see the error message: There is a problem with this Windows Installer package. A program required for this install to complete could not be run. Contact your support personnel or package vendor.

This can happen if the original installation directory has already been deleted or required files are missing.

<!-- very specific on-premise content, a bit dated:
If you run the client installer on a computer where the server has been installed with the original r4.306 installer, the client installer will try to unregister the client twice. In this case, you cannot recreate the _unregister.bat_ file. Go to solution 3. -->

There are different options to solve the problem:

## Option 1: client installer repair function

You can use the repair function of the client installer if the client is installed on your device. Run the client installer. If the repair function is not available or does not work, go to option 2 below.

## Option 2: create and analyze a log file

Windows MSI installers allow you to create a debug log file. The log file will help you to find the cause of the problem. If the two examples below do not help, go to option 3.

Create the log file in the same directory where the MSI file is stored.

You can create a log file as follows:

1. Open a Windows command prompt (CMD).
2. Start the installer by running one of the following commands:
   - errors only: `msiexec /i injixo_client.msi /le error.log`
   - full debug output: `msiexec /i injixo_client.msi /lv debug.log`

### Examples

If the file unregister.bat cannot be found, the log file contains the following message:

```
MSI (s) (B0:40) [14:08:31:233]: Note: 1: 1721 2: unregisterClient 3: C:\Program Files (x86)\InVision WFM\Client\ 4: C:\Program Files (x86)\InVision WFM\Client\unregister.bat
MSI (s) (B0:40) [14:08:34:062]: Product: injixo Client -- Error 1721. There is a problem with this Windows Installer package. A program required for this install to complete could not be run. Contact your support personnel or package vendor. Action: unregisterClient, location: C:\Program Files (x86)\InVision WFM\Client\, command: C:\Program Files (x86)\InVision WFM\Client\unregister.bat
```

You can solve this issue as follows:

1. Re-create all folders in the path that is displayed in the log file.
2. Create an _unregister.bat_ file and add `echo 1` to it.
3. Save the file and run the installer again.

If the register.bat file cannot be started, you will see the following message:

```
Error 1721. There is a problem with this Windows Installer package. A program required for this install to complete could not be run. Contact your support personnel or package vendor. Action: registerClient, location: C:\Program Files (x86)\InVision WFM\Client\, command: C:\Program Files (x86)\InVision WFM\Client\register.bat
```

The installer creates a (temporary) folder. The folder is removed when you close the message box.

To solve the problem, proceed as follows:

1. Do not close the message.
2. Create a new client folder in a different directory.
3. Go to the defined installation directory, e.g. C:\Program Files (x86)\InVision WFM\Client
4. Copy the content of the client folder to the new folder.
5. Close the error message.
6. Run the register.bat from the new folder.

## Option 3: manually edit the Windows registry

> Modifying the Windows registry can cause issues with the operating system. Create a backup.

To delete the entries created by the client installer:

1. Open the Windows registry (`Start > Run > regedit`).
2. Go to the key **HKEY_CURRENT_USER\Software\Microsoft\Installer\Products**.
3. Delete the directory `1B19A99FB16314A459325F171A154DCE` from the tree.
4. Close the registry and run the installer again to install the client.
