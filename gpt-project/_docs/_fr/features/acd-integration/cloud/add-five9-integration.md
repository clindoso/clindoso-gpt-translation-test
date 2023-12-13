---
title: Ajouter une intégration Five9
description: Connectez votre ACD Five9 à injixo et préparez un rapport personnalisé pour regrouper les files d’attente par compétences.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from: /fr/five9-grouping-by-skills/
redirect_reason: renamed file in June 2021
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Une intégration Five9 est une intégration cloud permettant d’importer les données d’appels, les statuts agent et les données d’adhérence en temps réel.

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Prérequis

Si vous regroupez vos files d’attente par campagne, l’intégration lit le journal d’appels standard de Five9.

Si vous regroupez vos files d’attente par compétence, l’intégration lit un journal d’appels personnalisé de Five9 qui inclut les compétences. Pour importer les données depuis les files d’attente regroupées par compétences, suivez les étapes ci-dessous dans Five9&nbsp;:

 1. Créez un nouveau dossier partagé pour les rapports.
 2. Personnalisez le journal des appels standard pour y inclure la colonne «&nbsp;SKILL&nbsp;».
 3. Sauvegardez et nommez le rapport personnalisé «&nbsp;Call Log with Skills&nbsp;» dans le dossier partagé.

Pour en savoir plus sur la personnalisation des rapports, veuillez consulter le Help Center Five9.

## Ajouter votre intégration Five9

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Five9**, cliquez sur _Ajouter cette intégration_{:.doc-button}.
4. Entrez un nom unique permettant d’identifier la source de données.
5. Entrez le nom d’utilisateur et le mot de passe pour un utilisateur avec un accès admin dans votre compte Five9.
6. Dans la section **Configuration**, sélectionnez la région de votre compte et l’option de regroupement.
7. Cliquez sur _Sauvegarder l’intégration_{:.doc-button}.

La nouvelle intégration importe désormais les données dans injixo. Le premier import peut prendre jusqu’à 15&nbsp;minutes. Toutes les files d’attente du système connecté seront automatiquement disponibles pour le mapping sur la {% link_new page de configuration des Workloads | features/forecast/injixo-forecast/manage-workloads.md | #créer-un-workload %} dans injixo Forecast.

## Que se passe-t-il en cas d’états agent parallèles&nbsp;?

Les rapports Five9 contiennent parfois plusieurs états pour un agent à la même heure, par exemple&nbsp;:

| État   | Heure de début | Heure de fin |
| ------- | ---------- | -------- |
| Prêt   | 13:00:00   | 13:00:05 |
| Entrant | 13:00:00   | 13:03:00 |

Pour éviter qu’un état remplace l’autre, l’intégration modifie le début de l’état le plus long. Le début de l’état le plus long devient la fin de l’état le plus court&nbsp;:

| État   | Heure de début | Heure de fin |
| ------- | ---------- | -------- |
| Prêt   | 13:00:00   | 13:00:05 |
| Entrant | 13:00:05   | 13:03:00 |
