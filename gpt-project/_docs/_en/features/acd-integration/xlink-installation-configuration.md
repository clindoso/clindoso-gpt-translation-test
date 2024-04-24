---
title: Install and configure Xlink
description: Install the Xlink client and connect it with injixo to allow data imports.
product_label:
  - on-premise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/system-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-configuration-import-csv.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-configuration-import-odbc.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-log-files.md
  - overwrite_title: Add title for untranslated source
    filepath: support/faq/xlink-frequent-error-messages.md
---

In this article, you will learn:

- how to create an Xlink user.
- how to install the Xlink application.
- how to configure the connection between Xlink and the injixo host/Server.
- how to update Xlink.

You can use Xlink to import contact or agent data to on-premise installations and cloud tenants.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

## Prerequisites

Xlink requires a firewall exception. Xlink uses TCP/IP port 45054 for outgoing connections to the cloud. Tenants created before 2019 use port 80. In on-premise installations, the port defaults to 45054. You can configure the port in the file isps.cfg on the server using the parameter _IESPort_).

To install Xlink, you need Windows administrator rights on the computer where Xlink will be installed.

1. Download the [Xlink application](https://downloads.injixo.com/de#xlink-software-dokumentation) and unzip the ZIP archive.
2. Copy only the subfolder **Xlink** to any directory, e.g. _C:\\Xlink_, on the computer where you want to install Xlink.

Note: When you install Xlink for the first time, copy the configuration files **isps_Ul.ini**, **isps.cfg** and **acd_map.ini** from the subfolder _sample-configurations_ into your Xlink installation directory.

## Configure the Xlink connection

To configure both the login credentials and the server connection, you need to create a user and edit two files. Check out the following chapters depending on your WFM plan.

injixo Advanced and injixo Enterprise WFM:

- [Cloud: Create an Xlink user](#cloud-create-an-xlink-user)
- [Cloud: Configure login credentials](#cloud-configure-login-credentials)
- [Cloud: Configure the server connection](#cloud-configure-the-server-connection)

injixo Enterprise WFM On-Premise:

- [On-Premise: Create an Xlink user](#on-premise-create-an-xlink-user)
- [On-Premise: Configure login credentials](#on-premise-configure-login-credentials)
- [On-Premise: Configure the server connection](#on-premise-configure-the-server-connection)

### Cloud: Create an Xlink user

To install Xlink, you need a user with _Admin_ access.

1. Log in to injixo and go to _Account > Users_{:.breadcrumbs}
2. Click _New User_{:.doc-button}.
3. Enter an **email address** for the user. This must start with _xlink_, e.g. _xlink@yourcompany.com_.
4. Enter any text for **First name** and **Last name**, e.g. _Xlink User_.
5. On the right side, check the **Grant admin access** checkbox. No need to add any other role.
6. Click _Create_{:.doc-button} to save your changes.
7. Click the **new user** in the list of users.
8. Click _Set new password_{:.doc-button} and enter a new password. Keep this password safe.
9. Click _Save_{:.doc-button}.

Xlink will later use the user and password to connect to the server.

### Cloud: Configure login credentials

1. Open the **isps_Ul.ini** file in the Xlink installation directory with a text editor.
2. Go to the _[DB]_ section.
3. Replace **xlink@xxxx.com** with the *xlink@yourcompany.com* user you created earlier.
4. Open the file **Passcode.exe** in the **support-applications** folder.
5. In the **upper field**, enter the _Xlink user password_ to display an encrypted password in the **lower field**.
6. Copy the **encrypted password** to the clipboard for the next step and click _OK_{:.doc-button}.
   {{ 2 | image: 'Passcode.exe with text input', '75%' }}

7. Replace the string **\<password from generator\>** (including the < >) with _your-encrypted-password_ you copied from _Passcode.exe_. The result should look like this:

   ```
   [DB]
   1=WFM,0,xlink@yourcompany.com,your-encrypted-password
   ```

8. Save the changes and close the **file** _isps_ul.ini_.

### Cloud: Configure the server connection

1. Open the **isps.cfg** file in the Xlink installation directory.
2. Log in to injixo and click **WFM** in the navigation bar on top.
3. Copy the highlighted part of the host URL from the browser address bar (https://**hostname**.injixo.com/iwfm/).
4. In the **isps.cfg** file, replace **iwfm-xxxx** in the line **URL = "iwfms://iwfm-xxxx.injixo.com:45054"** with the host URL part copied before. The result should look like this:

   ```
   [IES System WFM]
   Name = "WFM"
   Url = "iwfms://your-hostname.injixo.com:45054"
   ```

5. Save the changes and close the **file** _isps.cfg_.

### On-Premise: Create an Xlink user

To install Xlink, you need a user who belongs to the user group _System_.

1. Log in to injixo and go to _Administration > System > User Authorization_{:.breadcrumbs}.
2. Click the {% icon item-add %} to create a new user.
3. Enter _xlink_ as **username** and add a password.
4. Click _OK_{:.doc-button}
5. Click the **new user** in the list of users.
6. Under **Membership**, click the {% icon item-add %} and select **System**.
7. Click _OK_{:.doc-button} twice.

Xlink will later use the user and password to connect to the server.

### On-Premise: Configure login credentials

1. Open the **isps_Ul.ini** file in the Xlink installation directory with a text editor.
2. Go to the _[DB]_ section.
3. Replace **xlink@xxxx.com** with the _xlink_ user you created.

4. Open the file **Passcode.exe** in the **support-applications** folder.
5. In the **upper field**, enter the _Xlink user password_ to display an encrypted password in the **lower field**.
6. Copy the **encrypted password** to the clipboard for the next step and click _OK_{:.doc-button}  
   {{ 2 | image: 'Passcode.exe without text input', '75%' }}

7. Replace the string **\<password from generator\>** (including the < >) with _your-encrypted-password_ you copied from _Passcode.exe_. The result should look like this:

   ```
   [DB]
   1=WFM,0,xlink,your-encrypted-password
   ```

8. Save the changes and close the **file** _isps_ul.ini_.

### On-Premise: Configure the server connection

1. Open the **isps.cfg** file in the Xlink installation directory.
2. In the **isps.cfg** file, replace _iwfm-xxxx.injixo.com_ in the line **URL = "iwfms://iwfm-xxxx.injixo.com:45054"** with the server name or IP address of your locally installed injixo server.
3. Change the **existing entry for the protocol** from _iwfms_ to _iwfm_ if you have **not** configured SSL for the Enterprise Server (default).
4. Change the **existing port entry** from 80 to 45054 (default). If another port is configured in the server file _isps.cfg_, use that one. The result should look like this (default port, no SSL):

   ```
   [IES System WFM]
   Name = "WFM"
   Url = "iwfm://your-servername:45054"
   ```

5. Save the changes and close the **file** _isps.cfg_.

## Install the Xlink Windows service

1. Open the **Windows command line** as Administrator.
2. Run the command _isps_uls.exe -install_ to install the Windows service _ISPS Xlink_.

You will get a message when the ISPS Xlink service is installed and started.

## Test the server connection

Double-click the file **isps_Ul.exe** to open the Xlink user interface.

You will see a folder icon _WFM_ on the right. Click **+** to display the queues created in injixo. On the left, you will see the {% link_new external systems | features/acd-integration/new-external-system.md %} that you have created. There are different types of external systems that require additional configuration. Learn more about {% link_new ODBC interfaces | features/acd-integration/xlink-configuration-import-odbc.md %} and the {% link_new CSV interface | features/acd-integration/xlink-configuration-import-csv.md %}.

{{ 1 | image: 'Xlink user interface in English', '75%' }}

Note: The default language of the Xlink user interface is English. Optionally, you can change the language. The installation directory contains several language subfolders (e.g. _german_). Copy the two files from one of the subfolders into the installation directory and overwrite the existing files.

<!-- also in frequent error messages, merge? -->
<!-- frequent error messages needs a rework -- could be an faq or frequent errors sections somewhere -->

## Register the file ixculcmm.dll (for manual imports)

If the progress bar of the Xlink application remains at 0% during the manual import, perform the following steps:

1. Move the file **register.exe** from the **sample-configurations** subfolder into the Xlink installation directory.
2. Open the **Windows command line** as Administrator.
3. Navigate to your Xlink installation directory.
4. Run the command _register.exe ixculcmm.dll /system_.

You will see the success message _ixculcmm.dll registered SYSTEM GLOBAL_.

If you see an error message:

- remove the write protection from the file _ixculcmm.dll_ by right-clicking the file. Go to the _Properties_ tab and uncheck **Read only**.
- close the **Windows Services** window.
- close the Xlink application **isps_Ul.exe**.

Run the file registration command (from step 3 above) again.

> You may need to repeat these steps after updating Xlink.

<!-- duplicate content - move to linked file? -->

## Update Xlink

1. Download the latest version of the [Xlink Application](https://downloads.injixo.com/en#xlink-software-documentation).
2. Stop the service **ISPS Xlink**.
3. Create a **backup** your Xlink installation directory.
4. Copy the **new files** into your Xlink installation directory, overwriting the old files.
5. Start the service **ISPS Xlink**, check the log file **isps_uls.log**, and verify that Xlink connects to the server.

Learn more about the required commands and potential error messages when {% link_new updating the Xlink installation | support/faq/xlink-update.md %}.
