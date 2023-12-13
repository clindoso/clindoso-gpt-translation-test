---
title: Besoin en personnel
redirect_from:
  - /fr/planification-besoin-en-personnel/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/calculate-a-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/staff-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
---

Le menu *WFM > Planification > SchedulePro > Besoin en personnel*{:.breadcrumbs} vous permet de visualiser et modifier si nécessaire le besoin en personnel pour chaque Activité de vos Unités opérationnelles. Le besoin en personnel est un élément essentiel de la création des plannings.

Le besoin en personnel est calculé puis transféré dans le module de planification depuis *Forecast*{:.menu-item}. Lors de cette opération, le fuseau horaire et l'intervalle paramétrés pour l'Unité opérationnelle (15, 30 ou 60 minutes) sont respectés.

Avant d'optimiser les plannings de vos Employés, il est conseillé de bien vérifier que le besoin en personnel a été correctement transféré depuis *Forecast*{:.menu-item}.

Le besoin en personnel peut également être renseigné manuellement ou copié depuis un fichier Excel (possédant le même format). Utilisez alors des nombres positifs à deux décimales au maximum.

> Remarque
>
> Le menu *Besoin en personnel*{:.menu-item} affiche les valeurs calculées ou renseignées manuellement pour chaque Activité. Vous pouvez visualiser le besoin global dans la `Heatmap` du *Centre de planification*{:.menu-item} (à la ligne "Toutes les présences").

## Afficher le besoin en personnel

Il faut tout d'abord renseigner les paramètres suivants :

| Unité opérationnelle | Sélectionner l'Unité opérationnelle pour laquelle vous souhaitez afficher les valeurs du besoin en personnel. La dernière Unité opérationnelle consultée est affichée par défaut. |
| Date | Sélectionner la date à laquelle le besoin en personnel doit être affiché. La date du jour est affichée par défaut. |

Cliquer sur *Appliquer*{:.doc-button} pour confirmer la sélection et afficher le besoin en personnel des différentes Activités de l'Unité opérationnelle à la date souhaitée. Vous pouvez ainsi vérifier que le transfert du besoin en personnel depuis *Forecast*{:.menu-item} a bien été réalisé.

> Remarque
>
> Le nom des Activités supprimées est affiché en italique et la ligne correspondante est grisée. Les Multi-Activités apparaissent en gras et leur Sous-Activités sont classées par ordre alphabétique en dessous.

## Renseigner manuellement un besoin en personnel

Pour renseigner manuellement le besoin en personnel d'une Activité, cliquer sur la cellule de l'intervalle souhaité et entrer la valeur correspondante.
Il est également possible de renseigner le besoin en personnel pour plusieurs Activités et sur plusieurs intervalles à la fois en copiant-collant des valeurs provenant d'une feuille Excel (possédant le même format).

Cliquer sur *Enregistrer*{:.doc-button} pour sauvegarder la saisie.

## Supprimer un besoin en personnel

Pour supprimer le besoin en personnel d'une Activité donnée, sélectionner les intervalles à supprimer et utiliser la touche de suppression de votre clavier. Cliquer sur *Enregistrer*{:.doc-button} pour valider l'opération.
Le besoin en personnel est alors remis à zéro.
