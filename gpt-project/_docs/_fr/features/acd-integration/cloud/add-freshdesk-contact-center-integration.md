---
title: Ajouter une intégration Freshdesk Contact Center
description: Découvrez comment connecter votre CRM Freshdesk Contact Center à injixo pour importer des données.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Une intégration Freshdesk Contact Center est une intégration cloud permettant d’importer l’historique des appels, les statuts agent et les données d’adhérence en temps réel.

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Ajouter une intégration Freshdesk Contact Center 

Pour ajouter une nouvelle intégration Freshdesk Contact Center dans injixo, vous devez disposer d’un compte Freshdesk Contact Center Pro ou Enterprise.

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Freshworks**, cliquez sur _Sélectionner le modèle_{:.doc-button}.
4. Dans la section **Freshdesk Contact Center**, cliquez sur _Ajouter cette intégration_{:.doc-button}.

## Configurer votre intégration Freshdesk Contact Center

1. Entrez un nom unique permettant d’identifier la source de données.
2. Dans la section **Identifiants**, entrez votre nom de domaine Freshdesk Contact Center complet, en incluant le sous-domaine, par exemple exemple.freshcaller.com.
3. Accédez à Freshdesk Contact Center et copiez une clé API valide d’un utilisateur ayant le rôle Account Administrator.
4. Retournez à injixo et collez la clé API dans le champ **Clé API**.
5. Sélectionnez la [stratégie de regroupement pour les files d’attente importées](#noms-de-files-dattente-par-stratégie-de-regroupement).
6. Cliquez sur _Sauvegarder l’intégration_{:.doc-button}. 

Après avoir sauvegardé votre configuration, vous pouvez accéder à la section **Installer l’application injixo** sur la page.

## Installer l’application injixo

1. Dans la section **Installer l’application injixo**, générez et copiez la **clé API injixo**.
2. Installez l’application injixo requise dans votre compte Freshdesk dans [Freshworks marketplace](https://www.freshworks.com/apps/freshcaller/injixo_1/).
3. Sur la page d’installation de l’application injixo, collez la clé API copiée.
4. Pour importer des données en temps réel, cochez la case **Export real-time agent status data** dans la page d’installation de l’application injixo de Freshworks marketplace.

## Noms de files d’attente par stratégie de regroupement

Lors de l’import des données, la stratégie de regroupement impacte le nom des files d’attente créées dans injixo&nbsp;:

| Stratégie de regroupement   | Nom de la file d’attente                               | Exemple           |
| ------------------- | ---------------------------------------- | ----------------- |
| Numéro de téléphone        | Numéro de téléphone                             | +49123456789      |
| Routing(team/agent) | Nom de l’équipe                                | Tech Support Team |
| Routing(team/agent) | Nom de l’agent (si aucun nom d’équipe n’est assigné) | Agent 1           |

Pour les appels n’appartenant à aucun groupe dans Freshdesk Contact Center, le nom de la file d’attente est Undefined_Queue.
