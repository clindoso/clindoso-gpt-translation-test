---
title: Een Freshchat-integratie toevoegen
description: Lees hoe je je Freshchat-CRM verbindt met injixo om gegevens te importeren.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
redirect_from:
  - nl/add-freshdesk-messaging-integration/
redirect_reason: Updated filename on 15 September 2023
---

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Een Freshchat-integratie toevoegen

Om in injixo een nieuwe Freshchat-integratie toe te voegen, heb je een Freshchat Pro- of Enterprise-account nodig.

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Freshworks**-tegel op _Kies een model_{:.doc-button}.
4. Klik in de sectie **Freshchat** op _Voeg integratie toe_{:.doc-button}.

## Je Freshchat-integratie configureren

1. Geef de nieuwe integratie een unieke naam die naar de gegevensbron verwijst.
2. Voer in de sectie **Toegangsgegevens** je volledige Freshchat-domeinnaam met subdomein in, bijvoorbeeld: example.freshchat.com.
3. Ga naar Freshchat en kopieer een geldige API-key van een gebruiker met de rol Account Administrator.
4. Ga terug naar injixo en plak de API-key in het veld **API-key**.
5. Klik op _Integratie opslaan_{:.doc-button}.

### De injixo-app installeren

Voor de Freshchat-integratie is een clienttoepassing nodig. Ga nadat je de configuratie hebt opgeslagen verder met de sectie **Installeer injixo app**.

Genereer en kopieer hier de **injixo API-key**.

Volg de instructies op het scherm om de injixo-app in je Freshchat-account te configureren. Ga voor meer informatie naar de [Freshworks marketplace](https://www.freshworks.com/apps/injixo_connect).

## Freshchat-gegevens in injixo

### Contacten

In Freshchat bestaat een chat meestal uit verschillende gesprekken die plaatsvinden tussen je teamleden en je klanten. In injixo telt elke afgesloten chat als een contact, ongeacht het aantal gesprekken.

Voorbeeld: Een klant begint een chat op de website. Een medewerker van het contactcenter reageert hierop, maar lost het probleem pas een dag later op, omdat er meer informatie nodig was. In injixo wordt dit als één contact gezien.

### Naamgevingsconventie bronqueue

De bronqueues die injixo aanmaakt op basis van je chats komen volgens de volgende conventie tot stand:

"groepnaam"

Voorbeelden:

- Customer Support
- Undefined_Queue

### Verwijderde chats en spamchats

Een chat kan worden verwijderd of als spam worden gemarkeerd wanneer deze is bijgewerkt. In dit geval kan de integratie geen groepnaam bepalen. De bronqueues die deze chats tellen, krijgen het label Undefined_Queue. Meestal zijn deze queues niet relevant voor het plannen van de workload van je medewerkers.

## Veelgestelde vragen

| Vraag                                                                                                                                                                       | Antwoord                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| injixo laat ineens geen nieuwe Freshchat-gegevens meer zien, maar op de pagina in **Account > Integraties**  is de status van mijn Freshchat-integratie nog steeds Operationeel. Wat kan ik doen? | De injixo-app haalt gegevens op uit Freshchat en stuurt gebeurtenissen naar injixo. Communicatiefouten tussen de injixo-app en injixo kunnen ertoe leiden dat gegevens uit Freshchat niet meer worden weergegeven. De Freshchat-integratie kan zulke communicatiefouten niet herkennen.<br><br>Controleer of de injixo API-key die je bij de configuratie van injixo in je Freshchat-account hebt ingevoerd nog geldig is. Als de API-key ongeldig is, vervang je de API-key op de app-installatiepagina in injixo. Als de API-key nog steeds geldig is, neem dan contact op met het supportteam van injixo. |
