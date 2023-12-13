---
title: Modèles hebdomadaires
---

## Définition
Les modèles hebdomadaires forment la base des modèles de planification. Le modèle hebdomadaire est un regroupement d'un ou plusieurs modèles horaires qui pourront être utilisés lors de l'optimisation.

## Rubrique Généralités
Voici les champs qui doivent être renseignés lors de la création d'un modèle hebdomadaire :

- Nom : indiquez un nom univoque pour le modèle hebdomadaire (50 caractères max.)
- Abréviation : indiquez une abréviation univoque pour le modèle hebdomadaire, qui sera utilisée ultérieurement dans l'affichage des autres modules (25 caractères max.)
- Couleur : sélectionnez une couleur dans la liste déroulante, dans laquelle le modèle hebdomadaire sera affiché dans les autres modules. Le blanc, le noir et le gris ne procurent aucun affichage optimal
- Nbre max. de jours dérogatoires par sem. : indiquez pour une période d'une semaine le nombre maximum de jours pour lesquels le moteur d'optimisation ne doit pas obligatoirement utiliser le modèle hebdomadaire concerné. Le moteur peut, ainsi, utiliser des modèles horaires (pour le nombre de jours indiqué et si la couverture du besoin de l'activité le nécessite), qui sont attribués aux autres modèles hebdomadaires du modèle de planification. Vous pouvez également indiquer dans le point de menu modèles de planification un modèle hebdomadaire qui sera spécialement utilisé aux jours dérogatoires.

{{ 1 | image: "WTP_creation", '75%' }}

## Rubrique Modèles horaires
C'est ici que vous pourrez attribuer les modèles horaires à utiliser lors de l'utilisation du modèle hebdomadaire par le moteur d'optimisation.
Cliquer sur le "+" de la section "Modèles horaires", une boite de dialogue s'ouvre et vous permet de sélectionner le ou les modèles horaires.

{{ 2 | image: "WTP_DM", '75%' }}

> Remarque
>
> N'attribuez au modèle hebdomadaire que des modèles horaires assignés à l'unité opérationnelle. Les modèles de planification qui contiennent des modèles horaires non assignés ne seront pas utilisés lors de l'optimisation.
