---
title: Planifier des Activités supplémentaires
product_label:
  - advanced
  - enterprise
permalink: /fr/planifier-activites-supplementaires/
permalink_reason: article used in intercom and email
description: Remplacer une activité existante par une Activité supplémentaire comme le back-office, l'e-mail ou le chat.
redirect_from:
  - /fr/schedules-activites-supplementaires/
redirect_reason: Updated filename on 21 April 2022
---

La fonctionnalité **Planifier des Activités supplémentaires** vous permet d'affecter les heures-personnes à planifier sur des Activités (comme le backoffice, les e-mails ou le chat) et sélectionner les employés concernés.
L'optimisation garantit que les créneaux des Activités supplémentaires sont positionnés de manière optimale pour limiter l'impact sur la couverture.

## Vue d'ensemble

La planification des Activités supplémentaires ne peut être réalisée que sur un planning existant, nous recommandons donc d'utiliser cette fonctionnalité à la fin de votre processus de création de planning. Les Activités supplémentaires peuvent remplacer uniquement des activités de type _Présence_ avec les options _Rémunérées_ et _Remplaçable_.

Pour planifier des Activités supplémentaires, les étapes sont les suivantes :

1. Aller à _Plan > Schedules_{:.breadcrumbs}.
2. Cliquer sur **Actions de planification** pui **Planifier des Activités supplémentaires**.

La page Vue d'ensemble présente l'**historique de planification** des Activités supplémentaires (en cours et passé). Les informations suivantes sont disponibles :

- Date et heure du démarrage du processus
- Identifiant de l'Utilisateur
- Unité opérationnelle concernée
- Activité supplémentaire planifiée
- Période sélectionnée
- Statut du processus

## Configurer une nouvelle Activité supplémentaire

Pour commencer le processus de planification d'une nouvelle activité, cliquez sur _Configurer les Activités supplémentaires_{:.doc-button} sur la page Vue d'ensemble.

### Paramètres

Dans la section **Configuration**, renseignez les informations suivantes :

<style>
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

| Paramètres                                               | Description                                                                                                                                                                                                                                   |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unité opérationnelle                                     | Sélectionnez une Unité opérationnelle dans la liste ou tapez son nom pour filtrer les résultats. Après avoir sélectionné l'Unité opérationnelle, la liste des Activités de type _Présence_ qui ne sont pas _remplaçables_ est affichée.       |
| Activité supplémentaire à planifier                      | Sélectionnez une Activité dans la liste ou tapez son nom pour filtrer les résultats. Les Activités proposées sont uniquement celles de type _Présence_ et _Rémunérée_.                                                                        |
| Période                                                  | Sélectionnez la période sur laquelle l'Activité supplémentaire doit être planifiée. Par défaut, la période est la semaine prochaine (Lundi à Dimanche. Si la date du jour est un lundi, alors la semaine par défaut est la semaine en cours). |
| Durée minimum de l'activité                              | Sélectionnez la durée minimum de l'Activité supplémentaire. La plage varie de 15 à 120 minutes et la valeur par défaut est 30 minutes. Les options possibles dépendent de l'intervalle de l'Unité opérationnelle sélectionnée.                |
| Total d'heures-personnes à planifier                               | Sélectionnez les heures-personnes que vous souhaitez distribuer entre les Employés.                                                                                                                                                             |
| Répartir uniformément les heures-personnes entre les employés | Si cette option est cochée, l'optimisation distribuera uniformément les heures-personnes. Attention, la couverture résultante peut être moins optimisée.                                                                                        |

### Sélectionner les Employés

Dans la section **Employés**, vous sélectionnez les Employés pour lesquels l'Activité supplémentaire sera planifiée. Initialement, tous les Employés de l'Unité opérationnelle sont affichés mais vous ne pouvez sélectionner que ceux qui disposent de la compétence pour réaliser l'Activité supplémentaire. Vous pouvez également réduire votre sélection en choisissant un {% link_new Groupe | features/administration/selections.md %} ou un Filtre avancé à partir de la liste déroulante correspondante.

<!-- add settings screenshot-->

## Générer et consulter les propositions

Une fois la configuration effectuée, cliquer sur _Générer les propositions_{:.doc-button} en bas de la page pour commencer le processus d'optimisation. Vous êtes redirigé vers la page Vue d'ensemble et une nouvelle entrée est disponible dans l'**historique de planification**.

La colonne **Statut** indique à l'utilisateur l'état de l'optimisation et se met à jour automatiquement une fois le processus terminé. La valeur peut être une des suivantes :

- **Propositions disponibles**<br>
  Le processus s'est déroulé avec succès et les propositions sont générées.
- **Optimisation impossible**<br>
  Les Employés sélectionnés n'ont pas suffisamment d'Activités remplaçable de type _Présence_ ou la durée minimum de l'Activité supplémentaire est trop grande.
- **L'optimisation a échoué. Merci d'essayer à nouveau**<br>
  Le processus n'a pu s'exécuter à cause d'une erreur interne.

Le temps de calcul dépend donc de la quantité de données à traiter, c’est à dire le nombre d’Employés, la période, etc. La génération des propositions peut aller de quelques secondes à plusieurs minutes.

Une fois l'optimisation terminée, cliquer sur **Voir les résultats** de la colonne **Statut** pour consulter les propositions.

Les heures-personnes proposés est affiché en haut de la page. Chaque proposition détaille le créneau horaire, l'Activité supplémentaire, l'Employé concerné, l'Activité précédemment planifiée (qui sera remplacée) et l'impact sur la couverture.

La couverture affichée est calculée au moment de la génération des propositions et ne sera pas mise à jour lors des modifications ultérieures du planning.

Vous pouvez rejeter une proposition en désélectionnant la case à gauche de celle-ci. Après avoir planifié les propositions sélectionnées, celles qui ont été exclues sont affichées comme tel et vous ne pourrez plus les utiliser.

Recommencez le processus depuis le début si vous souhaitez obtenir de nouvelles propositions, par exemple en modifiant les paramètres comme la _Durée minimum de l'activité_

<!-- add suggestions screenshot-->

## Planifier les propositions

Une fois les propositions sélectionnées, cliquez sur _Planifier les Activités supplémentaires_{:.doc-button} en bas de la page pour les insérer dans le planning. Cette étape peut prendre quelques minutes en fonction du nombre de sélections. Une fois l'insertion terminée, vous êtes redirigé vers la page de résultats.

La page de résultats affiche les propositions planifiées avec succès. Si certaines insertions ont échoué, vous pouvez les consulter dans une vue à part pour les ignorer ou les ajouter manuellement à partir du menu _Schedules_{:.menu-item}.

Naviguer entre les vues en utilisant les onglets `Planifiées` - `Refusées` - `Exclues`.

Cliquez sur _Retour à la Vue d'ensemble_{:.doc-button} en bas de la page pour revenir sur la page Vue d'ensemble.

> Remarque
>
> Vous pouvez consulter à nouveau la page des propositions inscrites dans le planning en cliquant sur **Voir les résultats**.

<!-- add results screenshot-->
