---
title: Supprimer le contenu des catégories
product_label:
  - advanced
  - enterprise
description: Suppression des données de planification d'une ou plusieurs catégories
toc: false
redirect_from:
  - /fr/schedules-supprimer-categorie/
redirect_reason: Updated filename on 21 April 2022
---

_Plan > Schedules_{:.breadcrumbs} permet de supprimer les données de planification pour une sélection d'employés sur une ou plusieurs catégories.

## Suppression des données de planification

Les étapes suivantes permettent de supprimer les données de planification :

1. Cliquer sur _Actions de planification_{:.doc-button}.
2. Sélectionner **Supprimer le contenu des catégories**.
3. Sélectionner une **Unité opérationnelle** dans la section _Paramètres_.
4. Modifier la **Période** (facultatif). La période est pré-remplie avec la période sélectionnée dans _Schedules_.
5. Cocher la ou les catégories concernées dans la section **Catégorie(s) dont le contenu doit être supprimé**.
6. Cocher les employés concernés dans la section **Employés**. Vous pouvez filtrer les employés en sélectionnant un Groupe ou un filtre avancé à partir de la liste déroulante.
7. Cliquer sur _Supprimer le contenu des catégories_{:.doc-button}.

{{ 1 | image: 'Empty level dialog', '80%' }}

Une notification dans le module _Schedules_ vous indiquera si la tâche a correctement démarré.

> Soyez prudents lors de la suppression des données car cette action est irréversible.

> Nous vous conseillons de ne pas supprimer les Desiderata de congés & absences.
>
> Les {% link_new desiderata de congés & absences | features/scheduling/time-off/vacation-absences-management.md %} validés sont présents uniquement dans la catégorie _Planning_. Si vous supprimez le contenu de la catégorie _Planning_ comme expliqués ci-dessus, tous les congés validés seront donc également supprimés sans aucun moyen de les récupérer. Nous vous conseillons donc de réaliser une sauvegarde des congés validés dans une autre catégorie.
