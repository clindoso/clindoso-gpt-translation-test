---
title: Créer des horaires adaptés à vos contrats
redirect_from:
  - /fr/creer-modeles-horaires-adaptes/
redirect_reason: Filename changed in April 2022
---

## Scénario

Vous souhaitez créer dans injixo des horaires de travail qui correspondent aux contrats de vos employés à temps plein ou à temps partiel.

Plusieurs contrats existent dans votre organisation, par exemple :

- 40 heures (5 x 8h)
- 32 heures (4 x 8h)
- 30 heures (5 x 6h)
- 24 heures (4 x 6h)
- 20 heures (5 x 4h)
- 12 heures (3 x 4h or 2 x 6h)

Dans cet exemple, votre centre de contact est ouvert de 7h à 19h. Les appels sont répartis selon une courbe classique en dos de chameau avec deux pics, un dans la matinée et l'autre dans l'après-midi.

> Remarque
>
> Par souci de simplicité, nous ne prenons pas en compte les pauses dans cet exemple. Lorsque vous créez des modèles horaires, vous devez prendre en compte les pauses et les ajouter au temps de travail total. Par exemple, une pause non rémunérée de 30 minutes par jour augmente le temps de travail total d'un employé de la même durée.

## Modélisation dans injixo

Les horaires de travail sont modélisés dans injixo avec les {% link_new Modèles horaires | features/administration/daymodels/daymodel-creation.md %}.
Les Modèles horaires sont combinés avec les {% link_new Contrats | features/administration/create-contracts.md %} pour déterminer les horaires sur lesquels un employé peut travailler.
Les Modèles horaires sont assignés à une {% link_new Unité opérationnelle | features/administration/create-and-manage-planning-units.md %}.
Vous pouvez utiliser ces Modèles horaires dans différentes {% link_new méthodes de planification | features/scheduling/scheduling-methods.md %} pour créer vos plannings. Vous pouvez également {% link_new combiner les méthodes de planification | features/scheduling/combined-scheduling-methods.md %} pour couvrir l'ensemble de vos contraintes.

## Approche recommandée

Il convient dans un premier temps d'identifier quel contrat est attribué à chaque employé puis vous pouvez démarrer la création de vos Modèles horaires :

1. Créer un Modèle horaire variable unique pour tous les horaires de travail avec le même nombre d'heures travaillées par jour. Le nombre de jours travaillés et le nombre d'heures totales par semaine sont déterminés par le contrat de l'employé.

   En théorie, les contrats de 12h, 24h et 30h peuvent être gérés avec un unique Modèle horaire variable de 6 heures entre 7h et 19h si les employés travaillent le même nombre d'heures par jour.<br><br>

   En réalité, les contrats offres souvent plus de flexibilité, permettant aux employés de travailler plus ou moins d'heures par jour. Par exemple, vos employés peuvent travailler entre 6h et 8h par jour avec un objectif de 37,5h par semaine. En conséquence, selon votre flexibilité, plusieurs modèles horaires peuvent être nécessaires.<br><br>

2. Définir pour tous vos modèles horaires :

   - Le nombre total d'heures travaillées
   - Le nombre, le positionnement et la durée des pauses
   - Toutes les activités fixes

3. Déterminer si les employés ont des horaires flexibles pour le début ou la fin de journée et, si oui, de quelle ampleur est cette flexibilité.

   En début et en fin de journée, le besoin en personnel est moindre. Des Modèles horaires variables avec des heures de début différentes améliorent votre couverture.

   Les horaires avec peu d'heures quotidiennes vous permettent de couvrir les pics d'appels alors que vos employés à temps plein sont suffisants pour couvrir la faible activité du déjeuner. Ainsi, les modèles horaires des employés à temps partiel sont positionnés dans la matinée ou l'après-midi afin de minimiser leur présence au milieu de la journée.

## Résultat

En définissant des Modèles horaires variables pour vos employés à temps partiel permettant de compléter la couverture assurée par vos employés à temps plein, vous avez créé tous les éléments assurant la génération d'un planning optimisé.

{{ 1 | image: 'Couverture', '75%' }}
