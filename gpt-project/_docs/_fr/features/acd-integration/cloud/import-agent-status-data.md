---
title: Importer les statuts agent
product_label:
  - advanced
  - enterprise
  - classic
description: Configurez injixo pour importer les données de statut agent.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-on-premise-integration.md
---

Les systèmes externes, comme les ACD, enregistrent le passage d’une activité à l’autre par les employés. injixo utilise ces données dans la Gestion intrajournalière.

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Prérequis

Pour importer les données de statut agent, vous devez {% link_new ajouter une intégration | features/acd-integration/cloud/how-integrations-work.md %}. L’intégration doit prendre en charge l’import des statuts agent.

Pour vérifier si votre intégration prend en charge l’import des statuts agent, accédez à _Account > Intégrations_{:.breadcrumbs}. Les intégrations affichent les labels Statut agent (données historiques) et/ou Adhérence Temps Réel.

Après avoir ajouté l’intégration, vous devez ajouter des identifiants utilisateur externes aux employés dans injixo. Vous pouvez également réassigner les activités du système externe aux mêmes activités dans injixo.

## Identifiants utilisateur externes

Les identifiants utilisateur externes sont spécifiques au système externe. Ils identifient les utilisateurs dans le système externe par une adresse e-mail, un nom d’utilisateur ou un identifiant agent.

Pour éviter l’échec des imports, vérifiez que l’orthographe, les majuscules et minuscules, ainsi que les espaces sont corrects.

| Fournisseur                 | Identifiant utilisateur requis              |
| ---------------------- | ------------------------------------- |
| Five9                  | nom d’utilisateur Five9                  |
| Genesys Cloud          | nom d’utilisateur PureCloud              |
| Genesys Engage         | nom d’utilisateur PureEngage             |
| Talkdesk               | adresse e-mail utilisée dans Talkdesk        |
| UJET                   | adresse e-mail utilisée dans UJET            |
| Sikom                  | nom d’utilisateur Sikom                  |
| Mitel MiVoice Business | nom d’utilisateur Mitel MiVoice Business |
| Vonage                 | identifiant agent Vonage                  |
| Avaya CMS              | nom d’utilisateur Avaya CMS              |

## Mapper les identifiants utilisateur externes aux employés dans injixo

Pour importer des données, vous devez ajouter des identifiants utilisateur externes aux employés. Vous pouvez les ajouter à tous les employés ou seulement à ceux dont vous souhaitez importer les données de statut agent.

1. Accédez à _WFM > Administration > Planification > Employés_{:.breadcrumbs} et sélectionnez un employé.
2. En haut à droite, cliquez sur **Systèmes externes**, ou faites défiler vers le bas jusqu’à la section **Systèmes externes**.
3. Cliquez sur l’icône Ajouter {% icon item-add | icon-only %} pour ajouter un système externe.  
   Une fenêtre s’ouvre.
4. Dans le menu déroulant **Système externe**, sélectionnez l’intégration que vous avez précédemment configurée.
5. Dans le champ **ID de l’employé dans le système externe**, ajoutez un numéro unique pour l’employé, par exemple le matricule de l’employé.
6. Dans le champ **Extension**, saisissez l’identifiant utilisateur de l’employé dans le système externe, par exemple l’adresse e-mail de l’employé.
7. Cliquez sur _OK_{:.doc-button}.

Après avoir mis à jour les sections des employés, la prochaine importation importera les données de statut des agents.


## Réassigner les activités du système externe

Les activités du système externe sont les activités enregistrées par le système externe lorsque les employés se connectent, se déconnectent ou passent d'une activité à une autre, par exemple des e-mails aux appels.

Vous pouvez réassigner les activités du système externe aux activités existantes. Si vous décidez de {% link_new créer de nouvelles activités | features/administration/activities.md | #créer-une-activité %}, assurez-vous de les ajouter à votre {% link_new unité opérationnelle | features/administration/create-and-manage-planning-units.md | #ajouter-des-activités %} pour les afficher correctement ultérieurement.

Par défaut, les intégrations placent ces activités dans l’activité Présent (ID 1) et le statut agent sera affiché comme Présent pour toutes les activités. injixo peut afficher les mêmes activités que votre système externe. Pour ce faire, vous devez réassigner les activités du système externe à d’autres activités injixo en suivant les étapes ci-dessous.


Pour remapper une activité&nbsp;:

1. Accédez à _Plan > Configuration > Activités_{:.breadcrumbs}.
2. Sélectionnez l’activité que vous souhaitez remapper.
3. Dans la section **Systèmes externes**, cliquez sur _Modifier dans WFM_{:.doc-button}.
4. Accédez à la section **Systèmes externes**.
5. Cliquez sur l’icône Ajouter {% icon item-add | icon-only %}.

6. Dans la fenêtre **Systèmes externes**&nbsp;:<br>
   - Dans le menu déroulant **Système externe**, sélectionnez votre intégration.
   - Dans le menu déroulant **ID de l’activité du système externe**, sélectionnez l’activité du système externe que vous souhaitez mapper à l’activité injixo actuellement sélectionnée.
   - Dans le menu déroulant **Classification**, sélectionnez la valeur 1.
7. Cliquez sur _OK_{:.doc-button}.

Pour remapper d’autres activités, cliquez sur l’activité suivante et procédez à partir du menu de configuration sur la droite.



Lorsque vous avez terminé le mapping des activités, accédez à _Account > Intégrations_{:.breadcrumbs} et cliquez sur l’icône Reprendre l’import {% icon play_circle | icon-only %} à côté de votre intégration pour reprendre l’import des données.
