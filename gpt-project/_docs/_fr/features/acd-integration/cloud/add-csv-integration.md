---
title: Ajouter une intégration par fichier CSV
navigation_title: CSV
description: Importer des données historiques dans injixo à l’aide de fichiers CSV.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /fr/csv-format/
redirect_reason: /csv-format/ used on in injixo UI (injixo.com/csv-importer)
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
---

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Qu’est-ce qu’une intégration par fichier CSV&nbsp;?

Une intégration par fichier CSV importe les données historiques de contact ou de statuts agent à partir d’un fichier CSV. Utilisez une intégration par fichier CSV si injixo ne peut se connecter à aucun autre système externe.

Voici une vue d’ensemble du processus d’intégration par fichier CSV&nbsp;: 

- Créez une intégration par fichier CSV dans injixo.
- Créez un schéma CSV.
- Mappez les colonnes (à l’aide des menus déroulants ou d’une requête SQL).
- Importez automatiquement ou manuellement les fichiers CSV.

## Ajouter une intégration par fichier CSV

Pour importer différents formats de fichiers CSV (par exemple avec différents séparateurs, formats de date ou noms de colonne), configurez une intégration distincte pour chacun d’entre eux. Selon le fichier CSV généré par votre système externe, injixo peut attendre des colonnes différentes de celles du fichier. [En savoir plus](#mapping-des-colonnes) sur les colonnes attendues par injixo et comment les mapper si votre fichier CSV contient des noms de colonnes différents.

Pour ajouter une intégration CSV dans injixo, suivez ces étapes&nbsp;:

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Universal Interfaces**, cliquez sur _Sélectionner le modèle_{:.doc-button}.
4. Dans la section **CSV**, cliquez sur _Ajouter cette intégration_{:.doc-button}.

## Configurer une nouvelle intégration par fichier CSV

1. Dans la section **Informations générales**, entrez un nom unique permettant d’identifier la source de données.
2. Dans la section **injixo Cloud Link**, installez {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md | #installer-injixo-cloud-link %} et connectez-le. Si vous souhaitez [importer les données manuellement](#import-manuel-de-fichiers), vous pouvez ignorer cette étape.
3. Dans la section **Configuration du schéma CSV**, sélectionnez le type de données à importer&nbsp;:
   - **Données sur les contacts**&nbsp;: les données importées contiennent tous les volumes offerts et traités enregistrés par votre système externe, tels que les appels, les chats, les réseaux sociaux, les tickets, les e-mails ou les documents.
   - **Statuts agent**&nbsp;: les données importées contiennent toutes les activités des agents enregistrées par votre système externe, par exemple connexion, déconnexion, en appel, traitement post-appel, pause, prêt, etc.
4. Cliquez sur _Créer un nouveau schéma CSV_{:.doc-button}.
5. Configurez les paramètres du schéma CSV. Cela comprend&nbsp;:
   - le paramétrage et la configuration du pré-traitement,
   - le mapping des colonnes (par défaut [via les menus déroulants](#mapping-des-colonnes), ou par [requête SQL](#mapping-des-colonnes-requête-sql)).
      En savoir plus sur la [création d’un schéma CSV](#créer-un-schéma-csv) en incluant les options de configuration ci-dessus.
6. Pour créer l’intégration, cliquez sur _Sauvegarder l’intégration_{:.doc-button}.

Après avoir sauvegardé l’intégration, vous pouvez [importer les données manuellement](#import-manuel-de-fichiers) ou [automatiquement](#import-automatique-de-fichiers).

## Créer un schéma CSV

Chaque intégration par fichier CSV possède son propre schéma. Un schéma décrit le formatage et le mapping des colonnes du fichier CSV. Si votre système externe génère un fichier CSV qui ne contient pas les noms exacts des colonnes indiquées dans injixo, vous pouvez les mapper dans injixo à l’aide des [menus déroulants (par défaut)](#mapping-des-colonnes) ou d’une [requête SQL](#mapping-des-colonnes-requête-sql).  
[En savoir plus](#mapping-des-colonnes) sur les colonnes attendues par injixo et comment les mapper si votre fichier CSV contient des noms de colonnes différents.

Avant de créer le schéma CSV, vous devez [ajouter une intégration par fichier CSV](#ajouter-une-intégration-par-fichier-csv) et sélectionner le type de données à importer. Les paramètres que vous configurez pour le schéma CSV dépendront du type de données à importer sélectionnées (données sur les contacts ou statuts agent).

### Paramétrage et configuration du pré-traitement

1. Dans la section **Configuration**, ajoutez un modèle de fichier CSV généré par votre système externe. Ceci vous permet de voir comment injixo traitera les fichiers de votre système pendant l’import.
2. Configurez les paramètres suivants. Selon le type de données à importer, différents paramètres sont à configurer&nbsp;:<br><br>

   | Paramètre                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Séparateur de colonnes du fichier CSV**                              | Caractère de séparation utilisé dans le fichier CSV importé, par exemple point-virgule                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | **Fuseau horaire**                                                 | Fuseau horaire dans lequel votre système externe récupère les données, par exemple Europe/Paris (UTC+01:00)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | **Groupement des données**<br>(Données sur les contacts uniquement)                     | Le groupement des données dépend de la méthode de création de votre fichier CSV&nbsp;:<br>**Par contact**&nbsp;: pour les fichiers contenant une ligne pour chaque contact. Étant donné que les données de contact sont agrégées en intervalles de 15&nbsp;minutes, l’intervalle de l’unité opérationnelle doit être de 15&nbsp;minutes. Les nouveaux imports de données remplaceront les données précédemment importées pour cet intervalle. Si votre fichier contient la même date et heure plusieurs fois, ces données seront ajoutées sur l’intervalle.<br><br>**Par intervalle**&nbsp;: pour les données agrégées contenant une ligne avec toutes les informations de contact par intervalle. Sélectionnez également la durée d’intervalle correspondant à celle de votre fichier CSV. Si vous sélectionnez un intervalle plus long que celui des fichiers importés, vous verrez un message d’erreur. Si vous sélectionnez un intervalle de 15&nbsp;minutes pour un fichier dont les intervalles sont plus longs (par exemple de 30&nbsp;minutes), chaque intervalle manquant (ici, chaque seconde) sera marqué d’un 0 ou du texte «&nbsp;no data&nbsp;», en fonction de votre choix dans l’option **Traitement des données manquantes dans les intervalles**. |
   | **Traitement des données manquantes dans les intervalles**<br>(Données sur les contacts uniquement) | Définissez la façon dont les données manquantes de la file d’attente cible seront affichées dans les autres modules d’injixo&nbsp;:<br>**Remplir avec des zéros**&nbsp;: les valeurs manquantes seront remplacées par 0.<br>**Laisser vide**&nbsp;: les valeurs manquantes seront remplacées par le texte «&nbsp;no data&nbsp;».<br>L’option **Laisser vide** fonctionne dans la plupart des cas. Les imports remplaceront les données existantes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

3. (Facultatif) Dans la section **Configuration du pré-traitement**, sélectionnez les options qui s’appliquent au format de votre fichier CSV&nbsp;:<br><br>

   | Option de pré-traitement       | Description                                                                                                                                                                                             |
   | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Ajouter une ligne d’en-tête**         | Pour les fichiers sans ligne d’en-tête, injixo nommera les colonnes A, B, C, etc. dans la page de [mapping des colonnes](#mapping-des-colonnes).                                                                                                            |
   | **Ignorer les lignes vides**        | injixo ignore les lignes vides contenant uniquement des séparateurs.                                                                                                                                                  |
   | **Ignorer les premières lignes**        | injixo supprime les lignes supplémentaires au début du fichier. Saisissez le nombre de lignes à ignorer.                                                                                               |
   | **Ignorer les lignes contenant** | injixo ignore les lignes contenant certains caractères. Saisissez une chaîne de caractères (veillez à respecter les majuscules et le minuscules). injixo ignore les lignes contenant cette chaîne de caractères. Vous pouvez ajouter plusieurs chaînes en cliquant sur _Ajouter une chaîne de caractères_{:.doc-button}. |

4. Pour continuer vers le mapping des colonnes, cliquez sur _Mapping des colonnes_{:.doc-button}.

### Mapping des colonnes

Par défaut, vous pouvez utiliser les menus déroulants dans la section **Mapping des colonnes** pour définir la correspondance des colonnes de vos fichiers CSV avec celles requises par injixo. Avant de mapper les colonnes, vous devez compléter la [configuration](#paramétrage-et-configuration-du-pré-traitement).
Si votre système externe génère des fichiers CSV qui ne contiennent pas les colonnes attendues, vous pouvez les [mapper à l’aide d’une requête SQL](#mapping-des-colonnes-requête-sql).

La page de mapping affiche un aperçu du fichier CSV importé.

1. À l’aide des menus déroulants, mappez les colonnes et les formats du fichier CSV.

2. Remplissez les champs.  
   Pour en savoir plus sur les options pour les [données sur les contacts](#menus-déroulants-pour-les-données-sur-les-contacts) et les [statuts agent](#menus-déroulants-pour-les-statuts-agent), consultez le tableau ci-dessous.

3. Pour sauvegarder votre configuration, cliquez sur _Enregistrer le modèle_{:.doc-button}.

#### Menus déroulants pour les données sur les contacts

Si vous avez sélectionné **Données sur les contacts** comme type de données à importer, la page de mapping par défaut affiche les éléments suivants&nbsp;:

| Champ          | Description                                                                                                                                                                                                                                          | Requis pour les données par intervalle | Requis pour les données par contact |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------: | :-----------------------------: |
| **File d’attente** | Nom de la file d’attente à partir de laquelle les données sont importées                                                                                                                                                                                                        |               Oui                |               Oui               |
| **Date**       | Valeurs et format de la date<br>Par défaut, vous pouvez sélectionner un format de date correspondant au format du fichier CSV dans la liste déroulante. Pour configurer un [format de date personnalisé](#format-de-date-personnalisé), cliquez sur l’{% icon gear %} et saisissez le format dans le champ de texte. |               Oui                |               Oui               |
| **Heure**       | Valeurs et format utilisés                                                                                                                                                                                                                          |               Oui                |               Oui               |
| **Date et heure**  | Valeurs de date et heure avec un [format personnalisé](#format-de-date-et-heure-personnalisé)<br>Cette colonne est disponible lorsque vous activez l’option **Date et heure dans la même colonne**.                                                                              |               Oui                |               Oui               |
| **Reçus**    | Contacts reçus (par intervalle pour les données par intervalle)<br>Accepte les nombres entiers ou les décimales indiquées par un point.                                                                                                                                            |               Oui                |               Oui               |
| **Traités**    | Contacts traités (par intervalle pour les données par intervalle)<br>Accepte les nombres entiers et les décimales indiquées par un point.<br>Pour les données par contact, la valeur des contacts traités peut uniquement être 0 ou 1 (ou des décimales).                                              |               Oui                |               Oui               |
| **TMT**        | Temps moyen de traitement par intervalle<br> Les formats pris en charge sont les secondes (nombre entier) ou hh:mm:ss (par exemple 00:05:00).<br>Si aucune colonne ne correspond au TMT, sélectionnez **Aucune colonne**.<br>Ce champ s’affiche uniquement pour les données par intervalle.                           |                Non                |               Non                |
| **Durée**   | Durée de l’enregistrement en secondes (nombre entier)<br>Ce champ s’affiche uniquement pour les données par contact.                                                                                                                                                                        |                Non                |               Oui               |
| **Média**    | Nom du canal prédéfini (premier menu déroulant) ou colonne à sélectionner contenant le nom du canal (second menu déroulant)<br>Valeurs autorisées&nbsp;: calls, emails, chats, documents, cases, social_media                                                           |               Oui                |               Oui               |

#### Menus déroulants pour les statuts agent

Si vous avez sélectionné Statuts agent comme type de données à importer, la page de mapping par défaut affiche les éléments suivants&nbsp;:

| Champ                   | Description                                                                                                                                                                                                                                                                          | Requis |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| **Identifiant de l’agent**    | Identifiant unique de l’agent, par exemple identifiant interne ou nom                                                                                                                                                                                                                                     | Oui      |
| **Identifiant de l’activité** | L’activité sur laquelle travaille l’agent                                                                                                                                                                                                                                                     | Oui      |
| **Date de début**          | Date à laquelle l’agent a commencé l’activité<br>Par défaut, vous pouvez sélectionner un format correspondant au format de votre fichier CSV dans la liste déroulante. Pour configurer un [format de date personnalisé](#format-de-date-personnalisé), cliquez sur l’{% icon gear %} et saisissez le format dans le champ de texte.   | Oui      |
| **Heure de début**          | Heure à laquelle l’agent a commencé l’activité                                                                                                                                                                                                                                         | Oui      |
| **Date et heure de début**     | [Date et heure avec format personnalisé](#format-de-date-et-heure-personnalisé) contenant la date et l’heure auxquelles l’agent a commencé l’activité<br>Cette colonne est disponible lorsque vous activez l’option **Date et heure dans la même colonne**.                                                                 | Oui      |
| **Date de fin**            | Date à laquelle l’agent a terminé l’activité<br>Par défaut, vous pouvez sélectionner un format de date prédéfini correspondant au format du fichier CSV depuis la liste déroulante. Pour configurer un [format de date personnalisé](#format-de-date-personnalisé), cliquez sur l’{% icon gear %} et saisissez le format personnalisé dans le champ de texte. | Non       |
| **Heure de fin**            | Heure à laquelle l’agent a terminé l’activité                                                                                                                                                                                                                                         | Non       |
| **Date et heure de fin**       | [Date et heure avec format personnalisé](#format-de-date-et-heure-personnalisé) contenant la date et l’heure auxquelles l’agent a terminé l’activité<br>Cette colonne est disponible lorsque vous activez l’option **Date et heure dans la même colonne**.                                                                 | Non       |

#### Format de date personnalisé

Vous pouvez configurer un format de date personnalisé correspondant à la date dans vos fichiers CSV. Ajoutez les caractères suivants au champ **Format de date personnalisé**&nbsp;:

- pour le jour&nbsp;: **D** (chiffres simples de 1 à 9) ou **DD** (pour les zéros de tête)
- pour le mois&nbsp;: **M** (chiffres simples de 1 à 9) ou **MM** (pour les zéros de tête)
- pour l’année&nbsp;: **YY** ou **YYYY**

Tous les autres caractères sont interprétés comme des séparateurs.

Exemples&nbsp;:

| Date     | Format de date personnalisé |
| -------- | ------------------ |
| 13/1,22  | D/M,YY             |
| 010122   | DDMMYY             |
| 13012022 | DDMMYYYY           |

#### Format de date et heure personnalisé

Pour ajouter un format de date et heure personnalisé, activez l’option **Date et heure dans la même colonne**.
En plus du [format de date personnalisé](#format-de-date-personnalisé), vous devez définir le format de l’heure avec des minuscules&nbsp;:

- pour les heures&nbsp;: **h** (chiffres simples de 1 à 9) ou **hh** (pour les zéros de tête),
- pour les minutes&nbsp;: **m** (chiffres simples de 1 à 9) ou **mm** (pour les zéros de tête),
- (facultatif) pour les secondes&nbsp;: **s** (chiffres simples de 1 à 9) ou **ss** (pour les zéros de tête).

Exemples&nbsp;:

| Date et heure  | Format de date et heure |
| -------------- | ---------------- |
| 13/1,22 9:15:8 | J/M,AA h:m:s     |
| 010122 09-15   | JJMMAA hh-mm     |

### Mapping des colonnes (requête SQL)

Pour la plupart des fichiers CSV, vous pouvez utiliser le mapping par défaut à l’aide des menus déroulants. Si votre système externe génère des fichiers CSV qui ne contiennent pas certaines des colonnes requises par le formulaire de mapping par défaut (c’est à dire si elle nécessitent des calculs supplémentaires) ou s’ils contiennent des formats non pris en charge, la [méthode de mapping par défaut](#mapping-des-colonnes) risque de ne pas fonctionner pour vous. Dans ce cas, vous pouvez mapper les colonnes à l’aide d’une requête SQL (SQLite). Elle vous permettra de convertir les valeurs totales en moyennes ou de calculer un volume d’appels pour plusieurs colonnes, par exemple. Cette méthode de mapping n’est disponible que pour les données de contact. Elle ne peut pas être utilisée pour les données de statut agent.

#### Prérequis techniques

Veuillez prendre en compte les exigences suivantes pour écrire une requête SQL pour le mapping des colonnes&nbsp;:

- Utilisez `uploaded_file` comme nom de la table.
- Utilisez des minuscules pour le nom des colonnes.
- Utilisez le type de données date et heure pour la colonne date et heure (au format `YYYY-MM-DD hh:mm:ss`).
- Utilisez la syntaxe de requête [SQLite](https://www.sqlite.org).

Une requête SQL [SQLite](https://www.sqlite.org) supporte les opérations mathématiques, les conversions de données et les alias de colonnes (pour mapper des noms de colonne différents). Pour en savoir plus sur les limitations des éléments suivants, consultez sqlite.org&nbsp;:

- [précision numérique](https://www.sqlite.org/datatype3.html)
- [fonctions mathématiques](https://www.sqlite.org/lang_mathfunc.html)
- [conversions implicites de données](https://www.sqlite.org/datatype3.html#affinity)
- [fonctions de date et heure](https://www.sqlite.org/lang_datefunc.html)
- [manipulation de chaînes](https://www.sqlite.org/lang_corefunc.html#string_functions)

Pour mapper les colonnes à l’aide d’une requête SQL, suivez ces étapes&nbsp;:

> Changer de méthode de mapping remplacera un schéma CSV existant
>
> Si vous avez déjà créé un schéma CSV, changer de méthode de mapping et sauvegarder le nouveau schéma remplacera le précédent schéma. Une fois remplacé, vous ne pouvez pas restaurer le schéma CSV.

1. Activez l’option **Utiliser une requête SQL pour mapper les colonnes** en haut à droite de la page de mapping des colonnes.
2. Saisissez une requête SQL (SQLite) dans le champ de texte. Conseil&nbsp;: copiez et collez les exemples de requêtes ci-dessous en fonction de vos besoins.

Si vous souhaitez importer des données de contact par intervalle et par contact, vous devez ajouter une intégration distincte et écrire une requête SQL pour chacune d’entre elles.

### Colonnes requises dans la requête SQL

Le tableau suivant présente une vue d’ensemble des colonnes requises dans la requête SQL&nbsp;:

> En fonction de votre [offre WFM](https://www.injixo.com/pricing/), tous les canaux pour la file d’attente source d’injixo ne seront peut-être pas disponibles.

| Nom de la colonne | Type de données | Requis | Détails                                                                                                                                                                                                  |
| ----------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| queue       | Chaîne    | Oui      | Identifiant de la file d’attente                                                                                                                                                                                 |
| timestamp   | Datetime  | Oui      | Début de l’intervalle au format AAAA-MM-DD hh:mm:ss                                                                                                                                                  |
| offered     | Nombre entier   | Oui      | Nombre de contacts (par exemple, appels ou e-mails) dans l’intervalle                                                                                                                                                 |
| answered    | Nombre entier   | Oui      | Par intervalle&nbsp;: nombre de contacts traités dans l’intervalle<br>Par contact&nbsp;: la valeur 1 indique que le contact a été traité. La valeur 0 indique que le contact n’a pas été traité. |
| aht         | Float     | Non       | Temps de traitement moyen pour tous les contacts dans l’intervalle                                                                                                                                                   |
| duration    | Nombre entier   | Oui      | Temps de traitement total pour un seul contact                                                                                                                                                                  |
| channel     | Chaîne    | Oui      | Identifiant pour le canal de la file d’attente source dans injixo<br>Valeurs acceptées&nbsp;: calls, chats, emails, social_media, documents, cases.                                                                            |

#### Exemples de requêtes simples

Données de contact par intervalle&nbsp;:

```sql
SELECT
   queue, timestamp,
   offered, handled, aht,
   channel
FROM uploaded_file
```

Données de contact par contact&nbsp;:

```sql
SELECT
   queue, timestamp,
   offered, handled, duration,
   channel
FROM uploaded_file
```

Les exemples plus complexes suivants montrent l’application d’opérations mathématiques et de fonctions SQLite.

#### Exemple de requête complexe 1

- Diviser HandleTime par HandledCalls pour le temps moyen de traitement (TMT) requis.
- Combiner Date et Time à l’aide de SUBSTR pour le format date et heure AAAA-MM-JJ HH:MM:SS.

|   File d’attente    |    Date    | Heure  | Reçu | HandledCalls | Aband | HandleTime | HoldTime |
| :--------: | :--------: | :---: | :------: | :----------: | :---: | :--------: | :------: |
| test queue | 06/03/2023 | 07:30 |    5     |      5       |   -   |   1324,6   |    -     |
| test queue | 06/03/2023 | 08:00 |    2     |      2       |   -   |    1548    |    -     |

```
SELECT
  Queue as queue,
  SUBSTR(Date, 7, 4) || '-'|| SUBSTR(Date, 1, 2) || '-' || SUBSTR(Date, 4,2) || ' ' || Time || ':00' as timestamp,
  Received as offered,
  HandledCalls as handled,
  HandleTime/HandledCalls as aht,
  'chats' as channel
FROM uploaded_file
```

#### Exemple de requête complexe 2

- Utilisez `date('now')` de SQLite pour obtenir la date actuelle et la combiner avec l’heure du fichier.
- Supprimer les décimales et les convertir en nombre entier.
- Combiner Date et Time à l’aide de SUBSTR pour le format date et heure AAAA-MM-JJ HH:MM:SS.

Dans cet exemple, les en-têtes des colonnes contiennent des caractères vides. 

| Nom de la file d’attente | Heure au format hh:mm | Appels reçus | Appels traités | Temps moyen de traitement (TMT) |
| :--------: | :-----------: | :-----------: | :-----------: | :-------------------------: |
| demo queue |     07:00     |      3.4      |      2.9      |          00:05:30           |
| demo queue |     08:30     |      5.7      |      5.2      |          00:10:15           |

Vous pouvez remplacer la ligne d’en-tête en utilisant les options de prétraitement de l’intégration&nbsp;:

- Ignorer les 1 premières lignes&nbsp;: supprime l’en-tête original
- Ajouter une ligne d’en-tête&nbsp;: ajoute des en-têtes de colonne avec des lettres

```
 SELECT
   A as queue,
   DATE('now')||' '|| "B"||':00' as timestamp,
   FLOOR(C) as offered,
   FLOOR (D) as handled,
   (CAST(substr(E, 1, 1) AS INTEGER) * 3600) +
   (CAST(substr(E, 3, 2) AS INTEGER) * 60) +
   CAST(substr(E, 6, 2) AS INTEGER) as aht,
   'calls' as channel
FROM uploaded_file
```

Si vous ne remplacez pas la ligne d’en-tête, faites référence aux noms de colonnes réels en utilisant des guillemets doubles&nbsp;: 

```
 SELECT
   "Queue Name" as queue,
   DATE('now')||' '|| "Hour in hh:mm"||':00' as timestamp,
   FLOOR("Offered Calls") as offered,
   FLOOR ("Handled Calls") as handled,
   (CAST(substr("Average Handling Time", 1, 1) AS INTEGER) * 3600) +
   (CAST(substr("Average Handling Time", 3, 2) AS INTEGER) * 60) +
   CAST(substr("Average Handling Time", 6, 2) AS INTEGER) as aht,
   'calls' as channel
FROM uploaded_file
```

#### Exemple de requête complexe 3

- Calculer les appels traités en soustrayant AbandonedCalls de OfferedCalls.
- Transformer la chaîne Start au format spécial dans le format date et heure AAAA-MM-DD HH:MM:SS requis.

|  Name  |       Start       | OfferedCalls | AbandonedCalls | AverageHandlingTime |
| :----: | :---------------: | :----------: | :------------: | :-----------------: |
| queue1 | 20230613 15:30:00 |      10      |       2        |         300         |
| queue2 | 20230613 15:35:00 |      15      |       3        |         450         |
| queue3 | 20230613 15:40:00 |      12      |       2        |         350         |

<!-- notes for database integrations -->
<!-- In this example, the date time format in the Start column is not supported by built-in SQLite `datetime()` and `strftime()` functions. You need to change the string first. -->
<!-- changed the example from datetime(substr(Start, 1, 4) || '-' || to substr(Start, 1, 4) || '-' || -->
<!-- `datetime` is not required here, but in database integrations it would be needed due to the reqiured datetime datatype in the table around line 210 -->

```
SELECT
  Name as queue,
    substr(Start, 1, 4) || '-' ||
    substr(Start, 5, 2) || '-' ||
    substr(Start, 7, 2) || ' ' ||
    substr(Start, 10, 8) as timestamp,
  Offered as offered,
  (Offered - Abandoned) as handled,
  AverageHandlingTime as aht,
  'calls' as channel
FROM uploaded_file
```

<!-- do not change the heading, used in the integrations UI -->

## Modifier un schéma CSV

Lorsque la structure des données d’un fichier change, vous devez modifier le schéma CSV de l’intégration.

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Cliquez sur l’{% icon pencil %} en face de l’intégration que vous souhaitez modifier.
3. Cliquez sur _Modifier le schéma CSV_{:.doc-button}.
   Vous pouvez modifier les options dans la section **Paramétrage**. Pour modifier les options de pré-traitement, cliquez sur _Recharger le fichier_{:.doc-button} et importez le fichier CSV modifié ou original.
4. Cliquez sur _Mapping des colonnes_{:.doc-button}. Vous pouvez modifier le mapping de vos colonnes si nécessaires.
5. Cliquez sur _Enregistrer le modèle_{:.doc-button}.

> Le regroupement des données ne peut être modifié
>
> Lorsque vous modifiez un schéma CSV, vous ne pouvez pas modifier le regroupement des données (par exemple par contact ou par intervalle).

## Exemples de mappings

Dans cette section, vous trouverez des exemples de fichiers CSV et les mappings associés. Vous pouvez utiliser les exemples comme modèles pour vos propres fichiers CSV.

### Données de contact (par intervalle)

Fichier CSV&nbsp;:

```

Queue;Date;Time;IncomingCalls;AnsweredCalls;AHT
My Inbound Queue;25/05/2020;08:00;15;14;230
My Inbound Queue;25/05/2020;08:15;16;15;210
My Inbound Queue;25/05/2020;08:30;20;18;235
My Inbound Queue;25/05/2020;08:45;18;15;215

```

<!-- left-align all tables -->
<style>
table {
   margin-left: 0px;
}
</style>

Mapping des colonnes&nbsp;:

| Colonne      | Mapping de la colonne/valeur |
| ----------- | ------------------- |
| Nom de la file d’attente  | File d’attente               |
| Date        | Date                |
| Format de la date | jj/mm/aaaa          |
| Heure        | Heure                |
| Format de l’heure | hh:mm               |
| Reçus     | IncomingCalls       |
| Traités     | AnsweredCalls       |
| TMT         | TMT                 |
| Format du TMT  | Secondes             |

Cette exemple n’inclut pas de colonne Média. Dans la configuration du schéma CSV, sélectionnez l’option **Média**. Par exemple, pour définir le canal pour les appels, sélectionnez **Appels** dans le menu déroulant.

### Données de contact (par contact)

Fichier CSV&nbsp;:

```

Queue;Date;Time;Offered;Answered;Duration
My Inbound Queue;25/05/2020;08:00;1;1;100
My Inbound Queue;25/05/2020;08:03;1;0;0
My Inbound Queue;25/05/2020;08:04;1;1;120
My Inbound Queue;25/05/2020;08:07;1;0;0

```

Mapping des colonnes&nbsp;:

| Colonne      | Mapping de la colonne/valeur |
| ----------- | ------------------- |
| Nom de la file d’attente  | File d’attente               |
| Date        | Date                |
| Format de la date | jj/mm/aaaa          |
| Heure        | Heure                |
| Format de l’heure | hh:mm               |
| Reçus     | Reçus             |
| Traités     | Reçus            |
| Durée    | Durée            |

Cette exemple n’inclut pas de colonne Média. Dans la configuration du schéma CSV, sélectionnez l’option **Média**. Par exemple, pour définir le canal pour les appels, sélectionnez **Appels** dans le menu déroulant.

### Statuts agent

Fichier CSV&nbsp;:

```

StartDate;StartTime;AgentID;AgentActivityID
2022-04-22;08:34:29;816;1013;
2022-04-22;08:34:42;816;1015;
2022-04-22;08:34:48;816;1015;
2022-04-22;08:39:11;816;1015;

```

Mapping des colonnes&nbsp;:

| Colonne              | Mapping de la colonne/valeur |
| ------------------- | ------------------- |
| Identifiant de l’agent    | AgentID             |
| Identifiant de l’activité | AgentActivityID     |
| Date de début          | StartDate           |
| Format de la date         | aaaa-mm-jj          |
| Heure de début          | StartTime           |
| Format de l’heure         | hh:mm:ss            |

## Importer des fichiers CSV

Une fois votre intégration sauvegardée, vous pouvez commencer à importer des fichiers CSV.
Les encodages de fichier suivants sont pris en charge&nbsp;:

- UTF-8
- ISO-8859-1/Latin-1
- ISO-8859-9
- Windows-1252

Nous recommandons d’utiliser UTF-8 pour éviter les messages d’erreur génériques.

### Import automatique de fichiers

[Configurez une intégration CSV](#configurer-une-nouvelle-intégration-par-fichier-csv) et connectez Cloud Link. injixo Cloud Link importera les nouvelles données dans injixo. À chaque nouvel enregistrement de fichier CSV dans le dossier d’installation d’injixo Cloud Link, un nouvel import commence par défaut. Vous pouvez modifier le dossier d’installation par défaut (C:\\Program Files\\injixo Cloud Link) pendant l’installation.

Vous pouvez également configurer un {% link_new dossier d’importation | features/acd-integration/cloud/install-cloud-link.md | #configurer-le-dossier-dimport %} distinct pour les imports de fichiers. Sauvegardez les nouveau fichiers dans le dossier d’importation.

Une fois les données importées, vous pouvez {% link_new ajouter de nouvelles files d’attente à un workload | features/forecast/injixo-forecast/manage-workloads.md %} dans Forecast, ou bien vous verrez les données mises à jour dans vos workloads existants. Si aucune donnée n’est importée, utilisez l’import de fichier manuel décrit ci-dessous pour vérifier si le format de votre fichier est valide.

### Import manuel de fichiers

Vous pouvez importer des données manuellement dans injixo à l’aide d’une page Web.

Une fois que vous avez [ajouté une intégration par fichier CSV](#configurer-une-nouvelle-intégration-par-fichier-csv), vous pouvez importer des données manuellement (vous pouvez ignorer l’installation d’injixo Cloud Link).

1. Accédez à [https://www.injixo.com/csv-importer](https://www.injixo.com/csv-importer).
2. Cliquez sur **ouvrez votre explorateur de fichier** et sélectionnez un fichier CSV (ou déposez-le directement dans le navigateur).
3. Dans le menu déroulant en bas à gauche, sélectionnez votre intégration par fichier CSV.
4. Cliquez sur _Importer le fichier_{:.doc-button}.
   Pour éviter les messages d’erreur, le format du fichier doit correspondre au [schéma CSV](#créer-un-schéma-csv).
5. Pour importer les données, cliquez sur _Confirmer_{:.doc-button}.

Une fois les données traitées, vous pouvez {% link_new ajouter les files d’attente à un workload | features/forecast/injixo-forecast/manage-workloads.md %} dans injixo Forecast. La taille de fichier maximum est 7&nbsp;Mo.

## Foire aux questions

| Question                                                                  | Réponse                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Est-il possible d’importer deux fois le même fichier&nbsp;?                                         | Oui, si vous importez des données manuellement. Non, si vous utilisez Cloud Link. Non. Pour détecter les doublons, injixo calcule les sommes de contrôle pendant l’import. Les fichiers importés avec la même somme de contrôle ne seront pas importés à nouveau. Si le fichier a le même nom mais un contenu différent, il sera importé. |
| Les fichiers CSV importés automatiquement seront-ils supprimés d’injixo après l’import&nbsp;? | Non. Les fichiers importés resteront dans le dossier du client injixo Cloud Link. Vous pouvez les supprimer manuellement ou configurer une tâche récurrente.                                                                                                                                              |
| Est-il possible d’importer un fichier CSV contenant des données futures&nbsp;?                        | Oui, mais il est recommandé d’éviter d’importer des fichiers contenant des données futures. injixo n’ignore pas les données futures, mais les conserve comme données historiques. Vous pouvez toujours calculer des prévisions mais les graphiques d’historique et de prévision seront superposés.                                               |
