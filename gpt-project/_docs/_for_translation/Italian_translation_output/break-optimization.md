---
title: Ottimizzare le pause <!-- DeepL translation -->
product_label:
  - essential
  - advanced
  - enterprise
permalink: /break-optimization/
permalink_reason: /break-optimization/ used in email and in Intercom message
description: Scopri come ottimizzare la distribuzione delle pause nella tua pianificazione per migliorare la copertura. <!-- DeepL translation -->
promote-service: schedule-optimization-workshop
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-activity-coverage.md
deepl_translation: true
---

La funzionalità **Ottimizza le pause** sposta le pause all'interno della tua pianificazione per ottimizzare la copertura delle attività con il fabbisogno di personale.<br> <!-- DeepL translation -->
Gli orari di inizio e fine dei turni non cambiano. La funzionalità **Ottimizzare le pause** non modifica i corridoi di pausa configurati nei modelli di orario, ma sposta le pause all'interno di tali corridoi. Puoi ottimizzare ulteriormente le pause se i fabbisogni di personale cambiano. <!-- DeepL translation -->

### Quando devo Ottimizzare le pause? <!-- DeepL translation -->

Considera l’esempio seguente. <!-- TM 100 -->

Due Dipendenti sono in pianificazione nello stesso giorno con una pausa dalle 12:00 alle 13:00. Le loro pause possono iniziare ogni 30&nbsp;minuti tra mezzogiorno e le 15&nbsp;PM.<br> <!-- DeepL translation -->
Utilizza l'ottimizzazione delle pause per migliorare la copertura delle attività di tipo Presenza intorno a mezzogiorno. L'ottimizzazione delle pause sposta almeno una delle pause a un orario successivo, tra le 12:00 e le 15:00. <!-- DeepL translation -->

### Prerequisiti <!-- TM 100 -->

Per utilizzare la funzionalità **Ottimizzare le pause**, devono essere soddisfatte le seguenti condizioni: <!-- DeepL translation -->

- C'è una pianificazione nella sezione Schedules [livello](/glossario/sovrimpressione/#livello). <!-- aggiungi il link ai livelli una volta che è stato rielaborato https://help.injixo.com/tips-on-shift-center-usage#tip-9-working-with-different-levels --> <!-- DeepL translation -->
- La tua pianificazione include attività di tipo Presenza per le fasce orarie che vuoi ottimizzare. L'ottimizzazione delle pause sostituirà queste attività con delle pause. <!-- DeepL translation -->
- I tuoi modelli di orario includono {% link_new break corridors | features/administration/daymodels/daymodel-creation.md | #add-a-break-activity %}. <!-- DeepL translation -->

## Esegui un'ottimizzazione delle pause <!-- DeepL translation -->

1. Vai su _Plan > Schedules_{:.breadcrumbs}. <!-- TM 100 -->
2. Dal menu _Azioni di pianificazione_{:.doc-button}, seleziona **Approvare gli scambi di turni**. <!-- TM 73 -->
3. Nella sezione **Imposta ottimizzazione delle pause**, configura l'ottimizzazione delle pause: <!-- DeepL translation -->

   - **Unità di pianificazione**: L'unità di pianificazione per la quale vuoi eseguire l'ottimizzazione delle pause. <!-- DeepL translation -->
   - (Opzionale) **Gruppo di selezione** <!-- DeepL translation -->
   - **Intervallo di date**: Puoi selezionare da un giorno fino a due mesi nel futuro. <!-- DeepL translation -->
   <!-- do NOT explain feature-flag-based *Use Smart Optimization* checkbox-->

4. Clicca su _Ottimizza le pause_{:.doc-button}. <!-- non gestito come lavoro di JobProcessor --> <!-- DeepL translation -->

Il processo di ottimizzazione può durare fino a 60&nbsp;minuti. La durata del processo è influenzata da fattori quali il numero di Dipendenti, il numero di pause nella pianificazione e la lunghezza del periodo da ottimizzare. <!-- La funzionalità **Ottimizza le pause** utilizza la migliore soluzione trovata durante il processo di ottimizzazione - in quale altro modo potrebbe funzionare? È necessario? --> <!-- DeepL translation -->
Durante il processo di ottimizzazione, non puoi modificare la pianificazione per l'intervallo di date interessato.<br>Una volta terminata l'ottimizzazione, injixo salva la pianificazione ottimizzata nel livello Schedule<!-- aggiungi il link all'articolo Levels https://help.injixo.com/tips-on-shift-center-usage#tip-9-working-with-different-levels dopo che è stato aggiornato --> e aggiorna lo stato nella sezione **Cronologia dell'ottimizzazione delle pause**. <!-- DeepL translation -->

## Capire lo stato di ottimizzazione <!-- DeepL translation -->

Ogni ottimizzazione delle pause crea una voce nella tabella della sezione **Cronologia dell'ottimizzazione delle pause**. La tabella include dettagli sulla data di inizio dell'ottimizzazione, la persona che l'ha eseguita, l'unità di pianificazione, il gruppo di selezione, il periodo e lo stato. Quando la data di fine di un'ottimizzazione corrisponde alla data corrente, la voce viene rimossa dall'elenco. <!-- DeepL translation -->

La tabella seguente fornisce maggiori dettagli sui possibili stati di ottimizzazione: <!-- DeepL translation -->

| Parametro        | Descrizione                                                                                                                                                                                                      | <!-- TM 66 -->
| ------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| L'ottimizzazione delle pause è riuscita.          | La pianificazione risultante è stata salvata nel livello Schedules.                                                | <!-- DeepL translation -->
| Pianificazione parzialmente ottimizzata | L'ottimizzazione non ha potuto ottimizzare tutte le pause. | Per saperne di più su questo stato, consulta la [sezione dedicata qui sotto] (#pianificazione parzialmente ottimizzata).             | <!-- DeepL translation -->
| Ottimizzazione fallita | Non è stato possibile avviare l'ottimizzazione.          | Prova a riavviare l'ottimizzazione. Se questo stato persiste, crea un ticket per contattare il nostro team di assistenza. | <!-- DeepL translation -->

### Pianificazione parzialmente ottimizzata <!-- DeepL translation -->

<!-- Do not change this heading: /break-optimizations#partly-optimized-schedule is used within the break optimization UI -->

Lo stato Pianificazione parzialmente ottimizzata viene visualizzato quando l'ottimizzazione delle pause non è riuscita a ottimizzare tutte le pause nel periodo selezionato. Ci sono tre possibili cause: <!-- DeepL translation -->

- L'ottimizzazione non ha spostato alcune pause perché, ad esempio, si sarebbero sovrapposte ad attività di tipo Meeting. Le pause mantengono la posizione che avevano prima dell'inizio dell'ottimizzazione. <!-- DeepL translation -->
- L'ottimizzazione non ha incluso alcune pause perché, ad esempio, sono più brevi di 5 minuti o perché non corrispondono all'intervallo {% link_new utilizzato dall'unità di pianificazione | features/administration/create-and-manage-planning-units.md | #create-planning-units %}. <!-- DeepL translation -->
- L'ottimizzazione ha ignorato alcune pause per evitare {% link_new regola di pianificazione | features/administration/create-contracts.md | #scheduling-rules %} violazioni, come ad esempio la pianificazione di una persona per un'attività per la quale non possiede le Qualifiche richieste. <!-- DeepL translation -->

## Vedere i risultati del calcolo <!-- TM 77 -->

Per vedere i dettagli di un'ottimizzazione delle pause completata, clicca sul pulsante _Vedi i risultati_{:.doc}. <!-- DeepL translation -->
Nella finestra che si apre, il riquadro **Stato** mostra il numero di pause ottimizzate.<br> <!-- DeepL translation -->
Un diagramma con due grafici mostra la differenza tra la copertura prima dell'ottimizzazione delle pause (rappresentata da una linea gialla) e la copertura dopo l'ottimizzazione delle pause (rappresentata da una linea verde).<br> <!-- DeepL translation -->
L'asse orizzontale rappresenta le date del periodo selezionato <!-- DeepL translation -->
L'asse verticale rappresenta la copertura totale per tutte le attività pianificate nell'unità di pianificazione e/o nel gruppo di selezione selezionato, espressa in valori assoluti. Ad esempio, un valore di 5 può rappresentare una carenza di personale (5 Dipendenti pianificati in meno rispetto al necessario) o un'eccedenza di personale (5 persone pianificate in più rispetto al previsto). Per saperne di più sulla copertura, {% link_new controlla la tua pianificazione nel livello Pianificazione | funzionalità/scheduling/schedules/schedulazioni-attività-copertura.md %}.<br> <!-- DeepL translation -->

<!-- From this sentence on, we need to change the information about coverage and the graph. "Perfect coverage" is not a term that has any meaning, see: https://ivx.slack.com/archives/C9Y6W10NS/p1691742308844969?thread_ts=1690371315.535319&cid=C9Y6W10NS. The graph label on the y-axis is also very confusing, "coverage - Total deviation from 0. It does not display clearly what is the value in the graph. The deviation is just the absolute value between the real coverage and the optimized coverage. -->

Più la linea verde è vicina allo 0, più l'ottimizzazione delle pause ha migliorato la copertura. <!-- DeepL translation -->

### Come vengono calcolati i valori del grafico? <!-- DeepL translation -->

Considera l’esempio seguente. <!-- TM 100 -->

Hai pianificato due attività nella tua unità di pianificazione: Assistenza clienti e Problemi finanziari. L'unità di pianificazione utilizza un intervallo di 15&nbsp;minuti, che si traduce in quattro intervalli all'ora.<br>La tabella seguente mostra i valori di copertura e la copertura espressa in valori assoluti: <!-- DeepL translation -->

<!-- left-align table -->
<style>
table { <!-- TM 100 -->
   margin-left: 0px; <!-- TM 100 -->
}
</style> <!-- TM 100 -->

| Nome dell'attività | Valori di copertura per intervallo | Valori assoluti di copertura per intervallo | <!-- DeepL translation -->
| ---------------- | ---------------------------- | ------------------------------------- |
| Assistenza clienti | [0, -2, -1, 0] | [0, 2, 1, 0] | <!-- DeepL translation -->
| Problemi finanziari | [3, 2, -2, 0] | [3, 2, 2, 0] | <!-- DeepL translation -->

Per questo esempio, i valori risultanti di copertura totale sull'asse verticale sono 3, 4, 3 e 0. <!-- DeepL translation -->

### Visualizza gli intervalli di un giorno <!-- DeepL translation -->

Se selezioni un periodo fino a tre giorni, il diagramma visualizza gli intervalli per ogni giorno come impostazione predefinita.<br> <!-- DeepL translation -->
Se selezioni un periodo fino a quattro giorni o più, il diagramma visualizza i valori totali per ogni giorno. Per visualizzare gli intervalli di un giorno, procedi come segue: <!-- DeepL translation -->

1. Passa il mouse su un giorno del diagramma e cliccalo. <!-- DeepL translation -->
2. Clicca sul pulsante _Torna alla panoramica giornaliera_{:.doc} per tornare alla panoramica giornaliera. <!-- DeepL translation -->
