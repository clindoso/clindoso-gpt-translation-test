---
title: Een Five9-integratie toevoegen
description: Verbind je Five9-ACD met injixo en bereid een aangepast rapport om queues op basis van vaardigheden te groeperen.
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

Een Five9-integratie is een cloudintegratie die de oproepgeschiedenis, en agentstatus- en RTA-gegevens importeert.

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Voorwaarden

Als je je queues op basis van campagne groepeert, dan leest de integratie het standaard call log report van Five9.

Als je je queues op basis van vaardigheden groepeert, dan heeft de integratie een aangepast call log report van Five9 nodig, waaraan vaardigheden zijn toegevoegd. Om gegevens van queues te importeren die op basis van vaardigheden zijn gegroepeerd, volg je de onderstaande stappen in Five9:

 1. Maak een nieuwe gedeelde rapportmap aan.
 2. Bewerk het standaard call log report door een kolom met de naam "SKILL" toe te voegen.
 3. Sla het aangepaste rapport in de gedeelde map op als "Call Log with Skills".

Raadpleeg het Five9 Help Center voor meer gedetailleerde informatie over het aanpassen van rapporten.

## Je Five9-integratie toevoegen

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Five9**-tegel op _Voeg integratie toe_{:.doc-button}.
4. Geef de nieuwe integratie een unieke naam die naar de gegevensbron verwijst.
5. Voer de gebruikersnaam en het wachtwoord in van een persoon met adminrechten in je Five9-account in.
6. Selecteer in de sectie **Configuratie** je accountregio en groeperingskeuze.
7. Klik op _Integratie opslaan_{:.doc-button}.

De integratie importeert nu gegevens naar injixo. Het importeren kan tot 15 minuten duren. Alle queues van het verbonden systeem zijn automatisch beschikbaar om op het {% link_new workload-configuratiescherm | features/forecast/injixo-forecast/manage-workloads.md | #workloads-aanmaken %} in injixo Forecast te worden toegewezen.

## Wat gebeurt er bij parallelle agentstatussen?

Soms rapporteert Five9 tegelijkertijd meerdere statussen voor een agent, bijvoorbeeld:

| Status   | Starttijd | Eindtijd |
| ------- | ---------- | -------- |
| Ready   | 13:00:00   | 13:00:05 |
| Inbound | 13:00:00   | 13:03:00 |

Om te voorkomen dat de ene status door de andere wordt overschreven, wijzigt de integratie het begin van de langstdurende status. Het begin van de langstdurende status wordt dan als begin van de kortere status gebruikt:

| Status   | Starttijd | Eindtijd |
| ------- | ---------- | -------- |
| Ready   | 13:00:00   | 13:00:05 |
| Inbound | 13:00:05   | 13:03:00 |
