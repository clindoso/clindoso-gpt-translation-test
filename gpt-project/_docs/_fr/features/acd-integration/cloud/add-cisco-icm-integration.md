---
title: Ajouter une intégration Cisco ICM
description: Connectez votre système Cisco ICM à injixo et utilisez les données importées dans injixo Intraday
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

L’intégration Cisco ICM importe les données d’adhérence en temps réel. Cette intégration utilise {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Ajouter une intégration Cisco ICM

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Cisco ICM**, cliquez sur _Ajouter cette intégration_{:.doc-button}.

## Configurer votre intégration Cisco ICM

1. Entrez un **Nom** unique permettant d’identifier la source de données.
2. Dans la section **injixo Cloud Link**, cliquez sur le **lien de téléchargement** pour votre système d’exploitation.<br>
> Remarque
> 
> Si vous avez déjà téléchargé Cloud Link pour une autre intégration, vous devez quand même télécharger la version spécifique à Cisco à partir de cette page.
3. Installez et connectez {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.<br>
4. Dans la section **Configuration**, paramétrez votre intégration&nbsp;:
 - Entrez une chaîne de connexion avec les paramètres requis pour connecter votre base de données Cisco&nbsp;:
`DRIVER={MS SQL Server};Server=myServerAddress;Database=myDataBase;UserId=myUsername;Password=myPassword;`
 - Sélectionnez le **Fuseau horaire de votre base de données** depuis le menu déroulant.
 - Entrez l’**ID client** de votre Cisco ICM et votre **mot de passe**.
 - Entrez votre **Passerelle périphérique 1**.
 - (Facultatif) Entrez votre **Passerelle périphérique 2**.
4. Cliquez sur _Sauvegarder l’intégration_{:.doc-button}.

injixo commencera à importer les données d’adhérence en temps réel, mais les données ne seront visibles qu’après avoir mappé les identifiants utilisateur externes à vos employés.

## Mapper des utilisateurs externes à vos employés

1. Accédez à _WFM > Administration > Planification > Employés_{:.breadcrumbs}.
2. Mappez les identifiants utilisateur externes à vos employés.

> Remarque
>
> Les identifiants utilisateur externes sont les identifiants Unified CCE Skill Target.

En savoir plus sur le {% link_new mapping des identifiants utilisateur externes | features/acd-integration/cloud/import-agent-status-data.md | #mapper-les-identifiants-utilisateur-externes-aux-employés-dans-injixo %} aux employés.

## Mapper les statuts agents aux activités dans injixo

1. Accédez à _WFM > Administration > Planification > Activités_{:.breadcrumbs}.
2. Mappez les activités de Cisco ICM aux activités dans injixo.

En savoir plus sur le {% link_new mapping des activités externes | features/acd-integration/cloud/import-agent-status-data.md | #réassigner-les-activités-du-système-externe %} aux activités dans injixo.