---
title: Combiner les méthodes de planification
product_label:
  - advanced
  - enterprise
  - classic
description: Combinez les différentes méthodes de planification pour répondre aux besoins de votre organisation.
---

Vous pouvez combiner toutes les {% link_new méthodes de planification | features/scheduling/scheduling-methods.md %} de différentes façons pour équilibrer les besoins des conseillers et les contraintes de votre organisation.

Les exemples suivants illustrent plusieurs combinaisons possibles entre les méthodes de planification. Vous pouvez les utiliser telles qu’elles sont présentées ici ou vous en inspirer pour créer vos propres combinaisons.

## Planification fixe et roulements/horaires totalement flexibles

Si vous souhaitez une majorité de plannings flexibles, vous pouvez assigner des modèles de planification aux conseillers avec un cycle flexible. Si le planning de certains conseillers contient des restrictions strictes ou si vous souhaitez récompenser les meilleurs conseillers ou les plus expérimentés, vous pouvez définir des rotations d’horaires pour ceux-ci.

Lors de la planification, commencez par insérer vos rotations d’horaires, puis lancez une optimisation du planning. Vos roulements ou vos horaires flexibles seront optimisés selon la couverture prévue par vos rotations d’horaires.

Si certains conseillers doivent travailler certains jours de la semaine, vous pouvez également créer une rotation d’horaires qui définit ces jours. Les jours restants doivent rester vides. Vous devez ensuite assigner un modèle de planification au conseiller concerné.

Lorsque vous insérez la rotation et lancez une optimisation complète, les jours vides seront remplis par les horaires ou les roulements flexibles conformément aux règles des contrats pour créer un planning complet.

## Roulements flexibles et horaires totalement flexibles

Si vous souhaitez que certains conseillers travaillent selon un planning en roulement, et d’autres de manière plus flexibles sur certains jours de la semaine, assignez le modèle de planification B ou D aux conseillers en roulement et le modèle de planification A à tous les autres.
Les conseillers en roulement suivront le roulement défini, tandis que l’optimisation planifiera les employés flexibles de manière à répondre à vos autres besoins.

## Roulements flexibles et disponibilités

Si un conseiller travaille sur un planning en roulement, mais que ses disponibilités sont restreintes sur certaines heures (par exemple, il ne peut pas travailler après 17h00 le mercredi), définissez la restriction et assignez-lui un modèle de planification.

Sur les semaines pendant lesquelles le conseiller travaille le matin, ses disponibilités permettront de le planifier les mercredis. Cependant, sur les semaines pendant lesquelles il travaille le soir, ses disponibilités l’empêcheront d’être planifié les mercredis. Le moteur d’optimisation lui attribuera des horaires sur les autres jours de la semaine.

## Planification fixe et disponibilités

Vous pouvez ajouter des modèles horaires de type Période de disponibilité dans les rotations d’horaires pour influencer la planification sur certains jours. Vous trouverez ci-dessous deux exemples possibles.

**Journées de travail un week-end sur deux**&nbsp;:

1. Créez un modèle horaire de type Cadre de disponibilité avec un cadre temporel de 0h00 à 0h01 comme bloqueur.
2. Ajoutez le modèle horaire dans une rotation d’horaires un week-end sur deux (laissez les autres jours vides).
3. Assignez la rotation d’horaires aux conseillers et insérez la rotation avant de lancer l’optimisation.

injixo ne planifie le conseiller qu’un week-end sur deux et optimise les autres jours.

**Travail de nuit une semaine sur deux**&nbsp;:

1. Créez un modèle horaire de type Cadre de disponibilité avec un cadre temporel de 12h00 à 0h00 comme bloqueur.
2. Ajoutez le modèle horaire pour chaque jour de la semaine dans une rotation d’horaires (laissez les autres jours vides).
3. Assignez la rotation d’horaires aux conseillers et insérez-la avant de lancer l’optimisation.

injixo planifiera les horaires de nuit pour le conseiller sur les semaines où celui-ci est disponible (conformément au modèle de planification). Pour les autres semaines, injixo planifie d’autres horaires.
