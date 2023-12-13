---
title: Resolve login error messages 256905 and 256907
toc: false
description: Resolve various error messages that may appear during login.
product_label:
  - on-premise
---

When logging in to **injixo Enterprise on-premise**, various error messages may appear. These are usually prefixed with the error number '256907' and an additional error code.

> If you see the error message '256905-' during login, update your client first.

The error message **The client has not been correctly installed. Number 256907-100** can appear for a variety of reasons.

- Have you successfully run the file _regdll.bat_ included in the client folder? The client registration must be executed in the context of the currently logged in Windows user. If the client is automatically deployed, run the batch file at Windows startup, e.g. with a logon-script, to register the client in the user context.

- Are you using Internet Explorer in 32-Bit mode?

- In Internet Options, check if your browser is allowed to download and execute ActiveX-elements. Further information can be found in the {% link_new system requirements | getting-started/system-requirements.md %} article. The currently loaded add-ons in the Internet Explorer should contain one or two add-ons from InVision. Make sure to add the server address to your trusted sites.

- It may be that certain Class IDs (CLSIDs) are blocked. Check your [Windows Group Policies](https://docs.microsoft.com/en-us/internet-explorer/ie11-deploy-guide/enable-and-disable-add-ons-using-administrative-templates-and-group-policy).

If you have tried everything above and the issue is not resolved, {% link_new create a ticket | support/create-ticket.md %}.

All other potential error messages are listed below, most of which are self-explanatory. Further explanations have been added in parentheses.

| Error Number | Message                                                                                                                                                                                                                                              |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 256907-3     | Access to the server has been denied. Your login details (user name, password) are incorrect. Ensure that you use the correct upper and lower case making your entries.                                                                              |
| 256907-4     | You are already logged into another computer. Log off the other computer first before you log in again. (This will only appear if the option to restrict logins from multiple computers is activated.)                                               |
| 256907-5     | The Enterprise server has not been started. Wait until the server is started before logging in.                                                                                                                                                      |
| 256907-6     | The Enterprise server could not be found. Contact your system administrator. (The URL parameter in isps.cfg does not contain the correct IP address)                                                                                                 |
| 256907-7     | The server connection aborted. The reason for this error are mostly network problems. Contact your system administrator.                                                                                                                             |
| 256907-8     | You cannot login at the moment because all of the licenses are being used. Try again later.                                                                                                                                                          |
| 256907-9     | Your account is deactivated. Contact your system administrator. (Administrators can check the login checkbox for the user again. If you are the only Admin, restart the service.)                                                                    |
| 256907-10    | The single login has failed. Logging in without entering the user name and password is not possible. The single login functionality is either deactivated completely or just for your domain. Please log in again using your user name and password. |
| 256907-11    | You are attempting to log in with a client which is not compatible with the server version. Either your client is not up to date or it has not been correctly installed. Contact your system administrator.                                          |
| 256907-12    | Your session has expired. The client login failed. Please log in again with your user name and password.                                                                                                                                             |
