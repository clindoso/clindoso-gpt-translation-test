EN,DE,File
---,---,install-cloud-link.md
title: Install injixo Cloud Link,title: Install injixo Cloud Link,install-cloud-link.md
product_label:,product_label:,install-cloud-link.md
- essential,- essential,install-cloud-link.md
- advanced,- advanced,install-cloud-link.md
- enterprise,- enterprise,install-cloud-link.md
- classic,- classic,install-cloud-link.md
description: Install the injixo Cloud Link client to import data into injixo.,description: Install the injixo Cloud Link client to import data into injixo.,install-cloud-link.md
related_articles:,related_articles:,install-cloud-link.md
- overwrite_title: Add title for untranslated source,- overwrite_title: Add title for untranslated source,install-cloud-link.md
filepath: features/acd-integration/cloud/how-integrations-work.md,filepath: features/acd-integration/cloud/how-integrations-work.md,install-cloud-link.md
- overwrite_title: Add title for untranslated source,- overwrite_title: Add title for untranslated source,install-cloud-link.md
filepath: features/acd-integration/cloud/import-agent-status-data.md,filepath: features/acd-integration/cloud/import-agent-status-data.md,install-cloud-link.md
---,---,install-cloud-link.md
New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.,New to integrations? Learn {% link_new the basics | features/acd-integration/cloud/how-integrations-work.md %} first.,install-cloud-link.md
## What is injixo Cloud Link?,## What is injixo Cloud Link?,install-cloud-link.md
injixo Cloud Link is a client software that needs to be installed when setting up on-premise integrations. injixo Cloud Link regularly imports data into injixo. You can also install injixo Cloud Link when configuring your CSV integrations to regularly import new CSV files from a folder.,injixo Cloud Link is a client software that needs to be installed when setting up on-premise integrations. injixo Cloud Link regularly imports data into injixo. You can also install injixo Cloud Link when configuring your CSV integrations to regularly import new CSV files from a folder.,install-cloud-link.md
The client installation directory contains:,The client installation directory contains:,install-cloud-link.md
- the injixo-cloud-link executable.,- the injixo-cloud-link executable.,install-cloud-link.md
- one or more injixo-cloud-link.\*.log file(s).,- one or more injixo-cloud-link.\*.log file(s).,install-cloud-link.md
- the injixo-cloud-link.toml config file.,- the injixo-cloud-link.toml config file.,install-cloud-link.md
- a licenses folder with open source library licenses.,- a licenses folder with open source library licenses.,install-cloud-link.md
## Prerequisites,## Prerequisites,install-cloud-link.md
- Windows: injixo Cloud Link runs on Windows 10 and above and on Windows Server 2016 and above. <!-- what about Linux -->,- Windows: injixo Cloud Link runs on Windows 10 and above and on Windows Server 2016 and above. <!-- what about Linux -->,install-cloud-link.md
- Linux: The unixODBC package must be installed.,- Linux: The unixODBC package must be installed.,install-cloud-link.md
- Firewall/Proxy: Port 443 must be open for outgoing traffic. injixo Cloud Link uses TLS-encryption with TCP over port 443.,- Firewall/Proxy: Port 443 must be open for outgoing traffic. injixo Cloud Link uses TLS-encryption with TCP over port 443.,install-cloud-link.md
"Note: On-premise integrations access a local system to pull data from, e.g. an ACD or CRM. Depending on the database type, you must install a database driver.","Note: On-premise integrations access a local system to pull data from, e.g. an ACD or CRM. Depending on the database type, you must install a database driver.",install-cloud-link.md
## Install injixo Cloud Link,## Install injixo Cloud Link,install-cloud-link.md
"When you add an {% link_new on-premise integration | features/acd-integration/cloud/add-on-premise-integration.md %}, {% link_new a CSV integration | features/acd-integration/cloud/add-csv-integration.md %}, or {% link_new a database integration | features/acd-integration/cloud/add-database-integration.md %}, the **injixo Cloud Link** section provides links to download the client installer (for Windows) or archive (for Linux).","When you add an {% link_new on-premise integration | features/acd-integration/cloud/add-on-premise-integration.md %}, {% link_new a CSV integration | features/acd-integration/cloud/add-csv-integration.md %}, or {% link_new a database integration | features/acd-integration/cloud/add-database-integration.md %}, the **injixo Cloud Link** section provides links to download the client installer (for Windows) or archive (for Linux).",install-cloud-link.md
### Windows service installation,### Windows service installation,install-cloud-link.md
Install the first service using the Windows client installer:,Install the first service using the Windows client installer:,install-cloud-link.md
1. Click **Download for Windows 64-bit** and run the installer.,1. Click **Download for Windows 64-bit** and run the installer.,install-cloud-link.md
2. Click **Next**.,2. Click **Next**.,install-cloud-link.md
3. (Optional) Change the installation directory.,3. (Optional) Change the installation directory.,install-cloud-link.md
"4. Click **Next**, then **Install**.","4. Click **Next**, then **Install**.",install-cloud-link.md
A console window displays a PIN that is valid for 5 minutes.,A console window displays a PIN that is valid for 5 minutes.,install-cloud-link.md
"To [connect Cloud Link to your integration](#connect-cloud-link-to-your-integration), follow the instructions in the console window.","To [connect Cloud Link to your integration](#connect-cloud-link-to-your-integration), follow the instructions in the console window.",install-cloud-link.md
5. Click **Finish** in the installer.,5. Click **Finish** in the installer.,install-cloud-link.md
The installer creates the **injixo Cloud Link** Windows service.,The installer creates the **injixo Cloud Link** Windows service.,install-cloud-link.md
"### <a name=""install-multiple-cloud-link-services-windows"">Install multiple Windows services","### <a name=""install-multiple-cloud-link-services-windows"">Install multiple Windows services",install-cloud-link.md
"You can install up to eight additional services for separate integrations. To avoid overwriting previous service instances, install them in separate directories.","You can install up to eight additional services for separate integrations. To avoid overwriting previous service instances, install them in separate directories.",install-cloud-link.md
"To install a second Cloud Link service on Windows, add a new integration and proceed as follows:","To install a second Cloud Link service on Windows, add a new integration and proceed as follows:",install-cloud-link.md
1. Click **Download for Windows 64-bit**.,1. Click **Download for Windows 64-bit**.,install-cloud-link.md
2. Open a Windows command prompt (cmd).,2. Open a Windows command prompt (cmd).,install-cloud-link.md
"3. For the second instance, run the following command:","3. For the second instance, run the following command:",install-cloud-link.md
```,```,install-cloud-link.md
"msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS="":instance.1""","msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS="":instance.1""",install-cloud-link.md
```,```,install-cloud-link.md
> Increase the instance ID in the TRANSFORMS parameter when you install more instances.,> Increase the instance ID in the TRANSFORMS parameter when you install more instances.,install-cloud-link.md
>,>,install-cloud-link.md
"> For example, the third instance requires `"":instance.2""`, the fourth instance`"":instance.3""`, and so on.","> For example, the third instance requires `"":instance.2""`, the fourth instance`"":instance.3""`, and so on.",install-cloud-link.md
4. Follow the instructions in the installation procedure.,4. Follow the instructions in the installation procedure.,install-cloud-link.md
"The installer will suggest a new default installation directory that includes the instance, e.g. (Instance 1).","The installer will suggest a new default installation directory that includes the instance, e.g. (Instance 1).",install-cloud-link.md
"Tip: To identify which integration the installation belongs to, you can add ACD and import type details, e.g. (ACD - agent import) to the default installation directory.","Tip: To identify which integration the installation belongs to, you can add ACD and import type details, e.g. (ACD - agent import) to the default installation directory.",install-cloud-link.md
You will see the new directory and a new Windows service named injixo Cloud Link (Instance {id}).,You will see the new directory and a new Windows service named injixo Cloud Link (Instance {id}).,install-cloud-link.md
### Linux service installation,### Linux service installation,install-cloud-link.md
Install the first service based on the following example:,Install the first service based on the following example:,install-cloud-link.md
1. Click **Download for Linux 64-bit** and extract the archive into your preferred installation folder.,1. Click **Download for Linux 64-bit** and extract the archive into your preferred installation folder.,install-cloud-link.md
2. Open a terminal.,2. Open a terminal.,install-cloud-link.md
3. Install the injixo Cloud Link service:,3. Install the injixo Cloud Link service:,install-cloud-link.md
`sudo ./injixo-cloud-link service install`,`sudo ./injixo-cloud-link service install`,install-cloud-link.md
4. Start the installed service:,4. Start the installed service:,install-cloud-link.md
`sudo ./injixo-cloud-link service start`,`sudo ./injixo-cloud-link service start`,install-cloud-link.md
5. Display a PIN with the command:,5. Display a PIN with the command:,install-cloud-link.md
`sudo ./injixo-cloud-link pin`,`sudo ./injixo-cloud-link pin`,install-cloud-link.md
A console window displays a PIN that is valid for 5 minutes.,A console window displays a PIN that is valid for 5 minutes.,install-cloud-link.md
"To [connect Cloud Link to your integration](#connect-cloud-link-to-your-integration), follow the instructions in the console window.","To [connect Cloud Link to your integration](#connect-cloud-link-to-your-integration), follow the instructions in the console window.",install-cloud-link.md
"### <a name=""install-multiple-cloud-link-services-linux"">Install multiple Linux services","### <a name=""install-multiple-cloud-link-services-linux"">Install multiple Linux services",install-cloud-link.md
"You can install multiple services that serve separate integrations. To avoid overwriting previously installed services, use separate directories.","You can install multiple services that serve separate integrations. To avoid overwriting previously installed services, use separate directories.",install-cloud-link.md
"To install more services on Linux, add a new integration and proceed as follows:","To install more services on Linux, add a new integration and proceed as follows:",install-cloud-link.md
1. Create a new directory and copy the files from the original installation directory.,1. Create a new directory and copy the files from the original installation directory.,install-cloud-link.md
2. Open the injixo-cloud-link.toml file.,2. Open the injixo-cloud-link.toml file.,install-cloud-link.md
3. Change the value for **name** in the **[app]** section to a new ID:,3. Change the value for **name** in the **[app]** section to a new ID:,install-cloud-link.md
```,```,install-cloud-link.md
[app],[app],install-cloud-link.md
"name = ""com.injixo.cloud-link.instance.1""","name = ""com.injixo.cloud-link.instance.1""",install-cloud-link.md
```,```,install-cloud-link.md
4. Install and start the new service from the new directory as described above.,4. Install and start the new service from the new directory as described above.,install-cloud-link.md
## Connect Cloud Link to your integration,## Connect Cloud Link to your integration,install-cloud-link.md
"The Cloud Link installation displays the following message, including a PIN:","The Cloud Link installation displays the following message, including a PIN:",install-cloud-link.md
```,```,install-cloud-link.md
"** Before you are able to run the client,","** Before you are able to run the client,",install-cloud-link.md
** link it to your injixo account:,** link it to your injixo account:,install-cloud-link.md
**  1) Log in to injixo.com,**  1) Log in to injixo.com,install-cloud-link.md
**  2) Visit https://www.injixo.com/account/integrations,**  2) Visit https://www.injixo.com/account/integrations,install-cloud-link.md
**  3) Select an integration you want to connect the client to,**  3) Select an integration you want to connect the client to,install-cloud-link.md
**  4) Enter your pin: 424242 (expires in 5 minutes),**  4) Enter your pin: 424242 (expires in 5 minutes),install-cloud-link.md
```,```,install-cloud-link.md
1. Go back to the **Add a new integration** page in your browser.,1. Go back to the **Add a new integration** page in your browser.,install-cloud-link.md
"2. In the **injixo Cloud Link** section, enter your PIN in the six-digit input field **PIN shown during installation**.","2. In the **injixo Cloud Link** section, enter your PIN in the six-digit input field **PIN shown during installation**.",install-cloud-link.md
3. Click _Connect_{:.doc-button}.,3. Click _Connect_{:.doc-button}.,install-cloud-link.md
Cloud Link connects to injixo. You can continue setting up your {% link_new on-premise integration | features/acd-integration/cloud/add-on-premise-integration.md %} or {% link_new CSV integration | features/acd-integration/cloud/add-csv-integration.md %}.,Cloud Link connects to injixo. You can continue setting up your {% link_new on-premise integration | features/acd-integration/cloud/add-on-premise-integration.md %} or {% link_new CSV integration | features/acd-integration/cloud/add-csv-integration.md %}.,install-cloud-link.md
## Connect through a proxy server,## Connect through a proxy server,install-cloud-link.md
"To connect through a proxy server, add the proxy hostname or IP address to the **https_proxy** environment variable:","To connect through a proxy server, add the proxy hostname or IP address to the **https_proxy** environment variable:",install-cloud-link.md
"- Windows: Add the environment variable to the **System variables** section. If services do not run with the LocalSystem account, configure a user variable.","- Windows: Add the environment variable to the **System variables** section. If services do not run with the LocalSystem account, configure a user variable.",install-cloud-link.md
- Linux: Set the environment variable in /etc/environment or in /etc/profile.d,- Linux: Set the environment variable in /etc/environment or in /etc/profile.d,install-cloud-link.md
Example: `https_proxy=http://your.proxy.example`,Example: `https_proxy=http://your.proxy.example`,install-cloud-link.md
"If required, you can add the port number (if not port 80) and user credentials for authentication:","If required, you can add the port number (if not port 80) and user credentials for authentication:",install-cloud-link.md
Example: `https_proxy=http://username:password@your.proxy.example:8080`,Example: `https_proxy=http://username:password@your.proxy.example:8080`,install-cloud-link.md
## Share injixo destination IP addresses <!-- rethink the name -->,## Share injixo destination IP addresses <!-- rethink the name -->,install-cloud-link.md
"To allow injixo Cloud Link to connect to the injixo cloud servers, share the following URLs:","To allow injixo Cloud Link to connect to the injixo cloud servers, share the following URLs:",install-cloud-link.md
- injixo-\*.s3-eu-west-1.amazonaws.com,- injixo-\*.s3-eu-west-1.amazonaws.com,install-cloud-link.md
- www.injixo.com,- www.injixo.com,install-cloud-link.md
"You cannot share a single IP address. Deployment and update processes periodically change server IP addresses. Consider installing injixo Cloud Link in the DMZ. If the connection to the server fails, you will see [Windows socket error messages](https://docs.microsoft.com/en-us/windows/win32/winsock/windows-sockets-error-codes-2) in the log file.","You cannot share a single IP address. Deployment and update processes periodically change server IP addresses. Consider installing injixo Cloud Link in the DMZ. If the connection to the server fails, you will see [Windows socket error messages](https://docs.microsoft.com/en-us/windows/win32/winsock/windows-sockets-error-codes-2) in the log file.",install-cloud-link.md
## Logging,## Logging,install-cloud-link.md
injixo Cloud Link rotates log files daily and after restart but does not delete log files. The current logs are located in injixo-cloud-link.log. Rotated log files include the rotation date in the filename. You need to set up your own recurring deletion or do it manually.,injixo Cloud Link rotates log files daily and after restart but does not delete log files. The current logs are located in injixo-cloud-link.log. Rotated log files include the rotation date in the filename. You need to set up your own recurring deletion or do it manually.,install-cloud-link.md
### Activate verbose logging,### Activate verbose logging,install-cloud-link.md
"For database integrations, injixo Cloud Link supports a verbose logging mode. When activated, the log file displays the total number of fetched rows and the first ten rows of data for each request.","For database integrations, injixo Cloud Link supports a verbose logging mode. When activated, the log file displays the total number of fetched rows and the first ten rows of data for each request.",install-cloud-link.md
You can activate verbose logging as follows:,You can activate verbose logging as follows:,install-cloud-link.md
1. Stop injixo Cloud Link.,1. Stop injixo Cloud Link.,install-cloud-link.md
"2. In the installation directory, open the injixo-cloud-link.toml file.","2. In the installation directory, open the injixo-cloud-link.toml file.",install-cloud-link.md
"3. In the **[app]** section, set **verbose** to true:","3. In the **[app]** section, set **verbose** to true:",install-cloud-link.md
```,```,install-cloud-link.md
[app],[app],install-cloud-link.md
verbose = true,verbose = true,install-cloud-link.md
```,```,install-cloud-link.md
4. Save the file and restart injixo Cloud Link.,4. Save the file and restart injixo Cloud Link.,install-cloud-link.md
## Configure import folder,## Configure import folder,install-cloud-link.md
"By default, injixo Cloud Link uploads files that are saved in its installation folder. For CSV integrations, you can configure a custom import folder as follows:","By default, injixo Cloud Link uploads files that are saved in its installation folder. For CSV integrations, you can configure a custom import folder as follows:",install-cloud-link.md
1. Stop injixo Cloud Link.,1. Stop injixo Cloud Link.,install-cloud-link.md
"2. In the installation directory, open the injixo-cloud-link.toml file.","2. In the installation directory, open the injixo-cloud-link.toml file.",install-cloud-link.md
"3. In the **[app]** section, set the value for **importDirectory** to your import folder.","3. In the **[app]** section, set the value for **importDirectory** to your import folder.",install-cloud-link.md
- Use relative or absolute paths.,- Use relative or absolute paths.,install-cloud-link.md
- Escape backslashes with a second backslash.,- Escape backslashes with a second backslash.,install-cloud-link.md
4. Save the file and restart injixo Cloud Link.,4. Save the file and restart injixo Cloud Link.,install-cloud-link.md
## Frequently asked questions,## Frequently asked questions,install-cloud-link.md
<style>,<style>,install-cloud-link.md
table th:first-of-type {,table th:first-of-type {,install-cloud-link.md
width: 25%;,width: 25%;,install-cloud-link.md
},},install-cloud-link.md
table th:nth-of-type(2) {,table th:nth-of-type(2) {,install-cloud-link.md
width: 75%;,width: 75%;,install-cloud-link.md
},},install-cloud-link.md
</style>,</style>,install-cloud-link.md
| Question                                                                        | Answer                                                                                                                                                                                                                                                                                                                                                                                                           |,| Question                                                                        | Answer                                                                                                                                                                                                                                                                                                                                                                                                           |,install-cloud-link.md
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |,| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |,install-cloud-link.md
| How do I get a new PIN if the old one has expired?                              | Restart injixo Cloud Link. Enter the new PIN from the log file in the six-digit input field in the **injixo Cloud Link** section on the configuration page.                                                                                                                                                                                                                                                      |,| How do I get a new PIN if the old one has expired?                              | Restart injixo Cloud Link. Enter the new PIN from the log file in the six-digit input field in the **injixo Cloud Link** section on the configuration page.                                                                                                                                                                                                                                                      |,install-cloud-link.md
"| How do I delete Cloud Link from my system?                                      | 1. Re-run the injixo Cloud Link installer or go to _Programs > Programs and Features_{:.breadcrumbs} in Windows.<br>2. Right-click the **injixo Cloud Link** entry in the list and select **Uninstall** or **Uninstall/Change**.<br>3. Follow the on-screen instructions.<br><br>To uninstall additional instances, go to _Programs > Programs and Features_{:.breadcrumbs} in Windows and follow steps 2 and 3. |","| How do I delete Cloud Link from my system?                                      | 1. Re-run the injixo Cloud Link installer or go to _Programs > Programs and Features_{:.breadcrumbs} in Windows.<br>2. Right-click the **injixo Cloud Link** entry in the list and select **Uninstall** or **Uninstall/Change**.<br>3. Follow the on-screen instructions.<br><br>To uninstall additional instances, go to _Programs > Programs and Features_{:.breadcrumbs} in Windows and follow steps 2 and 3. |",install-cloud-link.md
| How do I move injixo Cloud Link to a new server?                                | 1. Click the {% icon pencil %} to the right of an integration to edit it.<br>2. Click **Connect a new installation of injixo Cloud Link**.<br>3. Download injixo Cloud Link again if needed and install the software on the new server.                                                                                                                                                                          |,| How do I move injixo Cloud Link to a new server?                                | 1. Click the {% icon pencil %} to the right of an integration to edit it.<br>2. Click **Connect a new installation of injixo Cloud Link**.<br>3. Download injixo Cloud Link again if needed and install the software on the new server.                                                                                                                                                                          |,install-cloud-link.md
"| How do I change the integration for an existing injixo Cloud Link installation? | 1. Go to the installation directory and copy the PIN from the log file.<br>2. Delete the existing integration and create a new integration.<br>3. Connect your running injixo Cloud Link to the new integration. For this, enter the PIN during the configuration process for the new integration.                                                                                                               |","| How do I change the integration for an existing injixo Cloud Link installation? | 1. Go to the installation directory and copy the PIN from the log file.<br>2. Delete the existing integration and create a new integration.<br>3. Connect your running injixo Cloud Link to the new integration. For this, enter the PIN during the configuration process for the new integration.                                                                                                               |",install-cloud-link.md
