---
title: Automate recurring jobs with JobManager <!-- GPT translation -->
product_label:
  - enterprise
description: Automatizza la generazione di report con il JobManager. <!-- GPT translation -->
promote-service: enhanced-reporting
gpt_translation: true
---

In _WFM > Administration > System > JobManager_{:.breadcrumbs}, gli utenti con accesso amministratore possono definire dei modelli di lavoro per lavori ricorrenti, come l’inserimento di rotazioni, la creazione di report, l’estrazione delle assegnazioni dei turni tramite sorteggio o calcolo degli orari di lavoro target. <!-- GPT translation -->

 <!-- that can run with the privileges of other users. -->

<!-- The JobProcessor runs activated templates at the specified time. -->

## Creare un modello settimanale <!-- TM 61 -->

1. Clicca sull’icona Nuovo {% icon item-add | icon-only %}. <!-- GPT translation -->
2. Inserisci un **Nome** (massimo 50 caratteri). <!-- TM 71 -->
3. Spunta la casella **Attivo** per attivare l’esecuzione pianificata. <!-- GPT translation -->
4. Seleziona un Tipo di attività. Questa categoria non ha impatto sul procedimento, ma ti permette di filtrare per tipo di attività in un secondo momento. <!-- GPT translation -->
5. Imposta una **Priorità**. Intervallo di valori: da 1 a 10 (il valore più basso è 10). <!-- GPT translation -->
6. (Facoltativo) Seleziona un altro **Utente**. Per impostazione predefinita viene selezionato l’utente che ha fatto il login. È possibile utilizzare un diverso utente per eseguire i tipi di lavoro con autorizzazioni diverse. <!-- GPT translation -->
6. Clicca su _Chiudi_{:.doc-button}. <!-- TM 69 -->
   Configura le informazioni aggiuntive necessarie per eseguire i processi nelle sezioni Periodo di elaborazione, Parametri di processo e Date di processo. <!-- GPT translation -->

<!-- To edit existing templates, click an item in the list. -->
<!-- Existing templates with the configured parameters can be edited via _JobManager_{:.menu-item} at any time. -->

<!-- outdated for cloud -->
<!-- {{ 1 | image: "Job Configuration", '50%' }} -->

### Impostare il margine temporale per l’elaborazione dei processi <!-- GPT translation -->

Definisci in quali giorni un modello di processi attivo deve essere eseguito. I periodi possono essere assoluti, in base a un intervallo di date fisso, o relativi, per le settimane o i mesi attuali o precedenti. I periodi relativi alla data attuale sono utili per i lavori che si ripetono con regolarità. <!-- GPT translation -->

Per esempio, per generare un report che copre ogni periodo di 24 ore, è meglio scegliere il periodo relativo.  <!-- GPT translation -->

- Unità di tempo: Relativa <!-- GPT translation -->
- Valore di riferimento fino a: -1 (Seleziona **giorno** dal menu a tendina) <!-- GPT translation -->
- Valore di riferimento fino a: -1 (disponibile dopo aver cliccato su **OK** per salvare le altre proprietà del modello generale). <!-- GPT translation -->

### Impostare i parametri di processamento <!-- GPT translation -->

Quando salvi un processo, viene impostato soltanto il periodo di tempo durante il quale il processo è in corso. Aggiungi gli altri parametri generali e specifici per ogni processo seguendo questi passaggi: <!-- GPT translation -->

4. Clicca sull’icona Aggiungi {% icon item-add | icon-only %}. <!-- TM 86 -->
   Si aprirà una finestra. <!-- TM 100 -->
2. Inserisci un **Nome** (massimo 50 caratteri). <!-- TM 66 -->
3. Inserisci un **Valore** per il parametro che hai inserito nel passaggio precedente. <!-- GPT translation -->

Per avere più informazioni sui parametri e sui valori disponibili, leggi l’articolo {% link_new Esempi di JobManager | features/reporting/jobmanager/jobmanager-examples.md %}. <!-- GPT translation -->

### Impostare le date di processamento <!-- GPT translation -->

Definisci i giorni e le ore in cui il JobProcessor esegue i modelli attivi. Puoi impostare una o più date di processamento per un’elaborazione. <!-- GPT translation -->

Scegli dalle seguenti opzioni: <!-- GPT translation -->

- Feriali (lunedì-venerdì) <!-- GPT translation -->
- Giorno del mese (1-31): seleziona una data che ricorre in ogni mese del periodo di processamento del job. Per esempio, il 30 di febbraio non viene preso in considerazione. <!-- GPT translation -->
- Ultimo giorno del mese <!-- GPT translation -->

Ogni opzione richiede di impostare l'ora nel formato HH:MM. <!-- GPT translation -->

### Impostare le opzioni di processamento dei task <!-- GPT translation -->

Puoi spuntare la casella per eliminare il job dopo che il suo risultato è stato restituito, una funzionalità utile in caso di pianificazione di esecuzioni di job che devono essere processati solo una volta. <!-- more functionality in on-premise --> <!-- GPT translation -->