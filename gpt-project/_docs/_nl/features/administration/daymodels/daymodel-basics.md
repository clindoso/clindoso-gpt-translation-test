---
title: Dagmodellen begrijpen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lees welke dagmodellen er zijn, waar je voor en na het aanmaken van een dagmodel rekening mee moet houden en wat het voor de planning betekent als je een dagmodel wijzigt.
related_articles:
  - overwrite_title: Dagmodellen aanmaken
    filepath: features/administration/daymodels/daymodel-creation.md
---

Dagmodellen zijn sjablonen voor diensten. Ze staan voor de werkdag van je ingeplande medewerkers en bepalen de begin- en eindtijden van diensten, hoeveel uur een medewerker per dag werkt en wanneer medewerkers beschikbaar zijn voor werk. injixo genereert diensten op basis van je dagmodellen.

De dagmodellen die je aanmaakt worden standaard automatisch aan alle eenheden van je bedrijf toegewezen. Om deze standaardinstelling te wijzigen, kun je de {% link_new eenheid bewerken | features/administration/create-and-manage-planning-units.md | #dagmodellen-beperken %}. Tijdens de planningsoptimalisatie houdt injixo alleen rekening met dagmodellen die aan de eenheid zijn toegewezen.

Als de dagmodellen die voor je eenheid zijn geconfigureerd niet aan alle werkafspraken voldoen, kun je ook persoonlijke dagmodellen aan individuele medewerkers toewijzen. Tijdens de planningsoptimalisatie gebruikt injixo deze persoonlijke dagmodellen alleen voor de betreffende personen.

Dagmodellen bevatten de activiteiten van het type aanwezigheid, afwezigheid en pauze binnen een dienst. Daarom is het belangrijk dat je {% link_new relevante activiteiten aan dagmodellen toevoegt | features/administration/daymodels/daymodel-creation.md | #activiteiten-aan-dagmodellen-toevoegen %}.

Dagmodellen worden aan {% link_new dienstenseries | features/administration/shift-sequences.md %} toegevoegd en kunnen worden ingedeeld in {% link_new weekpatronen | features/administration/work-time-pattern-models.md | #weekmodellen-aanmaken %}.


## Typen dagmodellen

Er zijn drie typen dagmodellen. 

> Opmerking
> 
> - Dagmodellen van het type Gefixeerde dienst worden ook wel gefixeerde dagmodellen genoemd.<br> 
> - Dagmodellen van het type Variabele dienst worden ook wel variabele dagmodellen genoemd.


| Type                | Beschrijving                                                                                                                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gefixeerde dienst         | Diensten met een gefixeerd dagmodel hebben een vaste begin- en eindtijd die niet kan worden verschoven. Bij een gefixeerd dagmodel is er altijd maar één dienst mogelijk. Gefixeerde dagmodellen worden meestal aan {% link_new dienstenseries | features/administration/shift-sequences.md %} toegevoegd.                                      |
| Variabele dienst      | Diensten met een variabel dagmodel hebben een flexibele begintijd binnen een gedefinieerde tijdsspanne. Dit resulteert in meerdere mogelijke diensten. Variabele dagmodellen die aan dienstenseries worden toegevoegd, worden automatisch gefixeerde dagmodellen, omdat ze op de eerstvolgende begintijd van een dienst worden ingesteld. |
| Beschikbaarheidskader | Dit dagmodeltype wordt gebruikt om een tijdsbereik in te stellen dat korter is dan de openingstijden van de eenheid. Nadat je dienstenseries met dit dagmodeltype hebt ingevoerd, selecteert injixo bij de optimalisatie en inschrijven op diensten dagmodellen die compatibel zijn met deze beschikbaarheidsperiode. Je kunt dit type ook gebruiken om de beschikbaarheid voor verschillende medewerkers tegelijkertijd te configureren.          |

## Wanneer je welk dagmodel moet gebruiken bij het plannen

Er kunnen meerdere redenen zijn om een bepaald type dagmodel te kiezen. In de volgende lijst vind je een algemeen advies:

- Gefixeerde dienst: Gebruik gefixeerde dagmodellen om medewerkers met vaste werktijden in te plannen. Hun diensten beginnen en eindigen altijd op een vaste tijd en kunnen niet binnen de planning worden verschoven.
Je kunt vaste dagmodellen in weekpatronen gebruiken om {% link_new geoptimaliseerde planningen aan te maken | features/scheduling/scheduling-optimization.md %}, om zich herhalende weekpatronen te definiëren in {% link_new dienstenseries | features/scheduling/capacity/capacity-insert-shift-sequences.md %} of als je {% link_new inschrijven op diensten | features/scheduling/schedules/schedules-shift-bidding.md %} gebruikt.
- Variabele dienst:  Gebruik variabele dagmodellen om medewerkers met flexibele werktijden in te plannen. injixo kan een medewerker met een enkel dagmodel van dit type voor verschillende diensten inplannen. Dit dagmodel wordt gewoonlijk gebruikt bij het {% link_new aanmaken van geoptimaliseerde planningen | features/scheduling/scheduling-optimization.md %} of in {% link_new inschrijven op diensten | features/scheduling/schedules/schedules-shift-bidding.md %}.
- Beschikbaarheidskader: Als de openingstijden van je eenheid een grotere tijdsspanne beslaan dan één werkdag, dan kun je de opties van injixo om medewerkers in te plannen beperken. Om de beschikbaarheid voor meerdere medewerkers tegelijkertijd te beperken, gebruik je dagmodellen van het type Beschikbaarheidsperiode en voeg je ze toe aan dienstenseries. Als alternatief kun je de {% link_new beschikbaarheid voor afzonderlijke medewerkers configureren | features/administration/availabilities.md %} in de medewerkerinstellingen. Bij de planningsoptimalisatie wordt met beide instellingen rekening gehouden, zolang planningsregel 2611 is geactiveerd.

Als alternatief voor beschikbaarheid kun je {% link_new dienstenseries | features/administration/shift-sequences.md %} of weekmodellen in {% link_new planningsmodellen | features/administration/work-time-pattern-models.md | #weekmodellen-aanmaken %} gebruiken. Je kunt ze allebei ook gebruiken om vroege en late diensten te roteren.

We raden aan om een beperkt aantal variabele dagmodellen aan te maken (in combinatie met {% link_new beschikbaarheid van je medewerkers | features/administration/availabilities.md | #medewerkersbeschikbaarheden-aanmaken %}) in plaats van een groot aantal gefixeerde dagmodellen aan te maken.

## Basisactiviteit en dienstduur

Voor gefixeerde en variabele dagmodellen moet je voor elk dagmodel altijd een basisactiviteit instellen om de totale dienstduur te definiëren. Zowel in flexibele als gefixeerde dagmodellen kun je meer activiteiten toevoegen die de basisactiviteit overlappen. De duur van de overige activiteiten mag de tijdsduur van de basisactiviteit niet overschrijden.

De basisactiviteit beslaat de totale tijd dat een ingeplande medewerker aanwezig is tijdens een dienst, inclusief pauzes en andere onbetaalde activiteiten. Het is de eerste activiteit die je selecteert bij het maken van een nieuw dagmodel. Je kunt deze niet verwijderen of bewerken nadat het dagmodel is opgeslagen.

De totale tijd van een ingeplande dienst inclusief pauzes is de bruto dienstduur. Na aftrek van onbetaalde activiteiten, zoals pauzes of opstarttijden, is de resulterende werktijd de netto dienstduur. Je kunt de netto dienstduur zien onder de naam Werkelijke tijd in Schedules en het Dienstrooster-Center. Let op dat in contracten ook nettotijden worden vermeld. 

De lengte van een dagmodel moet voldoen aan de werkuren in je {% link_new contracten | features/administration/create-contracts.md %}.
Voor een contract van 40 werkuren per week, verdeeld over 5 weekdagen, is een dagmodel nodig met een nettowerktijd van 8 uur per dag. Voor een contract van 37,5 uur per week is een dagmodel met 7,5 uur nodig.

Gebruik de activiteit Aanwezigheid als basisactiviteit en zorg ervoor dat deze is geconfigureerd als Vervangbaar. Vervolgens kunnen de functionaliteiten Joboptimalisatie en Geoptimaliseerde planning maken de activiteit Aanwezigheid door andere activiteiten vervangen, zolang ze een {% link_new berekende personeelsbehoefte | features/forecast/injixo-forecast/staff-requirement.md %} hebben en geconfigureerd zijn als Planbaar.

### Gefixeerde elementen versus corridors

Je kunt een corridorelement aanmaken als je een activiteit toevoegt met een tijdsduur die korter is dan de tijd tussen de begin- en eindtijd van het element. Corridorelementen overlappen alle vaste elementen in een dienst. Geoptimaliseerde planning verplaatst de corridorelementen om de dekking te optimaliseren. Corridors kunnen elkaar overlappen, maar activiteiten in twee corridors kunnen dat niet.

Als je handmatig een dagmodel in de planning invoert, worden corridorelementen op de vroegst mogelijke tijd van de corridor geplaatst. Je kunt corridors handmatig verplaatsen binnen de gedefinieerde intervallen.

Als de duur van een corridorelement exact overeenkomt met het geconfigureerde begin- en eindtijdelement, wordt in plaats daarvan een gefixeerd element aangemaakt.

