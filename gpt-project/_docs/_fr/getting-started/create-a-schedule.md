---
title: Créer un planning
description: Suivez les étapes principales pour la création d’un planning.
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
related_articles:
  - overwrite_title: Résoudre les problèmes de planification
    filepath: best-practices/resolve-optimization-issues.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/why-level-copy.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/meetings/meetings-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-extra-activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-replace-activities.md
  - overwrite_title: Planifier les jours fériés
    filepath: best-practices/scheduling-public-holidays.md
redirect_from:
  - /fr/quickstart-scheduling/
redirect_reason: Updated filename on 27 July 2023
---

La création de plannings est une partie essentielle du {% link_new cycle du WFM | getting-started/the-wfm-cycle-in-injixo.md %}. Les plannings contiennent les journées et les activitées prévus pour vos employés.  

Utilisez cet article pour vérifier que toutes les étapes ont bien été suivies lors de l’onboarding.

Remarque&nbsp;: dans injixo Essential WFM, vous ne pouvez sauvegarder ni vos demandes de congés, ni le planning final.

## Prérequis

Avant de créer un planning, assurez-vous d’avoir correctement {% link_new mis en place votre configuration minimale | getting-started/set-up-base-configuration.md %} et {% link_new généré une prévision | getting-started/calculate-a-forecast.md %}. 

## Ordre de configuration

Nous vous recommandons de configurer les éléments de configuration dans l’ordre présenté dans cet article. Aucune configuration n’est identique, c’est pourquoi l’ordre optimal de configuration peut être différent pour votre organisation. N’hésitez pas à contacter votre consultant si vous avez des questions.

## Configurer les congés

Les employés peuvent demander des congés via injixo Me. Pour configurer les congés, accédez à _Plan > Congés/Absences_{:.breadcrumbs}&nbsp;:

1. Entrez les {% link_new droits aux congés | features/scheduling/time-off/vacation-entitlement.md %} de vos employés pour l’année en cours.
2. Créez une {% link_new période de congés | features/scheduling/time-off/time-off-periods.md %} et publiez-la. Une période de congé définit la période pendant laquelle les employés peuvent demander des congés et autres absences. Les employés recevront une notification dans injixo Me et pourront commencer à créer des demandes de congé pour cette période.

## Ajouter des activités de type Maladie ou Absence

Dans {% link_new Schedules | features/scheduling/schedules/schedules-overview.md %} et le {% link_new Centre de planification | features/scheduling/shiftcenter/shift-center-overview.md %}, vous pouvez gérer le planning de votre équipe. Entrez les {% link_new activités | features/administration/activity-types-and-properties.md | #types-dactivité %} de type Absence ou Maladie prévues dans le planning.

## Gérer les demandes de congé

Dans _Plan > Congés/Absences_{:.breadcrumbs}, approuvez ou rejetez les {% link_new demandes en attente | features/scheduling/time-off/vacation-absences-management.md %}.

> Créez une sauvegarde du planning en cours dans une autre catégorie
>
> Utilisez la fonction {% link_new Copier le contenu de la catégorie | features/scheduling/schedules/schedules-copy-level-content.md %} pour sauvegarder une copie de votre planning. Cela vous permet de ne pas perdre les demandes de congé approuvées ou les absences précédemment saisies si vous supprimez le planning et recommencez.

## Créer le planning

Dans {% link_new Schedules | features/scheduling/schedules/schedules-overview.md %}, le {% link_new Centre de planification | features/scheduling/shiftcenter/shift-center-overview.md %} ou {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %}, vérifiez si le {% link_new besoin en personnel | features/forecast/injixo-forecast/calculate-staff-requirements.md %} est correctement configuré pour vos activités.

1. Insérez des {% link_new rotations d’horaires | features/scheduling/schedules/schedules-insert-shift-sequences.md %} pour vos employés.
2. Configurez et utilisez d’autres {% link_new méthodes de planification | features/scheduling/scheduling-methods.md %} pour compléter le planning.
3. {% link_new Optimisez les activités | features/scheduling/schedules/schedules-job-optimization.md %}. Vous pouvez passer cette étape si vous {% link_new créez un planning optimisé | features/scheduling/schedules/schedules-job-optimization.md %}.

Conseil&nbsp;: si vous créez un planning à des fins de test, vous pouvez utiliser des {% link_new catégories vides | features/scheduling/schedules/schedules-empty-levels.md %}. Récupérez les demandes d’absences et de congés précédemment sauvegardées dans la catégorie Planning avant chaque test.

## Sauvegarder le planning final

Avant d’appliquer vos {% link_new modifications manuelles<sup>(en anglais)</sup>| features/scheduling/shiftcenter/modify-items.md %} <!--- todo: replace link when translated --> à votre planning original, {% link_new enregistrez une sauvegarde | features/scheduling/schedules/schedules-copy-level-content.md %} dans la catégorie État actuel. Ceci vous permet d’évaluer la pertinence de votre planning original par rapport aux versions suivantes.

## Publier le planning et autoriser les échanges de plannings

1. Créez et publiez une période de planification pour {% link_new permettre aux employés de consulter leur planning | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %} dans injixo Me.
2. (Facultatif) {% link_new Autorisez les échanges de journées | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %} entre les employés.  
    Par défaut, vous devez {% link_new consulter et approuver les échanges de journées en attente | features/scheduling/view-approve-shift-swap-requests.md %}, mais vous pouvez également autoriser des échanges automatiques entre les employés avec le paramètre _48152_{:.id-label} **Mode de déroulement des échanges de plannings**.
3. Partagez l’article {% link_new Explorez injixo Me | features/injixo-me/use-injixo-me/explore-injixo-me.md %} avec vos employés.
