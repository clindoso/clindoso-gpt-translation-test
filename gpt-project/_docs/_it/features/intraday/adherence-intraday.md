---
title: Utilizzare Aderenza Intraday
toc: true
product_label:
  - advanced
  - enterprise
description: Ottieni una panoramica del grado di aderenza dei dipendenti alla loro pianificazione durante il giorno.
---

In _Intraday > Aderenza Intraday_{:.breadcrumbs} puoi confrontare le attività pianificate per i dipendenti con le attività effettive, per identificare eventuali periodi fuori aderenza durante il giorno. Aderenza Intraday utilizza i {% link_new dati di aderenza in tempo reale | features/intraday/real-time-adherence.md %} provenienti dal tuo sistema ACD. Puoi accedere ai dati sull'aderenza per il mese in corso e per gli ultimi sei mesi.

## Prerequisiti

Per vedere i dati sull’aderenza, assicurati che si verifichino le seguenti condizioni:
- Hai aggiunto un'{% link_new integrazione | features/acd-integration/cloud/how-integrations-work.md %} che supporta l'importazione dei dati sugli stati degli agenti.
- Hai configurato l’{% link_new importazione dei dati sugli stati degli agenti | features/acd-integration/cloud/import-agent-status-data.md %}.

## Visualizzare i dati

Per mostrare i dati sull’aderenza per un giorno specifico, segui questi passaggi:

1. Seleziona un'**unità di pianificazione** o una **selezione**, oppure entrambe.
2. In cima alla pagina, seleziona una data utilizzando il selettore di data, o clicca su _Oggi_{:.doc-button} o _Ieri_{:.doc-button}.

La pagina mostra il punteggio totale di adesione, i punteggi di adesione per intervallo e una tabella con i dettagli dei dati di adesione per dipendente per il giorno selezionato.

### Punteggio di aderenza

La pagina mostra diversi dettagli sui punteggi di aderenza:

- **Aderenza**: la percentuale del tempo lavorativo trascorso in attività pianificate. Se il giorno non è ancora terminato, il punteggio viene calcolato fino all'ultimo timestamp aggiornato, che è visualizzato sopra il punteggio. Se il punteggio scende al di sotto del {% link_new punteggio di aderenza target | features/intraday/real-time-adherence.md | #define-the-target-adherence-score %}, viene evidenziato in rosso.
- **Punteggi per intervallo**: le barre blu verticali rappresentano i punteggi per intervallo. I punteggi inferiori al 100% rappresentano gli intervalli durante i quali le attività effettive dei dipendenti deviano dalle loro attività pianificate.
- **Punteggio di aderenza target**: la linea tratteggiata nel grafico mostra il punteggio di aderenza target.

<!-- Adherence in %	Percentage of working time spent in activities that comply with the scheduled activities	Minutes in adherence/scheduled minutes * 100% -->

### Tabella con la panoramica del personale

Sotto il punteggio di aderenza totale e i punteggi per intervallo, una tabella mostra i dettagli sull’aderenza per il giorno selezionato. Per ordinare i dati della tabella in base al punteggio di aderenza, clicca sull'intestazione **Aderenza**. Per ordinare i dati della tabella in base al nome, clicca sull’intestazione **Nome**. Scopri come {% link_new filtrare e ordinare | features/intraday/real-time-adherence.md | #search-and-filter %}.
Ogni riga mostra il punteggio di aderenza di un dipendente. Le discrepanze tra le attività pianificate per il dipendente e le sue attività effettive sono evidenziate. 

Quando il punteggio di un dipendente scende al di sotto del punteggio di aderenza target, il suo punteggio è evidenziato in rosso. Le {% link_new corrispondenze | features/intraday/adherence-matches.md %} e i {% link_new periodi di tolleranza | features/intraday/real-time-adherence.md | #buffer-time %} influiscono sugli stati e sui tipi di aderenza. Scopri che cosa sono lo {% link_new stato e i tipi | features/intraday/real-time-adherence.md | #status %}.

I tre tipi di non-aderenza sono identificati dai seguenti colori:

- Rosso: Non presente
- Giallo: Attività incorretta
- Azzurro: Non pianificata

## Aderenza intraday dei dipendenti

Per vedere i dettagli dell’aderenza di un dipendente in una nuova finestra, clicca sulla riga del dipendente. Per cambiare le date, utilizza il selettore del mese o le frecce di navigazione accanto alle date.

A sinistra, due riquadri mostrano una panoramica del mese selezionato:

- **Nome del dipendente**: mostra il punteggio di aderenza del dipendente, per quanto tempo era pianificato e i dettagli sull'aderenza per il mese selezionato. I valori includono i dati fino all'ultimo intervallo completato del giorno in corso.
- **Panoramica giornaliera**: i giorni per i quali sono disponibili dei punteggi di aderenza sono evidenziati in rosso. Passa il mouse su una data per vedere il punteggio di aderenza del dipendente selezionato. Clicca su una data per vedere più dettagli.

A destra, puoi vedere in dettaglio quando il dipendente era pianificato e gli intervalli in cui non ha rispettato la pianificazione:

- **Punteggio dell’aderenza Intraday**: calcolato utilizzando i dati fino all’ultimo intervallo completato del giorno in corso. È identico al punteggio giornaliero che vedi quando passi il mouse sopra una data nella **panoramica giornaliera**.
- Durata **Pianificati** e **Fuori aderenza**: somma delle durate di tutte le attività pianificate (attività del tipo Presenza, Meeting e Pausa) e deviazioni nel programma nella data selezionata.
- **Cronologia**: le barre colorate evidenziano le attività pianificate, le attività effettive, e gli stati fuori aderenza.  Nella riga **Fuori aderenza**, clicca sulle fasce temporali fuori aderenza per ingrandire. Clicca su _Ripristina zoom_{:.doc-button} per ripristinare lo zoom.
- **Tabella**: ogni riga mostra i dettagli dei periodi fuori aderenza. Clicca su un'intestazione per ordinare i dati in base al periodo di tempo, all’attività effettiva, allo stato, all’attività pianificata o alla durata fuori aderenza.

## Report sull’aderenza (file CSV)

Se vuoi analizzare i dati sull’aderenza alle attività pianificate e all'orario per singoli dipendenti su periodi più lunghi, per esempio per calcolare dei bonus, puoi scaricare un report in formato CSV che include i dati aggregati sull’aderenza alle attività pianificate e all’orario. Per scaricare il report sull'aderenza, segui questi passaggi:

1. Seleziona un'**unità di pianificazione** o una **selezione**, oppure entrambe.
2. Clicca su _Scarica report_{:.doc-button}.  
3. Nella finestra **Scarica report**, seleziona un periodo di riferimento per il report. Puoi scegliere qualsiasi intervallo di tempo, fino a un massimo di sei mesi nel passato.
4. Clicca su _Scarica report_{:.doc-button}.

La tabella qui sotto illustra le colonne del report, che sono in inglese.

| Colonna                     | Descrizione                                                                              | Calcolo                                                               |
| -------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Activity                   | L’attività alla quale si riferiscono i dati sull’aderenza.                                  | --                                                                         |
| Scheduled minutes          | La durata programmata per l'attività, in minuti.                                     | --                                                                         |
| Actual minutes             | Il tempo effettivamente impiegato nell'attività pianificata, in minuti.                             | --                                                                         |
| Minutes in adherence       | Il tempo impiegato in attività che corrispondono alle attività pianificate.                       | --                                                                         |
| Minutes out of adherence   | Il tempo impiegato in attività che non corrispondono alle attività pianificate.                | --                                                                         |
| Adherence in %             | La percentuale di tempo lavorativo impiegato in attività che corrispondono alle attività pianificate. | Minuti in aderenza alle attività pianificate/minuti pianificati * 100%                             |
| Minutes out of conformance | La differenza tra il tempo lavorativo effettivo e il tempo lavorativo pianificato.                    | Minuti effettivi di lavoro − minuti pianificati                                 |
| Conformance in %           | La percentuale di tempo lavorativo in aderenza al tempo lavorativo pianificato.                 | Tempo effettivo/tempo pianificato * 100%                                         |
| Scheduled in %             | La percentuale di tempo lavorativo pianificato per un’attività di un certo tipo.               | Tempo pianificato per il tipo attività in questione/tempo pianificato totale * 100% |
| Actual in %                | La percentuale di tempo lavorativo effettivamente impiegato in un’attività di un certo tipo.            | Tempo effettivo per il tipo di attività in questione/tempo effettivo totale * 100%       |

Ogni riga di dati include un link per visualizzare i dati in _Intraday > Aderenza Intraday_{:.breadcrumbs}.

## Domande frequenti

| Domanda                            | Risposta                                                                                                                                                                                        |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Perché alcuni dipendenti, o tutti, non sono visibili? | Prova a svuotare il campo di ricerca. Controlla se i dipendenti che cerchi sono pianificati per oggi nell’unità di pianificazione o nella selezione che hai scelto.                                                        |
| Perché non riesco a selezionare una specifica data? | È possibile accedere ai dati sull’aderenza storica per i sei mesi precedenti alla data attuale, più il mese in corso (per esempio, se oggi è il 15 luglio, puoi selezionare date comprese tra l’1 gennaio e il 15 luglio). |
| Quale fuso orario viene utilizzato da Aderenza Intraday? | Aderenza Intraday utilizza il fuso orario dell’unità di pianificazione selezionata. Il fuso orario è visibile in alto a destra della cronologia dell’aderenza. |