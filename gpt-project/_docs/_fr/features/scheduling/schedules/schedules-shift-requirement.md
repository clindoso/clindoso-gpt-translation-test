---
title: Besoin en missions
redirect_from:
  - /fr/besoin-missions/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-basics.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/day-types.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/employee-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
---

Le menu *WFM > Scheduling > Planification > Besoin en missions*{:.breadcrumbs} vous permet de définir le nombre minimum et maximum de Modèles horaires nécessaires pour chaque Type de jours (Lundi, Noël,..). Le Besoin en missions et le Besoin en personnel sont pris en compte lorsque vous utilisez la fonction `Générer`du menu *Période de planification*{:.menu-item}.

La `Génération de missions`, à l'opposé de l'optimisation complète (aussi appelée Autoscheduler), ne prend pas en compte les Employés et leurs Contrats pour la création des missions. Une mission correspond à une journée de travail avec une heure de début, une heure de fin et éventuellement une ou plusieurs pauses.

Par défaut, les missions sont créées sur la base des valeurs du tableau du Besoin en personnel. En conséquence, il y a un risque que toutes les missions générées ne puissent être couvertes car il se peut qu'il n'y ait pas assez d'Employés dont les contraintes horaires correspondent aux missions générées. Afin d'améliorer l'efficacité de la `Génération de missions`, il est recommandé de saisir des valeurs dans le tableau de Besoin en missions. Sur la base de votre connaissance des Employés planifiés, vous pouvez définir le nombre minimum et maximum d'Employés en mesure de réaliser chaque Modèle horaire. 

> Remarque
>
> Les valeurs que vous saisissez dans le tableau de Besoin en missions n'équivaut pas au nombre d'Employés requis par activité et par intervalle horaire. Le tableau sert à contraindre le nombre de missions générées selon un principe de minimum/maximum.

Lorsque vous utilisez le bouton `Générer`pour créer les missions, les valeurs présentes dans le tableau de Besoin en missions et Besoin en personnel sont prises en compte.

## Tableau de Besoin en missions

Sélectionnez dans la liste déroulante l'Unité opérationnelle sur laquelle vous souhaitez travailler, un tableau présentant le Besoin en missions s'affiche. Chaque ligne de ce tableau correspond à un Modèle horaire de type `Fixe`ou `Variable` disponible pour l'Unité opérationnelle sélectionnée et chaque colonne correspond à un Type de jours.

Par défaut, tous les Modèles horaires sont affectés à toutes les Unités opérationnelles. Le menu *WFM > Administration > Planification > Unités opérationnelles*{:.breadcrumbs} vous permet d'attribuer des Modèles horaires spécifiquement à des Unités opérationnelles. Dans ce cas, le tableau de besoin en missions n'affichera que les Modèles horaires attribués à cette Unité opérationnelle.

Le tableau affiche les valeurs minimum et maximum. Vous pouvez saisir et modifier les valeurs en cliquant sur les cellules correspondantes.

> Remarque
>
> Le tableau affiche également le Besoin en missions pour des Types de jours qui ont été supprimés dans le menu *Administration*{:.menu-item}. Ces valeurs sont alors affichées en italique et ne peuvent être modifiées.

## Saisir un Besoin en missions

Lors de cette étape, vous définissez le nombre minimum et maximum de Modèles horaires `Fixes` et `Variables` qui peuvent être crées pour l'Unité opérationnelle sélectionnée. Si vous utilisez les Rotations d'horaires, le nombre de Modèles Horaires que vous allez utiliser lors de l'insertion de la Rotation d'horaires doit être comptabilisé dans la valeur minimum.

**Exemple**

Supposons que vous ayez défini une Rotation d'horaires qui insère un Modèle horaire spécifique 2 fois sur la journée du lundi. Si vous souhaitez disposer de 3 missions supplémentaires utilisant ce Modèle horaire sur la journée du lundi lors de la Génération de missions, vous devez définir comme valeur minimum `5` (2+3) dans le tableau.

**Plage de valeurs**

Les valeurs doivent être des nombres entiers. Vous pouvez saisir le même nombre pour la valeur minimum et maximum. Ainsi, vous définirez une valeur cible. Dans ce cas, un nombre fixe de missions est créé lors de la Génération de missions, quel que soit le Besoin en personnel calculé lors de la prévision.

Nous recommandons de laisser le plus de cellules vierges possibles. Si vous ne saisissez des valeurs que sur des horaires sensibles, la Génération de missions sera plus apte à couvrir de façon optimale le Besoin en personnel.

> Remarque
>
> Pour les journées non travaillées (jours fériés par exemple), il est recommandé de définir le Besoin en missions à `0`. De cette façon, vous vous assurez qu'aucune mission ne sera créée sur ces journées.

Si vous essayez de saisir une valeur minimum qui ne soit pas inférieure ou égale à la valeur maximum, un message d'erreur vous demandera de corriger la saisie. Une fois la saisie terminée, cliquez sur le bouton `Enregistrer` sous le tableau.

Les Modèles horaires utilisés lors de planification peuvent être visualisés dans l'onglet `Modèles horaires - Couverture` de la `Heatmap` du *Centre de planification*{:.menu-item}. Vous pouvez également afficher le besoin, l'occupation et la couverture en faisant un clic droit sur une cellule du tableau.

## Besoin en missions dans le Centre de planification

Vous pouvez obtenir plus d'informations sur le Besoin en mission dans l'onglet `Activités - Besoin` de la `Heatmap` du Centre de planification en faisant un clic droit sur les cellules du tableau pour afficher les données suivantes :
- `Occupation par rapport au Besoin en missions`
 Cet indicateur permet de mesurer la qualité de la `Génération de missions` en indiquant comment le Besoin en personnel pour cette Activité serait couvert si toutes les missions générées avaient été occupées.
 - `Couverture par rapport au Besoin en missions`
 Cet indicateur affiche la différence entre les missions nécessaires pour couvrir 100% du Besoin en missions et les créneaux horaires effectivement générés.
