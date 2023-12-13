---
title: Configurer des réunions de groupe
product_label:
  - advanced
  - enterprise
redirect_from:
  - /fr/meetings-reunions-de-groupe/
redirect_reason: Updated filename on 21 April 2022
---

Pour planifier une réunion de groupe, cliquez sur _Paramétrage_{:.doc-button} dans la section correspondante en haut de la page d’accueil. La page **Configurer une réunion de groupe** s’ouvre.

## Paramètres de configuration

Dans la section **Configuration**, renseignez les informations suivantes :

| Paramètres           | Description                                                                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Unité opérationnelle | Sélectionnez une Unité opérationnelle dans la liste ou tapez son nom pour filtrer les résultats.                                                                                                                               |
| Activité             | Sélectionnez une Activité dans la liste ou tapez son nom pour filtrer les résultats. Les Activités proposées sont uniquement celles de type `Meeting`.                                                                         |
| Période              | Sélectionnez la période sur laquelle la réunion doit être planifiée. Par défaut, la période est la semaine prochaine (Lundi à Dimanche. Si la date du jour est un lundi, alors la semaine par défaut est la semaine en cours). |
| Durée                | La durée des réunions est exprimée en minutes. La valeur par défaut est de 30 minutes. Les valeurs affichées dépendent de l'intervalle de planification de l'unité opérationnelle sélectionnée.                                |

{{ 1 | image: "Paramètres", '60%' }}

Des contraintes supplémentaires peuvent être ajoutées en cliquant sur _Définir une contrainte de disponibilité supplémentaire_. Vous pouvez ainsi ajouter une liste de créneaux valides pour chaque jour de la semaine ou pour un ensemble de jours (Lundi à Vendredi/Samedi/Dimanche).
Pour ajouter d’autres jours, cliquez sur **Ajoutez une période**.

## Définir les participants

La section _Organisateur_ vous permet de définir l'organisateur de la réunion. Plusieurs options sont disponibles :

- **Aucun organisateur** : si aucun organisateur n'est défini pour les réunions de groupe, celles-ci pourront se chevaucher.
- **Organisateur interne** : cette option permet de sélectionner l'utilisateur planifié dans injixo en tant qu'organisateur de la réunion de groupe. Le système prend ainsi en compte la disponibilité de celui-ci dans le calcul des propositions. Il est possible de définir un organisateur n'appartenant pas à l'unité opérationnelle sélectionnée, mais l'intervalle de planification des 2 unités opérationnelles concernées doit être identique.
- **Organisateur externe** : cette option permet de définir un organisateur externe. Les réunions de groupe ne pourront donc pas se chevaucher.

{{ 2 | image: "Réunion sans organisateur", '60%' }}

La section **Participants**, vous permet de définir la liste des participants qui doivent assister aux réunions de groupe.

Utilisez la case à cocher à gauche du nom d’un Employé pour le sélectionner ou le désélectionner. Vous pouvez filtrer les participants en sélectionnant un {% link_new Groupe | features/administration/selections.md %} ou un filtre avancé à partir de la liste déroulante.

Activez le paramètre _Diviser la réunion en plusieurs créneaux_ si vous souhaitez diviser la réunion de groupe en plusieurs créneaux. Utilisez alors le menu déroulant pour indiquer le nombre minimum de participants par créneau.

{{ 3 | image: "Participants", '60%' }}

## Générer les propositions

Une fois la réunion configurée, cliquez sur _Générer les propositions_{:.doc-button}. Le processus démarre et vous êtes redirigés vers la page d'accueil.

Continuer votre lecture avec l'article {% link_new Comment planifier les propositions | features/scheduling/meetings/scheduling-suggestions.md %}.
