---
title: Ajouter une intégration Mitel
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Apprenez comment connecter votre CRM Mitel à injixo pour importer des données.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Une intégration Mitel est une intégration on-premise permettant d’importer les historiques d’appels, des e-mails, des chats et des médias sociaux, ainsi que les données de statut agent.

Cette intégration utilise {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Ajouter une intégration Mitel

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Mitel**, cliquez sur _Ajouter cette intégration_{:.doc-button}.

## Configurer votre nouvelle intégration Mitel

1. Entrez un nom unique permettant d’identifier la source de données.
2. Installez et connectez {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Dans la section **Paramètres régionaux**, sélectionnez le **fuseau horaire de l’ACD**.
4. Dans la section **Identifiants de la base de données**, configurez votre intégration&nbsp;:
 - Saisissez l’hôte et le port de votre base de données.
 - Saisissez le nom d’utilisateur et le mot de passe de votre base de données.
5. Si vous souhaitez importer les données de statut agent, cochez la case **Importer les statuts agents** dans la section **Configuration**.<br>Remarque&nbsp;: pour importer correctement les données de statut agent, vous devez d’abord {% link_new mapper les identifiants et les activités externes | features/acd-integration/cloud/import-agent-status-data.md %}.
6. Cliquez sur _Sauvegarder l’intégration_{:.doc-button}.

L’intégration commence à importer les données dans injixo. 

## Modifier une intégration Mitel

Si les détails de l’intégration changent, comme par exemple les identifiants du serveur de base de données, vous pouvez modifier et mettre à jour la configuration de votre intégration. L’import de données continuera en utilisant la configuration mise à jour.
