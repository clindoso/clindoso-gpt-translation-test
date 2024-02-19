---
title: Ajouter une intégration Odigo
description: Découvrez comment connecter votre ACD Odigo à injixo pour importer des données.
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

L'intégration Odigo importe les statuts agent en temps réel et les données d’adhérence en temps réel.

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Ajouter une intégration Odigo

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Odigo**, cliquez sur _Ajouter cette intégration_{:.doc-button}.
4. Entrez un nom unique permettant d’identifier la source de données.
5. Dans les sections **Identifiants** et **Données sur les contacts**, renseignez tous les champs obligatoires.
6. (Facultatif) Configurez l’importation des statuts agent pause détaillés&nbsp;:
- Cochez la case **Importer les statuts agent de pause détaillés**.<br>
  Lors de l’importation des statuts pause, injixo inclura des informations sur le type de pause prise.<br>
  Remarque&nbsp;: si vous cochez cette case, vous devez également mettre à jour le {% link_new mapping des activités externes | features/acd-integration/cloud/import-agent-status-data.md | #réassigner-les-activités-du-système-externe %}.
- Saisissez votre URL Odigo comprenant l’identifiant du tenant.
- Entrez le nom d’utilisateur et le mot de passe pour le service web.
7. Cliquez sur _Sauvegarder l’intégration_{:.doc-button}.

## Configurer votre intégration Odigo

1. Dans la section **Générer un jeton d’URL injixo**, cliquez sur _Générer_{:.doc-button}.
2. Copiez le jeton d’URL injixo dans votre presse-papiers.<br>
Le jeton d’URL injixo ne s’affiche qu’une seule fois. Si vous ne pouvez pas terminer votre configuration immédiatement, sauvegardez-le dans un endroit sûr, par exemple dans un gestionnaire de mots de passe.
3. Dans la section Administration de votre interface Odigo, activez l’envoi de notifications vers un serveur externe. Pour ce faire, contactez Odigo.
4. Collez le **jeton d'URL injixo** copié comme URL de notification.
5. Enregistrez vos paramètres dans Odigo et retournez dans injixo.

Pour activer l’intégration, vous devez redémarrer le serveur. Pour ce faire, contactez Odigo.<br>
injixo commencera alors à importer les données d’adhérence en temps réel, mais les données ne seront visibles qu’après avoir mappé les identifiants utilisateur externes à vos employés.

## Associer des utilisateurs externes à vos employés

1. Accédez à _WFM > Administration > Planification > Employés_{:.breadcrumbs}.
2. Mappez les identifiants utilisateurs externes à vos employés.

En savoir plus sur le {% link_new mapping des identifiants utilisateur externes | features/acd-integration/cloud/import-agent-status-data.md | #mapper-les-identifiants-utilisateur-externes-aux-employés-dans-injixo %} aux employés.

## Mapper les statuts agent aux activités dans injixo

1. Accédez à _WFM > Administration > Planification > Activités_{:.breadcrumbs}.
2. Mappez les activités d’Odigo avec les activités d’injixo.

En savoir plus sur le {% link_new mapping des activités externes | features/acd-integration/cloud/import-agent-status-data.md | #réassigner-les-activités-du-système-externe %} aux activités dans injixo.
