---
title: Créer des modèles de planification
redirect_from:
  - /fr/wtpm_creating/
  - /fr/week_time_patterns/
  - /fr/wtpm_overview.md/
  - /fr/understanding_wtpms/
product_label:
  - advanced
  - enterprise
  - classic
description: Utilisez les modèles de planification pour l’optimisation de votre planning afin de vous assurer que les employés ne se voient pas simplement attribuer des journées aléatoires.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Planifier des journées doubles
    filepath: best-practices/scheduling-split-shifts.md
---

Un modèle de planification est composé de [modèles hebdomadaires](#créer-un-modèle-hebdomadaire) et définit la façon dont les {% link_new modèles horaires | features/administration/daymodels/daymodel-basics.md %} sont assignés à vos employés.

L’image ci-dessous illustre la configuration des modèles horaires et des modèles hebdomadaires dans un modèle de planification.

{{ 1 | image: 'Structure d’un modèle de planification' }}

Les modèles de planification vous permettent de créer des cycles de journées et de définir des contraintes de planification pour la fonctionnalité **Optimiser le planning**.<br>
Voici les avantages des modèles de planification&nbsp;:

- Ils définissent les modèles horaires à utiliser pour planifier un employé.
- Les journées ne sont pas assignées aux employés de manière aléatoire.
- Ils définissent l’heure de début des journées.
- Ils définissent l’ordre d’assignation des modèles horaires.

Au lieu d’utiliser les modèles de planification, vous pouvez également utiliser les rotations d’horaires ou configurer les {% link_new disponibilités | features/administration/availabilities.md %} de vos employés.

## Prérequis

Pour pouvoir utiliser les modèles de planification, assurez-vous&nbsp;:
- d’avoir créé des {% link_new modèles horaires | features/administration/daymodels/daymodel-creation.md %} et des [modèles hebdomadaires](#créer-un-modèle-hebdomadaire), et d’avoir assigné des modèles horaires aux modèles hebdomadaires,
- que chaque modèle de planification contient au moins un modèle hebdomadaire,
- que chaque modèle hebdomadaire contient au moins un {% link_new modèle horaire | features/administration/daymodels/daymodel-basics.md %},
- d’avoir assigné des modèles de planification à vos employés.

## Créer un modèle hebdomadaire

Un modèle hebdomadaire est un ensemble de modèles horaires. Vous pouvez regrouper les modèles horaires sur la base de n’importe quel critère, par exemple par durée des journées, par activités, par heure de début, etc.<br>

Vous pouvez uniquement utiliser les modèles hebdomadaires dans un modèle hebdomadaire. Pour une semaine de travail, injixo planifiera les employés selon les modèles horaires inclus dans le modèle de planification. Ainsi, vous pouvez garantir des heures de travail plus justes et plus régulières pour vos employés.

Pour créer un modèle hebdomadaire, suivez ces étapes&nbsp;:

1. Accédez à _Plan > Configuration > Modèles hebdomadaires_{:.breadcrumbs}.
2. Cliquez sur l’icône Créer {% icon item-add | icon-only %} dans la barre d’action.
    Un panneau de configuration s’ouvre à droite.
3. Configurez les paramètres du modèle hebdomadaire&nbsp;:<br>
  **Nom**&nbsp;: saisissez un nom unique (50 caractères maximum).<br>
  **Abréviation**&nbsp;: saisissez le nom ou une version plus courte de celui-ci (25 caractères maximum).<br>
  **Couleur**&nbsp;: la couleur peut vous aider à identifier le modèle hebdomadaire dans une liste, par exemple.<br>
  **Nombre max. de jours dérogatoires par semaine**&nbsp;: les [jours dérogatoires](#jours-dérogatoires) permettent à injixo de contourner les règles du modèle de planification pour mieux couvrir le besoin en personnel.
4. Cliquez sur _OK_{:.doc-button}.

Vous pouvez maintenant ajouter des modèles horaires à votre modèle hebdomadaire.

### Ajouter des modèles horaires à un modèle hebdomadaire

1. Dans le panneau de configuration du modèle hebdomadaire, accédez à la section **Modèles horaires** et cliquez sur l’icône Ajouter {% icon item-add | icon-only %}.
2. Sélectionnez un ou plusieurs modèles horaires dans la liste.
3. Cliquez sur _OK_{:.doc-button}.

Vous pouvez ajouter des {% link_new modèles horaires fixes et variables | features/administration/daymodels/daymodel-basics.md | #types-de-modèles-horaires %} à un modèle hebdomadaire. Si vous utilisez des modèles horaires variables, la fonctionnalité **Optimiser le planning** peut déterminer l’heure de début optimale des journées en respectant les contraintes définies par le modèle horaire.

> Remarque
>
> injixo peut uniquement planifier les modèles horaires assignés à l’unité opérationnelle à laquelle appartient l’employé. Si vous avez {% link_new limité les modèles horaires | features/administration/create-and-manage-planning-units.md | #limiter-les-modèles-horaires %} dans votre unité opérationnelle, les modèles horaires prévus par votre modèle de planification ne peuvent pas être utilisés.
>
> injixo peut remplacer les activités remplaçables par des activités planifiables dans une journée. Utilisez des modèles horaires variables pour chaque durée de journée requise par un contrat et utilisez l’activité système Présent (ID&nbsp;: 1) comme {% link_new activité de base | features/administration/daymodels/daymodel-basics.md | #activité-de-base-et-durée-de-la-journée %}. Ne définissez pas de modèles horaires pour chaque activité individuellement.

## Créer un modèle de planification

1. Accédez à _Plan > Configuration > Modèles de planification_{:.breadcrumbs}.
2. Cliquez sur l’icône Ajouter {% icon item-add | icon-only %} dans la barre d’action.
3. Configurez les paramètres du modèle de planification&nbsp;:<br>
  **Nom**&nbsp;: saisissez un nom unique (50 caractères maximum).<br>
  **Abréviation**&nbsp;: saisissez le nom ou une version plus courte de celui-ci (25 caractères maximum).<br>
  **Couleur**&nbsp;: la couleur peut vous aider à identifier le modèle de planification dans une liste, par exemple.<br>
  **Type**&nbsp;: le [type](#types-de-modèles-de-planification) détermine comment injixo utilise le modèle de planification.<br>
  **Modèle hebdomadaire pour les jours dérogatoires**&nbsp;: sélectionnez le modèle hebdomadaire à planifier pour les [jours dérogatoires](#jours-dérogatoires).
4. Cliquez sur _OK_{:.doc-button}.

Vous pouvez maintenant ajouter des modèles hebdomadaires à votre modèle de planification.

### Ajouter un modèle hebdomadaire à un modèle de planification

1. Dans la fenêtre de configuration du modèle de planification, cliquez sur l’icône Ajouter {% icon item-add | icon-only %} dans la section **Modèles hebdomadaires**.
2. Sélectionnez un **modèle hebdomadaire** dans la liste.
3. Définissez une **position**.<br>
  Si vous ajoutez plusieurs modèles hebdomadaires, cliquez sur l'icône Vers le bas {% icon down-arrow-blue | icon-only %} et Vers le haut {% icon up-arrow-blue | icon-only %} pour modifier la position.
4. Cliquez sur _OK_{:.doc-button}.

### Position

La position des modèles hebdomadaires dans les modèles de planification est pertinente si vous utilisez les modèles de planification de [type B ou D](#types-de-modèles-de-planification). injixo assignera les modèles hebdomadaires dans l’ordre configuré ici.

Utilisez les icônes Vers le bas {% icon down-arrow-blue | icon-only %} et Vers le haut {% icon up-arrow-blue | icon-only %} pour définir la position des modèles hebdomadaires.
## Types de modèles de planification

| Type | Name               | Utilisation des modèles hebdomadaires                                                      | Assignation de modèles horaires | Heure de début de la journée              | Résultat             |
| ---- | ------------------ | -------------------------------------------------------------------------- | -------------------- | ----------------------------- | --------------------------------- |
| A    | Sélection flexible | injixo peut sélectionner n’importe quel modèle horaire de n’importe quel modèle hebdomadaire pour chaque jour de la semaine. | injixo peut utiliser n’importe quel modèle horaire de n’importe quel modèle hebdomadaire. | Flexible     | Selon les horaires d’ouverture de votre centre de contacts, le type A peut donner lieu à une distribution des journées qui peut sembler aléatoire ou stressante pour vos employés. Par exemple, un employé peut travailler la matinée le lundi, la soirée le mardi et l’après-midi le mercredi, etc. |
| B    | Roulement fixe     | injixo planifie les modèles hebdomadaires dans l’ordre défini par leur position. | Pour chaque semaine, injixo sélectionne le modèle horaire qui couvre le besoin en personnel de manière optimale. | Fixe    | Le même modèle horaire est assigné à chaque employé pour toute la semaine, par exemple en commençant à 9h00 du lundi au vendredi. Définissez des [jours dérogatoires](#jours-dérogatoires) si vous souhaitez planifier un autre modèle horaire. Le roulement fixe est l’assignation de journées la plus régulière des quatre types. |
| C    | Roulement variable  | injixo ne prend pas en compte la position définie des modèles hebdomadaires. | injixo sélectionne un modèle horaire pour l’ensemble de la semaine. | Fixe    | Le modèle hebdomadaire qui couvre au mieux le besoin en personnel peut être assigné aux employés. Étant donné que les journées commencent à la même heure, les heures de travail des employés sur la semaine sont cohérentes. |
| D    | Roulement combiné (A/B) | injixo prend en compte la position définie pour les modèles hebdomadaires. | injixo sélectionne un modèle horaire pour l’ensemble de la semaine.| Flexible (avec cadre temporel)    |  Selon le besoin en personnel, injixo peut planifier des employés sur des journées du matin commençant entre 8h et 10h. Avec le type D, injixo peut les planifier de manière plus flexible pour couvrir le besoin en personnel de manière optimale, tout en assignant des plannings cohérents à vos employés. |

Le graphique suivant illustre la façon dont les différents types de modèles de planification influencent votre planning. Cet exemple inclut un modèle de planification avec quatre modèles hebdomadaires et trois modèles horaires dans chaque modèle hebdomadaire.

{{ 2 | image: 'Exemple de planning avec les différents types de modèles de planification' }}

## Jours dérogatoires

Les jours dérogatoires permettent de contourner les règles définies par le [type de modèle de planification](#types-de-modèles-de-planification) utilisé. Par exemple, vous pouvez utiliser des jours dérogatoires pour planifier le travail de nuit sur une semaine durant laquelle l’employé travaille normalement le matin.<br>

Les jours dérogatoires prennent en compte en priorité le besoin en personnel et permettent une meilleure couverture. Cependant, les plannings de vos employés seront moins réguliers.

Pour planifier des jours dérogatoires, suivez ces étapes&nbsp;:

1. [Créez un modèle hebdomadaire distinct](#créer-un-modèle-hebdomadaire) et ajoutez-le aux modèles horaires que vous souhaitez utiliser comme exceptions.
2. Dans la fenêtre de configuration des modèles hebdomadaires que vous souhaitez utiliser pour une journée type, définissez le nombre de jours dérogatoires par semaine.
3. Dans la fenêtre de configuration du modèle de planification, sélectionnez le modèle hebdomadaire que vous souhaitez utiliser pour les jours dérogatoires.

Lors de la sélection d’un modèle horaire pour la semaine, injixo ne peut pas utiliser les modèles horaires définis pour les jours dérogatoires. Assurez-vous que toutes les données de configuration requises pour la planification (c’est-à-dire tous les modèles horaires utilisés, ainsi que le modèle de planification) sont conformes aux {% link_new indications des temps de travail | features/administration/create-contracts.md | #indications-des-temps-de-travail %} définies dans le contrat de l’employé. Si le modèle horaire utilisé pour la semaine correspond au contrat, injixo peut remplacer le modèle horaire original avec un modèle horaire défini pour les jours dérogatoires, pour mieux couvrir le besoin en personnel.

## Assigner des modèles de planification aux employés

1. Accédez à _Plan > Configuration > Employés_{:.breadcrumbs}.
2. Sélectionnez un employé dans la liste.
3. Cliquez sur l’icône Ajouter {% icon item-add | icon-only %} dans la section **Modèles de planification**.<br>
   Un panneau de configuration s’ouvre à droite.
4. Configurez les paramètres&nbsp;:<br>
  **Valide du/Valide jusqu’au**&nbsp;: définissez une {% link_new période de validité | features/administration/set-a-validity-period.md %}.<br>
  **Modèle de planification**<br>
  **Date de référence**&nbsp;: définissez une date de référence qui définit le premier jour du modèle de planification.
5. Cliquez sur _OK_{:.doc-button}.

Utilisez la fonctionnalité de {% link_new mise à jour en masse | features/administration/mass-update.md %} pour assigner un modèle de planification à plusieurs employés en une fois.

> Attention lors de l’utilisation de la mise à jour en masse pour l’assignation de modèles de planification de type B
>
> Si vous utilisez la fonctionnalité de mise à jour en masse et définissez la même date de référence pour tous les employés, tous les employés seront planifiés à l’aide du même modèle hebdomadaire en même temps.
>
> À la place, sélectionnez des groupes plus petits pour la mise à jour en masse et définissez les lundis suivants comme dates de référence pour ces groupes. Ainsi, chaque groupe commencera sa rotation sur une semaine différente.

## Exemples

### Exemple A&nbsp;: roulement fixe avec matinées et après-midi

Utilisez un modèle de planification de type B (roulement fixe) et assignez-y trois modèles hebdomadaires différents&nbsp;. Assurez-vous de définir la position des modèles hebdomadaires.

- Le modèle hebdomadaire 1 (position 1) contient les modèles horaires pour les matinées (les journées commencent entre 7h et 9h).
- Le modèle hebdomadaire 2 (position 2) contient les modèles horaires pour les soirées (les journées terminent à 23h).
- Le modèle hebdomadaire 3 (position 3) contient les modèles horaires pour les après-midi (les journées commencent entre 11h et midi).

Avec ce modèle de planification, les employés seront en roulement régulier entre une semaine de matinées, une semaine de soirées et une semaine d’après-midis. 

Bien qu’une certaine flexibilité soit requise, les employés ont des heures de travail de travail régulières tout au long de la semaine.

### Exemple B&nbsp;: jours dérogatoires pour les soirées

Configurez un modèle de planification avec trois modèles hebdomadaires différents. Configurez un maximum de deux jours dérogatoires par semaine.

- Le modèle hebdomadaire 1 contient les modèles horaires pour les matinées.
- Le modèle hebdomadaire 2 contient les modèles horaires pour les soirées.
- Le modèle hebdomadaire 3 contient les modèles horaires pour les nuits (sélectionnez-le depuis le menu déroulant **Modèle hebdomadaire pour les jours dérogatoires**).

Avec ce modèle de planification, les employés alterneront entre des matinées pendant la première semaine et des soirées la semaine suivante. Cependant, comme vous avez défini deux jours dérogatoires, les employés peuvent recevoir deux nuits par semaine, si cela permet de couvrir le besoin en personnel de manière optimale.

<!-- TODO: very special example, add some more context  -->
<!-- ### Example: Performance-Based Scheduling With WTPMs and Preferred Day Models

Use Work Time Pattern Models and preferred day models  for Performance-Based Shift Assignment.

* Within the Week Time Patterns, assign the shifts according to agents' performance.
* Assign the Work Time Pattern Model to an agent with a validity period. Adjust it regularly according to performance scores.

For your high achievers you can pick some of the day models and assign them directly to these employees as personal day models. The AutoScheduler will only use these day models while generating schedules. This ensures that out-of-favor shifts are not assigned to high performing agents. -->

<!-- TODO: Example: normal use case scheduling different hours or working days in different weeks -->
<!-- ### Example: Scheduling Different Number of Working Days or Hours in Different Weeks -->
<!-- There is a bad German article /de/scheduling-different-wtm/ using WTPM Type B with two WTMs 4x10 and 5x8 hour shifts, with Autoscheduler contract parameter. minimum days per week with value 4 and scheduling parameter 2602 with value 10:00 -->
