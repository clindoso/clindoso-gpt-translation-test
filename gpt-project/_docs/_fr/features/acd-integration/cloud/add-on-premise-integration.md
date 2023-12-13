---
title: Ajouter une intégration on-premise
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Connectez votre base de données on-premise à injixo pour importer des données de contact, de TMT et des statuts agent.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Qu’est-ce qu’une intégration on-premise&nbsp;?

Les intégrations on-premise utilisent {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} pour se connecter à un système dans votre infrastructure locale. Une fois connectée, l’intégration on-premise tentera d’importer les données historiques sur 3&nbsp;ans.

## Ajouter une intégration on-premise

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Sélectionnez votre système externe et cliquez sur _Ajouter une intégration_{:.doc-button}. Si votre système externe existe en différents modèles cliquez sur _Sélectionner le modèle_{:.doc-button} et cliquez sur _Ajouter cette intégration_{:.doc-button}.
3. Complétez les champs requis. Pour identifier facilement votre source de données, entrez un nom unique pour votre intégration.
4. Installez le client {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
5. Cliquez sur _Sauvegarder l’intégration_{:.doc-button}.

{{ 1 | image: 'intégration Genesys Engage', '85%' }}

L’intégration importe désormais les données de contact dans injixo. Le premier import peut prendre un certain temps. Toutes les files d’attente du système connecté seront automatiquement disponibles sur la {% link_new page de configuration des Workloads | features/forecast/injixo-forecast/manage-workloads.md | #créer-un-workload %} dans injixo Forecast.

Si votre intégration supporte l’import de données de statuts agents, vous devez {% link_new mapper | features/acd-integration/cloud/import-agent-status-data.md %} les identifiants utilisateur et les activités externes. L’intégration peut ensuite importer les statuts agent.
