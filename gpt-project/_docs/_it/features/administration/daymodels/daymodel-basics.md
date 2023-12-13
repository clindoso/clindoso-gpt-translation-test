---
title: Comprendere i modelli di orario
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Scopri che cosa sono i modelli di orario, che cosa devi tenere in considerazione prima di creare un modello di orario, e l'impatto delle modifiche ai modelli di orario sulla pianificazione.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
---

I modelli di orario sono schemi per i turni. Rappresentano la giornata lavorativa dei dipendenti che pianifichi, e definiscono quando i dipendenti sono disponibili per il lavoro, le ore di inizio e di fine dei turni, nonché il numero di ore giornaliere di lavoro di un dipendente. injixo crea le pianificazioni sulla base dei modelli di orario.

Per impostazione predefinita, i modelli di orario che crei vengono assegnati automaticamente a tutte le unità di pianificazione della tua organizzazione. Per modificare questa impostazione, {% link_new modifica l’unità di pianificazione | features/administration/create-and-manage-planning-units.md | #limit-day-models %}. Durante l’ottimizzazione della pianificazione, injixo terrà in considerazione soltanto i modelli di orario assegnati all’unità di pianificazione.

Se i modelli di orario configurati per la tua unità di pianificazione non rispecchiano alcuni accordi di lavoro, puoi anche aggiungere dei modelli di orario personalizzati a singoli dipendenti. Durante l’ottimizzazione della pianificazione, injixo terrà in considerazione quei modelli di orario personalizzati solo per il dipendente in questione.

I modelli di orario contengono le attività del tipo Presenza, Assenza e Pausa di un turno. Per questo motivo, è necessario {% link_new aggiungere le attività rilevanti ai modelli di orario | features/administration/daymodels/daymodel-creation.md %}.  <!--  Add #add-activities-to-day-models when IT day model creation is updated-->

I modelli di orario vengono aggiunti alle {% link_new rotazioni | features/administration/shift-sequences.md %} e possono essere raggruppati in {% link_new modelli settimanali | features/administration/work-time-pattern-models.md | #create-week-time-patterns %}.


## Tipi di modelli di orario

Esistono tre tipi diversi di modelli di orario. 

> Nota
> 
> - I modelli di orario del tipo Turno fisso sono anche chiamati modelli di orario fissi.<br> 
> - I modelli di orario del tipo Turno variabile sono anche chiamati modelli di orario variabili.


| Tipo                | Descrizione                                                                                                                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Turno fisso         | I turni che utilizzano un modello di orario fisso hanno un’ora di inizio e un’ora di fine prestabilite, che non possono essere spostate. Da un modello di orario fisso si può ottenere un unico turno. I modelli di orario fissi vengono generalmente aggiunti alle {% link_new rotazioni | features/administration/shift-sequences.md %}.                                      |
| Turno variabile      | I turni con un modello di orario variabile hanno un’ora di inizio flessibile all’interno di un intervallo di tempo definito. Questo significa che diversi turni sono possibili. I modelli di orario variabili che vengono aggiunti alle rotazioni diventeranno automaticamente dei modelli di orario fissi perché sono impostati sulla prima finestra di inizio possibile di un turno. |
| Margine di disponibilità | Questo modello di orario è utilizzato per definire un intervallo di tempo che è più breve dell’orario di apertura dell’unità di pianificazione. Quando inserisci rotazioni che contengono modelli di orario di questo tipo, injixo selezionerà i modelli di orario che sono compatibili con questo margine di disponibilità durante l’ottimizzazione e l’offerta dei turni. Puoi utilizzare questo tipo anche per configurare contemporaneamente le disponibilità di diversi dipendenti.          |

## Quale modello di orario utilizzare per la pianificazione?

Non esiste uno scenario unico che stabilisca quando utilizzare un determinato tipo di modello di orario, ma l'elenco seguente fornisce alcune indicazioni generali:

- Turno fisso: Utilizza i modelli di orario fissi per pianificare i dipendenti che hanno orari di lavoro fissi. I loro turni iniziano e finiscono sempre a un'ora ben definita, e non possono essere spostati all'interno della pianificazione.
Puoi utilizzare i modelli di orario fissi nei modelli di pianificazione per {% link_new creare pianificazioni ottimizzate | features/scheduling/scheduling-optimization.md %}, per definire schemi settimanali che si ripetono all’interno di {% link_new rotazioni | features/scheduling/capacity/capacity-insert-shift-sequences.md %}, oppure nell’{% link_new offerta dei turni | features/scheduling/schedules/schedules-shift-bidding.md %}.
- Turno variabile: Utilizza i modelli di orario variabili per pianificare i dipendenti che hanno orari di lavoro flessibili. injixo può pianificare un dipendente per turni diversi con un unico modello di orario di questo tipo. Questo modello di orario viene utilizzato generalmente durante la {% link_new creazione di pianificazioni ottimizzate | features/scheduling/scheduling-optimization.md %} o nell'{% link_new offerta dei turni | features/scheduling/schedules/schedules-shift-bidding.md %}.
- Margine di disponibilità: Se la tua unità di pianificazione ha un orario di apertura che oltrepassa una giornata lavorativa, puoi limitare le opzioni di pianificazione dei dipendenti in injixo. Per limitare le disponibilità di diversi dipendenti contemporaneamente, utilizza i modelli di orario del tipo Margine di disponibilità e aggiungili alle rotazioni. In alternativa, puoi {% link_new configurare le disponibilità per i singoli dipendenti | features/administration/availabilities.md %} nelle impostazioni del dipendente. Entrambe le opzioni sono tenute in conto durante l'ottimizzazione della pianificazione se la regola di pianificazione 2611 è attiva.

In alternativa alle disponibilità, puoi utilizzare le {% link_new rotazioni | features/administration/shift-sequences.md %} o i modelli settimanali all'interno dei {% link_new modelli di pianificazione | features/administration/work-time-pattern-models.md | #create-week-time-patterns %}. È possibile anche utilizzare entrambe le opzioni, per esempio per far ruotare i turni diurni e notturni.

Consigliamo di creare un numero limitato di modelli di orario variabili (in combinazione con le {% link_new disponibilità dei dipendenti | features/administration/availabilities.md | #create-employee-availabilities %}), piuttosto che creare una grande quantità di modelli di orario fissi.

## Attività di base e durata del turno

Per ogni modello di orario fisso o variabile dovrai impostare un'attività che definisce la durata totale del turno. In entrambi i tipi di modello di orario, è possibile aggiungere altre attività che si sovrappongono all'attività di base. La durata delle altre attività non deve superare la durata dell'attività di base.

L'attività di base copre l'intera durata della presenza di un dipendente durante un turno, comprese le pause ed eventuali altre attività non retribuite. È la prima attività che selezioni quando crei un nuovo modello di orario, e non è possibile eliminarla o modificarla dopo aver salvato il modello di orario.

La durata totale di un turno pianificato, comprese le pause, è la durata lorda del turno. Sottraendo dalla durata lorda le attività non retribuite, come le pause non retribuite o il tempo di preparazione, si ottiene la durata netta del turno. La durata netta del turno è visibile in Schedules e nel Centro dei turni con l'etichetta Ore effettive. Tieni in considerazione che anche i contratti specificano la durata netta.

La durata di un modello di orario deve rispettare le ore lavorative stabilite dai {% link_new contratti | features/administration/create-contracts.md %}.
Per esempio, un contratto di 40 ore settimanali distribuite su 5 giorni richiede un modello di orario con una durata netta di 8 ore al giorno. Un contratto di 37,5 ore settimanali richiede un modello di orario con 7,5 ore giornaliere.

Utilizza l'attività Presente come attività di base, e assicurati che sia configurata come Sostituibile. In questo modo, le funzionalità Ottimizzazione delle mansioni e Crea una pianificazione ottimizzata possono sostituire l'attività Presente con altre attività, purché queste abbiano un {% link_new fabbisogno di personale calcolato | features/forecast/injixo-forecast/staff-requirement.md %} e siano configurate come pianificabili.

### Elementi fissi e corridoi

Puoi creare un elemento di corridoio aggiungendo un'attività di durata inferiore rispetto all'intervallo tra l'ora di inizio e l'ora di fine dell'elemento. Gli elementi di corridoio si sovrappongono a tutti gli elementi fissi di un turno. Durante la pianificazione ottimizzata, injixo sposterà gli elementi di corridoio per ottimizzare la copertura. I corridoi in quanto tali possono sovrapporsi, ma le attività all'interno di due corridoi non possono sovrapporsi.

Quando inserisci manualmente un modello di orario in una pianificazione, gli elementi di corridoio vengono posizionati nella prima fascia oraria possibile del corridoio. Puoi spostare manualmente i corridoi nell'ambito degli intervalli definiti.

Quando la durata di un elemento di corridoio corrisponde esattamente all'ora di inizio e di fine dell'elemento, viene creato un elemento fisso.

