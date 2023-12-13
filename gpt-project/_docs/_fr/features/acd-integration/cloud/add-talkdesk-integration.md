---
title: Ajouter une intégration Talkdesk
description: Découvrez comment connecter votre ACD Talkdesk à injixo pour importer des données.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

Une intégration Talkdesk est une intégration cloud permettant d’importer l’historique des appels et les données de statut agent.

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Ajouter une intégration Talkdesk

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.  
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Talkdesk**, cliquez sur _Ajouter cette intégration_{:.doc-button}.
4. Entrez un nom unique permettant d’identifier la source de données.
5. Dans la section **Identifiants de l’utilisateur**, remplissez les champs avec les informations spécifiques à Talkdesk.

   - Saisissez le nom de votre compte Talkdesk.
   - Saisissez l’ID et le Secret d’un client Talkdesk OAuth.

     > Pour obtenir l’ID et le Secret du client, [créez un nouveau client OAuth](https://docs.talkdesk.com/docs/creating-a-new-oauth-client) dans Talkdesk.
     >
     > Vous pouvez également utiliser un client OAuth existant avec la configuration ci-dessous&nbsp;:
     >
     > - Type d’autorisation&nbsp;: client-credentials
     > - Portée&nbsp;: data-reports:read et data-reports:write

6. Dans la section **Configuration**, sélectionnez la région de votre compte.

7. Cliquez sur _Sauvegarder l’intégration_{:.doc-button}.  
   L’intégration testera la connexion et signalera les éventuels problèmes.  
   Une fois la vérification validée, l’intégration commencera à importer les données dans injixo.

<!-- ## Talkdesk Data in injixo -->

## Et ensuite&nbsp;?

Une fois que les données d’appel ont été importées dans les files d’attente, vous pouvez créer votre premier Workload. Pour en savoir plus sur la configuration des statuts agents, consultez les articles connexes.
