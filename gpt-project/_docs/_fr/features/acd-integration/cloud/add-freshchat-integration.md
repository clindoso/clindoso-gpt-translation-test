---
title: Ajouter une intégration Freshchat
description: Apprenez comment connecter votre CRM Freshchat à injixo pour importer des données.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
redirect_from:
  - /fr/add-freshdesk-messaging-integration/
redirect_reason: Updated filename on 15 September 2023
---

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Ajouter une intégration Freshchat

Pour ajouter une nouvelle intégration Freshchat dans injixo, vous devez avoir un compte Freshchat Pro ou Enterprise. Suivez la procédure décrite dans {% link_new Ajouter une intégration Cloud | features/acd-integration/cloud/add-cloud-integration.md %}&nbsp;:

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Freshworks**, cliquez sur _Sélectionner le modèle_{:.doc-button}.
4. Dans la section **Freshchat**, cliquez sur _Ajouter cette intégration_{:.doc-button}.

## Configurer votre intégration Freshchat 

1. Entrez un nom unique permettant d’identifier la source de données.
2. Dans la section **Identifiants**, entrez votre nom de domaine Freshchat complet, en incluant le sous-domaine, par exemple exemple.freshchat.com.
3. Accédez à Freshchat et copiez une clé API valide d’un utilisateur ayant le rôle Account Administrator.
4. Retournez à injixo et collez la clé API dans le champ **Clé API**.
5. Cliquez sur _Sauvegarder l’intégration_{:.doc-button}. 

### Installer l’application injixo

L’intégration Freshchat nécessite une application client. Une fois que vous avez enregistré votre configuration, vous pouvez accéder à la section **Installer l’application injixo** en bas de la page.

Générez et copiez la **clé API injixo** ici.

Pour paramétrer l’application injixo dans votre compte Freshdesk, suivez les instructions à l’écran. Pour en savoir plus, reportez-vous à [Freshworks marketplace](https://www.freshworks.com/apps/freshdesk/injixo_connect).

## Données Freshchat dans injixo

### Contrats

Dans Freshchat, une conversation Chat contient généralement plusieurs conversations qui ont lieu entre les conseillers et les clients. Dans injixo, chaque contact par Chat résolu est compté comme un seul contact, sans tenir compte du nombre de conversations.

Exemple&nbsp;: un client crée une conversation par Chat sur le site, le conseiller répond mais résout le problème le jour suivant, car d’autres informations sont nécessaires. Cela représente un seul contact dans injixo.

### Convention d’affectation des noms des files d’attente

injixo crée des files d’attente source à partir de vos Chats en suivant cette convention&nbsp;:

«&nbsp;nom de groupe&nbsp;»

Exemples&nbsp;:

- Customer Support
- Undefined_Queue

### Chats supprimés et indésirables

Un Chat peut être supprimé ou marqué comme indésirable lorsqu’il est mis à jour. Dans ce cas, l’intégration ne peut pas déterminer le nom de groupe. Les files d’attente source qui comptabilisent ces Chats sont catégorisées en Undefined_Queue. Ces files d’attente sont généralement sans importance pour planifier le volume d’activité de vos employés.

