---
title: Script per le multiattività
description: Calcolare il fabbisogno di personale per le multiattività.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /it/requirement-multiactivity/
redirect_reason: Updated filename on 06 March 2024
---

Utilizza lo script per le multiattività per calcolare il fabbisogno di personale per le tue multiattività. Il calcolo si basa su Erlang-C e sul livello di servizio.

## Prerequisiti

- Crea almeno una {% link_new multiattività | features/administration/activity-types-and-properties.md | #subattività %} e assegnala alla tua unità di pianificazione.
- Crea un {% link_new workload | features/forecast/injixo-forecast/create-workloads.md | #creare-un-workload %} per ogni subattività della multiattività.

## Esportare la previsione per tutti i workload delle subattività

Prima di poter eseguire lo script per le multiattività, esporta le previsioni per i workload creati per tutte le subattività:

1. In _Forecast > Workloads_{:.breadcrumbs} seleziona il workload che hai creato per una subattività.
2. Seleziona il periodo nel selettore di data. Clicca sul numero della settimana per selezionare la settimana per intero, oppure clicca e trascina per selezionare un periodo più breve o più lungo.
3. Dal {% icon ellipsis_v %} in alto a destra, seleziona **Utilizza previsione**.
4. Nella finestra che si apre seleziona la previsione che vuoi utilizzare.
5. Clicca su _Utilizza previsione_{:.doc-button}.
6. Clicca su _Chiudi_{:.doc-button}.
7. Ripeti i passaggi dall’1 al 6 per tutti i workload creati per le tue subattività.

injixo salva i dati necessari al calcolo del fabbisogno di personale in code in _WFM > Administration > Forecasting > Servizi_{:.breadcrumbs}. Le code hanno il nome del workload corrispondente, preceduto da un asterisco, per esempio: *nomeDelWorkload.

## Configurare lo script

1. Vai su _Forecast > Script di fabbisogno_{:.breadcrumbs}.
2. Nel riquadro **Chiamate entranti - Multi-attività**, clicca su _Apri_{:.doc-button}.  
3. Nella finestra di configurazione dello script, configura i parametri seguenti (i nomi di alcuni parametri sono in inglese):
   - Nella sezione **Data**:
     - **Data d'inizio**: inserisci la data di inizio per il calcolo del fabbisogno di personale.
     - **Numero giorni**: inserisci il numero di giorni dopo la data di inizio per i quali vuoi calcolare il fabbisogno di personale.
   - Nella sezione **Parametri Unità pianificative**:
     - **Unità pianificativa** e **Multiattività**.<br>
     La finestra di configurazione dello script si aggiorna e mostra i parametri di calcolo per le subattività rivelanti.
   - Nella sezione **Subattività** puoi configurare dei parametri di calcolo diversi per ogni subattività. Comincia dai parametri nella sezione **Parametri Servizi**:
    - **Calculation Method** (metodo di calcolo): scegli tra **Erlang-C**, **Linear** e **Chat**.<br>La finestra di configurazione dello script si aggiorna e mostra i parametri di calcolo rivelanti. Vedi la [tabella qui sotto](#parametri-di-calcolo-nella-sezione-parametri-erlang-c) per scoprire quali parametri sono configurabili per ciascun metodo di calcolo.
    - **Servizio**: seleziona la coda che contiene i dati che vuoi utilizzare per il calcolo.
    - **Operazioni**: seleziona il tipo di volume di contatto, per esempio Chiamate entranti.
    - **Durata media di gestione** (AHT): se i tuoi workload hanno un tempo medio di gestione (AHT) previsto, seleziona il valore corrispondente. Altrimenti seleziona **[Nessuno]**.
    - **Versione**: seleziona **Auto-Forecast**. In injixo Enterprise on-premise puoi selezionare una versione diversa.

## Parametri di calcolo nella sezione Parametri Erlang C

| Parametro                         | Descrizione                                                                                                            | Configurabile in Erlang-C | Configurabile in Linear | Configurabile in Chat |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |--------  | -------- |
| Service level (%) (Livello di servizio, in percentuale)             | La percentuale di contatti che dovrebbero essere processati nel lasso di tempo configurato nel parametro                                                                                                                                                                    | Sì | No | Sì |
| Service level (sec.) (Livello di servizio, in secondi)            | Il lasso di tempo entro il quale la percentuale di contatti che configuri nel parametro **Service level (%)** dovrebbe essere processata.                                                                                                                                                                                            | Sì | No | Sì |
| Supplemento (%)                         | Il valore percentuale per il quale vuoi incrementare il fabbisogno di personale calcolato. Scopri come [configurare questo parametro](#configurare-il-parametro-supplemento--per-tenere-conto-dello-shrinkage) per tenere dello shrinkage. | Sì | Sì | Sì |
| Risorse minime            | Inserisci un valore per sovrascrivere un fabbisogno di personale troppo basso.                                                                                                                                                                                                                                                     | Sì | Sì | Sì |
| Risorse massime            | Inserisci un valore per sovrascrivere un fabbisogno di personale troppo alto.                              | Sì | Sì | Sì |
| Durata media costante di gestione (AHT fisso) | Se hai selezionato un tipo nel parametro **Durata media di gestione** nella sezione **Parametri Servizi**, qui lascia il valore prestabilito.<br> Se hai selezionato **[Nessuno]** nel parametro **Durata media di gestione**, inserisci un valore in secondi.                                 | Sì | Sì | Sì |
| Seq (%)                  | La percentuale di AHT che i dipendenti impiegano in compiti che non possono essere svolti in parallelo, come, per esempio, l’elaborazione post-chiamata.                                                                                                                                                                                                                                                                                   | No | No | Sì |
| Numero massimo di sessioni                          | Il numero massimo di sessioni di chat che un dipendente può gestire contemporaneamente.                                                                                                                                             | No | No | Sì |

### Configurare il parametro Supplemento (%) per tenere conto dello shrinkage

Per configurare il parametro **Supplemento (%)** in modo che tenga conto dello shrinkage, utilizza la formula seguente, dove s% è il tuo tasso di shrinkage: 1/(1-s%)-1. Il risultato espresso in percentuale è il valore che devi inserire nel parametro **Supplemento (%)**. Per esempio, per tenere conto di uno shrinkage del 20%, calcola 1/(1-0.2)-1, il cui risultato è 25%.

## Avviare lo script

- Per avviare il calcolo, clicca su _OK_{:.doc-button}.<br>Si apre una finestra che mostra i paramentri che hai inserito e i risultati dello script. <br>

## Vedere i risultati del calcolo

Puoi vedere il fabbisogno di personale aggiornato per l’unità di pianificazione e la multiattività selezionate in {% link_new Dashboards | features/monitoring/dashboards/manage-dashboards.md %} o nella finestra dei parametri nel {% link_new Centro dei turni | features/scheduling/edit-or-delete-staff-requirements.md %} o in {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %}.

