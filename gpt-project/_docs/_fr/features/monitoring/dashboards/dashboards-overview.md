---
title: Gérer les tableaux de bord
permalink: /fr/dashboards-overview/
promote-service: team-leader-training
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Utilisez les tableaux de bord pour analyser vos données de volume de contacts et d’occupation.
related_articles:
  - overwrite_title: Utiliser les graphiques
    filepath: features/monitoring/dashboards/work-with-charts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/dashboards-examples.md
---

Dans _Analyze > Dashboards_{:.breadcrumbs}, vous pouvez créer et afficher des tableaux de bord pouvant contenir jusqu'à quatre graphiques différents. Chaque graphique peut afficher des diagrammes pour plusieurs séries temporelles et plages de dates. Si vous n'avez pas encore de tableau de bord, la page affiche le mode édition et vous pouvez [créer un tableau de bord](#créer-un-tableau-de-bord).

- Pour afficher un tableau de bord existant, sélectionnez un tableau de bord dans le menu déroulant ou saisissez un nom dans le champ pour filtrer.  
- Pour afficher les valeurs pour un intervalle spécifique, faites passer votre curseur sur un graphique dans le tableau de bord.
- Pour passer en mode plein écran, cliquez sur l’icône Passer en mode plein écran {% icon maximize | icon-only %} en haut à droite.

Vous pouvez également {% link_new basculer entre la vue graphique et la vue tableau | features/monitoring/dashboards/work-with-charts.md | #explorer-les-graphiques %} avec l'icône Visualiser le tableau {% icon table-list | icon-only %} et l'icône Visualiser le graphique {% icon chart-view | icon-only %} en haut à droite de la vue.

##  Créer un tableau de bord

1. Accédez à _Analyze > Dashboards_{:.breadcrumbs}.
2. Depuis l’{% icon ellipsis_v %} sur la droite, sélectionnez **Créer un nouveau tableau de bord**.
3. Remplissez les champs suivants&nbsp;:
  - **Nom**&nbsp;: nom unique pour votre tableau de bord.
  -  **Disposition**&nbsp;: sélectionnez le nombre et la disposition de vos graphiques.
  - **Graphique sans titre**&nbsp;: nom de chaque graphique. Il n’est pas nécessaire d’entrer des noms uniques.
4. Sélectionnez une **plage de dates** pour chaque graphique.
5. (Optionnel) Activez l'option **Utiliser les périodes glissantes** pour décaler la date de début d'un jour chaque jour.
6. Depuis l'arborescence à gauche, faites glisser et déposez les séries temporelles dans les graphiques pour visualiser différentes données clés&nbsp;:
   - **Workloads**&nbsp;: historique, prévision, prévision importée et versions de la prévision. 
   - **Unités opérationnelles**&nbsp;: occupation, besoin en personnel et couverture des journées et activités planifiés, ainsi que les journées demandées dans Me.
   - **Files d’attente WFM**&nbsp;: données des workloads dans les files d'attente WFM que vous avez enregistrées en cliquant sur _Utiliser la prévision_{:.doc-button} dans la page du workload. Cette option est disponible en fonction de votre plan WFM. 

      > Remarque
      >
      > - L’icône Information {% icon circle_exclamation | icon-only %} dans la légende d'un graphique est affichée si vous n'avez pas de données sur une période.
      > - Dans les workloads, vous pouvez voir des chiffres clés spéciaux en fonction de votre intégration. Par exemple, si vos workloads ne contiennent que les files d'attente d'une intégration Genesys Cloud, vous verrez des informations relatives aux appels abandonnés, au délai moyen de réponse et aux appels répondus respectant votre objectif de qualité de service. 

7. Cliquez sur _Enregistrer_{:.doc-button}.<br>Pour revenir au mode d'affichage, cliquez sur _Fermer le mode édition_{:.doc-button}.

### Dupliquer un tableau de bord

Pour créer un nouveau tableau de bord avec les mêmes propriétés générales qu’un tableau de bord existant, suivez ces étapes&nbsp;:
1. Accédez à _Analyze > Dashboards_{:.breadcrumbs}.
2. Depuis le menu déroulant, sélectionnez un tableau de bord.
3. Depuis l’{% icon ellipsis_v %}, sélectionnez Copier le tableau de bord.
4. Modifiez le nom et les détails de configuration, si nécessaire.
5. Cliquez sur _Enregistrer_{:.doc-button}.

### Actualiser automatiquement les tableaux de bord

Vous pouvez actualiser automatiquement le tableau de bord sélectionné. Pour ce faire, sélectionnez un intervalle dans le menu déroulant à droite et cliquez sur _{% icon arrows-rotate | icon-only %}Rafraîchissement auto._{:.doc-button}.<br>Dans le coin inférieur gauche de la page, vous pouvez voir la date et l’heure de la dernière mise à jour du tableau de bord.

## Modifier un tableau de bord

1. Accédez à _Analyze > Dashboards_{:.breadcrumbs}.
2. Depuis le menu déroulant, sélectionnez un tableau de bord.
3. Depuis l’{% icon ellipsis_v %} à droite, sélectionnez **Modifier**.
4. Modifiez le tableau de bord, {% link_new personnalisez les séries temporelles | features/monitoring/dashboards/work-with-charts.md | #personnaliser-les-séries-temporelles %} ou {% link_new supprimez-les | features/monitoring/dashboards/work-with-charts.md | #supprimer-une-série-temporelle %}.
5. Cliquez sur _Enregistrer_{:.doc-button}. Pour revenir au mode d'affichage, cliquez sur _Fermer le mode édition_{:.doc-button}.

## Supprimer un tableau de bord

1. Accédez à _Analyze > Dashboards_{:.breadcrumbs}.
2. Depuis le menu déroulant, sélectionnez un tableau de bord.
3. Depuis l’{% icon ellipsis_v %} à droite, cliquez sur **Modifier**.
4. Cliquez sur _Supprimer_{:.doc-button} en bas à droite.  
5. Dans la fenêtre de confirmation, cliquez sur _Supprimer le tableau de bord_{:.doc-button}.<br> Pour annuler la suppression, cliquez sur _Conserver le tableau de bord_{:.doc-button}.

Si vous supprimez le dernier tableau de bord restant, la page affiche le mode édition jusqu'à ce qu’un nouveau tableau de bord soit créé.
