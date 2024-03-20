---
title: Outbound calls-script <!-- GPT translation -->
description: De personeelsbehoefte voor uitgaande oproepen berekenen. <!-- GPT translation -->
toc: true
product_label:
- essential
- advanced
- enterprise
- classic
redirect_from:
- "/requirement-outbound/"
redirect_reason: Updated filename on 18 March 2024
gpt_translation: True
---

Gebruik het Outbound Calls-behoeftescript om de personeelsbehoefte te berekenen voor campagnes met uitgaande oproepen. De berekening is gebaseerd op het totale aantal contacten dat in de campagne wordt gecontacteerd, de campagnedelta, en de verwachte gemiddelde afhandeltijd. <!-- GPT translation -->

## Vereisten <!-- TM 100 -->

Begin met het exporteren van de forecast om de personeelsbehoefte te berekenen op basis van een voorspelde oproepverdeling: <!-- GPT translation -->

1. Selecteer in _Forecast > Workloads_{:.breadcrumbs} een workload. <!-- GPT translation -->
2. Selecteer met behulp van de datumkiezer een tijdsbestek. Klik op het weeknummer om de hele week te selecteren of klik op een dag en sleep om een periode te selecteren die korter of langer is dan een week. <!-- GPT translation -->
3. Selecteer **Toon forecast** vanuit het {% icon ellipsis_v %} rechts bovenin. <!-- GPT translation -->
4. In het venster **Bereken de personeelsbehoefte op basis van** selecteer je de forecast die je wilt gebruiken. <!-- GPT translation -->
5. Klik op _Gebruik forecast_{:.doc-button}. <!-- GPT translation -->
6. Klik op _Sluiten_{:.doc-button}. <!-- GPT translation -->

Je kunt het Outbound calls requirement-script ook gebruiken om de personeelsbehoefte te berekenen zonder dat daarvoor een forecast nodig is. Zie hoe je de parameters instelt in de tabel onder de [sectie Campaigngegevens](#campaigngegevens). <!-- GPT translation -->

## De script instellen <!-- GPT translation -->

1. Ga naar _Forecast > Behoefte-scripts_{:.breadcrumbs}. <!-- GPT translation -->
2. Klik in de tegel **Gebelde Outbound Contacten** op _Openen_{:.doc-button}. <!-- GPT translation -->

Het venster \`Systeemscript\|Configuratievenster\` bestaat uit drie secties. Zie de tabellen hieronder voor instructies over het configureren van de parameters. <!-- GPT translation -->

### Sectie **Campagnegegevens** <!-- GPT translation -->

| Parameter                    | Beschrijving                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- GPT translation -->
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Queue                        | Selecteer de queue waarvoor je het programma wilt gebruiken.                                                                                                                                                                                                                                                                                                                                                                                                                                                              | <!-- GPT translation -->
| Records                      | Het totale aantal contacten voor je campagne. Selecteer **vast** en geef een waarde op in onderstaand veld om personeelsbehoefte te berekenen zonder forecast. Selecteer **variabel** en selecteer een waarde met forecasted contacten.                                                                                                                                                                                                                                                                                                                                                                                                                                                             | <!-- GPT translation -->
| Contactrate (%)               | Het percentage beantwoorde uitgaande oproepen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | <!-- GPT translation -->
| Opnieuw bellen (%)              | Het aandeel contacten dat opnieuw wordt gekozen na een onsuccesvolle belpoging. De opnieuw bellen-pogingen worden verdeeld over een datumbereik die je met de parameters **Begindatum** en **Einddatum** instelt. Lees meer over het opnieuw bellen-percentage in de [betreffende sectie hieronder](#wat-is-het-redial-rate-). | <!-- GPT translation -->
| Begindatum                   | Begin van het datumbereik voor de berekening.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | <!-- GPT translation -->
| Einddatum                    | Einddatum van het bereik voor de berekening. Selecteer **Datum** en voer hieronder een datum in, of selecteer **Looptijd Campagne in dagen (1-30)** en voer hieronder een waarde in. | <!-- GPT translation -->
| RPC (%) | Het percentage oproepen dat door de juiste ontvangers wordt aangenomen. Selecteer **vast** en voer een waarde toe in het onderstaande veld in of selecteer **variabel** en selecteer een waarde met voorspelde 'reached' rate.                                                                                                                                                                                                                                                             | <!-- GPT translation -->
| Reserve (%)                | (Optioneel) Het percentage betaalde tijd waarin medewerkers niet beschikbaar zijn om contacten af te handelen, bijvoorbeeld door ongeplande pauzes of ziekteverlof.     | <!-- GPT translation -->

### Optie: Afhandeltijd <!-- GPT translation -->

| Parameter        | Beschrijving                                                                                                                                                                                                                                                                                                                                                  | <!-- GPT translation -->
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vast/flexibel   | Select **vast** en voer vaste waarden in de velden hieronder in, of selecteer **flexibel** en selecteer waardetypes in de velden hieronder.                                                                                                                                                               | <!-- GPT translation -->
| RPC in seconden   | Average Handling Time (AHT) in seconden voor een gesprek met de juiste contactpersoon. Deze waarde is inclusief de After-Call Work-tijd (ACW).                                                                                                                                                                                                                                                        | <!-- GPT translation -->
| WPC in seconden   | AHT, in seconden, voor een oproep die door de verkeerde contactpersoon is beantwoord, zoals een gesprek dat door de verkeerde contactpersoon of die naar een voicemail is doorverbonden.                                                                                                                                                                                          | <!-- GPT translation -->


### Sectie Werkbelasting medewerkers <!-- GPT translation -->

| Parameter        | Beschrijving                                                                                                                                                                                                      | <!-- GPT translation -->
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Eenheden | De eenheid waarvoor je het personeelsbehoefte wilt berekenen. Als je de eenheid wijzigt, dan wordt het vervolgkeuzemenu **Activiteit** bijgewerkt en toont deze alle activiteiten die aan de eenheid zijn toegewezen. | <!-- GPT translation -->
| Activiteit         | De activiteit waarvoor je de personeelsbehoefte wilt berekenen.                                                                                                                                            | <!-- GPT translation -->
| Min. aantal medewerkers    | Het minimaal aantal benodigde medewerkers dat u per interval nodig heeft. Voer een waarde in om intervallen waarvoor minder medewerkers nodig zijn te overschrijven.        | <!-- GPT translation -->
| Maximum aantal medewerkers    | Het hoogste aantal medewerkers dat per interval nodig is. Voer een waarde in om intervallen voor superieure personeelsbehoeften te overschrijven.                                                                          | <!-- GPT translation -->

## Het script uitvoeren <!-- GPT translation -->

- Klik op _OK_{:.doc-button} om de berekening te starten.<br>Er wordt een venster geopend dat de ingevoerde parameters en de scriptresultaten weergeeft. <!-- GPT translation -->

 Je kunt de {% link_new opgeslagen personeelsbehoefte in Dienstrooster-Center bekijken | features/scheduling/edit-or-delete-staff-requirements.md %}. <!-- GPT translation -->

Opmerking: In injixo Enterprise on-premise ga je naar *WFM > Forecast > ForecastPro > Forecast*{:.breadcrumbs} of *WFM > Administration > Forecasting > Scripts*{:.breadcrumbs}. Voor de combinatie van queue, waarde type en versie is een bestaande forecast vereist. De naam van het script kan variëren, omdat je de mogelijkheid hebt om bij het aanmaken van het script een aangepaste naam te definiëren. <!-- GPT translation -->

## Wat is de call-back rate (CBR)? <!-- GPT translation -->

Het redial-percentage is het percentage oproepen dat opnieuw worden geprobeerd nadat eerdere pogingen geen succes hadden. Bij het proces van het opnieuw proberen (redialen) wordt doorgegaan totdat minder dan 1% van de oproepen onbeantwoord blijft.<br>Voorbeeld: Als je 5.000 mensen wilt bereiken, dan betekent een redial-percentage van 10% dat bij de tweede poging 500 niet beantwoorde oproepen zijn herhaald, tijdens de derde poging 50 oproepen zijn herhaald en tijdens de vierde poging 5 oproepen zijn herhaald. In totaal worden er in dit geval 5.555 uitgaande oproepen gedaan. <!-- GPT translation -->
