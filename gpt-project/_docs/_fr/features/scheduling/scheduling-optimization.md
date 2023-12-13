---
title: Optimisation
promote-service: schedule-optimization-workshop
redirect_from:
  - /fr/optimisation/
redirect_reason: Updated filename on 21 April 2022
---

Le menu *WFM > Planification > SchedulePro > Optimisation*{:.breadcrumbs} vous permet d'optimiser les plannings de vos employés. Trois types d'optimisation sont possibles :

- Planning complètement optimisé : le système crée les plannings en utilisant tous les modèles horaires à sa disposition pour assurer la meilleure couverture du besoin en personnel de chaque activité.
- Optimisation des tâches : le système optimise uniquement les activités des employés. Les heures de début et de fin des journées de travail ne sont donc pas modifiées. Les activités déjà inscrites dans le planning sont modifiées si nécessaire et si leur paramétrage le permet. Toutes les activités sont optimisées, y compris les activités de type Pause.
- Optimisation des pauses : le système positionne les pauses et toutes autres activités à corridor de telle sorte que la couverture du besoin en personnel soit optimisée.

## Planning complètement optimisé

L'option *Planning complètement optimisé*{:.doc-button} (également appelée AutoScheduler) vous permet de créer automatiquement les plannings de vos employés pour assurer la meilleure couverture du besoin en personnel de chaque activité. Pour se faire, le système utilise les Modèles horaires et les Activités préalablement paramétrés.

Cette option utilise les objets d'administration suivants :

- Employés : dates de début et de fin de période d'emploi, Contrat, Compétence(s), Unité(s) opérationnelle(s) et Disponibilités.
- Contrats : indication des temps de travail ou répartition des heures sur les jours de la semaine, paramètres de l'AutoScheduler et Règles de planification.
- Activités :
    - Planifiable automatiquement : seules les activités dont la case `Planifiable automatiquement` est cochée sont optimisées.
    - Remplaçable : les activités dont la case `Remplaçable` est cochée peuvent être remplacées lors de l'optimisation.
    - Ordre d'importance : l'optimisation tient compte de l'Ordre d'importance des activités entre elles.
- Modèles horaires : seuls les Modèles horaires attribués à l'Unité Opérationnelle sont utilisés lors de l'optimisation.
- Modèles de planification : seuls les Modèles de planification attribués à un employé sont utilisés lors de l'optimisation.

En cliquant sur *Planning complètement optimisé*{:.doc-button}, une fenêtre de dialogue apparaît :

- Horaires : renseigner la période d'optimisation (max 10 semaines)
- Unité opérationnelle : sélectionner l'Unité opérationnelle à optimiser
- Groupes : si vous sélectionner un Groupe, seuls les plannings des Employés appartenant à ce Groupe seront créés. Sélectionner `Tous` pour optimiser l'ensemble des Employés de l'Unités opérationnelle.
- Optimisation renouvelée : cocher cette case si vous souhaitez renouveler l'optimisation en cas de modification du besoin en personnel par exemple.

Après avoir sélectionné les paramètres cliquer sur *OK*{:.doc-button}.

Vous pouvez suivre l'état d'avancement de l'optimisation et visualiser le détail des optimisations précédentes. Une fois l'optimisation réalisée le statut `Terminé` s'affiche.

> Remarque
>
> L'optimisation est un processus complexe. C'est grâce à un nombre très élevé d'itérations que le système peut trouver la meilleure combinaison possible respectant les contraintes de planification et le besoin en personnel des différentes Activités. Le temps de calcul dépend de la quantité de données à traiter, c'est à dire le nombre d'Activités et de Compétences, le nombre d'Employés, la période, etc.

Les plannings sont verrouillés lors de l'Optimisation sur la période concernée, vous ne pouvez donc pas les modifier lors de ce processus.

L'optimisation passe en statut `Terminé` lorsque pendant 3 minutes aucune nouvelle combinaison ne peut améliorer la couverture ou après 60 minutes de traitement. Les plannings sont alors automatiquement sauvegardés.

## Optimisation des tâches

L'Optimisation des tâches est utilisée lorsque des Modèles horaires et/ou des Activités sont déjà présents dans le planning des Employés, soit parce qu'une optimisation a déjà été faite, soit parce que des Rotations d'horaires ont été insérées.

Lors de l'Optimisation des tâches, des Activités peuvent être remplacées par d'autres pour couvrir au mieux le besoin en personnel, mais les heures de début et de fin des journées de travail des Employés restent inchangées.

L'Optimisation des tâches inclut également l'Optimisation des pauses. Les pauses variables (paramétrées dans un corridor) sont déplacées au moment le plus pertinent, tout en respectant les contraintes spécifiées dans le Modèle horaire.

**Exemple**

Le planning d'un Employé contient déjà l'Activité `E-mail` de 8h à 12h, une pause déjeuner de 12h à 13h et l'Activité `Présent` de 13h à 17h. L'Activité `Présent` est remplaçable, mais pas l'Activité `E-mail`.
Entre 13h et 17h il y a un besoin non couvert sur l'Activité `Téléphone`.
En lançant une Optimisation des tâches, le système vérifiera que l'Employé possède bien la Compétence sur l'Activité `Téléphone` et, si cela est le cas, remplacera l'Activité `Présent` par l'Activité `Téléphone`.

Cette option utilise les objets d'administration suivants :

- Employés : seuls les plannings des Employés avec les bonnes Compétences seront modifiés.
- Activités :
  - Planifiable automatiquement : seules les activités dont la case `Planifiable automatiquement` est cochée sont optimisées.
  - Remplaçable : les activités dont la case `Remplaçable` est cochée peuvent être remplacées lors de l'optimisation.
  - Ordre d'importance : l'optimisation tient compte de l'ordre d'importance des activités entre elles.
  - Surcouverture du besoin pour les valeurs nulles : si cette case est cochée, le système peut planifier des Activités sur lesquelles il n'y a aucun besoin en personnel. Nous ne conseillons pas d'activer cette option.
  - Priorité: si la règle de planification *2660*{:.id-label} *Respecter les priorités des activités* est activée, seules les Activités avec une Priorité plus élevée pourront remplacer des Activités déjà planifiées.

> Remarque
>
> Si vous planifiez vos Employés à l'aide de la Génération de missions, nous vous conseillons de ne créer que des Modèles horaires incluant l'Activité `Présent` et de vous assurer que celle-ci est bien `Remplaçable`. Ainsi vous évitez que des Employés s'inscrivent sur certaines missions incluant déjà des Activités, et que celles-ci soient modifiées après l'optimisation.

En cliquant sur *Optimisation des tâches*{:.doc-button}, une fenêtre de dialogue apparaît :

- Horaires : renseigner la période d'optimisation (max 10 semaines)
- Unité opérationnelle : sélectionner l'Unité opérationnelle à optimiser
- Groupes : si vous sélectionner un Groupe, seuls les plannings des Employés appartenant à ce Groupe seront créés. Sélectionner `Tous` pour optimiser l'ensemble des Employés de l'Unités opérationnelle.

Après avoir sélectionné les paramètres cliquer sur *OK*{:.doc-button}.

Vous pouvez suivre l'état d'avancement de l'optimisation et visualiser le détail des optimisations précédentes. Une fois l'optimisation réalisée le statut `Terminé` s'affiche.

Les plannings sont verrouillés lors de l'Optimisation sur la période concernée, vous ne pouvez donc pas les modifier lors de ce processus.

L'optimisation passe en statut `Terminé` lorsque pendant 3 minutes aucune nouvelle combinaison ne peut améliorer la couverture ou après 60 minutes de traitement. Les plannings sont alors automatiquement sauvegardés.

## Optimisation des pauses

Vous pouvez utiliser cette option pour optimiser les pauses variables (à corridor) paramétrées dans les Modèles horaires et ce même lorsque des Modèles horaires et/ou des Activités sont déjà présents dans le planning des Employés, soit parce qu'une optimisation a déjà été faite ou parce que des Rotations d'horaires ont été insérées.

Le but est ici d'optimiser les pauses des Employés tout en garantissant que la couverture des Activités soit la meilleure possible.

Les heures de début et de fin de la pause peuvent donc être modifiées, cependant les heures de début et de fin de la journée de travail de l'Employé ainsi que les Activités productives ne le sont pas.

En cliquant sur *Optimisation des pauses*{:.doc-button}, une fenêtre de dialogue apparaît :

- Horaires : renseigner la période d'optimisation (max. 10 semaines).
- Unité opérationnelle : sélectionner l'Unité opérationnelle à optimiser.
- Groupes : si vous sélectionner un Groupe, seuls les plannings des Employés appartenant à ce Groupe seront créés. Sélectionner Tous pour optimiser l'ensemble des Employés de l'Unités opérationnelle.

Après avoir sélectionné les paramètres cliquer sur *OK*{:.doc-button}.

Vous pouvez suivre l'état d'avancement de l'optimisation et visualiser le détail des optimisations précédentes. Une fois l'optimisation réalisée le statut `Terminé` s'affiche.

> Remarque
>
> Si un autre processus d'optimisation tourne en arrière plan, il se peut que la fenêtre de dialogue de l'Optimisation des pauses ne s'ouvre pas immédiatement.

## Scheduling Report

Un rapport d'exécution de l'optimisation peut être consulté en cliquant sur l'icône _!["icône notification"](/assets/img/{{ page.lang }}/features/scheduling-optimization/image-1.png)_{:.doc-button-icon} de la colonne *Résultat*{:.menu-item}. Ce rapport sera ouvert dans une nouvelle fenêtre ou dans un lecteur de fichiers PDF.
