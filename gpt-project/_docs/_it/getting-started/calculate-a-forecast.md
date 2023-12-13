---
title: Calcolare una previsione
description: Segui i passaggi necessari per generare una previsione
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
redirect_from:
  - /it/quickstart-forecasting/
redirect_reason: Updated filename on 29 November 2023
---

Questo articolo elenca i passaggi necessari per creare la prima {% link_new previsione | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}. Sulla base dei dati storici, la previsione calcolerà il numero di dipendenti necessari per gestire i volumi in entrata per una specifica attività in un’unità di pianificazione.
Questo articolo fornisce una panoramica della procedura di creazione di una previsione. Per avere più informazioni, segui i link inclusi nell’articolo.

Utilizza questo articolo come elenco dei passaggi necessari per aiutarti durante l’onboarding. In caso di dubbi, contatta il tuo consulente.

## Prerequisito

Prima di creare una pianificazione, assicurati di avere {% link_new impostato correttamente la configurazione di base | getting-started/set-up-base-configuration.md %}.
## 1\. Impostare un’integrazione

In _Account > Integrazioni_{:.breadcrumbs}, imposta un’{% link_new integrazione | features/acd-integration/cloud/how-integrations-work.md %} con il tuo sistema esterno per importare i dati storici. L’integrazione importerà i dati in injixo e creerà delle code.

## 2\. Impostare un workload

In _Forecast_{:.breadcrumbs}, crea un {% link_new workload dalle code create dall’integrazione | features/forecast/injixo-forecast/manage-workloads.md %}. Nel giro di pochi minuti verrà generata una previsione.

Nota: per {% link_new importare previsioni esterne | features/forecast/injixo-forecast/import-forecast.md %} è necessario selezionare almeno una coda. Se non ci sono code, è necessario caricare almeno un punto dati utilizzando un’{% link_new integrazione CSV | features/acd-integration/cloud/add-csv-integration.md %}.

## 3\. Creare e aggiungere eventi

Crea tutti gli {% link_new eventi | features/forecast/injixo-forecast/events-and-holidays.md %} che possono influire sul calcolo della previsione. Aggiungi gli eventi creati allo storico dati e alla previsione all’interno dei workload per rendere il calcolo più accurato.

## 4\. Salvare una versione della previsione

Una {% link_new versione della previsione | features/forecast/injixo-forecast/store-forecast-versions.md %} è un’istantanea del calcolo attuale. Salva la versione della previsione per rivederla in seguito, oppure per confrontare la previsione con il volume effettivo del giorno in questione, per esempio, in {% link_new Dashboards | features/forecast/injixo-forecast/store-forecast-versions.md %}.

## 5\. Calcolare il fabbisogno di personale

Per creare pianificazioni ottimizzate o per lanciare l’ottimizzazione delle mansioni, è necessario prima {% link_new calcolare il fabbisogno di personale | features/forecast/injixo-forecast/staff-requirement.md %} per le attività corrispondenti all’interno dei workload.


## E adesso?

Ce l’hai fatta! Adesso è tutto pronto per {% link_new creare la prima pianificazione | getting-started/create-a-schedule.md %} basata sulla previsione e sul fabbisogno di personale.
