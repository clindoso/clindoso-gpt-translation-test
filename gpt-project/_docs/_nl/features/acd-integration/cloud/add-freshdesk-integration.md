---
title: Een Freshdesk-integratie toevoegen
description: Lees hoe je je Freshdesk-CRM verbindt met injixo om gegevens te importeren.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Een Freshdesk-integratie is een cloudintegratie die contactvolumes importeert voor e-mail, webformulieren, chat en sociale mediaberichten.

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Een Freshdesk-integratie toevoegen

Om in injixo een nieuwe Freshdesk-integratie toe te voegen, heb je een Freshdesk Pro- of Enterprise-account nodig.

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Freshworks**-tegel op _Kies een model_{:.doc-button}.
4. Klik in de sectie **Freshdesk** op _Voeg integratie toe_{:.doc-button}.

## Je Freshdesk-integratie configureren

1. Geef de nieuwe integratie een unieke naam die naar de gegevensbron verwijst.
2. Voer in de sectie **Toegangsgegevens** je volledige Freshdesk-domeinnaam met subdomein in, bijvoorbeeld: example.freshdesk.com.
3. Ga naar Freshdesk en kopieer een geldige API-key van een gebruiker met de rol Account Administrator.
4. Ga terug naar injixo en plak de API-key in het veld **API-key**.
5. Klik op _Integratie opslaan_{:.doc-button}.

## De injixo-app installeren

Voor de Freshdesk-integratie is een clienttoepassing nodig. Ga nadat je de configuratie hebt opgeslagen verder met de sectie **Installeer injixo app**.

Om een **injixo API-key** te genereren en kopiëren, klik je op _Genereren_{:.doc-button}.

Volg de instructies op het scherm om de injixo-app in je Freshdesk-account te configureren. Ga voor meer informatie naar de [Freshworks marketplace](https://www.freshworks.com/apps/freshdesk/injixo_connect).

## Freshdesk-gegevens in injixo

injixo importeert alle ticketgegevens uit Freshdesk. Tickets bevatten meestal meerdere gesprekken die tussen je medewerkers en klanten plaatsvinden.<br>
Opmerking: injixo kan de ticketduur niet uit Freshdesk importeren. Daarom wordt in injixo Forecast voor workloads met Freshdesk-queues geen AHT-grafiek weergegeven.

### Tickets en gesprekken

In injixo worden alle gesprekken gegroepeerd op basis van het communicatiekanaal in Freshdesk (source, oftewel bron). Een gesprek kan een nieuw ticket zijn of een antwoord op een bestaand ticket.

In injixo worden de gesprekken in een Freshdesk-ticket afzonderlijk geteld als een binnenkomend contact.

Voorbeeld: Een gebruiker maakt per e-mail een ticket aan. Het teamlid beantwoordt deze vervolgens en sluit het ticket. Twee dagen later wordt het ticket opnieuw geopend door een volgende e-mail, die tot een nieuw gesprek leidt.

Het aantal aangeboden contacten in injixo is meestal hoger dan het aantal tickets dat in Freshdesk gerapporteerd wordt.

### Gebeurtenissen van verschillende bronnen

In een Freshdesk-ticket kunnen antwoorden in verschillende injixo-queues worden gevolgd in het kanaal Cases.

Voorbeeld: Als er per e-mail een antwoord op een ticket binnenkomt, dan zie je het contact in een injixo-queue die overeenkomt met de Freshdesk-groep en de bronnaam. Een chat in hetzelfde ticket wordt in een afzonderlijke queue geteld.

### Naamgevingsconventie bronqueue

injixo maakt bronqueues aan op basis van je tickets. De naamgevingsconventie van deze queues is afhankelijk van de fase van de gegevensimport (initieel of doorlopend). Tijdens deze initiële import komt de naam van de bronqueue volgens de volgende conventie  tot stand:

- "groepnaam + bronnaam + Tickets"
- "groepnaam + bronnaam + Replies"

Voorbeelden:

- CustomerService chat Tickets
- CustomerService email Replies
- Unknown group/source Tickets

Bij een nieuw ticket wordt een ticketqueue aangemaakt. Bij een antwoord op een queue wordt er een antwoordqueue aangemaakt, waar ook verdere antwoorden in worden opgeslagen. Om alle informatie over een ticket te krijgen, dien je zowel naar het ticketqueue als naar de antwoordqueue te kijken.

### Verwijderde tickets en spamtickets

De groepnaam en de bronnaam kunnen niet worden vastgesteld als een ticket dat al is verwijderd of als spam is gemarkeerd, wordt gewijzigd. De bronqueues die deze tickets tellen, krijgen het label Unknown group/source Tickets of Unknown group/source Replies. Meestal zijn deze queues niet relevant voor het plannen van de workload van je medewerkers.

## Veelgestelde vragen

| Vraag                                                                                                                                                                       | Antwoord                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| injixo laat ineens geen nieuwe Freshdesk-gegevens meer zien, maar op de pagina in **Account > Integraties** is de status van mijn Freshdesk-integratie nog steeds Operationeel. Wat kan ik doen? | De injixo-app haalt gegevens op uit Freshdesk en stuurt gebeurtenissen naar injixo. Communicatiefouten tussen de injixo-app en injixo kunnen ertoe leiden dat gegevens uit Freshdesk niet meer worden weergegeven. De Freshdesk Contact Center-integratie kan zulke communicatiefouten niet herkennen.<br><br>Controleer of de injixo API-key die je bij de configuratie van injixo in je Freshdesk-account hebt ingevoerd nog geldig is. Als de API-key ongeldig is, vervang je de API-key op de app-installatiepagina in injixo. Als de API-key nog steeds geldig is, neem dan contact op met het supportteam van injixo. |
