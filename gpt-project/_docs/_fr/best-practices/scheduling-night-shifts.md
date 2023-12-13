---
title: Planification des équipes de nuit
redirect_from:
  - /fr/planification-nuit/
redirect_reason: Filename changed in April 2022
---

injixo vous offre plusieurs options adaptées à la plupart des façons de planifier le travail de nuit. Avant d'aller plus loin dans ces différentes options, il y a quelques limites générales à observer.

- La période de repos est vérifiée avant et après l’horaire de nuit, vous devez donc tenir compte de l'ensemble du contexte hebdomadaire.
- Si vous planifiez 24h/24, 7j/7, vous devez vous assurer qu’il existe bien un besoin en personnel pour le lundi de la semaine suivante. Sans cela, vos employés ne seront pas planifiés le lundi matin.

Pour qu'injixo ait la même compréhension des horaires de nuit que vous, vous devez régler les paramètres suivants (via le menu _WFM > Administration > Système > Configuration)_{:.breadcrumbs} :

_48161_{:.id-label} _Mode de définition du travail de nuit_<br>
_48121_{:.id-label} _Début de la période du travail de nuit_<br>
_48122_{:.id-label} _Amplitude de la période du travail de nuit_<br>
_48162_{:.id-label} _Heure de référence pour le travail de nuit_<br>

Vous pouvez utiliser les contrats pour apporter des restrictions supplémentaires au travail de nuit. Rappelez-vous que devez non seulement adapter les contrats (via le menu _Administration > Planification > Contrats_{:.breadcrumbs}), mais également les règles de planification (via le menu _Administration > Système > Règles de planification_{:.breadcrumbs}), que vou pourrez activer.
Ceci inclut les règles suivantes :

_2632_{:.id-label} _Nombre maximum de jours de comptabilisation avec travail de nuit effectué sur une semaine prévu dans le contrat_<br>
_2633_{:.id-label} _Nombre maximum de jours de comptabilisation avec travail de nuit effectué sur un mois prévu dans le contrat_<br>
_2634_{:.id-label} _Nombre maximum de jours de comptabilisation consécutifs avec travail de nuit prévu dans le contrat_<br>
_2635_{:.id-label} _Nombre minimum de jours libres après un travail de nuit prévu dans le contrat_<br>
_2636_{:.id-label} _Temps de repos après un travail de nuit_<br>
_2637_{:.id-label} _Nombre maximum de jours travaillés avant un travail de nuit_<br>

## Scénario 1 : les employés sont planifiés de nuit sur une base hebdomadaire

Dans ce scénario vous intégrez vos modèles horaires de nuit dans vos modèles de planification existants. Vous créez votre propre modèle hebdomadaire pour la semaine de travail de nuit et vous n'y ajoutez que les modèles horaires que vous considérez comme des horaires de nuit.

{{ 1 | image: "oragnisation de planification des modèles de planification standard", '75%' }}

Si vous n’utilisez pas encore les modèles de planification, ça se passe {% link_new ici | best-practices/fair-shift-distribution.md | #rotations-avec-optimisation--mod%C3%A8les-de-planification %}.

**Avantage** :

- Tous les employés reçoivent une répartition équitable des horaires de nuit.

**Inconvénient** :

- Les horaires de nuit ne sont planifiés que sur une semaine complète.

## Scénario 2 : Les horaires de nuit sont l'exception

Comme dans le scénario 1, vous avez besoin de créer un modèle hebdomadaire pour vos horaires de nuit et vous le définissez comme _modèle hebdomadaire pour les jours dérogatoire_ dans votre modèle de planification.

{{ 2 | image: "organisation de la planifcation des modèles de planification avec exception", '75%' }}

Vous déterminez le nombre d’horaires de nuit possible via le _nombre max. de jours dérogatoire par sem._ dans le modèle hebdomadaire respectif. Vous pouvez ainsi ajouter les modèles horaires de nuit uniquement sur une seul semaine (un seul modèle hebdomadaire) ou sur plusieurs.

Dans cette approche, les horaires de nuit ne sont utilisés que si la couverture des activité le nécessite. Cela permet à certains employés d'avoir des semaines sans horaire de nuit.

**Avantage** :

- Si votre centre de contacts est en sous-effectif, il est presque certain que les modèles horaires des jours dérogatoire sont toujours utilisés.

**Inconvénients** :

- Les horaires de nuit étant planifiés au hasard, il se peut que le planning produit ne soit pas équitable car vous ne pouvez pas établir une rotation pour l’attribution des horaires de nuit.
- Si il y a un fort sous-effectif pendant la journée, les équipes de nuit peuvent être en sous-effectif.

## Scénario 3 : Les horaires de nuit sont équitablement répartis entre les employés

Si vous souhaitez vous assurer que les horaires de nuit sont répartis de manière équitable entre vos employés, vous pouvez les planifier à l’aide d’une rotation d’horaires. Il fait tout d'abord calculer le nombre d’horaires de nuit nécessaires et la meilleure façon de les répartir entre tous les employés. Notez qu'il se peut que vous deviez modifier voire même recréer votre rotation d’horaires à cause du turnover de vos employés (arrivées/départs).

{{ 3 | image: "oragnisation des horaires de nuit par rotations d'horaires", '75%' }}

Si vous n'avez pas encore créé de rotation d’horaires, vous trouverez des informations à ce sujet {% link_new ici | features/administration/shift-sequences.md %}.

Vous pouvez ensuite utiliser l’optimisation complète (AutoScheduler) pour répartir et attribuer les modèles horaires des autre journées.

**Avantage** :

- Les horaires de nuit sont toujours répartis équitablement entre tous les employés.

**Inconvénients** :

- Effort manuel important pour maintenir à jour les rotations d’horaires.
- Pas de flexibilité.
- Planification manuelle en cas d'absence ou de vacances.

## Scénario 4 : Les employés veulent des horaires de nuit (planification des horaires de nuit par génération de missions)

Si vous souhaitez donner à vos employés la possibilité de choisir leurs propres horaires de nuit, vous pouvez utiliser la génération de missions. Vous devez décider à l'avance si les employés souhaitent travailler uniquement en horaires de de nuit ou si vous souhaitez utiliser la génération de missions pour tous vos employés. Nous vous recommandons de combiner la planification des équipes de nuit avec un planning entièrement optimisé par le moteur d’optimisation.

Vous devez limiter le nombre maximum d’horaires de nuit dans le menu _Planification > SchedulePro > Besoin en missions_{:.breadcrumbs}. Si vos employés ne souhaitent travailler que la nuit et que vous utilisez également une planification entièrement optimisée, vous devez limiter le besoin en missions des autres modèles horaires à 0.

{{ 4 | image: "interface besoin en mission", '75%' }}

**Avantage** :

- L'équité car les employés choisissent eux-mêmes les horaires de nuit.

**Inconvénients** :

- Les horaires de nuit doivent être planifiés manuellement si un nombre insuffisant d’employés se sont inscrits.
- Les inscriptions sur les horaires de nuit doivent être faites avant le reste de la planification afin qu'elles soient incluses dans celle-ci.
