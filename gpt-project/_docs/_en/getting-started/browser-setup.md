---
title: Browser setup
description: Learn how to set up your browser to work with injixo.
product_label:
  - on-premise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: support/faq/client-installer-errors.md
  - overwrite_title: Add title for untranslated source
    filepath: support/faq/session-timeout-message.md
redirect_from:
  - /setup-guide/
redirect_reason: Updated filename on 27 July 2023
---

To work with ActiveX-based features in WFM, use {% link_new Microsoft Edge in Internet Explorer (IE) mode | support/faq/configure-edge-internet-explorer-mode.md %}. You can find a list of compatible browsers in the {% link_new System requirements | getting-started/system-requirements.md | #browser-requirements %}.

If you have insufficient rights to change the browser settings or to install software, contact your IT department.

## Configure the trusted sites and security zone settings

injixo Classic and injixo Enterprise WFM contain ActiveX controls. You need to allow the browser (Edge in IE Mode) to run these ActiveX controls.

In the browser settings, add all injixo pages (_\*.injixo.com_) to the trusted sites:

1. Open the Windows start menu, type internet options, and press the Enter key.
2. On the **Security** tab, select the **Trusted sites** zone, and click _Sites_{:.doc-button}.
3. In the **Add this website to the zone** field, enter https://\*.injixo.com.
4. Check the checkbox **Require server verification (https:) for all sites in this zone**.
5. Click **Add**.
6. Click **Close**.

{{ 1 | image: 'security settings', '45%', 'jpg' }}

Adjust the security zone level for the trusted sites:

1. On the Windows start menu, type internet options, and press the Enter key.
2. On the **Security** tab, select the **Trusted sites** zone.
3. Uncheck the checkbox **Enable Protected Mode**.  
   Note: This checkbox is no longer available in Windows 11 and above.
4. On the **Security** tab, adjust the security level for **Trusted Sites** to **Medium** or **Medium-Low**. Medium-Low allows you to skip steps 6 to 9.
5. Click _OK_{:.doc-button}.
6. Click _Custom level..._{:.doc-button}.
7. In the **Security Settings** dialog window, change the following settings:

   | Setting                                           | State             |
   | ------------------------------------------------- | ----------------- |
   | Script ActiveX Controls marked safe for scripting | ENABLED           |
   | Run ActiveX Controls and Plugins                  | ENABLED           |
   | Download Signed ActiveX Controls                  | PROMPT or ENABLED |
   | Automatic Prompting for ActiveX Controls          | ENABLED           |

8. Click _OK_{:.doc-button}.
   The following message appears: Are you sure you want to change the settings for this zone?
9. Click _Yes_{:.doc-button}.
10. To close the dialog window, click _OK_{:.doc-button}.

## injixo client installation

injixo Classic and injixo Enterprise WFM contain ActiveX controls, which require {% link_new Microsoft Edge in IE mode | support/faq/configure-edge-internet-explorer-mode.md %} and the injixo client.

If you see an error message <!-- Add message after it has been changed in injixo? --> when logging in or within injixo:

- use a {% link_new compatible browser | getting-started/system-requirements.md | #browser-requirements %}.
- install the injixo client (as described below).

### Automatic client installation (WFM start page)

If you are using the above browser settings, the client installs itself automatically when WFM is entered.

1. Go to _WFM_{:.menu-item}.
2. Wait until the download has finished and the client installation starts.
3. The browser shows this message: This webpage wants to run the following add-on: 'injixo Enterprise' from 'InVision AG'.<br>If the prompt does not appear, ask your IT for help.
4. Click _Install_{:.doc-button} to install the required add-ons.
5. Click _Install_{:.doc-button} to install the client.

After successful installation, you can access ActiveX components.

### Manual client installation

Install the client manually, e.g. in injixo WFM Enterprise on-premise or when the automatic installation does not work.

Note: If you are using a software distribution tool, run the installer for the user who will be logged in to the computer later, e.g. using Microsoft's msiexec.exe with the runas /user option.

1. Download the [latest injixo client](https://downloads.injixo.com/en#client-components).
2. To run the MSI installer, click _Run_{:.doc-button}.
3. To continue, click _Next_{:.doc-button}.
4. (Optional) Edit the installation path.
5. If the computer is shared by several users, select **Everyone**.
6. To continue, click _Next_{:.doc-button}.
7. To start the installation, click _Install_{:.doc-button}.
   The following message appears: Do you want to allow the following program from an unknown publisher to make changes to this computer?
8. Click _Yes_{:.doc-button} to confirm the message.

After successful installation, you can access ActiveX components.
