---
title: Een Odigo-integratie toevoegen
description: Lees hoe je je Odigo-ACD verbindt om gegevens te importeren.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Agentstatusgegevens toevoegen
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

De Odigo-integratie importeert realtime agentstatus- en RTA-gegevens.

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Een Odigo-integratie toevoegen

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Odigo**-tegel op _Voeg integratie toe_{:.doc-button}.
4. Geef de nieuwe integratie een unieke naam die naar de gegevensbron verwijst.
5. (Optioneel) Configureer de import van agentstatussen Pauze met details:
- Vink het selectievakje **
Agentstatus Pauze met details importeren**.<br>Bij het importeren van pauzestatussen registreert injixo ook het type van de genomen pauzes.<br>Opmerking: Als je dit selectievakje aanvinkt, dan moet je ook de {% link_new toegewezen activiteiten | features/acd-integration/cloud/import-agent-status-data.md | #activiteiten-van-het-externe-systeem-toewijzen %} bijwerken.
- Voer je Odigo-URL in, inclusief tenant-ID.
- Voer de gebruikersnaam en het wachtwoord in voor de webservice in.
6. Klik op _Integratie opslaan_{:.doc-button}.

## Je Odigo-integratie configureren

1. Klik in de sectie **injixo-URL-token genereren** op _Genereren_{:.doc-button}.
2. Kopieer de injixo-URL-token naar je klembord.<br>
De injixo-URL-token wordt slechts één keer weergegeven. Als je je configuratie niet meteen kunt afronden, sla het dan op een veilige plaats op, bijvoorbeeld in een wachtwoordmanager.
3. Activeer in de sectie Administration in je Odigo-interface de optie voor het sturen van meldingen naar een externe server. Neem hiervoor contact op met Odigo.
4. Gebruik de gekopieerde **injixo-URL-token** als meldings-URL.
5. Sla je instellingen op in Odigo en ga terug naar injixo.

Om de integratie te activeren, moet je eerst de server opnieuw opstarten. Neem hiervoor contact op met Odigo.<br>
Vanaf nu importeert injixo RTA-gegevens. Deze worden pas zichbaar nadat je externe gebruikers-id's aan je medewerkers hebt toegewezen.

## Externe gebruikers aan je medewerkers toewijzen

1. Ga naar _WFM > Administratie > Planning > Medewerkers_{:.breadcrumbs}.
2. Wijs externe gebruikers-id's toe aan je medewerkers.

Lees meer over {% link_new het toewijzen van externe gebruikers-ID's | features/acd-integration/cloud/import-agent-status-data.md | #medewerker-ids-van-externe-systemen-aan-medewerkers-toewijzen-in-injixo %}.

## Agentstatussen koppelen aan injixo-activiteiten

1. Ga naar _WFM > Administratie > Planning > Activiteiten_{:.breadcrumbs}.
2. Wijs Odigo-activiteiten toe aan injixo-activiteiten.

Lees meer over het {% link_new toewijzen van externe activiteiten | features/acd-integration/cloud/import-agent-status-data.md | #activiteiten-van-het-externe-systeem-toewijzen %} aan injixo-activiteiten.
