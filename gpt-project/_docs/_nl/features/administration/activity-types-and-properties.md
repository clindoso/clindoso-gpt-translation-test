---
title: Activiteitentypen en -eigenschappen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lees meer over de verschillende typen activiteiten en het doel van elke configuratie-optie voor activiteiten.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Eenheden configureren
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Personen met meerdere kwalificaties inplannen
    filepath: best-practices/how-to-schedule-multiskill-agents.md
redirect_from:
  - /nl/activity-properties/
redirect_reason: Updated filename on 11 October 2023
---

Bij het maken en bewerken van activiteiten beïnvloeden de verschillende configuratieopties hoe activiteiten in je planningen en rapporten worden gebruikt en weergegeven.

## Activiteitentype

Het activiteitentype heeft invloed op je planning en bepaalt:
- hoe Geoptimaliseerde planning met de activiteit omgaat.
- waar je de activiteit kunt gebruiken.
- hoe de activiteit in Schedules en Dienstrooster-Center wordt weergegeven.
- of de activiteit in rapporten wordt opgenomen. <!-- illness, absences, vacation -->

In de volgende tabel vind je meer informatie over elk activiteitentype:

| Type           | Beschrijving        |
| -------------- | ------------------- | ---------------------------------------------------- |
| Aanwezigheid   | Alle activiteiten waar medewerkers aan werken.<br>Activiteiten van het type Aanwezigheid worden door injixo op basis van de personeelsbehoefte ingepland.                               |
| Pauze          | Betaalde of onbetaalde pauzes in een dienst.<br>Alleen activiteiten van het type Pauze kunnen in dagmodellen als pauze-activiteit worden geconfigureerd. Je kunt de functionaliteit {% link_new pauze-optimalisatie | features/scheduling/schedules/break-optimization.md %} gebruiken om pauzes te verdelen over de planningen om een optimale dekking te bereiken voor activiteiten met personeelsbehoefte. |
| Ziek           | Betaalde of onbetaalde afwezigheid zoals ziekteverlof of een afspraak bij de dokter.<br>In ziekterapporten worden alleen activiteiten van het type Ziek weergegeven.                    |
| Vakantie          | Betaald of onbetaald verlof, collectieve vrije dagen, etc.<br> In vakantierapporten worden alleen activiteiten van het type Vakantie weergegeven.                                    |
| Afwezigheid  | Overige afwezigheid die van invloed is op de planning, bijvoorbeeld externe training, overurencompensatie, etc.<br>In afwezigheidsrapporten worden alleen activiteiten van het type Afwezigheid weergegeven.              |
| Vergadering  | Activiteitentype om {% link_new vergaderingen te plannen | features/scheduling/meetings/meetings-overview.md %}. |

## Activiteiteneigenschappen

Activiteiteneigenschappen hebben invloed op je planning en hoe je de activiteit kunt gebruiken.
Je kunt activiteiteneigenschappen instellen via de volgende selectievakjes.

| Eigenschap                                    | Effect                                                                                                                                                                                                                                                                                                                 
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Betaald                                     | Activeert de berekening van de werktijd voor ingeplande activiteiten. Als pauzes of afwezigheid worden betaald, dan tellen ze mee als werktijd. Als ze niet worden betaald, dan tellen ze niet mee bij de berekening van de nettowerktijd.   |
| Rusttijd aanhouden                          | Voorkomt niet-naleving van de rusttijd die in het contract is overeengekomen. injixo controleert de rusttijd alleen als planningsregel _2601_{:.id-label} is geactiveerd. |
| Planbaar                                    | injixo kan de activiteit inplannen als je de functionaliteit Geoptimaliseerde roosters maken gebruikt, of de activiteit optimaliseren tijdens de job-optimalisatie. Deze eigenschap wordt meestal gebruikt voor activiteiten met personeelsbehoefte. Dat is meestal niet het geval voor activiteiten van het type Afwezigheid, Vakantie en Ziek.              |
| Aanvraagbaar in Me                          | Zorgt ervoor dat medewerkers in injixo Me verlof en ziekteverlof kunnen aanvragen (afwezigheid, vakantie en ziek) als er een {% link_new verlofperiode | features/scheduling/time-off/time-off-periods.md %} is met de status Gepubliceerd). Bij inschrijven op diensten kunnen activiteiten van het type Aanwezigheid en Pauze automatisch worden aangevraagd. |
| Ruilbaar via Diensten ruilen                | Zorgt ervoor dat medewerkers {% link_new de activiteit met elkaar kunnen ruilen | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %} in injixo Me. Hiervoor moeten alle activiteiten (inclusief pauzes) in dagmodellen worden geconfigureerd als **Ruilbaar via Diensten ruilen**.    |
| Overbezetting toestaan als personeelsbehoefte nul is | injixo kan de activiteit zelfs inplannen op tijden zonder personeelsbehoefte. Standaard worden intervallen met nulbehoeften niet gedekt.  |
| Vervangbaar                               | injixo kan de activiteit vervangen door andere planbare activiteiten met personeelsbehoefte. Dit is nodig om {% link_new vergaderingen in te plannen | features/scheduling/meetings/meetings-overview.md %} op deze activiteit. |
| Toestaan als Activiteit over de hele dag                | Je kunt de activiteit voor een hele dag inplannen in Schedules of onder het tabblad Activiteiten over de hele dag in het dagaanzicht in het Dienstrooster-Center. Als deze activiteit als betaalde activiteit is geconfigureerd, dan krijgt de betreffende medewerker de bijbehorende dagelijkse target toegewezen, zoals vermeld in het contract.<br>Vereist om collega's toe te staan om de activiteit in injixo Me aan te vragen als Activiteit over de hele dag.   |
| Kan een dagstatus zijn                    | Alleen beschikbaar voor Activiteiten over de hele dag. Dagstatus zorgt ervoor dat je de activiteit handmatig met een dagstatus in het Dienstrooster-Center kunt inplannen via het tabblad Activiteiten over de hele dag. Zo blijft het vervangen planningsitem bewaard, zodat deze op een later moment kan worden geraadpleegd. Als gevolg worden medewerkers die voor een activiteit met deze eigenschap zijn ingepland door injixo uitgesloten bij de dekkingsberekening, maar de oorspronkelijke vermelding in de planning blijft zichtbaar. |
| Speciale behandeling in geoptimaliseerde planning | Alleen beschikbaar voor activiteiten van het type Aanwezigheid. Activiteiten met deze eigenschap kunnen alleen strikt worden gepland zoals ze zijn geconfigureerd. De activiteiten kunnen niet worden vervangen en hun tijdsduur is niet flexibel. <br>Lees meer in de [sectie hieronder](#speciale-behandeling-in-geoptimaliseerde-planning).

## Speciale behandeling in geoptimaliseerde planning

Deze activiteiteneigenschap geeft aan dat de functionaliteit Geoptimaliseerde planning de activiteit alleen strikt kan inplannen zoals deze is geconfigureerd. Deze eigenschap wordt meestal gebruikt voor het plannen van overwerk of backoffice-activiteiten.<br>
Er zijn twee verschillende gebruiksscenario's voor deze activiteiteneigenschap:

Optie 1: De activiteit is onderdeel van een dagmodel. In dit geval kan de activiteit alleen worden gepland voor de geconfigureerde tijdsduur en binnen het tijdsbestek dat is gedefinieerd in het dagmodel. De activiteit kan niet worden gebruikt om andere vervangbare activiteiten te vervangen. Hoe Geoptimaliseerde planning omgaat met de activiteit hangt ook af van {% link_new hoe de activiteit is geconfigureerd binnen het dagmodel | features/administration/daymodels/daymodel-creation.md %}:
- Geconfigureerd als vast element. Geoptimaliseerde planning plant de activiteit alleen in op precies dezelfde tijd waarvoor deze is geconfigureerd.
- Geconfigureerd als corridorelement: Planningsoptimalisatie kan de activiteit binnen de gedefinieerde corridor verplaatsen om de dekking van andere activiteiten te optimaliseren.

Voorbeeld:

- Je voegt een backoffice-activiteit zonder personeelsbehoefte en met een tijdsduur van één uur toe aan je dagmodel. Geoptimaliseerde planning plant de activiteit voor exact een uur in. Als de activiteit in het dagmode is geconfigureerd als een corridorelement, dan wordt de activiteit binnen de corridor verplaatst naar het tijdslot waar deze de dekking voor andere activiteiten zo min mogelijk beïnvloedt.

Optie 2: De activiteit is niet toegevoegd aan dagmodel. In dit geval kan Geoptimaliseerde planning de activiteit niet automatisch plannen, en deze ook niet gebruiken om andere vervangbare activiteiten te vervangen. De activiteit kan alleen handmatig worden ingepland.

Voorbeeld:

- Maak een overwerkactiviteit aan die geen deel uitmaakt van een dagmodel. De functionaliteit Geoptimaliseerde planning plant de activiteit niet in en gebruikt deze ook niet om andere activiteiten te vervangen. Voeg de activiteit indien nodig handmatig toe aan je planning. In dit geval heb je altijd de volledige controle over wanneer de activiteit is ingepland, voor welke tijdsduur en aan wie deze wordt toegewezen.

> Opmerking
>
> De eigenschap is alleen beschikbaar nadat je de activiteit hebt aangemaakt.

## Deelactiviteiten

Je kunt activiteiten aan andere activiteiten toewijzen. De activiteit waaraan activiteiten worden toegewezen, wordt dan een multiactiviteit. De toegewezen activiteiten zijn de deelactiviteiten van de multiactiviteit. Met multiactiviteiten kan injixo collega's inplannen die meerdere kwalificaties hebben als een van deze kwalificaties nodig is. In de lijst met activiteiten worden multiactiviteiten voorzien van het pictogram <em class="multiactivity-icon"></em>.

De functionaliteit Geoptimaliseerde planning maken kan multiactiviteiten inplannen als aan de volgende criteria is voldaan:

- Selecteer voor de multiactiviteit en alle deelactiviteiten het type Aanwezigheid.
- Configureer zowel de multiactiviteit als de deelactiviteiten als betaald en planbaar.
- Wijs alle deelactiviteiten (en de multiactiviteit in een tweede stap) toe aan je eenheid.
- Om te controleren wie er kan worden ingepland, wijs je aan elke deelactiviteit een andere kwalificatie toe.
- (Optioneel) Wijs een kwalificatie toe aan de multiactiviteit. In dit geval moeten collega's deze extra kwalificatie hebben om de multiactiviteit uit te kunnen voeren. Standaard vereist de multiactiviteit zelf geen kwalificaties.

> Opmerking
>
> Als je de functionaliteit Geoptimaliseerde planning maken niet gebruikt, maar alleen de job-optimalisatie uitvoert, dan kan injixo vervangbare activiteiten door multiactiviteiten vervangen. Voorwaarde hiervoor is dat een persoon minimaal een deelactiviteit van de multiactiviteit kan uitvoeren.
