---
title: Événements et congés
toc: false
redirect_from:
  - /fr/evenements-conges/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

Forecast prend en compte les congés des différentes régions ainsi que les événements (journées atypiques comme par exemple une panne informatique ou une action commerciale).

## Congés

Des calendriers de jours fériés sont disponibles et peuvent être sélectionnés lors de la création du Workload.

## Types d'événements

Vous pouvez créer vos propres types d'événements dans Forecast et ajouter jusqu'à 7 types d'événement pour chaque catégorie disponible. Notez que ces types d'événements personnalisés ne sont pas rattachés spécifiquement à un Workload.

Lors de la sélection d'un Workload, les types d'événements et les jours fériés peuvent être ajoutés en cliquant sur le bouton _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} à droite de l’écran puis en sélectionnant `Personnaliser les types d'événements`.

Une fois la catégorie choisie, les types d'événements associés s'affichent. Vous pouvez alors créer, modifier ou supprimer un type d'événement. Lors de la suppression d'un type d'événement, tous les événements associés (passés et futurs) seront supprimés définitivement.

{{ 1 | image: "personnaliser les types d'événements", '50%' }}

## Événements

Les types d'événements peuvent être ajoutés sur une journée spécifique en cliquant sur le bouton _![Context Menu in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} et en sélectionnant `Attribuer un (des) événement(s)`.

Les événements passés et futurs sont à renseigner. Les événements passés seront analysés par les algorithmes de Forecast et permettront au système de calculer une prévision plus juste.

{{ 2 | image: "ajouter un type d'événements", '50%' }}
