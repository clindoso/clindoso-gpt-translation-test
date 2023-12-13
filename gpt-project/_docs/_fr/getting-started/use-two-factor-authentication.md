---
title: Utiliser l’authentification à 2 facteurs (2FA)
product_label:
  - essential
  - advanced
  - enterprise
description: Apprenez à activer et désactiver l’authentification à 2 facteurs pour votre compte.
---

## Qu’est-ce que l’authentification à 2 facteurs&nbsp;?

L’authentification à 2 facteurs (2FA) ajoute un niveau de sécurité supplémentaire à vos comptes en ligne.  
Pour vous connecter à votre compte lorsque la 2FA est activée, vous avez besoin&nbsp;:

- de vos identifiants de connexion,
- d’un mot de passe supplémentaire, généré par un autre appareil.

> Pour plus de sécurité, activez la 2FA pour votre compte injixo dès que possible.

## Prérequis&nbsp;: installer une application d'authentification

injixo prend en charge les applications d'authentification répertoriées dans le tableau ci-dessous.  
Si vous utilisez un appareil Android, téléchargez l’une des applications sur le Google Play Store. Si vous utilisez un appareil Apple, téléchargez-la sur l’App Store Apple.

|-------|--------|---------|
| Google Authenticator | [App Store Apple](https://apps.apple.com/us/app/google-authenticator/id388497605) | [Google Play Store](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) |
| Microsoft Authenticator | [App Store Apple](https://apps.apple.com/us/app/microsoft-authenticator/id983156458) | [Google Play Store](https://play.google.com/store/apps/details?id=com.azure.authenticator) |
| Authy | [App Store Apple](https://apps.apple.com/us/app/authy/id494168017) | [Google Play Store](https://play.google.com/store/apps/details?id=com.authy.authy) |

## Activer la 2FA pour votre compte

Pour activer la 2FA pour votre compte, vous avez besoin d'accéder à un appareil principal (par exemple, un ordinateur) et à votre appareil personnel.  
Sur votre ordinateur ou appareil principal, procédez comme suit&nbsp;:

1. Connectez-vous à injixo et cliquez sur votre **nom d’utilisateur** en haut à droite de la barre de navigation.
2. Cliquez sur l’onglet **Sécurité**. En haut de la page, vous pouvez voir l’état actuel de vos paramètres de 2FA.
3. Cliquez sur _Activer la 2FA_{:.doc-button}.
4. Saisissez votre mot de passe.
5. Cliquez sur _Continuer_{:.doc-button}.  
   La page Activer l'authentification à 2 facteurs s'ouvre. Elle indique les étapes que vous devez suivre ensuite.

Sur votre appareil personnel, suivez les étapes indiquées sur la page Activer l’authentification à 2 facteurs&nbsp;:

1. Installez l’une des [applications d’authentification prises en charge](#prérequis-installer-une-application-dauthentification).
2. Ouvrez l’**application d’authentification** sur votre appareil et ajoutez une nouvelle entrée pour injixo.  
   Pour ce faire, choisissez l'une des options suivantes&nbsp;:
   - Scannez le **code QR** sur la page Activer l'authentification à 2 facteurs, avec l'application d'authentification.
   - Saisissez la **clé** affichée sur la page Activer l'authentification à 2 facteurs, dans l'application d'authentification.
Votre application d’authentification est maintenant configurée et commence à générer des mots de passe à usage unique (OTP).

Sur votre ordinateur ou appareil principal, procédez comme suit&nbsp;:

1. Sur la page d'activation de la 2FA, entrez un OTP dans le champ **Mot de passe à usage unique**.
2. Cliquez sur _Continuer_{:.doc-button}.
3. Conservez les codes de secours ou téléchargez-les sous forme de fichier. Cliquez sur _Télécharger_{:.doc-button} ou _Copier_{:.doc-button}. Si vous ne voyez pas les codes de secours, ils ont été désactivés pour le compte de votre entreprise. <!-- feature flag -->

   > Conservez vos codes de secours dans un endroit sûr.
   >
   > Si vous perdez l'accès à votre appareil personnel, vous ne pourrez accéder à votre compte qu'en utilisant un code de secours.<br>Conservez vos codes de secours en toute sécurité, par exemple dans un gestionnaire de mots de passe, ou imprimez-les et assurez-vous que vous seul pouvez y accéder.

4. Cochez la case **J’ai sauvegardé mes codes de secours**.
5. Cliquez sur _Activer la 2FA_{:.doc-button}.  
   Vous recevrez un e-mail vous informant de la désactivation de la 2FA.  
À partir de maintenant, vous aurez besoin à la fois de vos identifiants de connexion et d'un OTP pour vous connecter à injixo.

## Se connecter lorsque la 2FA est activée

1. Entrez votre **adresse e-mail** et votre **mot de passe** sur l’écran de connexion d’injixo et cliquez sur _Se connecter_{:.doc-button}.  
2. Entrez l’**OTP** généré par votre application d'authentification.  
   Chaque OTP est valide pendant seulement 30 secondes, puis l'application en génère un nouveau.
3. Cliquez sur _Vérifier_{:.doc-button} pour terminer le processus de connexion.

Si vous ne pouvez pas vous connecter, vérifiez sur votre application d'authentification que le code OTP que vous avez saisi est toujours valide. Si ce n'est pas le cas, entrez simplement un nouvel OTP.  
Si vous ne pouvez toujours pas vous connecter, suivez les instructions ci-dessous pour vous connecter avec un code de secours.

### Se connecter à l’aide d’un code de secours

Lors de la configuration de la 2FA pour votre compte, vous recevez 10 codes de secours. Si vous n'avez pas accès à votre appareil personnel, vous pouvez vous connecter à injixo en utilisant l'un de vos codes de secours.

> Remarque
>
> Connectez-vous uniquement avec un code de secours en cas d’urgence. Vous ne pouvez utiliser chaque code de secours qu’une seule fois. Par défaut, vous devez toujours vous connecter à l’aide d’un OTP.

Pour vous connecter avec un code de secours au lieu d’un OTP, suivez ces étapes&nbsp;:

1. Entrez votre **adresse e-mail** et votre **mot de passe** sur l’écran de connexion d’injixo et cliquez sur _Connexion_{:.doc-button}.
2. Cliquez sur le lien **Code de secours** situé en dessous du champ du mot de passe à usage unique.
3. Saisissez l’un de vos codes de secours à 10 caractères dans le champ **Code de secours**.
4. Cliquez sur _Vérifier_{:.doc-button} pour terminer le processus de connexion.

<!-- a tag required. configured name used in injixo UI link -->

### Se connecter sans appareil personnel ni codes de secours

Si vous ne pouvez pas vous connecter avec la 2FA et que vous ne pouvez pas accéder à vos codes de secours, contactez un utilisateur disposant d'un accès administrateur. Il pourra désactiver la 2FA pour votre compte. Vous pourrez ensuite vous connecter à votre compte sans OTP et réinitialiser vos paramètres de 2FA.

## Utiliser la 2FA sur un nouvel appareil personnel

Pour utiliser un autre appareil pour la génération OTP, vous devez temporairement désactiver la double authentification pour votre compte et la [réactiver en utilisant votre nouvel appareil](#activer-la-2fa-pour-votre-compte).

Si vous ne pouvez pas désactiver la 2FA vous-même, demandez à un utilisateur disposant d’un accès administrateur de la désactiver pour votre compte.

## Désactiver la 2FA pour votre compte

> Remarque
>
> Il n’est pas recommandé de désactiver la 2FA. Si la 2FA a été rendue obligatoire sur votre compte, vous ne pouvez pas la désactiver.

1. Connectez-vous à injixo et cliquez sur **votre nom** en haut à droite de la barre de navigation.
2. Cliquez sur l’onglet **Sécurité**. En haut de la page, vous pouvez voir l’état actuel de vos paramètres de 2FA.
3. Cliquez sur _Désactiver la 2FA_{:.doc-button}.
4. Saisissez votre **mot de passe**.
5. Cliquez sur _Continuer_{:.doc-button} pour confirmer la désactivation.

Vous recevrez un e-mail vous informant de la désactivation de la 2FA. Vous pouvez maintenant vous reconnecter sans OTP.

> Vous avez reçu l’e-mail de désactivation de la 2FA sans l’avoir désactivée vous-même&nbsp;?
>
> Vérifiez votre compte avec un administrateur de votre entreprise. Pensez à changer votre mot de passe.
