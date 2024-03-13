---
title: Een forecast berekenen
description: Volg de basisstappen die nodig zijn om een forecast te maken.
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
redirect_from:
  - /nl/quickstart-forecasting/
redirect_reason: Updated filename on 29 November 2023
---

In dit artikel vind je de stappen die nodig zijn om je eerste {% link_new forecast | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} te maken. Op basis van historische gegevens berekent de forecast het aantal medewerkers dat nodig is om de binnenkomende volumes voor een activiteit in een eenheid te verwerken.
Dit artikel geeft een overzicht van de procedure voor het maken van een forecast. Volg de links in dit artikel voor meer informatie over elke stap.

Gebruik dit artikel als checklist als aanvulling op je onboarding. Als je vragen hebt, neem dan contact op met je consultant.

## Vereiste

Zorg ervoor dat je eerst {% link_new je basisconfiguratie juist hebt ingesteld | getting-started/set-up-base-configuration.md %} voordat je een planning aanmaakt.

## 1\. Een integratie configureren

Ga naar _Account > Integraties_{:.breadcrumbs} om een {% link_new integratie | features/acd-integration/cloud/how-integrations-work.md %} met je externe systeem te configureren, zodat er historische gegevens kunnen worden geüpload. De integratie uploadt gegevens naar injixo en maakt queues aan.

## 2\. Een workload configureren

Maak onder _Forecast_{:.breadcrumbs} een {% link_new workload aan van de queues die door je integratie zijn aangemaakt | features/forecast/injixo-forecast/manage-workloads.md %}. De forecast wordt binnen enkele minuten gegenereerd.

Opmerking: Om {% link_new externe forecasts te importeren | features/forecast/injixo-forecast/import-forecast.md %} moet je minimaal een queue selecteren. Als er geen queue beschikbaar is, upload dan minimaal een datapunt met behulp van een {% link_new CSV-integratie | features/acd-integration/cloud/add-csv-integration.md %}.

## 3\. Gebeurtenissen aanmaken en toevoegen

Maak al je {% link_new gebeurtenissen | features/forecast/injixo-forecast/events-and-holidays.md %} aan die invloed kunnen hebben op je forecastberekening. Voeg de aangemaakte gebeurtenissen toe aan de historie en forecast in je workload(s) voor een beter berekeningsresultaat.

## 4\. Een forecastversie opslaan

Een {% link_new forecastversie | features/forecast/injixo-forecast/store-forecast-versions.md %} is een snapshot van het huidige berekeningsresultaat. Sla de forecastversie op om deze op een later moment te beoordelen of om je forecast met het volume op de betreffende dag te vergelijken, bijvoorbeeld in {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %}.

## 5\. De personeelsbehoefte berekenen

Om geoptimaliseerde planningen te maken of de joboptimalisatie uit te voeren, moet je eerst {% link_new de personeelsbehoefte berekenen | features/forecast/injixo-forecast/staff-requirement.md %} voor de betreffende activiteiten in je workloads.


## En nu?

Dat was alles! Je bent nu klaar om {% link_new je eerste planning te maken | getting-started/create-a-schedule.md %} op basis van je forecast en personeelsbehoefte.
