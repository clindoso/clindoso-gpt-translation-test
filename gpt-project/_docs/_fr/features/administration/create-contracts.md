---
title: Créer des contrats
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Créez des contrats afin de définir le temps de travail par semaine et d’autres règles pour vos employés.
redirect_from:
  - /fr/contracts-overview/
  - /fr/contract-creation/
redirect_reason: Updated filename on 08 December 2023
---

Dans _WFM > Administration > Planification > Contrats_{:.breadcrumbs}, vous pouvez saisir les contrats pour les employés que vous souhaitez planifier. Vous pouvez créer un nombre illimité de contrats. Les contrats vous permettent de définir des contraintes de temps pour la planification&nbsp;:

- le nombre minimum et maximum de jours de travail par semaine,
- le nombre minimum, à effectuer et maximum d’heures de travail par jour,
- le nombre minimum, à effectuer et maximum d’heures de travail par semaine.

Les contrats reflètent également des informations sur les politiques de temps de travail dans votre organisation, par exemple le nombre de jours de repos entre les journées. Vous pouvez également définir des paramètres de planification pour la fonctionnalité Optimiser le planning.

## Créer un contrat

1. Cliquez sur l’icône Créer {% icon item-add | icon-only %}.
2. Dans la section **Généralités**, saisissez les informations de base pour le contrat&nbsp;:<br>
    - Saisissez un **nom** (50 caractères maximum).
    - Saisissez une **abréviation** (25 caractères maximum).
    - Sélectionnez une **couleur**.
3. Dans la section **Jours trav. par sem.**, entrez le nombre de jours de travail par semaine.
4. Dans la section **Calcul des jours travaillés**, choisissez une méthode de calcul&nbsp;: <br>
    - **Standard** respecte l'ordre des jours dans la semaine de planification.<br>
    - **Flexible** choisit librement les jours de travail dans le cadre des heures d’ouverture de l’unité opérationnelle.
5. Entrez les [**Indications des temps de travail**](#indications-des-temps-de-travail) et la [**Répartition sur les jours de la semaine**](#répartition-sur-les-jours-de-la-semaine).
6. (Optionnel) Configurez les [**paramètres de l’AutoScheduler**](#paramètres-de-lautoscheduler) et les **Paramètres de planification**.
7. Pour enregistrer votre contrat, cliquez sur _OK_{:.doc-button}.

## Indications des temps de travail

Les indications des temps de travail pour le nombre d’heures minimum, à effectuer et maximal sont essentielles pour la planification. Les indications des temps de travail fonctionnent conjointement avec les Règles et Paramètres de planification.

### Jour

- **Minimum**&nbsp;: saisissez le nombre d’heures de travail minimum par jour. Si vous ne saisissez aucune valeur, le temps cible sera considéré comme minimum. Ce paramètre est contrôlé par la règle de planification _2615_{:.id-label}.
- **À effectuer**&nbsp;: saisissez le nombre d’heures de travail à effectuer par jour. Nous recommandons de saisir une valeur comprise entre 0 et 24 heures et de prendre en compte les horaires de travail standard.
- **Maximum**&nbsp;: saisissez le nombre d’heures de travail maximum par jour. Si vous ne saisissez aucune valeur, le temps à effectuer sera considéré comme maximum. Ce paramètre est contrôlé par la règle de planification _2614_{:.id-label}.

### Semaine

- **Minimum**&nbsp;: saisissez le nombre d’heures de travail minimum par semaine. Vous pouvez définir le début de la semaine de planification en utilisant paramètre _48420_{:.id-label}. Vous pouvez définir le nombre de jours dans un week-end avec le paramètre _48421_{:.id-label}.
- **À effectuer**&nbsp;: saisissez le nombre d’heures de travail à effectuer par semaine. Cette valeur est requise si vous ne saisissez aucune valeur dans Répartition sur les jours de la semaine. Vous pouvez définir le début de la semaine de planification en utilisant paramètre _48420_{:.id-label}.
- **Maximum**&nbsp;: saisissez le nombre d’heures de travail maximum par semaine. Ce paramètre est contrôlé par les règles de planification _2618_{:.id-label} et _2629_{:.id-label}. 

### Mois

- **Maximum**&nbsp;: saisissez le nombre d’heures de travail maximum par mois. Ce paramètre est contrôlé par la règle de planification _2619_{:.id-label}.


## Répartition sur les jours de la semaine

Vous pouvez définir le nombre d’heures de travail par jour pour les employés avec ce contrat. Si les directives de temps de travail sont configurées, vous n’avez pas besoin d’entrer de valeurs ici. Cependant, il est utile de calculer les absences payées, telles que les vacances ou les maladies.

Exemple&nbsp;: un employé a un jour de congé payé le vendredi et son contrat spécifie 8 heures sur les vendredis. 8 heures de travail seront comptabilisées pour cette journée.

Saisissez le nombre d’heures de travail maximum par jour. Pour les jours non travaillés, entrez 0:00 heures. Laisser un champ vide reviendra par défaut à la formule&nbsp;: [Heures à effectuer hebdomadaires / Nombre de jours ouvrables]. Cela peut conduire à des erreurs de calcul.

## Paramètres de l’AutoScheduler


- **Nbre max. de jours travaillés consécutifs**&nbsp;: saisissez le nombre maximum de jours de travail consécutifs que la fonctionnalité Optimiser le planning doit prendre en compte. Peut être vide pour les unités opérationnelles sans horaires d’ouverture le week-end. Par exemple, si une personne travaille 5 jours par semaine, utilisez ce paramètre pour l’empêcher de travailler 10 jours consécutifs.
- **Nbre min. de jours libres par sem.**&nbsp;: saisissez le nombre minimum de jours de travail consécutifs que la fonctionnalité Optimiser le planning doit prendre en compte pour chaque semaine de planification. Peut être vide pour les unités opérationnelles sans horaires d’ouverture le week-end.
- **Nbre min. de jours libres consécutifs par sem.**&nbsp;: saisissez le nombre minimum de jours libres consécutifs que la fonctionnalité Optimiser le planning doit prendre en compte pour chaque semaine de planification.
- **Nbre max. de jours libres consécutifs**&nbsp;: saisissez le nombre maximum de jours libres consécutifs que la fonctionnalité Optimiser le planning doit prendre en compte. La valeur n’est pas vérifiée par semaine mais sur plusieurs semaines.
- **Temps de repos min. (en heures) entre 2 missions**&nbsp;: saisissez la période de repos minimale que la fonctionnalité Optimiser le planning doit prendre en compte entre deux journées consécutives.	
- **Nbre min. de jours travaillés par sem.**&nbsp;: Saisissez le nombre minimum de jours de travail à planifier par semaine de planification.
- **Détermination du temps de travail à planifier avec les comptes temps dû**&nbsp;: cochez cette case si vous souhaitez utiliser les valeurs des comptes temps dû calculés dans la fonctionnalité Optimiser le planning. En savoir plus sur les {% link_new comptes temps dû | features/scheduling/planning-periods/target-work-accounts.md %}.
- **Un samedi au max. travaillé toutes les n semaines**&nbsp;: saisissez le nombre maximum de semaines (1-5) pendant lesquelles un employé peut travailler le samedi. Par exemple, une valeur de 2 signifie un samedi sur deux.
- **Planification d’un jour de travail après un jour de congés complet**&nbsp;: force la fonctionnalité Optimiser le planning à planifier une journée de travail après une journée complète de congé. Si l’employé a plusieurs jours de congé consécutifs, la journée de travail est planifiée après le dernier jour de congé.