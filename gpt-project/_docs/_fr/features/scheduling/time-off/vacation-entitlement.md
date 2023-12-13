---
title: Droits aux congés
toc: false
redirect_from:
  - /fr/droits-conges/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-absences-management.md
---

Si vous souhaitez limiter la pose de congés par vos Employés, vous devez leur attribuer un solde de congés. Le menu
_Droits aux congés_{:.menu-item} offre une vue globale sur le nombre de jours restants et vous permet de réaliser des modifications.
Pour accéder au menu, cliquez sur _Plan > Droits aux congés_{:.breadcrumbs}.

Pour injixo Enterprise On Premise, l'accès au menu est inchangé et accessible via _WFM > Scheduling > SchedulePro > Droits aux congés_{ :.breadcrumbs}.

> Remarque
>
> Pour autoriser vos Employés à saisir des demandes de congés dans le portail Me, vous devez créer une {% link_new Période de planification | features/scheduling/planning-periods/what-are-planning-periods.md %}.

## Définition des paramètres

Dans la partie supérieure, vous pouvez choisir l'Unité opérationnelle et l'année pour laquelle vous souhaitez éditer les droits aux congés. Il est également possible de filtrer par Groupe.

## Vue d'ensemble

Le tableau présente les colonnes suivantes :

- **Matricule**

- **Employés**

  Si des Employés appartiennent à plusieurs Unités opérationnelles au cours de l'année, il suffit de mettre à jour les données une seule fois.

- **Contrat**

  Le paramètre `Calcul des jours travaillés` dans le Contrat (flexible ou standard) influe sur le calcul des congés.

- **Solde année en cours**

  Le solde de congés de l'année en cours d'un Employé est calculé en fonction du solde de congés de l'année précédente plus le droit au congés de l'année en cours moins le nombre de jours de congés validés.
  Un jour de congés validé est inscrit dans la Catégorie `Planning` du _Centre de planification_{:.menu-item}.

- **Solde année précédente**

  Nombre de jours de congés de l'année précédente. Vous pouvez écraser ces données manuellement avec une valeur positive ou négative.

- **Année en cours**

  Nombre de jours de congés pour l'année en cours. Vous pouvez écraser ces données manuellement avec une valeur positive ou négative.

- **Congés pris**

  Pourcentage présentant le nombre de jours de congés déjà pris par les Employés divisé par le droit aux congés de l'année en cours. L'entête de la colonne affiche un pourcentage moyen sur la sélection.

## Opérations

En cliquant sur _Transférer le solde vers_{:.doc-button} vous pouvez également transférer le solde des congés de tous les Employés vers l'année suivante si les données sont disponibles.

En cliquant sur _Congés/Absences_{:.doc-button} vous serez redirigé vers le menu correspondant pour traiter les demandes de congés en cours.

En cliquant sur _Export CSV_{:.doc-button} vous téléchargez les données du tableau dans un fichier au format CSV.
