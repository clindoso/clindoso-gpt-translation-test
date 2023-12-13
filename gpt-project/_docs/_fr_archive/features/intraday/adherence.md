---
title: Adherence
toc: false
archived_date: 2021-04-22
archive_ref: 20210422-fr-adherence
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Le module _Adherence_{:.menu-item} vous permet de comparer en temps réel les plannings théoriques et réels de vos employés.

Adherence est accessible dans le menu _Intraday_{:.menu-item}. Pour avoir accès à cette fonctionnalité, les utilisateurs doivent avoir le rôle *Admin*, *Planificateur* ou *Superviseur* (avancé ou basique).

## Vue d'ensemble

L'écran principal présente un tableau affichant l'activité planifiée et l'activité actuelle des Employés sélectionnés. Vous pouvez trier les colonnes affichées en cliquant sur leur en-têtes.
Pour afficher les données des Employés, sélectionnez tout d'abord une Unité opérationnelle et/ou un Groupe.

Les colonnes du tableau sont les suivantes :

| En-tête | Description |
|--- |--- |
| Nom | Nom de l'employé. |
| Activité planifiée | Activité issue de la Catégorie *Planning*. |
| Statut | Statut de l'adhérence de l'employé au planning. Ce statut peut être *Adhérent*, *Non présent*, *Activité incorrecte* ou *Non planifié*. Chaque statut a son propre code couleur. |
| Activité actuelle | Activité issue de la Catégorie *Système externe* ou *Saisie des temps de présence*. |
| Ecart avec le planning | Durée totale de l'écart. |
| Durée de l'activité actuelle | Durée de l'activité en cours. |

## Barre de recherche

La barre de recherche en haut de la page vous permet de filtrer l'affichage selon le nom de l'employé, l'activité ou le statut d'adhérence. Pour effectuer une recherche sur plusieurs critères, séparez-les par des virgules.

## Statut agent

Chaque employé se voit attribuer un statut basé sur la comparaison entre l'activité planifiée et l'activité actuelle. Dans le cas où les 2 activités sont de même type, l'employé est adhérent à son planning.

Si les 2 activités sont de type différent, l'employé est alors non adhérent à son planning et identifié en écart. 3 raisons peuvent expliquer un écart au planning :

**Non présent** : l'employé est censé être présent mais ne s'est pas connecté au système externe.
**Activité incorrecte** : le type de l'activité actuelle de l'employé est différent de celui de l'activité planifiée.
**Non planifié** : l'employé n'a aucune activité planifiée mais est connecté au système externne.

## Employés en écart

Il est rare que les employés adhèrent à leur planning à la seconde près. C'est pour cela que vous pouvez définir une durée en dessous de laquelle les écarts ne seront pas identifés.
Ce seuil peut être paramétré pour chacun des statuts en cliquant sur l'icône de paramètre en haut à droite de l'écran. Ces paramètres sont identiques pour tous les utilisateurs.

Aussitôt que la durée de l'écart dépasse le seuil défini, l'employé est mis en évidence. Pour plus de clarté, il est possible d'afficher uniquement les employés en dépassement en cochant la case *Afficher uniquement les dépassements* à droite de la *barre de recherche*.

## Score d'adhérence

{{ 1 | image: "score Adherence",'50%' }}

Le bloc *Adhérence* à gauche de l'écran présente une vue synthétique des résultats de l'adhérence des Unités opérationnelles et/ou des Groupes sélectionnés.

Le *pourcentage d'adhérence* indique le pourcentage d'employés qui sont adhérents au planning.

Le bloc *Ecart en cours* détaille la distribution des écarts par statut.

Un récapitulatif est également affiché dans le dernier bloc et présente pour les activités de type *Présence* et *Pause* le nombre d'employés planifiés, en cours d'activité et la différence des deux.

Vous pouvez filtrer la liste des Employés affichés en cliquant sur le statut de leur écart.

## Détail par activité

{{ 2 | image: "Détail par activité",'50%' }}

Le bloc *Détail par activité* présente, pour chaque activité de l'Unité opérationnelle et/ou du Groupe sélectionné, un aperçu du nombre d'employés planifiés et du nombre d'employés déclarant cette activité dans le système externe.

Vous pouvez trier l'une ou l'autre des colonnes en cliquant sur son en-tête.

Les colonnes du tableau sont les suivantes :

| En-tête | Description |
| --- | --- |
| Activité | Activité planifiée. |
| Planifiés | Nombre d'employés planifiés sur cette activité. |
| En cours | Nombre d'employés ayant déclaré l'activité dans le système externe. |

Vous pouvez filtrer la liste des Employés affichés en cliquant sur l'activité.

> Remarques
>
> - Les données affichées dans le module *Adherence*{:.menu-item} sont issues du système externe connecté à injixo. Chaque Employé doit avoir un *ID de système externe* paramétré dans sa *fiche employé* pour que le lien soit correctement établi.
> - 2 rapports sont disponibles dans le menu *Reports*{:.menu-item} pour suivre l'adhérence à la planification (Activités et temps de travail) à posteriori.
