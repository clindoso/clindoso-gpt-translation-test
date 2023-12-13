---
title: Een planning aanmaken
description: Volg de basisstappen die nodig zijn om een planning te maken.
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
related_articles:
  - overwrite_title: Planningsproblemen oplossen
    filepath: best-practices/resolve-optimization-issues.md
  - overwrite_title: Back-ups maken van planningen en planningen vergelijken
    filepath: best-practices/why-level-copy.md
  - overwrite_title: Wat is de feature Meetings?
    filepath: features/scheduling/meetings/meetings-overview.md
  - overwrite_title: Extra activiteiten inplannen
    filepath: features/scheduling/schedules/schedules-extra-activities.md
  - overwrite_title: Activiteit in batches vervangen
    filepath: features/scheduling/schedules/schedules-replace-activities.md
  - overwrite_title: Nationale feestdagen plannen
    filepath: best-practices/scheduling-public-holidays.md
redirect_from:
  - nl/quickstart-scheduling/
redirect_reason: Updated filename on 27 July 2023
---

Het aanmaken van planningen is een essentieel onderdeel van de {% link_new WFM-cyclus | getting-started/the-wfm-cycle-in-injixo.md %}. Planningen bevatten de diensten en activiteiten die voor je medewerkers zijn ingepland.  

Gebruik dit artikel als checklist als aanvulling op je onboarding.

Opmerking: In injixo Essential WFM kun je geen back-up maken van je verlofaanvragen of de uiteindelijke planning.

## Vereisten

Zorg dat je eerst je {% link_new basisconfiguratie juist hebt ingesteld | getting-started/set-up-base-configuration.md %} en {% link_new een forecast hebt gegenereerd | getting-started/calculate-a-forecast.md %} voordat je begint met het maken van een planning. 

## Configuratievolgorde

We raden je aan om de configuratie-items in de volgorde in te stellen zoals in dit artikel wordt weergegeven. Elke configuratie-instelling is anders, daarom kan de optimale volgorde voor jouw organisatie afwijken. Als je vragen hebt, neem dan contact op met je consultant.

## Verlof configureren

In injixo Me kunnen je medewerkers een verlofaanvraag indienen. Ga naar _Plan > Vakantie/Afwezigheid_{:.breadcrumbs} om verlof en afwezigheid te beheren.

1. Voer de {% link_new vakantierechten | features/scheduling/time-off/vacation-entitlement.md %} van je medewerkers voor het huidige jaar in.
2. Maak een {% link_new verlofperiode | features/scheduling/time-off/time-off-periods.md %} aan en publiceer deze. Een verlofperiode geeft het tijdframe aan waarin medewerkers verlof en andere afwezigheid kunnen aanvragen. Medewerkers ontvangen een melding in injixo Me en kunnen vanaf dat moment verlofaanvragen indienen voor die betreffende periode.

## Ziekte of afwezigheid invoeren

In {% link_new Schedules | features/scheduling/schedules/schedules-overview.md %} en het {% link_new Dienstrooster-Center | features/scheduling/shiftcenter/shift-center-overview.md %}, kun je de planning van je team beheren. Voer alle reeds bekende {% link_new activiteiten | features/administration/activity-types-and-properties.md | #activiteitentype %} van het type Afwezigheid of Ziek in de planning in.

## Verlofaanvragen beheren

In _Plan > Verlof/Afwezigheid_{:.breadcrumbs} kun je alle {% link_new ingediende aanvragen | features/scheduling/time-off/vacation-absences-management.md %} goedkeuren of afwijzen.

> Maak op een ander niveau een back-up van het huidige planning.
>
> Gebruik {% link_new Niveau-inhoud kopiëren | features/scheduling/schedules/schedules-copy-level-content.md %} om een kopie van je planning op te slaan. Zo weet je zeker dat er geen goedgekeurde verlofaanvragen en eerder ingevoerd ziekteverlof verloren gaan als je de planning verwijdert en opnieuw begint.

## De planning aanmaken

Controleer in {% link_new Schedules | features/scheduling/schedules/schedules-overview.md %}, {% link_new Dienstrooster-Center | features/scheduling/shiftcenter/shift-center-overview.md %} of {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %}, of de {% link_new personeelsbehoefte | features/forecast/injixo-forecast/staff-requirement.md | #berekende-personeelsbehoefte-bekijken %} goed is ingesteld voor je activiteiten.

1. Voer {% link_new dienstenseries | features/scheduling/capacity/capacity-insert-shift-sequences.md %} in voor je medewerkers.
2. Configureer en pas {% link_new planningsmethoden | features/scheduling/scheduling-methods.md %} toe om je planning af te ronden.
3. Voer de {% link_new joboptimalisatie | features/scheduling/schedules/schedules-job-optimization.md %} uit. Je kunt deze stap overslaan als je een {% link_new geoptimaliseerde planning maakt | features/scheduling/schedules/schedules-job-optimization.md %}.

Tip: Als je een planning maakt voor testdoeleinden, dan kun je {% link_new lege niveaus | features/scheduling/schedules/schedules-empty-levels.md %} gebruiken. Kopieer de opgeslagen verlofperiodes en verlofaanvragen voor elke testrun weer terug naar het niveau Planning.

## Een back-up maken van je uiteindelijke planning

Sla voordat je je oorspronkelijke planning {% link_new handmatig wijzigt | features/scheduling/shiftcenter/modify-items.md %} eerst een {% link_new back-up | features/scheduling/schedules/schedules-copy-level-content.md %} op in het niveau Huidige staat. Zo kun je de kwaliteit van je oorspronkelijke planning vergelijken met nieuwere versies.

## De planning publiceren en diensten ruilen toestaan

1. Maak een planningsperiode aan, zodat {% link_new medewerkers hun planning kunnen bekijken | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %} in injixo Me.
2. (Optioneel) {% link_new Geef medewerkers toestemming om diensten te ruilen | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}.  
    Je dient eerst {% link_new alle nog niet beoordeelde aanvragen om diensten te ruilen te bekijken en goed te keuren | features/scheduling/view-approve-shift-swap-requests.md %}, maar je kunt ook automatische dienstruilingen tussen medewerkers toestaan met de instelling _48152_{:.id-label} **Ruilautorisatie**.
3. Deel het artikel {% link_new injixo Me verkennen | features/injixo-me/use-injixo-me/explore-injixo-me.md %} met je medewerkers.
