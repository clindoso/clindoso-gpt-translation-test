---
title: Planningsmethoden
promote-service: new-planner-training
description: Lees meer over de verschillende planningsmethoden in injixo.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Planningsmethoden combineren
    filepath: features/scheduling/combined-scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/set-a-validity-period.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
---

injixo werkt met verschillende planningsmethoden die je afzonderlijk of als {% link_new combinatie | features/scheduling/combined-scheduling-methods.md %} kunt gebruiken.

De verschillende planningsmethoden zijn ontworpen voor verschillende usecases. Alle planningsmethoden houden rekening met de informatie in de {% link_new contracten | features/administration/create-contracts.md %} van je medewerkers, zoals het aantal werkdagen, het aantal werkuren per dag, week of maand, en andere planningsparameters.

## Vereisten

Voordat je planningsmethoden kunt gaan gebruiken, moeten onder _Plan > Configuratie_{:.breadcrumbs} de volgende configuratiegegevens zijn ingesteld:

- Kwalificaties
- Activiteiten
- Dagmodellen
- Eenheden
- Contracten
- Medewerkers

Voor sommige planningsmethoden zijn aanvullende configuratiegegevens nodig, bijvoorbeeld dienstenseries of planningsmodellen.

## Gefixeerde planning

De methode Gefixeerde planning is gebaseerd op {% link_new dienstenseries | features/administration/shift-sequences.md %}. Een dienstenserie is een weekpatroon van dagmodellen of activiteiten dat aangeeft op welke dag medewerkers werken en wat de exacte begin- en eindtijden van hun diensten zijn. Zodoende is gefixeerde planning de meest consistente, maar ook minst flexibele planningsmethode.

Planningen die op basis van dienstenseries zijn aangemaakt, kunnen elke dag hetzelfde zijn of in intervallen van 2 tot 53 weken veranderen.

Nadat de planning is geoptimaliseerd, kun je nog {% link_new Pauzes optimaliseren | features/scheduling/schedules/break-optimization.md %} of de {% link_new Joboptimalisatie | features/scheduling/schedules/schedules-job-optimization.md %} gebruiken om je planning verder te optimaliseren.

**Pauzes optimaliseren** verschuift ingeplande pauzes naar tijdslots waar ze de minste impact hebben op je dekking. injixo kan pauzes alleen verschuiven binnen een {% link_new corridor in een dagmodel | features/administration/daymodels/daymodel-basics.md | #gefixeerde-elementen-versus-corridors %}.

**Joboptimalisatie** kan activiteiten die als vervangbaar zijn geconfigureerd vervangen door andere planbare activiteiten om voor alle activiteiten een optimale dekking te bereiken, op basis van de personeelsbehoefte. De begin- en eindtijden van diensten blijven ongewijzigd. **Joboptimalisatie** kan ook de pauzetijden in een planning optimaliseren, op een vergelijkbare manier als **Pauzes optimaliseren** dat doet.

## Geoptimaliseerde planning

De methode Geoptimaliseerde planning biedt de meeste flexibiliteit. Bij deze methode gebruik je de functionaliteit {% link_new Geoptimaliseerde planning maken | features/scheduling/schedules/schedules-optimized-schedules.md %} om automatisch een volledige planning aan te maken. injixo zorgt daarbij voor een optimale dekking voor alle activiteiten, waarbij zo min mogelijk medewerkers worden ingepland.

Standaard kan de functionaliteit **Geoptimaliseerde planning maken** medewerkers inplannen op basis van alle {% link_new dagmodellen | features/administration/daymodels/daymodel-basics.md %} die aan hun eenheid zijn toegewezen en compatibel zijn met hun contract. 

Afhankelijk van je configuratie kan het gebruik van verschillende dagmodellen leiden tot zeer inconsistente planningen. Zo kunnen medewerkers op maandag een nachtdienst krijgen, op dinsdag een middagdienst en op woensdag een ochtenddienst.

Om te bepalen welke dagmodellen kunnen worden gebruikt om een planning aan te maken, gebruik je {% link_new planningsmodellen | features/administration/work-time-pattern-models.md %}. Een planningsmodel bestaat uit {% link_new weekmodellen | features/administration/work-time-pattern-models.md | #weekmodellen-aanmaken %} en bepaalt hoe dagmodellen aan je medewerkers worden toegewezen. Met planningsmodellen kun je herhalende patronen van diensten aanmaken en planningsbeperkingen instellen voor de functionaliteit **Geoptimaliseerde planning maken**.

Om een medewerker met een of meerdere planningsmodellen in te plannen, wijs je alle betreffende planningsmodellen aan hen toe. Dit moet je voor elke medewerker individueel doen.

### Volledig flexibele diensten

Om planningen aan te maken met volledig flexibele diensten, maak je planningsmodellen van het {% link_new type A | features/administration/work-time-pattern-models.md | #planningsmodeltypen %} aan, die je vervolgens aan je medewerkers toewijst.

Met type A kan injixo elk dagmodel uit het planningsmodel selecteren voor elke dag van elke week, zolang dit compatibel is met het contract van de medewerker.

Met deze methode maak je de beste planningen aan die aan de bedrijfsbehoeften voldoen. Tegelijkertijd kan dit zorgen voor zeer inconsistente planningen, wat een negatieve invloed kan hebben op je medewerkers. Om deze negatieve impact te verlagen, kun je bepaalde diensten voor bepaalde mensen uitsluiten door individuele dagmodellen aan hen toe te wijzen, of door [beschikbaarheden](#beschikbaarheden) te gebruiken.

### Flexibele diensten rouleren

Om planningen aan te maken met roulerende flexibele diensten, maak je planningsmodellen van het {% link_new type B, C of D | features/administration/work-time-pattern-models.md | #planningsmodeltypen %} aan, die je vervolgens aan je medewerkers toewijst.

Bij type B, C of D bepaal je een specifieke volgorde die injixo aanhoudt bij het selecteren van dagmodellen die in het geselecteerde planningsmodel beschikbaar zijn en compatibel zijn met de contracten van je medewerkers. Je kunt ook een vaste begintijd instellen voor de diensten of een tijdskader instellen waarin de dienst begint.

### Beschikbaarheden

Je kunt {% link_new beschikbaarheden | features/administration/availabilities.md %} gebruiken om in te stellen dat medewerkers op een bepaalde dag, of gedurende een aantal uren, niet beschikbaar zijn om te werken. Beschikbaarheden vullen de beperkingen aan die voortkomen uit contracten en de openingstijden van eenheden.

Medewerkers aan wie beschikbaarheden zijn toegewezen, kunnen alleen worden ingepland voor diensten die binnen de tijdskdaders passen waarin zij beschikbaar zijn.

## Inschrijven op diensten

Als je gebruikmaakt van {% link_new Inschrijven op diensten | features/scheduling/schedules/schedules-shift-bidding.md %}, dan wordt de uiteindelijke planning altijd pas aangemaakt nadat medewerkers de kans hebben gehad om voorkeursdiensten aan te vragen in injixo Me.

Volg deze stappen om een planning aan te maken op basis van Inschrijven op diensten:

1. Bepaal hoeveel diensten je voor een {% link_new planningsperiode | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} nodig hebt.
2. {% link_new Maak diensten aan | features/scheduling/schedules/schedules-shift-bidding.md | #diensten-genereren %} op basis van de voorspelde personeelsbehoefte.
3. Stel de status van je planningsperiode in op **Gepubliceerd**. Medewerkers kunnen twee diensten per dag aanvragen (maximaal 10).
4. Begin met het {% link_new verloten | features/scheduling/shift-bidding.md | #lottery-of-requested-shifts %} van de aangevraagde diensten.
5. Wijs de resterende diensten toe. Medewerkers wier aanvragen niet zijn ingewilligd, worden bij deze stap ingepland.

Nadat de planning is aangemaakt, kun je nog steeds de {% link_new Joboptimalisatie | features/scheduling/schedules/schedules-job-optimization.md %} uitvoeren om de ingeplande activiteiten en de pauzetijden te optimaliseren.

> Gebruik de activiteit Aanwezigheid als je Inschrijven op diensten en **Joboptimalisatie** combineert.
>
> Als medewerkers diensten aan kunnen vragen in injixo Me, maar je later **Joboptimalisatie** wilt gebruiken, gebruik dan alleen standaard systeemactiviteit Aanwezigheid (activiteiten-ID: 1) als activiteit in de dagmodellen. Zo voorkom je dat medewerkers diensten met specifieke activiteiten aanvragen, en vervolgens door de **Joboptimalisatie** aan totaal andere activiteiten worden toegewezen.
