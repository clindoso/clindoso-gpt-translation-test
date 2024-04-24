---
title: Update from versions earlier than 2012.3
redirect_from:
  - /update-old-versions/
  - /which-version-am-i-using/
redirect_reason: file removed September 2020
product_label:
  - on-premise
description: Learn how to update your injixo Enterprise on-premise server to the latest version if you are currently on a version earlier than 2012.3
---

This article explains how to update the injixo Enterprise Server from an old version (r4.306 and below or build 9628 and below) to the latest version. There are a few one-time steps required; your next update will be much easier. Read here about {% link_new new versions | support/injixo-enterprise-on-premise/update-new-versions.md %}.

## Check the current Version Number

To start the server after the update you will need a new license key if the currently used version is older than 2012.3. Contact your Customer Success Manager.

If you are using a build > 9159, you will find the build number in the top right corner of injixo Enterprise after logging in. Otherwise, you need to navigate to the injixo Enterprise installation directory. It contains either a file called _version.yaml_ (InVision WFM-build) or _serinf.txt_ (Version/PackageNo).

Install the license as follows:

1. Copy the new license file into the injixo Enterprise installation directory.
2. Rename the file to _license.cfg_ after copying.

## Update Preparation

Download the current [injixo Enterprise on-premise version](https://downloads.injixo.com/en#server-on-premise).

> Important: Unicode Required
>
> The current injixo version uses Unicode (utf-16) as database encoding.  
> Check the current encoding with this database query:  
> `SELECT vs_version_no, encoding FROM vs_version;`  
> If the result is **not utf-16**, a {% link_new data conversion from ANSI to Unicode | support/injixo-enterprise-on-premise/unicode-migration.md %} is required.

This article uses the term **injixo Enterprise installation directory**. The files can be installed in a custom location, the default path is `C:\Program Files\injixo Enterprise\WFM\Server`. The best option to find the right folder is to check the Windows service named _injixo Enterprise WFM_ or _InVision Enterprise WFM_; there you find _Path to Executable_ on the _General_ tab.

Then prepare the update as follows:

1. Create a backup of your database and your installation before you begin.
2. Stop the service _InVision Enterprise WFM_.
3. Stop the service _InVision Enterprise WFM AutoScheduler_ (if installed).
4. Open a Windows Command Line (cmd) and navigate into the injixo Enterprise installation directory.
5. Delete the _InVision Enterprise WFM_ service by running: `sc delete "InVision Enterprise WFM"`.

## Remove old Files

- Delete the folder `auxiliary\calendar`. The update contains a new calendar folder.
- Delete the files _ivDc64.ivm_ and _ivCamp64.ivm_. These were used for modules which are no longer available.
- Remove all dll files from the folder `handler`, such as _eMemory64.dll_ or _eClient32.dll_. Keep only the files whose filename starts with _ijp_ and ends with _exe_, e.g. _ijp_aae.exe_.

## Microsoft VC Redist 2010 (64-Bit)

Install the [Microsoft Visual C++ 2010 Redistributable Package (x64)](https://www.microsoft.com/en-us/download/details.aspx?id=26999) on the server; if you have components installed on different servers, you will need to install the package on all of them. If the package is not installed, error messages will be displayed when starting the components, e.g. in `ies64.log` regarding the file `msvcr100.dll`.

## Edit the existing Database Connection

New versions use a new parameter _DBConnectString_ for the database connection. This replaces the _DBServerName_ parameter. Skip this step if the parameter _DBConnectString_ is already configured.

Adjust the configuration as follows:

1. Open _isps.cfg_ in the injixo Enterprise installation directory.
2. Add one of the following examples to the existing **[InVision General Model Settings]** section below the already existing parameter _DBConnectString_:

   - Microsoft SQL

     ```
     DBConnectString = "Driver={SQL Server};
     SERVER=<Server Address>\<Instance Name>;DATABASE=<DB Schema Name>;UID=<User Name>;PWD=<Password>"
     ```

   - Oracle

     ```
     ;admin client
     DBConnectString = "DRIVER={Oracle in <Driver Name>};DBQ=<Oracle Alias>;UID=<User Name>;PWD=<Password>;FWC=T;EXC=T;LOB=T;"
     ```

     ```
     ;oracle instant client
     DBConnectString	= "DRIVER=(Oracle in XEClient);<User Name>/<Password>@Host:Port/<TNS Name>"
     ```

   - PostgreSQL
     ```
     DBConnectString = "Driver={PostgreSQL Unicode};Server=<Server Address>;Port=5432;Database=<DB Schema Name>;Uid=<User Name>;Pwd=<Password>;Encoding=UNICODE;TextAsLongVarchar=1;MaxLongVarcharSize=65536"
     ```

3. Replace the placeholders (`<>`) with the details for the existing database connection entries in the parameter _DBConnectString_.

4. Make sure that only one _[InVision General Model Settings]_ section exists in the file. Remove additional occurrences or use an _X_ inside the brackets to comment it out.

The final section might look like this:

```
[InVision General Model Settings]
DBServerName = "Driver={SQL Server};
SERVER=myserver\test;DATABASE=iwfm;UID=sa;PWD=mypassword"
DBConnectString = "Driver={SQL Server};
SERVER=myserver\test;DATABASE=iwfm;UID=sa;PWD=mypassword"
```

## Database Version Update

Check the database version with the following query: `select vs_version_no from vs_version;`

New versions require at least database version _20122001_ or _20130001_. If your database version matches, no further steps are required. If you have an older version, contact your Customer Success team. <!-- Old scripts required, mss_113_114.sql or ora_113_114.sql, next run consist64.exe /update -->

## Customize Email Server Settings

The email settings are no longer made via the injixo Enterprise interface; settings _48105_{:.id-label} and _48106_{:.id-label} are no longer taken into account. Please add the following paragraph to the `isps.cfg` and configure the SMTP parameters.

If the section with `ShortName = ivemail` is already configured in `isps.cfg` by a previous update, you can skip this step. Otherwise add the following paragraph and configure the parameters for sending e-mails:

    ```
    [22bafe6c-fc65-44a4-aeb6-b60281e0b2fc]
    ShortName = ivemail
    SMTPServer = smtp.yourprovider.com
    SMTPPort = 465
    SMTPTimeout = 60
    SMTPFromEmail = YourValidSenderMailAdress@yourprovider.com
    SMTPSecureMode = TLS
    SMTPUser = YourValid
    SMTPUser@yourprovider.com
    SMTPPwd = yourpassword
    SMTPTag = "Your custom topic"
    ```

Permitted values for the **SMTPSecureMode** parameter are SSL, PLAIN, and TLS. **SMTPTag** is optional to add a prefix to the subject of your emails sent from your injixo Enterprise Server, e.g. _Your custom topic_{:.menu-item}.

Test the new configuration by sending a report via e-mail after the update. If there is an error, the error message will be displayed in the report.

### Self managed certificate

If you are using a certificate for sending e-mails, you must add your certificate to the file `certificates\cacert.pem`.

However, the file `certificates\cacert.pem` will be overwritten with every future server update, so you will have to edit the file each time. Activate write protection for the file to be reminded when unpacking a new package. Alternatively, you can save the edited file away and copy it back into the `certificates` folder after the update.

## Extract new Files

If your version was already a 64-bit version, unpack the already downloaded archive in the injixo Enterprise installation directory. Overwrite any existing files.

> Update of an InVision WFM 32-bit version
>
> Do you have `ies.exe` and `ivtaskwd.ivm` instead of `ies64.exe` and `ivtaskwd64.ivm` in your injixo Enterprise installation directory? Then you are using a 32-bit version of injixo Enterprise. The update requires a new installation folder, and the installation of a new 64-bit Oracle database client may be required. The original \*.cfg files need to be transferred from the old to the new injixo Enterprise installation directory. In addition, the file named `esystem.dat` must be copied over and then renamed to esystem64.dat.

## Service Installation and Start

If necessary, rename the folder _InVision Enterprise WFM_ to _injixo Enterprise WFM_ before installing the service.

Install the new Windows service as follows:

1. Open a Windows command line.
2. Navigate to the _injixo Enterprise WFM_ directory.
3. Execute the command `isps_r464.exe --install --name "injixo Enterprise WFM" --fullname "injixo Enterprise WFM"`.
4. Restart the service and any other services stopped at the beginning of the installation to complete the update.

## Your next update

Plan [your next, much easier update](/update-new-versions) now to benefit from the latest software updates.
