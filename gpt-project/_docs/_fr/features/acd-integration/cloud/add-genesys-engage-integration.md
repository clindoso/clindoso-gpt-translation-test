---
title: Ajouter une intégration Genesys Engage
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Découvrez comment connecter votre CMS Genesys Engage à injixo pour importer les données.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Une intégration Genesys Engage est une intégration on-premise permettant d’importer l’historique des appels et les données de statut agent.

Cette intégration utilise {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Ajouter une intégration Genesys Engage

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Genesys**, cliquez sur _Sélectionner le modèle_{:.doc-button}.
4. Dans la section **Genesys Engage**, cliquez sur _Ajouter cette intégration_{:.doc-button}.

## Configurer votre nouvelle intégration Genesys Engage

1. Entrez un nom unique permettant d’identifier la source de données.
2. Installez et connectez {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Dans la section **Identifiants de la base de données**, configurez votre intégration&nbsp;:
 - Sélectionnez l’adaptateur de votre base de données.
 - Entrez l’hôte et le port de votre base de données.
 - Entrez le nom d’utilisateur et le mot de passe de votre base de données.
 - Entrez le nom de la base de données ETL.
 - Entrez le nom de la base de données de configuration.
4. Si vous souhaitez importer les données de statut agent, cochez la case **Importer les données agents** dans la section **Configuration**.<br>
Remarque&nbsp;: pour importer correctement les données de statuts agent, vous devez d’abord {% link_new mapper les identifiants et les activités externes | features/acd-integration/cloud/import-agent-status-data.md | #mapper-les-identifiants-utilisateur-externes-aux-employés-dans-injixo %}.
5. Cliquez sur _Sauvegarder l’intégration_{:.doc-button}.

L’intégration commence à importer les données dans injixo. 

## Modifier une intégration Genesys Engage

Si les détails de l’intégration changent, par exemple les identifiants du serveur de base de données, vous pouvez modifier et mettre à jour la configuration de votre intégration. L’import de données continuera en utilisant la configuration mise à jour.
