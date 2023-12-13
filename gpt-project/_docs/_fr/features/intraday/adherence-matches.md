---
title: Configurer Matches
toc: true
product_label:
  - advanced
  - enterprise
description: Créer des règles pour définir les combinaisons d'activités planifiées et réalisées pour que vos conseillers soient adhérents au planning.
redirect_from:
  - /fr/configurer-matches/
redirect_reason: Updated filename to match EN in April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Matches permet de créer des règles pour contrôler l'adhérence de vos employés.

Pour comprendre Matches, veuillez lire l'article {% link_new Adhérence Temps Réel | features/intraday/real-time-adherence.md %} en premier.

## A quoi correspond Matches ?

_Matches_{:.menu-item} vous permet de :
* améliorer les règles d'adhérence entre les statuts agent et les activités planifiées.
* réduire les informations erronées à cause de règles mal définies.

Vous pouvez améliorer votre Score d'adhérence en quelques clics. Remarque : Les modifications dans Matches affectent uniquement le module Adhérence. Les rapports standards injixo ne sont pas affectés.

## How to Access Matches?

Vous pouvez accéder à **Matches** de plusieurs manières dans le module _Adherence_{:.menu-item}.

* Cliquez sur le bouton _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} et sélectionner **Matches**.

    {{ 4 | image: 'Accéder à Matches via le menu','40%' }}

* Cliquer sur l'**icône Matches** en passant le curseur sur le nom de l'activité dans la section _Détail par activité_. 

    {{ 3 | image: "Accéder à Matches via la vue d'ensemble des activités",'40%' }}

## Visualiser la configuration

La liste des activités est affichée sur la gauche de l'écran. Sélectionner une activité pour visualiser le détail de la configuration.

* _Activité actuelle_ présente les mappings des status agents existants, groupés par système externe.
* _Activité planifiée_ présente les activités planifiables et les types d'activités qui permettent de valider l'adhérence de l'employé.

Par défaut, chaque activité est liée à elle-même et à son type d’activité.

{{ 5 | image: 'Matches par défaut', '100%' }}

## Configurer Matches

Vous pouvez modifier le mapping d'une _activité du système externe_ avec des activités planifiables et des types d'activités.

1. Cliquer sur _Editer_{:.doc-button} pour ouvrir l'écran d'édition.
    {{ 2 | image: 'Gérer la modélisation avec Matches',' 40%' }}

2. Sélectionner **les activités et les types d'activités** que vous souhaitez inclure. Les données existantes sont listées en premier.
3. Cliquer sur _Appliquer_{:.doc-button} pour valider vos modifications.

{{ 1 | image: "Vue d'ensemble Matches","100%" }}

> Vous ne pouvez pas supprimer l'activité associée par défaut.

## Configurer Matches pour l'activité *Hors ligne*

Si un agent dispose d'un planning mais qu'il n'est pas connecté à un système externe, il apparaît comme *En dépassement* avec le statut *Non présent*.

Selon votre configuration, il est possible que les agents se déconnectent lorsqu'ils sont en pause, en réunion ou en formation. Dans ce cas, la liste des activités contient une entrée dédiée pour le statut *Hors ligne*. En créant une correspondance entre le statut *Hors ligne* avec des activités, vous éviterez d'avoir des agents *En dépassement* et cela améliorera votre score d'adhérence.
