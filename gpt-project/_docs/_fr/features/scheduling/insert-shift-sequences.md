---
title: Insérer des Rotations d'horaires
promote-service: new-planner-training
redirect_from:
  - /fr/inserer-rotations-horaires/
redirect_reason: Updated filename on 21 April 2022
---

Dans le menu _WFM > Planification > SchedulePro > Insérer des rotations d'horaires_{:.breadcrumbs}, vous utilisez les {% link_new Rotations d'horaires | features/administration/shift-sequences.md %} préalablement créées et affectées à vos employés et les insérez dans les plannings pour une période donnée.

Une Rotation d'horaires est un cycle répétitif de journées. Les Rotations d'horaires peuvent contenir un Modèle horaire ou une Activité par journée. Les Rotations d'horaires sont créées dans le menu _WFM > Administration > Planification > Rotations d'horaires_{:.breadcrumbs} et assignées aux Employés dans la fiche Employé.

## Définition des paramètres

Dans un premier temps, vous devez choisir les paramètres suivants.

| Paramètres           | Description                                                                                                                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Date de début        | Sélectionnez la date de démarrage pour l'insertion des Rotations d'horaires. La date du jour est sélectionnée par défaut.                                                                              |
| Date de fin          | Sélectionnez la date de fin pour l'insertion des Rotations d'horaires. Veuillez noter que l'insertion des Rotations d'horaires est limitée à deux années. La date du jour est sélectionnée par défaut. |
| Unité opérationnelle | Sélectionnez l'Unité opérationnelle pour laquelle vous voulez insérer les Rotations d'horaires. La dernière Unité opérationnelle utilisée est sélectionnée par défaut.                                 |
| Groupe               | Sélectionnez le Groupe d'Employés concernés.`[Tous]` est sélectionné par défaut.                                                                                                                       |
| Catégorie source     | Sélectionnez la catégorie de planning dans laquelle la Rotation d'horaires doit être insérée. La catégorie `Planning` est sélectionnée par défaut.                                                     |

Cliquez sur _Établir la liste des employés_{:.doc-button} pour afficher la liste des Employés. La liste ne contient que les Employés à qui une Rotation d'horaires est affectée sur la période sélectionnée et qui appartiennent à l'Unité opérationnelle et au Groupe sélectionnés.

Vous pouvez maintenant choisir sur quels Employés vous allez insérer les Rotations d'horaires et sélectionner les options d'insertion.

## Sélectionner les Employés

Pour sélectionnez tous les Employés, vous devez cocher la case située en haut de la colonne gauche du tableau. Vous pouvez également sélectionner les Employés individuellement en cochant les cases à gauche de leur matricule. Veuillez noter que lorsque vous triez la liste (en cliquant sur le nom d'une colonne), les sélections déjà réalisées seront effacées.

> Remarque
>
> Lorsque vous configurez les données d'un Employé, il est possible de lui affecter plus d'une Rotation d'horaires. Ainsi, lorsque vous établissez la liste des Employés, un Employé peut apparaitre plusieurs fois. Consultez la section _Insérer plusieurs rotations d'horaires pour un employé_ ci-dessous pour avoir plus d'information.

## Sélectionner les options

Dans la partie _Options_{:.menu-item}, vous pouvez choisir quels éléments du planning doivent être supprimés lors de l'insertion des Rotations d'horaires. Aucune option n'est sélectionnée par défaut.

- Supprimer des Activités à journées entières : si cette option est sélectionnée, les Activités à journées entières de l'Employé sur la période sélectionnée seront supprimées du planning et remplacées par la Rotation d'horaires choisie. Pour éviter que les Activités à journée entière (comme les congés) ne soient effacés par une Rotation d'horaires, activez la Règle de planification _2645_{:.id-label} _Remplacement des journées entières par des missions ou des activités_. Enfin, notez que l'insertion des Rotations d'horaires remplace toujours les Activités à journées entières par d'autres Activités à journées entières, peu importe la configuration de l'option et de la Règle de planification.

- Supprimer le cadre de disponibilité : si cette option est sélectionnée, les cadres de disponibilités des Employés seront supprimés et remplacés par ceux paramétrés dans la Rotation d'horaires sur la période sélectionnée.

- Supprimer toutes les Activités et Missions : si cette option est sélectionnée, toutes les Activités et tous les horaires des Employés seront supprimés et remplacés par la Rotation d'horaires sur la période sélectionnée. Les cadres de disponibilités ne seront pas supprimés. Si cette option n'est pas sélectionnée, les Activités et les Modèles horaires sont insérés dans le planning et les horaires et Activités existants seront conservés.

> Remarques
>
> - Les options ne sont appliquées que lors de l'insertion de la première Rotation d'horaires. Par exemple, si plusieurs Rotations d'horaires sont sélectionnées les unes après les autres pour un Employé, le contenu du planning n'est supprimé que lors de l'insertion de la première Rotation d'horaires.
> - Les Règles de planification suivantes sont importantes et leur statut doit être vérifié :
>   - _2648_{:.id-label} _Protection en écriture des activités déjà inscrites dans le Centre de Planification_
>   - _2613_{:.id-label} _Nombre maximum de missions au cours d'un jour de comptabilisation prévu dans le contrat_
>   - _2602_{:.id-label} _Durée maximum d'une activité prévue dans le contrat_
>   - _2611_{:.id-label} _Disponibilité d'un employé_

## Insérer les Rotations d'horaires

Une fois que vous avez sélectionné les paramètres, les Employés et les options, vous démarrez l'insertion des Rotations d'horaires en cliquant sur _Insérer des rotations_{:.doc-button}.

L'insertion des Rotations d'horaires démarre immédiatement après.

Une vérification est réalisée lors du processus d'insertion. Si une affectation enfreint une Règle de planification définie comme majeure, elle n'est pas exécutée. Lorsque le processus d'insertion est terminé, une note décrivant les affectations impossibles apparait. Si toutes les insertions ont été faites avec succès, vous recevrez un message de confirmation

> Remarque
>
> Le premier jour de la Rotation d'horaires est toujours inséré en fonction de la date de référence précisée dans la fiche de l'Employé.

**Exemple 1**
La date de démarrage et la date de référence sont identiques. La période d'insertion est du 9 au 29 juillet. Le premier jour de la Rotation d'horaires (par exemple un début de semaine, le lundi) est inséré.

**Exemple 2**
La période d'insertion est identique, mais la date de démarrage et la date de référence sont différentes. La Rotation d'horaires démarre le 9 juillet. La date de référence est le 2 juillet. Le 8ème jour de la rotations d'horaires (par exemple le second lundi) est inséré le 9 juillet.

## Insérer plusieurs Rotations d'horaires pour un Employé

Lorsque vous configurez les données relatives aux Employés dans la section _Administration_{:.menu-item}, il est possible d'assigner à un Employé plusieurs Rotations d'horaires en donnant à chaque Rotations d'horaires un `Ordre` dont la valeur peut aller de 1 à 10. Ainsi, lorsque vous établissez la liste des Employés, un Employé peut apparaitre plusieurs fois. Vous devez choisir quelle Rotation doit être insérée dans le planning de l'Employé parmi les Rotations proposées. Si vous sélectionnez le même Employé plusieurs fois, les séquences seront insérées consécutivement en commençant par celle ayant la valeur d'`Ordre` la plus basse jusqu'à la valeur d'`Ordre` la plus élevée.

Pour savoir si le contenu d'une Rotation d'horaires est supprimé par l'insertion d'une autre Rotation d'horaires, il faut vous reporter aux options décrites précédemment. Les Activités qui ne sont pas à journée entière seront toujours supprimées.
