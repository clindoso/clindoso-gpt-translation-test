---
title: Metodi di pianificazione
promote-service: new-planner-training
description: Scopri i diversi metodi di pianificazione disponibili in injixo.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Combinare diversi metodi di pianificazione
    filepath: features/scheduling/combined-scheduling-methods.md
  - overwrite_title: Creare contratti
    filepath: features/administration/create-contracts.md
  - overwrite_title: Impostare le date <!--temporary title-->
    filepath: features/administration/set-a-validity-period.md
  - overwrite_title: Creare e configurare i dipendenti
    filepath: features/administration/employee-overview.md
  - overwrite_title: Configurare injixo Me
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
---

Leggendo questo articolo, scoprirai:
- quali metodi di pianificazione possono essere utilizzati;
- quale metodo di pianificazione utilizzare in base al caso specifico.

Puoi utilizzare un solo metodo di pianificazione, oppure {% link_new combinarne | features/scheduling/combined-scheduling-methods.md %} più di uno.

I metodi di pianificazione tengono conto delle informazioni incluse nei {% link_new contratti | features/administration/create-contracts.md %} che sono assegnati ai dipendenti. I contratti includono il numero di giorni lavorativi, le ore lavorative giornaliere, settimanali o mensili, e altri parametri utili per la pianificazione.

## Pianificazione fissa

La pianificazione fissa è il metodo che permette la minore flessibilità. Questo metodo di pianificazione è basato sulle {% link_new rotazioni | features/administration/shift-sequences.md %}.

Le rotazioni definiscono:  
- i giorni lavorativi di un dipendente;
- l’ora d’inizio e l’ora di fine esatte del turno per ogni giorno lavorativo.

Le pianificazioni create in base a queste rotazioni possono essere le stesse ogni settimana, oppure cambiare sulla base di intervalli lunghi dalle 2 alle 53 settimane.  

Dopo aver creato la pianificazione, puoi ottimizzare i seguenti elementi:  
- la posizione delle pause all’interno di {% link_new corridoi | features/administration/daymodels/daymodel-basics.md | #elementi-fissi-e-corridoi %};
- le {% link_new attività sostituibili | features/administration/activity-types-and-properties.md | #proprietà-delle-attività %}.

## Pianificazione ottimizzata

La pianificazione ottimizzata è il metodo che permette la maggiore flessibilità. Utilizza {% link_new Crea una pianificazione ottimizzata | features/scheduling/schedules/schedules-optimized-schedules.md %} per creare automaticamente una pianificazione completa. injixo genererà la migliore copertura possibile per le varie attività con il minor numero di dipendenti.

Per definire quali turni sono disponibili per la pianificazione, utilizza i {% link_new modelli di pianificazione | features/administration/work-time-pattern-models.md %}.

### Turni totalmente flessibili

Per ottenere dei turni totalmente flessibili, assegna ai tuoi dipendenti il modello di pianificazione di {% link_new tipo A | features/administration/work-time-pattern-models.md | #types-of-work-time-pattern-models %}.  

I turni che sono disponibili in base al modello di pianificazione e che sono in accordo con il contratto del dipendente possono essere pianificati in qualunque giorno. 

Per aumentare le probabilità che le pianificazioni siano accettate dai dipendenti, è possibile escludere alcuni turni attribuendo ai dipendenti dei modelli di orario personali, oppure utilizzando le [disponibilità](#disponibilità).

### Turni flessibili con avvicendamento

Per ottenere dei turni flessibili con avvicendamento, assegna ai tuoi dipendenti modelli di pianificazione di {% link_new tipo B, C o D | features/administration/work-time-pattern-models.md | #types-of-work-time-pattern-models %}.

I turni che sono disponibili in base al modello di pianificazione scelto e che sono in accordo con il contratto del dipendente vengono pianificati secondo un ordine specifico. Possono persino avere la stessa ora di inizio tutti i giorni.

### Disponibilità

Le {% link_new disponibilità | features/administration/availabilities.md %} possono essere aggiunte alla pianificazione ottimizzata per restringere le opzioni di turni.

## Offerta dei turni

Con l'{% link_new offerta dei turni | features/scheduling/schedules/schedules-shift-bidding.md %}, la pianificazione viene finalizzata solo dopo aver coinvolto i dipendenti. I dipendenti possono richiedere i turni che preferiscono all’interno del portale dei dipendenti.

Panoramica della procedura:

1. Definisci il numero di turni necessari.
2. Genera i turni sulla base del fabbisogno di personale previsto.
3. Imposta lo status del periodo di pianificazione su **Pubblicato**. I dipendenti possono richiedere fino a due turni per giorno (fino a 10 turni in totale).
4. Avvia la {% link_new lotteria dei turni | features/scheduling/shift-bidding.md | #lottery-of-requested-shifts %} per i turni richiesti.
5. Assegna i turni restanti. In questo passaggio vengono pianificati i dipendenti le cui richieste non sono state esaudite durante la lotteria dei turni.
