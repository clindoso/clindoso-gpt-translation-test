---
title: Set up secure connections using TLS 1.2
description: Configure TLS 1.2 in your browser and operating system for a secure connection to injixo.
product_label:
  - advanced
  - enterprise
  - classic
redirect_from: /secured-connections/
redirect_reason: renamed file in August 2021
---

In this article, you will learn:

- how to activate secure connections in Microsoft Edge.
- how to configure your Windows operating system to use secure connections.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

The injixo services are accessible via internet browsers and use secure internet connections according to the Transport Layer Security (TLS) standard. Modern browsers use the secure TLS 1.2 standard by default. Currently, only TLS 1.2 is considered sufficiently secure.

Legacy injixo client components, such as the injixo client, the Reportserver, Xlink, or custom Ruby and .NET SDK applications, directly connect to the server using TLS 1.2, independent of your browser configuration. If you are using the injixo client, configure your Windows operating system accordingly.

## Configure TLS 1.2 in Microsoft Edge

1. Open the **Windows start menu**, type _internet options_, and press _Enter_.
2. Click the **Advanced** tab and scroll to the bottom.
3. Activate **Use TLS 1.2**.
4. Click _OK_{:.doc-button}.

{{ 1 | image: 'Internet Options Dialog', '50%' }}

## Windows TLS 1.2 Support

The following Windows versions include support for TLS 1.2:

- Windows 8, 8.1, 10, and 11
- Windows Server 2012 (R2), 2016, and 2019

In Windows 10, Windows Server 2016, 2019, and newer versions, TLS 1.2 is automatically activated. In earlier versions, you need to activate it manually.

Older Windows versions do not support TLS 1.2. Do not use these versions with injixo for security reasons. If you need support during an update, contact your customer success team.

## Configure TLS 1.2 in Windows

As Windows does not provide a built-in tool to configure and activate TLS 1.2, you need to use an external tool, such as [IIS Crypto 2.0](https://www.nartac.com/Products/IISCrypto).

If you are familiar with the Windows registry editor, you can also activate TLS 1.2 manually using regedit.exe:

1. Open **Regedit.exe** as Administrator.
2. Go to the path  
   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols`.
3. Right-click **Protocols**, select **New**, select **Key**. Create a new key named **TLS 1.2**. Skip this step is the key _TLS 1.2_ already exists.
4. Go to the new path `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2`.
5. Right-click **TLS 1.2**, select **New**, select **DWORD (32 bit) value**. Create a new entry **DisabledByDefault** with value **0**.
6. Right-click **TLS 1.2** again, select **New**, select **DWORD (32 bit) value**. Create another value **Enabled**.
7. To change the value for **Enabled** to **1**, double-click **Enabled**, selected **Adjust value to 1**, click **OK**.
8. Restart your computer.
