---
title: Che cosa sono i periodi di pianificazione?
description: Scopri a che cosa servono i periodi di pianificazione e come visualizzarli, modificarli ed eliminarli (in Schedules).
product_label:
  - essential
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Permettere ai dipendenti di vedere le loro pianificazioni
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md
  - overwrite_title: Permettere ai dipendenti di scambiarsi i turni
    filepath: features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md
  - overwrite_title: Offerta dei turni
    filepath: features/scheduling/schedules/schedules-shift-bidding.md
  - overwrite_title: Periodi di permesso
    filepath: features/scheduling/time-off/time-off-periods.md
---

I periodi di pianificazione sono periodi di alcuni giorni, settimane o mesi. Utilizzali per:

- permettere ai dipendenti di {% link_new vedere le loro pianificazioni | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %};
- permettere ai dipendenti di {% link_new scambiarsi i turni | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %};
- aprire {% link_new l’offerta dei turni | features/scheduling/schedules/schedules-shift-bidding.md %} ai dipendenti.

Per permettere ai dipendenti di richiedere permessi, utilizza i {% link_new periodi di permesso | features/scheduling/time-off/time-off-periods.md %}.

## Stato

Ogni periodo di pianificazione ha uno stato. Lo stato permette o limita alcune opzioni per i dipendenti durante il periodo di pianificazione. Generalmente, lo stato di un periodo di pianificazione viene modificato diverse volte durante il processo di pianificazione, per esempio dopo che una pianificazione è stata finalizzata, oppure al termine del periodo utile per inoltrare le richieste di turni.

| Stato                | Descrizione                                                                                                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Non pubblicato           | I dipendenti non possono visualizzare la pianificazione pubblicata, non possono partecipare all’{% link_new offerta dei turni                                                                                                                 | features/scheduling/schedules/schedules-shift-bidding.md %} e non possono scambiarsi i turni. Utilizza questo stato se per il momento non vuoi comunicare la pianificazione ai dipendenti. |
| Offerta dei turni attivata | I dipendenti possono vedere la pianificazione pubblicata, partecipare all’offerta dei turni e scambiarsi i turni. Questo stato non può essere impostato se il periodo di pianificazione ha una scadenza che è già stata superata. |
| Pubblicato             | I dipendenti possono vedere la pianificazione pubblicata e scambiarsi i turni. Non possono partecipare all’offerta dei turni.                                                                                      |
| Finito              | Questo stato indica che la pianificazione è definitiva. I dipendenti possono ancora scambiarsi i turni.                                                                                                           |

## Visualizzare i periodi di pianificazione

1. Vai su _Plan > Schedules_{:.breadcrumbs}.
2. Clicca su _Periodi di pianificazione_{:.doc-button}.
3. Seleziona una **unità di pianificazione** dal primo menu a tendina. Per filtrare la tabella, comincia a digitare il nome dell'unità che cerchi.
4. (Facoltativo) Per filtrare i periodi di pianificazione, scegli una **Selezione** dal secondo menu a tendina. Per filtrare la tabella, comincia a digitare il nome del periodo che cerchi.  
   Se esistono dei periodi di pianificazione per l’unità di pianificazione (e per la selezione) che hai scelto, verranno visualizzati. Continua a leggere per saperne di più sulle schede e sulle colonne della tabella.

### Schede In corso e Scaduto

Tutti i periodi di pianificazione dell’unità di pianificazione e del gruppo di selezione scelti verranno visualizzati nelle schede seguenti:

- **In corso**: i periodi di pianificazione in corso e i periodi di pianificazione futuri;
- **Scaduto**: i periodi di pianificazione passati.

Le due schede saranno vuote se non hai ancora creato nessun periodo di pianificazione, oppure se i criteri del filtro non corrispondono a nessun periodo di pianificazione.

### Colonne della tabella

La tabella dei periodi di pianificazione comprende sei colonne:

- **Stato**: lo stato del periodo di pianificazione;
- **Selezione**: il gruppo di dipendenti per i quali il periodo di pianificazione è rilevante;
- **Valido da**: la data di inizio del periodo di pianificazione;
- **Valido fino**: la data di fine del periodo di pianificazione;
- **Deadline**: la data entro la quale i dipendenti possono partecipare all’offerta dei turni;
- **Ereditato da**: quando crei un periodo di pianificazione per un’unità di pianificazione di livello superiore, tutte le unità di pianificazione di livello inferiore ereditano il suo stato. La colonna mostra il nome dell’unità di pianificazione di livello superiore, nel caso in cui ce ne sia una.

Per ordinare il contenuto della tabella in base a una colonna, clicca sulla rispettiva **intestazione**. Per invertire l’ordine, clicca di nuovo.

## Creare i periodi di pianificazione

1. Vai su _Plan > Schedules_{:.breadcrumbs}.
2. Clicca su _Periodi di pianificazione_{:.doc-button}.
3. Clicca su _Crea periodo di pianificazione_{:.doc-button} in alto a destra.
4. Seleziona una unità di pianificazione, un intervallo di date, una deadline (facoltativa), e uno [stato](#stato) per il periodo di pianificazione.
5. Per salvare il periodo di pianificazione, clicca su _Salva_{:.doc-button}.

## Modificare i periodi di pianificazione

Per aggiornare lo stato di un periodo di pianificazione, seleziona un nuovo stato dal menu a tendina nella colonna **Stato**. Il nuovo stato viene salvato automaticamente.

Per modificare tutte le impostazioni di un periodo di pianificazione (incluso lo stato), passaci sopra con il mouse e clicca sull’{% icon pencil %} a destra.

## Eliminare i periodi di pianificazione

Spunta le **caselle** a sinistra del periodo o dei periodi che vuoi eliminare. Spunta la casella in alto per selezionare tutte le voci della tabella. Clicca su _Elimina selezionato_{:.doc-button}sotto la tabella.
