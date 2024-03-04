---
title: Modifier ou supprimer le besoin en personnel
toc: false
product_label:
  - advanced
  - enterprise
description: Découvrez comment modifier ou supprimer les valeurs du besoin en personnel calculées par injixo.
archive_ref: 20210819-en-employee-requirement
related_articles:
  - overwrite_title: Qu'est-ce que le Centre de planification&nbsp;?
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/calculate-a-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/calculate-staff-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
redirect_from:
  - /fr/employee-requirement/
redirect_reason: Updated filename on 28 February 2024
---

Le besoin en personnel définit le nombre d’employés dont vous avez besoin pour une activité à une heure spécifique. Vous avez besoin d’un besoin en personnel pour créer des plannings à l’aide de la fonctionnalité **Optimiser le planning** ou pour les optimiser à l’aide des fonctionnalités **Optimiser les activités** ou **Optimiser les pauses**.

La génération du besoin en personnel est la dernière étape du processus de prévision. Dans injixo Forecast, vous pouvez utiliser le besoin automatiquement généré, ou appliquer une méthode spécifique de calcul du besoin en personnel. Avant de créer un planning, assurez-vous que le besoin en personnel a été généré pour toutes les activités concernées.

## Voir et modifier le besoin en personnel

Dans injixo, vous pouvez voir le besoin en personnel dans les fonctionnalités suivantes&nbsp;:

- _Forecast_{:.menu-item}
- _Analyze > Dashboards_{:.breadcrumbs}
- _Plan > Schedules_{:.breadcrumbs}
- _Plan > Centre de planification_{:.breadcrumbs} 

Le tableau suivant inclut des détails concernant les options disponibles dans chaque fonctionnalité&nbsp;:

<style>
table {
   margin-left: 0px;
}
</style>

| Fonctionnalité  | Voir | Modifier | Supprimer |
| ------ |--------| -------- |-------- |
| _Forecast_{:.menu-item} | Oui | Oui | Oui |
| _Analyze > Dashboards_{:.breadcrumbs} | Oui | Non | Non |
| _Plan > Schedules_{:.breadcrumbs} | Oui | Non | Non |
| _Plan > Centre de planification_{:.breadcrumbs} | Oui | Oui | Non |

### Modifier le besoin en personnel dans le Centre de planification

1. Accédez à _Plan > Centre de planification_{:.breadcrumbs}.
2. Au bas du panneau, cliquez sur l’onglet **Activités - Besoin** ou **Récapitulatif de l’activité**.<br>
   > Message Données inexistantes dans une cellule
   >
   > Si une cellule du bas du tableau affiche le message Données inexistantes, sélectionnez **Planning** ou **État actuel** depuis le menu déroulant **Catégories** en haut à droite.

3. Pour développer une unité opérationnelle, cliquez sur l’icône Développer {% icon plus | icon-only %} à gauche de chaque tableau.
4. Effectuez un clic droit dans une cellule et sélectionnez **Modifier le besoin en personnel...**.
5. Dans la fenêtre **Modifier le besoin en personnel...**, cliquez sur une cellule et entrez la nouvelle valeur.<br>
  Vous ne pouvez pas modifier les cellule surlignées en bleu, car elles représentent les activités supprimées toujours assignées à l’unité opérationnelle.<br>
  
6. (Facultatif) Pour modifier plusieurs cellules à la fois, copiez une ligne de valeurs depuis une feuille de calcul. Cliquez sur une cellule et faites glisser le curseur vers la droite. Appuyez sur Ctrl+V pour coller les valeurs.<br>
7.  Cliquez sur _OK_{:.doc-button}.

### Modifier le besoin en personnel dans Forecast

Pour modifier manuellement le besoin en personnel, vous pouvez appliquer le script de besoin constant dans _Forecast_{:.breadcrumbs}. La procédure suivante explique comment configurer le script pour ce scénario précis. Pour en savoir plus sur les options de configuration, consultez l’article {% link_new Besoin constant | features/forecast/requirement-scripts/requirement-constant.md %}.

1. Accédez à _Forecast > Calcul du besoin_{:.breadcrumbs}.
2. Dans la section **Besoin constant**, cliquez sur _Ouvrir_{:.doc-button}.<br>
3. Dans la fenêtre de configuration du script, configurez les paramètres suivants&nbsp;:
   - Dans la section **Date**&nbsp;:
     - **Start Date**
     - **Number of Days**&nbsp;: saisissez le nombre de jours consécutifs après la date de début auquel s’applique le besoin en personnel modifié.
     - **Consider Each Day of the Week**&nbsp;: sélectionnez **No**.
     - **Add to Existing Requirement**&nbsp;: laissez la case vide.
     - **Number Of Days With Timespans**&nbsp;: pour modifier le besoin en personnel pour tous les jours sur une plage de dates, sélectionnez 1.
     - **Timespans Per Day**&nbsp;: sélectionnez le nombre de périodes par jour pour lesquelles vous souhaitez modifier le besoin en personnel (par exemple, 1 si vous souhaitez modifier les besoins en personnel pour toute la journée, mais 3 si vous souhaitez définir un besoin en personnel différent pour le matin, l'après-midi et le soir).
     - **Number of Activities**&nbsp;: sélectionnez le nombre d’activités pour lesquelles vous souhaitez modifier le besoin en personnel.
   - Dans la section **Data**&nbsp;:
     - **Planning unit** et **Activity**&nbsp;: sélectionnez les données pertinentes pour chaque activité dont vous souhaitez modifier le besoin en personnel.
     - **Agents**&nbsp;: saisissez le nombre à utiliser comme besoin en personnel.
     - **Start** et **End**&nbsp;: définissez les périodes pour lesquelles vous souhaitez modifier le besoin en personnel.
4. Cliquez sur _OK_{:.doc-button}.

## Supprimer le besoin en personnel

Il n’existe pas d’option permettant de supprimer directement le besoin en personnel dans injixo. Vous pouvez modifier le besoin en personnel et le définir sur 0, ce qui a le même effet que de le supprimer.

 Il existe deux possibilités pour définir le besoin en personnel sur 0&nbsp;:
 - Suivez les étapes pour [modifier le besoin en personnel dans le Centre de planification](#modifier-le-besoin-en-personnel-dans-le-centre-de-planification) et saisissez ou copiez 0 dans les cellules concernées.
 
 - Suivez les étapes pour [modifier le besoin en personnel dans Forecast](#modifier-le-besoin-en-personnel-dans-forecast) et saisissez 0 dans le champ **Agents**.

L’image ci-dessous illustre la configuration du script de besoin constant pour supprimer le besoin en personnel dans Forecast pour un jour ouvrable entier (ici&nbsp;: Day 1)&nbsp;:

{{ 3 | image: 'Exemple de script de besoin constant avec une activité de 00:00 à 00:00 et 0 besoin en personnel', '80%' }}
