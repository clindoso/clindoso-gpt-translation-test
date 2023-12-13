---
title: Comment fonctionnent les intégrations&nbsp;?
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Découvrez comment fonctionnent les intégrations, quelles sont les intégrations disponibles et comment les ajouter et les supprimer.
promote-service: acd-integration-support
redirect_from: /fr/cloud-overview/
redirect_reason: renamed file in June 2021
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Pour vous aider dans votre planification, injixo a besoin des données historiques de contact et les statuts agents de vos systèmes externes, comme votre système de téléphonie (ACD) ou votre outil de gestion clients (CRM). L’intégration avec votre ACD et/ou votre CRM permet à injixo de récupérer et de traiter vos données.

injixo propose des intégrations natives spécifiques à certains systèmes et des intégrations universelles, pour les systèmes on-premise et cloud. En fonction de l’intégration, injixo récupère des données toutes les 15, 30 ou 60&nbsp;minutes (import de données historiques), voire en quelques secondes (import de données en temps réel).


## Type d’intégration

Le type d’intégration détermine le mode de connexion d’injixo au système externe&nbsp;:

- Les intégrations cloud se connectent et importent directement des données à partir d’un système cloud, par exemple Five9 ou Vonage.
- Les intégrations on-premise utilisent {% link_new d’injixo cloud Link | features/acd-integration/cloud/install-cloud-link.md %} pour se connecter à un système de votre réseau local, par exemple Genesys Engage ou Sikom. Une fois connectée, l’intégration on-premise importera les données historiques sur 3 ans maximum.

## Intégrations spécifiques à certains systèmes et intégrations universelles

Les intégrations spécifiques à un système sont adaptées à ce système et doivent être le choix à privilégier. Si aucune intégration spécifique n’est disponible, vous pouvez également utiliser l’une des options d’intégration universelles&nbsp;:

- Base de données&nbsp;: intégration on-premise pouvant lire les données à partir d’une base de données à l’aide d’une requête SQL.
- CSV&nbsp;: intégration par fichier permettant d’importer des fichiers CSV à l’aide d’injixo cloud Link.
- API injixo&nbsp;: intégration cloud nécessaire à l’envoi de requêtes HTTP à l’API injixo.

## Quelles sont les données importées&nbsp;?

En fonction de l’intégration, injixo importe des données de contact et/ou les statuts agents&nbsp;:

- Les données de contact (appels, Chat, réseaux sociaux, tickets, e-mails, documents) contiennent les volumes d’appels reçus et répondus, ainsi que le temps moyen de traitement. Elles sont utilisées pour calculer les prévisions.
- Les données de statuts agents (connexion, déconnexion, clôture, pauses, etc.) contiennent des informations sur les activités des employés, comme le passage d’une activité à une autre. Elles sont utilisées en gestion intra-journalière.

## Ajouter une intégration

Pour en savoir plus sur la configuration de votre intégration, lisez les articles suivants&nbsp;:

- {% link_new Ajouter une intégration cloud | features/acd-integration/cloud/add-cloud-integration.md %}
- {% link_new Ajouter une intégration on-premise | features/acd-integration/cloud/add-on-premise-integration.md %}
- {% link_new Ajouter une intégration CSV | features/acd-integration/cloud/add-csv-integration.md %}
- {% link_new Ajouter une intégration via base de données | features/acd-integration/cloud/add-database-integration.md %}
- {% link_new Import de données via l’API injixo | features/acd-integration/cloud/import-data-with-injixo-api.md %}

Une fois que vous avez ajouté une intégration, celle-ci commence à envoyer les données à injixo.

Les données de contact sont importées automatiquement. Pour exploiter des données de contact, ajoutez les files d’attente importées à un (nouveau) Workload pour {% link_new calculer une prévision | getting-started/calculate-a-forecast.md %}. Calculez ensuite le besoin en personnel et générez votre planning.

> Prérequis pour afficher les données de statuts agents
>
> Pour voir les statuts agents dans Intraday, {% link_new mappez les identifiants utilisateur externes et les activités externes | features/acd-integration/cloud/import-agent-status-data.md %}. Pour ce faire, commencez par interrompre l’import de données de votre intégration.

<!-- add list of articles? or generic steps? -->

## Mettre en pause l’import de données

Une fois l’intégration paramétrée, un mapping initial des activités est mis en place. Pour conserver ce mapping et éviter de dupliquer des activités, mettez en pause l’intégration en cliquant sur l’{% icon pause_circle %} en face de l’intégration dans la vue d’ensemble.

Pour redémarrer l’intégration une fois que le mapping est réalisé, cliquez sur l’{% icon play_circle %}. Les données manquantes seront à nouveau importées.

## Supprimer une intégration

La suppression d’une intégration ne supprimera pas les données importées. Les files d’attente restent assignées à vos Workloads. Vous ne pouvez pas supprimer les files d’attente créées par une intégration.

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Cliquez sur l’{% icon pencil %} en face de l’intégration que vous souhaitez supprimer.
3. En bas à gauche, cliquez sur _Supprimer l’intégration_{:.doc-button}.
4. Dans la fenêtre de confirmation, cliquez sur _Supprimer l’intégration_{:.doc-button}.
