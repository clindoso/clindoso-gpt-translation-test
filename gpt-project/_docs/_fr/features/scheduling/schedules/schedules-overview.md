---
title: Qu’est ce que Schedules?
product_label:
  - essential
  - advanced
  - enterprise
  - classic
promote-service: team-leader-training
redirect_from:
  - /fr/schedules-vue-ensemble/
redirect_reason: Updated filename on 21 April 2022
---

Dans _Plan > Schedules_{:.breadcrumbs} vous pouvez visualiser et gérer vos plannings de multiples façons.

## Sections

Dans la partie supérieure de l'écran, vous pouvez filtrer les éléments affichés.

Dans la partie centrale, vous pouvez consulter le planning de vos Employés.

Dans la partie inférieure, vous pouvez consulter les données relatives à la planification de vos activités.

{{ 1 | image: 'Vue journalière'}}

### Filtres

{{ 2 | image: 'Filtres'}}

Vous pouvez filtrer la vue selon les éléments suivants : Unités Opérationnelles, Groupe ou Employé.

Pour créer ou modifier un filtre avancé, il suffit de cliquer sur l'icône correspondante puis sur le crayon à droite de `Filtre avancé`.

Par défaut la catégorie _Planning_ est affichée, vous pouvez en afficher une ou plusieurs autres grâce au bouton `Catégorie`.

### Période affichée

La période affichée peut être modifiée des façons suivantes :

- Pour sélectionner une plage de dates, cliquer sur la date ou l'icône du calendrier
- Pour réduire ou agrandir la plage de dates, désélectionner la date de début ou de fin avec d'en choisir une nouvelle
- Pour basculer entre les vues quotidiennes, hebdomadaires et mensuelles, utiliser les raccourcis présents à gauche de la plage de dates
- Pour avancer ou reculer utiliser les flèches droite et gauche
- Pour afficher le détail d'une journée, cliquer sur l'en-tête de celle-ci en haut du planning

### Basculer en mode plein écran

Il est possible de basculer en mode plein écran en cliquant sur l'icône correspondante dans la barre de filtre. Cela vous permet ainsi de visualiser un plus grand nombre d'employé en masquant les filtres et la barre de navigation dans la partie supérieure de l'écran.

Pour afficher à nouveau les filtres, déplacez le curseur en haut de l'écran. Vous pouvez ainsi par exemple changer d'unité opérationnelle ou de plage de dates en restant en mode plein écran.

Pour désactiver le mode plein écran, cliquer sur l'icône correspondante ou appuyer sur la touche `ESC`.

## Planning

La partie centrale de l'écran affiche le planning des Employés.

### Unité opérationnelle & Employés

La colonne de gauche présente les Unités opérationnelles. Le nombre affiché dans la cellule correspond au nombre d'Employés affectés à cette Unité opérationnelle.
La liste des Employés s'affiche en cliquant sur l'Unité opérationnelle. `Nom de l'Employé` présent en tête de colonne vous permet de les trier par ordre ascendant ou descendant.

### Détails concernant les Employés

En passant le curseur sur un Employé, une infobulle apparait et affiche le Contrat et les Compétences de l'Employé. Si vous cliquez sur le nom de l'Employé dans l'infobulle, sa fiche s'ouvre dans une nouvelle fenêtre.

### Catégories

La seconde colonne affiche les `Catégories` de planning. Par défaut la catégorie _Planning_ est affichée, des catégories supplémentaires peuvent être sélectionnées via _Catégorie_{:.doc-button} dans la partie supérieure de l'écran.

### Temps de travail

La troisième colonne affiche le temps de travail planifié, le temps de travail contractuel et la différence des deux. Vous pouvez décider d'afficher ou de masquer ces informations en cliquant sur les flèches de l'en-tête. Vous pouvez afficher les 3 valeurs, uniquement la différence ou masquer toute la colonne.

Un indicateur de couleur permet de savoir si le nombre d'heures contractuelles a été atteint.

- Rouge : la différence est négative
- Bleu : la différence est positive
- Gris : le nombre d'heures contractuelles et planifiées sont identiques

Vous pouvez trier la colonne correspondant à chaque jour par heure de début ou nom de l'Activité. Si vous avez plusieurs Catégories affichées, vous pouvez choisir sur laquelle le tri sera fait.

## Affichage d'une ou plusieurs journées

Vous pouvez naviguer dans le planning en cliquant sur les en-têtes de colonne, ce qui vous permet de visualiser une journée unique, une semaine ou un mois.

Dans la vue journalière, les Activités et les horaires sont affichés. Lorsque vous affichez plusieurs journées, la première Activité de la journée ainsi que la durée de travail sont affichées.

En passant le curseur sur une cellule, une infobulle apparait et affiche la liste des Activités sur cette journée ainsi qu'un éventuel commentaire. Si vous cliquez sur l'icone avec les trois points dans l'en-tête de colonne, vous pouvez trier par date de début ou nom de l'Activité.

Un double clic ouvre le {% link_new mode édition | features/scheduling/schedules/schedules-edit.md %}.

### Changer l'intervalle horaire de la vue journalière

Sélectionner une ou deux journées pour modifier la vue par intervalle horaire de 15 ou 30 minutes. L'intervalle horaire affiché par défaut est 60 minutes.

{{ 3 | image: "intervalle horaire"}}

Sur l'axe horaire, cliquer entre les heures pour modifier la granularité d'affichage.

L'intervalle sélectionné sera conservé pour la prochaine session de l'utilisateur.

## Fonctionnalités additionnelles

Les fonctionnalités suivantes sont disponibles uniquement dans les offres injixo Advanced WFM et Enterprise WFM.

### Optimisation des pauses

Optimisez les pauses directement depuis Schedules en cliquant sur **Actions de planification** puis {% link_new Optimisation des pauses | features/scheduling/schedules/break-optimization.md %}.

### Planifier des activités supplémentaires

Planifiez les activités supplémentaires directement depuis Schedules en cliquant sur **Actions de planification** puis {% link_new Planifier les Activités supplémentaires | features/scheduling/schedules/schedules-extra-activities.md %}.
