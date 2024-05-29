---
title: Automatizza i lavori ricorrenti con JobManager <!-- DeepL translation -->
product_label:
  - enterprise
description: Automatizza la generazione di report e molto altro ancora utilizzando il JobManager. <!-- DeepL translation -->
promote-service: enhanced-reporting
deepl_translation: true
---

In _WFM > Amministrazione > Sistema > JobManager_{:.breadcrumbs}, gli utenti con accesso all'amministrazione possono impostare modelli di lavoro per lavori ricorrenti, come l'inserimento di sequenze di turni, la creazione di report, l'esecuzione della lotteria o dell'assegnazione dei turni e il calcolo dei conti lavoro target. <!-- DeepL translation -->

 <!-- che può essere eseguito con i privilegi di altri utenti. --> <!-- DeepL translation -->

<!-- Il JobProcessor esegue i modelli attivati all'ora specificata. --> <!-- DeepL translation -->

## Creare un modello settimanale <!-- TM 61 -->

1. Clicca sull'icona {% item-add %}. <!-- DeepL translation -->
2. Inserisci un **Nome** (massimo 50 caratteri). <!-- TM 71 -->
3. Seleziona la casella **Abilitato** per attivare l'esecuzione programmata. <!-- DeepL translation -->
4. Seleziona un tipo di lavoro. Questa categoria non ha alcun impatto, ma puoi ordinare per tipo di lavoro in un secondo momento. <!-- DeepL translation -->
5. Imposta una **Priorità**. Gamma di valori: da 1 a 10 (il più basso) <!-- DeepL translation -->
6. (Opzionale) Seleziona un altro **Utente**. L'impostazione predefinita è l'utente attualmente connesso. Può essere utilizzato per eseguire tipi di lavoro con permessi diversi. <!-- DeepL translation -->
6. Clicca su _Chiudi_{:.doc-button}. <!-- TM 69 -->
   Configura le informazioni aggiuntive necessarie per eseguire i lavori nelle sezioni Periodo di tempo per l'elaborazione dei lavori, Parametri di elaborazione dei lavori e Date di elaborazione dei lavori. <!-- DeepL translation -->

<!-- Per modificare i modelli esistenti, clicca su una voce dell'elenco. --> <!-- DeepL translation -->
<!-- I modelli esistenti con i parametri configurati possono essere modificati in qualsiasi momento tramite _JobManager_{:.menu-item}. --> <!-- DeepL translation -->

<!-- obsoleto per il cloud --> <!-- DeepL translation -->
<!-- {{ 1 | image: "Job Configuration", '50%' }} --> <!-- DeepL translation -->

### Imposta il periodo di tempo per l'elaborazione del lavoro <!-- DeepL translation -->

Definisce in quali giorni deve essere eseguito un modello attivo. I periodi possono essere assoluti utilizzando un intervallo di date fisso o relativi per le settimane o i mesi attuali o precedenti. I periodi relativi alla data corrente sono utili per i lavori ricorrenti. <!-- DeepL translation -->

Ad esempio, per creare un report ogni giorno alle 6 del mattino per il giorno precedente, seleziona quanto segue: <!-- DeepL translation -->

- Unità di tempo: Relativa <!-- DeepL translation -->
- Valore di riferimento fino a: -1 (Seleziona **giorno** dal menu a tendina) <!-- DeepL translation -->
- Valore di riferimento fino a: -1 (disponibile dopo aver cliccato su **OK** per salvare le altre proprietà generali del modello) <!-- DeepL translation -->

### Imposta i parametri di elaborazione del lavoro <!-- DeepL translation -->

Quando salvi un lavoro, viene impostato solo il periodo di tempo per l'elaborazione del lavoro. Aggiungi gli altri parametri generali e specifici per il lavoro uno alla volta per ogni lavoro come segue: <!-- DeepL translation -->

4. Clicca sull’icona Aggiungi {% icon item-add | icon-only %}. <!-- TM 86 -->
   Si aprirà una finestra. <!-- TM 100 -->
2. Inserisci un **Nome** (massimo 50 caratteri). <!-- TM 66 -->
3. Inserisci un **Valore** per il parametro definito come nome. <!-- DeepL translation -->

Per saperne di più sui parametri e sui valori disponibili, consulta l'articolo {% link_new JobManager examples | features/reporting/jobmanager/jobmanager-examples.md %}. <!-- DeepL translation -->

### Imposta le date di elaborazione dei lavori <!-- DeepL translation -->

Definisce in quali giorni e a che ora il JobProcessor esegue i modelli attivi. Puoi impostare una o più date di elaborazione per un lavoro. <!-- DeepL translation -->

Scegli tra le seguenti opzioni: <!-- DeepL translation -->

- Giorno feriale (lunedì-domenica) <!-- DeepL translation -->
- Giorno del mese (1-31): Seleziona una data che ricorre in ogni mese del periodo di elaborazione del lavoro. Ad esempio, il 30 febbraio non viene eseguito. <!-- DeepL translation -->
- Ultimo giorno del mese <!-- DeepL translation -->

Ogni opzione richiede di impostare l'ora nel formato HH:MM. <!-- DeepL translation -->

### Imposta le opzioni di elaborazione del lavoro <!-- DeepL translation -->

Puoi selezionare la casella di controllo per cancellare il lavoro dopo l'elaborazione, il che è utile per pianificare ed eseguire i lavori solo una volta. <!-- maggiori funzionalità in on-premise --> <!-- DeepL translation -->
