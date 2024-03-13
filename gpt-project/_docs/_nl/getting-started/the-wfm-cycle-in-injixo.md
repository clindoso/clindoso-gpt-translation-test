---
title: De WFM-cyclus in injixo
description: Lees hoe injixo je door de WFM-cyclus helpt
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

Het doel van workforce management (WFM) is het optimaliseren van de inzet van je medewerkers om bedrijfsdoelen en beoogde service levels te behalen. injixo helpt je om tijdens de verschillende fasen van de WFM-cyclus efficiënter te werken:

  {{ 1 | image: "WFM-cyclus: Forecasts maken, Plannen, Planningen maken, Intraday management, Analyse", '60%' }}

- Forecasts maken: Voorspel je workload op de korte, middellange en lange termijn.
- Plannen: Neem beslissingen op het gebied van werving, budget en trainingsstrategieën voor de toekomst.
- Planningen maken: Maak de best mogelijke planningen voor je medewerkers en je bedrijfsbehoeften.
- Intraday Management: Pas je planningen in realtime aan onvoorziene omstandigheden aan. 
- Analyse: Begrijp, voorspel en verbeter de prestaties van je bedrijf.

In dit artikel vind je een overzicht van hoe injixo je tijdens alle fasen van de WFM-cyclus ondersteunt.
Om te beginnen moeten we injixo alle informatie aanleveren die nodig is om een betrouwbare forecast te genereren. Hiervoor zet je een integratie op met je Automatic Call Distribution-systeem (ACD) of je Customer Relationship Management-systeem (CRM).

Ben je nog niet zo vertrouwd met workforce management? Lees dan meer over de belangrijkste concepten en definities in onze [woordenlijst](https://help.injixo.com/glossary/overview). 

## 1\. Forecasts maken

### Een integratie configureren

Om de workload van je organisatie op een specifiek moment in de toekomst te kunnen voorspellen, heeft injixo toegang nodig tot je contactgegevens en/of agentstatusgegevens in externe systemen, zoals een ACD- of CRM-systeem). Om injixo gegevens te laten importeren en verwerken, is het van belang dat je {% link_new je externe systemen in injixo integreert | features/acd-integration/cloud/how-integrations-work.md %}. injixo biedt native, vendor-specifieke integraties en universele integraties. Afhankelijk van de integratie ontvangt injixo informatie in intervallen van 15, 30 of 60 minuten (import van historische gegevens) of zelfs binnen seconden (real-time gegevensimport). 

Zodra je een integratie hebt toegevoegd, stuurt deze automatisch, continu gegevens naar injixo.
Geïmporteerde contactgegevens worden opgeslagen in queues, die altijd gekoppeld zijn aan een kanaal. Je hebt deze queues nodig om workloads aan te maken, want hierop wordt je forecast gebaseerd.

Je kunt je integraties configureren onder _Account > Integraties_{:.breadcrumbs}.

### Een workload maken


Om injixo Forecast te kunnen gebruiken, moet je eerst {% link_new een workload aanmaken | features/forecast/injixo-forecast/manage-workloads.md | #workloads-aanmaken %} op basis van de queues die door je integratie zijn geïmporteerd. Workloads bevatten al je historische gegevens en gerelateerde forecasts. Om een forecast te maken, moet je ACD op de juiste manier zijn verbonden. Ook moeten de geïmporteerde queues beschikbaar zijn.

Ga naar _Forecast > Workloads_{:.breadcrumbs} om workloads aan te maken. 

### Een forecast berekenen

{% link_new injixo Forecast | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} combineert je historische gegevens met het meest geschikte algoritme om hoogwaardige forecasts te genereren voor tot wel 365 dagen.

De gegenereerde forecast wordt na elke nieuwe gegevensimport bijgewerkt. Je kunt ook {% link_new gebeurtenissen toevoegen | features/forecast/injixo-forecast/events-and-holidays.md %} die invloed hebbeno p je forecast.

### De personeelsbehoefte berekenen

Zodra je een forecast hebt gegenereerd, kun je {% link_new de personeelsbehoefte berekenen | features/forecast/injixo-forecast/staff-requirement.md %}, oftewel het aantal medewerkers dat moet worden ingepland om de verwachte workload te dekken. Voor eht berekenen van je personeelsbehoefte kun je verschillende {% link_new berekeningsmethoden | best-practices/requirement-scripts.md %} gebruiken. Hierbij wordt rekening gehouden met factoren als je beoogde service level, beoogde antwoordtijd, shrinkage, enz. Indien nodig kun je ook zonder forecast een contante personeelsbehoefte instellen.

Tijdens het planningsproces kun je je personeelsbehoefte gebruiken om geoptimaliseerde planningen aan te maken voor specifieke perioden, eenheden en activiteiten.

## 2\. Plannen

Gebruik de gegevens die door injixo Forecast zijn gegenereerd om je personeelsbehoefte te vergelijken met het aantal medewerkers dat daadwerkelijk beschikbaar is. Op basis van een langetermijnforecast kun je beter en tijdig beslissingen nemen over verlofaanvragen, het juiste moment om vacatures uit te schrijven of welke trainingsprogramma's je medewerkers moeten volgen om zich voor te bereiden op aanstaande projecten.

## 3\. Planningen maken

### Een planning maken

Zodra je je personeelsbehoefte hebt berekend, biedt injixo verschillende {% link_new planningsmethoden | features/scheduling/scheduling-methods.md %} die je kunt kiezen en combineren om je medewerkers zo in te plannen dat aan de behoeften van je bedrijf wordt voldaan.

Onder _Plan > Schedules_{:.breadcrumbs} kun je planningsregels en beperkingen instellen om aan arbeidswetgeving, bepalingen in de contracten van je medewerkers en voorkeuren van medewerkers te voldoen.

injixo biedt meerdere planningsfunctionaliteiten zoals {% link_new geoptimaliseerde planning | features/scheduling/schedules/schedules-optimized-schedules.md %}, {% link_new medewerkers op de hoogte brengen van planningswijzigingen | features/scheduling/schedules/schedules-notify-scheduling-changes.md %} of {% link_new medewerkers de mogelijkheid bieden om diensten te ruilen | features/scheduling/planning-periods/enable-employees-to-swap-shifts.md %} met hun collega's.

### Verlof plannen

Onder {% link_new Vakantie/Afwezigheid | features/scheduling/time-off/vacation-absences-management.md %} kun je verlofsaldi en verlofaanvragen, ziekteverlof, persoonlijke vrije dagen en andere soorten afwezigheid beheren. Medewerkers kunnen hun verlofaanvragen indienen via {% link_new injixo Me | features/injixo-me/use-injixo-me/explore-injixo-me.md %}. Vervolgens kun je deze aanvragen goedkeuren of afwijzen op basis van de personeelsbehoefte, de beschikbaarheid van medewerkers en overige vooraf vastgelegde regels of beperkingen.

Ga naar _Plan > Vakantie/Afwezigheid_{:.breadcrumbs} om vakanties en afwezigheid te beheren.

## 4\. Intraday Management

Met {% link_new Intraday Adherence | features/intraday/adherence-intraday.md %} kun je ingeplande activiteiten met de uitgevoerde activiteiten vergelijken om eventuele afwijkingen vaststellen. Vervolgens worden gedetailleerde statistieken en een adherence-score weergegeven.

Dit is ook in realtime mogelijk met {% link_new Real-Time Adherence | features/intraday/real-time-adherence.md %}. Hier vind je een uitgebreid overzicht, filteropties en een aanpasbare beoogde adherence-score.

Met die informatie kun je de planning op heel korte termijn aanpassen om in te spelen op onvoorziene gebeurtenissen, om te voorkomen dat je te veel of te weinig personeel inzet.

## 5\. Analyse
 
Met injixo kun je {% link_new dashboards aanmaken | features/monitoring/dashboards/dashboards-overview.md %} met grafische elementen om verschillende metrics beter zichtbaar te maken, bijvoorbeeld een vergelijking van personeelsbehoefte en de werkelijke dekking, of het voorspelde tegenover het werkelijke aantal binnenkomende gesprekken voor verschillende tijdreeksen.

injixo kan ook {% link_new meerdere soorten rapporten genereren | features/reporting/standard-reports/creating-reports.md %} waarmee je relevante metrics in de gaten kunt houden, waaronder capaciteit volgens contracttype, gewerkte tijd per eenheid of vakantieoverzicht.
