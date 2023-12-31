---
title: Use two-factor authentication (2FA)
product_label:
  - essential
  - advanced
  - enterprise
description: Learn how to activate and deactivate two-factor authentication for your account.
---

## What is two-factor authentication?

Two-factor authentication (2FA) adds a layer of security to your online accounts.  
To log in to your account when 2FA is active, you need:
- your login credentials
- an extra password, generated by a different device

> Activate 2FA for your injixo account as soon as possible to increase security.

## Prerequisite: install an authenticator app

injixo supports the authenticator apps listed in the table below.  
If you are using an Android device, download one of the apps from the Google Play Store. If you are using an Apple device, download it from the Apple App Store.

|-------|--------|---------|
| Google Authenticator | [Apple App Store](https://apps.apple.com/us/app/google-authenticator/id388497605) | [Google Play Store](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) |
| Microsoft Authenticator | [Apple App Store](https://apps.apple.com/us/app/microsoft-authenticator/id983156458) | [Google Play Store](https://play.google.com/store/apps/details?id=com.azure.authenticator) |
| Authy | [Apple App Store](https://apps.apple.com/us/app/authy/id494168017) | [Google Play Store](https://play.google.com/store/apps/details?id=com.authy.authy) |

## Activate 2FA for your account

To activate 2FA for your account, you need access to a main device (e.g. a computer) and to your personal device.  
On your computer or main device, proceed as follows:

1. Log in to injixo and click your user name at the top right in the navigation bar.
2. Click the **Security** tab.
3. Click _Activate 2FA_{:.doc-button}.
4. Enter your password.
5. Click _Continue_{:.doc-button}.  
   The **Activate two-factor authentication** page opens. It lists the steps you need to follow next.

On your personal device, follow the steps listed on the Activate two-factor authentication page:

1. Install one of the [supported authenticator apps](#prerequisite-install-an-authenticator-app).
2. Open the authenticator app on your device, and add a new entry for injixo.  
   To do this, choose one of the following options:
   - Scan the QR code on the **Activate two-factor authentication** page with the authenticator app.
   - Enter the key displayed on the **Activate two-factor authentication** page into the authenticator app.  
Your authenticator app is now set up and starts generating one-time passwords (OTP).

On your computer or main device, proceed as follows:

1. On the **Activate two-factor authentication** page, enter an OTP into the **One-time password** field.
2. Click _Continue_{:.doc-button}.
3. Store the backup codes or download them as a file. Click _Download_{:.doc-button} or _Copy_{:.doc-button}. If you don't see the backup codes, they have been deactivated for your company account. <!-- feature flag -->

   > Store your backup codes in a safe place
   >
   > If you lose access to your personal device, you will only be able to access your account by using a backup code.<br>Store your backup codes safely, e.g. in a password manager, or print them out and make sure only you can access them.

4. Check the checkbox **I securely stored my backup codes.**
5. Click _Activate 2FA_{:.doc-button}.  
   You will receive an email that informs you about the 2FA activation.  
From now on, you will need both your login credentials and an OTP to log in to injixo.

## Log in when 2FA is active

1. Enter your email address and password on the injixo login screen and click _Login_{:.doc-button}.  
2. Enter the OTP generated by your authenticator app.  
   Each OTP is valid for 30 seconds only, then the app generates a new one.
3. Click _Verify_{:.doc-button} to complete the login process.

If you cannot login, check on your authenticator app that the OTP you entered is still valid. If this is not the case, simply enter a new OTP.  
If you still cannot log in, follow the instructions below to log in with a backup code.

### Log in with a backup code

During the 2FA setup for your account, you receive 10 backup codes. If you don't have access to your personal device, you can log in to injixo using one of your backup codes.

> Note
>
> Only log in with a backup code in case of an emergency. You can use each backup code only once. By default, you should always log in using an OTP.

To log in with a backup code instead of an OTP, proceed as follows:

1. Enter your email address and password on the injixo login screen and click _Login_{:.doc-button}.
2. Click the backup code link below the **One-time password** field.
3. Enter one of your 10-character backup codes in the **Backup code** field.
4. Click _Verify_{:.doc-button} to complete the login process.

<!-- a tag required. configured name used in injixo UI link -->

### Log in without your personal device and backup codes

If you are not able to log in with 2FA and you cannot access your backup codes, reach out to a user with admin access. They can deactivate 2FA for your account. You will then be able to log in to your account without an OTP and reset your 2FA settings.

## Use 2FA on a new personal device

To use a different device to generate OTPs, you need to temporarily deactivate 2FA for your account and [activate it again using your new device](#activate-2fa-for-your-account).

If you cannot deactivate 2FA yourself, ask a user with admin access to deactivate it for your account.

## Deactivate 2FA for your account

> Note
>
> Deactivating 2FA is not recommended. If 2FA has been enforced on your account, you cannot deactivate it.

1. Log in to injixo and click your user name at the top right in the navigation bar.
2. Click the **Security** tab.  
   At the top of the page, you can see the current status of your 2FA settings.
3. Click _Deactivate 2FA_{:.doc-button}.
4. Enter your password.
5. Click _Continue_{:.doc-button} to confirm the deactivation.

You will receive an email that informs you about the 2FA deactivation. From now on, you can log in again without using an OTP.

> Did you receive the 2FA deactivation email without deactivating 2FA yourself?
>
> Check your account together with an admin from your company. Consider changing your password.
