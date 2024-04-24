---
title: Regolare la previsione
product_label:
  - advanced
  - enterprise
  - classic
description: Regola manualmente i volumi di contatto e l’AHT previsti.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/calculate-staff-requirements.md
  - overwrite_title: Aggiungere eventi e festivi
    filepath: features/forecast/injixo-forecast/events-and-holidays.md
---

Puoi regolare una previsione generata per rimuovere irregolarità dal volume di contatto o dal tempo medio di gestione (AHT).

Regola la previsione se si verifica una delle seguenti condizioni:

- Non hai abbastanza dati storici, o i dati non sono accurati.
- Il volume di contatto o i valori dell’AHT si discostano dalle tendenze attuali e non prevedi che questa situazione cambi. Queste deviazioni potrebbero essere causate, per esempio, da modifiche strutturali del tuo modello aziendale.
- I volumi di contatto sono insolitamente alti o bassi durante un dato periodo, per esempio durante una campagna di marketing.<br> In questo caso, rimuovi le irregolarità o {% link_new aggiungi un'interruzione | features/forecast/injixo-forecast/events-and-holidays.md  | #aggiungere-un-evento-o-uninterruzione-a-un-workload %} per escludere il periodo dal calcolo della previsione.

Eventuali nuovi calcoli delle previsioni non sovrascrivono i valori modificati manualmente.

## Regolare il volume

1. In _Forecast > Workload_{:.breadcrumbs}, scegli un workload.
2. Seleziona un intervallo di tempo dal selettore di data. Clicca sul numero della settimana per selezionare la settimana intera, oppure clicca su un giorno e trascina per selezionare un periodo più breve o più lungo di una settimana.<br>L’intervallo di tempo che selezioni determina le opzioni di regolazione visualizzate.
3. Nella sezione del volume, clicca su _Regola il volume_{:.doc-button}.
4. Nella finestra di configurazione, configura la regolazione:
  - **Intervallo di date**: disponibile se nel passaggio 2 hai selezionato un periodo di diversi giorni.
  - **Ora di inizio** e **Ora di fine**: disponibili se nel passaggio 2 hai selezionato un solo giorno.
  - **modifica (%)** o **sovrascrivi**: seleziona un’opzione dal menu a tendina.<br>**modifica (%)** regola il valore attuale del volume secondo una percentuale, che può essere un numero positivo o negativo.<br>**sovrascrivi** sostituisce il valore attuale del volume con un nuovo valore, che deve essere un numero intero positivo.
  - **Valore**: inserisci un valore per modificare o sovrascrivere il volume.<br>Scopri [come vengono regolati i valori del volume e dell’AHT](#in-che-modo-lintervallo-di-tempo-selezionato-influisce-sulle-regolazioni-del-volume-e-dellaht).
5. Clicca su _Applica regolazione_{:.doc-button}.<br>
   Le modifiche sono evidenziate nel grafico del volume. Passa con il mouse sopra il grafico per vedere più dettagli sul volume di contatto, sull’AHT, sul fabbisogno di personale e sugli eventi.

## Regolare l’AHT

1. In _Forecast > Workload_{:.breadcrumbs}, scegli un workload.
2. Seleziona un intervallo di tempo dal selettore di data. Clicca sul numero della settimana per selezionare la settimana intera, oppure clicca su un giorno e trascina per selezionare un periodo più breve o più lungo di una settimana.
3. Accanto a **AHT**, clicca sull’{% icon eye_slash %}.
4. Clicca su _Regola l’AHT_{:.doc-button}.
5. Nella finestra di configurazione, configura la regolazione:
  - **Intervallo di date**: disponibile se nel passaggio 2 hai selezionato un periodo di diversi giorni.
  - **Ora di inizio** e **Ora di fine**: disponibili se nel passaggio 2 hai selezionato un solo giorno.
  - **modifica (%)** o **sovrascrivi**: seleziona un’opzione dal menu a tendina.<br>**modifica (%)** regola il valore attuale dell’AHT secondo una percentuale, che può essere un numero positivo o negativo.<br>**sovrascrivi** sostituisce il valore attuale dell’AHT con un nuovo valore, che deve essere un numero intero positivo.
  - **Valore**: inserisci un valore per modificare o sovrascrivere l’AHT.<br> Scopri [come vengono regolati i valori del volume e dell’AHT](#in-che-modo-lintervallo-di-tempo-selezionato-influisce-sulle-regolazioni-del-volume-e-dellaht).
6. Clicca su _Applica regolazione_{:.doc-button}.<br>
  Le modifiche sono evidenziate nel grafico dell’AHT. Passa con il mouse sopra il grafico per vedere più dettagli sul volume di contatto, sull’AHT, sul fabbisogno di personale e sugli eventi.
 
Ripeti questa procedura per regolare di nuovo i valori se c’è una differenza significativa tra la previsione generata e la tua regolazione manuale.

> Nota
>
> Se regoli di nuovo i valori del volume o dell’AHT, la finestra di configurazione non mostra i valori che hai inserito in precedenza. Un nuovo aumento o diminuzione in percentuale aggiorna il valore modificato in precedenza, non il valore originale.

## In che modo l'intervallo di tempo selezionato influisce sulle regolazioni del volume e dell’AHT?

Le regolazioni hanno un impatto diverso a seconda dell'intervallo di tempo che hai selezionato nel selettore di data:

| Valore  |      Intervallo di tempo              |  Impatto della regolazione |
| ----------- | ---------------------------- | ------------------------------------------------------------------------------------------------------ | 
| Volume |     Un solo giorno      | Un valore in percentuale riduce o incrementa i valori esistenti per tutti gli intervalli compresi tra l'**ora di inizio** e l'**ora di fine**.<br> Un valore assoluto sovrascrive i valori esistenti per tutti gli intervalli compresi tra l'**ora di inizio** e l'**ora di fine**.                                               |
| Volume | Diversi giorni | Sia un valore in percentuale che un valore assoluto incrementano o riducono il volume totale. Il valore si distribuisce proporzionalmente nel periodo selezionato, mantenendo invariate le tendenze e i modelli di distribuzione per tutti gli intervalli.                                                                      |
|  AHT   |     Un solo giorno     | Un valore in percentuale riduce o incrementa i valori esistenti per gli intervalli compresi tra l'**ora di inizio** e l'**ora di fine**.<br> Un valore assoluto sovrascrive i valori esistenti per tutti gli intervalli compresi tra l’**ora di inizio** e l’**ora di fine**.                                                                                       |
|  AHT   | Diversi giorni | Sia un valore in percentuale che un valore assoluto incrementano o riducono la media ponderata totale visualizzata. I valori dell’AHT si distribuiscono lungo il periodo selezionato, mantenendo invariate le tendenze e i modelli di distribuzione per tutti gli intervalli. Questo potrebbe causare valori più alti o più bassi in uno o più giorni. |

## Eliminare le regolazioni

È possibile eliminare le regolazioni che non sono più rilevanti.

1. In _Forecast > Workload_{:.breadcrumbs}, scegli un workload.
2. Seleziona le regolazioni che vuoi eliminare.
  - Nella sezione del volume, clicca su _Regola il volume_{:.doc-button}.
  - Nella sezione dell’**AHT**, clicca su _Regola l’AHT_{:.doc-button}.
3. Seleziona un **intervallo di date**.
4. Clicca su _Elimina tutte le regolazioni_{:.doc-button} per rimuovere tutte le regolazioni dall'intervallo di date selezionato.<br>
  injixo mostra i valori di previsione originali per l'intervallo di date selezionato.

## Utilizzare il fabbisogno di personale per la pianificazione

Le regolazioni manuali ricalcolano automaticamente il fabbisogno di personale.

Se hai {% link_new configurato il calcolo del fabbisogno di personale | features/forecast/injixo-forecast/calculate-staff-requirements.md %} nella pagina dei workload, puoi utilizzare i nuovi valori per la pianificazione cliccando su _Salva fabbisogno di personale_{:.doc-button}.<br>
Per utilizzare i valori aggiustati per lo script per le multiattività, per le chiamate in uscita o per il fabbisogno costante, procedi come di seguito:

1. Dal {% icon ellipsis_v %} in alto a destra, seleziona **Utilizza previsione**.
2. Nella finestra di configurazione, clicca su _Utilizza previsione_{:.doc-button}.
3. In _Forecast > Script di fabbisogno_{:.breadcrumbs} seleziona uno script.
4. Configura lo script e avvialo.<br>Scopri come configurare lo {% link_new script per le multiattività | features/forecast/requirement-scripts/multiactivity-script.md %}, lo script per le {% link_new chiamate in uscita | features/forecast/requirement-scripts/outbound-calls-script.md %} e lo script per il {% link_new fabbisogno costante | features/forecast/requirement-scripts/requirement-constant.md %}.
