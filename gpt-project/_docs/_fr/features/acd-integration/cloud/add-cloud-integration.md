---
title: Ajouter une intégration Cloud
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: false
description: Connecter votre ACD Cloud à injixo pour importer des données.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-five9-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Qu’est-ce qu’une intégration Cloud&nbsp;?

Les intégrations Cloud récupèrent des données directement depuis un système Cloud. injixo supporte plusieurs intégrations Cloud.

## Ajouter une intégration Cloud

1. Accédez à *Account > Intégrations*{:.breadcrumbs}. La page affiche toutes les intégrations disponibles.
2. Cliquez sur *Ajouter cette intégration*{:.doc-button} et saisissez les informations requises. Dans cet exemple, nous configurons l’intégration Five9, mais le procédé pour configurer les autres intégrations Cloud est similaire.
3. Sélectionnez un nom unique pour votre intégration. Le nom doit refléter la source de données.
4. Saisissez le **nom d’utilisateur** et le **mot de passe** pour un utilisateur disposant de droits administrateur dans votre compte Five9.
5. Configurez les détails spécifiques à l’intégration (par exemple, la région de votre compte Five9 et le regroupement des files d’attente).
6. Cliquez sur _Sauvegarder l’intégration_{:.doc-button} pour créer l’intégration avec les informations fournies.

{{ 1 | image: 'Intégration Five9', '80%' }}

La nouvelle intégration importe désormais les données dans injixo. Le premier import peut prendre jusqu’à 15&nbsp;minutes. Toutes les files d’attente du système connecté seront automatiquement disponibles pour le mappage sur la {% link_new page de configuration des Workloads | features/forecast/injixo-forecast/manage-workloads.md | #créer-un-workload %} dans injixo Forecast.

Si votre intégration supporte l’import de données de statuts agents, vous devez {% link_new mapper les identifiants utilisateur et les activités externes | features/acd-integration/cloud/import-agent-status-data.md %} avant de pouvoir importer les statuts agents.
