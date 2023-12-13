---
title: Vue d'ensemble
product_label:
  - advanced
  - enterprise
toc: false
permalink: /fr/meetings/
redirect_from:
  - /fr/meetings-vue-ensemble/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/meetings/scheduling-suggestions.md
---

<!-- permalink reason: /de/meetings-overview/ used in email and in Intercom message-->

**Meetings** vous permet d'économiser du temps et des efforts en trouvant le meilleur créneau pour vos réunions.

Grâce à l'utilisation d'algorithmes performants, _Meetings_{:.menu-item} vous garantit que les réunions proposées sont optimales en termes d'impact sur la couverture des Activités et vous fait gagner un temps précieux sur leur gestion quotidienne.

Meetings est disponible au menu _Plan > Meetings_{:.breadcrumbs} et vous permet de planifier 3 types de réunions :

- {% link_new Réunions 1:1 | features/scheduling/meetings/one-on-ones.md %} : utiliser cette option pour planifier une réunion entre un Employé et un responsable d'équipe d'une même Unité opérationnelle.
- {% link_new Autoformations | features/scheduling/meetings/self-learning-sessions.md %}: utiliser cette option pour planifier des sessions individuelles de formation pour les employés.
- {% link_new Réunions de groupe | features/scheduling/meetings/group-meetings.md %}: utiliser cette option pour planifier une réunion de groupe pour vos employés avec ou sans organisateur.

{{ 1 | image: 'Overview page'}}

## Prérequis d'utilisation

Les prérequis sont les suivants :

- Pour planifier une réunion, l'Employé doit disposer d'un planning sur la période concernée dans la catégorie _Planning_.
  _Meetings_{:.menu-item} peut uniquement remplacer les Activités de type _Présence_ qui sont _Remplaçables_. Par conséquent, les activités d'un autre type ne seront pas remplacées même si elles sont remplaçables
- Les employés ne faisant pas partie de l'Unité opérationnelle concernée sur la période sélectionnée sont exclus des propositions de réunions.
- Toutes les dates et heures des réunions font référence au fuseau horaire de l’Unité opérationnelle
- La durée maximale de l'optimisation est de 10 minutes.

## Utilisation de Meetings

Suivez les étapes suivantes pour générer des propositions de réunions :

1. Aller à _Plan > Meetings_{:.breadcrumbs}.
2. Sélectionner le type de réunion à planifier. Vous pouvez choisir entre des {% link_new Réunions 1:1 | features/scheduling/meetings/one-on-ones.md %}, des {% link_new Autoformations | features/scheduling/meetings/self-learning-sessions.md %} ou des {% link_new Réunions de groupe | features/scheduling/meetings/group-meetings.md %}. Cliquer sur le bouton _Paramétrage_{:.doc-button} du type de réunion souhaité.
3. Renseigner les **paramètres** pour le type de réunion sélectionné.
4. Cliquer sur **Générer les propositions**.

Les propositions générées apparaissent à la section _Propositions disponibles_. Cette section affiche la date et l'heure auxquelles le processus a été lancé, le type de réunion, l'unité opérationnelle concernée, le nombre de participants et les actions possibles à réaliser.

Vous pouvez alors :

- {% link_new Voir | features/scheduling/meetings/scheduling-suggestions.md | #voir-les-propositions-de-réunions %} les propositions de réunions.
- {% link_new Planifier | features/scheduling/meetings/scheduling-suggestions.md | #planifier-les-propositions %} les propositions.
