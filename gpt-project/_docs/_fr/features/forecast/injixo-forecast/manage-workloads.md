---
title: Création de workloads
redirect_from:
  - /fr/gestion-workloads/
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Créez des workloads représentant votre historique et vos prévisions de volume de contact et de TMT. Découvrez les différents types de workloads.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/forecast-activate-business-hours.md
---

Pour créer, modifier ou supprimer des workloads, accédez à _Forecast_{:.breadcrumbs}.

Les workloads permettent de mapper les canaux d’entrée de votre système externe, qui importe les détails des interactions avec vos clients. injixo Forecast calculera une prévision pour le workload en fonction des données de contact importées et stockées dans les files d’attente. Les événements configurables, les jours fériés ou les heures d’ouverture influencent le résultat de la prévision. Vous pouvez également {% link_new importer votre prévision | features/forecast/injixo-forecast/import-forecast.md %} dans des workloads.

Les workloads permettent de configurer le calcul du besoin en personnel. Le besoin en personnel est nécessaire à la planification.

Vous débutez avec injixo Forecast&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Prérequis

- {% link_new Ajoutez une intégration | features/acd-integration/cloud/how-integrations-work.md %} spécifique à votre système externe ou par fichier CSV et importez des données historiques pour au moins une file d’attente.
- Importez les contacts entrants, le temps moyen de traitement (TMT) et les contacts traités. Les workloads contenant plusieurs files d'attente auront besoin des contacts traités pour afficher le TMT et calculer les moyennes pondérées.

injixo crée des files d’attente en utilisant les données importées par une intégration. L’intervalle d’importation des données détermine l’intervalle des files d’attente créées à partir de ces données. Vous pouvez uniquement ajouter des files d’attente avec le même intervalle à un workload.

## Files d’attente et canaux

Les données de contact importées par une intégration sont stockées dans des files d’attente. Ces files d’attente sont toujours associées à un canal. Lorsque vous [créez des workloads](#créer-un-workload), vous pouvez filtrer les files d’attente par canal pour les assigner au workload. Les intégrations spécifiques à un système externe définissent automatiquement le canal pour les files d’attente. Toutes les intégrations ne prennent pas en charge tous les canaux.
Pour une intégration par fichier CSV, vous devez définir le canal manuellement. Vous pouvez ajouter un canal par colonne ou sélectionner un canal pour l’ensemble du fichier lorsque vous {% link_new mappez les colonnes | features/acd-integration/cloud/add-csv-integration.md | #mapping-des-colonnes %} d'un fichier CSV.  

Les intégrations prennent en charge les canaux suivants&nbsp;:

- Appels
- Chats
- E-mails
- Cas
- Documents
- Réseaux sociaux

injixo Forecast regroupe les files d’attente par canal. Vous pouvez uniquement ajouter des files d’attente avec le même canal à un workload.

<!-- anchor for intercom forecast tour -->

## Créer un workload

Nous vous recommandons de créer un workload pour chaque activité que vous souhaitez planifier à l'aide du besoin en personnel. Les multi-activités nécessitent un workload pour l'activité principale et un workload pour chaque sous-activité.

1. Cliquez sur _Nouveau workload_{:.doc-button} en haut de la liste.
2. Saisissez les informations générales pour votre workload&nbsp;:
   - **Nom**&nbsp;: nom unique pour identifier votre workload.
   - **Fuseau horaire**&nbsp;: le fuseau horaire du workload ne peut pas être modifié ultérieurement.

     > Remarque
     >
     > - Pour enregistrer le besoin en personnel pour une unité opérationnelle, le fuseau horaire du workload doit correspondre au fuseau horaire de l’unité opérationnelle.
     > - Si vous sélectionnez un fuseau horaire pour votre workload différent de celui du fuseau horaire de l'intégration utilisée pour importer les données, les données importées seront affichées avec un décalage horaire dans le workload. Par exemple, si une intégration par fichier CSV est définie sur l’heure UTC et que votre workload est défini sur l’heure CEST (UTC +2 heures), les données importées marquées à 08:00 seront affichées à 10:00 dans le workload.

   - (Facultatif) **Calendrier des jours fériés**&nbsp;: inclut les jours fériés pouvant affecter votre prévision.
   - (Facultatif) Sélectionnez une **unité opérationnelle** et une **activité**&nbsp;: nécessaire pour {% link_new activer les heures d'ouverture | features/forecast/injixo-forecast/forecast-activate-business-hours.md %} dans la section **Horaires d'ouverture**.

3. (injixo Classic uniquement) Sélectionnez une option dans la section **Modèle de prévision**&nbsp;:

   - **Mode Live** (payant)&nbsp;: facturé par mois. Il n’est pas possible de revenir au mode Test.
   - **Mode Test** (gratuit)&nbsp;: vous pouvez uniquement consulter les prévisions et ne pouvez pas transférer le besoin en personnel pour la planification.

4. Dans la section **Assigner des files d'attente**, sélectionnez les files d’attente pour votre workload.

   Pour limiter les files d’attente affichées&nbsp;:

   - Filtrez les files d’attente par canal (Appels, Chats, etc.).
   - Utilisez les cases à cocher pour afficher les files d’attente sélectionnées, non sélectionnées ou inactives. Les files d'attente inactives sont celles importées par des intégrations qui ont été supprimées.
   - Utilisez le champ de recherche au-dessus du tableau. Vous pouvez rechercher par nom de file d’attente, d’intégration ou de workload.
  Remarque&nbsp;: si l’intervalle ou le canal d’une file d’attente ne correspond pas à ceux des files d’attente sélectionnées, toutes les files d’attente non correspondantes seront grisées.

5. Cliquez sur _Créer_{:.doc-button}.

   La page affiche les données historiques et une première version de la prévision.  
   Lorsque le calcul est terminé, actualisez la page pour voir la version finale de la prévision.  
   Le nouveau workload est affiché dans la liste des workloads.

Si vous utilisez injixo Essential, vous pouvez créer des workloads Basic. Les workloads Basic nécessitent au moins deux semaines de données historiques. Les workloads Basic ne prennent pas en charge les heures d’ouverture.

Si vous utilisez injixo Advanced ou Enterprise WFM, vous pouvez créer des workloads Smart. Les workloads Smart génèrent une prévision basée sur un seul jour de données historiques. Les workloads Smart prennent en charge les heures d’ouverture.

Si vous utilisez injixo Classic, vous devez également sélectionner le modèle de prévision (Smart ou Basic) pour chaque workload. Pour les workloads Smart, vous pouvez choisir entre le mode Live et le mode Test. Le mode Test est gratuit mais vous permet uniquement de voir la prévision et vous ne pouvez pas transférer le besoin en personnel à des fins de planification. Le mode Live offre toutes les fonctionnalités et est facturé mensuellement. Les workloads Smart en mode Live ne peuvent pas être rétablis en mode Test.

<!-- hidden: feature not live yet -->
<!-- ## Create workloads without historical data

You only need an integration and historical data import if you want injixo to create forecasts. To add forecast data by {% link_new importing a forecast | features/forecast/injixo-forecast/import-forecast.md %} that has been generated externally or to {% link_new create constant staff requirements | features/forecast/requirement-scripts/requirement-constant.md %}, you can create a workload using the tab *Forecast Import*:

1. Go to **Forecast**{:.breadcrumbs}.
2. Click _Create Workload_{:.doc-button} in the upper right corner of the forecast page.
3. In the *Basic configuration* section, enter a **Name** for your new workload.
4. Select the **Time zone** to display data. Note: The set time zone must match the planning unit to save staff requirements.
5. (Optional) Select the **Holiday region** to acknowledge all public holidays that affect your forecast for the year.
6. Select the **Planning unit** and the **Activity**. Note: You must select an option to calculate staff requirements.
    {{ 4 | image: 'Import Workload basic configuration section' }}
7. Click the tab **Forecast import**.
8. Select your **Interval length** and the **Channel** for the data import. Both must correspond with your import file.
    {{ 5 | image: 'Import Workload parameters' }}
9. Click *Create workload*{:.doc-button}. -->

## Modifier des workloads

1. Sélectionnez un workload dans la liste des workloads ou saisissez le nom du workload dans le champ de recherche.
2. Pour modifier les détails du workload, cliquez sur l'{% icon pencil %}  
   Vous pouvez ajouter ou supprimer des files d'attente sans réimporter les données.
3. Cliquez sur _Sauvegarder_{:.doc-button}.
   La nouvelle configuration peut mettre à jour la prévision.

## Supprimer des workloads

1. Cliquez sur l'{% icon trash %} à côté du workload dans la liste.
2. Dans la fenêtre de confirmation, cliquez sur _Supprimer le Workload_{:.doc-button}.  
    injixo conserve les données historiques associées. Pour réutiliser les données, ajoutez la file d’attente ou les files d’attente à un autre workload.
