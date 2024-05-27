---
title: Automate recurring jobs with JobManager <!-- GPT translation -->
product_label:
  - enterprise
description: Automatizza la generazione di report e tanto altro utilizzando il JobManager. <!-- GPT translation -->
promote-service: enhanced-reporting
gpt_translation: true
---

In _WFM > Administration > System > JobManager_{:.breadcrumbs} (in inglese), i dipendenti con accesso amministratore possono impostare i modelli di attività per i processi che si ripetono, come l’inserimento di rotazioni per dipendenti, la creazione di report, l’esecuzione della sorteggio dei turni o delle assegnazioni, e il calcolo dei conti delle ore target. <!-- GPT translation -->

 <!-- che possono essere eseguiti con i privilegi di altri utenti. --> <!-- GPT translation -->

<!-- The JobProcessor runs activated templates at the specified time. --> <!-- GPT translation -->

## Creare un modello settimanale <!-- TM 61 -->

1. Clicca sull’icona Nuovo {% icon item-add | icon-only %}. <!-- GPT translation -->
2. Inserisci un **Nome** (massimo 50 caratteri). <!-- TM 71 -->
3. Spunta la casella **Abilitato** per attivare l’esecuzione pianificata. <!-- GPT translation -->
4. Seleziona Aquesto come tipo di lavoro, questa scelta non influisce sul processo, ma in seguito potrai fare il filtro per questo tipo di lavoro. <!-- GPT translation -->
5. Imposta una **Priorità**. Intervallo consentito: 1–10 (la priorità più bassa) <!-- GPT translation -->
6. (Facoltativo) Seleziona un diverso **Utente**. Di default è selezionato l’utente attualmente in uso. Può essere utile per eseguire tipi di lavoro con autorizzazioni diverse. <!-- GPT translation -->
6. Clicca su _Chiudi_{:.doc-button}. <!-- TM 69 -->
   Configura le informazioni aggiuntive necessarie per eseguire i processi nelle sezioni Periodo di elaborazione dei processi, Parametri del processo, and Date del Processo. <!-- GPT translation -->

<!-- To edit existing templates, click an item in the list. --> <!-- GPT translation -->
<!-- I template esistenti con i parametri configurati possono essere modificati tramite _JobManager_{:.menu-item}&nbsp; in qualsiasi momento. --> <!-- GPT translation -->

<!-- outdated for cloud --> <!-- GPT translation -->
<!-- {{ 1 | image: "Configurazione attività", '50%' }} --> <!-- GPT translation -->

### Impostare il periodo per il processo dei task <!-- GPT translation -->

Stabilire i giorni in cui un modello di processi dovrebbe essere attivo. I periodi possono essere assoluti, utilizzano un intervallo di date fisso, o relativi, per settimane o mesi passate, correnti o future. I periodi relativi alla data attuale sono utili per le attività che si ripetono con frequenza. <!-- GPT translation -->

Per esempio, per creare un report ogni giorno, alle 6 del mattino, sul giorno precedente, seleziona le seguenti opzioni: <!-- GPT translation -->

- Unità di tempo: Relativo <!-- GPT translation -->
- Inizio del periodo precedente: -1 (seleziona **Giorno** nel menu a tendina) <!-- GPT translation -->
- Valore di confronto da: -1 (disponibile dopo aver cliccato su **OK** per salvare le altre proprietà del modello generale) <!-- GPT translation -->

### Impostare i parametri per il processamento dei report <!-- GPT translation -->

Quando salvi un processamento, imposti solo il periodo in cui il processamento avrà luogo. Aggiungi gli altri parametri generali e specifici del processamento, uno per volta, come descritto di seguito. <!-- GPT translation -->

4. Clicca sull’icona Aggiungi {% icon item-add | icon-only %}. <!-- TM 86 -->
   Si aprirà una finestra. <!-- TM 100 -->
2. Inserisci un **Nome** (massimo 50 caratteri). <!-- TM 66 -->
3. Inserisci un **valore** per il parametro che hai definito come “name”. <!-- GPT translation -->

Scopri i parametri e i valori disponibili nell’articolo {% link_new Esempi di JobManager | features/reporting/jobmanager/jobmanager-examples.md %}. <!-- GPT translation -->

### Impostare le date di processamento dei processi <!-- GPT translation -->

Stabilisci i giorni e l’orario in base ai quali il JobProcessor eseguirà i modelli attivi. Puoi impostare più date di processamento per un processo. <!-- GPT translation -->

Scegli tra le seguenti opzioni: <!-- GPT translation -->

- Giorno feriale (lunedì-venerdì) <!-- GPT translation -->
- Giorno del mese (1-31): seleziona una data che ricorre in tutti i mesi del periodo di processamento pianificazione. Per esempio, il 30 febbraio non viene considerato. <!-- GPT translation -->
- Ultimo giorno del mese <!-- GPT translation -->

Ogni opzione richiede di impostare l’ora nel formato HH:MM. <!-- GPT translation -->

### Impostare le opzioni di processamento <!-- GPT translation -->

Puoi selezionare l’opzione per eliminare il job dopo il processamento, ; che è utile per pianificare e far girare i processi una sola volta. <!-- more functionality in on-premise --> <!-- GPT translation -->
