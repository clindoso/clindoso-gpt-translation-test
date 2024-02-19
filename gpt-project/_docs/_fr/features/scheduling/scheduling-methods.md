---
title: Méthodes de planification
promote-service: new-planner-training
description: Découvrez les différentes méthodes de planification dans injixo.
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

injixo propose différentes méthodes de planification, que vous pouvez utiliser individuellement ou {% link_new combiner | features/scheduling/combined-scheduling-methods.md %}.

Les différentes méthodes de planification sont conçues pour s'adapter à différents scénarios. Tous les méthodes de planification tiennent compte des informations configurées dans les {% link_new contrats | features/administration/create-contracts.md %} de vos employés, telles que le nombre de jours de travail, les heures de travail par jour, semaine ou mois, ainsi que d'autres paramètres de planification.

## Prérequis

Avant de commencer à utiliser les méthodes de planification, assurez-vous d'avoir configuré les données de configuration suivantes dans _Plan > Configuration_{:.breadcrumbs}&nbsp;:

- compétences,
- activités,
- modèles horaires,
- unités opérationnelles,
- contrats,
- employés.

Certaines méthodes de planification peuvent également demander le paramétrage d’autres données de configuration, par exemple les rotations d’horaires ou les modèles de planification.

## Planification fixe

La méthode de planification fixe est basée sur des {% link_new rotations d’horaires | features/administration/shift-sequences.md %}. Une rotation d’horaires est un cycle de modèles horaires ou d’activités qui définit les jours pendant lesquels un employé travaille, ainsi que les heures de début et de fin exactes de la journée. Par conséquent, la planification fixe est la méthode de planification la plus cohérente, mais elle offre le moins de flexibilité.

Les plannings créés à partir des rotations d’horaires peuvent être les mêmes chaque semaine ou changer par intervalle de 2 à 53 semaines.

Une fois le planning créé, vous pouvez toujours utiliser la fonctionnalité {% link_new Optimiser les pauses | features/scheduling/schedules/break-optimization.md %} ou {% link_new Optimiser les activités | features/scheduling/schedules/schedules-job-optimization.md %} pour optimiser davantage votre planning.

**Optimiser les pauses** déplace les pauses planifiées vers le créneau sur lequel elles auront le moins d’impact sur votre couverture. injixo peut seulement déplacer les pauses configurées dans le {% link_new corridor d’un modèle horaire | features/administration/daymodels/daymodel-basics.md | #éléments-fixes-et-corridors %}.

**Optimiser les activités** peut remplacer les activités configurées comme remplaçables par d’autres activités pour obtenir la meilleure couverture possible pour toutes les activités, selon leur besoin en personnel. Les heures de début et de fin des journées restent les mêmes. **Optimiser les activités** peut également modifier les heures de pauses dans un planning, de la même façon que la fonctionnalité **Optimiser les pauses**.

## Planification optimisée

La méthode de planification optimisée est l’option la plus flexible. Cette méthode propose d’utiliser la fonctionnalité {% link_new Optimiser le planning | features/scheduling/schedules/schedules-optimized-schedules.md %} pour créer automatiquement l’ensemble du planning. injixo garantira la meilleure couverture possible pour toutes les activités avec le moins d’employés possible.

Par défaut, la fonctionnalité **Optimiser le planning** peut planifier les employés à l’aide de n’importe quel {% link_new modèle horaire | features/administration/daymodels/daymodel-basics.md %} assigné à leur unité opérationnelle et compatible avec leur contrat. 

Selon votre configuration, l'utilisation de différents modèles horaires dans la planification peut entraîner la création d’horaires incohérents. Par exemple, les employés pourraient être planifiés pour travailler de nuit le lundi, l'après-midi le mardi et le matin le mercredi.

Pour définir les modèles horaires à utiliser pour la création du planning, configurez les {% link_new modèles de planification | features/administration/work-time-pattern-models.md %}. Un modèle de planification est composé de {% link_new modèles hebdomadaires | features/administration/work-time-pattern-models.md | #créer-un-modèle-hebdomadaire %} et définit la façon dont les modèles horaires sont assignés à vos employés. Les modèles de planification vous permettent de créer des cycles de journées et de définir des contraintes de planification pour la fonctionnalité **Optimiser le planning**.

Pour planifier les employés à l’aide de modèles de planification, attribuez un seul modèle de planification à chaque employé concerné. Il n’est pas possible d’attribuer plusieurs modèles de planification à un employé pour une même période de validité.

### Horaires totalement flexibles

Pour créer des plannings dont les horaires sont entièrement flexibles, créez des modèles de planification de {% link_new type A | features/administration/work-time-pattern-models.md | #types-de-modèles-de-planification %} et assignez-les à vos employés.

Avec le type A, injixo peut sélectionner n'importe quel modèle horaire inclus dans le modèle de planification pour chaque jour de chaque semaine, s’il est conforme au contrat d’un employé.

Cette méthode permet de créer les meilleurs plannings pour répondre à vos besoins opérationnels. Cependant, elle peut entraîner la création de plannings incohérents pouvant avoir un impact négatif sur vos employés. Pour réduire cet impact négatif, vous pouvez exclure certaines journées pour certains employés en leur assignant des modèles horaires individuels ou à l’aide des [disponibilités](#disponibilités).

### Roulements flexibles

Pour créer des plannings en roulements flexibles, créez des modèles de planification de {% link_new type B, C ou D | features/administration/work-time-pattern-models.md | #types-de-modèles-de-planification %} et assignez-les à vos employés.

Les types B, C et D vous permettent de définir un ordre spécifique à respecter par injixo lors de la sélection des modèles horaires parmi ceux disponibles dans le modèle horaire sélectionné et compatible avec le contrat de l’employé. Vous pouvez également définir une heure de début fixe pour les journées, ou un cadre temporel dans lequel les journées commencent.

### Disponibilités

Vous pouvez utiliser les {% link_new disponibilités | features/administration/availabilities.md %} pour définir quand les employés ne sont pas disponibles pour travailler un jour en particulier ou sur certains créneaux. Les disponibilités ajoutent d’autres contraintes de planification à celles définies par les contrats et les horaires d’ouverture des unités opérationnelles.

Lorsque des disponibilités sont assignées à vos employés, ils peuvent uniquement être planifiés pour les journées compatibles avec leurs cadres de disponibilité.

## Génération de missions

Si vous utilisez la génération de missions, le planning final est créé seulement après que les employés ont envoyé leurs demandes de journées dans injixo Me.

Pour créer un planning à l’aide de la génération de missions, suivez ces étapes&nbsp;:

1. Définissez le nombre de journées dont vous avez besoin sur une {% link_new période de planification | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %}.
2. {% link_new Générez les missions | features/scheduling/schedules/schedules-shift-bidding.md | #générer-les-missions %} selon le besoin en personnel.
3. Attribuez le statut **Publiée** à votre période de planification. Vos employés peuvent demander deux missions par jour (jusqu’à 10 au total).
4. Lancez un {% link_new tirage au sort | features/scheduling/shift-bidding.md | #tirage-au-sort %} pour les journées demandées. 
5. Attribuez les missions restantes. Les employés dont les demandes n’ont pas été satisfaites seront planifiés lors de cette étape.

Une fois le planning créé, vous pouvez toujours utiliser la fonctionnalité {% link_new Optimiser les activités | features/scheduling/schedules/schedules-job-optimization.md %} pour optimiser les activités et la position des pauses.

> Utilisez l’activité Présent si vous combinez la génération de missions et **Optimiser les activités**
>
> Si les employés peuvent demander des journées dans injixo Me, mais que vous souhaitez **Optimiser les activités** plus tard, utilisez uniquement l’activité système par défaut Présent (ID de l’activité&nbsp;: 1) comme activité dans les modèles horaires. Ainsi, vous évitez que les employés demandent des journées contenant des activités spécifiques, mais se voient ensuite attribuer des activités différentes lorsque vous utilisez la fonctionnalité **Optimiser les activités**.