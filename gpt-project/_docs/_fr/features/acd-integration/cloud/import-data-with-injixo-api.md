---
title: Importer des données via l’API injixo
navigation_title: API injixo
product_label:
  - advanced
  - enterprise
description: Ajouter une intégration par API injixo pour importer les données de contact et les statuts agents depuis votre système externe.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/dashboards-overview.md
---

injixo utilise des intégrations spécifiques à certains systèmes et universelles pour importer les données de contact et les statuts agents depuis des systèmes externes. 

## Qu’est-ce qu’une intégration par API injixo&nbsp;?

Dans injixo Advanced WFM et Enterprise WFM, les intégrations par API injixo vous permettent d’envoyer des requêtes API pour importer des données (si aucune intégration standard n’existe pour votre système externe). Pour ce faire, l’API injixo propose les ressources suivantes&nbsp;:

- [Ressource pour les événements de contact](https://api.injixo.com/resources/integration_contact_event/)&nbsp;: les événements de contact sont importés lorsque des clients contactent votre organisation par téléphone, e-mail ou Chat. injixo stocke ces données dans des files d’attente regroupées par nom et par canal.
- [Statuts agent](https://api.injixo.com/resources/integration_agent_status/)&nbsp;: les statuts agents sont importés lorsque les employés de votre organisation passent d’une activité à l’autre. Par exemple&nbsp;: connexion, clôture ou déconnexion.

## Ajouter une intégration par API injixo

Les utilisateurs disposant d’un accès admin peuvent ajouter une intégration API injixo en suivant les instructions ci-dessous&nbsp;:

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Universal Interfaces**, cliquez sur _Sélectionner le modèle_{:.doc-button}.
4. Dans la section **injixo API**, cliquez sur _Ajouter cette intégration_{:.doc-button}.
5. Saisissez un nom unique pour la nouvelle intégration.
6. Cliquez sur **Sauvegarder l’intégration**.<br>La section **Accès à l’API injixo** devient disponible.
7. Pour générer la clé API injixo, cliquez sur _Générer_{:.doc-button}.

L’authentification fonctionne également avec les jetons d’accès personnels créés dans les profils utilisateur dans la section {% link_new **Jetons d’accès personnels** | features/reporting/injixo-api/injixo-api.md | #générer-un-jeton-daccès-personnel %}.

> Vous ne pouvez pas accéder à la clé API ultérieurement. 
>
> - Conservez la clé API en sécurité, par exemple dans votre gestionnaire de mots de passe.
> - La clé API actuelle expirera si un utilisateur crée une nouvelle clé API pour l’intégration ou supprime l’intégration.

## Import de données

Pour identifier l’intégration API et l’authentifier, incluez la clé API injixo et l’ID de configuration de l’intégration dans les requêtes API&nbsp;:

1. Ajoutez votre clé API à l’en-tête de requête Authorization.
2. Recherchez ou copiez votre identifiant de configuration de l’intégration&nbsp;:
    - Accédez à _Account > Intégrations_{:.breadcrumbs}.
    - Dans la section de votre intégration API, cliquez sur l’{% icon pencil %}.
    - Dans la section **Accès à l’API injixo**, cliquez sur _{% icon clone | icon-only %} Copier_{:.doc-button}.
3. Ajoutez l’ID de configuration de votre intégration à l’objet **meta** du corps de la requête.

Pour importer régulièrement des données de votre système externe vers injixo, exécutez votre propre application. Pour des exemples de scripts Ruby et Python, consultez les guides utilisateur dans la [documentation API injixo](https://api.injixo.com).

## Tester les imports de données

Pour tester l’intégration, vous pouvez envoyer des requêtes POST uniques à l’API. Le tableau de données dans les exemples ci-dessous contient un seul point de données. Vous pouvez le modifier si nécessaire. Remplacez au minimum l’exemple de clé API (abc123456=) et la valeur integrationConfigurationId (1234) avec les vôtres.

L’API supporte uniquement le protocole HTTPS. Envoyez vos requêtes à https://api.injixo.com pour éviter les erreurs `not_found`.

### cURL sur la ligne de commande

Les exemples suivants indiquent comment envoyer des données à l’API à l’aide de [cURL](https://curl.se/). cURL est un outil de ligne de commande qui échange des données avec un serveur via un terminal.

Événements de contact&nbsp;:

```
curl -X POST \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer abc123456=" \
 -d '{"data":[{"properties":{"offered":true,"handled":false,"duration":124.6},"queueName":"Level 1 support","queueIdentifier":"1337_99","timestamp":"2021-12-06T10:34:22Z","channel":"calls"}],"meta":{"integrationConfigurationId":1234}}' \
 https://api.injixo.com/external-systems/contact-events
```

Remarque&nbsp;: chaque nouvelle combinaison de `queueIdentifier`, `queueName` et `integrationConfigurationId` créera une file d’attente. Pour éviter les doublons de noms de file d’attente, assurez-vous d’ajouter le même queueIdentifier ou le même integrationConfigurationId pour chaque requête avec le même nom de file d’attente. 

Statuts agents&nbsp;:

```
curl -X POST \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer abc123456==" \
 -d '{"data":[{"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2021-12-06T10:00:00Z","endTime":"2021-12-06T15:00:00Z"}],"meta":{"integrationConfigurationId":8431,"externalSystem":"My ACD"}}' \
 https://api.injixo.com/external-systems/agent-statuses
```

### Clients REST

Les exemples suivants indiquent comment envoyer des données à l’API à l’aide d’un client REST, comme [Postman](https://www.postman.com/downloads/).

1. Ajoutez un en-tête de requête JSON&nbsp;:

   ```
   {
  "Content-type": "application/json",
  "Authorization": "Bearer abc123456="
}
   ```

2. Ajoutez un corps de requête JSON différent pour les événements de contact et les données de statut agent.<br><br>

   Exemple de corps de requête pour les événements de contact&nbsp;: `/external-systems/contact-events`

   ```
   {
  "data": [
    {
      "properties": { "offered": true, "handled": false, "duration": 124.6 },
      "queueName"&nbsp;: "Level 1 support",
      "queueIdentifier": "1337_99",
      "timestamp": "2021-12-06T10:34:22Z",
      "channel": "calls"
    },
    {
      "properties": { "offered": true, "handled": true, "duration": 200.1 },
      "queueName"&nbsp;: "Level 1 support",
      "queueIdentifier": "1337_99",
      "timestamp": "2021-12-06T10:46:22Z",
      "channel": "calls"
    }
  ],
  "meta": { "integrationConfigurationId": 1234 }
}
   ```

   Exemple de corps de requête pour les statuts agent&nbsp;: `/external-systems/agent-statuses`

   ```
   {
  "data": [
    {"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2022-12-06T08:00:00Z","endTime":"2022-12-06T13:00:00Z"},
    {"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2022-12-07T09:00:00Z","endTime":"2022-12-07T10:00:00Z"}
  ],
  "meta": {
    "integrationConfigurationId": 1234
    "externalSystem": "My ACD"
  }
}
   ```

## Votre première requête API - Et ensuite&nbsp;?

Une fois que vous avez envoyé une requête API, vous pourrez voir les données dans injixo après un temps d’attente. Vous pouvez utiliser les données importées de la manière suivante&nbsp;:

- Requêtes pour les événements de contact&nbsp;: dans Forecast, les pages Créer un workload et Éditer le workload afficheront les files d’attente importées lorsque les données ont été traitées.
- Requêtes pour les statuts agents&nbsp;: la première requête avec de nouveaux identifiants agent n’importera pas de données réelles de statut agent dans le Centre de planification. Pour voir les données, {% link_new mappez au moins un identifiant externe | features/acd-integration/cloud/import-agent-status-data.md | #mapper-les-identifiants-utilisateur-externes-aux-employés-dans-injixo %} (envoyé comme agentIdentifier) à un employé. Vous devez envoyer une autre requête pour afficher les données.
