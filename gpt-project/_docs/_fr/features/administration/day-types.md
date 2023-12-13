---
title: Créer et utiliser des types de jours
description: Créez des types de jours pour modéliser les jours fériés et autres jours atypiques qui modifient vos heures d’ouverture.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/planning-calendar.md
  - overwrite_title: Planifier les jours fériés
    filepath: best-practices/scheduling-public-holidays.md
---

Les types de jours définissent les jours avec des heures de travail standard et les jours avec des heures de travail atypiques.

Ajoutez des types de jour à votre {% link_new unité opérationnelle | features/administration/create-and-manage-planning-units.md | #ajouter-des-horaires-douverture %} pour définir des horaires d’ouverture pour les jours standard de la semaine et pour les journées atypiques, par exemple si votre centre de contacts est ouvert les jours fériés. injixo prendra en compte les horaires d’ouverture définis pour ces jours lors de l’optimisation du planning.

Dans _Plan > Configuration > Types de jours_{:.breadcrumbs}, vous pouvez&nbsp;:

- voir les types de jours par défaut,
- créer, modifier et supprimer des types de jours personnalisés.

## Créer un type de jour personnalisé

Certains jours, vos horaires d’ouverture peuvent différer de vos horaires standard, par exemple en cas de promotions spéciales ou de jours fériés. Pour créer des types de jours personnalisés pour ces jours, suivez ces étapes&nbsp;:

1. Cliquez sur l’icône Créer {% icon item-add | icon-only %} dans la barre d’action.
2. Saisissez un **nom** (50 caractères maximum).
3. Saisissez une **abréviation** (25 caractères maxiumum).  
   L’abréviation apparaîtra dans le calendrier de planification.
4. (Facultatif) Cochez la case **Mode jour férié**.<br>[En savoir plus](#mode-jour-férié) sur la configuration du type de jours pour les jours fériés.
5. Cliquez sur _OK_{:.doc-button}.

## Mode jour férié

 Pour marquer un type de jour comme férié, cochez la case **Mode jour férié** dans la fenêtre de configuration du type de jour.

### Créer des types de jours pour les jours fériés

Vous pouvez créer des types de jours pour les jours fériés de deux façons&nbsp;:

- En créant des types de jours avec le mode jour férié et en les {% link_new ajoutant à votre calendrier de planification | features/administration/planning-calendar.md | #insérer-un-type-de-jour-et-un-modèle-de-calendrier %}.

- En ajoutant un {% link_new modèle de calendrier | features/administration/planning-calendar.md %}<!--todo: add correct anchor when the article is translated, see EN--> à votre calendrier de planification. Tous les types de jours pour les jours fériés seront alors automatiquement créés avec le mode jour férié.

Le mode jour férié réduira les heures de travail des employés conformément. Si vous décidez de planifier le jour comme un jour de travail standard, vous pouvez toujours désactiver le mode jour férié en {% link_new modifiant le type de jour | features/administration/day-types.md | #modifier-un-type-de-jour %}.

## Modifier un type de jour

> Attention
>
> Si vous modifiez le mode jour férié d’un type de jour en cours d’utilisation, vous devez recalculer les comptes horaires ou les {% link_new comptes temps dû | features/scheduling/planning-periods/target-work-accounts.md %}.
   
1. Sélectionnez un type de jour dans la liste.
2. Modifiez les données de votre choix.
3. Cliquez sur _OK_{:.doc-button}.

## Supprimer un type de jour

> Remarque
> 
> Avant de supprimer un type de jour, {% link_new supprimez-le de tous les calendriers de planification | features/administration/planning-calendar.md | #supprimer-des-données %}. Vous ne pouvez pas supprimer les types de jours par défaut.

1. Sélectionnez un type de jour dans la liste.
2. Cliquez sur l’{% icon item-delete %} dans la barre d’action.

## Types de jours dans la planification

injixo prend en compte les types de jours lors de la planification. 
- Si votre unité opérationnelle est ouverte régulièrement lors des jours fériés, il vous suffit {% link_new d’ajouter des horaires d’ouverture à l’unité opérationnelle | features/administration/create-and-manage-planning-units.md | #ajouter-des-horaires-douverture %}.  
- Si votre unité opérationnelle est fermée lors d’un jour férié, ou si elle est ouverte sur des horaires spéciaux, lisez l’article {% link_new Planifier les jours fériés | best-practices/scheduling-public-holidays.md %}.
