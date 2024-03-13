---
title: Een Freshdesk Contact Center-integratie toevoegen
description: Lees hoe je je Freshdesk Contact Center-CRM verbindt met injixo om gegevens te importeren.
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

Een Freshdesk Contact Center-integratie is een cloudintegratie die de oproepgeschiedenis, en realtime adherencegegevens importeert.

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Een Freshdesk Contact Center-integratie toevoegen 

Om in injixo een nieuwe Freshdesk Contact Center-integratie toe te voegen, heb je een Freshdesk Contact Center Pro- of Enterprise-account nodig.

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Freshworks**-tegel op _Kies een model_{:.doc-button}.
4. Klik in de sectie **Freshdesk Contact Center** op _Voeg integratie toe_{:.doc-button}.

## Maak je Freshdesk Contact Center-integratie aan

1. Geef de nieuwe integratie een unieke naam die naar de gegevensbron verwijst.
2. Vul in de sectie **Toegangsgegevens** je domeinnaam van het Freshdesk Contact Center in (inclusief subdomein), bijvoorbeeld example.freshcaller.com.
3. Ga naar Freshdesk Contact Center en kopieer een geldige API-key van een gebruiker met de rol Account Administrator.
4. Ga terug naar injixo en plak de API-key in het veld **API key**.
5. Selecteer de [groeperingskeuze voor geïmporteerde queues](#queuenamen-op-basis-van-groeperingskeuze).
6. Klik op _Integratie opslaan_{:.doc-button}. 

Ga nadat je de configuratie hebt opgeslagen verder met de sectie **Installeer injixo app** op de pagina.

## De injixo-app installeren

1. Genereer in de sectie **Installeer injixo app** de **injixo API-key** en kopieer deze.
2. Configureer de benodigde injixo-app in je Freshdesk-account in de [Freshworks marketplace](https://www.freshworks.com/apps/freshcaller/injixo_1/).
3. Plak de gekopieerde API-key in de installatiepagina van de injixo-app.
4. Om in realtime gegevens te importeren, vink je het selectievakje **Export real-time agent status data** aan op de installatiepagina van de injixo-app in Freshworks marketplace.

## Queuenamen op basis van groeperingskeuze

Bij het importeren van gegevens heeft de groeperingskeuze invloed op de naamgeving van de queues die in injixo worden aangemaakt:

| Groeperingskeuze   | Naam van de queue                               | Voorbeeld           |
| ------------------- | ---------------------------------------- | ----------------- |
| Telefoonnummer        | Telefoonnummer                             | +49123456789      |
| Routering (team/agent) | Naam van het team                                | Tech Support Team |
| Routering (team/agent) | Naam van de agent (indien er geen naam voor het team is toegewezen) | Agent 1           |

Oproepen die buiten een groep vallen in het Freshdesk Contact Center krijgen de queuenaam Undefined_Queue.

## Veelgestelde vragen

| Vraag                                                                                                                                                                       | Antwoord                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| injixo laat ineens geen nieuwe Freshdesk Contact Center-gegevens meer zien, maar op de pagina in **Account > Integraties** is de status van mijn Freshdesk Contact Center-integratie nog steeds Operationeel. Wat kan ik doen? | De injixo-app haalt gegevens op uit Freshdesk Contact Center en stuurt gebeurtenissen naar injixo. Communicatiefouten tussen de injixo-app en injixo kunnen ertoe leiden dat gegevens uit Freshdesk Contact Center niet meer worden weergegeven. De Freshdesk Contact Center-integratie kan zulke communicatiefouten niet herkennen.<br><br>Controleer of de injixo API-key die je bij de configuratie van injixo in je Freshdesk-account hebt ingevoerd nog geldig is. Als de API-key ongeldig is, vervang je de API-key op de app-installatiepagina in injixo. Als de API-key nog steeds geldig is, neem dan contact op met het supportteam van injixo. |
