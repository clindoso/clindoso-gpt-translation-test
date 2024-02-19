---
title: Gérer la 2FA
product_label:
  - essential
  - advanced
  - enterprise
description: Découvrez comment activer et désactiver la 2FA pour les comptes utilisateur de vos employés.
redirect_from:
  - /fr/2fa/
redirect_reason: Updated filename on 14 July 2023
---

> Seuls les utilisateurs ayant un accès admin peuvent gérer l'authentification à deux facteurs (2FA) pour les autres utilisateurs.

## Voir les paramètres de la 2FA des autres utilisateurs

Pour voir le statut de la 2FA des autres utilisateurs, suivez ces étapes&nbsp;:
1. Accédez à _Account > Utilisateurs_{:.breadcrumbs}.
2. Dans la colonne **2FA** à droite, une icône en forme de bouclier indique le statut de la 2FA pour chaque utilisateur. Faites passer votre curseur dessus pour voir plus d’informations.
  - Icône rouge {% icon 2FA-red | icon-only %}&nbsp;: la 2FA n'est pas active.
  - Icône orange avec point d'exclamation {% icon 2FA-orange | icon-only %}&nbsp;: la 2FA a été rendue obligatoire pour l’utilisateur. L'utilisateur doit activer la 2FA lors de sa prochaine connexion.
  - Icône orange avec coche {% icon 2FA-orange | icon-only %}&nbsp;: la 2FA est active. L'utilisateur a activé la 2FA lui-même.
  - Icône verte avec coche {% icon 2FA-green | icon-only %}&nbsp;: la 2FA est active. La 2FA a été rendue obligatoire.
## Rendre obligatoire l’activation de la 2FA pour les autres utilisateurs  
Vous pouvez demander aux autres utilisateurs d'activer la 2FA. L'activation de la 2FA pour les autres utilisateurs entraîne les conséquences suivantes&nbsp;:

- Les utilisateurs ne pourront pas se connecter s'ils n'activent pas la 2FA.
- Les utilisateurs ne pourront plus désactiver la 2FA pour leurs comptes personnels.

Avant de rendre obligatoire la 2FA pour les autres utilisateurs, assurez-vous qu'ils aient accès à l'une des {% link_new applications d'authentification prises en charge | getting-started/use-two-factor-authentication.md | #prérequis-installer-une-application-dauthentification %}.

### Rendre obligatoire l’activation de la 2FA pour certains utilisateurs

1. Accédez à _Account > Utilisateurs_{:.breadcrumbs}.
2. Cliquez sur le **nom** de l’utilisateur pour lequel vous souhaitez rendre obligatoire l’activation de la 2FA.  
   La page contenant les informations sur l'utilisateur s'ouvre.
3. Dans la section **Sécurité**, cochez la case **Activer l'authentification à 2 facteurs**.
4. Cliquez sur _Enregistrer_{:.doc-button} pour confirmer l’activation.

### Rendre obligatoire l’activation de la 2FA pour tous les utilisateurs

1. Accédez à _Account > Sécurité_{:.breadcrumbs}. Sur cette page, vous pouvez voir la distribution actuelle de la 2FA parmi vos utilisateurs.
2. Cliquez sur _Rendre obligatoire l'authentification à 2 facteurs pour tous_{:.doc-button}.  
   Vous verrez un message de confirmation vert. Le texte du bouton changera en _Rendre optionnelle l'authentification à 2 facteurs pour tous_{:.doc-button}.

### Désactiver la 2FA pour certains utilisateurs

Dans certains cas, vous souhaiterez peut-être désactiver temporairement la 2FA ou en exclure complètement certains utilisateurs&nbsp;:

1. Accédez à _Account > Utilisateurs_{:.breadcrumbs}.
2. Cliquez sur le **nom** de l’utilisateur pour lequel vous souhaitez désactiver la 2FA.  
   La page contenant les informations sur l'utilisateur s'ouvre.
3. Dans la section **Sécurité**, décochez la case **Activer l'authentification 2 facteurs**.
4. Cliquez sur _Enregistrer_{:.doc-button} pour confirmer la désactivation.
