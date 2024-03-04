---
title: Ajouter une intégration Genesys Cloud
description: Découvrez comment connecter votre CRM Genesys Cloud à injixo pour importer des données.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Une intégration Genesys Cloud est une intégration cloud permettant d’importer l’historique des appels, des e-mails et des discussions, ainsi que les statuts agent et les données d’adhérence temps réel.

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Ajouter une intégration Genesys Cloud

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Genesys**, cliquez sur _Sélectionner le modèle_{:.doc-button}.
4. Dans la section **Genesys Cloud**, cliquez sur _Ajouter cette intégration_{:.doc-button}.

## Configurer votre intégration Genesys Cloud

1. Entrez un nom unique permettant d’identifier la source de données.
2. Dans la section **Identifiants API**, copiez et collez votre clé API Genesys Cloud et votre secret API.
3. Dans la section **Configuration**, sélectionnez la région de votre compte.
4. (Facultatif) Cochez la case **Importer les statuts détaillés des agents on-queue**.<br>Le statut agent on-queue inclut plusieurs statuts&nbsp;; par exemple, en communication, en interaction, inactif, ne répond pas. Lors de l’import des statuts agent, injixo fait la distinction entre les statuts individuels regroupés sous «&nbsp;on-queue&nbsp;».
5. Cliquez sur _Sauvegarder l’intégration_{:.doc-button}.

## Foire aux questions

| Question                            | Réponse                                                                                                                                           |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------- |
| L'intégration importe des données pour les appels abandonnés, le délai moyen de réponse et les appels répondus respectant l’objectif de qualité de service. Pourquoi ces données ne s’affichent-elles pas dans Dashboards&nbsp;? | Vous pouvez afficher ces données dans Dashboards si vous ajoutez exclusivement des files d'attente de votre intégration Genesys Cloud lorsque vous configurez un workload dans Forecast. Vous ne pouvez pas afficher ces données si des files d'attente d'autres intégrations sont incluses.
