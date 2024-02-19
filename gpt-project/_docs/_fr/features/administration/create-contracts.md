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

Dans _Plan > Configuration > Contrats_{:.breadcrumbs}, vous pouvez saisir les contrats pour les employés que vous souhaitez planifier. Vous pouvez créer un nombre illimité de contrats. Les contrats vous permettent de définir des contraintes de temps pour la planification&nbsp;:

- le nombre minimum et maximum de jours de travail par semaine,
- le nombre minimum, cible et maximum d’heures de travail par jour,
- le nombre minimum, cible et maximum d’heures de travail par semaine,
- le nombre d’heures de travail maximum par jour.

Les contrats reflètent également des informations sur les politiques de temps de travail dans votre organisation, par exemple le nombre de jours de repos entre les journées. Vous pouvez également définir des paramètres de planification pour la fonctionnalité **Optimiser le planning**.

## Créer un contrat

Pour créer un contrat, accédez à _Plan > Configuration > Contrats_{:.breadcrumbs} et suivez les étapes ci-dessous&nbsp;:

1. Cliquez sur l’{% icon item-add %} en haut à gauche.
2. Dans la section **Généralités**, saisissez les informations de base pour le contrat&nbsp;:<br>
    - **Nom**&nbsp;: saisissez un nom unique (50 caractères maximum).
    - **Abréviation**&nbsp;: saisissez le nom ou une version plus courte de celui-ci (25 caractères maximum).
    - **Couleur**&nbsp;: la couleur peut notamment vous aider à identifier le contrat.
3. Dans la section **Jours trav. par sem.**, entrez le nombre de jours de travail par semaine.
4. Dans la section **Calcul des jours travaillés**, choisissez une méthode de calcul&nbsp;: <br>
    - **Standard** respecte l'ordre des jours dans la semaine de planification.<br>
    - **Flexible** choisit librement les jours de travail dans le cadre des heures d’ouverture de l’unité opérationnelle.
5. Entrez les [**Indications des temps de travail**](#indications-des-temps-de-travail) et la [**Répartition sur les jours de la semaine**](#répartition-sur-les-jours-de-la-semaine).
6. (Facultatif) Configurez les [**paramètres de l’AutoScheduler**](#paramètres-de-lautoscheduler) ou les [**Paramètres de planification**](#règles-de-planification).
7. Pour enregistrer votre contrat, cliquez sur _OK_{:.doc-button}.

## Indications des temps de travail

Les indications des temps de travail pour le nombre d’heures minimum, cible et maximal sont essentielles pour la planification. Les indications des temps de travail fonctionnent de pair avec les paramètres de planification et les paramètres de l’AutoScheduler.

### Jour

- **Minimum**&nbsp;: saisissez le nombre minimum d’heures de travail par jour. Si vous ne saisissez aucune valeur, le temps cible sera considéré comme le minimum. Ce paramètre est contrôlé par le paramètre de planification _2615_{:.id-label}.
- **Cible**&nbsp;: saisissez le nombre d’heures de travail cible par jour. Saisissez une valeur comprise entre 0 et 24&nbsp;heures et tenez compte des horaires de travail standard.
- **Maximum**&nbsp;: saisissez le nombre maximum d’heures de travail par jour. Si vous ne saisissez aucune valeur, le temps cible sera considéré comme le maximum. Ce paramètre est contrôlé par le paramètre de planification _2614_{:.id-label}.

### Semaine

- **Minimum**&nbsp;: saisissez le nombre minimum d’heures de travail par semaine. Vous pouvez définir le début de la semaine de planification en utilisant paramètre _48420_{:.id-label}. Vous pouvez définir le nombre de jours dans un week-end avec le paramètre _48421_{:.id-label}.
- **Cible**&nbsp;: saisissez le nombre d’heures de travail cible par jour. Cette valeur est requise si vous ne saisissez aucune valeur dans **Répartition sur les jours de la semaine**. Vous pouvez définir le début de la semaine de planification en utilisant paramètre _48420_{:.id-label}.
- **Maximum**&nbsp;: saisissez le nombre maximum d’heures de travail par semaine. Ce paramètre est contrôlé par les paramètres de planification _2618_{:.id-label} et _2629_{:.id-label}. 

### Mois

- **Maximum**&nbsp;: saisissez le nombre d’heures de travail maximum par mois. Ce paramètre est contrôlé par le paramètre de planification _2619_{:.id-label}.


## Répartition sur les jours de la semaine

Vous pouvez définir le nombre d’heures de travail par jour pour les employés avec ce contrat. Dans la configuration des **Indications des temps de travail**, cette section est facultative. Cependant, elle est utile pour calculer les absences payées, telles que les vacances ou les maladies.

Exemple&nbsp;:
Un employé travaille 35&nbsp;heures par semaine et 7&nbsp;heures par jour avec des jours de repos le mercredi et le dimanche. Pour garantir une distribution adéquate sur la semaine, saisissez 7:00 dans les champs lundi, mardi, jeudi, vendredi et samedi et saisissez 0:00 dans les champs mercredi et dimanche. Si un employé tombe malade ou prend des jours de congés rémunérés, ses heures de travail seront calculées conformément aux temps saisis ici.

Si vous laissez un champ vide, injixo utilisera la formule par défaut&nbsp;: [Heures cibles hebdomadaires / Nombre de jours ouvrables]. Cela peut entraîner des erreurs de calcul car injixo considérera que la distribution des heures de travail doit être égale sur tous les jours de travail.

## Paramètres de l’AutoScheduler


- **Nbre max. de jours travaillés consécutifs**&nbsp;: remplissez ce champ si votre unité opérationnelle est ouverte 7 jours sur 7. Saisissez le nombre maximum de jours libres consécutifs que la fonctionnalité **Optimiser le planning** doit prendre en compte. Par exemple, si un employé travaille 5 jours par semaine, utilisez ce paramètre pour l’empêcher de travailler 10 jours consécutifs.
- **Nbre min. de jours libres par sem.**&nbsp;: remplissez ce champ si votre unité opérationnelle est ouverte le week-end. Saisissez le nombre minimum de jours libres consécutifs que la fonctionnalité **Optimiser le planning** doit prendre en compte pour chaque semaine de travail.
- **Nbre min. de jours libres consécutifs par sem.**&nbsp;: remplissez ce champ si vous voulez vous assurer que vos employés disposent d’au moins une période de jours de repos consécutifs par semaine. Saisissez le nombre minimum de jours de repos consécutifs que la fonctionnalité **Optimiser le planning** doit prendre en compte pour chaque semaine de planification.
- **Nbre max. de jours libres consécutifs**&nbsp;: remplissez ce champ si vous souhaitez limiter le nombre de jours de repos consécutifs pour vos employés pour garantir un niveau d’occupation cohérent et éviter des périodes de repos trop longues. Saisissez le nombre maximum de jours libres consécutifs que la fonctionnalité **Optimiser le planning** doit prendre en compte. La valeur n’est pas vérifiée par semaine mais sur plusieurs semaines.
- **Temps de repos min. (en heures) entre 2 missions**&nbsp;: remplissez si vous devez respecter le droit du travail concernant les périodes de repos entre les journées. Saisissez la période de repos minimale que la fonctionnalité **Optimiser le planning** doit prendre en compte entre deux journées consécutives.	
- **Nbre min. de jours travaillés par sem.**&nbsp;: remplissez ce champ pour maintenir un niveau d’occupation minimum par semaine dans votre unité opérationnelle. Ainsi, vous pouvez vous assurer que vous disposez toujours d’un nombre suffisant d’employés pour traiter les volumes d’appels prévus. Saisissez le nombre minimum de jours de travail à planifier par semaine de planification.
- **Détermination du temps de travail à planifier avec les comptes temps dû**&nbsp;: cochez cette case si vous souhaitez utiliser les valeurs des comptes temps dû calculés dans la fonctionnalité **Optimiser le planning**. En savoir plus sur les {% link_new comptes temps dû | features/scheduling/planning-periods/target-work-accounts.md %}.
- **Un samedi au max. travaillé toutes les n semaines**&nbsp;: remplissez ce champ si vous souhaitez garantir une distribution équitable du travail le week-end entre les employés et empêcher que les mêmes employés travaillent les samedis, par exemple. Saisissez le nombre maximum de semaines consécutives (1-5) pendant lesquelles un employé peut travailler le samedi. Par exemple, une valeur de 2 signifie un samedi sur deux.
- **Planification d’un jour de travail après un jour de congés complet**&nbsp;: remplissez ce champ si vous souhaitez forcer la fonctionnalité **Optimiser le planning** à planifier un jour de travail après un jour de congé entier. Si l’employé a plusieurs jours de congé consécutifs, la journée de travail est planifiée après le dernier jour de congé.

## Règles de planification

Les règles de planification sont un ensemble de règles générales et spécifiques aux contrats utilisées dans votre processus de planification. Dans la configuration du contrat, les règles de planification sont appelées paramètres de planification.

Pour voir la liste complète des règles de planification, accédez à _WFM > Administration > Système > Règles de planification_{:.breadcrumbs}. Pour voir la description d’une règle, cliquez sur la règle concernée dans la liste. Les règles de planification sont généralement configurées au cours de votre onboarding avec votre consultant injixo.

Les utilisateurs disposant d’un accès admin peuvent modifier chaque règle, définir des exceptions et rétablir les valeurs spécifiques à un utilisateur aux valeurs par défaut.

> Risque potentiel d’erreurs de planification
>
> Les modifications des règles de planification sont complexes et peuvent donner lieu à des erreurs de planification si elles ne sont pas effectuées correctement. Ne les modifiez pas vous-même si vous avez des doutes sur les conséquences. Si vous devez modifier une règle de planification, contactez votre consultant.

Les règles de planification spécifiques aux contrats garantissent que les conditions de chaque contrat sont prises en compte pendant la planification. Par exemple, si un contrat spécifie une certaine durée de la période de repos ou un nombre maximum d’heures de travail par jour, les règles de planification permettent de s’assurer que ces conditions sont satisfaites. La violation de ces règles peut entraîner des conflits de planification, l’insatisfaction des employés et, potentiellement, des violations des contrats.

### Indicateur de statut

Vous pouvez voir le statut de chaque règle de planification dans la liste&nbsp;:

  - Gris&nbsp;: la règle est désactivée et ne sera pas prise en compte pour la planification.
  - Jaune la règle est en mode mineur. Si cette règle est enfreinte, un message d’avertissement sera généré, mais l’action continuera.
  - Rouge&nbsp;: la règle est activée. En cas de violation du contrat, un message d’erreur comprenant des informations supplémentaires sera généré. 