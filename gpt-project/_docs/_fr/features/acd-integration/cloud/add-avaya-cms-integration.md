---
title: Ajouter une intégration Avaya CMS
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Découvrez comment connecter votre base de données Avaya à injixo pour importer les données.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Avaya CMS est une intégration on-premise permettant d’importer des données d’appel et les statuts agent.

Cette intégration utilise {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Ajouter une intégration Avaya CMS

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Avaya CMS**, cliquez sur _Ajouter cette intégration_{:.doc-button}.

## Configurer votre nouvelle intégration Avaya CMS

1. Saisissez un nom unique pour la nouvelle intégration.
   Le nom vous aidera à identifier la source des données et à déterminer la relation entre les files d’attente et les intégrations.<br>Exemple&nbsp;: Intégration Avaya - Équipe support client
1. Installez et connectez {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
1. Dans la section **Configuration**, paramétrez votre intégration&nbsp;:
 - Entrez la [chaîne de connexion](#chaîne-de-connexion) définissant les paramètres requis pour connecter la base de données du CMS. 
 - Sélectionnez le Fuseau horaire de votre base de données depuis le menu déroulant.
 - Cochez la case **Importer les statuts agent détaillés** pour ajouter des informations sur les skills (profil agent) et les splits (routage des appels) aux statuts agent importés.
 - Pour importer les données de statut agent en temps réel, cochez la case **Importer les données en temps réel**. Dans ce cas, entrez un numéro de port dans le champ **Port**.<br>
   injixo Cloud Link ouvrira un socket d’écoute TCP sur le port spécifié. Le service Avaya Generic RTA se connectera à ce port et commencera à importer les données de statut agent en temps réel. Le service Avaya Generic RTA est sous licence et configuré dans Avaya.
1. Pour créer l’intégration, cliquez sur _Sauvegarder l’intégration_{:.doc-button}.

L’intégration commence à importer les données dans injixo. Si vous souhaitez importer des données de statut agent, vous devez {% link_new mapper les identifiants et les activités externes | features/acd-integration/cloud/import-agent-status-data.md %} une fois votre intégration Avaya configurée. Si vous avez activé l’option **Importer les données en temps réel**, mettez votre intégration en pause.

## Chaîne de connexion

L’intégration Avaya CMS nécessite une chaîne de connexion pour se connecter à votre base de données Avaya CMS. Étant donné qu’Avaya CMS utilise généralement une base de données IBM Informix, vous devez utiliser une chaîne de connexion spéciale. 

Exemples de chaînes de connexion utilisant le pilote ODBC IBM Informix&nbsp;:<br>
- `DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=myServerAddress;DATABASE=myDatabase;HOST=myHost;SERVICE=myService;UID=myUsername;PWD=myPassword;PROTOCOL=onsoctcp;DELIMIDENT=y;` (accès natif via le pilote ODBC)
- `DSN=AvayaCMS;DELIMIDENT=y;` (nécessite une connexion ODBC appelée AvayaCMS)
Si votre Avaya CMS n’utilise pas une base de données IBM Informix, vous devez obtenir la chaîne de connexion appropriée pour votre type de base de données et le pilote ODBC. Avaya ne prend en charge que la connectivité ODBC.

## Modifier une intégration Avaya CMS

Si les détails de l’intégration changent, comme par exemple les identifiants du serveur de la base de données, vous pouvez modifier et mettre à jour la configuration de votre intégration. L’import de données continuera en utilisant la configuration mise à jour.
