---
title: De personeelsbehoefte berekenen
product_label:
  - advanced
  - enterprise
  - classic
description: De personeelsbehoefte berekenen voor oproepen, chats, e-mail en meer.
related_articles:
  - overwrite_title: Oproepenscript voor multiactiviteiten
    filepath: features/forecast/requirement-scripts/requirement-multiactivity.md
  - overwrite_title: Uitgaande oproepen
    filepath: features/forecast/requirement-scripts/requirement-outbound.md
  - overwrite_title: Constante behoefte
    filepath: features/forecast/requirement-scripts/requirement-constant.md
  - overwrite_title: De personeelsbehoefte bewerken of verwijderen
    filepath: features/scheduling/employee-requirement.md
---

De laatste stap bij het maken van forecasts is het berekenen van de personeelsbehoefte met behulp van een van de berekeningsmethoden. Om in te stellen waar de personeelsbehoefte wordt opgeslagen, selecteer je een eenheid en een activiteit in je workloads. Je kunt ook zonder forecast constante personeelsbehoeften schrijven.

Ben je nog niet zo vertrouwd met injixo Forecast? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Beschikbare berekeningsmethoden

Er zijn verschillende berekeningsmethoden beschikbaar in injixo om de personeelsbehoefte te berekenen. Klik op de onderstaande links om te lezen hoe je een berekeningsmethode configureert.

- {% link_new Erlang-C, Linear en Chat | features/forecast/injixo-forecast/staff-requirement.md | #geïntegreerde-berekeningsmethoden-configureren %}
- {% link_new Multiactiviteit | features/forecast/requirement-scripts/requirement-multiactivity.md %}
- {% link_new Outbound | features/forecast/requirement-scripts/requirement-outbound.md %}
- {% link_new Constante behoefte | features/forecast/requirement-scripts/requirement-constant.md %}

Opmerking: Lees het artikel {% link_new Het correcte behoeftescript selecteren | best-practices/requirement-scripts.md %} om te lezen welke methode het beste bij je usecase past.

## Geïntegreerde berekeningsmethoden configureren

De geïntegreerde methoden werken de resultaten van de personeelsbehoefteberekening bij op basis van nieuwe gegevensimports, gewijzigde berekeningsparameters of {% link_new handmatige wijzigingen | features/forecast/injixo-forecast/manual-adjustments.md %}.

1. Ga naar _Forecast_{:.doc-button} en selecteer een workload.
2. Scrol naar de sectie **Personeelsbehoefte**:

   - Klik in een nieuwe workload op _Berekeningsparameters configureren_{:.doc-button}.
   - Klik op _Berekeningsmethode bewerken_{:.doc-button} om de geconfigureerde berekeningsmethode te wijzigen.

4. Selecteer in het vervolgkeuzemenu **Berekeningsmethode** de berekeningsmethode Erlang C (voor oproepen), Chat of Linear (voor volumes die kunnen worden opgeslagen).
   Opmerking: Lees meer over [de optie Andere](#andere-berekeningsmethoden), die ook beschikbaar is in het vervolgkeuzemenu.

5. Configureer in de sectie **Berekeningsparameters** de [berekeningsparameters](#berekeningsparameters) voor de geselecteerde berekeningsmethode.
6. Selecteer in de sectie **Opslaglocatie** een eenheid en een activiteit. Als je [personeelsbehoeften voor planningsdoeleinden overzet](#de-personeelsbehoefte-overzetten-voor-planningsdoeleinden), sla ze dan hier op.

7. Klik op _Configuratie opslaan_{:.doc-button}.

### Berekeningsparameters

Er zijn verschillende verplichte en optionele parameters die afhankelijk zijn van de geselecteerde berekeningsmethode:

| Parameter                         | Details                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Beoogde servicegraad              | Percentage ontvangen oproepen of chats dat binnen de beoogde antwoordtijd moeten worden verwerkt.                                                                                                                                                                                                                                                                          |
| Beoogde antwoordtijd                | Tijd waarin het percentage oproepen of chats moet worden verwerkt dat in de parameter Beoogde servicegraad wordt gespecificeerd, bijvoorbeeld 80% van de oproepen binnen 20 seconden.                                                                                                                                                                                                     |
| Shrinkage                         | Het percentage ongeplande afwezigheid, bijvoorbeeld toiletbezoek en korte pauzes, medewerkers die te laat komen, onverwacht ziekteverlof of technische problemen. Om het totaal aantal benodigde medewerkers te bepalen, rekening houdend met shrinkage, `(s%)`, deel je het aantal medewerkers door `(1 - s%)`. Als je 70 medewerkers nodig hebt en het shrinkagepercentage 10% bedraagt, dan heb je in totaal 78 medewerkers nodig. |
| Minimale bezetting            | Voer een waarde in om intervallen te overschrijven met lagere waarden. In het dagaanzicht weergegeven als een horizontale lijn.                                                                                                                                                                                                                                                      |
| Maximale bezetting            | Voer een waarde in om intervallen te overschrijven met hogere waarden. In het dagaanzicht weergegeven als een horizontale lijn. Opmerking: De ingevoerde waarden kunnen de oorspronkelijk berekende waarden voor personeelsbehoefte overschrijven.                                                                                                                                                         |
| Vaste gemiddelde afhandeltijd (AHT) | Voer een waarde in om de voorspelde AHT te overschrijven met een vaste waarde. Selecteer **Gebruik de vaste AHT alleen wanneer er geen AHT-waarde beschikbaar is** om de vaste AHT-waarde alleen te gebruiken voor perioden waarin geen AHT-waarde als fallback beschikbaar is. Bij het berekenen van de personeelsbehoefte worden de AHT-waarden van de forecast gebruikt.                                  |
| Maximum aantal sessies                  | Maximaal aantal parallelle chatgesprekken dat medewerkers tegelijkertijd kunnen afhandelen.                                                                                                                                                                                                                                                                                   |
| Overhead                          | Percentage van de AHT dat medewerkers aan taken moeten besteden die zij niet tegelijkertijd kunnen uitvoeren, bijvoorbeeld nawerk-opmerkingen invoeren in het CRM-systeem. Deze parameter heeft geen effect als je bij Maximaal aantal sessies 1 invoert.                                                                                                                                              |

### Berekende personeelsbehoefte bekijken

In de sectie **Personeelsbehoefte** onderaan de pagina wordt een grafiek weergegeven met de berekende personeelsbehoefte. Boven de grafiek zie je de geconfigureerde waaren voor de parameters en het totaal aantal ingeplande uren dat nodig is voor de geselecteerde periode.

Beweeg de muis over de grafiek om een tooltip weer te geven met het volume, de AHT en het aantal medewerkers dat nodig is voor het interval (in het dagaanzicht) of het aantal ingeplande uren voor de dag (week- en maandaanzicht). Als je een vaste AHT-tijd hebt ingesteld, dan wordt in de tooltip de vaste waarde weergegeven in plaats van de voorspelde AHT.

{{ 1 | image: 'Grafiek voor personeelsbehoefte'}}

### De personeelsbehoefte overzetten voor planningsdoeleinden

Draag de personeelsbehoefte voor een bepaalde periode over om geoptimaliseerde planningen te maken of om een joboptimalisatie uit te voeren.

1. Ga naar _Forecast_{:.doc-button} en selecteer een **workload**.
2. Selecteer in het dag-, week-, of maandaanzicht een **tijdsperiode** waarvoor je de personeelsbehoefte wil overzetten.
3. (Optioneel) Selecteer in de sectie **Personeelsbehoefte** een **forecastversie** of de **geïmporteerde forecast** voor de berekening van de personeelsbehoefte in het vervolgkeuzemenu aan de rechterkant.

   > De geselecteerde waarde wordt teruggezet naar Auto-Forecast.
   >
   > Forecastversies en de geïmporteerde forecast moeten eerder al zijn opgeslagen voor de betreffende tijdsperiode. Lees meer over {% link_new forecastversies | features/forecast/injixo-forecast/store-forecast-versions.md %} of over hoe je {% link_new een forecast importeert | features/forecast/injixo-forecast/import-forecast.md %}.

4. Klik in de sectie **Personeelsbehoefte** op _Behoefte gebruiken_{:.doc-button}.  
   Het geselecteerde tijdsbestek, de eenheid en de activiteit worden in een nieuw venster weergegeven.  
   Als je bij het configureren van de berekeningsmethode voor de workload geen eenheid en activiteit hebt geselecteerd, dan wordt de volgende melding weergegeven: Niet toegewezen. Om dit te verhelpen, sluit je het venster en klik je op **Berekeningsmethode bewerken**.

5. Klik op _Opslaan_{:.doc-button} om de personeelsbehoefte over te zetten.  
   De personeelsbehoefte voor je activiteit is opgeslagen.  
   Je kunt de stappen voor de volgende workload herhalen of doorgaan met je planningsproces.

<!-- Header used in intercom forecast tour -->

## Andere berekeningsmethoden

De twee andere methodenn om de personeelsbehoefte te berekenen hebben een script nodig en configureren de parameters in een apart venster.

| Methode             | Gebruik                                                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Andere              | Berekeningsmethoden voor backoffice, berekeningen op basis van de gemiddelde antwoordtijd en de afbrekingspercentages.               |
| Andere scripts | Berekeningsmethoden voor multiactiviteit, outbound en de mogelijkheid om constante personeelsbehoeften te schrijven zonder een forecast. |

### De berekeningsmethode Andere instellen

1. Ga naar _Forecast_{:.doc-button} en selecteer een **workload**.
2. Klik in de sectie **Personeelsbehoefte** op _Edit calculation_{:.doc-button}.
3. Klik in het vervolgkeuzemenu **Berekeningsmethode** op **Andere**.
4. Klik op _Opslaan_{:.doc-button}.

Voer de scripts als volgt uit:

1. Selecteer de **tijdsperiode** waarvoor je de personeelsbehoefte wilt opslaan.
2. Klik op _Forecast gebruiken_{:.doc-button}.  
   De resultaten worden overgezet naar WFM.
3. Selecteer in de sectie **Personeelsbehoefte** een script in het vervolgkeuzemenu.
4. Configureer de parameters in het nieuwe venster of tabblad. Selecteer de volgende waarden voor de parameters Queue en Versie:
   - Parameter Queue: De queue die dezelfde naam heeft als de workload die begint met een asterisk (*).
   - Parameter Versie: De Auto-Forecast-versie
5. Klik op _OK_{:.doc-button} om het script uit te voeren.  
   De berekeningsresultaten worden in een venster weergegeven.

### De behoefte berekenen voor multiactiviteiten of outbound-campagnes

1. Ga naar _Forecast_{:.doc-button} en selecteer een **workload**.
2. Selecteer de **tijdsperiode** waarvoor je de personeelsbehoefte wilt aanmaken.
3. Om de forecast voor de gewenste periode in de Auto-Forecast-versie over te nemen, klik je op _Forecast gebruiken_{:.doc-button}.

   > Voordat je het script voor multiactiviteiten start, klik je in elke workload voor de deelactiviteiten op _Forecast gebruiken_{:.doc-button}

4. Klik op **Berekeningen voor multiactiviteit, constante behoefte en outbound** in de rechter bovenhoek.
5. Selecteer een **behoeftescript** in het vervolgkeuzemenu.
6. Configureer de parameters in het nieuwe venster of tabblad. Selecteer de volgende waarden voor de parameters Queue en Versie:
   - Parameter Queue: De queue die dezelfde naam heeft als de workload die begint met een asterisk (*). Selecteer bij multiactiviteiten de juiste workloads voor de deelactiviteiten.
   - Parameter Versie: De Auto-Forecast-versie
7. Klik op _OK_{:.doc-button} om het script uit te voeren.  
   De waarden voor de personeelsbehoefte worden opgeslagen. De berekeningsresultaten worden in een nieuw venster weergegeven.

## Constante personeelsbehoeften schrijven

1. Ga naar _Forecast_{:.doc-button}.
2. Klik op **Berekeningen voor multiactiviteit, constante behoefte en outbound**.
3. Selecteer het **Constante behoeftescript** in het vervolgkeuzemenu.
4. Configureer de parameters in het nieuwe venster of tabblad. Lees meer over {% link_new het Constante behoeftescript | features/forecast/requirement-scripts/requirement-constant.md %}.
5. Klik op _OK_{:.doc-button} om het script uit te voeren.  
   De waarden voor de personeelsbehoefte worden opgeslagen. De berekeningsresultaten worden in een nieuw venster weergegeven.
