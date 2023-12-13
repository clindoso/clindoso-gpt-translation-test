---
title: Gegevens importeren met injixo API
navigation_title: injixo API
product_label:
  - advanced
  - enterprise
description: Een injixo API-integratie toevoegen om contact- en agentstatusgegevens van je externe systeem te downloaden.
related_articles:
  - overwrite_title: Workloads beheren
    filepath: features/forecast/injixo-forecast/manage-workloads.md
  - overwrite_title: Dashboards beheren
    filepath: features/monitoring/dashboards/dashboards-overview.md
---

injixo gebruikt aanbiederspecifieke en universele integraties om contact- en agentstatusgegevens van externe systemen te importeren.

## Wat is een injixo API-integratie?

In injixo Advanced en Enterprise WFM zorgt injixo API-integraties ervoor dat je API-verzoeken kunt sturen om gegevens te importeren (bijvoorbeeld als er geen standaardintegratie is voor je externe systeem). Voor dit doel biedt de API van injixo de volgende bronnen:

- [Bron van contactgebeurtenis](https://api.injixo.com/resources/integration_contact_event/): Contactgebeurtenissen worden geregistreerd als klanten telefonisch, per e-mail of via de chat contact opnemen met je bedrijf. injixo slaat deze gegevens op in queues die worden gegroepeerd op basis van queuenaam en kanaal.
- [Bron agentstatus](https://api.injixo.com/resources/integration_agent_status/): Agentstatusgegevens worden geregistreerd als je teamleden van de ene activiteit overgaan naar de volgende, bijvoorbeeld aanmelden, nawerk of afmelden.

## Een injixo API-integratie toevoegen

Gebruikers met admintoegang kunnen als volgt een injixo API-integratie toevoegen:

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Universal interfaces**-tegel op _Kies een model_{:.doc-button}.
4. Klik in de sectie **injixo API** op **Voeg integratie toe**.
5. Geef de nieuwe integratie een unieke naam die nog niet wordt gebruikt.
6. Klik op **Integratie opslaan**.<br>De sectie **Toegang tot de injixo API** wordt geactiveerd.
7. Klik op _Genereren_{:.doc-button} om de injixo API-key te genereren.

Authenticatie werkt ook met persoonlijke access tokens die in gebruikersprofielen in de sectie {% link_new **Persoonlijke access tokens** | features/reporting/injixo-api/injixo-api.md | #authorization-personal-access-token %} zijn aangemaakt.

> Je hebt later geen toegang meer tot de API-key. 
>
> - Sla de API-key op een veilige plaats op, bijvoorbeeld in je wachtwoordmanager.
> - De huidige API-key vervalt als een gebruiker voor de integratie een nieuwe API-key genereert of de integratie verwijdert.

## Importgegevens

Om de API-integratie te identificeren en authenticeren, voeg je de injixo API-key en de configuratie-ID van de integratie toe aan de API-aanvragen:

1. Voeg je API-key toe aan de Authorisatie-aanvraagheader.
2. Zoek of kopieer de configuratie-ID van je integratie:
    - Ga naar _Account > Integraties_{:.breadcrumbs}.
    - Klik in de sectie API-integratie op het pictogram Bewerken {% icon pencil | icon-only %}.
    - Klik in de sectie **Toegang tot de injixo API** op _{% icon clone | icon-only %} Kopiëren_{:.doc-button}.
3. Voeg de configuratie-ID van je integratie toe aan het **meta**-object in de aanvraagbody.

Om gegevens van je externe systeem regelmatig in injixo te importeren, moet je je eigen applicatie uitvoeren. Raadpleeg de gebruikershandleidingen in de [injixo API documentation](https://api.injixo.com) voor voorbeeldscripts in Ruby en Pyton.

## Gegevensimports testen

Voor het testen kun je losse POST-aanvragen naar de API sturen. Het datumbereik in de onderstaande voorbeelden bevatten een enkel gegevenspunt, dat indien gewenst kan worden gewijzigd. Vervang in ieder geval de voorbeeld-API-key (abc123456=) en de integrationConfigurationId-waarde (1234) door die van jezelf.

De API ondersteunt alleen HTTPS. Stuur je verzoeken naar https://api.injixo.com om te voorkomen dat de foutmelding `not_found` optreedt.

### cURL in de opdrachtregel

De volgende voorbeelden laten zien hoe je met [cURL](https://curl.se/) gegevens naar de API stuurt. cURL is een opdrachregelprogramma dat via een terminal gegevens uitwisselt met een server.

Contactgebeurtenissen:

```
curl -X POST \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer abc123456=" \
 -d '{"data":[{"properties":{"offered":true,"handled":false,"duration":124.6},"queueName":"Level 1 support","queueIdentifier":"1337_99","timestamp":"2021-12-06T10:34:22Z","channel":"calls"}],"meta":{"integrationConfigurationId":1234}}' \
 https://api.injixo.com/external-systems/contact-events
```

Opmerking: Voor elke nieuwe combinatie van `queueIdentifier`, `queueName` en `integrationConfigurationId` wordt een nieuwe queue aangemaakt. Om dubbele queuenamen te voorkomen, dien je dezelfde queueIdentifier of dezelfde integrationConfigurationId toe te voegen voor elke aanvraag met met dezelfde queuenaam. 

Agentstatus:

```
curl -X POST \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer abc123456==" \
 -d '{"data":[{"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2021-12-06T10:00:00Z","endTime":"2021-12-06T15:00:00Z"}],"meta":{"integrationConfigurationId":8431,"externalSystem":"My ACD"}}' \
 https://api.injixo.com/external-systems/agent-statuses
```

### REST-clients

De volgende voorbeelden laten zien hoe je met een REST-client, zoals [Postman](https://www.postman.com/downloads/), gegevens naar de API stuurt.

1. Voeg een JSON-aanvraagheader toe:

   ```
   {
  "Content-type": "application/json",
  "Authorization": "Bearer abc123456="
}
   ```

2. Voeg een andere JSON-aanvraagbody toe die afwijkt voor contactgebeurtenissen en agentstatusgegevens.<br><br>

   Voorbeeld van een aanvraagbody voor contactgebeurtenissen: `/external-systems/contact-events`:

   ```
   {
  "data": [
    {
      "properties": { "offered": true, "handled": false, "duration": 124.6 },
      "queueName": "Level 1 support",
      "queueIdentifier": "1337_99",
      "timestamp": "2021-12-06T10:34:22Z",
      "channel": "calls"
    },
    {
      "properties": { "offered": true, "handled": true, "duration": 200.1 },
      "queueName": "Level 1 support",
      "queueIdentifier": "1337_99",
      "timestamp": "2021-12-06T10:46:22Z",
      "channel": "calls"
    }
  ],
  "meta": { "integrationConfigurationId": 1234 }
}
   ```

   Voorbeeld van een aanvraagbody voor de agentstatus: `/external-systems/agent-statuses`:

   ```
   {
  "data": [
    {"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2022-12-06T08:00:00Z","endTime":"2022-12-06T13:00:00Z"},
    {"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2022-12-07T09:00:00Z","endTime":"2022-12-07T10:00:00Z"}
  ],
  "meta": {
    "integrationConfigurationId": 1234,
    "externalSystem": "My ACD"
  }
}
   ```

## Je eerste API-aanvraag - en nu?

Nadat je een API-aanvraag hebt verstuurd, duurt het even voordat je de gegevens in injixo kunt zien. Je kunt als volgt met de geïmporteerde gegevens werken:

- Aanvragen voor contactgebeurtenissen: Zodra de gegevens zijn verwerkt, worden de geïmporteerde queues op de pagina's Nieuwe workload en Workload bewerken in Forecast weergegeven.
- Aanvragen voor agentstatusgegevens: Bij een eerste aanvraag met nieuwe agent-ID's worden er niet direct agentstatusgegevens in het Dienstrooster-Center weergegeven. Om gegevens te bekijken, dien je ten minste {% link_new een externe ID aan een medewerker toe te wijzen | features/acd-integration/cloud/import-agent-status-data.md | #medewerker-ids-van-externe-systemen-aan-medewerkers-toewijzen-in-injixo %} (verzonden als agentIdentifier). Om de gegevens weer te geven, dien je een andere aanvraag te sturen.
