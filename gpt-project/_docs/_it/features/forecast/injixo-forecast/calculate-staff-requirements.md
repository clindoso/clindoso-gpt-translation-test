---
title: Calcolare il fabbisogno di personale
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Calcola il fabbisogno di personale per le chiamate, le chat, le email e altro.
related_articles:
  - overwrite_title: Script per le multiattività
    filepath: features/forecast/requirement-scripts/requirement-multiactivity.md
  - overwrite_title: Script per le chiamate in uscita
    filepath: features/forecast/requirement-scripts/requirement-outbound.md
  - overwrite_title: Script per il fabbisogno di personale costante
    filepath: features/forecast/requirement-scripts/requirement-constant.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/edit-or-delete-staff-requirements.md
redirect_from:
  - /it/staff-requirement/
redirect_reason: Updated filename on 04 March 2024
---

Dopo aver creato una previsione puoi calcolare il fabbisogno di personale. Puoi scegliere tra i diversi script di fabbisogno e metodi di calcolo disponibili in injixo. Se è necessario puoi anche definire un fabbisogno di personale costante senza previsioni.

È la prima volta che utilizzi injixo Forecast? Meglio cominciare dalle {% link_new basi | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Metodi di calcolo e script di fabbisogno

injixo offre metodi di calcolo e script di fabbisogno.
Scopri qual è lo {% link_new script di fabbisogno o metodo di calcolo | best-practices/requirement-scripts.md %} più adatto al tuo caso.<br>
Scopri come configurare i [metodi di calcolo](#configurare-i-metodi-di-calcolo) nella prossima sezione.<br>
Per imparare a configurare gli script di fabbisogno, clicca sui link seguenti:

- {% link_new Script per le multiattività | features/forecast/requirement-scripts/requirement-multiactivity.md %}
- {% link_new Script per le chiamate in uscita | features/forecast/requirement-scripts/requirement-outbound.md %}
- {% link_new Script per il fabbisogno di personale costante | features/forecast/requirement-scripts/requirement-constant.md %}

## Configurare i metodi di calcolo

I metodi di calcolo calcolano il fabbisogno di personale tenendo conto delle importazioni di dati recenti, delle modifiche ai parametri di calcolo e delle {% link_new regolazioni manuali | features/forecast/injixo-forecast/manual-adjustments.md %}.
Puoi cambiare il metodo di calcolo scelto in qualsiasi momento.

1. In _Forecast > Workload_{:.breadcrumbs}, scegli un workload.
2. Nella sezione **Fabbisogno di personale**, clicca su _Modifica fabbisogno di personale_{:.doc-button}.
3. Dal menu a tendina **Metodo di calcolo** scegli un’opzione:
   - **Erlang-C**
   - **Chat**
   - **Linear**
4. Nella sezione **Parametri di calcolo**, configura i [parametri di calcolo](#parametri-di-calcolo).
5. Nella sezione **Unità di pianificazione e attività associate**, seleziona l’unità di pianificazione e l’attività per le quali vuoi utilizzare il fabbisogno di personale.  
   Scopri come [utilizzare il fabbisogno di personale per la pianificazione](#utilizzare-il-fabbisogno-di-personale-per-la-pianificazione).
6. Clicca su _Salva_{:.doc-button}.

Il grafico nella sezione **Fabbisogno di personale** mostra il fabbisogno di personale calcolato.<br> Sotto il grafico vedrai i valori che hai configurato per i parametri e il totale delle ore di lavoro necessarie per il periodo selezionato.<br> Muovi il mouse sopra il grafico per vedere dettagli sul volume, sul tempo medio di gestione (AHT), sul fabbisogno di personale, sulle regolazioni manuali e sugli eventi aggiunti all'intervallo.

### Parametri di calcolo

La tabella seguente include i parametri che è possibile configurare per ogni metodo di calcolo:

| Parametro                         | Descrizione                                                                                                                                                                                                                                                                                                           | Configurabile in Erlang-C | Configurabile in Chat | Configurabile in Linear |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |--------  | -------- |
| Livello di servizio target              | Percentuale di chiamate o chat in entrata che devono essere processate entro il tempo di risposta target.                                                                                                                                                                                                                                                                          | Sì | Sì | No |
| Tempo di risposta target                | Tempo in cui la percentuale di chiamate o di chat indicata nel parametro Livello di servizio target deve essere processata.                                                                                                                                                                                            | Sì | Sì | No |
| Shrinkage                         | La percentuale di tempo retribuito in cui i dipendenti non sono in grado di lavorare, per esempio per le pause bagno, i ritardi, le assenze per malattia non pianificate e i problemi tecnici. | Sì | Sì | Sì |
| Numero minimo di dipendenti            | Inserisci un valore per sovrascrivere gli intervalli che hanno un fabbisogno di personale più basso.                                                                                                                                                                                                                                                     | Sì | Sì | Sì |
| Numero massimo di dipendenti            | Inserisci un valore per sovrascrivere gli intervalli con fabbisogno di personale più elevato.                              | Sì | Sì | Sì |
| Tempo medio di gestione (AHT) fisso | Inserisci un valore per sovrascrivere l’AHT previsto.<br>Spunta la casella **Applica l’AHT fisso solo quando non ci sono valori AHT** per utilizzare l’AHT fisso soltanto per i periodi senza dati sull’AHT. Per impostazione predefinita, il calcolo del fabbisogno di personale utilizza i valori dell’AHT provenienti dalla previsione.                                  | Sì | Sì | Sì |
| Sessioni massime                  | Numero massimo di sessioni di chat parallele che i dipendenti possono gestire contemporaneamente.                                                                                                                                                                                                                                                                                   | No | Sì | No |
| Overhead                          | Percentuale dell’AHT che un dipendente deve impiegare in compiti che non possono essere svolti in parallelo, per esempio riportare nel sistema CRM gli appunti in seguito a una telefonata. Questo parametro non viene tenuto in considerazione se hai inserito 1 nel campo **Sessioni massime**.                                                                                                                                             | No | Sì | No |

## Utilizzare il fabbisogno di personale per la pianificazione

Per creare una pianificazione sulla base del fabbisogno di personale, devi prima salvarlo. Per salvare il fabbisogno di personale, segui i passaggi descritti di seguito.

È possibile utilizzare il fabbisogno di personale calcolato per le versioni di una previsione o per le previsioni importate che hai salvato per il periodo selezionato.<br>
Scopri che cosa sono le {% link_new versioni di una previsione | features/forecast/injixo-forecast/store-forecast-versions.md %} e come {% link_new importare una previsione | features/forecast/injixo-forecast/import-forecast.md %}.

1. In _Forecast > Workload_{:.breadcrumbs}, scegli un workload.
2. Scegli il periodo per il quale vuoi utilizzare il fabbisogno di personale.
3. Nella sezione **Fabbisogno di personale**, scegli una versione della previsione dal menu a tendina a sinistra.
4. Clicca su _Salva fabbisogno di personale_{:.doc-button}.
5. Nella finestra **Salva fabbisogno di personale**, clicca su _Salva_{:.doc-button}.

injixo salva il fabbisogno di personale per l’unità di pianificazione e l’attività che hai selezionato durante la configurazione del metodo di calcolo.

> Nota
>
> È possibile utilizzare il fabbisogno di personale per un’unità di pianificazione o un’attività diversa. <br> Per farlo, ripeti il procedimento per [configurare i metodi di calcolo](#configurare-i-metodi-di-calcolo), e seleziona un’unità di pianificazione o un’attività diversa. Poi segui il procedimento per [utilizzare il fabbisogno di personale per la pianificazione](#utilizzare-il-fabbisogno-di-personale-per-la-pianificazione).
