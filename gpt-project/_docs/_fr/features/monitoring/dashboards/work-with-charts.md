---
title: Utiliser les graphiques
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Apprenez à travailler avec des graphiques d’un tableau de bord.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/dashboards-examples.md
---

Dans _Analyze > Dashboards_{:.breadcrumbs}, vous pouvez travailler avec des graphiques et des séries temporelles pour analyser vos données. Commencez par sélectionner un tableau de bord depuis le menu déroulant en haut.

Vous débutez avec Dashboards&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/monitoring/dashboards/dashboards-overview.md %}.

## Explorer les graphiques

Les actions suivantes sont disponibles dans **Dashboards**&nbsp;:

- Pour modifier la plage de dates pour laquelle vous affichez les données, sélectionnez une plage de dates à l’aide du sélecteur de dates en haut à droite de chaque graphique.
- Pour zoomer sur un graphique, cliquez et faites glisser pour sélectionner votre zone d'intérêt. 
- Pour zoomer en arrière, cliquez sur _Réinitialiser le zoom_{:.doc-button}.
- Pour passer en vue tableau, cliquez sur l'icône Visualiser le tableau {% icon table-list | icon-only %} en haut à droite d'un graphique.
- Pour revenir en vue graphique, cliquez sur l'icône Visualiser le graphique {% icon chart-view | icon-only %}.
- Pour copier des données dans le presse-papiers, cliquez sur l'icône Copier {% icon clone | icon-only %}.

> Remarque
>
> Les informations de date et d'heure sont localisées selon vos paramètres de langue dans injixo. Ceci peut entraîner des problèmes si vous copiez des données d’injixo dans un document Excel ou Google Sheets qui utilise une autre langue.

## Travailler avec les séries temporelles

Les séries temporelles sont des séquences de points de données enregistrés à intervalles réguliers. Les sous-sections suivantes expliquent comment utiliser les séries temporelles dans **Dashboards** pour utiliser, personnaliser et analyser vos données et prendre des décisions éclairées.

### Surligner les séries temporelles

Pour surligner temporairement une série temporelle spécifique dans la vue du graphique, survolez le nom de la série temporelle dans la légende. Toutes les autres séries temporelles s'effaceront en arrière-plan.

### Afficher et masquer les séries temporelles

Masquez et affichez d'autres séries temporelles en cliquant sur l'icône Masquer {% icon eye | icon-only %} ou l'icône Afficher {% icon eye_slash | icon-only %} à côté du nom dans la légende.

### Personnaliser les séries temporelles

1. Accédez à _Analyze > Dashboards_{:.breadcrumbs}.
2. Depuis l'{% icon ellipsis_v %}, cliquez sur **Modifier**.
3. Faites passer votre curseur sur le nom de la série temporelle dans la légende et cliquez sur l'icône Modifier {% icon pencil | icon-only %}.
4. Dans la fenêtre **Personnaliser le graphique**, modifiez les propriétés de la série temporelle&nbsp;:
   - Modifiez le **Nom** affiché dans la légende.
   - Choisissez entre **Étape** ou **Histogramme** (graphique en barres) dans le menu déroulant **Type**. 
   - Sélectionnez une autre **couleur** prédéfinie.
   - Sélectionnez comment les données sont agrégées dans le graphique. Choisissez **Par intervalle** (disponible pour les plages horaires jusqu'à 8 jours) pour afficher les valeurs d'intervalle, ou **Par jour** pour afficher les valeurs quotidiennes.
   - Sélectionnez si vous souhaitez afficher les valeurs de l'axe des ordonnées à **Gauche (par défaut)** ou à **Droite**.
5. Cliquez sur _Sauvegarder_{:.doc-button}.<br>Pour revenir au mode d'affichage, cliquez sur _Fermer le mode édition_{:.doc-button}.

### Supprimer une série temporelle

1. Accédez à _Analyze > Dashboards_{:.breadcrumbs}.
2. Depuis l'{% icon ellipsis_v %}, cliquez sur **Modifier**.
3. Faites passer votre curseur sur le nom de la série temporelle dans la légende et cliquez sur l'icône Modifier {% icon pencil | icon-only %}.
4. Dans la fenêtre **Personnaliser le graphique**, cliquez sur _Supprimer_{:.doc-button}.
5. Cliquez sur _Enregistrer_{:.doc-button}.<br>Pour revenir au mode d'affichage, cliquez sur _Fermer le mode édition_{:.doc-button}.

