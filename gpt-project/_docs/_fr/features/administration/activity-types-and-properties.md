---
title: Type et propriétés des activités
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Découvrez les différents types d’activité et le but des options de configuration de chaque activité.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/how-to-schedule-multiskill-agents.md
redirect_from:
  - /fr/activity-properties/
redirect_reason: Updated filename on 11 October 2023
---

Lorsque vous {% link_new créez et modifiez des activités | features/administration/activities.md %}, les différentes options de configuration influencent l’utilisation et l’affichage des activités dans vos plannings et vos rapports.

## Types d’activité

Le type d’activité impacte la planification et détermine&nbsp;:
- la gestion de l’activité dans l’optimisation du planning,
- où l’activité peut être utilisée,
- l’affichage de l’activité dans Schedules et le Centre de planification,
- l’inclusion de l’activité dans les rapports. <!-- illness, absences, vacation -->

Le tableau suivant détaille chaque type d’activité&nbsp;:

| Type     | Description                                                                                                                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Présence | Toutes les activités sur lesquelles travaillent les employés.<br>injixo planifie les activités de type Présence selon le besoin en personnel.                                    |
| Pause    | Pauses rémunérées ou non rémunérées dans une journée.<br>Seules les activités de type Pause peuvent être configurées dans les modèles horaires comme activités de pause. Vous pouvez utiliser la fonctionnalité {% link_new d’optimisation des pauses | features/scheduling/schedules/break-optimization.md %} pour répartir les pauses dans les plannings. Ainsi, vous pouvez obtenir une couverture optimale pour les activités avec besoin en personnel. |
| Maladie  | Absences rémunérées ou non rémunérées, par exemple les congés maladie ou les rendez-vous médicaux.<br>Seules les activités de type Maladie apparaissent dans les rapports statistiques sur les maladies.                             |
| Congé | Congés rémunérés ou non rémunérés, fermeture temporaire/saisonnière, etc.<br> Seules les activités de type Congé apparaissent dans les rapports statistiques sur les congés.                                                 |
| Absence  | Autres absences qui influencent le planning&nbsp;: formations hors site, compensation des heures supplémentaires, etc.<br>Les rapports statistiques sur les absences affichent uniquement les activités de type Absence.              |
| Meeting  | Nécessaire pour {% link_new planifier des réunions                                                                                                                      | features/scheduling/meetings/meetings-overview.md %} |

## Propriétés des activités

Les propriétés des activités influencent votre planning et votre utilisation de l’activité.
Vous pouvez définir les propriétés des activités avec les cases suivantes.

| Propriété                                    | Résultat                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Rémunérée                                        | Active le calcul des heures de travail pour les activités planifiées. Si les pauses ou les absences sont rémunérées, elles sont calculées en tant qu’heures de travail. Si elles ne sont pas rémunérées, elles ne sont pas incluses dans le calcul du temps de travail net.                                                                                                                                       |
| Respecter le temps de repos                     | Empêche les violations du temps de repos configuré dans le contrat. injixo vérifie le temps de repos uniquement si la règle de planification _2601_{:.id-label} est activée.   |
| Planifiable automatiquement                                   | injixo peut planifier l’activité si vous utilisez la fonctionnalité Optimiser le planning ou l’optimiser pendant l’optimisation du planning. Cette propriété est généralement utilisée pour les activités qui présentent un besoin en personnel. Elle n’est généralement pas utilisée pour les activités de type Absence, Congé et Maladie.                                                                               |
| Autoriser les demandes dans Me                           | Permet aux employés de créer des demandes d’absences (absences, congés et maladie) dans injixo Me (si le statut Publié est activé sur une {% link_new Période de congés      | features/scheduling/time-off/time-off-periods.md %}). Dans la Génération de missions, les journées contenant des activités de type Présence et Pause peuvent être demandées automatiquement. |
| Bourse d’échanges              | Permet aux employés {% link_new d’échanger l’activité entre eux | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %} dans injixo Me. Pour ce faire, l’option **Autoriser les demandes dans Me** doit être activée pour toutes les activités incluses dans les modèles horaires (y compris les pauses).    |
| Surcouverture du besoin pour les valeurs nulles | injixo peut planifier l’activité, même sur des périodes sans besoin en personnel. Par défaut, les intervalles sans besoin ne seront pas couverts.                                                                                                                                                                                                                |
| Remplaçable                               | injixo peut remplacer l’activité avec d’autres activités remplaçables automatiquement qui présentent un besoin en personnel. Nécessaire pour {% link_new planifier des réunions  | features/scheduling/meetings/meetings-overview.md %} sur cette activité.                                                                                                               |
| Activité à journée entière                | Vous pouvez planifier l’activité sur toute une journée (dans Schedules ou dans l’onglet Activités à journée entière dans la vue journalière du Centre de planification). Si l’activité est également configurée comme Rémunérée, l’employé reçoit la cible journalière correspondant au contrat.<br>Requis pour permettre aux employés de demander l’activité comme activité à journée entière dans injixo Me.   |
| Statut journalier                                | Disponible uniquement pour les activités à journée entière. Le Statut journalier vous permet de planifier l’activité manuellement dans le Centre de planification en tant que statut journalier dans l’onglet Activités à journée entière. Ceci permet de conserver le planning remplacé à titre d’information. Par conséquent, injixo exclut du calcul de la couverture les employés planifiés pour une activité avec cette propriété, mais le planning original reste visible. |
| Traitement spécial pour la planification optimisée | Disponible uniquement pour les activités de type Présence. Les activités ayant cette propriété peuvent uniquement être planifiées selon leur configuration. Les activités ne peuvent être remplacées et leur durée n’est pas flexible. <br>Lisez la [section suivante](#traitement-spécial-pour-la-planification-optimisée) pour en savoir plus.

## Traitement spécial pour la planification optimisée

Cette propriété permet à la fonctionnalité Optimiser le planning de planifier l’activité uniquement selon sa configuration. Cette propriété est généralement utilisée pour la planification des heures supplémentaires ou des activités de back-office.<br>
Il existe deux utilisations possibles de cette propriété&nbsp;:

Option 1&nbsp;: l’activité est assignée à un modèle horaire. Dans ce cas, l’activité peut uniquement être planifiée pour la durée configurée et sur la période définie par le modèle horaire. L’activité ne peut pas être utilisée pour remplacer d’autres activités remplaçables. Le moteur d’optimisation traite l’activité selon sa {% link_new configuration dans le modèle horaire | features/administration/daymodels/daymodel-creation.md %}&nbsp;:
- Configurée comme élément fixe&nbsp;: le moteur d’optimisation planifiera l’activité seulement à l’heure exacte pour laquelle elle a été configurée.
- Configurée comme élément de corridor&nbsp;: le moteur d’optimisation peut déplacer l’activité dans le corridor défini pour optimiser la couverture d’autres activités.

Exemple d’utilisation&nbsp;:

- Ajoutez à votre modèle horaire une activité de back-office sans besoin en personnel et avec une durée d’une heure. Le moteur d’optimisation planifiera l’activité pour une heure exactement. Si l’activité est configurée comme élément de corridor dans le modèle horaire, l’activité sera déplacée dans le corridor, sur le créneau qui aura l’impact le plus faible sur la couverture des autres activités.

Option 2&nbsp;: l’activité est n’est pas assignée à un modèle horaire. Dans ce cas, le moteur d’optimisation ne peut pas planifier l’activité automatiquement et ne peut pas l’utiliser pour remplacer d’autres activités remplaçables. L’activité peut uniquement être planifiée manuellement.

Exemple d’utilisation&nbsp;:

- Créez une activité pour les heures supplémentaires, qui ne sera assignée à aucun modèle horaire. La fonctionnalité Optimiser le planning ne planifiera pas l’activité et ne l’utilisera pas pour remplacer d’autres activités. Ajoutez manuellement l’activité au planning si nécessaire. Dans ce scénario, vous gardez le contrôle sur la planification de l’activité, sa durée et son assignation aux employés.

> Remarque
>
> Cette propriété est uniquement disponible après avoir créé l’activité.

## Sous-activités

Vous pouvez assigner des activités à d’autres activités. L’activité à laquelle les activités sont assignées devient alors une multi-activité. Les activités assignées sont les sous-activités de la multi-activité. Les multi-activités vous permettent de planifier les employés possédant plusieurs compétences lorsque l’une de leurs compétences est requise. Dans la liste d’activités, les multi-activités sont marquées d’une icône <em class="multiactivity-icon"></em>. 

La fonctionnalité Optimiser le planning peut planifier des multi-activités si les conditions suivantes sont remplies&nbsp;:

- Les multi-activités et toutes les sous-activités sont de type Présence,
- Les multi-activités et toutes les sous-activités sont configurées comme rémunérées et planifiables automatiquement,
- Toutes les sous-activités (et les multi-activités dans l’étape suivante) sont assignées à votre unité opérationnelle.
- Pour décider des conseillers pouvant être planifiés, assignez une compétence différente à chaque sous-activité.
- (Facultatif) Assignez une compétence à la multi-activité. Dans ce cas, les conseillers doivent posséder cette compétence supplémentaire pour travailler sur la multi-activité. Par défaut, la multi-activité ne nécessite aucune compétence.

> Remarque
>
> Si vous n’utilisez pas la fonctionnalité Optimiser le planning mais uniquement Optimiser les activités, injixo peut remplacer les activités remplaçables avec des multi-activités, à condition qu’un conseiller puisse travailler au moins sur l’une des sous-activités de la multi-activité.
