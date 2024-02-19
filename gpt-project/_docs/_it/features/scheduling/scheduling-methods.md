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
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/set-a-validity-period.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
---

injixo offre diversi metodi di pianificazione, che puoi utilizzare singolarmente oppure {% link_new in combinazione tra loro | features/scheduling/combined-scheduling-methods.md %}.

I diversi metodi di pianificazione sono pensati per essere usati in situazioni diverse. Tutti i metodi di pianificazione tengono conto delle informazioni configurate nei {% link_new contratti | features/administration/create-contracts.md %} dei dipendenti, come il numero di giorni lavorativi, le ore lavorative giornaliere, settimanali o mensili, e altri parametri di pianificazione.

## Prerequisiti

Prima di cominciare a utilizzare i metodi di pianificazione, è necessario aver configurato i seguenti dati di configurazione in _Plan > Configurazione_{:.breadcrumbs}:

- Qualifiche
- Attività
- Modelli di orario
- Unità di pianificazione
- Contratti
- Dipendenti

Alcuni metodi di pianificazione potrebbero richiedere la configurazione di altri dati di configurazione, per esempio, le rotazioni o i modelli di pianificazione.

## Pianificazione fissa

La pianificazione fissa si basa sulle {% link_new rotazioni | features/administration/shift-sequences.md %}. Una rotazione è una sequenza settimanale di modelli di orario o attività che definisce i giorni in cui un dipendente lavora, e gli orari di inizio e di fine dei suoi turni. Di conseguenza, la pianificazione fissa è il metodo di pianificazione più costante, ma è anche quello che offre la minore flessibilità.

Le pianificazioni create in base alle rotazioni possono essere le stesse ogni settimana, oppure cambiare in intervalli che vanno dalle 2 alle 53 settimane.

Dopo aver creato la pianificazione, puoi sempre {% link_new ottimizzare le pause | features/scheduling/schedules/break-optimization.md %}, oppure avviare l’{% link_new ottimizzazione delle mansioni | features/scheduling/schedules/schedules-job-optimization.md %} per ottimizzare ulteriormente la pianificazione.

La funzionalità **Ottimizzare le pause** sposta le pause pianificate in modo che abbiano il minor impatto sulla copertura. injixo può spostare le pause soltanto all’interno di un {% link_new corridoio in un modello di orario | features/administration/daymodels/daymodel-basics.md | #elementi-fissi-e-corridoi %}.

L’**Ottimizzazione delle mansioni** può sostituire le attività configurate come sostituibili con altre attività pianificabili per ottenere la migliore copertura possibile per tutte le attività in base al loro fabbisogno di personale. Gli orari di inizio e di fine dei turni restano invariati. L’**Ottimizzazione delle mansioni** può anche modificare gli orari delle pause all’interno di una pianificazione, analogamente a quanto fa la funzionalità **Ottimizzare le pause**.

## Pianificazione ottimizzata

La pianificazione ottimizzata è il metodo di pianificazione che offre la maggiore flessibilità. Con questo metodo, utilizzi la funzionalità {% link_new Crea una pianificazione ottimizzata | features/scheduling/schedules/schedules-optimized-schedules.md %} per creare automaticamente una pianificazione completa. injixo garantisce la migliore copertura possibile per tutte le attività con l’impiego di meno dipendenti possibili.

Per impostazione predefinita, la funzionalità **Crea una pianificazione ottimizzata** può pianificare i dipendenti utilizzando qualsiasi {% link_new modello di orario | features/administration/daymodels/daymodel-basics.md %} che è assegnato alla loro unità di pianificazione e che è compatibile con il loro contratto.

A seconda della tua configurazione, pianificare con modelli di orario diversi può generare pianificazioni molto incoerenti, per esempio i dipendenti potrebbero avere il turno di notte il lunedì, il turno pomeridiano il martedì, e il turno di mattina il mercoledì.

Per stabilire quali modelli di orario possono essere utilizzati per creare una pianificazione, configura i {% link_new modelli di pianificazione | features/administration/work-time-pattern-models.md %}. Un modello di pianificazione è composto da {% link_new modelli settimanali | features/administration/work-time-pattern-models.md | #creare-un-modello-settimanale %}, e definisce il modo in cui i modelli di orario vengono assegnati ai dipendenti. Con i modelli di pianificazione puoi creare degli schemi di turni che si ripetono e stabilire dei vincoli di pianificazione per la funzionalità **Crea una pianificazione ottimizzata**.

Per pianificare i dipendenti utilizzando i modelli di pianificazione, assegna un modello di pianificazione a ogni dipendente. Non è possibile assegnare più modelli di pianificazione con lo stesso periodo di validità allo stesso dipendente.

### Turni totalmente flessibili

Per creare pianificazioni con turni totalmente flessibili, crea modelli di pianificazione del {% link_new tipo A | features/administration/work-time-pattern-models.md | #tipi-di-modelli-di-pianificazione %} e assegnali ai dipendenti.

Con il tipo A, injixo può scegliere qualsiasi modello di orario incluso nel modello di pianificazione per ogni giorno di ogni settimana, purché sia compatibile con il contratto di una persona.

Questo metodo genera le pianificazioni migliori per soddisfare le tue esigenze operative. Allo stesso tempo, però, può generare pianificazioni orari molto incoerenti che hanno un impatto negativo sui dipendenti. Per ridurre questo impatto negativo, puoi evitare che determinati turni vengano assegnati ad alcuni dipendenti assegnando loro modelli giornalieri individuali o utilizzando le [disponibilità](#disponibilità).

### Turni flessibili alternati

Per creare pianificazioni con turni flessibili alternati, crea modelli di pianificazione del {% link_new tipo B, C o D | features/administration/work-time-pattern-models.md | #tipi-di-modelli-di-pianificazione %} e assegnali ai dipendenti.

Con i tipi B, C e D stabilisci un ordine specifico che injixo deve seguire durante la selezione dei modelli di orario tra quelli che sono disponibili nel modello di pianificazione selezionato e che sono compatibili con il contratto dei dipendenti. Puoi anche stabilire un orario di inizio fisso per i turni o un intervallo di tempo entro cui i turni possono iniziare.

### Disponibilità

Puoi utilizzare le {% link_new disponibilità | features/administration/availabilities.md %} per definire i giorni o la fascia oraria in cui i dipendenti non sono disponibili a lavorare. Le disponibilità aggiungono alla pianificazione ulteriori restrizioni oltre a quelle definite dai contratti e dagli orari delle unità di pianificazione.

Quando ai dipendenti vengono assegnate delle disponibilità, i dipendenti possono essere pianificati soltanto per turni che rientrano negli intervalli in cui sono disponibili.

## Offerta dei turni

Se utilizzi l’{% link_new offerta dei turni | features/scheduling/schedules/schedules-shift-bidding.md %}, la pianificazione finale viene generata solo dopo che i dipendenti hanno avuto la possibilità di richiedere i turni in injixo Me.

Per creare una pianificazione utilizzando l’offerta dei turni, segui questi passaggi:

1. Stabilisci il numero di turni necessari per un periodo di pianificazione.
2. {% link_new Genera i turni | features/scheduling/schedules/schedules-shift-bidding.md | #generate-shifts %} in base al fabbisogno di personale previsto.
3. Imposta lo status del periodo di pianificazione su **Pubblicato**. I dipendenti possono richiedere due turni per giorno (fino a un massimo di 10).
4. Avvia la {% link_new lotteria dei turni | features/scheduling/shift-bidding.md | #lottery-of-requested-shifts %} per i turni che sono stati richiesti.
5. Assegna i turni restanti. In questo passaggio vengono pianificati i dipendenti le cui richieste non sono state esaudite durante la lotteria dei turni.

Dopo aver creato la pianificazione, puoi comunque avviare l’ottimizzazione delle mansioni per ottimizzare le attività pianificate e la posizione delle pause.

> Utilizza l'attività Presente se combini l'offerta dei turni e l'**Ottimizzazione delle mansioni**.
>
> Se i dipendenti possono richiedere turni in injixo Me ma vuoi avviare l'**Ottimizzazione delle mansioni** in seguito, utilizza soltanto l'attività di sistema predefinita Presente (ID attività: 1) come attività nei modelli di orario. In questo modo eviti che i dipendenti richiedano turni con attività specifiche ma che ricevano attività completamente diverse dall'**ottimizzazione delle mansioni**.
