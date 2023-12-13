---
title: Méthodes de planification
promote-service: new-planner-training
description: Découvrez les différentes méthodes de planification d’injixo.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/combined-scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/set-a-validity-period.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
---

En lisant cet article, vous apprendrez&nbsp;:
- quelles méthodes de planification peuvent être utilisées,
- quelles sont les méthodes de planification à utiliser selon le cas.

Vous pouvez utiliser chaque méthode de planification seule ou en {% link_new combinaison | features/scheduling/combined-scheduling-methods.md %}.

Les méthodes de planification prennent en compte les informations des {% link_new contrats | features/administration/create-contracts.md %} assignés aux employés. Les contrats définissent le nombre de journées de travail, le nombre d’heures de travail par journée, semaine ou mois et d’autres paramètres de planification.
## Planification fixe

La planification fixe est l’option la moins flexible. Cette méthode de planification est basée sur les {% link_new rotations&nbsp;d’horaires | features/administration/shift-sequences.md %}.

Les rotations d’horaires définissent&nbsp;:  
- les journées de travail d’un employé sur une semaine,
- l’heure de début et de fin exactes de la mission pour chaque journée de travail.

Les plannings créés à partir de ces rotations d’horaires peuvent être les mêmes chaque semaine ou changer par intervalle de 2 à 53&nbsp;semaines.  

Après la création du planning, vous pouvez optimiser les éléments suivants&nbsp;:  
- le positionnement des pauses dans les {% link_new corridors | features/administration/daymodels/daymodel-basics.md | #éléments-fixes-et-corridors %},
- les {% link_new activités remplaçables | features/administration/activity-types-and-properties.md | #propriétés-des-activités %}.

## Planification optimisée

La planification optimisée est l’option la plus flexible. Utilisez la fonction {% link_new Optimiser&nbsp;le&nbsp;planning | features/scheduling/schedules/schedules-optimized-schedules.md %} pour créer automatiquement un planning complet. injixo planifiera la meilleure couverture possible pour les différentes activités, avec le moins d’employés possible.

Pour définir les missions à planifier, utilisez les {% link_new modèles&nbsp;de&nbsp;planification | features/administration/work-time-pattern-models.md %}.

### Horaires totalement flexibles

Pour créer des horaires totalement flexibles, assignez le modèle de planification de {% link_new type&nbsp;A | features/administration/work-time-pattern-models.md | #types-de-modèles-de-planification %} à vos employés.  

Tout horaire disponible conforme au modèle de planification et au contrat de l’employé peut être planifié sur n’importe quelle journée.

Pour augmenter les chances que vos plannings soient acceptés par vos employés, vous pouvez exclure certains horaires en ajoutant des modèles horaires personnels aux employés ou en utilisant les [disponibilités](#disponibilités).

### Roulements flexibles

Pour créer des roulements flexibles, assignez les modèles de planification de {% link_new type&nbsp;B, C, ou D | features/administration/work-time-pattern-models.md | #types-de-modèles-de-planification %} à vos employés.

Les horaires disponibles conformément au modèle de planification sélectionné et au contrat de l’employé sont planifiés dans un ordre spécifique. Ils peuvent avoir la même heure de début chaque jour.

### Disponibilités

Les {% link_new disponibilités | features/administration/availabilities.md %} peuvent compléter la planification optimisée afin de limiter les options des missions.

## Génération de missions

Dans la {% link_new génération&nbsp;de&nbsp;missions | features/scheduling/schedules/schedules-shift-bidding.md %}, le planning final est généré après l’inscription de vos employés. Ils peuvent demander les horaires de leur choix dans le portail employé.

Vue d’ensemble du processus&nbsp;:

1. Définissez le nombre de missions nécessaires.
2. Générez des missions selon le besoin en personnel.
3. Attribuez le statut **Publiée** à votre période de planification. Vos employés peuvent demander deux missions par jour (jusqu’à 10 au total).
4. Lancez un nouveau {% link_new tirage au sort | features/scheduling/shift-bidding.md | #tirage-au-sort %} pour les missions demandées.
5. Attribuez les missions restantes. Les employés dont les demandes n’ont pas été satisfaites seront planifiés lors de cette étape.
