---
title: Comprendre les modèles horaires
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Découvrez les différents types de modèles horaires, ce qu’il faut prendre en compte avant de pouvoir créer un modèle horaire et l’impact de la modification d’un modèle horaire sur le planning.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
---

Les modèles horaires représentent des journées types. Ils représentent les journées de travail pour les employés que vous planifiez et définissent les heures de début et de fin des journées, ainsi que le nombre d’heures travaillées par jour et les disponibilités de chacun. injixo crée des plannings en fonction de vos modèles horaires.

Par défaut, les modèles horaires que vous créez sont automatiquement attribués à toutes les unités opérationnelles de votre organisation. Pour modifier ce comportement par défaut, {% link_new modifiez l’unité opérationnelle | features/administration/create-and-manage-planning-units.md | #limiter-les-modèles-horaires %}. Lors de l’optimisation du planning, injixo ne prendra en compte que les modèles horaires assignés à l’unité opérationnelle.

Si les modèles horaires configurés pour votre unité opérationnelle ne couvrent pas certains accords de travail, vous pouvez également ajouter des modèles horaires personnels à certains employés. Pendant l’optimisation du planning, injixo n’utilisera que les modèles horaires personnels pour cet employé.

Les modèles horaires contiennent les activités de type présence, absence et pause d’une journée. Vous devez donc ajouter les activités concernées aux modèles horaires. <!-- add link when translated -->

Les modèles horaires sont ajoutés aux {% link_new rotations d’horaires | features/administration/shift-sequences.md %} et peuvent être regroupés en {% link_new modèles hebdomadaires | features/administration/modeles-hebdomadaires.md %}.


## Types de modèles horaires

Il existe trois différents types de modèles horaires. 

> Remarque
> 
> - Les modèles horaires de type Mission à horaires fixes sont également appelés modèles horaires fixes.<br> 
> - Les modèles horaires de type Mission à horaires variables sont également appelés modèles horaires variables.


| Type                | Description                                                                                                                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mission à horaires fixes         | Les journées qui utilisent un modèle horaire fixe ont une heure de début et de fin fixes et ne peuvent être déplacées. Il ne peut y avoir qu’une seule journée possible avec un modèle horaire fixe. Les modèles horaires fixes sont généralement ajoutés aux {% link_new rotations d’horaires | features/administration/shift-sequences.md %}.                                      |
| Mission à horaires variables      | Les journées qui utilisent un modèle horaire variable ont une heure de début flexible dans un cadre prédéfini. Cela permet de créer plusieurs journées possibles. Les modèles horaires variables ajoutés aux rotations d’horaires deviendront automatiquement des modèles horaires fixes car ils sont définis sur la première position de début possible d'une journée. |
| Cadre de disponibilité | Ce type de modèle horaire est utilisé pour définir une plage horaire inférieure à celle des horaires d’ouverture de l’unité opérationnelle. Après avoir inséré des rotations d’horaires contenant ce type de modèle horaire, injixo sélectionnera les modèles horaires compatibles avec cette plage de disponibilité pendant l’optimisation et la génération de missions. Vous pouvez également utiliser ce type de modèle horaires pour configurer les disponibilités de plusieurs employés en même temps.          |

## Quel modèle horaire utiliser pour la planification&nbsp;?

Il n’y a pas de cas d'utilisation unique pour déterminer le type de modèle horaire à utiliser, mais voici quelques indications générales&nbsp;:

- Mission à horaires fixes&nbsp;: utilisez des modèles horaires fixes pour planifier les employés ayant des horaires de travail fixes. Leurs journées commenceront et se termineront toujours à une heure fixe et ne pourront pas être déplacées dans le planning.
Vous pouvez utiliser des modèles horaires fixes dans les modèles de planification pour {% link_new optimiser le planning | features/scheduling/scheduling-optimization.md %}, définir des modèles hebdomadaires cycliques dans les {% link_new rotations d’horaires | features/scheduling/capacity/capacity-insert-shift-sequences.md %} des équipes, ou pour la {% link_new génération de missions | features/scheduling/schedules/schedules-shift-bidding.md %}.
- Mission à horaires variables&nbsp;:  utilisez des modèles horaires variables pour planifier les employés ayant des horaires de travail flexibles. injixo peut planifier un employé pour différentes journées en utilisant un seul modèle horaire de ce type. Ce modèle horaire est généralement utilisé lors de {% link_new l’optimisation du planning | features/scheduling/scheduling-optimization.md %} ou lors de la {% link_new génération de missions | features/scheduling/schedules/schedules-shift-bidding.md %}.
- Cadre de disponibilité&nbsp;: si les heures d’ouverture de votre unité opérationnelle s’étendent sur une période plus longue qu'une journée de travail, vous pouvez limiter les options de planification des employés dans injixo. Pour limiter la disponibilité de plusieurs employés à la fois, utilisez des modèles horaires de type Cadre de disponibilité et ajoutez-les aux rotations d’horaires. Vous pouvez également {% link_new configurer les disponibilités pour chaque employé | features/administration/availabilities.md %} individuellement dans les paramètres des employés. Les deux sont pris en compte lors de l’optimisation du planning si la règle de planification _2611_{:.id-label} est activée.

Vous pouvez également utiliser des {% link_new rotations d’horaires | features/administration/shift-sequences.md %} ou des modèles hebdomadaires dans les {% link_new modèles de planification | features/administration/modeles-hebdomadaires.md %}. Vous pouvez également utiliser les deux pour alterner les journées du matin et du soir, par exemple.

Nous recommandons de créer un ensemble limité de modèles horaires variables (combinés avec les {% link_new disponibilités de vos employés | features/administration/availabilities.md | #create-employee-availabilities %}) plutôt que de créer un grand nombre de modèles horaires fixes.

## Activité de base et durée de la journée

Pour les modèles horaires fixes et variables, vous devez toujours configurer une activité de base pour chaque modèle horaire afin de définir la durée totale de la journée. Vous pouvez ajouter des activités supplémentaires qui couvrent l’activité de base dans les deux types de modèles horaires. La durée des activités supplémentaires ne doit pas dépasser celle de l’activité de base.

L’activité de base couvre la durée totale pendant laquelle un employé planifié est présent pendant une journée, y compris les pauses et autres activités non rémunérées. Il s’agit de la première activité à sélectionner lors de la création d’un nouveau modèle horaire. Après avoir enregistré le modèle horaire, vous ne pouvez ni la supprimer ni la modifier.

Le temps total d’une journée planifiée est la durée brute de la journée, pauses incluses. Après déduction des activités non rémunérées, telles que les pauses ou les temps de préparation, la durée de travail résultante est la durée nette de la journée. Vous pouvez voir la durée nette de la journée sous le nom Horaires effectifs dans Schedules et dans le Centre de planification. Remarque&nbsp;: les contrats spécifient également les temps nets. 

La durée d’un modèle horaire doit être conforme aux heures de travail indiquées dans vos {% link_new contrats | features/administration/create-contracts.md %}.
Par exemple, un contrat de 35&nbsp;heures par semaine sur 5&nbsp;jours nécessite un modèle horaire dont la durée de travail nette est de 7&nbsp;heures. Un contrat de 37,5&nbsp;heures nécessite une durée de travail nette de 7,5&nbsp;heures.

Utilisez l’activité Présent comme activité de base et assurez-vous qu’elle est configurée comme Remplaçable. Les fonctionnalités Optimiser les activités et Optimiser le planning peuvent ensuite remplacer l’activité Présent par d’autres activités, à condition que {% link_new le besoin en personnel | features/forecast/injixo-forecast/staff-requirement.md %} de ces autres activités soit calculé et qu'elles soient configurées comme Planifiables automatiquement.

### Éléments fixes et corridors

Vous pouvez créer un élément de corridor si vous ajoutez une activité d’une durée plus courte que la durée entre le début et la fin de l’élément. Les éléments de corridor superposent tous les éléments fixes dans une journée. L’optimisation du planning permettra de déplacer les éléments du corridor afin d’optimiser la couverture. Les corridors peuvent se chevaucher, mais pas les activités à l’intérieur de deux corridors.

Lorsque vous insérez manuellement un modèle horaire dans le planning, les éléments du corridor sont placés le plus tôt possible dans le corridor. Vous pouvez déplacer manuellement les corridors dans leurs intervalles définis.

Lorsque la durée d’un élément de corridor correspond exactement à l’élément d’heure de début et de fin configuré, un élément fixe est créé à la place.

