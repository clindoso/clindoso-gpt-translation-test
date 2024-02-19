---
title: Filtrer à l’aide des groupes
description: Découvrez comment utiliser les groupes comme filtre.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: true
---

Vous débutez avec les groupes&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/administration/selections.md %}.

Lorsque vous gérez votre équipe, vous devez souvent grouper les employés ayant des conditions de travail similaires, par exemple ceux devant se rendre à la garderie ou encore ceux dépendant d’un superviseur en particulier. Les groupes vous permettent créer vos propres critères de regroupement, ce qui est utile si vous avez besoin d’options de regroupement allant au-delà des {% link_new unités opérationnelles | features/administration/create-and-manage-planning-units.md %} et du {% link_new filtre avancé | features/administration/employee-filter.md %}.

Les unités opérationnelles vous aident à regrouper les employés selon la structure de votre organisation, par exemple en assignant les employés travaillant sur différents fuseaux horaires à différentes unités opérationnelles. Le filtre avancé agit en fonction des éléments de configuration d’injixo, comme les contrats et les activités. Les groupes vous aident à regrouper les employés pour répondre aux besoins de votre organisation.

Vous pouvez créer un groupe pour affiner les filtres sur une unité opérationnelle ou pour gérer les employés sur les différentes unités opérationnelles. Par exemple, vous pouvez créer un groupe pour vous assurer que les plannings des employés devant se rendre à la garderie soient gérés séparément, ou pour filtrer les plannings des employés de différentes unités opérationnelles pour une campagne marketing sur différents fuseaux horaires.

## Utiliser les groupes pour filtrer les employés dans les unités opérationnelles

injixo propose des filtres basés sur les unités opérationnelles et les groupes dans **Plan** et **Intraday**. Après avoir sélectionné l’unité opérationnelle, vous pouvez également filtrer les employés par groupe.

Exemple&nbsp;: vous avez trois unités opérationnelles et l’une des unités opérationnelles inclut des employés participant à un programme de formation. Vous pouvez utiliser les groupes pour les regrouper et gérer leurs plannings séparément, par exemple pour planifier des réunions spécifiques.

## Utiliser les groupes pour gérer les employés de différentes unités opérationnelles

Dans injixo, il existe trois façons de filtrer à l’aide des groupes dans les unités opérationnelles. Vous pouvez trouver des exemples de filtrage à l’aide des groupes sous cette section.

Le tableau suivant présente une vue d’ensemble des trois options différentes pour filtrer par groupe dans les unités opérationnelles. Vous trouverez ces options dans les composants ou les fonctionnalités d’injixo.

| Composant/fonctionnalité | Option de filtrage |
|-------------------------|----------------------------|
| Schedules               | Toutes les unités opérationnelles et un groupe. |
| Congés/Absences                | Toutes les unités opérationnelles et un groupe. |
| Adhérence Temps Réel     | Un groupe et aucune unité opérationnelle |
| Adhérence Intrajournalière      | Un groupe et aucune unité opérationnelle |
| Centre de planification            | Une sélection (aucun filtre d’unité opérationnelle disponible). |
| Notifier les employés           | Une unité opérationnelle et un groupe. Répétez ces étapes pour toutes les unités opérationnelles que vous souhaitez filtrer. |
| Période de planification  | Une unité opérationnelle et un groupe. Répétez ces étapes pour toutes les unités opérationnelles que vous souhaitez filtrer. |
| Meetings                | Une unité opérationnelle et un groupe. Répétez ces étapes pour toutes les unités opérationnelles que vous souhaitez filtrer. |
| Périodes de congés        | Une unité opérationnelle et un groupe. Répétez ces étapes pour toutes les unités opérationnelles que vous souhaitez filtrer. |
| Droits aux congés    | Une unité opérationnelle et un groupe. Répétez ces étapes pour toutes les unités opérationnelles que vous souhaitez filtrer. |

Pour toutes les fonctionnalités de _Plan > Schedules > Actions de planification_{:.breadcrumbs}, vous devez sélectionner une unité opérationnelle et un groupe, et appliquer l’action de planification à chaque unité opérationnelle que vous souhaitez filtrer.

Les exemples suivants donnent davantage de détails sur les trois options de filtrage pour les groupes, comme indiqué dans le tableau ci-dessis.

## Exemples

Les exemples ci-dessous utilisent un groupe appelé Onboarding. Le groupe Onboarding a pour but de regrouper les employés en phase d’onboarding dans votre organisation, quelle que soit leur unité opérationnelle. En utilisant le groupe Onboarding, il est plus simple de gérer leurs plannings et de suivre leurs besoins.

Avec la configuration suivante, vous pouvez utiliser le groupe Onboarding comme filtre couvrant les unités opérationnelles&nbsp;:

1. {% link_new Créez et configurez un groupe | features/administration/selections.md | #créer-un-groupe %} appelé Onboarding.
2. {% link_new Assignez les employés | features/administration/selections.md | #assigner-des-employés-aux-groupes %} en phase d’onboarding au groupe Onboarding.

### Option de filtrage&nbsp;1&nbsp;: toutes les unités opérationnelles et un groupe

Dans _Plan > Schedules_{:.breadcrumbs}, vous pouvez filtrer les plannings des employés du groupe Onboarding à l’aide des menus déroulants suivants&nbsp;:

- **Unité opérationnelle**&nbsp;: sélectionnez **Toutes les unités opérationnelles**.
- **Sélectionnez un groupe**&nbsp;: sélectionnez **Onboarding**.  
   Si le menu déroulant **Sélectionner un groupe** ne s’affiche pas, cliquez sur l’icône Filtrer les groupes {% icon selection-filter-u | icon-only %} en haut à gauche.

### Option de filtrage&nbsp;2&nbsp;: un groupe et aucune unité opérationnelle

Dans _Intraday > Adhérence Temps Réel_{:.breadcrumbs}, vous pouvez filtrer les activités planifiées des employés du groupe Onboarding et les comparer avec le statut actuel d’un employé en temps réel. Ceci est utile, notamment pour vérifier si un employé réalise les activités prévues dans sa phase d’onboarding.

Pour filtrer par groupe, utilisez les menus déroulants suivants&nbsp;:

- **Unité opérationnelle**&nbsp;: assurez-vous qu’aucune unité opérationnelle n’est sélectionnée.
- **Groupe**&nbsp;: sélectionnez **Onboarding**.

### Option de filtrage&nbsp;3&nbsp;: un groupe et une unité opérationnelle

S’il existe certaines conditions spécifiques concernant les congés/absences pour les employés en phase d’onboarding, vous pouvez créer des périodes de congé pour le groupe Onboarding. Par exemple, si vous avez les unités opérationnelles suivantes pour trois bureaux différents&nbsp;: Bureau&nbsp;1, Bureau&nbsp;2 et Bureau&nbsp;3. Ces trois bureaux comprennent des employés en phase d’onboarding et assignés au groupe Onboarding.

 Pour créer des périodes de congés spécifiques pour le groupe Onboarding&nbsp;:

1. Dans _Plan > Congés/Absences_{:.breadcrumbs}, cliquez sur _Période de congés_{:.doc-button}.  
   Vous serez redirigé vers la page **Période de congés**.
2. Cliquez sur _Nouvelle période de congés_{:.doc-button}.  
   Une fenêtre s’ouvre.
3. Filtrez par groupe à l’aide des menus déroulants suivants&nbsp;:  
   - **Unité opérationnelle**&nbsp;: sélectionnez **Bureau&nbsp;1**.
   - **Groupe**&nbsp;: sélectionnez **Onboarding**.
4. Remplissez les champs restants.  
   En savoir plus sur le configuration des {% link_new périodes de congés | features/scheduling/time-off/time-off-periods.md %}.
5. Cliquez sur _Enregistrer_{:.doc-button}.
6. Répétez les étapes 1 à 5 pour les unités opérationnelles Bureau&nbsp;2 et Bureau&nbsp;3.
