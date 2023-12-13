---
title: Utilisation de l'API injixo
product_label:
  - advanced
  - enterprise
redirect_from:
  - /fr/api-utilisation/
redirect_reason: Updated filename on 21 April 2022
---

injixo intègre une API qui permet d'exporter les données de votre application injixo.

> **Changement d'URL** : l'API est désormais accessible via legacy-api.injixo.com
>
> Nous allons bientôt remplacer l'ancienne URL pour accéder à l'API. Elle est désormais accessible via legacy-api.injixo.com. L'ancienne URL reste temporairement valide, vous avez ainsi le temps de modifier vos requêtes existantes.

## Description de L'API

La description complète de l'API et des endpoints disponibles sont consultables à l'adresse https://legacy-api.injixo.com. Cliquez sur un endpoint pour afficher les paramètres et les valeurs possibles de retour.

{{ 1 | image: "endpoint API injixo" }}

## Générer un jeton d'accès personnel

Un jeton d'accès personnel est nécessaire pour utiliser l'API injixo. Les étapes suivantes vous montrent comment créer un jeton d'accès personnel (uniquement disponible pour les utilisateurs disposant du rôle Admin) :

1. Connectez-vous à injixo et cliquez sur votre nom en haut à droite de l'écran pour accéder au détail de votre **profil**.
2. Cliquez sur le menu **Jetons d'accès personnels**.
3. Cliquez sur *Ajouter un jeton*{:.doc-button}
4. Renseignez une **description** pour ce jeton.
5. Cliquez sur *Générer le jeton*{:.doc-button}.
6. Copiez le jeton généré puis cliquez sur *Fait*{:.doc-button}.

{{ 2 | image: "endpoint API injixo" }}

Sauvegardez le jeton d'accès qui vient d'être généré car celui n’apparaît qu’une fois.

> Remarque
> 
> Si les droits *Admin* sont supprimés du compte utilisateur, ou si l'utilisateur est bloqué ou supprimé, tous les jetons liés à ce compte seront automatiquement désactivés.

### Accéder à l’API injixo avec votre jeton d'accès

Une fois le jeton d'accès personnel généré, une application tierce est nécessaire pour extraire les données depuis injixo. Il peut s'agir d'un outil de Business Intelligence (PowerBI par exemple), d'une application du type [Advanced Rest Client](https://install.advancedrestclient.com/install) (ARC) ou encore d'une extension sur votre navigateur. L'application doit être capable de gérer l'en-tête *authorization: Bearer*.

L'exemple suivant vous montre comment extraire des données relatives aux employés à l'aide de l'application [Advanced Rest Client](https://install.advancedrestclient.com/install).

Le endpoint vous permettant d'extraire les données relatives aux employés est : https://legacy-api.injixo.com/v1/employees. Pour extraire les données remplissez l'application ARC comme suit :

{{ 3 | image: "ARC example" }}

### Formats d'export

Plusieurs formats d'export de données sont disponibles dans l'API injixo : JSON, CSV ou XML. L'extension ajoutée à l’URL du Endpoint conditionne le format d'export, par exemple *https://legacy-api.injixo.com/v1/activities.xml* exportera les données relatives au activités au format XML. Si aucun format n'est spécifié, la valeur par défaut est JSON.

### Champs Path parameters et Query parameters

Des paramètres spécifiques peuvent être ajoutés à la fin de l'URL pour n'extraire que les données souhaitées ou n'afficher que certains résultats :

- Path parameters : ces paramètres sont obligatoires pour extraire les données spécifiques au Endpoint. Ce sont par exemple des ID ou des dates. Attention, s'il s'agit de dates, le format est obligatoirement **YYYY-MM-DD**.
- Query parameters : ces paramètres sont optionnels et permettent de compléter l'URL en limitant l'affichage des résultats. Utiliser le **?** pour le premier paramètre et **&** pour les suivants.

{{ 4 | image: "path and query parameters" }}

**Exemple :**
Le Endpoint suivant permet d'extraire les données de planning de l'*unité opérationnelle* ID 1001 pour la période allant du 01/11/2021 au 15/11/2021 sur la Catégorie *Planning* :
**https://legacy-api.injixo.com/v1/planning_units/1001/planning_units/2021-11-01?level=schedule&end_date=2021-11-15**

Ici, les *Path parameters* sont l'ID de l'unité opérationnelle (1001) et la date de début (2021-11-01) et les *Query parameters* sont la catégorie (level=schedule) et la date de fin de la période (end_date=2021-11-15).

## Utiliser cURL

[cURL](https://curl.haxx.se) est une interface en ligne de commande, destinée à récupérer le contenu d'une ressource via une URL.

Par exemple,

**curl -H "Content-Type: application/json" -H "Authorization: Bearer MmU5OTM4MTAzMWfakeVjYWU4NjViOGRhZWU3ZTU2NTc=" https://legacy-api.injixo.com/v1/employees**

retournera :

**{"employees":[{"birth_date":"1900-01-01", "birth_place":"", "color":13026816, "current_identification":"", "deleted":false, "employee_id":1001, "last_name":"Martin", "first_name":"Gabriel", "personnel_number":"1001", "schedule_position":0, "automated_shift_assignment":true}]}**

Ajouter l’extension *.csv*, comme dans l’exemple suivant :

**curl -H "Content-Type: application/json" -H "Authorization: Bearer MmU5OTM4MTAzMWfakeVjYWU4NjViOGRhZWU3ZTU2NTc=" https://legacy-api.injixo.com/v1/employees.csv**

retournera :

**automated_shift_assignment;birth_date;birth_place;color;current_identification;deleted;employee_id;first_name;last_name;personnel_number;schedule_position
true;1900-01-01;"";13026816;"";false;1001;Gabriel;Martin;1001;0**

## Comment créer des rapports personnalisés ?

Pour créer vos rapports personnalisés, il est nécessaire de comprendre comment vos données métier sont structurées dans injixo. l'API injixo suit simplement la structure du modèle de données injixo (par exemple : les employés sont affectés à une unité opérationnelle).

Vous trouverez ci-dessous les étapes à suivre pour créer vos rapports :

1. Définissez le périmètre de votre rapport.
2. Identifiez les données pertinentes dans injixo.
3. Identifiez les endpoints.
4. Requêtez les données.
5. Traitez les résultats dans l'outil de votre choix.

Si vous souhaitez par exemple savoir quels employés sont planifiés sur une période donnée, exportez les informations du Endpoint `/schedules` pour récupérer les horaires et activités de chaque employé. Exportez également les données depuis `/activities` et `/employees` pour les combiner à la requête initiale et avoir le nom des activités et des employés au lieu des ID.
