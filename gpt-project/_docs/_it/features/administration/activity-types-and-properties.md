---
title: Tipi e proprietà delle attività
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Scopri i diversi tipi di attività e le opzioni di configurazione di ogni attività.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/how-to-schedule-multiskill-agents.md
redirect_from:
  - /it/activity-properties/
redirect_reason: Updated filename on 11 October 2023
---

Durante {% link_new la creazione e la modifica delle attività | features/administration/activities.md %}, le varie opzioni di configurazione influiscono sul modo in cui le attività vengono utilizzate e visualizzate nelle pianificazioni e nei report.

## Tipi di attività

Il tipo di attività influisce sulla tua pianificazione e determina:
- il modo in cui la pianificazione ottimizzata tratta l’attività;
- dove l’attività può essere utilizzata;
- il modo in cui l’attività viene visualizzata in Schedules e nel Centro dei turni;
- se l’attività viene inclusa nei report oppure no. <!-- illness, absences, vacation -->

La tabella seguente comprende informazioni più dettagliate su ogni tipo di attività:

| Tipo     | Descrizione                                                                                                                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Presenza | Tutte le attività in cui sono impegnati i dipendenti.<br>Le attività del tipo Presenza vengono pianificate da injixo in base al fabbisogno di personale.                                    |
| Pausa    | Pause, retribuite o non retribuite, durante un turno.<br>Solo le attività del tipo Pausa possono essere configurate nei modelli di orario come attività di pausa. Puoi utilizzare la funzionalità {% link_new ottimizzazione delle pause | features/scheduling/schedules/break-optimization.md %} per distribuire le pause all’interno delle pianificazioni in modo da ottenere la copertura ottimale per le attività con fabbisogno di personale. |
| Malattia  | Assenze, retribuite o non retribuite, come i permessi per malattia o le visite mediche.<br>Solo le attività del tipo Malattia vengono incluse nei report sui congedi per malattia.                             |
| Ferie | Permessi retribuiti o non retribuiti, chiusure aziendali, etc.<br> Solo le attività del tipo Ferie vengono incluse nei report sulle ferie.                                                 |
| Assenza  | Assenze di altri tipi che influiscono sulla pianificazione, come, per esempio, formazione fuori sede, permessi banca ore, etc.<br>I report sulle assenze includono solo le attività del tipo Assenza.              |
| Meeting  | Tipo di attività per {% link_new pianificare le riunioni | features/scheduling/meetings/meetings-overview.md %}. |

## Proprietà delle attività

Le proprietà delle attività influiscono sulla pianificazione e sull’utilizzo dell’attività.
Puoi impostare le proprietà delle attività con le caselle seguenti:

| Proprietà                                    | Effetto                 |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Retribuita                                        | Attiva il calcolo delle ore lavorate per le attività pianificate. Se le pause o le assenze sono retribuite, vengono calcolate come ore lavorative. Se non sono retribuite, non vengono incluse nel calcolo delle ore lavorate nette.                                                                                                                                       |
| Rispettare ore di riposo                     | Impedisce la violazione delle ore di riposo previste dal contratto. injixo verifica le ore di riposo soltanto se la regola di pianificazione _2601_{:.id-label} è attiva.   |
| Pianificabile                                   | Consente a injixo di pianificare l’attività se utilizzi la funzionalità Crea una pianificazione ottimizzata, o di ottimizzarla durante l’ottimizzazione delle mansioni. Consigliamo di usare questa proprietà per le attività che hanno un fabbisogno di personale. Generalmente non è utilizzata per le attività del tipo Assenza, Ferie e Malattia.                                                                               |
| Richiedibile in Me                           | Consente ai dipendenti di richiedere permessi (assenze, ferie, e malattie) in injixo Me (se c’è un {% link_new Periodo di permesso  | features/scheduling/time-off/time-off-periods.md %} con stato Pubblicato). Nell’offerta dei turni, i turni con attività del tipo Presenza e Pausa possono essere richiesti automaticamente. |
| Scambiabile con scambio turni              | Consente ai dipendenti {% link_new di scambiarsi l’attività | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %} in injixo Me. Per poterlo fare, tutte le attività (pause incluse) comprese nei modelli di orario devono essere configurate come **Scambiabile con scambio turni**.                                                                                                                          |
| Permettere la sovracopertura se il fabbisogno per il turno è pari a zero | Consente a injixo di pianificare l’attività anche durante i periodi che non hanno un fabbisogno di personale. Per impostazione predefinita, gli intervalli con fabbisogno pari a zero non vengono coperti.                                                                                                                                                                                                                |
| Sostituibile                               | Consente a injixo di sostituire l’attività con attività pianificabili che hanno un fabbisogno di personale. Questa opzione è necessaria per {% link_new pianificare riunioni | features/scheduling/meetings/meetings-overview.md %} durante quest’attività.                                                                                                               |
| Attività di un giorno intero                | Consente di pianificare l’attività per un’intera giornata (in Schedules o nella scheda Attività di giorno intero nel Centro dei turni). Se l’attività è configurata come Retribuita, al dipendente viene accreditato l’ammontare giornaliero in base al contratto.<br>Necessaria per consentire ai dipendenti di richiedere l’attività come attività di un giorno intero in injixo Me.   |
| Stato giornaliero                                | Disponibile solo per le attività di un giorno intero. Lo stato giornaliero permette di pianificare manualmente l’attività nel Centro dei turni come stato giornaliero nella scheda Attività di un giorno intero. La pianificazione sostituita viene salvata, e può essere consultata in seguito. Di conseguenza, injixo esclude dal calcolo della copertura i dipendenti pianificati per le attività con questa proprietà, ma la voce della pianificazione originale resta visibile. |
| Trattamento speciale nella pianificazione ottimizzata | Disponibile soltanto per le attività del tipo Presenza. Le attività con questa proprietà possono essere pianificate solo esattamente come sono configurate. Non possono essere sostituite e non hanno una durata flessibile.<br>Per saperne di più, vai alla [sezione seguente](#trattamento-speciale-nella-pianificazione-ottimizzata). |

## Trattamento speciale nella pianificazione ottimizzata

Questa proprietà permette alla funzionalità Crea una pianificazione ottimizzata di pianificare l’attività esclusivamente secondo la sua configurazione. Questa proprietà viene utilizzata generalmente per pianificare gli straordinari o le attività di back-office.<br>
Può essere utilizzata in due modi diversi:

Opzione 1: l’attività fa parte di un modello di orario. In questo caso, l’attività può essere pianificata soltanto per la durata configurata e all’interno del periodo definito dal modello di orario. L’attività non può essere utilizzata per sostituire altre attività sostituibili. Il modo in cui l’attività viene trattata durante la pianificazione ottimizzata dipende anche dalla sua {% link_new configurazione all’interno del modello di orario | features/administration/daymodels/daymodel-creation.md | #aggiungere-unattività-del-tipo-presenza-o-assenza %}:
- Attività configurata come elemento fisso: durante l’ottimizzazione della pianificazione, l’attività verrà pianificata per la durata esatta per cui è stata configurata.
- Attività configurata come elemento di corridoio: durante l’ottimizzazione della pianificazione, l’attività potrà essere spostata all’interno del corridoio definito per ottimizzare la copertura di altre attività.

Esempio:

- Aggiungi un’attività di back office senza fabbisogno di personale e con la durata di un’ora al tuo modello di orario. Durante la pianificazione ottimizzata, l’attività verrà pianificata esattamente per un’ora. Se nel modello di orario è configurata come elemento di corridoio, l’attività verrà spostata all’interno del corridoio, nella fascia oraria che avrà l’impatto minore sulla copertura delle altre attività.

Opzione 2: l’attività non fa parte di un modello di orario. In questo caso, la funzionalità Crea una pianificazione ottimizzata non pianificherà automaticamente l’attività, e non potrà usarla per sostituire delle attività sostituibili. L’attività potrà essere pianificata soltanto manualmente.

Esempio:

- Crea un’attività per lo straordinario che non fa parte di un modello di orario. La funzionalità Crea una pianificazione ottimizzata non pianificherà l’attività e non la utilizzerà per sostituire delle attività sostituibili. Aggiungi manualmente l’attività alla pianificazione se è necessario. Così facendo, puoi controllare quando l’attività viene pianificata e per quanto tempo, e a quali dipendenti viene assegnata.

> Nota
>
> Questa proprietà è disponibile solo dopo aver creato l’attività.

## Subattività

È possibile assegnare delle attività ad altre attività. L’attività alla quale vengono assegnate altre attività diventa una multiattività. Le attività assegnate diventano le subattività della multiattività. Le multiattività permettono di pianificare dipendenti che hanno più di una qualifica quando una delle loro qualifiche è richiesta. Nell’elenco delle attività, le multiattività sono contrassegnate da un’icona con la lettera M: <em class="multiactivity-icon"></em>.

Per far sì che la funzionalità Crea una pianificazione ottimizzata possa pianificare le multiattività, porta a termine le azioni seguenti:

- seleziona il tipo Presenza per le multiattività e tutte le subattività;
- configura sia le multiattività che le subattività come retribuite e pianificabili;
- assegna tutte le subattività (e, in un secondo tempo, la multiattività) alla tua unità di pianificazione;
- per controllare quali dipendenti possono essere pianificati, assegna a ogni subattività una qualifica diversa;
- (facoltativo) assegna una qualifica alla multiattività. In questo caso, i dipendenti dovranno avere questa qualifica aggiuntiva per poter svolgere la multiattività. Per impostazione predefinita, la multiattività di per sé non richiede nessuna qualifica.

> Nota
>
> Se non utilizzi la funzionalità Crea una pianificazione ottimizzata, ma avvii solo l’ottimizzazione delle mansioni, injixo può sostituire le attività sostituibili con le multiattività soltanto se un dipendente può svolgere almeno una delle subattività assegnate alla multiattività.
