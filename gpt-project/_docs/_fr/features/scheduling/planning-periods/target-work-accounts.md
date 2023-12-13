---
title: Comptes temps dû
redirect_from:
  - /fr/comptes-temps-du/
redirect_reason: Updated filename on 21 April 2022
---

Le menu *WFM > Planification > TimeManager > Comptes temps dû*{:.breadcrumbs} vous permet de calculer, visualiser et modifier le temps de travail de vos Employés pour chaque Période de planification. Lors de la modification manuelle, vous pouvez ajouter ou soustraire des heures sur plusieurs comptes à la fois, par exemple pour les ajuster durant les variations saisonnières. La valeur calculée par défaut dépend de la durée hebdomadaire théorique (champ `A effectuer` du Contrat) du temps de travail d'un Employé.

## Définition des Paramètres

Dans un premier temps saisissez les paramètres suivants :

| Paramètre | Description |
| --------- | ----------- |
| Unité opérationnelle | Unité opérationnelle pour laquelle vous souhaitez afficher les Comptes temps dû. La dernière Unité opérationnelle consultée est affichée par défaut. |
| Groupe | Groupe pour lequel vous souhaitez afficher les Comptes temps dû. Le dernier Groupe consulté est affiché par défaut. |
| Période de planification | Période de planification pour laquelle vous souhaitez afficher les Comptes temps dû. Toutes les Périodes de planification de type 'Standard' sont disponibles. |

Confirmez votre sélection en cliquant sur *Appliquer*{:.doc-button} pour afficher ou mettre à jour la vue générale des Comptes temps dû.

## Vue Générale

| Colonne  | Description |
| -------  | ------- |
| Employé | Liste des Employés concernés. |
| Solde calculé | Affiche le temps de travail cible des Employés après réalisation de l'opération `Calculer`. La valeur est affichée en heures et ne peut-être modifiée. Les valeurs manquantes signifient qu'il n'y a pas encore de Comptes temps dû calculés pour la Période de planification. |
| Solde manuel | Permet de saisir manuellement un temps de travail cible. |

La vue d'ensemble ne contient aucune valeur si aucun Compte temps dû n'a été calculée pour la période spécifiée.

> Remarque
>
> La colonne `Solde calculé` et le *Centre de planification*{:.menu-item} continue d'afficher le temps de travail cible ou contractuel même si un `Solde manuel` a été saisi.

## Calculer les Comptes temps dû

Pour obtenir le *Solde calculé* (temps de travail théorique) pour une Période de planification, cliquez sur *Calculer*{:.doc-button} dans la section *Paramètres*. Une tâche s'exécute en arrière-plan et la vue générale est mise à jour à la fin du calcul.

> Remarque
>
> Les Comptes temps dû ne sont calculés que pour les Employés qui ont une Période d'emploi et un Contrat valides sur cette période.

## Ajuster les Comptes temps dû

La section `Effectuer une opération` vous permet d'augmenter ou diminuer la valeur calculée du temps de travail cible en pourcentage ou en valeur absolue.

| Paramètre | Description |
| ------- | ----------- |
| Valeur en pourcentage | Permet d'augmenter ou de diminuer le nombre d'heure en pourcentage. |
| Valeur en absolue | Permet d'augmenter ou de diminuer le nombre d'heure à partir de la valeur indiquée. |
| Opération | Permet d'ajouter (`Créditer`) ou retirer (`Débiter`) des heures. |
| Valeur | La Valeur en pourcentage doit être comprise entre 1 et 100%. La Valeur en absolue doit être inférieure à 9999:00 heures. |

Pour ajuster les Comptes temps dû, cliquez sur le bouton *Appliquer*{:.doc-button}. Une tâche s'exécute en arrière-plan et la colonne Valeur modifiée est mise à jour.
