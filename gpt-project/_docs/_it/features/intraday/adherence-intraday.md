---
title: Aderenza Intraday
toc: true
product_label:
  - advanced
  - enterprise
description: Ottieni una panoramica del grado di aderenza dei dipendenti alla loro pianificazione nel corso della giornata.
---

Con Aderenza Intraday, puoi confrontare le attività pianificate con le attività effettive dei dipendenti per identificare i periodi fuori aderenza nel corso della giornata.

In Aderenza Intraday i dati saranno visibili dopo che avrai impostato l’{% link_new importazione degli stati degli agenti in tempo reale | features/acd-integration/cloud/import-agent-status-data.md %}.

È la prima volta che ti occupi di aderenza in tempo reale? Meglio cominciare dalle {% link_new basi | features/intraday/real-time-adherence.md %}.

## Visualizzare e cercare i dati

1. Vai su _Intraday > Aderenza Intraday_{:.breadcrumbs}.
2. Per visualizzare i dati sugli agenti, seleziona un'unità di pianificazione e/o una selezione.
3. Per visualizzare un altro giorno, clicca su _Oggi_{:.doc-button} o _Ieri_{:.doc-button}, oppure seleziona una data.

La tabella mostra i dettagli dei periodi fuori aderenza per dipendente. Nell’intestazione della tabella, puoi identificare i periodi con un’aderenza bassa. Puoi ordinare la tabella o utilizzare la funzione di ricerca in alto per filtrare i dati visualizzati grazie alle opzioni per {% link_new filtrare e ordinare | features/intraday/real-time-adherence.md | #search-and-filter %}.

{{ 1 | image: 'Aderenza Intraday','100%' }}

> Limita la visualizzazione dei dati di alcuni dipendenti a utenti specifici
>
> Configura i diritti di accesso a unità di pianificazione o selezioni specifiche in base agli {% link_new utenti o ruoli utente | getting-started/configure-user-roles.md | #impostare-le-autorizzazioni-per-wfm %}.

## Punteggio di aderenza

Il punteggio mostra se ci sono state discrepanze tra le attività pianificate e le attività effettive dei dipendenti.

Grazie al grafico, puoi analizzare l’aderenza lungo il corso della giornata. Se la giornata non è finita, il punteggio viene calcolato fino al momento dell’ultimo aggiornamento, che è mostrato sopra il punteggio dell’aderenza.

La linea tratteggiata indica il punteggio di aderenza target. Scopri come {% link_new modificarlo | features/intraday/real-time-adherence.md | #define-the-target-adherence-score %}.

{{ 2 | image: 'Punteggio di aderenza','100%' }}

## Tabella con l’aderenza degli agenti

La tabella mostra i dettagli sull’aderenza dei dipendenti pianificati per il giorno in corso. È possibile ordinare i dati della tabella in base al nome del dipendente e al punteggio di aderenza.

Ogni riga della tabella contiene la linea temporale di un dipendente. Puoi individuare facilmente le discrepanze tra le attività pianificate e le attività effettive del dipendente. Ogni dipendente ha un punteggio di aderenza personale. I punteggi individuali si sommano e formano il punteggio totale dell’unità di pianificazione (visibile nell’intestazione della colonna). Le deviazioni sono evidenziate quando il punteggio scende al di sotto del {% link_new punteggio aderenza target configurato | features/intraday/real-time-adherence.md | #define-the-target-adherence-score %}.

I colori identificano i tre tipi di stati fuori aderenza:

- Non presente (rosso)
- Attività incorretta (giallo)
- Non pianificata (blu)

Clicca su un agente per vedere la sua {% link_new aderenza intraday | features/intraday/adherence-intraday.md | #aderenza-intraday-dei-dipendenti %}. Le {% link_new corrispondenze | features/intraday/adherence-matches.md %} e i {% link_new periodi di tolleranza | features/intraday/real-time-adherence.md | #buffer-time %} influiscono sugli stati e sui tipi di aderenza. Scopri di più sugli {% link_new stati e i tipi | features/intraday/real-time-adherence.md | #status %} di aderenza.

{{ 3 | image: 'Tabella con l’aderenza dei dipendenti','100%' }}

## Aderenza intraday dei dipendenti

La schermata Aderenza intraday dei dipendenti include maggiori dettagli sugli eventi che influiscono sull’aderenza. Qui è possibile vedere quali dipendenti non hanno aderito alla pianificazione. Per approfondire le attività di un dipendente durante la giornata, clicca su una voce della pianificazione. Le singole attività verranno mostrate usando i colori configurati.

Nella linea temporale, potrai confrontare le attività pianificate e quelle effettive, e vedere i relativi stati fuori aderenza. La tabella sottostante contiene una riga per ogni periodo fuori aderenza.

Per modificare il giorno visualizzato, puoi:

- selezionare il mese in alto e utilizzare la panoramica giornaliera a sinistra;
- utilizzare le frecce che si trovano a destra e a sinistra della data attuale, sopra la tabella.

La panoramica giornaliera mostra il punteggio di aderenza per ogni giorno del mese selezionato. Sopra la panoramica giornaliera vedrai dei dati relativi al mese in corso, come, per esempio, il punteggio di aderenza o il totale di ore pianificate.

{{ 4 | image: 'Dettagli sull’aderenza intraday dei dipendenti','120%' }}

## Report sull’aderenza (file CSV)

In certi casi potresti avere bisogno di analizzare i dati sull’aderenza e sulla conformità di alcuni dipendenti specifici per un periodo più lungo, per esempio per calcolare dei bonus. Il report sull’aderenza è un file in formato CSV che include dati aggregati sull’aderenza e sulla conformità. Per scaricarlo, segui questi passaggi:

1. Vai su _Intraday > Aderenza Intraday_{:.breadcrumbs}.
2. Seleziona almeno un’unità di pianificazione e/o una selezione.
3. Clicca su _Scarica report_{:.doc-button}.  
   Si aprirà una finestra.
4. Seleziona un periodo di riferimento per il report. Puoi scegliere qualsiasi intervallo di tempo, fino a un massimo di sei mesi nel passato.
5. Clicca su _Scarica report_{:.doc-button}.

La tabella qui sotto illustra le colonne del report, che sono in inglese.

| Colonna             | Descrizione                                                                     | Calcolo                                                                |
| ------------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Minutes in adherence | Minuti in aderenza: il tempo impiegato in attività che corrispondono alle attività pianificate      | -- |
| Minutes out of adherence  | Minuti fuori aderenza: il tempo impiegato in attività che non corrispondono alle attività pianificate        | -- |                  
| Adherence in %   | Aderenza in percentuale: la percentuale di tempo di lavoro impiegato in attività che corrispondono alle attività pianificate       | Minuti in aderenza/minuti pianificati * 100% |
| Minutes out of conformance   | Minuti fuori conformità: la differenza tra il tempo di lavoro effettivo e il tempo di lavoro pianificato             | Minuti effettivi di lavoro – minuti pianificati |
| Conformance in % | Conformità: la percentuale di tempo di lavoro in conformità con il tempo di lavoro pianificato | Tempo effettivo/tempo pianificato * 100% |
| Scheduled in %  | Pianificato in percentuale: la percentuale del tempo di lavoro pianificato per un’attività di un certo tipo | Tempo pianificato per il tipo di attività/tempo pianificato totale * 100%              |
| Actual in %  | Effettivo in percentuale: la percentuale del tempo di lavoro effettivamente impiegato in un’attività di un certo tipo | Tempo effettivo per il tipo di attività/tempo effettivo totale * 100%              |

Ogni riga di dati include un link per visualizzare i dati in _Intraday > Aderenza Intraday_{:.breadcrumbs}.

## Domande frequenti

| Domanda                            | Risposta                                                                                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Perché alcuni dipendenti, o tutti, non sono visibili? | Prova a svuotare il campo di ricerca. Controlla se i dipendenti che cerchi sono pianificati per oggi nell’unità di pianificazione o nella selezione che hai scelto.           |
| Perché non riesco a selezionare una specifica data? | È possibile accedere ai dati sull’aderenza storica per i sei mesi precedenti alla data attuale, più il mese in corso (per esempio, se oggi è il 15 luglio, puoi selezionare date comprese tra l’1 gennaio e il 15 luglio). |
