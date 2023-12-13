---
title: Ajouter une intégration Freshdesk
description: Découvrez comment connecter votre CRM Freshdesk à injixo pour importer des données.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

L’intégration Freshdesk est une intégration cloud permettant d’importer les volumes de contact pour les e-mails, les formulaires web, le Chat, et les messageries de réseaux sociaux.

Vous débutez avec les intégrations&nbsp;? Commencez avec les {% link_new concepts fondamentaux | features/acd-integration/cloud/how-integrations-work.md %}.

## Ajouter une intégration Freshdesk

1. Accédez à _Account > Intégrations_{:.breadcrumbs}.
2. Si une intégration est déjà présente, cliquez sur _Ajouter une intégration_{:.doc-button}.
3. Dans la section **Freshworks**, cliquez sur _Sélectionner le modèle_{:.doc-button}.
4. Dans la section Freshdesk, cliquez sur _Ajouter cette intégration_{:.doc-button}.

## Configurer votre intégration Freshdesk

1. Saisissez un nom unique permettant d’identifier la source de données.
2. Dans la section **Identifiants**, saisissez votre nom de domaine Freshdesk complet, en incluant le sous-domaine, par exemple exemple.freshdesk.com.
3. Accédez à Freshdesk et copiez une clé API valide d’un utilisateur ayant le rôle Account Administrator.
4. Retournez à injixo et collez la clé API dans le champ **Clé API**.
5. Cliquez sur _Sauvegarder l’intégration_{:.doc-button}. 

## Installer l’application injixo

L’intégration Freshdesk nécessite une application client. Une fois que vous avez enregistré votre configuration, vous pouvez accéder à la section **Installer l’application injixo** en bas de la page.

Pour générer et copier la **clé API injixo**, cliquez sur _Générer_{:.doc-button}.

Pour paramétrer l’application injixo dans votre compte Freshdesk, suivez les instructions à l’écran. Pour en savoir plus, reportez-vous à [Freshworks marketplace](https://www.freshworks.com/apps/freshdesk/injixo_connect).

## Données Freshdesk dans injixo

injixo importe toutes les données de ticket depuis Freshdesk. Les tickets contiennent généralement plusieurs conversations qui ont lieu entre les conseillers et les clients.<br>
Remarque&nbsp;: injixo ne peut pas importer la durée des tickets depuis Freshdesk. Vous ne pourrez donc pas voir le graphique du TMT pour les workloads avec des files d’attente Freshdesk dans injixo Forecast.

### Tickets et conversations

Dans injixo, toutes les conversations sont regroupées par canal de communication Freshworks (Source). Une conversation peut être un nouveau ticket ou une réponse à un ticket existant.

Dans injixo, toutes les conversations d’un ticket Freshdesk sont comptées séparément en tant que contact reçu.

Exemple&nbsp;: un utilisateur ouvre un ticket en envoyant un e-mail. Le conseiller répond ensuite et ferme le ticket. Deux jours plus tard, le ticket est rouvert en raison d’un nouvel e-mail, ce qui crée une nouvelle conversation.

Le nombre de contacts reçus dans injixo sera généralement plus élevé que le nombre de tickets enregistrés dans Freshdesk.

### Événements de différentes sources

Dans un ticket Freshdesk, les réponses peuvent être suivies dans différentes files d’attente d’injixo à l’aide du canal Cas.

Exemple&nbsp;: lorsque la réponse à un ticket se fait par e-mail, vous verrez le contact dans une file d’attente d’injixo correspondant au groupe Freshdesk et au nom de la source. Une conversation par Chat dans le même ticket sera comptée dans une file d’attente distincte.

### Convention d’affectation des noms des files d’attente

injixo crée des files d’attente source à partie de vos tickets. La convention d’affectation des noms de ces files d’attente dépend du stade de l’import des données (initial ou continu). Au cours de cet import initial, les noms des files d’attente source suivront cette convention&nbsp;:

- "nom du groupe + nom de la source + Tickets"
- "nom du groupe + nom de la source + Replies"

Exemples&nbsp;:

- CustomerService chat Tickets
- CustomerService e-mail Replies
- Unknown group/source Tickets

Un nouveau ticket créera une nouvelle file d’attente. Une réponse à un ticket créera une file d'attente de réponses qui comptabilisera également les autres réponses. Pour obtenir toutes les informations d’un ticket, vous devez consulter à la fois le ticket et la file d'attente des réponses.

### Tickets supprimés et tickets indésirables

Le nom du groupe et de la source ne peuvent être déterminés lorsqu’un ticket déjà supprimé ou marqué comme indésirable est modifié. Les files d’attente source qui comptent ces tickets seront marquées Unknown group/source Tickets or Unknown group/source Replies. Ces files d’attente sont généralement sans importance pour la planification de la charge de travail des conseillers.
