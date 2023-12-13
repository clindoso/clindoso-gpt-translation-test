---
title: JobProcessor
redirect_from:
  - /fr/jobprocessor/
redirect_reason: Updated filename on 21 April 2022
---

Le menu JobProcessor vous permet de visualiser les opérations exécutées par les utilisateurs injixo et est accessible via *WFM > Administration > Système > JobProcessor*{:.breadcrumbs}. Vous pouvez suivre l'avancement des opérations en cours ou consulter le rapport des opérations réalisées.

Les opérations suivantes peuvent être consultées dans le menu JobProcessor :

  - Planification
    - SchedulePro
      - Optimisation
      - Périodes de planification
        - Générer les Missions
        - Tirage au sort des Missions
        - Attribuer les Missions
        - Calcul des Comptes temps dû
        - Échanger des Activités
        - Copier une Catégorie
        - Supprimer une Catégorie
      - Insérer des Rotations d'horaires
  - Supervision
    - Reports
  - Administration
    - Planification
      - Employés
        - Modification massive

Vous pouvez annuler ces tâches en cours d'exécution (comme par exemple interrompre une optimisation en cours) ou consulter les rapports d'exécution de tâches précédemment lancées.

Les tâches ne peuvent être démarrées directement dans le menu JobProcessor mais seulement dans le menu correspondant (Insérer des Rotations d'horaires, Reports, Optimisation, etc.).

## Exécution d'une tâche

Lorsque vous réalisez une action nécessitant l'utilisation du JobProcessor, une fenêtre de dialogue s'ouvre et affiche la date et l'heure de l'exécution de la tâche, les options sélectionnées par l'utilisateur ainsi que l'état d'avancement du processus.

{{ 1 | image: "popup jobprocessor", '50%' }}

Les opérations sont lancées en tâche de fond, vous pouvez donc continuer à utiliser injixo. Fermer la boîte de dialogue n'annulera pas l'exécution du processus.

> Remarque
>
> Vous ne pouvez plus annuler une tâche qui a démarré via la boite de dialogue. Vous ne pouvez plus l'annuler que dans le menu JobProcessor.

## Vue d'ensemble des tâches

L'ensemble des opérations en cours d'exécution ou déjà exécutées par le JobProcessor peuvent être consultées dans le menu *WFM > Administration > Système > JobProcessor*{:.breadcrumbs}.

{{ 2 | image: "overview jobprocessor", '50%' }}

Pour chaque opération les informations suivantes sont disponibles :
- Le statut
- Le rapport de résultat
- Le type de tâche
- L'ID de la tâche
- L'utilisateur ayant lancé le processus
- La date et l'heure de début de la tâche
- Le temps d'attente
- Le temps de traitement
- La date et l'heure de fin de la tâche
- L'hôte
- L'adresse e-mail de l'utilisateur (s'il a sélectionné l'option *Mail de confirmation*)

Vous pouvez filtrer la liste des processus affichés selon leur statut (*Tous*, *Tâche traitées* ou *Tâche non traitées*) ou selon l'utilisateur.

## Fonctionnalités disponibles

Pour chaque processus sélectionné les actions suivantes peuvent être réalisées :

- *Replacer*{:.doc-button} la tâche dans la file d'attente : le processus sera relancé avec les mêmes paramètres.
- *Interrompre*{:.doc-button} la tâche : le processus en attente ou en cours d'exécution sera immédiatement interrompu.
- *Supprimer*{:.doc-button} la tâche : le processus sera supprimé de la vue d'ensemble.

La liste des tâches affichées n'est pas mise à jour automatiquement. Pour remettre à jour la page cliquez sur *Actualiser le récapitulatif*{:.doc-button}.
