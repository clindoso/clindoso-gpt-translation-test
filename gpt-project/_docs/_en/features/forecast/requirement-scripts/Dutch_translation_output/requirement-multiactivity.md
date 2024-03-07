---
title: Multiactiviteitenscript <!-- GPT translation -->
description: De personeelsbehoefte voor multiactiviteiten berekenen. <!-- GPT translation -->
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

Gebruik het Multiactivity-script om de personeelsbehoefte voor je multiactiviteiten te berekenen. De berekening is gebaseerd op Erlang-C met gebruik van een service level. <!-- GPT translation -->

## Vereisten <!-- TM 100 -->

- Maak  acht minimaal een {% link_new Workforce Timekeeper-kader | features/administration/activity-types-and-properties.md | #activiteitentypes %} aan en wijs het toe aan je eenheid. <!-- GPT translation -->
- Maak een {% link_new workload | features/forecast/injixo-forecast/manage-workloads.md | #workloads-aanmaken %} aan voor elke deelactiviteit van de multiactiviteit. <!-- GPT translation -->

## De forecast exporteren voor alle deelforecasts. <!-- GPT translation -->

Voordat je het script voor Meerdere activiteiten kunt uitvoeren, exporteer je de forecasts voor alle workloads die zijn aangemaakt voor de deelactiviteiten: <!-- GPT translation -->

1. Selecteer in _Forecast > Workloads_{:.breadcrumbs} de workload die je voor een deelactiviteit hebt aangemaakt. <!-- GPT translation -->
2. Selecteer het tijdsbestek met de datumkiezer. Klik op een weeknummer om de hele week te selecteren, of klik op een dag en sleep om een kortere of langere periode dan een week te selecteren. <!-- GPT translation -->
3. Selecteer **Gebruik forecast** in het {% icon ellipsis_v %} rechtsboven. <!-- GPT translation -->
4. Selecteer in het nieuw geopende venster de forecast die je wilt gebruikten. <!-- GPT translation -->
5. Klik op _Forecast gebruiken_{:.doc-button}. <!-- GPT translation -->
6. Klik op *Sluiten*{:.doc-button}. <!-- GPT translation -->
7. Herhaal de stappen 1-6 voor alle workloads die voor je deelactiviteiten worden aangemaakt. <!-- GPT translation -->

injixo slaat de gegevens die nodig zijn voor de berekening van de personeelsbehoefte op in queues in _WFM > Beheer > Forecast > Queues_{:.breadcrumbs}. De queues hebben de naam van de betreffende workload met een asterisk ervoor, bijvoorbeeld: \*yourWorkloadName. <!-- GPT translation -->

## Het script configureren <!-- GPT translation -->

1. Ga naar *Forecast > Behoefte-scripts*{:.breadcrumbs}. <!-- GPT translation -->
2. Klik in de **Calls - Multi-Activity**-tegel op _Openen_{:.doc-button}.   <!-- GPT translation -->
3. Configureer in het script configuratievenster de volgende instellingen: <!-- GPT translation -->
   - In de sectie **Datum**: <!-- GPT translation -->
      - **Begindatum**: Voer de begindatum toe voor de berekening van de personeelsbehoefte. <!-- GPT translation -->
    - **Aantal dagen**: Voer het aantal dagen in vanaf de begindatum waarvoor je de personeelsbehoefte wilt berekenen. <!-- GPT translation -->
   - In de sectie **Eenheidparameters**: <!-- GPT translation -->
     - **Eenheid** en **Multi-Activiteit**.<br> <!-- GPT translation -->
    In het venster met de scriptconfiguratie worden de berekeningsparameters voor de relevante deelactiviteiten bijgewerkt en weergegeven. <!-- GPT translation -->
   - In de sectie **Deelactiviteit** kun je verschillende rekenparameters voor elke deelactiviteit instellen. Begin met de parameters in de sectie **Queue_parameters**: <!-- GPT translation -->
    - **Berekeningsmethode**: Selecteer **Erlang-C**, **Lineair** of **Chat**.<br>In het scriptconfiguratievenster worden relevante configureerbare parameters weergegeven. In de onderstaande [tabel](#calculation-parameters-in-the-erlang-c-section) kun je zien welke parameters voor elke berekeningsmethode kunnen worden geconfigureerd. <!-- GPT translation -->
    - **Queue**: Selecteer de queue die de gegevens bevat die je voor de berekening wilt gebruiken. <!-- GPT translation -->
    - **Processen**: Selecteer het waardetype van het contactvolume, bijvoorbeeld: Aantal oproepen. <!-- GPT translation -->
    - **Gemiddelde afhandeltijd**: Als er voor je workloads een forecasted average handle time (AHT) is, dan selecteer je eerst het relevante waarde-type. Anders selecteer je **[Geen]**. <!-- GPT translation -->
    - **Versie**: Selecteer **Auto-Forecast**. In injixo Enterprise on-premise, kun je eventueel een andere versie selecteren. <!-- GPT translation -->

## Berekeningsparameters in de sectie Erlang C <!-- GPT translation -->

| Parameter                         | Beschrijving                                                                                                            | Configuratie in Erlang-C | Configuratie in Lineair | Configuratie in Chat | <!-- GPT translation -->
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |--------  | -------- |
| Service Level (%)             | Percentage contacten dat binnen een tijd behandeld moeten zijn, zoals is ingesteld in de parameter **Service Sec.**.                                                                                                                                                                    | Ja | Nee | Ja | <!-- GPT translation -->
| Service Niveau             | Tijd waarbinnen het percentage contacten dat je in het parameter **Service Level (%)** instelt, afgehandeld moet zijn.                                                                                                                                      | Ja | Nee | Ja | <!-- GPT translation -->
| Bijtelling (%)                         | Het percentage waarmee je de berekende personeelsbehoefte wilt verhogen. Lees hoe je deze parameter [configureert](#configure-the-add--parameter-to-account-for-shrinkage) om rekening te houden met krimp. | Ja | Ja | Ja | <!-- GPT translation -->
| Minimale bezetting            | Voer een waarde in om de staff requirement op het afgegeven niveau de overschrijden.                                                                                                                                                                                                                                                     | Ja | Ja | Ja | <!-- GPT translation -->
| Maximale bezetting            | Voer een waarde in om hogere bezetingsvereisten te overschrijven.                              | Ja | Ja | Ja | <!-- GPT translation -->
| Vaste gemiddelde verwerkingstijd | Als je een type hebt geselecteerd in het veld **Gemiddelde verwerkingstijd** in de sectie **Queu <!-- GPT translation -->
| Volgorde (%)                  | Percentage van de AHT dat medewerkers besteden aan taken die ze niet parallel kunnen uitvoeren, zoals nawerk.                                                                                                                                                                                              | Nee | Nee | Ja | <!-- GPT translation -->
| Max. sessies                          | Maximale aantal parallelle chats waarvoor een medeweker tegelijkertijd verantwoordelijk kan zijn.                                                                                                                                             | No | No | Yes | <!-- GPT translation -->

### Configure the Add (%) parameter to account for shrinkage <!-- GPT translation -->

Om de **Optellen (%)**-parameter zo te configureren dat deze rekening houdt met je krimp, gebruik je de volgende formule. Waarbij s% je krimppercentage is: 1/(1-s%)-1. Het resultaat dat als een percentage is uitgedrukt, vul je in als waarde in de parameter **Optellen (%)**.  Om bijvoorbeeld rekening te houden met een krimp van 20%, zien de berekening er als volgt uit: 1/(1-0.2)-1, dat uitkomt op 25%. <!-- GPT translation -->

## Het script uitvoeren <!-- GPT translation -->

- Klik op _OK_{:.doc-button} om de berekening uit te voeren.<br>Er wordt een venster geopend met de geselecteerde invoerparameters en de resultaten van het script. <br> <!-- GPT translation -->

## De berekeningsresultaten bekijken <!-- GPT translation -->

Je kunt de gewijzigde personeelsbehoefte voor de geselecteerde eenheid en multiactiviteit bekijken in de {% link_new Dashboard | features/monitoring/dashboards/dashboards-overview.md %} of in het paramameter-menu in het {% link_new Dienstrooster-Center | features/scheduling/edit-or-delete-staff-requirements.md %} of in {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %}. <!-- GPT translation -->