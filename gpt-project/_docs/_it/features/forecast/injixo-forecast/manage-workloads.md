---
title: Creare i workload
redirect_from:
  - /it/workloads/
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Crea i workload per rappresentare il volume di contatto storico e previsto e l’AHT. Scopri i diversi tipi di workload.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Attivare gli orari di apertura
    filepath: features/forecast/injixo-forecast/forecast-activate-business-hours.md
---

Per creare, modificare o eliminare i workload, vai su _Forecast_{:.breadcrumbs}.

I workload mappano i canali di ingresso del tuo sistema esterno, che registra i dettagli delle tue interazioni con i clienti. Sulla base dei dati sui contatti, importati nelle code, injixo Forecast calcolerà una previsione per il workload. Gli eventi configurabili, le festività e gli orari di apertura influiscono sulla previsione. Puoi anche {% link_new importare la tua previsione | features/forecast/injixo-forecast/import-forecast.md %} nei workload.

I workload ti permettono di configurare il calcolo fabbisogno di personale. Il fabbisogno di personale è necessario per la pianificazione.

È la prima volta che utilizzi injixo Forecast? Meglio cominciare dalle {% link_new basi | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Prerequisiti

- Aggiungi un’{% link_new integrazione nativa o CSV | features/acd-integration/cloud/how-integrations-work.md %} e importa i dati storici per almeno una coda.
- Importa i contatti in arrivo, il tempo medio di gestione (AHT), e i contatti gestiti. I workload con più di una coda richiedono i dati sui contatti gestiti per poter mostrare il tempo medio di gestione e calcolare le medie ponderate.

injixo crea code utilizzando i dati importati da un'integrazione. L'intervallo di importazione dei dati determina l'intervallo delle code create a partire da quei dati. È possibile aggiungere a un workload solo code con lo stesso intervallo.

## Code e canali

I dati di contatto importati da un'integrazione vengono salvati all’interno di code. Queste code sono sempre associate a un canale. Quando [crei un workload](#creare-un-workload), puoi filtrare le code in base al canale per assegnarle al workload. Le integrazioni native impostano automaticamente il canale per le code. Non tutte le integrazioni supportano tutti i canali.
Per le integrazioni CSV, è necessario impostare manualmente il canale. È possibile aggiungere un canale per colonna, o selezionare un canale per il file durante la {% link_new mappatura delle colonne | features/acd-integration/cloud/add-csv-integration.md | #mappare-le-colonne %}  

Le integrazioni supportano i seguenti canali:

- Chiamate
- Chat
- Email
- Casi
- Documenti
- Social media

injixo Forecast raggruppa le code in base al canale. È possibile aggiungere a un workload solo code con lo stesso canale.

<!-- anchor for intercom forecast tour -->

## Creare un workload 

Ti consigliamo di creare un workload per ogni attività che vuoi pianificare utilizzando il fabbisogno di personale. Le multiattività richiedono un workload per la multiattività e un workload per ogni subattività.

1. Clicca su _Nuovo workload_{:.doc-button} sopra l’elenco.
2. Inserisci alcune informazioni generali sul workload:
   - **Nome**: nome unico che identifichi il tuo workload.
   - **Fuso orario**: il {% link_new fuso orario | best-practices/working-with-timezones.md %} per il workload non può essere modificato in seguito.

     > Nota
     >
     > - Per salvare il fabbisogno di personale di un’unità di pianificazione, il fuso orario del workload deve corrispondere al fuso orario dell’unità di pianificazione.
     > - Se imposti per il workload un fuso orario diverso rispetto a quello dell’integrazione che usi per importare i dati, i dati importati presenteranno uno sfasamento nel workload. Per esempio, se l’integrazione CSV è impostata sul fuso orario UTC, e il tuo workload è impostato sul fuso orario CEST (UTC+2), i dati importati contrassegnati alle 08:00 saranno visualizzati nel workload alle 10:00.

   - (Facoltativo) **Festivo regionale**: include le festività nazionali che potrebbero influire sulla previsione.
   - (Facoltativo) **Unità di pianificazione** e **Attività**: necessarie per {% link_new attivare gli orari di apertura | features/forecast/injixo-forecast/forecast-activate-business-hours.md %} nella sezione **Orario di apertura**.

3. (Solo per injixo Classic) Seleziona una delle opzioni della sezione **Modelli di prezzo**:

   - **Modalità Live** (a pagamento): fatturata mensilmente. Non può essere riportata alla modalità Test.
   - **Modalità Test** (gratis): puoi solo visualizzare le previsioni, e non puoi trasferire i fabbisogni di personale per la pianificazione.

4. Nella sezione **Assegna code al workload**, seleziona le code per il tuo workload.

   Per scegliere quali code vengono visualizzate:

   - Filtra le code in base al canale (Chiamate, Chat, etc...).
   - Usa le caselle per mostrare le code selezionate, non selezionate, o inattive. Le code inattive sono quelle importate da integrazioni che sono state eliminate.
   - Usa il campo di ricerca sopra la tabella. Puoi cercare per coda, integrazione o nome del workload.

   Nota: se l’intervallo o il canale di una coda non corrispondono a quelli delle code selezionate, tutte le code che non corrispondono verranno mostrate oscurate.

5. Clicca su _Crea workload_{:.doc-button}.

   La pagina mostra i dati storici e una prima versione della previsione.  
   Al termine del calcolo, aggiorna la pagina per vedere la versione finale della previsione.  
   Il nuovo workload viene visualizzato nell'elenco dei workload.

Se utilizzi injixo Essential, puoi creare workload di tipo Basic. I workload Basic richiedono almeno due settimane di dati storici. I workload Basic non supportano gli orari di apertura.

Se utilizzi injixo Advanced o Enterprise WFM, puoi creare workload di tipo Smart. I workload Smart possono generare una previsione sulla base di un solo giorno di dati storici. I workload Smart supportano gli orari di apertura.

Se utilizzi injixo Classic, devi inoltre selezionare il modello di previsione (Smart o Basic) per ogni workload. Per i workload Smart, devi scegliere tra la modalità Live e la modalità Test. La modalità Test è gratuita ma ti permette solo di visualizzare le previsioni, e non puoi trasferire il fabbisogno di personale per la pianificazione. La modalità Live offre la funzionalità al completo e viene fatturata mensilmente. I workload Smart in modalità Live non possono essere riportati alla modalità Test.

<!-- hidden: feature not live yet -->
<!-- ## Create workloads without historical data

You only need an integration and historical data import if you want injixo to create forecasts. To add forecast data by {% link_new importing a forecast | features/forecast/injixo-forecast/import-forecast.md %} that has been generated externally or to {% link_new create constant staff requirements | features/forecast/requirement-scripts/requirement-constant.md %}, you can create a workload using the tab *Forecast Import*:

1. Go to **Forecast**{:.breadcrumbs}.
2. Click _Create Workload_{:.doc-button} in the upper right corner of the forecast page.
3. In the *Basic configuration* section, enter a **Name** for your new workload.
4. Select the **Time zone** to display data. Note: The set time zone must match the planning unit to save staff requirements.
5. (Optional) Select the **Holiday region** to acknowledge all public holidays that affect your forecast for the year.
6. Select the **Planning unit** and the **Activity**. Note: You must select an option to calculate staff requirements.
    {{ 4 | image: 'Import Workload basic configuration section' }}
7. Click the tab **Forecast import**.
8. Select your **Interval length** and the **Channel** for the data import. Both must correspond with your import file.
    {{ 5 | image: 'Import Workload parameters' }}
9. Click *Create workload*{:.doc-button}. -->

## Modificare un workload

1. Seleziona un workload dall'elenco dei workload, o digita il nome del workload nel campo di ricerca.
2. Per modificare i dettagli del workload, clicca sull’{% icon pencil %}.  
   È possibile aggiungere o rimuovere code senza dover reimportare i dati. Le code nell’elenco vengono oscurate se il loro intervallo o il loro canale non corrispondono a quelli delle code già assegnate.
3. Clicca su _Salva workload_{:.doc-button}.  
   La nuova configurazione potrebbe aggiornare la previsione.

## Eliminare un workload

1. Clicca sull’{% icon trash %} accanto a un workload nell’elenco.
2. Nella finestra di conferma, clicca su _Elimina workload_{:.doc-button}.  
    injixo salva i dati storici associati. Per riutilizzare i dati, aggiungi la coda o le code a un altro workload.
