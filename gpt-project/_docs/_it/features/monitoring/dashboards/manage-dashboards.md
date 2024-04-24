---
title: Gestire i pannelli di controllo
permalink: /it/dashboards-overview/
promote-service: team-leader-training
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Utilizza i pannelli di controllo per analizzare il volume di contatto e il livello di occupazione.
related_articles:
  - overwrite_title: Lavorare con i grafici
    filepath: features/monitoring/dashboards/work-with-charts.md
  - overwrite_title: Esempi di pannelli di controllo
    filepath: features/monitoring/dashboards/dashboards-examples.md
redirect_from:
  - /it/dashboards-overview/
redirect_reason: Updated filename on 5 March 2024
---

In _Analyze > Dashboards_{:.breadcrumbs} puoi creare e visualizzare pannelli di controllo con un massimo di quattro grafici diversi. Ogni grafico può includere diagrammi per più serie temporali e intervalli di date. Se non esiste ancora nessun pannello di controllo, la pagina mostra la modalità di modifica, e puoi [creare un pannello di controllo](#creare-un-pannello-di-controllo).

- Per mostrare un pannello di controllo esistente, selezionalo dal menu a tendina o digita il nome nel campo per filtrare i risultati.  
- Per visualizzare i valori per un intervallo specifico, passa il mouse sopra un grafico nel pannello di controllo.
- Per passare alla modalità a schermo intero, clicca sull’{% icon maximize %} in alto a destra.

Puoi anche {% link_new passare dalla visualizzazione dei grafici a quella delle tabelle e viceversa | features/monitoring/dashboards/work-with-charts.md | #orientarsi-tra-i-grafici %} con l'icona Mostra tabella {% icon table-list | icon-only %} e l'icona Mostra grafico {% icon chart-view | icon-only %} in alto a destra della schermata.

## Creare un pannello di controllo

1. Vai su _Analyze > Dashboards_{:.breadcrumbs}.
2. Dal {% icon ellipsis_v %} a destra seleziona **Crea nuova dashboard**.
3. Configura i campi seguenti:
  - **Nome**: nome unico per il pannello di controllo.
  - **Layout**: seleziona il numero e il formato dei grafici.
  - **Grafico senza titolo**: nome per ogni grafico. I nomi non devono essere unici.
4. Seleziona un **intervallo di date** per ogni grafico.
5. (Facoltativo) Attiva l'opzione **Usa le date disponibili** per spostare la data di inizio di un giorno ogni giorno.
6. Dai menu espandibili a sinistra trascina le serie temporali nei grafici per visualizzare diversi dati chiave:
   - **Workload**: dati storici, previsioni, previsioni importate, e {% link_new versioni della previsione | features/forecast/injixo-forecast/save-forecast-versions.md %}.
   - **Unità di pianificazione**: copertura del personale, fabbisogno di personale e copertura per turni e attività pianificati, oltre ai turni richiesti in Me.
   - **Code WFM**: i dati dei workload in code WFM che hai salvato cliccando su _Utilizza previsione_{:.doc-button} nella pagina del workload. Quest’opzione potrebbe non essere disponibile nel tuo piano WFM. 

      > Nota
      >
      > - L’ {% icon circle_exclamation %} nella legenda di un grafico viene visualizzata se per un dato periodo non sono disponibili dati.
      > - Nei workload potresti vedere dei dati chiave speciali, a seconda della tua integrazione: per esempio se i tuoi workload contengono solo code da un'[integrazione Genesys Cloud](/add-genesys-cloud-integration/), vedrai informazioni relative alle chiamate abbandonate, alla velocità media di risposta e alle chiamate a cui è stata data risposta entro il livello di servizio.

7. Clicca su _Salva_{:.doc-button}.<br>Per tornare alla modalità di visualizzazione, clicca su _Chiudi la modalità Modifica_{:.doc-button}.

### Duplicare un pannello di controllo

Per creare un nuovo pannello di controllo con le stesse proprietà generali di un pannello di controllo esistente, segui questi passaggi:
1. Vai su _Analyze > Dashboards_{:.breadcrumbs}.
2. Dal menu a tendina seleziona un pannello di controllo.
3. Dal {% icon ellipsis_v %} seleziona **Duplica dashboard**.
4. Se necessario, modifica il nome e i dati di configurazione.
5. Clicca su _Salva_{:.doc-button}.

### Aggiornare automaticamente un pannello di controllo

È possibile aggiornare automaticamente il pannello di controllo selezionato. Per farlo, seleziona un intervallo dal menu a tendina a destra e clicca sull' _{% icon arrows-rotate | icon-only %} Aggiorna automaticamente_{:.doc-button}.<br>In basso a sinistra nella pagina puoi vedere l'ultimo aggiornamento del pannello di controllo.

## Modificare un pannello di controllo

1. Vai su _Analyze > Dashboards_{:.breadcrumbs}.
2. Dal menu a tendina seleziona un pannello di controllo.
3. Dal {% icon ellipsis_v %} a destra seleziona **Modifica**.
4. Modifica il pannello di controllo, {% link_new personalizza le serie temporali | features/monitoring/dashboards/work-with-charts.md | #personalizzare-le-serie-temporali %} oppure {% link_new eliminale | features/monitoring/dashboards/work-with-charts.md | #eliminare-le-serie-temporali %}.
5. Clicca su _Salva_{:.doc-button}. Per tornare alla modalità di visualizzazione, clicca su _Chiudi la modalità Modifica_{:.doc-button}.

## Eliminare un pannello di controllo

1. Vai su _Analyze > Dashboards_{:.breadcrumbs}.
2. Dal menu a tendina seleziona un pannello di controllo.
3. Dal {% icon ellipsis_v %} a destra seleziona **Modifica**.
4. Clicca su _Elimina_{:.doc-button} in basso a destra.  
5. Nella finestra di conferma, clicca su _Elimina dashboard_{:.doc-button}.<br> Per annullare l’eliminazione, clicca su _Mantieni dashboard_{:.doc-button}.

Se elimini l’ultimo pannello di controllo esistente, la pagina mostrerà la modalità di modifica finché non [crei un nuovo pannello di controllo](#creare-un-pannello-di-controllo).
