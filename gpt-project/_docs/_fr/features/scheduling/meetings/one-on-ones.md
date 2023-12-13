---
title: Configurer une réunion 1:1
product_label:
  - advanced
  - enterprise
redirect_from:
  - /fr/meetings-reunions-one-to-one/
redirect_reason: Updated filename on 21 April 2022
---

Pour planifier une réunion 1:1, cliquez sur _Paramétrage_{:.doc-button} dans la section correspondante en haut de la page d'accueil. La page **Configurer une réunion 1:1** s'ouvre.

## Paramètres de configuration

Dans la section **Configuration**, renseignez les informations suivantes :

| Paramètres           | Description                                                                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Unité opérationnelle | Sélectionnez une Unité opérationnelle dans la liste ou tapez son nom pour filtrer les résultats.                                                                                                                               |
| Activité             | Sélectionnez une Activité dans la liste ou tapez son nom pour filtrer les résultats. Les Activités proposées sont uniquement celles de type `Meeting`.                                                                         |
| Période              | Sélectionnez la période sur laquelle la réunion doit être planifiée. Par défaut, la période est la semaine prochaine (Lundi à Dimanche. Si la date du jour est un lundi, alors la semaine par défaut est la semaine en cours). |
| Durée                | La durée des réunions est exprimée en minutes. La valeur par défaut est de 30 minutes. Les valeurs affichées dépendent de l'intervalle de planification de l'unité opérationnelle sélectionnée.                                |

Dans la section **Paramètres optionnels**, vous pouvez renseigner d'autres contraintes :

- L'écart minimum à respecter entre les réunions.
- Le nombre de réunions par jour.
- Une couverture minimale à respecter.

{{ 1 | image: "Paramètres de configuration", '60%' }}

## Définir les participants

Toutes les réunions 1:1 se déroulent entre un organisateur (par exemple un superviseur) et une liste de participants.

Pour le choix de l'**Organisateur**, vous avez deux options :

- **Renseigner manuellement**<br>
  Sélectionnez cette option si l'organisateur n'est pas planifié dans injixo. Définissez une liste de créneaux valides pour chaque jour de la semaine ou pour un ensemble de jours (Lundi à Vendredi/Samedi/Dimanche). Pour ajouter d'autres jours, cliquez sur _Ajouter le jour et la période_{:.doc-button}. Pour supprimer les jours, utiliser _Supprimer le jour_{:.doc-button}. Au moins une entrée doit être définie.

Pour ajouter d'autres créneaux horaires par jour, cliquez sur _+ Période_{:.doc-button}.

{{ 2 | image: 'Organisateur - Renseigner manuellement ', '60%' }}

- **Choisir un Employé**<br>
  Sélectionnez cette option si l'organisateur est planifié dans injixo. Vous pouvez sélectionner des Employés d'une Unité opérationnelle différente. Dans ce cas, les deux Unités opérationnelles doivent être configurées sur le même intervalle. Avez cette option, les réunions planifiées seront également écrites dans le planning de l'organisateur.

{{ 3 | image: "Organisateur - Choisir un Employé", '60%' }}

Dans la section **Participants**, vous définissez la liste des participants qui doivent assister aux réunions 1:1. Par défaut, la liste complète des Employés de l'Unité opérationnelle est sélectionnée. Vous pouvez filtrer les participants en sélectionnant un Groupe ou un filtre avancé à partir de la liste déroulante. Utilisez la case à cocher à gauche du nom d'un Employé pour le sélectionner ou le désélectionner.

{{ 4 | image: 'Participants', '60%' }}

## Générer les propositions

Une fois les réunions configurées, cliquez sur _Générer les propositions_{:.doc-button}. La génération des sessions démarre et vous êtes redirigés vers la page d'accueil.

Continuer votre lecture avec l'article {% link_new Comment planifier les propositions | features/scheduling/meetings/scheduling-suggestions.md %}.
