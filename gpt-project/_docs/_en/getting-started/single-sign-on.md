---
title: Single sign-on (SSO)
product_label:
  - advanced
  - enterprise
description: Learn how to set up and use SSO in injixo.
---

SSO is an authentication mechanism that allows users to log in to multiple applications and websites with just one set of credentials. A trust relationship is set up between a central identity management service (identity provider/IdP) and an application (service provider/SP), in this case injixo.

The IdP is a third-party product, such as OneLogin, Microsoft Azure AD, Okta, or Google. Using SSO means that your organization will benefit from aligned security policies, such as two-factor authentication and password rotation. Users authenticate against the IdP that redirects to injixo.

The IdP setup has been tested with the above IdPs. If you cannot integrate your specific IdP, contact us.

## Requirements

The following requirements must be met in order to integrate injixo into the IdP of choice:

- SAML 2.0 protocol support
- Federation metadata URL access via web
- The email address registered in injixo and your IdP must be connected to a mailbox

> To improve security, activate encrypted assertions/token encryption (strongly recommended).

## Activate SSO for your account

Only users with admin access can activate SSO.

1. Register injixo as a new SAML or SSO application in your IdP.  
   You can download [this injixo logo](/assets/img/common/injixo-logo.png) to add it to the web application page.

2. In injixo, go to _Account > Security_{:.breadcrumbs} and configure SSO under **Single Sign-On**.

3. In the **injixo SAML Metadata** section you have two options, depending on whether your IdP supports file uploads:

   - File uploads supported: Click _{% icon download | icon-only %} Download_{:.doc-button} and complete the IdP configuration with the downloaded XML file.
   - File uploads not supported: Click **Service Provider details** and add the displayed URLs to your IdP configuration.

4. (Optional) If you use encrypted SAML assertions, click _{% icon download | icon-only %} Download_{:.doc-button} in the **Token Encryption** section. Add the downloaded certificates to your IdP configuration.
5. Depending on whether your IdP provides an URL for federation metadata, finish the configuration as follows:

   - IdP provides federation metadata URL: Copy your federation metadata URL for the registered application from your IdP. Paste the URL into the **Federation Metadata URL** field in the **Identity Provider** section.
   - IdP does not provide federation metadata URL: Download the Federation Metadata XML file and host it yourself. As an example, learn how to set up your own custom [SAML application with Google](https://support.google.com/a/answer/6087519?hl=en).

6. Click _Save configuration_{:.doc-button}.  
   SSO is now active but all users can still log in with their username and password.

> To ensure an even higher level of security, you can [enforce SSO for all users](#enforce-sso-for-all-users).

## Test the SSO configuration

Click _Test configuration_{:.doc-button} to test the login through the IdP. The IdP generates a SAML response that is sent to injixo. You are redirected to your IdP's login page, where you enter the IdP credentials. If the IdP configuration is correct and the authentication process is successful, you will be logged in to injixo.

{{ 4 | image: 'Successfully testing the SSO configuration for the current user', '80%' }}

<!-- A valid SubjectConfirmation was not found on this Response in our internal server logs -->

The SAML response from the IdP contains the authenticated user's assertion with attributes and profile information. If the process was not successful and you see an error message, check the application configuration, the user configuration, and the Recipient, InResponseTo, NotBefore, and NotOnOrAfter attributes set in the IdP. 

You can debug the SubjectConfirmation XML element in the SAML response in your browser's dev tools or in external SAML tools. To see the unencrypted response in plain text, deactivate encrypted assertions.

Example for the SubjectConfirmation XML element in a SAML response:

```
<saml:Subject>
    <saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">email@company.org</saml:NameID>
    <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
        <saml:SubjectConfirmationData NotOnOrAfter="2022-08-11T08:25:25Z"
            Recipient="https://www.injixo.com/sso/saml/acs"
            InResponseTo="_abcdefgh-0444-4567-abcd-abcdabcdabcd"
    />
    </saml:SubjectConfirmation>
</saml:Subject>
```

## Enforce SSO for all users

To test whether the configuration has been successful, you can deactivate all logins with username and password by enforcing SSO for all users. However, you need to make sure that:

- all injixo users exist in the IdP and in injixo.
- the injixo email matches the appropriate IdP identifier.
- all injixo users are assigned to the IdP injixo SSO application.

Once SSO is enforced, it is no longer possible to:

- login using username and password (all existing passwords will be invalidated).
- reset passwords inside injixo (neither by user nor by admin).
- manage access to injixo outside the IdP.

Enforce SSO in the **3. Enforcement** section. The button _Enforce_{:.doc-button} is selectable after you have tested your SSO configuration successfully.

{{ 5 | image: 'Button to enforce SSO for all users', '80%' }}

## Change email addresses when SSO is enforced

When you enforce SSO, users cannot change their email addresses themselves because the injixo email address needs to match the appropriate IdP identifier.

Only admin users can change email addresses in injixo.

## Log in using SSO

When SSO is set up, your users can log in via [https://www.injixo.com/login/sso](https://www.injixo.com/login/sso). They need to enter their email address and are redirected to the IdP's login screen. If users are already logged in, they will be automatically redirected back to injixo. Otherwise, they need to enter the IdP password.

## Revoke access to injixo

To revoke a user's access to injixo via SSO, you must delete the injixo user assignment in the IdP. Note: If the user still exists in injixo, they will still be billed. To avoid costs, you must also {% link_new deactivate or remove the user | features/administration/deactivate-employees.md %}.

## Deactivate SSO

To deactivate SSO and allow logins with username and password again, users with admin access can deactivate SSO. This will delete the IdP connection and all entered configuration details. After SSO has been deactivated, all active users receive an email to set a new injixo password. Afterwards, logging in with user name and password via [https://www.injixo.com/login](https://www.injixo.com/login) is possible again.
