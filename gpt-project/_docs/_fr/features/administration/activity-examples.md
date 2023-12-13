---
title: Exemples de configuration des activités
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: false
description: Configurer les activités standards à l’aide d’exemples
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

Pour configurer la façon dont injixo gère les activités lors de la planification et pour les rapports, utilisez les {% link_new types d’activités et leurs propriétés | features/administration/activity-types-and-properties.md %} dans _Plan > Configuration > Activités_{:.breadcrumbs}.

Ci-dessous, vous trouverez des exemples de configuration pour les activités fréquemment utilisées, leur type et les propriétés correspondantes.

## Présence, pause, maladie et congés

Ce tableau présente des exemples de configuration pour les activités de type Présence, Pause, Maladie et Congés.
L’activité Présent est une activité standard préconfigurée dans injixo. Vous pouvez l’utiliser pour toutes les activités sur lesquelles vos employés travaillent et basées sur le besoin en personnel, par exemple pour les appels. 

<div class="table__wrapper" markdown="1">

<style>
table {
   width: 100%;
}
</style>

|                                        |  Présent  | Pause-déjeuner |         Maladie         |  Congé |
| ------------------------------------------- | :---------------------: | :----------------------: | :---------------------: | :---------------------: |
| **Type**                                        |         Présence         |          Pause           |         Maladie         |        Congé         |
| Rémunérée                                        | <i class="fa fa-check"> |                          | <i class="fa fa-check"> | <i class="fa fa-check"> |
| Respecter le temps de repos                     | <i class="fa fa-check"> |                          |                         |
| Planifiable automatiquement                                   | <i class="fa fa-check"> |                          |                         |
| Autoriser les demandes dans Me                                 |                         | <i class="fa fa-check">  |                         | <i class="fa fa-check"> |
| Remplaçable                                 | <i class="fa fa-check"> |                          |                         |
| Bourse d’échanges            | <i class="fa fa-check"> | <i class="fa fa-check">  |                         |
| Activité à journée entière                  |                         |                          | <i class="fa fa-check"> | <i class="fa fa-check"> |

</div>

Selon la politique de votre organisation, les contrats ou la réglementation du travail, certaines pauses peuvent également être non rémunérées. Dans ce cas, décochez la case Rémunérée.

## Absences et réunions

Ce tableau présente des exemples de configuration pour les activités de type Absence et Meeting.
Les absences rémunérées sont généralement utilisées pour compenser les heures supplémentaires ou comme bloqueur pour {% link_new planifier les jours fériés | best-practices/scheduling-public-holidays.md %}.
Si un employé ne peut travailler sous aucun prétexte certains jours, vous pouvez bloquer ces jours en utilisant la configuration de la colonne Absence non rémunérée du tableau.

<div class="table__wrapper" markdown="1">

|                                          | Absence rémunérée | Absence non rémunérée |    Réunion à journée entière     |  Formation  |
| --------------------------------------------- | :-----------------------: | :-------------------------: | :---------------------: | :---------------------: |
| **Type**                                          |          Absence          |           Absence           |         Meeting         |         Meeting         |
| Rémunérée                                          |  <i class="fa fa-check">  |                             | <i class="fa fa-check"> | <i class="fa fa-check"> |
| Respecter le temps de repos                       |                           |                             | <i class="fa fa-check"> |
| Planifiable automatiquement                                     |                           |                             |                         |
| Autoriser les demandes dans Me                                   |  <i class="fa fa-check">  |   <i class="fa fa-check">   |                         |
| Remplaçable                                   |                           |                             |                         |
| Bourse d’échanges              |                           |                             |                         |
| Activité à journée entière                    |  <i class="fa fa-check">  |   <i class="fa fa-check">   |                         | <i class="fa fa-check"> |

</div>

Vous pouvez également utiliser des absences rémunérées comme jours de compensation pour les heures supplémentaires ou comme bloqueur rémunéré lors de la {% link_new planification des jours fériés | best-practices/scheduling-public-holidays.md %}.<br>
L’activité Absence non rémunérée peut également être utilisée pour déterminer de manière flexible les jours pendant lesquels un employé ne travaillera sous aucun prétexte.