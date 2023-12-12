---
title: Install injixo Cloud Link
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Install the injixo Cloud Link client to import data into injixo.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.

## What is injixo Cloud Link?

injixo Cloud Link is a client software that needs to be installed when setting up on-premise integrations. injixo Cloud Link regularly imports data into injixo. You can also install injixo Cloud Link when configuring your CSV integrations to regularly import new CSV files from a folder.

The client installation directory contains:

- the injixo-cloud-link executable.
- one or more injixo-cloud-link.\*.log file(s).
- the injixo-cloud-link.toml config file.
- a licenses folder with open source library licenses.

## Prerequisites

- Windows: injixo Cloud Link runs on Windows 10 and above and on Windows Server 2016 and above. <!-- what about Linux -->
- Linux: The unixODBC package must be installed.
- Firewall/Proxy: Port 443 must be open for outgoing traffic. injixo Cloud Link uses TLS-encryption with TCP over port 443.

Note: On-premise integrations access a local system to pull data from, e.g. an ACD or CRM. Depending on the database type, you must install a database driver.

## Install injixo Cloud Link

When you add an {% link_new on-premise integration | features/acd-integration/cloud/add-on-premise-integration.md %}, {% link_new a CSV integration | features/acd-integration/cloud/add-csv-integration.md %}, or {% link_new a database integration | features/acd-integration/cloud/add-database-integration.md %}, the **injixo Cloud Link** section provides links to download the client installer (for Windows) or archive (for Linux).

### Windows service installation

Install the first service using the Windows client installer:

1. Click **Download for Windows 64-bit** and run the installer.
2. Click **Next**.
3. (Optional) Change the installation directory.
4. Click **Next**, then **Install**.  
   A console window displays a PIN that is valid for 5 minutes.  
   To [connect Cloud Link to your integration](#connect-cloud-link-to-your-integration), follow the instructions in the console window.
5. Click **Finish** in the installer.  
   The installer creates the **injixo Cloud Link** Windows service.

### <a name="install-multiple-cloud-link-services-windows">Install multiple Windows services

You can install up to eight additional services for separate integrations. To avoid overwriting previous service instances, install them in separate directories.

To install a second Cloud Link service on Windows, add a new integration and proceed as follows:

1. Click **Download for Windows 64-bit**.
2. Open a Windows command prompt (cmd).
3. For the second instance, run the following command:

   ```
   msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS=":instance.1"
   ```

   > Increase the instance ID in the TRANSFORMS parameter when you install more instances.
   >
   > For example, the third instance requires `":instance.2"`, the fourth instance`":instance.3"`, and so on.

  
4. Follow the instructions in the installation procedure.  
   The installer will suggest a new default installation directory that includes the instance, e.g. (Instance 1).  
   Tip: To identify which integration the installation belongs to, you can add ACD and import type details, e.g. (ACD - agent import) to the default installation directory.  
   You will see the new directory and a new Windows service named injixo Cloud Link (Instance {id}).

### Linux service installation

Install the first service based on the following example:

1. Click **Download for Linux 64-bit** and extract the archive into your preferred installation folder.
2. Open a terminal.
3. Install the injixo Cloud Link service:  
   `sudo ./injixo-cloud-link service install`
4. Start the installed service:  
   `sudo ./injixo-cloud-link service start`
5. Display a PIN with the command:  
   `sudo ./injixo-cloud-link pin`  
   A console window displays a PIN that is valid for 5 minutes.  
   To [connect Cloud Link to your integration](#connect-cloud-link-to-your-integration), follow the instructions in the console window.

### <a name="install-multiple-cloud-link-services-linux">Install multiple Linux services

You can install multiple services that serve separate integrations. To avoid overwriting previously installed services, use separate directories.

To install more services on Linux, add a new integration and proceed as follows:

1. Create a new directory and copy the files from the original installation directory.
2. Open the injixo-cloud-link.toml file.
3. Change the value for **name** in the **[app]** section to a new ID:

   ```
   [app]
   name = "com.injixo.cloud-link.instance.1"
   ```

4. Install and start the new service from the new directory as described above.

## Connect Cloud Link to your integration

The Cloud Link installation displays the following message, including a PIN:

```
** Before you are able to run the client,
** link it to your injixo account:
**  1) Log in to injixo.com
**  2) Visit https://www.injixo.com/account/integrations
**  3) Select an integration you want to connect the client to
**  4) Enter your pin: 424242 (expires in 5 minutes)
```

1. Go back to the **Add a new integration** page in your browser.
2. In the **injixo Cloud Link** section, enter your PIN in the six-digit input field **PIN shown during installation**.
3. Click _Connect_{:.doc-button}.
   Cloud Link connects to injixo. You can continue setting up your {% link_new on-premise integration | features/acd-integration/cloud/add-on-premise-integration.md %} or {% link_new CSV integration | features/acd-integration/cloud/add-csv-integration.md %}.

## Connect through a proxy server

To connect through a proxy server, add the proxy hostname or IP address to the **https_proxy** environment variable:

- Windows: Add the environment variable to the **System variables** section. If services do not run with the LocalSystem account, configure a user variable.
- Linux: Set the environment variable in /etc/environment or in /etc/profile.d

Example: `https_proxy=http://your.proxy.example`

If required, you can add the port number (if not port 80) and user credentials for authentication:

Example: `https_proxy=http://username:password@your.proxy.example:8080`

## Share injixo destination IP addresses <!-- rethink the name -->

To allow injixo Cloud Link to connect to the injixo cloud servers, share the following URLs:

- injixo-\*.s3-eu-west-1.amazonaws.com
- www.injixo.com

You cannot share a single IP address. Deployment and update processes periodically change server IP addresses. Consider installing injixo Cloud Link in the DMZ. If the connection to the server fails, you will see [Windows socket error messages](https://docs.microsoft.com/en-us/windows/win32/winsock/windows-sockets-error-codes-2) in the log file.

## Logging

injixo Cloud Link rotates log files daily and after restart but does not delete log files. The current logs are located in injixo-cloud-link.log. Rotated log files include the rotation date in the filename. You need to set up your own recurring deletion or do it manually.

### Activate verbose logging

For database integrations, injixo Cloud Link supports a verbose logging mode. When activated, the log file displays the total number of fetched rows and the first ten rows of data for each request.

You can activate verbose logging as follows:

1. Stop injixo Cloud Link.
2. In the installation directory, open the injixo-cloud-link.toml file.
3. In the **[app]** section, set **verbose** to true:

   ```
   [app]
   verbose = true
   ```

4. Save the file and restart injixo Cloud Link.

## Configure import folder

By default, injixo Cloud Link uploads files that are saved in its installation folder. For CSV integrations, you can configure a custom import folder as follows:

1. Stop injixo Cloud Link.
2. In the installation directory, open the injixo-cloud-link.toml file.
3. In the **[app]** section, set the value for **importDirectory** to your import folder.
   - Use relative or absolute paths.
   - Escape backslashes with a second backslash.
4. Save the file and restart injixo Cloud Link.

## Frequently asked questions

<style>
table th:first-of-type {
    width: 25%;
}
table th:nth-of-type(2) {
    width: 75%;
}
</style>

| Question                                                                        | Answer                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How do I get a new PIN if the old one has expired?                              | Restart injixo Cloud Link. Enter the new PIN from the log file in the six-digit input field in the **injixo Cloud Link** section on the configuration page.                                                                                                                                                                                                                                                      |
| How do I delete Cloud Link from my system?                                      | 1. Re-run the injixo Cloud Link installer or go to _Programs > Programs and Features_{:.breadcrumbs} in Windows.<br>2. Right-click the **injixo Cloud Link** entry in the list and select **Uninstall** or **Uninstall/Change**.<br>3. Follow the on-screen instructions.<br><br>To uninstall additional instances, go to _Programs > Programs and Features_{:.breadcrumbs} in Windows and follow steps 2 and 3. |
| How do I move injixo Cloud Link to a new server?                                | 1. Click the {% icon pencil %} to the right of an integration to edit it.<br>2. Click **Connect a new installation of injixo Cloud Link**.<br>3. Download injixo Cloud Link again if needed and install the software on the new server.                                                                                                                                                                          |
| How do I change the integration for an existing injixo Cloud Link installation? | 1. Go to the installation directory and copy the PIN from the log file.<br>2. Delete the existing integration and create a new integration.<br>3. Connect your running injixo Cloud Link to the new integration. For this, enter the PIN during the configuration process for the new integration.                                                                                                               |
