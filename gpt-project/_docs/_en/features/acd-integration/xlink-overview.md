---
title: Xlink overview
promote-service: acd-integration-support
product_label:
  - on-premise
description: Use the Xlink application to import data into injixo. Learn how to install and configure it.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-installation-configuration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-import-mode.md
---

The Xlink application imports data from third-party systems such as telephone systems (ACD). The _Xlink Suite_{:.menu-item} is available for download at [downloads.injixo.com](https://downloads.injixo.com).

Xlink imports two different types of data:

- call or contact data into queues (**PhoneLink**)
- employee-related login/logout/status change data (**TimeLink**)

<div markdown="1" class="hint-box-default hint-box-red">

Xlink integration is outdated

If you are currently using Xlink in your injixo Cloud WFM plan, please update it immediately to injixo Cloud Link, or a solution that meets the latest integration standards. Ask our Customer Experience experts for support [here](https://www.injixo.com/contact/?message_type=support-enquiry&message=Please%20help%20me%20to%20update%20my%20integration.%20I%20understand%20this%20is%20required%20to%20ensure%20continuous%20data%20import%20to%20injixo%20after%20January%2030,%202023.).

</div>

Note: To import data into workloads, use a {% link_new native integration | features/acd-integration/cloud/how-integrations-work.md %} as an alternative, which is easier to configure. If your ACD is not listed, use Xlink and let your Customer Success Manager know that your specific ACD is not supported yet.

## Technical requirements

- Operating system : Windows Server 2012/Windows 7 (or higher)
- CPU : 2 cores \@2,2GHz (or higher)
- RAM: 2 GB (excluding operating system)
- Hard disk: 20 GB hard disk (excluding operating system)

Note: XLink can be deployed on a virtualized environment.

### ISPS Xlink Windows service (isps_uls.exe)

Xlink uses a Windows service for data import. The service named _ISPS XLink_ always imports all data of a whole day. The service can be installed only once on the same computer and starts automatically after installation.

Type **isps_uls.exe** in the Windows command line to see the available parameters:

- _-install_/_-remove_: installs or uninstalls the _ISPS XLink_ service. During installation, the _startup type_ parameter defaults to _automatic_ to ensure a service restart after a server restart.
- _-console_: starts the service in console mode. This mode uses the user account associated with the Windows session. You can use this option to identify configuration problems.

Note: After installation, the Windows service uses the logon option _Local System Account_ (tab _Login as_) by default. Configure an administrator account if no values are imported despite correct configuration or Xlink cannot access the import folder.

Read the article {% link_new Install and configure Xlink | features/acd-integration/xlink-installation-configuration.md %} for detailed installation instructions.

## XLink user interface (isps_ul.exe)

Xlink has a user interface where you can configure settings, {% link_new create/modify PhoneLink mappings | features/acd-integration/xlink-mapping-telephony.md %} or {% link_new configure/manually start data import | features/acd-integration/xlink-import-mode.md %}.

Note: The user interface defaults to English. To change this, copy the two files from your preferred language sub folders into the installation directory. Overwrite the existing files.

Run the file **isps_ul.exe** to start the user interface.

{{ 1 | image: 'Xlink Interface'}}

The Xlink user interface consists of three areas:

1. _Interface_: External systems created under _WFM_{:.menu-item}.
2. _iWFM Queues_: Created queues and assigned value types from your injixo tenant.
3. _Assigned Valuetypes_: Mappings for the selected queue. No entries if no mappings exist.

## Backup configuration and mappings

To restore the Xlink configuration after a Xlink reinstallation (in case of data loss), periodically back up the following files:

- isps_ul.ini
- acd_map.ini
- isps.cfg
- \*.bas
