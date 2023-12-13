---
title: Set up Internet Explorer mode in Microsoft Edge
product_label:
  - advanced
  - enterprise
  - classic
description: Set up Internet Explorer Mode in Microsoft Edge. This allows you to use injixo, including those components based on ActiveX.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/browser-setup.md
---

In inijxo Enterprise on-premise and injixo Classic, the WFM module (https://\*.injixo.com/iwfm/\*) requires Microsoft&nbsp;Edge in [Internet&nbsp;Explorer mode](https://docs.microsoft.com/en-us/deployedge/edge-ie-mode) (IE mode) to run ActiveX components. injixo supports Microsoft&nbsp;Edge version 97 and above. In Microsoft&nbsp;Edge, you can check the version using the URL _edge://version_.

You need Windows administrator rights to configure Internet Explorer mode (IE mode) for Microsoft Edge. Contact your IT, if necessary.

## Prepare the client

1. Open the **Windows start menu**.
2. Search for **Internet Options**.
3. On the **Security** tab, check the **Enable Protected Mode** checkbox for the **Internet** zone.  
   Skip this step on Windows 11 and above.
4. Click _Sites_{:.doc-button}.
5. Click _Add_{:.doc-button}.
6. Add _\*.injixo.com_ to the trusted sites.
7. To save your settings, click _OK_{:.doc-button}.


## Configure Internet Explorer Mode in Edge

Internet Explorer Mode in Microsoft Edge requires an XML file that contains a site list. The site list file can be installed locally (see example below) or hosted. If you host the site list file on a server, the same file is available for all users.

### 1. Create a site list XML file

1. Create a new XML file (e.g. sitelist.xml) with the following content:

   ```
   <site-list version="1.0">
     <!-- iwfm-xxxx must be your injixo host. You can find it in the URL of injixo WFM -->
     <site url="https://iwfm-xxxx.injixo.com/iwfm/">
       <compat-mode>Default</compat-mode>
       <open-in>IE11</open-in>
     </site>
     <shared-cookie
       domain=".injixo.com"
       name="injixo_session"
       source-engine="MSEdge">
     </shared-cookie>
     <shared-cookie
       domain=".injixo.com"
       name="iwfm_language_id"
       source-engine="MSEdge">
     </shared-cookie>
   </site-list>
   ```

2. In injixo, click **WFM** to access WFM and copy the displayed **URL**.
3. In the XML file, replace the value for the URL with your injixo host URL.
4. Save the file on your computer.

Learn more about the [IE mode](https://docs.microsoft.com/en-us/deployedge/edge-ie-mode) and related [group policies](https://learn.microsoft.com/en-us/deployedge/edge-ie-mode-policies) in the Microsoft documentation.

### 2. Adjust the Windows registry

1. To access the registry editor, open the Windows start menu, enter **regedit**, and press **Enter**.
2. Go to **HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft**.
3. Right-click the **Microsoft** folder.
4. In the context menu, select **New** and **Key**.
5. Name the new key **Edge**.

Add the entry **InternetExplorerIntegrationLevel**:

1. Right-click the new **Edge** folder.
2. In the context menu, select **New**, then **DWORD value 32-bit**.
3. Name the new entry **InternetExplorerIntegrationLevel**.
4. Double-click the entry.
5. Enter 1 (or hexadecimal: 0x00000001).

Add the entry **InternetExplorerIntegrationSiteList**:

1. Right-click the new **Edge** folder.
2. In the context menu, select **New** and then **String** value (REG_SZ).
3. Name the new entry **InternetExplorerIntegrationSiteList**.
4. Double-click the new entry.
5. Enter the path to your site list XML file (e.g. file:///c:/path/to/sitelist.xml).  
   Note: If you host the site list, enter the server URL, e.g. https://your.company.com/sitelist.xml.

To save all changes, click _Ok_{:.doc-button}.

Tip: You can see configured registry entries and policies under [edge://policy/](edge://policy/).

### 3. Activate the new site list

To force Edge to use the new site list, proceed as follows:

1. Restart Edge.
2. To display the site list configuration (and to troubleshoot issues), go to [edge://compat](edge://compat).
3. To apply the configuration, click **Force update**{:.doc-button}.

The list updates and displays the configured URL under _domain_.

You can now log in to injixo. Only WFM will use IE mode (indicated by an Internet Explorer symbol next to the URL). All other components (e.g. Plan) will use the standard Edge mode.

> If Edge does not switch back from IE mode to standard Edge mode, delete the cookies in Edge.

## Deactivate sleeping tabs

By default, Edge tabs go into sleep mode after two hours of inactivity. In injixo Advanced and Enterprise WFM, this interrupts the connection to the Shift Center.

To avoid tabs going into sleep mode, add _injixo.com_ to the block list in the Edge settings:

1. Open Microsoft Edge.
2. Click **Settings and More** (...) or press **Alt+F**.
3. Click **Settings**.
4. On the left, click **System**.
5. In the **Save resources** section next to **Never put these sites to sleep**, click **Add**.
6. In the input field, enter *https://www.injixo.com*.
7. Click **Add**.
8. Close the **Settings** tab.

Note: Windows administrators can configure this exception for all users. Administrators can also increase the sleep interval in the registry using group policies.
