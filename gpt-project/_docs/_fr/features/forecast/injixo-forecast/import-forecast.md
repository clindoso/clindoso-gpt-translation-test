---
title: Importer une prévision
description: Importez une prévision d’une source externe dans injixo Forecast.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

Si vous souhaitez utiliser des données historiques générées par une source externe, telle qu'une application externe ou provenant de vos clients, vous pouvez importer des prévisions externes dans injixo Forecast.

Vous débutez avec injixo Forecast&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Préparer l’importation

### Prérequis

Pour importer une prévision, vous avez besoin au minimum&nbsp;:

- d’une {% link_new intégration | features/acd-integration/cloud/how-integrations-work.md %} permettant d’importer des données,
- d'un workload contenant une file d’{% link_new attente | features/forecast/injixo-forecast/manage-workloads.md | #files-dattente-et-canaux %}.
 
### Créer une file d'attente


Pour créer une file d’attente, vous devez importer des données de contact historiques à l’aide d’une intégration. Les files d’attente sont créées automatiquement par des intégration.

Si vous n’avez pas d’intégration permettant d’importer des données historiques en continu, créez une file d’attente en important un fichier CSV simple&nbsp;:

1. {% link_new Créez une intégration par fichier CSV | features/acd-integration/cloud/add-csv-integration.md | #configurer-une-nouvelle-intégration-par-fichier-csv %}.
   - Ignorez l’installation de Cloud Link.
   - Dans la section **Configuration du schéma CSV**, sélectionnez **Données de contact**.
2. Créez un fichier CSV de données de contact contenant au moins une ligne pour un seul intervalle, par exemple&nbsp;:
   ```
   Queue;Date;Time;IncomingCalls;AnsweredCalls;AHT
ForecastImportQueue;22/02/2022;02:02;2;2;2
   ```
3. {% link_new Importez le fichier CSV manuellement | features/acd-integration/cloud/add-csv-integration.md | #import-manuel-de-fichiers %}.  
   La file d’attente est créée après l’import. Utilisez cette file d’attente pour importer des prévisions dans tous vos workloads.

### Assigner la file d’attente à un workload

Lorsque vous créez un workload, vous devez assigner une file d’attente à ce workload.  Cela fait partie du processus de création des workloads et il s’agit d’un prérequis pour [importer une prévision](#importer-une-prévision). En savoir plus sur la {% link_new création de workloads | features/forecast/injixo-forecast/manage-workloads.md | #créer-un-workload %}.

Vous pouvez importer une prévision dans un workload existant, ou ajouter une file d’attente à un nouveau workload.

### Données d’import nécessaires

Vos données d’import doivent répondre aux exigences suivantes&nbsp;:

| Exigence                          | Détails                                                                                                                            |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Format de date et heure                     | YYYY-MM-DD HH:MM                                                                                                                   |
| Données de volume                          | Nombres entiers (nombres intègres)                                                                                                           |
| Données de TMT                             | Nombres entiers (nombres intègres) ou valeurs décimales (avec un point décimal)                                                                  |
| Format de la ligne d’en-tête                   | `Timestamp;Offered;AHT` ou avec texte personnalisé (par exemple, `Timestamp;Offered_customtext;AHT_customtext`)                                 |
| Caractères de séparation                 | Point-virgule ou virgule (détecté automatiquement)                                                                                                 |
| Taille de fichier maximale                    | 20 Mo<br>Limitez les fichiers à 20&nbsp;000 lignes (recommandé).                                                                         |
| Fuseau horaire                            | Doit correspondre au fuseau horaire de la file d’attente                                                                                             |
| Durée de l’intervalle                      | Doit correspondre à l’intervalle des files d’attente (15, 30 ou 60 minutes)                                                               |


Vous pouvez également {% link_new télécharger une prévision (ou une version de la prévision) | features/forecast/injixo-forecast/download-forecast.md %} au format CSV et l’utiliser comme modèle pour votre propre fichier d’import. La prévision ne lit que les colonnes `Timestamp`, `Offered` et `AHT`. Les autres colonnes, comme `Offered_operational` et `AHT_operational` dans l’exemple ci-dessous, sont ignorées.

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
2020-05-17 16:30;40;180;50;170
```

### Gérer les données manquantes

Il peut y avoir des intervalles sans données dans vos fichiers d’import. Le volume ou le graphique du TMT obtenu affichera les valeurs importées comme zéro (0). Les lignes ou valeurs vides ne seront pas importées.

Si aucune donnée n’est disponible pour un ou plusieurs intervalles, vous pouvez modifier votre fichier CSV de la façon suivante&nbsp;:

- Laissez le volume et le TMT vides&nbsp;:

  ```
  Timestamp;Offered;AHT
2020-05-17 15:00;30;210
2020-05-17 15:15;;
2020-05-17 15:30;40;180
  ```

- Importez des colonnes de zéros&nbsp;:


  ```
  Timestamp;Offered;AHT
2020-05-17 15:00;30;210
2020-05-17 15:15;0;0
2020-05-17 15:30;40;180
  ```

- Omettez la ligne entière&nbsp;:

  ```
  Timestamp;Offered;AHT
2020-05-17 15:00;30;210
2020-05-17 15:30;40;180
  ```

## Importer une prévision


1. Dans _Forecast > Workloads_{:.breadcrumbs}, sélectionnez le workload dans lequel vous souhaitez importer la prévision externe.
2. À partir du menu contextuel {% icon ellipsis_v | icon-only %} en haut à gauche, sélectionnez **Importer les données de prévision**.
3. Cliquez sur _Sélectionner un fichier_{:.doc-button} et sélectionnez le fichier CSV que vous souhaitez importer.
4. Cliquez sur _Importer les données_{:.doc-button}.<br>
   La page se mettra à jour et indiquera si l’import a réussi.
5. Cliquez sur _Fermer_{:.doc-button}.<br>
Rechargez la page pour voir le nouveau graphique pour la période d’import. Les valeurs importées sont affichées sous la forme d’une ligne marron dans les graphiques du volume and du TMT.

   Pour cacher la prévision importée sur le graphique, cliquez sur l’icône Afficher/masquer {% icon eye | icon-only %} dans la légende à côté d’**Import**.
