---
title: Notifications
product_label:
  - advanced
  - enterprise
description: Découvrez comment injixo gère les notifications et comment les configurer.
redirect_from: /fr/push-notifications/
redirect_reason: used in injixo UI and mailing
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-notify-scheduling-changes.md
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md
---

injixo peut envoyer des notifications par e-mail et des notifications push sur navigateur.

Par défaut, injixo envoie des notifications pour informer les employés des événements du processus de planification&nbsp;:

- publication de plannings,
- modification des plannings,
- demandes d’échanges de journées.

Les notifications par e-mail sont envoyées à l’adresse de connexion de chaque employé. Les notifications push du navigateur apparaissent sous forme de notifications pop-up cliquables si vous êtes connecté à injixo dans au moins un onglet du navigateur. En cliquant sur une notification, injixo s’affichera dans votre navigateur.

## Configurer les notifications

Les utilisateurs disposant d’un accès admin peuvent désactiver certaines notifications&nbsp;:

1. Accédez à _Account > Notifications_{:.breadcrumbs}.
2. Cliquez sur un onglet pour changer de catégorie de notification.  
   > Remarque
   > 
   > Si vous désactivez les notifications par e-mail pour Me, les employés ne pourront pas inviter leurs collègues à échanger des journées dans injixo Me.
3. Cochez ou décochez les cases **E-mail** ou **Navigateur** selon vos préférences.

Les paramètres de notification sont sauvegardés automatiquement. Les paramètres sélectionnés affectent tous les utilisateurs.

## Autoriser les notifications push sur navigateur

Si les notifications ne sont pas déjà configurées via des stratégies de groupe dans le système d’exploitation, les utilisateurs individuels peuvent les activer pour le navigateur actuel dans leur profil utilisateur&nbsp;:

1. Cliquez sur votre **nom d’utilisateur** en haut à droite pour ouvrir votre profil utilisateur.
2. Dans la section **Notifications**, cliquez sur _Autoriser les notifications d’injixo_{:.doc-button}.
3. Une fenêtre pop-up s’ouvre dans votre navigateur. Elle vous permet d’autoriser les notifications push sur votre navigateur.

## Résolution des problèmes relatifs aux notifications push sur navigateur

Les notifications push sur navigateur sont envoyées par le navigateur et le système d’exploitation, et les deux doivent être autorisés à envoyer des notifications. Les modes Ne pas déranger et de concentration (par exemple, le réveil et les priorités) peuvent vous empêcher de recevoir des notifications. Veuillez également vous assurer que votre navigateur est à jour. Videz le cache du navigateur et les supprimez les cookies si nécessaire.

Pour résoudre les problèmes liés aux notifications sur différents navigateurs et systèmes d’exploitation, consultez les liens suivants&nbsp;:

- Chrome&nbsp;: [Aide Google Chrome](https://support.google.com/chrome/answer/3220216?hl=fr),
- Firefox&nbsp;: [Mozilla Firefox Assistance](https://support.mozilla.org/fr/kb/notifications-web-push-firefox),
- Safari&nbsp;: [Guide d’utilisation de Safari](https://support.apple.com/fr-fr/guide/safari/sfri40734/15.1/mac/12.0),
- Windows&nbsp;: [Support technique Microsoft Windows](https://support.microsoft.com/fr-fr/windows/modifier-les-param%C3%A8tres-de-notification-dans-windows-8942c744-6198-fe56-4639-34320cf9444e#WindowsVersion=Windows_10),
- Android&nbsp;: [Aide Android](https://support.google.com/android/answer/9079661?hl=fr),
- Mac&nbsp;: [Assistance Apple macOS](https://support.apple.com/fr-fr/guide/mac-help/mchl2fb1258f/mac),
- iOS&nbsp;: [Assistance Apple iOS](https://support.apple.com/fr-fr/HT201925).

## Tester les notifications push sur navigateur

Pour vérifier si les notifications push sur navigateur fonctionnent sur votre appareil et le navigateur de votre choix,
accédez à <https://www.bennish.net/web-notifications.html/>.
