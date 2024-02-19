---
title: Modificare o eliminare il fabbisogno di personale
toc: false
product_label:
  - advanced
  - enterprise
description: Scopri come modificare o eliminare il fabbisogno di personale calcolato da injixo.
archive_ref: 20210819-en-employee-requirement
related_articles:
  - overwrite_title: Che cos’è il Centro dei turni?
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/calculate-a-forecast.md
  - overwrite_title: Calcolare il fabbisogno di personale
    filepath: features/forecast/injixo-forecast/staff-requirement.md
  - overwrite_title: Avviare l’ottimizzazione delle mansioni
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Creare una pianificazione ottimizzata
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
---

Il fabbisogno di personale definisce il numero di dipendenti necessari per un’attività in un dato periodo. Il fabbisogno di personale è necessario per creare le pianificazioni con la funzionalità **Crea una pianificazione ottimizzata**, o per ottimizzarle con l’**Ottimizzazione delle mansioni** o con la funzionalità **Ottimizzare le pause**.

Il calcolo del fabbisogno di personale è l’ultimo passaggio del procedimento di previsione. In injixo Forecast puoi utilizzare il fabbisogno di personale calcolato in modo automatico o utilizzare uno dei metodi di calcolo del fabbisogno di personale. Prima di creare una pianificazione, assicurati che il fabbisogno di personale sia stato calcolato per tutte le attività rilevanti.

## Vedere e modificare il fabbisogno di personale

In injixo è possibile vedere il fabbisogno di personale nelle quattro sezioni seguenti:

- _Forecast_{:.menu-item}
- _Analyze > Dashboard_{:.breadcrumbs}
- _Plan > Schedules_{:.breadcrumbs}
- _Plan > Centro dei turni_{:.breadcrumbs} 

La tabella seguente contiene informazioni dettagliate sulle opzioni disponibili in ciascuna sezione:

<style>
table {
   margin-left: 0px;
}
</style>

| Dove  | Vedere | Modificare | Eliminare |
| ------ |--------| -------- |-------- |
| _Forecast_{:.menu-item} | Sì | Sì | Sì |
| _Analyze > Dashboard_{:.breadcrumbs} | Sì | No | No |
| _Plan > Schedules_{:.breadcrumbs} | Sì | No | No |
| _Plan > Centro dei turni_{:.breadcrumbs} | Sì | Sì | No |

### Modificare il fabbisogno di personale nel Centro dei turni

1. Vai su _Plan > Centro dei turni_{:.breadcrumbs}.
2. In fondo alla pagina, seleziona la scheda **Attività - Fabbisogno** o sulla scheda **Sintesi delle attività**.<br>
   > Messaggio Nessun dato in una cella
   >
   > Se in una cella nella tabella più in basso compare il messaggio Nessun dato, seleziona **Piano** o **Stato effettivo** dal menu a tendina **Levels** in alto a destra.

3. Per espandere un’unità di pianificazione, clicca sull’icona con il segno più {% icon plus | icon-only %} a sinistra delle tabelle.
4. Clicca con il tasto destro su una cella nella tabella più in basso e seleziona **Elabora il fabbisogno di dipendenti**.
5. Nella finestra **Elabora il fabbisogno di dipendenti**, clicca su una cella e inserisci il nuovo valore.<br>
  Non è possibile modificare le celle su sfondo azzurro perché rappresentano attività che sono state eliminate ma sono ancora assegnate all’unità di pianificazione.<br>
  
6. (Facoltativo) Per modificare diverse celle contemporaneamente, copia una riga di valori da un foglio di calcolo. Clicca su una cella e trascina il mouse verso destra. Premi Ctrl+V per incollare i valori.<br>
7.  Clicca su _OK_{:.doc-button}.

### Modificare il fabbisogno di personale in Forecast

Per modificare manualmente il fabbisogno di personale puoi utilizzare lo script di fabbisogno costante in _Forecast_{:.breadcrumbs}. Il procedimento seguente spiega come configurare lo script per questo caso specifico. Per saperne di più sulle altre opzioni di configurazione, leggi l’articolo {% link_new Requisito costante | features/forecast/requirement-scripts/requirement-constant.md %}.

1. Vai su _Forecast > Script di fabbisogno_{:.breadcrumbs}.
2. Nel riquadro **Altri - Costante**, clicca su _Apri_{:.doc-button}.<br>
3. Nella finestra di configurazione dello script, configura i parametri seguenti (i nomi dei parametri sono in inglese):
   - Nella sezione **Date**:
     - **Start Date**: inserisci la data di inizio della modifica al fabbisogno di personale.
     - **Number of Days**: inserisci il numero di giorni consecutivi a partire dalla data di inizio per i quali vuoi modificare il fabbisogno di personale.
     - **Consider Each Day of the Week**: seleziona **No**.
     - **Add to Existing Requirement**: lascia questa casella non spuntata.
     - **Number Of Days With Timespans**: per modificare il fabbisogno di personale per tutti i giorni compresi in un dato periodo seleziona 1.
     - **Timespans Per Day**: seleziona il numero di periodi nell'ambito di un giorno per i quali vuoi modificare il fabbisogno di personale (per esempio, scegli 1 se vuoi modificare il fabbisogno di personale per un giorno intero; scegli 3 se vuoi impostare dei fabbisogni di personale diversi per la mattina, per il pomeriggio e per la sera).
     - **Number of Activities**: scegli il numero di attività per le quali vuoi modificare il fabbisogno di personale.
   - Nella sezione **Data**:
     - **Planning unit** e **Activity**: seleziona l’unità di pianificazione e l’attività per le quali vuoi modificare il fabbisogno di personale.
     - **Agents**: inserisci il numero di dipendenti per il fabbisogno di personale.
     - **Start** e **End**: definisci l’intervallo o gli intervalli di tempo per i quali vuoi modificare il fabbisogno di personale.
4. Clicca su _OK_{:.doc-button}.

## Eliminare il fabbisogno di personale

injixo non prevede un’opzione per eliminare il fabbisogno di personale. Puoi impostare il fabbisogno di personale a 0: questo corrisponde a eliminare il fabbisogno di personale.

 Ci sono due modi per impostare il fabbisogno di personale a 0:
 - Segui i passaggi per [modificare il fabbisogno di personale nel Centro dei turni](#modificare-il-fabbisogno-di-personale-nel-centro-dei-turni) e inserisci 0 nelle celle rilevanti.
 
 - Segui i passaggi per [modificare il fabbisogno di personale in Forecast](#modificare-il-fabbisogno-di-personale-in-forecast) e inserisci 0 nel campo **Agents**.

L’immagine di seguito mostra la configurazione dello script di fabbisogno costante per eliminare il fabbisogno di personale in Forecast per un giorno completo (in questo esempio è il Day 1):

{{ 3 | image: 'Esempio di script di fabbisogno costante con una attività dalle 00:00 alle 00:00 e fabbisogno di personale 0', '80%' }}
