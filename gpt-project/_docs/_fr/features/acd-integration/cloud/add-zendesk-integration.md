---
title: Ajouter une intégration Zendesk
description: Découvrez comment connecter votre CRM Zendesk à injixo pour importer des données.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

L’intégration Zendesk est une intégration cloud permettant d’importer les volumes de contact pour les e-mails, les formulaires web, le Chat, et les messageries de réseaux sociaux de Zendesk Support et Zendesk Talk. 

L’intégration importe uniquement les appels entrants (mais pas les appels sortants). Les données de temps moyen de traitement (TMT) sont uniquement disponibles pour Zendesk Talk.

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Ajouter une intégration Zendesk

Dans votre compte Zendesk, créez un jeton API pour un utilisateur disposant de [droits admin](https://support.zendesk.com/hc/fr/articles/4408843355290-Int%C3%A9gration-Zendesk-pour-Salesforce-Permissions-de-profil-requises).

Pour ajouter une intégration Zendesk dans injixo, suivez les étapes ci-dessous&nbsp;:

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Zendesk**, cliquez sur _Ajouter cette intégration_{:.doc-button}.
4. Entrez un nom unique permettant d’identifier la source de données.
5. Dans la section **Identifiants de l’utilisateur**, entrez vos identifiants Zendesk&nbsp;:
   * Saisissez votre nom de domaine Zendesk complet, en incluant le sous-domaine, par exemple&nbsp;: exemple.zendesk.com.
   * Saisissez votre nom d’utilisateur Zendesk.
   * Entrez votre jeton API.
6. Dans la section **Configuration**, choisissez une stratégie de regroupement. Sélectionnez l’option **SVI (Serveur vocal interactif)** ou **Numéro de téléphone**. La stratégie permet de déterminer le nom donné par injixo aux [files d’attente source créées](#noms-des-files-dattente-pour-zendesk-talk) pour les vues Zendesk Talk. L’option SVI utilise le groupe de destination. L’option Numéro de téléphone utilise le numéro de réception pour générer le nom de la file d’attente. Un appel sans les informations nécessaires apparaîtra comme non groupé. Les files d’attente source pour Zendesk Support ne sont pas affectées.

   > Une fois la configuration de l’intégration sauvegardée dans injixo, vous ne pourrez plus modifier la stratégie de regroupement.

7. Cliquez sur _Sauvegarder l’intégration_{:.doc-button}.

## Données Zendesk dans injixo

### Tickets et événements de contact

Dans Zendesk, un ticket contient généralement plusieurs interactions entre les membres de votre équipe et vos clients via différents canaux de communication.

Chaque interaction représente une tâche à prendre en charge par les membres de votre équipe. Une interaction peut être un nouveau ticket ou une modification d’un ticket existant.

Exemple&nbsp;: un utilisateur ouvre un ticket en créant un e-mail.  Le membre de l’équipe répond ensuite et ferme le ticket. Deux jours plus tard, l’utilisateur envoie un autre e-mail pour répondre au membre de l’équipe, ce qui rouvre le ticket. Dans injixo, deux e-mails sont comptés, bien qu’ils fassent partie du même ticket.

### Vues

injixo crée les files d’attente source selon vos vues Zendesk. Après l’import de données initial, vous verrez une file d’attente source pour chaque vue prise en charge que vous avez créée dans Zendesk. Si une vue contient des événements de différents canaux (par exemple, Chat et e-mail), ceux-ci apparaîtront dans des {% link_new canaux | features/forecast/injixo-forecast/manage-workloads.md | #files-dattente-et-canaux %} différents dans injixo.

Remarque&nbsp;: si vous ajoutez de nouvelles vues Zendesk après avoir sauvegardé l’intégration, de nouvelles files d’attente source seront générées automatiquement dans injixo, ainsi que l’historique correspondant.

### Vues non prises en charge

injixo peut créer des files d’attente source pour la plupart des vues, mais ne prend actuellement pas en charge les vues qui utilisent les champs de ticket suivants&nbsp;:

- Horaires d’ouverture
- SLA
- Média
- Compétences
- Conditions avec des valeurs spécifiques à l’utilisateur (par exemple, la personne affectée est (utilisateur actuel))

Si certaines de vos vues ont des conditions faisant référence à au moins l’un des champs ci-dessus, injixo ignorera ces vues et ne créera pas de files d’attente pour celles-ci.

### Mapping des canaux Zendesk dans injixo

La modification d’un événement dans un ticket Zendesk peut être comptée dans plusieurs canaux dans injixo.

Exemple&nbsp;: un e-mail créera un ticket qui s’affichera dans une file d’attente d’e-mails dans injixo. Si ce même ticket est intégré dans une vue de chat, il sera également compté dans une file d’attente de chat dans injixo.

| Canal Zendesk                           | injixo       |
| ----------------------------------------- | ------------ |
| email                                     | email        |
| mobile                                    | email        |
| web                                       | email        |
| chat                                      | chat         |
| native_messaging                          | chat         |
| sms                                       | social_media |
| any_channel                               | social_media |
| facebook                                  | social_media |
| twitter                                   | social_media |
| sunshine_conversations_facebook_messenger | social_media |
| instagram_dm                              | social_media |
| voice                                     | call         |
| api                                       | case         |
| answer_bot_for_web_widget                 | case         |
| chat_transcript                           | case         |
| mobile_sdk                                | case         |

### Noms des files d’attente pour Zendesk Support

Le nom de la file d’attente source créée pour les files d’attente Zendesk Support suivent la convention suivante&nbsp;: 

"nom de vue + (canal injixo)"

Exemples&nbsp;:

- Tickets de support (chat)

### Noms des files d’attente pour Zendesk Talk

Le nom de la file d’attente source créée pour les files d’attente Zendesk Talk suivent la convention suivante&nbsp;: 

"Calls Inbound For + stratégie de regroupement"

Exemples&nbsp;:

- Calls Inbound For +49123456789 (Numéro de téléphone)
- Calls Inbound For Senior Agents (SVI)
- Calls Inbound Ungrouped
