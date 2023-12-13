---
title: Configurer les rôles utilisateur
redirect_from:
  - /fr/user-and-role-authorization/
redirect_reason: renamed file in June 2021
description: Découvrez quels sont les rôles utilisateur disponibles, modifiez leurs permissions, créez de nouveaux rôles utilisateur et attribuez des rôles aux utilisateurs.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-user-accounts.md
---

## Que sont les rôles utilisateur&nbsp;?

Un rôle d’utilisateur définit les droits d’accès pour un groupe d’utilisateurs&nbsp;:

- aux produits et fonctionnalités dans injixo, par exemple _Forecast_{:.menu-item},
- aux fonctionnalités de WFM, par exemple _WFM > Administration_{:.breadcrumbs}.

injixo utilise des catégories de rôles, chacune ayant un {% link_new rôle utilisateur standard | getting-started/default-user-roles.md | #rôles-utilisateur-standard %} avec des droits d’accès, c’est-à-dire des autorisations prédéfinies. Lorsque vous ajoutez un nouveau rôle utilisateur dans une catégorie de rôle, il aura les droits d’accès aux produits et fonctionnalités du rôle utilisateur standard.<br>
La catégorie de rôle Autre n'a pas de rôle utilisateur standard.

### Voir et organiser les rôles utilisateur

Accédez à _Account > Rôles utilisateur_{:.breadcrumbs}.  
   Les rôles utilisateur sont regroupés dans des catégories de rôles prédéfinies (par exemple, la catégorie de rôle Planificateur). Les catégories de rôles peuvent aider à organiser les droits d’accès. Vous pouvez également faire glisser un rôle utilisateur d’une catégorie à l’autre ou rechercher des rôles utilisateur par nom.
   
   > Les droits sur les nouvelles fonctionnalités sont accordés en fonction de la catégorie de rôle.  
   >   
   >Les autorisations pour les nouvelles fonctionnalités d’injixo sont attribuées automatiquement aux rôles utilisateur en fonction de leur catégorie de rôle. Par exemple, une nouvelle fonctionnalité pour les planificateurs sera accessible à tous les rôles utilisateur de la catégorie de rôle Planificateur. Si vous avez déplacé un rôle utilisateur de la catégorie de rôle Planificateur vers une autre catégorie de rôle, il ne recevra plus automatiquement les autorisations pour la nouvelle fonctionnalité Planificateur. Si nécessaire, un utilisateur avec un accès Admin peut ajouter manuellement les permissions au rôle utilisateur. Il en va de même pour les rôles utilisateur de la catégorie de rôle Autre. Leurs autorisations doivent toujours être ajoutées manuellement.

   {{ 1 | image: "Catégories de rôles utilisateur", '80%' }}

### Créer un nouveau rôle utilisateur

1. Cliquez sur l’{% icon blue_plus %} dans n’importe quelle catégorie de rôle. Faites passer votre curseur sur les icônes {% icon info_circle | icon-only %} pour en savoir plus sur chaque catégorie de rôle.

   - Catégorie Autre&nbsp;: crée un rôle utilisateur vide. Aucune autorisation par défaut n’est définie.
   - Catégories de {% link_new rôle standard | getting-started/default-user-roles.md %}&nbsp;: les autorisations par défaut pour les composants d’injixo sont pré-sélectionnées. Les droits d’accès aux fonctionnalités WFM ne sont pas définis. 
  > Remarque
  >
  > Lorsque vous créez un nouveau rôle utilisateur, vous devez définir manuellement les [droits d'accès aux fonctionnalités WFM](#set-wfm-module-permissions).

2. Sur la page de création du rôle utilisateur, configurez le rôle utilisateur&nbsp;:

   - **Informations générales**&nbsp;: saisissez un **Nom**, une **Abréviation** et une **Description** facultative.
   - **Catégorie de rôle**&nbsp;: affiche la **Catégorie du rôle** présélectionnée.

3. (Facultatif) Modifiez les droits par défaut. Dans la section **Droits**, une coche grise à côté du nom d’un composant indique que toutes les autorisations pour ce composant sont accordées par défaut. Un signe «&nbsp;moins&nbsp;» gris indique que certaines autorisations pour ce composant ne sont pas accordées par défaut.  
   - Composant&nbsp;: pour accorder des autorisations pour toutes les fonctionnalités d’un composant, cochez la case à côté du nom du composant.
   - Fonctionnalité&nbsp;: pour accorder des autorisations pour des fonctionnalités individuelles, cliquez sur la flèche pointant vers le bas à côté du nom du composant. Cochez les cases à côté des fonctionnalités.
   - Pour ouvrir ou fermer toutes les sections, cliquez sur **Tout afficher**/**Tout réduire**.
   - Pour réinitialiser les autorisations sélectionnées à celles du rôle utilisateur standard, cliquez sur **Réinitialiser les droits par défaut**.
4. Pour enregistrer le nouveau rôle utilisateur, cliquez sur _Créer le rôle utilisateur_{:.doc-button}. Pour [définir les droits sur WFM](#set-wfm-module-permissions) pour le nouveau rôle utilisateur, cliquez sur _Créer et aller à Droits d’accès des rôles d’utilisateurs_{:.doc-button}.

   {{ 2 | image: "Page de création du rôle utilisateur", '80%' }}

### Attribuer des rôles utilisateur aux utilisateurs

1. Accédez à _Account > Utilisateurs_{:.breadcrumbs}.
2. Cliquez sur un **nom**.
3. Sous **Attribuer des rôles**, cochez une ou plusieurs cases. Pour filtrer les rôles d'utilisateur affichés, utilisez le champ **Rechercher un rôle.**
4. Cliquez sur _Enregistrer_{:.doc-button}.

   {{ 6 | image: 'Attribuer des rôles utilisateurs', '80%'}}

## <a name="set-wfm-module-permissions"></a> Définir les droits sur WFM

1. Dans _Account > Rôles utilisateur_{:.breadcrumbs}, sélectionnez un rôle utilisateur.
2. Dans la section **Droits**, cliquez sur _Aller au menu Droits d’accès des rôles d’utilisateurs_{:.doc-button}.  
   Ceci vous redirigera vers _WFM > Administration > Système > Droits d’accès des rôles d’utilisateurs_{:.breadcrumbs}.
3. Dans la section **Navigateur** à droite, cochez ou décochez les cases pour ajouter ou supprimer des droits.

{{ 4 | image: "Section Navigateur dans Droits d’accès des rôles d’utilisateurs", '60%' }}

Nous vous recommandons d’utiliser des droits liés aux rôles uniquement. Vous pouvez modifier les droits pour les utilisateurs individuels, si nécessaire. Pour modifier les droits individuels, accédez à _WFM > Administration > Système > Droits d’accès_{:.breadcrumbs}.

## Gérer l’accès de l’équipe&nbsp;: restreindre l’accès aux données de configuration

Si votre organisation inclut plusieurs équipes et si vous souhaitez restreindre l’accès aux données de l’équipe, vous pouvez ajouter plusieurs rôles utilisateur à un utilisateur. injixo combine les droits définis par différents rôles utilisateur. Vous pouvez restreindre l’accès aux éléments comme les unités opérationnelles, les modèles horaires, les activités ou les rapports.

**Exemple**

Si tous vos planificateurs doivent avoir accès au planning mais que chaque planificateur doit uniquement pouvoir modifier les données de son unité opérationnelle, vous pouvez assigner deux rôles utilisateur à chaque planificateur.

Vous pouvez créer un nouveau rôle utilisateur sans accès à certaines unités opérationnelles, ou supprimer l’accès à toutes les unités opérationnelles d’un rôle utilisateur existant. Pour supprimer l’accès à toutes les unités opérationnelles d’un rôle existant, procédez comme suit&nbsp;:

1. Accédez à _Account > Rôles utilisateur_{:.breadcrumbs}.
2. Sélectionnez le rôle utilisateur.
3. Cliquez sur _Aller à Droits d’accès des rôles d’utilisateurs_{:.doc-button}.
4. Faites défiler le menu de droite jusqu’à la section **Unités opérationnelles** (ou utilisez le lien d’accès rapide en haut de la page).
5. Cliquez sur l’{% icon item-delete %} à côté de l'entrée [TOUS] pour supprimer l’accès à toutes les unités opérationnelles.
6. Cliquez sur _OK_{:.doc-button}.

Ajoutez un accès aux unités opérationnelles souhaitées aux autres rôles en suivant les instructions ci-dessous&nbsp;:

1. Sélectionnez le second rôle utilisateur.
2. Dans la section **Unités opérationnelles**, cliquez sur l’{% icon item-add %}.
3. Sélectionnez les unités opérationnelles dans la liste. Maintenez la touche **CTRL** ou **Shift** enfoncée et cliquez pour sélectionner plusieurs unités opérationnelles.
4. Dans **Droits d’accès**, cochez une ou plusieurs cases pour définir les droits de **lecture**, de **modification** et de **suppression**.
5. Cliquez sur _OK_{:.doc-button}.

Pour terminer la configuration, accédez à _Account > Utilisateurs_{:.breadcrumbs} et [ajoutez les rôles à vos utilisateurs](#attribuer-des-rôles-utilisateur-aux-utilisateurs).


## Modifier des rôles utilisateur personnalisés ou standard

1. Accédez à _Account > Rôles utilisateur_{:.breadcrumbs}.
2. Sélectionnez le rôle utilisateur à modifier.
3. Apportez les modifications nécessaires aux paramètres utilisateur et cliquez sur _Enregistrer_{:.doc-button}.

## Supprimer des rôles utilisateur personnalisés

1. Accédez à _Account > Rôles utilisateur_{:.breadcrumbs}.
2. Sélectionnez le rôle utilisateur.
3. Cliquez sur _Supprimer le rôle utilisateur_{:.doc-button} en bas à droite. Les rôles utilisateur par défaut ne peuvent être supprimés.
