---
title: Vue d'ensemble et fonctionnalités
promote-service: team-leader-training
redirect_from:
  - /fr/dashboards-vue-ensemble/
redirect_reason: Updated filename on 21 April 2022
related_articles:
  - filepath: features/monitoring/dashboards/work-with-charts.md
  - filepath: features/monitoring/dashboards/dashboards-examples.md
---

Dashboards vous permet de consulter en détail les données relatives à vos Workloads et vos Unités opérationnelles à l'aide de tableaux de bord intra et interjournalier.

Pour accéder à Dashboards, cliquer sur Analyze dans la barre de navigation supérieure. Tous les utilisateurs d'injixo, à l’exception des agents, ont accès à ce menu. Vous pouvez créer de nombreux tableaux de bords et les enregistrer pour analyser les données ultérieurement. Chaque tableau de bord peut contenir jusqu’à quatre graphiques différents, chaque graphique pouvant afficher plusieurs type de données sur des périodes différentes.

> Qu’est-ce qu’une série de données ?
>
> Une série de données est un ensemble de valeurs associées à une date et une heure. Par exemple, si une file d’attente a reçu 15 appels de 9 h à 9 h 15 et 20 appels de 9 h 15 à 9 h 30, cet ensemble de données (le nombre d’appels et la période pendant laquelle ils sont arrivés) constitue une série de données.
>
> Notez que l’expression “série de données” peut désigner une ou plusieurs séries de données.

## Fonctionnalités générales

Lorsque vous ouvrez Dashboards, le système affiche le dernier tableau de bord enregistré et consulté. Si vous n’avez sauvegardé aucun tableau de bord, vous pouvez commencer à en créer un.

{{ 1 | image: 'Dashboard erstellen', '75%' }}

Pour changer de tableau de bord, ouvrez la liste déroulante. Vous pouvez faire une recherche par nom ou parcourir la liste des tableaux de bord disponibles.

Pour une vue plus détaillée, vous pouvez passer en mode plein écran en cliquant sur l’icône _![Fullscreenmode](/assets/img/common/dashboards/fullscreen.png)_{:.doc-button-icon} dans la partie supérieure droite de l'écran.

## Créer, modifier et supprimer des tableaux de bords

Pour créer un nouveau tableau de bord ou modifier un existant, cliquer sur l'icône _![Context menu](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon} à côté du nom du tableau de bord actuel et sélectionner l’option souhaitée. Attention les Workloads Smart en statut Test ne sont pas disponibles dans Dashboards.

{{ 2 | image: "Edit Mode", '75%' }}

Les étapes suivantes vous guideront dans la création ou la modification d'un tableau de bord :

- Choisissez un nom unique pour votre tableau de bord.
- Sélectionnez le nombre de graphiques souhaités en cliquant sur l’une des mises en page proposées.
- Donnez un titre à chaque graphique.
- Sélectionnez une plage de dates pour chaque graphique. La période sélectionnée s’affichera à la prochaine utilisation du tableau de bord. Vous pouvez également activer le mode période glissante.
- L’arborescence située à gauche de la zone de graphique permet de glisser-déposer une ou plusieurs séries de données pour chaque graphique. Si une série de données contient des données pour la période sélectionnée, le graphique se créé automatiquement. S’il n’y a pas de données disponibles, une icône d’avertissement _![Warning that there is no data](/assets/img/common/dashboards/no-data.png)_{:.doc-button-icon} s'affiche.
- Chaque série de données peut être personnalisée en cliquant sur l’icône (crayon) dans la légende. Vous pouvez :

  - Modifier le nom (affiché dans la légende)
  - Sélectionner le type de graphe (diagramme ou histogramme)
  - Sélectionner une couleur
  - Choisir l'agrégation des données par intervalle ou par jour. L’option intervalle n’est disponible que pour une période maximale de 8 jours.
  - Afficher les séries de données sur l’axe de droite.
  - Sauvegarder vos modifications
  - Supprimer la série de données du graphique

    {{ 3 | image: "Customize a Graph", '50%' }}

- Une fois la sauvegarde effectuée, les modifications sont visibles pour tous les utilisateurs de Dashboards.

Il est possible de copier un tableau de bord existant en cliquant sur l'icône _![Context menu](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon} puis "Copier le tableau de bord".

### Actions sur les graphiques

#### Sélectionner une période

Chaque graphique peut afficher des périodes différentes. Toutes les séries de données d'un graphique sont affichées pour la période spécifiée. La période sélectionnée peut être modifiée à l’aide du champ "Date" situé en haut à droite de chaque graphique. Pour n'afficher qu'un seul jour, sélectionnez le même jour pour les dates de début et de fin.

Vous pouvez activer le mode période glissante si vous le souhaitez. Dans ce mode, la plage de dates sélectionnée change automatiquement tous les jours. De cette façon, vous pouvez configurer un graphique qui présente des données sur les 7 derniers jours par exemple.

#### Mettre en évidence une série de données

Vous pouvez mettre en évidence une série temporelle en passant le curseur sur son nom dans la légende située sous le graphique.

#### Afficher et masquer des séries de données

Si vous souhaitez vous concentrer sur une série de données spécifique, vous pouvez masquer les autres séries de données du graphique en cliquant sur l’icône _![Show and hide graphs](/assets/img/common/dashboards/view.png)_{:.doc-button-icon} à côté de leur nom dans la légende. Cliquer sur cette icône pour les afficher à nouveau.

#### Afficher les horaires d'ouverture

Lorsque vous passez le curseur sur le nom de la série de données dans la légende, vous affichez les heures d'ouverture des Unités opérationnelles et des Workloads. La zone en dehors des heures d'ouverture est hachurée. Vous pouvez également épingler ces informations en cliquant sur _![Store clock](/assets/img/common/dashboards/store-clock.png)_{:.doc-button-icon}. Si aucune heure d'ouverture n'a été paramétrée, cette icône est grisée.

#### Zoom sur un graphique

Avec la fonction zoom, vous pouvez visualiser votre graphique plus en détail. Il vous suffit de sélectionner une zone sur votre graphique. Utilisez le bouton "Réinitialiser le zoom" pour revenir à la vue d'origine.

#### Données numériques

Vous pouvez passer de la vue graphique à la vue tabulaire avec l’icône _![Table view](/assets/img/common/dashboards/table.png)_{:.doc-button-icon} en haut à droite de chaque graphique.

#### Copier les données

Vous pouvez copier dans le presse-papier les données numériques des séries de données en cliquant sur l’icône _![Copy a table](/assets/img/common/dashboards/copy.png)_{:.doc-button-icon}.
