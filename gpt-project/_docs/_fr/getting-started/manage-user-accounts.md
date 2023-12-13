---
title: Gérer les comptes utilisateurs
description: Voir les utilisateurs facturés et non facturés Créer, modifier et supprimer des utilisateurs. Gérer les accès utilisateur en ajoutant des rôles utilisateur.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-2fa.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
redirect_from:
  - /fr/user-administration/
redirect_reason: page used in intercom, updated filename on 06 December 2022
---

Créez des comptes utilisateur dans injixo pour gérer les employés de votre organisation. 

Dans _Account > Utilisateurs_{:.breadcrumbs}, vous pourrez voir l’ensemble des utilisateurs&nbsp;:
- Utilisateurs facturés&nbsp;: cet onglet affiche tous les utilisateurs actifs dans votre tenant injixo.
- Utilisateurs non facturés&nbsp;: cet onglet affiche tous les {% link_new utilisateurs désactivés | features/administration/deactivate-employees.md %} qui ne peuvent plus se connecter à injixo. Votre organisation n’est plus {% link_new facturée | getting-started/how-does-billing-work.md %} pour les utilisateurs désactivés.

Pour retrouver un ou plusieurs utilisateurs, utilisez le champ de recherche en haut de la liste des utilisateurs. Utilisez des virgules pour séparer les entrées.
Pour filtrer les utilisateurs par rôle, cliquez sur l’en-tête de la colonne **Rôles utilisateur**. La fenêtre qui s’ouvre ensuite vous permet de sélectionner un ou plusieurs rôles. Tous les utilisateurs disposant de l’un des rôles sélectionnés seront affichés dans la liste.

## Créer des utilisateurs

Les utilisateurs sont également appelés employés. injixo propose trois façons de créer des utilisateurs&nbsp;:
- dans _Account > Utilisateurs_{:.breadcrumbs},
- dans _WFM > Administration > Planification > Employés_{:.breadcrumbs},
- dans {% link_new People | features/people/manage-people.md | #créer-un-nouvel-employé %}.

> Remarque
> 
> Vous n’avez besoin de créer un utilisateur qu’une seule fois dans ces modules. injixo synchronisera ensuite automatiquement ces données utilisateur dans les deux autres modules.

Pour créer un utilisateur, suivez ces étapes&nbsp;:

1. Accédez à _Account > Utilisateurs_{:.breadcrumbs}.
2. Cliquez sur _Créer un utilisateur_{:.doc-button}.
3. Remplissez les données utilisateur et cliquez sur _Créer_{:.doc-button}.

## Modifier un compte utilisateur

injixo propose deux modules dans lesquels vous pouvez modifier un compte utilisateur, en fonction de ce que vous souhaitez faire. Le tableau ci-dessous vous donne un aperçu des différentes options de configuration et de l’endroit où vous pouvez les trouver dans injixo. Vous pouvez également accéder à ces deux endroits depuis People.

| Je veux                                          | Quel module utiliser                                                                             |
| -------------------------------------------------- | ------------------------------------------------------------------------------------- |
| {% link_new Configurer les paramètres liés à la planification pour un utilisateur | features/administration/employee-overview.md | #aperçu-des-paramètres-employés %} (par exemple, assigner des activités, ajouter des niveaux de compétence, définir des disponibilités) | _WFM > Administration > Planification > Employés_{:.breadcrumbs} |
| {% link_new Modifier les informations de période d’emploi | getting-started/manage-user-accounts.md | #désactiver-un-compte-utilisateur %} pour un utilisateur | _WFM > Administration > Planification > Employés_{:.breadcrumbs} |
| Modifier la langue et le fuseau horaire pour un utilisateur | _Account > Utilisateurs_{:.breadcrumbs} |
| {% link_new Attribuer un rôle utilisateur à un utilisateur | getting-started/configure-user-roles.md | #attribuer-des-rôles-utilisateur-aux-utilisateurs %} | _Account > Utilisateurs_{:.breadcrumbs} |
| {% link_new Rendre obligatoire l’authentification à deux facteurs | getting-started/manage-2fa.md %} | _Account > Utilisateurs_{:.breadcrumbs} |

Si vous souhaitez modifier un utilisateur, par exemple pour changer son adresse e-mail, suivez ces étapes&nbsp;:

1. Accédez à _Account > Utilisateurs_{:.breadcrumbs}.
2. Cliquez sur le nom d’utilisateur d’un utilisateur existant.
3. Modifier les paramètres de l’utilisateur.
4. Cliquez sur _Enregistrer_{:.doc-button}.

### Accorder l’accès administrateur à un utilisateur

1. Accédez à _Account > Utilisateurs_{:.breadcrumbs}.
2. Cliquez sur le nom d’utilisateur d’un utilisateur existant.
3. Dans la section **Accès Admin**, cochez la case **Donner le rôle Admin à l’utilisateur**.
4. Cliquez sur _Enregistrer_{:.doc-button}.

### Débloquer les utilisateurs

Le compte d’un utilisateur qui entre un mot de passe erroné trois fois de suite sera verrouillé. Pour débloquer les utilisateurs verrouillés, suivez ces étapes&nbsp;:

1. Accédez à _Account > Utilisateurs_{:.breadcrumbs}.<br>
La liste des utilisateurs affiche une {% icon lock %} jaune à côté du nom de l'utilisateur verrouillé.
2. Cliquez sur le nom d'utilisateur de l’utilisateur bloqué.
3. Dans la section **Sécurité** à droite, cliquez sur _Déverrouiller l’utilisateur_{:.doc-button}.

Lorsque vous avez déverrouillé un utilisateur, nous vous recommandons de définir un nouveau mot de passe pour cet utilisateur. 

### Définir un nouveau mot de passe utilisateur

Si un utilisateur a oublié son mot de passe, il peut le réinitialiser en cliquant sur le lien **Mot de passe oublié&nbsp;?** sur la page de connexion. Vous pouvez également le configurer directement pour eux, par exemple après le verrouillage de leur compte.
Pour définir un nouveau mot de passe pour un utilisateur, suivez ces étapes&nbsp;:

> Remarque
>
> Les utilisateurs ne sont pas informés des changements de mot de passe. Vous devez les informer de leur nouveau mot de passe.

1. Accédez à _Account > Utilisateurs_{:.breadcrumbs}.
2. Cliquez sur le nom d’utilisateur d’un utilisateur existant.
3. Dans la section **Sécurité** à droite, cliquez sur _Définir un nouveau mot de passe_{:.doc-button}.
4. Entrez un nouveau mot de passe pour l’utilisateur.
5. Cliquez sur _Enregistrer_{:.doc-button}.



## Désactiver un compte utilisateur

Lisez l’article {% link_new Désactiver, réactiver et supprimer des employés | features/administration/deactivate-employees.md %} pour comprendre les conséquences de la suppression ou de la désactivation de comptes utilisateurs.

1. Accédez à _Account > Utilisateurs_{:.breadcrumbs}.
2. Cliquez sur le nom d’utilisateur d’un utilisateur existant.
3. Cliquez sur _Supprimer_{:.doc-button} en bas à droite.  
   Une fenêtre s’ouvre.
4. Pour désactiver l’utilisateur, cliquez sur _Période d’emploi_{:.doc-button} et définissez une date de départ. Toutes les données de planification seront conservées. Vous pourrez réactiver l’utilisateur ultérieurement.

Apprenez à {% link_new réactiver un utilisateur | features/administration/deactivate-employees.md | #réactiver-un-employé %}.

## Supprimer un compte utilisateur

> Attention
>
> Une fois un compte utilisateur supprimé, vous ne pourrez plus le réactiver. Le compte utilisateur sera supprimé de tous les plannings actuels et futurs pour lesquels l’employé était planifié.

Pour supprimer définitivement un compte utilisateur, suivez les étapes ci-dessous&nbsp;:

1. Accédez à _Account > Utilisateurs_{:.breadcrumbs}.
2. Cliquez sur le nom d’utilisateur d’un utilisateur existant.
3. Cliquez sur _Supprimer_{:.doc-button} en bas à droite.  
   Une fenêtre s’ouvre.
4. Cochez la case **J’ai compris que la fiche employé et les plannings de &lt;Nom de l’employé&gt; seront supprimés.**
5. Cliquez sur _Supprimer_{:.doc-button}. 

## Exporter la liste des utilisateurs au format CSV

Pour pouvez exporter l’ensemble de la liste au format CSV ou appliquer un filtre avant de l’exporter. Par exemple, vous pouvez importer ce fichier CSV dans des bases de données et des outils externes tels que les bases de données Data Warehouse, SAP et les systèmes de gestion des ressources humaines.

1. Accédez à _Account > Utilisateurs_{:.breadcrumbs}.
2. (Facultatif) Pour réduire la liste des utilisateurs affichés, utilisez le champ de recherche ou le filtre des rôles.
3. Cliquez sur _Exporter CSV_{:.doc-button} en haut à droite de la page.  
   Le fichier CSV sera téléchargé sur votre ordinateur.

Le fichier contient le nom, le prénom et l’adresse e-mail de connexion. Les champs sont séparés par des virgules. Le format du fichier est fixe et ne peut être changé.
