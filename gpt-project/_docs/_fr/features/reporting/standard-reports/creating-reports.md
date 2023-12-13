---
title: Créer des rapports
redirect_from:
  - /fr/reports/
  - /fr/available-reports/
redirect_reason: The first redirect is pretty old. The second is for an article deleted April 2022
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Générer des rapports standard au format HTML ou PDF avec différents paramètres.
promote-service: enhanced-reporting
toc: false
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/reporting/standard-reports/email-reports.md
  - overwrite_title: Add title for untranslated source
    filepath: features/reporting/standard-reports/planning-unit-reports.md
  - overwrite_title: Add title for untranslated source
    filepath: features/reporting/standard-reports/employee-reports.md
---

En lisant cet article, vous apprendrez&nbsp;:
- à créer des rapports selon différents paramètres et filtres,
- comment les rapports affichent les fuseaux horaires.

Les rapports contiennent différentes données, par exemple les plannings sauvegardés dans certaines catégories ou les données de configuration. Pour en savoir plus, lisez les articles {% link_new Rapports sur les unités opérationnelles | features/reporting/standard-reports/planning-unit-reports.md %} et {% link_new Rapports sur les employés | features/reporting/standard-reports/employee-reports.md %}. Vous pouvez créer des rapports au format HTML ou PDF.

 Vous pouvez créer des rapports au format HTML ou PDF.

> Certains rapports sont basés sur les groupes. Ces rapports contiennent des informations uniquement si vous ajoutez un {% link_new groupe | features/administration/selections.md %} à vos employés. 

## Créer des rapports

1. Accédez à *WFM > Supervision > Reports*{:.breadcrumbs}.
2. Sélectionnez une **Date de début** et une **Date de fin**.

3. Utilisez la section **Filtre** pour sélectionner les données affichées dans votre rapport&nbsp;:

    - **Filtre standard**&nbsp;: sélectionnez une **Unité opérationnelle**, un **Contrat** ou un **Groupe** pour affiner la liste d’employés. Pour sélectionner plusieurs éléments, appuyez sur la touche **CTRL** ou **Shift** lors de la sélection.

        {{ 1 | image: 'Standard Filter', '90%' }}

    - **Filtre avancé**&nbsp;: sélectionnez un nouveau {% link_new filtre avancé | features/administration/employee-filter.md %} pour créer une liste spécifique d’employés, par exemple basée sur les compétences. Pour créer un nouveau filtre, cliquez sur **Éditeur de filtres**.

      <br>Cochez la case **Période du rapport semblable à celle du filtre** pour remplacer les dates de début et de fin sélectionnées dans l’interface utilisateur.  

      {{ 2 | image: 'Employee Filter', '60%' }}  

      Les filtres avancés ne sont pas disponibles dans injixo Essential WFM.

4. Cliquez sur *Appliquer*{:.doc-button}.

5. (Facultatif) Dans la section **Employés**, sélectionnez des **Employés** individuels.

    {{ 3 | image: 'Employees section', '60%' }}

6. Dans la section **Paramètres**, vous pouvez&nbsp;:
    - sélectionner la **catégorie** dont vous souhaitez utiliser les données, 
    - définir le format **format** de sortie (PDF ou CSV),
    - {% link_new envoyer des rapports par e-mail | features/reporting/standard-reports/email-reports.md %} à certains utilisateurs,
    - rendre anonymes les noms et les matricules des employés.

    {{ 4 | image: 'Report parameters', '30%' }}

7. Dans la section **Rapports de données des unités opérationnelles** ou **Rapports de données des employés** à droite, cliquez sur le nom d’un rapport.

    {{ 5 | image: 'List of reports with sections', '50%' }}

    <br>
    Les icônes représentant un document à côté du nom de chaque rapport indiquent la période pour laquelle vous pouvez créer un rapport&nbsp;:
    - _![icône de rapport page simple](/assets/img/common/report-icon-single-file.png)_{:.doc-button-icon}&nbsp;: période d’un mois maximum,
    - _![icône de rapport pages multiples](/assets/img/common/report-icon-multiple-files.png)_{:.doc-button-icon}&nbsp;: période d’un an maximum. 

Une fenêtre de traitement de la tâche s’ouvre. Le rapport désiré est créé et affiché.

Vous pouvez créer d’autres rapports avec les mêmes paramètres. Si vous modifiez un filtre ou une date, cliquez sur *Appliquer*{:.doc-button}.

## Fuseaux horaires dans les rapports

Les heures affichées dans un rapport sont relatives au fuseau horaire de l’unité opérationnelle. L’en-tête du rapport indique l’écart de temps entre le fuseau horaire de l’unité opérationnelle et l’UTC, ainsi qu’entre le fuseau horaire de l’unité opérationnelle et celui de l’utilisateur local.

Exemple&nbsp;: un employé commence sa journée à 08:30 à New York. Le rapport utilise l’heure locale de Manchester (Royaume-Uni), où se trouve l’unité opérationnelle. Le décalage horaire est de +05:00. L’employé devra déduire ce décalage horaire de l’heure affichée pour déterminer l’heure de début de la journée. La journée commence donc à 03:30 à New York heure locale.
