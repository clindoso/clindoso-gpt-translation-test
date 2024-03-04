---
title: Inschrijven op diensten instellen
product_label:
  - advanced
  - enterprise
description: Diensten genereren zodat collega's zich kunnen inschrijven op diensten, medewerkers uitnodigen om zich in te schrijven op diensten, een verloting organiseren en de planning publiceren (Schedules).
related_articles:
  - overwrite_title: injixo Me configureren
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
  - overwrite_title: Wat zijn planningsperioden?
    filepath: features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md
  - overwrite_title: Medewerkersbehoefte bewerken of verwijderen
    filepath: features/scheduling/edit-or-delete-staff-requirements.md
  - overwrite_title: Dienstenbehoefte gebruiken
    filepath: features/scheduling/schedules/schedules-shift-requirement.md
  - overwrite_title: Inschrijven op diensten instellen
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
  - overwrite_title: Verzoeken voor diensten ruilen bekijken en goedkeuren
    filepath: features/scheduling/view-approve-shift-swap-requests.md
  - overwrite_title: Meldingen
    filepath: getting-started/notifications.md
---

Via Inschrijven op diensten kunnen je collega's actief deelnemen aan het planningsproces door zich in te schrijven op diensten. Stel eerst een roosterperiode in en genereer diensten om aan de slag te gaan.

## Inschrijven op diensten

Voordat je het inschrijven op diensten gaat starten, dien je eerst {% link_new de personeelsbehoefte te berekenen | features/forecast/injixo-forecast/calculate-staff-requirements.md %} en eventueel {% link_new dienstenseries in te voegen | features/scheduling/schedules/schedules-insert-shift-sequences.md %}.

1. Maak in Schedules een {% link_new roosterperiode | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md | #planningsperioden-aanmaken %} aan met de status Niet gepubliceerd.
2. Voer [minimum- en maximumwaarden](#je-dienstenmix-specificeren) in voor elk dagmodel in de tabel met dienstenbehoeften.
3. [Maak de diensten aan](#diensten-genereren).
4. Nodig medewerkers uit om zich [in injixo Me op diensten in te schrijven](#medewerkers-uitnodigen-om-zich-op-diensten-in-te-schrijven).
5. Als de periode voor het inschrijven op diensten is verlopen, kun je de [diensten verloten](#diensten-verloten-starten) en de [resterende diensten](#resterende-diensten-toewijzen) toewijzen waarop niemand zich heeft ingeschreven.
6. [Optimaliseer activiteiten en pauzes en publiceer de planning](#de-planning-optimaliseren-en-publiceren).

## Je dienstenmix specificeren

Voordat je de diensten aanmaakt waarop medewerkers zich kunnen inschrijven, moet je bepalen wat voor soort diensten je in de mix wilt opnemen. Pas eerst de waarden voor elke nieuwe roosterperiode aan voordat je begint met het genereren van diensten. Anders maakt injixo niet de juiste diensten aan die nodig zijn om de personeelsbehoefte te dekken.

1. Ga naar _Plan > Schedules_{:.breadcrumbs}.
2. Klik op _Roosterperiodes_{:.doc-button}.
3. Om de dienstenbehoefte aan te passen, beweeg je de cursor over **Roosterperiode** en klik je vervolgens aan de rechterkant op het {% icon ellipsis_v %}.
4. Selecteer _Aanpassen diensten genereren_{:.doc-button} in het overloopmenu.
5. In de tabel met dienstenbehoeften voer je {% link_new **Min-** en **Max-** waarden | features/scheduling/schedules/schedules-shift-requirement.md | #enter-required-shifts-into-the-table %} in voor je dagmodellen.

## Diensten genereren

Bij het genereren van diensten worden diensten aangemaakt voor elke dag in de planningsperiode. injixo houdt rekening met zowel bestaande diensten in de planning als met personeelsbehoeften om voor een optimale dekking te zorgen.

1. Ga naar _Plan > Schedules_{:.breadcrumbs}.
2. Klik op _Roosterperiodes_{:.doc-button}.
3. Beweeg de cursor over de **Roosterperiode** waarvoor je diensten wilt genereren en klik op het {% icon ellipsis_v %} aan de rechterkant.
4. Selecteer in het overloopmenu _Diensten genereren_{:.doc-button}.
   {{ 2 | image: 'Roosterperioden met dienstenfuncties', '80%' }}
5. (Optioneel) Wijzig de waarde voor **Vereiste diensten genereren**.

   - Optie **van de medewerkersbehoefte**: Bij een waarde van 100% dekt injixo de personeelsbehoefte met exact 100%. Bij een waarde van meer dan 100% worden er meer diensten gegenereerd dan door de behoefte worden gespecificeerd. Een waarde van minder dan 100% leidt tot minder diensten (nuttig als het aantal beschikbare medewerkers te laag is om de behoefte te dekken).
   - Optie **van het aantal uren in het contract**: Bij een waarde van 100% zorgt injixo ervoor dat alle medewerkers met de gegenereerde diensten aan het aantal uren in hun contract komen.

6. Klik op _Diensten genereren_{:.doc-button} om het genereren van diensten te starten.
    Zodra de diensten zijn gegenereerd, vind je in de JobProcessor een rapport met informatie over de invoergegevens en het resultaat.

   {{ 3 | image: 'Parametervenster voor dienstengeneratie', '50%' }}

Opmerking: In het Dienstrooster-Center kun je het resultaat van de dienstengeneratie overschrijven door {% link_new het aantal diensten te wijzigen dat voor een enkele dag is gegenereerd | features/scheduling/edit-or-delete-staff-requirements.md %} om bijvoorbeeld een enkele dag aan te passen voor testdoeleinden.

Het Dienstrooster-Center geeft de belangrijkste cijfers weer voor de dienstengeneratie. Je vindt ze in het {% link_new parametervenster | features/scheduling/shiftcenter/shift-center-overview.md | #parameter-window %} onderaan de pagina.

- Behoefte (onder het tabblad Dagmodellen): aantal gegenereerde diensten voor elk individueel dagmodel
- Bezetting volgens dienstenbehoefte (onder het tabblad Activiteiten): aantal gegenereerde diensten met de geselecteerde activiteit
  <!-- You can also rate the quality of a shift generation, as you can see here how the employee requirement would be covered if all generated shifts were staffed. -->
- Dekking volgens dienstenbehoefte (onder het tabblad Activiteiten): verschil tussen benodigde en gegenereerde diensten

## Medewerkers uitnodigen om zich op diensten in te schrijven

Nadat je diensten hebt gegenereerd, ga je als volgt te werk:

1. Wijzig de **status** van de {% link_new planningsperiode | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md | #status %} naar Shift bidding geactiveerd.
   Medewerkers ontvangen een [melding](#e-mail--en-browser-pushmeldingen).
2. (Optioneel) Voeg een **deadline** toe om een datum in te stellen waarvoor medewerkers zich op diensten kunnen inschrijven.
   Medewerkers schrijven zich op een dag in op twee diensten. Iedereen kan zich inschrijven op dezelfde dienst.
   Om de waarschijnlijkheid dat een dienst wordt toegewezen in te kunnen schatten, en eventueel alternatieve diensten te vinden, kunnen medewerkers zien hoeveel diensten er nodig zijn en hoeveel inschrijvingen er op de diensten zijn.

   > Inschrijvingen in injixo Me zijn beperkt tot uiterlijk 100 dagen van tevoren (voor planningsperioden > 100 dagen).

3. Als de inschrijvingsperiode voorbij is (of als de deadline is verstreken), zet je de planningsperiode terug naar **status** Niet gepubliceerd.

Om de inschrijvingen van andere medewerkers te bekijken, ga je naar Schedules of het Dienstrooster-Center en voeg je het aanzicht Aanvragen (eerste inschrijvingen) of Alternatieve inschrijving (tweede inschrijvingen) toe aan je overzicht. Lees meer over hoe je een aanzicht toevoegt in het {% link_new Dienstrooster-Center | features/scheduling/shiftcenter/shift-center-overview.md | #choose-the-time-range-and-levels %} en in {% link_new Schedules | features/scheduling/schedules/schedules-overview.md | #by-level %}.

## Diensten verloten starten

Als de inschrijvingsperiode is verstreken, plan je de inschrijvingen van je medewerkers in door middel van een verloting. Hierbij worden de gewenste diensten van de niveaus Aanvraag en Alternatieve aanvraag naar het niveau Schedule gekopieerd.

> Voordat je de dienstengeneratie opnieuw uitvoert, {% link_new dien je op een ongebruikt niveau een back-up te maken van alle dienstaanvragen | features/scheduling/schedules/schedules-copy-level-content.md %}, bijvoorbeeld Versie 1.
>
> Bij een nieuwe dienstengeneratie worden alle ingediende aanvragen in het niveau Aanvraag en Alternatieve aanvraag verwijderd.

Tip: Als bepaalde medewerkeres een hogere kans moeten krijgen om de aangevraagde diensten te krijgen, voer de verloting dan uit op basis van groepen. Roteer de volgorde van groepen in elke roosterperiode om een eerlijke verdeling op de lange termijn te garanderen.

Volg de onderstaande stappen om een verloting uit te voeren:

1. Ga naar _Plan > Schedules_{:.breadcrumbs}.
2. Klik op _Roosterperiodes_{:.doc-button}.
3. Beweeg de cursor over de **Roosterperiode** waarvoor je diensten wilt verloten en klik op het {% icon ellipsis_v %} aan de rechterkant.
4. Selecteer in het overstroommenu _Start diensten verloten_{:.doc-button}.
5. (Optioneel) Activeer de optie **Houd rekening met de gemiddelde begintijd van andere diensten** en voer een waarde voor de **bandbreedte** (hh:mm-formaat) in.
   - Indien geactiveerd, houdt injixo rekening met de (gemiddelde) begintijd van diensten. Lees meer over [hoe de bandbreedte-instelling werkt](#de-juiste-bandbreedte-instelling-selecteren).
   - Indien niet geactiveerd, kunnen medewerkers diensten krijgen met willekeurige begintijden.
     {{ 4 | image: 'Parametervenster voor verloting', '45%' }}
6. Om alle medewerkers te selecteren, vink je het bovenste **selectievakje** aan. Je kunt de lijst filteren op basis van groepen of medewerkerfilters en individuele medewerkers selecteren.
7. Klik op _Diensten verloten starten_{:.doc-button}.
   Nadat de verloting is afgerond, vind je de verlotingslog in de JobProcessor. Het rapport bevat de redenen waarom een dienst waarop iemand zich heeft ingeschreven niet is ingepland, en dagelijkse en totale verlotingsquota in %.

## Resterende diensten toewijzen

Nadat bij de verloting diensten zijn ingepland, zijn er vaak diensten die niet zijn toegewezen omdat niemand zich hierop heeft ingeschreven. In deze stap worden diensten aan medewerkers toegewezen die geen of onvoldoende diensten hebben gekregen.

1. Ga naar _Plan > Schedules_{:.breadcrumbs}.
2. Klik op _Roosterperiodes_{:.doc-button}.
3. Beweeg de cursor over de **Roosterperiode** waarvoor je diensten wilt toewijzen en klik op het {% icon ellipsis_v %} aan de rechterkant.
4. Selecteer in het overloopmenu _Diensten toewijzen_{:.doc-button}.
5. (Optioneel) Activeer de optie **Houd rekening met de gemiddelde begintijd van andere diensten** en voer waarde in bij **Bandbreedte** (hh:mm-formaat).
   - Indien geactiveerd, houdt injixo rekening met de (gemiddelde) begintijd van diensten. Lees meer over [hoe de bandbreedte-instelling werkt](#de-juiste-bandbreedte-instelling-selecteren).
   - Indien niet geactiveerd, kunnen medewerkers diensten krijgen met willekeurige begintijden.
     {{ 5 | image: 'Parameter diensten toewijzen', '45%' }}
6. Om alle medewerkers te selecteren, vink je het bovenste **selectievakje** aan. Indien gewenst, kun je de lijst filteren op basis van groepen of medewerkerfilters en individuele medewerkers selecteren.
7. Klik op _Diensten toewijzen_{:.doc-button}.
   Nadat de dienst is toegewezen, vind je een rapport onder _WFM > Administratie > Systeem > JobProcessor_{:.breadcrumbs} waarin alle toegewezen en niet-toegewezen diensten worden opgesomd.

Houd er rekening mee dat de planning mogelijk nog niet compleet is nadat de procedure is afgerond, bijvoorbeeld als er niet genoeg medewerkers zijn, medewerkers niet de juiste kwalificaties hebben voor diensten, of wanneer bij de toewijzing van een dienst een planningsregel wordt overtreden. Je kunt je configuratie wijzigen en het proces nogmaals uitvoeren of je planning handmatig aanpassen.

Tip: In plaats van het toewijzen van diensten kun je ook {% link_new Geoptimaliseerde planning maken | features/scheduling/schedules/schedules-optimized-schedules.md %} gebruiken om meerdere diensten toe te wijzen om de planning compleet te maken.

### De juiste bandbreedte-instelling selecteren

De berekening van de begintijd van de dienst op basis van de waarde voor de bandbreedte werkt anders met of zonder ingeplande diensten (bijvoorbeeld van dienstenreeksen).

- Met diensten: injixo berekent een gemiddelde begintijd voor de diensten en wijst deze vervolgens toe binnen de bandbreedte. Als bestaande diensten bijvoorbeeld om 8:00 uur en 12:00 uur beginnen, dan is het gemiddelde 10:00 uur. Als je een bandbreedte van 1 uur instelt, dan kunnen de overige diensten tussen 9:00 uur en 11:00 uur beginnen.
- Zonder diensten: De eerste toegewezen dienst bepaalt de begintijd van de dienst. Als de eerste dienst bijvoorbeeld om 9:00 uur begint, en je de bandbreedte instelt op 1 uur, dan beginnen de overige diensten tussen 8:00 uur en 10:00 uur.

## De planning optimaliseren en publiceren

Voer de {% link_new job-optimalisatie | features/scheduling/schedules/schedules-job-optimization.md %} uit om ingeplande activiteiten en pauzes in de roosterperiode te optimaliseren.

Om het {% link_new rooster te publiceren | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %} en agenten de mogelijkheid te geven om diensten te ruilen, dien je de {% link_new roosterperiode | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md | #status %} de **status** Gepubliceerd te geven. Als je {% link_new Diensten ruilen | features/scheduling/view-approve-shift-swap-requests.md %} hebt geconfigureerd, dan kunnen medewerkers hun eigen diensten bekijken en {% link_new met andere medewerkers ruilen | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}.

## E-mail- en browser-pushmeldingen

Als je de status van een roosterperiode wijzigt, dan stuurt injixo e-mail- en browser-pushmeldingen om de medewerkers in de betreffende roostereenheid over de wijzigingen te informeren en hen eraan te herinneren zich op diensten in te schrijven.

Gebruikers moeten de {% link_new browser-pushmeldingen | getting-started/notifications.md %} in hun browsers activeren. In de standaardinstelling stuurt je tenant zowel e-mails als browser-pushmeldingen.
