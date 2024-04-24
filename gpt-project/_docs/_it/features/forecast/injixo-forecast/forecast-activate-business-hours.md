---
title: Attivare gli orari di apertura
product_label:
  - advanced
  - enterprise
  - classic
toc: true
description: Scopri come attivare gli orari di apertura e come questi influiscono sulla previsione.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
---

È la prima volta che utilizzi injixo Forecast? Meglio cominciare dalle {% link_new basi | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

Per impostazione predefinita, i workload non tengono conto degli orari di apertura, e le previsioni sono basate sul volume giornaliero totale. Nella configurazione dei workload, puoi configurare injixo in modo che tenga conto degli orari di apertura e che li mostri nella previsione. Per impostazione predefinita, il fabbisogno di personale tiene sempre conto degli orari di apertura.

Se non configuri gli orari di apertura per l'unità di pianificazione, la pagina della previsione non mostrerà nessun fabbisogno di personale.

injixo Classic supporta gli orari di apertura soltanto nei workload di tipo Smart.

## Prerequisiti

Assicurati che si verifichino le seguenti condizioni:

- Hai configurato degli {% link_new orari di apertura | features/administration/create-and-manage-planning-units.md | #aggiungere-gli-orari-di-apertura %} validi e delle {% link_new attività | features/administration/activities.md %} per l'unità di pianificazione per la quale desideri attivare gli orari di apertura.
- Hai controllato le voci {% link_new **Validità dal**/**fino al** | features/administration/set-a-validity-period.md %} per l'unità di pianificazione e l'attività assegnata al workload, e le hai rimosse o modificate, se necessario.
- Hai le autorizzazioni necessarie per visualizzare e modificare le unità di pianificazione in questione.
- Se all'unità di pianificazione è stato assegnato un calendario pianificativo, hai anche le {% link_new autorizzazioni | getting-started/configure-user-roles.md | #impostare-le-autorizzazioni-per-wfm %} necessarie per far sì che il calendario pianificativo mostri gli orari di apertura.

## Attivare gli orari di apertura

Per includere nel calcolo della previsione i volumi al di fuori dagli orari di apertura, attiva gli orari di apertura separatamente per ogni workload.

1. In _Forecast > Workload_{:.breadcrumbs}, scegli un workload.
2. Clicca su _Modifica workload_{:.doc-button}.
3. Nella sezione **Configurazione di base**, seleziona un’unità di pianificazione e un’attività.
4. Spunta la casella **Previsione solo entro l'orario di apertura**.
5. Clicca su _Salva workload_{:.doc-button}.
   injixo calcola una nuova previsione. Il calcolo potrebbe richiedere del tempo.

Dopo che gli orari di apertura sono stati attivati, le fasce orarie al di fuori degli orari di apertura appaiono come aree grigie nel grafico della pagina **Forecast**.

## Gli effetti sulla previsione

Attivare gli orari di apertura in un workload comporta i seguenti effetti:

- injixo legge gli orari di apertura dell’unità di pianificazione e dell’attività assegnati al workload, e mostra come orari di apertura solo le fasce orarie in cui entrambi sono aperti. Tutti gli intervalli all’interno di questo periodo sono tenuti in considerazione e mostrati come aperti nel grafico della previsione.
- injixo ridistribuisce all’interno degli orari di apertura i volumi che si trovano al di fuori degli orari di apertura. Il volume giornaliero totale non cambia. La distribuzione è relativa ai valori esistenti degli intervalli, e quindi segue lo schema infragiornaliero previsto. I volumi al di fuori degli orari di apertura diventano 0.
- injixo imposta a 0 tutti i valori del tempo medio di gestione previsti per orari al di fuori degli orari di apertura.
