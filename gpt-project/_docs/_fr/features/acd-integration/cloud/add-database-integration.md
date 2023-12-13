---
title: Ajouter une intégration de base de données
navigation_title: Base de données
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Connecter votre base de données à injixo
redirect_from: /fr/add-odbc-integration/
redirect_reason: renamed article in September 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Qu’est-ce qu’une intégration de base de données&nbsp;?

Une intégration de base de données est un type d’intégration on-premise spécifique. Utilisez ce type d’intégration si votre système ne peut se connecter à l’aide d’une intégration Cloud ou d’une autre intégration on-premise.

Vous pouvez définir une requête SQL pour lire les données à partir d’une base de données. Les intégrations de base de données utilisent {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

## Ajouter une intégration de base de données

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Universal Interfaces**, cliquez sur _Sélectionner le modèle_{:.doc-button}.
4. Dans la section **Database**, cliquez sur _Ajouter cette intégration_{:.doc-button}.

## Configurer votre nouvelle intégration de base de données

1. Saisissez un nom unique permettant d’identifier la source de données.
2. Installez et connectez {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Sélectionnez votre **Type de base de données**.
4. Saisissez vos identifiants, en fonction de votre sélection.

   | Type de base de données                                  | Identifiants                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | MS SQL Server<br>MySQL<br>PostgreSQL | **Nom de la base de données**<br>**Hôte**<br>**Port**&nbsp;: si vous utilisez une instance nommée sur une connexion MS SQL Server, ne saisissez pas de port. À la place, ouvrez le port UDP 1434 dans votre pare-feu pour vous assurer que le service de navigateur SQL Server puisse déterminer le port d’injixo Cloud Link.<br>**Nom d’utilisateur**<br>**Mot de passe**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | Autre (ODBC)                                   | **Chaîne de connexion**&nbsp;: la chaîne de connexion contient les paramètres requis pour la connexion de l’intégration à votre serveur de base de données. Vous trouverez les chaînes de connexion pour votre type de base de données et de pilote ODBC sur [https://www.connectionstrings.com](https://www.connectionstrings.com).<br><br>Exemple pour une base de données InterSystem Caché&nbsp;:<br>`DRIVER={InterSystemsODBC};SERVER=myServerAddress;` `PORT=12345;DATABASE=myDataBase;UID=myUsername;PWD=myPassword;` <br><br>Les identificateurs SQL dans les requêtes seront délimités par des doubles guillemets. Ajoutez des options supplémentaires à la chaîne de connexion s’ils ne sont pas supportés par votre pilote ODBC par défaut, par exemple pour Informix.<br><br>Exemple pour une base de données IBM Informix&nbsp;:<br>`DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=myServerAddress;DATABASE=myDatabase;HOST=myHost;SERVICE=myService;UID=myUsername;PWD=myPassword;PROTOCOL=onsoctcp;DELIMIDENT=y;`<br><br>Vous pouvez également créer une source de données ODBC, dans laquelle vous pouvez configurer le pilote, le serveur, la base de données, etc. Cela vous permet d’ajouter l'option DSN ci-dessous en tant que chaîne de connexion au lieu d’inclure les détails de connexion dans la chaîne de connexion. Vous devrez ajouter les options qui ne peuvent pas être configurées dans la source de données ODBC, par exemple `DELIMIDENT=y`.<br><br>Exemples DSN&nbsp;:<br> `DSN=myODBCDatasourceName;`<br>`DSN=myODBCDatasourceName;DELIMIDENT=y;` |

## Configurer vos données d’import

1. Dans la section **Configuration**, sélectionnez le type de données que vous souhaitez importer depuis votre base de données&nbsp;:
   - **Par contact** pour les données historiques de contact avec une ligne pour chaque contact.
   - **Par intervalle** pour les données de contact historiques agrégées par intervalle de 15 ou 30&nbsp;minutes (définis comme durée d’intervalle).
   - **Statuts agents** pour les données de statuts agents.  
    Par défaut, les données sont importées toutes les 15 minutes, mais vous pouvez contrôler l’import à l’aide de deux cases à cocher supplémentaires&nbsp;:
        - **Importer les données en temps réel**&nbsp;: les données sont importées toutes les 10&nbsp;secondes. Disponible dans injixo Advanced WFM et Enterprise WFM uniquement.
        - **Rapprochement des données**&nbsp;: contrôle la période des données agent à importer toutes les 15&nbsp;minutes. Par défaut, les données importées sont celles des 24 dernières heures.  

2. Sélectionnez le **Fuseau horaire de la base de données** depuis le menu déroulant.
3. Saisissez la **requête SQL** qui sera utilisée pour importer les données de votre base de données. En savoir plus sur la requête [SQL](#requête-sql).
4. Pour créer l’intégration, cliquez sur _Sauvegarder l’intégration_{:.doc-button}.  
   L’intégration commence à importer les données dans injixo. Le premier import peut prendre du temps.  
   Toutes les files d’attente importées de la base de données connectée seront automatiquement disponibles sur la {% link_new page de configuration des Workloads | features/forecast/injixo-forecast/manage-workloads.md | # %} dans injixo Forecast.  
   Les activités externes seront disponibles dans l’activité Présent (ID 1). Pour importer des données de statuts agents, vous devez {% link_new mapper les identifiants et les activités externes | features/acd-integration/cloud/import-agent-status-data.md %}.

### Rapprochement des données

Il est parfois nécessaire de corriger manuellement les données de statut agent importées. Par exemple, il peut arriver qu’un employé oublie d’enregistrer la fin de sa journée et que vous ayez corrigé votre base de données pour indiquer son temps de travail réel.

La case **Rapprochement des données** est cochée par défaut. injixo importe à nouveau toutes les données&nbsp;:

- des 24 dernières heures,
- toutes les 15&nbsp;minutes.

Vous aurez toujours accès aux données les plus récentes des dernières 24&nbsp;heures. Seules les modifications des données plus anciennes que 24&nbsp;heures ne seront pas réimportées.

La réimportation continue des données peut ralentir votre base de données. Si vous avez besoin de désactiver le rapprochement des données, injixo n’importe que les données les plus récentes depuis la dernière importation réussie (généralement les données des 15 dernières minutes). Dans ce cas, vous devrez peut-être mettre à jour manuellement les données importées il y a plus de 15&nbsp;minutes dans injixo. Gardez la case cochée si possible, car les mises à jour manuelles des données représentent un volume de travail supplémentaire important et peut générer des erreurs.

Si vous mettez votre intégration en pause pendant moins de 24&nbsp;heures, injixo réimporte toutes les données dès le redémarrage de l’intégration. Ceci s’applique que la case soit cochée ou non.  
Si vous mettez votre intégration en pause pour période plus longue, toutes les données plus anciennes que 24&nbsp;heures ne seront pas réimportées.

## Requête SQL

La requête SQL pour une l’intégration d’une base de données doit contenir des noms de colonnes spécifiques. Le type de données à importer sélectionné détermine les colonnes attendues. Vous pouvez définir le nom de la table. Voici ci-dessous les requêtes SQL les plus simples que vous pouvez exécuter&nbsp;:

<style>
table th:first-of-type {
   width: 20%;
}
table th:nth-of-type(4) {
   width: 50%;
}
</style>

| Type de données importées | Exemple de requête                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------- |
| Par intervalle   | SELECT queueidentifier, queuename, timestamp, offered, answered, handlingtime, channel FROM table |
| Par contact    | SELECT queueidentifier, queuename, timestamp, answered, duration, channel FROM table              |
| Statuts agents     | SELECT agentidentifier, starttime, endtime, activity FROM table                                   |

> Remarque 
> 
> Dans la plupart des cas, les colonnes de votre base de données ne correspondront pas aux noms de colonnes attendus. Vous pouvez y remédier en utilisant les noms de colonnes requis en tant qu’alias de colonne ou créez une vue dans votre base de données.

Étendez les exemples de requêtes pour obtenir et filtrer des données de votre table personnalisée&nbsp;:

```
SELECT
  Start as "timestamp",
  Id as queueidentifier,
  Name as queuename,
  SUM(CASE "countId" WHEN 1000 THEN "val" ELSE 0 END) as offered,
  SUM(CASE "countId" WHEN 1001 THEN "val" ELSE 0 END) as answered,
  SUM(CASE "countId" WHEN 1002 THEN "val" ELSE 0 END) as handlingtime
  calls as channel
FROM table
WHERE countId IN (1000, 1001, 1002)
GROUP BY Start, Name
```

## Détails de la colonne

Les tableaux ci-dessous montrent les détails des colonnes attendues séparées par type d’importation.

### Statuts agents

<style>

table {
   width: 100%;
}  
table th:first-of-type {
   width: 20%;
}
table th:nth-of-type(4) {
   width: 50%;
}
</style>

| Colonne                    | Type de données | Requis | Détails                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| agentidentifier           | Chaîne    | Oui      | Identifiant unique de l’agent                                                                                                                                          |
| starttime                 | Datetime  | Oui      | Début de l’activité des statuts agent                                                                                                                                       |
| endtime                   | Datetime  | Non       | Fin de l’activité des statuts agent<br>Ne pas utiliser si l’activité est en cours                                                                                               |
| activité                  | Chaîne    | Oui      | Identifiant de l’activité externe                                                                                                                                     |

### Par intervalle

| Colonne                    | Type de données | Requis | Détails                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| queueidentifier           | Chaîne    | Oui      | Identifiant unique de la file d’attente<br>Vous pouvez renommer la file d’attente en modifiant queuename, mais queueidentifier restera identique.                                        |
| queuename                 | Chaîne    | Oui      | Identifiant de la file d’attente                                                                                                                                                 |
| timestamp                 | Datetime  | Oui      | Début de l’intervalle                                                                                                                                                    |
| reçus                   | Nombre entier   | Oui      | Nombre de contacts (par exemple, appels ou e-mails) dans l’intervalle                                                                                                                 |
| answered                  | Nombre entier   | Oui      | Nombre de contacts traités dans l’intervalle                                                                                                                |
| handlingtime              | Nombre entier   | Oui      | Temps de traitement total pour tous les contacts dans l’intervalle                                                                                                                       |
| média                   | Chaîne    | Non       | Identifiant pour le canal de la file d’attente source dans injixo.<br>S’il est vide, la valeur par défaut sera appels.<br>Valeurs acceptées&nbsp;: calls, chats, emails, social_media, documents, cases. |

### Par contact

| Colonne                    | Type de données | Requis | Détails                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| queueidentifier           | Chaîne    | Oui      | Identifiant unique de la file d’attente<br>Vous pouvez renommer la file d’attente en modifiant queuename, mais queueidentifier restera le même.                                        |
| queuename                 | Chaîne    | Oui      | Identifiant de la file d’attente                                                                                                                                                 |
| timestamp                 | Datetime  | Oui      | Début de l’intervalle                                                                                                                                                    |
| reçus                   | Nombre entier   | Oui      | Contact reçu (valeur 1)<br>Pas de contact reçu (valeur 0)                                                                                                                |
| answered                  | Nombre entier   | Oui      | Contact traité (valeur 1)<br>Pas de contact traité (valeur 0)                                                                                                                |
| durée                  | Nombre entier   | Oui      | Temps de traitement total pour un seul contact                                                                                                                                    |
| média                   | Chaîne    | Non       | Identifiant pour le canal de la file d’attente source dans injixo.<br>S’il est vide, la valeur par défaut sera appels.<br>Valeurs acceptées&nbsp;: calls, chats, emails, social_media, documents, cases. |

## Modifier une intégration de base de données

Lorsque les détails ou la structure des données de votre base de données change, vous pouvez modifier la configuration de votre intégration de base de données. Le prochain import de données sera effectué comme précédemment. Si vous avez besoin de réimporter toutes les données disponibles passées, créez une nouvelle intégration.

## Problèmes connus du pilote ODBC

Pour éviter d’augmenter le nombre de connexions TCP dans Cloud Link lors de l’interrogation des données depuis Amazon Athena, assurez-vous d’utiliser la [version 2.x du pilote ODBC 2.x](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver.html).

