---
title: Périodes de congés
description: Comprendre les Périodes de congés.
product_label:
  - essential
  - advanced
  - enterprise
redirect_from:
  - /fr/conges-absences-periodes-de-conges/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-entitlement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-absences-management.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md
---

## Vue d'ensemble

Dans le menu _Plan > Congés/Absences > Périodes de congés_{:.breadcrumbs}, vous définissez sur quelle période et quelle Activité les Employés peuvent effectuer des demandes de congés dans le portail _injixo Me_. Les Périodes de congés peuvent être définies par Unité opérationnelle et par Groupe.

Vous pouvez créer une période de congés pour toutes les Activités de type _Absence_, _Congés_ ou _Maladie_ paramétrées en tant que {% link_new *Desiderata* | features/administration/activities.md %}.

> Remarque
>
> L'option doit être activée dans _injixo Me_ pour que vos employés puissent soumettre leurs demandes d'absences. Pour se faire, connectez-vous en tant qu'Admin puis cliquez sur _Me_{:.breadcrumbs} dans la barre de navigation supérieure et activez l'option **Demandes d'absences**.

### Statut de la Période de congés

Le statut de la Période de congés détermine si les Employés peuvent soumettre leurs desiderata d'absences pour la période concernée. Ce statut peut être modifié à tout moment.

| Statut      | Description                                                                                                                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Non publiée | Les employés ne peuvent pas soumettre leurs desiderata d'absences dans _injixo Me_.                                                                                                              |
| Publiée     | Les employés peuvent soumettre leurs desiderata d'absences dans _injixo Me_. Une Période de congés publiée apparaît en blanc dans le calendrier du menu _Absences_{:.breadcrumbs} d'_injixo Me_. |

## Afficher les Périodes de congés

Suivez les étapes suivantes pour afficher les Périodes de congés :

1. Aller à _Plan > Congés/Absences_{:.breadcrumbs}
2. Cliquer sur _Période de congés_{:.doc-button} en haut à droite de l'écran
3. Sélectionner l'**Unité opérationnelle** et l'**Activité** pour mettre à jour la liste
4. Optionnel : sélectionner un **Groupe** pour filtrer à nouveau les résultats

Le système affiche 2 onglets :

- les Périodes de congés en cours dans l'onglet _En cours_
- les Périodes de congés expirées dans l'onglet _Expirée_

{{ 1 | image: "Vue d'ensemble", '90%' }}

Les informations affichées pour chaque onglet sont les suivantes :

- _Statut_ : Statut de la Période de congés
- _Groupe_ : Groupe pour lequel la Période de congés a été créée.
- _Valide du_ : Date de début de la Période de congés
- _Jusqu'au_ : Date de fin de la Période de congés (1 an maximum).
- _Date limite_ (optionnel) : Date jusqu’à laquelle les employés peuvent saisir leurs desiderata d’absences. Cette date doit toujours être antérieure à la date de début de la Période de congés. Vous pouvez également décider de ne pas définir de date limite.
- _Héritée_ : Indique si cette Période de congés est héritée d'une autre Période de congés créée pour une **Unité opérationnelle** supérieure.

Vous pouvez trier les informations affichées en cliquant sur l'en-tête de la colonne concernée.

## Créer une Période de congés

Suivez les étapes suivantes pour créer une Période de congés :

1. Aller à _Plan > Congés/Absences_{:.breadcrumbs}.
2. Cliquer sur _Période de congés_{:.doc-button} en haut à droite de l'écran.
3. Cliquer sur _Créer une période de congés_{:.doc-button}.
4. Sélectionner l'**Unité opérationnelle**, le **Groupe** (optionnel) et l'**Activité**.
5. Renseigner les dates de début et de fin de la Période de congés.
6. Optionnel : renseigner une _Date limite_ (date jusqu’à laquelle les employés peuvent saisir leurs desiderata d’absences).
7. Sélectionner un _Statut_. Les employés pourront soumettre leur desiderata d'absences si le statut **Publiée** est sélectionné.
8. Cliquer sur _Enregistrer_{:.doc-button} pour créer la Période de congés.

   {{ 2 | image: "Edition de la Période de congés", '40%' }}

## Modifier une Période de congés

Pour modifier le statut d'une Période de congés, sélectionnez le statut souhaité en cliquant dans le **menu déroulant** de la colonne _Statut_ pour la Période de congés concernée.

Pour modifier les paramètres de la Période de congés, cliquez sur l'icône en forme de crayon qui apparaît lorsque vous passez le curseur sur la Période de congés concernée. Vous pouvez modifier :

- Le Groupe
- L'Activité
- Les dates de début et de fin de la période
- La date limite
- Le statut

## Supprimer une Période de congés

Pour supprimer une ou plusieurs Périodes de congés, utilisez la **case à cocher** à gauche des Périodes concernées pour les sélectionner puis cliquer sur _Supprimer les lignes_{:.doc-button}.
