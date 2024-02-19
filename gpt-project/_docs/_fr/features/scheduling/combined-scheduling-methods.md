---
title: Combiner les méthodes de planification
product_label:
  - advanced
  - enterprise
  - classic
description: Combinez les différentes méthodes de planification pour répondre à vos besoins organisationnels.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/availabilities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-time-pattern-models.md
---

Vous pouvez combiner toutes les méthodes de planning de nombreuses façons pour créer des plannings permettant d’obtenir un équilibre entre les besoins de vos employés et ceux de votre organisation.

Les exemples suivants illustrent certains scénarios courants de combinaison des méthodes de planification. Vous pouvez également utiliser d’autres combinaisons de méthodes de planification pour répondre au mieux aux besoins de votre organisation.

## Scénario 1&nbsp;: employés avec horaires flexibles et employés avec heures ou jours de travail spécifiques  

Pour ce scénario, vous pouvez combiner la planification fixe avec des roulements flexibles ou des horaires totalement flexibles.

Pour planifier vos employés à l’aide de cette combinaison, vous devez d’abord paramétrer les données de configuration indiquées dans le tableau suivant et les assigner aux employés concernés&nbsp;:


| Employés avec horaires flexibles            | Employés travaillant sur des créneaux ou des jours spécifiques                                                                                                                |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Assignez aux employés le modèle de planification que vous souhaitez utiliser. | Créez des rotations d’horaires qui définissant les horaires ou les jours sur lesquels ils doivent travailler et laissez le reste de la semaine vide. <br>Assignez aux employés la rotation d’horaires et les modèles de planification pertinents.                                     |

Pour planifier vos employés, suivez ces étapes&nbsp;:

1. Insérez vos rotations d’horaires.
2. Utilisez la fonctionnalité **Optimiser le planning**.<br>injixo planifiera vos rotations et horaires totalement flexibles pour compléter la couverture fournie par les rotations d’horaires.


## Scénario 2&nbsp;: employés en roulement et employés avec horaires fixes

Pour ce scénario, vous pouvez combiner la planification fixe avec des roulements flexibles ou des horaires totalement flexibles.

Pour planifier vos employés à l’aide de cette combinaison, vous devez d’abord assigner les données de configuration aux employés concernés, comme indiqué dans le tableau ci-dessous&nbsp;:

| Employés avec roulements flexibles           | Employés avec horaires totalement flexibles                                                                                                                |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Assignez-leur des modèles de planification de type B ou D. | Assignez-leur des modèles de planification de type A.                                   |


Utilisez la fonctionnalité **Optimiser le planning**.<br>Les employés avec rotations flexibles se verront assigner la rotation définie par leurs modèles de planification et ceux avec des horaires totalement flexibles seront assignés au reste du planning.

## Scénario 3&nbsp;: employés avec rotations et disponibilité limitée

Ce scénario concerne les employés qui travaillent en rotation mais qui se sont pas disponibles sur certains créneaux. Par exemple, ne pouvant pas travailler après 17h le mercredi.

Pour ce scénario, vous pouvez combiner les disponibilités et les rotations flexibles. 

1. Configurez les {% link_new disponibilités | features/administration/availabilities.md %} qui définissent quand vos employés ne peuvent pas travailler. Dans le cas présent, ils sont disponibles le mercredi seulement jusqu’à 17h.
2. Assignez-leur les modèles de planification concernés.

Pour les semaines sur lesquelles les employés travaillent le matin, ils seront planifiés le mercredi.<br>Pour les semaines sur lesquelles les employés travaillent le soir, ils ne seront pas planifiés le mercredi et seront planifiés les autres jours de la semaine.

## Scénario 4&nbsp;: employés avec horaires fixes et contraintes de disponibilité ponctuelles 

Ce scénario concerne les employés qui travaillent en horaires fixes, mais ayant une disponibilité plus restreinte sur certains jours, par exemple en travaillant la nuit pendant le week-end, mais uniquement un week-end sur deux.

Pour ce scénario, vous pouvez ajouter des {% link_new modèles horaires de type Période de disponibilité | features/administration/daymodels/daymodel-basics.md | #types-de-modèles-horaires %} aux {% link_new rotations d’horaires | features/administration/shift-sequences.md %} pour influencer les résultats de planification sur certains jours.<br>Vous trouverez ci-dessous deux exemples possibles.

Pour planifier les employés un week-end sur deux, suivez ces étapes&nbsp;:

1. Créez un modèle horaire de type Période de disponibilité avec un cadre temporel de minuit (0:00) à 0:01, qui servira de bloqueur.
2. Ajoutez le modèle horaire à un week-end dans une rotation d’horaires de 14 jours et laissez les autres jours vides.
3. Assignez la rotation d’horaires aux employés concernés.
4. Insérez la rotation d’horaires dans votre planning.
5. Utilisez la fonctionnalité **Optimiser le planning**.

injixo ne planifie aucune journée un week-end sur deux, et optimise les jours restants.

Pour planifier les employés de nuit une semaine sur deux, suivez ces étapes&nbsp;:

1. Créez un modèle horaire de type Période de disponibilité avec un cadre temporel de minuit (0:00) à midi (12:00).
2. Ajoutez le modèle horaire à chaque jour de la semaine dans une rotation d’horaires de 14 jours et laissez tous les autres jours vides.
3. Assignez la rotation d’horaires aux employés concernés.
4. Insérez la rotation d’horaires dans votre planning.
5. Utilisez la fonctionnalité **Optimiser le planning**.

injixo planifie les nuits pour le semaines pendant lesquelles les employés sont disponibles, en suivant le modèle de planification assigné à chaque employé. Pour les autres semaines, injixo peut planifier n’importe quelle journée conforme au modèle de planification.
