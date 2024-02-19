---
title: Filtrare con i gruppi di selezione
description: Impara a utilizzare i gruppi di selezione come filtri.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: true
---

È la prima volta che ti occupi di gruppi di selezione? Meglio cominciare dalle {% link_new basi | features/administration/selections.md %}.

Per gestire un team è spesso necessario raggruppare i dipendenti che hanno condizioni lavorative simili, come, per esempio, i dipendenti che devono occuparsi dei figli piccoli, o i dipendenti che hanno lo stesso supervisore. I gruppi di selezione ti permettono di definire dei criteri di raggruppamento personalizzati. Questo può tornare utile quando ti servono altre opzioni di raggruppamento, oltre alle {% link_new unità di pianificazione | features/administration/create-and-manage-planning-units.md %} e ai {% link_new filtri personalizzati | features/administration/employee-filter.md %}.

Con le unità di pianificazione puoi raggruppare i dipendenti in base alla struttura della tua organizzazione, per esempio assegnando i dipendenti che lavorano in fusi orari diversi a unità di pianificazione diverse, mentre i filtri personalizzati sono basati sugli elementi della configurazione di injixo, come i contratti e le attività. Con i gruppi di selezione puoi raggruppare i dipendenti in modo che soddisfino le esigenze specifiche della tua organizzazione.

Puoi creare un gruppo di selezione per affinare la ricerca con i filtri nell’ambito di una unità di pianificazione oppure per gestire i dipendenti che sono in unità di pianificazione diverse. Per esempio, puoi creare un gruppo di selezione che raggruppa i dipendenti con figli piccoli, così che le loro pianificazioni possano essere gestite separatamente, oppure un gruppo di selezione per filtrare le pianificazioni di dipendenti che appartengono a unità di pianificazione diverse, per una campagna di marketing in posti con fusi orari diversi.

## Utilizzare i gruppi di selezione per filtrare i dipendenti all’interno di una unità di pianificazione

injixo offre filtri in base alle unità di pianificazione e ai gruppi di selezione in **Plan** e **Intraday**. Dopo aver selezionato l’unità di pianificazione, puoi filtrare ulteriormente i dipendenti in base al gruppo di selezione.

Per esempio, se hai tre unità di pianificazione, e una di queste include dei dipendenti che stanno partecipando a una formazione,  puoi utilizzare i gruppi di selezione per raggrupparli e gestire separatamente le loro pianificazioni, per esempio per programmare delle riunioni specifiche.

## Utilizzare i gruppi di selezione per gestire i dipendenti che appartengono a unità di pianificazione diverse

In injixo ci sono tre modi per filtrare con i gruppi di selezione i dipendenti che sono in unità di pianificazione diverse. Trovi i rispettivi esempi sotto questa sezione.

La tabella seguente offre una panoramica delle tre opzioni per filtrare i dipendenti che sono in unità di pianificazione diverse. Troverai queste opzioni nei componenti o nelle funzionalità di injixo.

| Componente/funzionalità | Opzione per filtrare i dipendenti |
|-------------------------|----------------------------|
| Schedules               | Tutte le unità di pianificazione e un gruppo di selezione. |
| Ferie/Assenze                | Tutte le unità di pianificazione e un gruppo di selezione. |
| Aderenza in Tempo Reale     | Un gruppo di selezione e nessuna unità di pianificazione. |
| Aderenza Intraday      | Un gruppo di selezione e nessuna unità di pianificazione. |
| Centro dei turni            | Un gruppo di selezione (il filtro per l’unità di pianificazione non è disponibile). |
| Informa i dipendenti           | Una unità di pianificazione e un gruppo di selezione. Ripeti per tutte le unità di pianificazione alle quali vuoi applicare il filtro. |
| Periodi di pianificazione  | Una unità di pianificazione e un gruppo di selezione. Ripeti per tutte le unità di pianificazione alle quali vuoi applicare il filtro. |
| Meetings                | Una unità di pianificazione e un gruppo di selezione. Ripeti per tutte le unità di pianificazione alle quali vuoi applicare il filtro. |
| Periodi di permesso        | Una unità di pianificazione e un gruppo di selezione. Ripeti per tutte le unità di pianificazione alle quali vuoi applicare il filtro. |
| Ferie spettanti    | Una unità di pianificazione e un gruppo di selezione. Ripeti per tutte le unità di pianificazione alle quali vuoi applicare il filtro. |

Per tutte le funzionalità in _Plan > Schedules > Azioni di pianificazione_{:.breadcrumbs}, devi selezionare una unità di pianificazione e un gruppo di selezione, e applicare l’azione di pianificazione a ogni unità di pianificazione che vuoi filtrare.

Gli esempi seguenti danno più dettagli sulle tre opzioni per filtrare con i gruppi di selezione descritte nella tabella precedente.

## Esempi

Gli esempi qui di seguito utilizzano un gruppo di selezione chiamato Inserimento. Il gruppo di selezione Inserimento raggruppa i dipendenti neoassunti, a prescindere dall’unità di pianificazione a cui appartengono. Con il gruppo di selezione Inserimento è più semplice gestire le loro pianificazioni e tener conto delle loro esigenze.

La configurazione seguente ti permette di utilizzare il gruppo di selezione Inserimento come filtro per diverse unità di pianificazione:

1. {% link_new Crea e configura un gruppo di selezione | features/administration/selections.md | #creare-i-gruppi-di-selezione %} chiamato Inserimento.
2. {% link_new Assegna i dipendenti | features/administration/selections.md | #assegnare-i-dipendenti-ai-gruppi-di-selezione  %} neoassunti al gruppo di selezione Inserimento.

### Opzione 1: tutte le unità di pianificazione e un gruppo di selezione

In _Plan > Schedules_{:.breadcrumbs}, puoi filtrare le pianificazioni dei dipendenti nel gruppo di selezione Inserimento con i seguenti menu a tendina:

- **Unità di pianificazione**: seleziona **Tutte le unità di pianificazione**.
- **Scegli la selezione**: seleziona **Inserimento**.  
   Se il menu a tendina **Scegli la selezione** non viene visualizzato, clicca sull’icona {% icon selection-filter-u %} in alto.

### Opzione 2: un gruppo di selezione e nessuna unità di pianificazione

In _Intraday > Aderenza in Tempo Reale_{:.breadcrumbs}, puoi filtrare le attività pianificate per i dipendenti che appartengono al gruppo di selezione Inserimento, e confrontarle con lo stato effettivo del dipendente in tempo reale. Questa funzione è utile, per esempio, per controllare se un dipendente sta svolgendo le attività pianificate per la sua fase di inserimento.

Per filtrare in base al gruppo di selezione, utilizza i seguenti menu a tendina:

- **Unità di pianificazione**: assicurati che nessuna unità di pianificazione sia selezionata.
- **Selezione**: seleziona **Inserimento**.

### Opzione 3: un gruppo di selezione e un’unità di pianificazione

Se i dipendenti nella fase di inserimento hanno delle condizioni particolari per i permessi, puoi creare dei periodi di permesso specifici per il gruppo di selezione Inserimento. Considera le seguenti unità di pianificazione per tre sedi diverse: Ufficio 1, Ufficio 2 e Ufficio 3. In questi 3 uffici lavorano dei dipendenti che sono nella fase di inserimento e sono assegnati al gruppo di selezione Inserimento.

Per creare dei periodi di permesso specifici per il gruppo di selezione Inserimento:

1. In _Plan > Ferie/Assenze_{:.breadcrumbs}, clicca su _Periodi di permesso_{:.doc-button}.  
   Si aprirà la pagina **Periodi di permesso**.
2. Clicca su _Nuovo periodo di permesso_{:.doc-button}.  
   Si aprirà una finestra.
3. Filtra in base alla selezione con i menu a tendina seguenti:  
   - **Unità di pianificazione**: scegli **Ufficio 1**.
   - **Selezione**: scegli **Inserimento**.
4. Compila gli altri campi.  
   Scopri come configurare i {% link_new periodi di permesso | features/scheduling/time-off/time-off-periods.md %}.
5. Clicca su _Salva_{:.doc-button}.
6. Ripeti i passaggi da 1 a 5 per le unità di pianificazione Ufficio 2 e Ufficio 3.
