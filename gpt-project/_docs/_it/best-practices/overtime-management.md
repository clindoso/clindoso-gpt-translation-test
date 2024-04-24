---
title: Gestire gli straordinari
product_label:
  - advanced
  - enterprise
  - classic
description: Scopri la migliore configurazione delle attività per pianificare il lavoro straordinario e documentarlo in modo trasparente.
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/importance-for-activities.md
---

In certi casi i dipendenti devono fare degli straordinari per poter mantenere un livello di servizio ragionevole. Gli straordinari si rendono necessari nel caso di carichi di lavoro inaspettatamente elevati o di carenze di personale causate da un alto tasso di assenze per malattia o ferie.  
In molti casi i contratti dei dipendenti stabiliscono una retribuzione maggiore per le ore di straordinario o la possibilità di compensare le ore di straordinario con giorni di ferie aggiuntivi. Quando i dipendenti fanno gli straordinari, è importante rispettare anche altre condizioni contrattuali, come il riposo tra un turno e l'altro. Se sei un fornitore di servizi, potresti essere tenuto a informare i clienti su ogni tipo di lavoro aggiuntivo pianificato.

In questo articolo trovi dei consigli sulla configurazione delle attività e delle multiattività per poter pianificare facilmente gli straordinari e visualizzarli correttamente nella fascia delle attività e nei report.

Gli straordinari dovrebbero essere pianificati manualmente nel Centro dei turni o in Schedules, in aggiunta alla pianificazione esistente.

## Creare le attività per gli straordinari

L’esempio di seguito utilizza una nuova attività dal nome Chiamate. Segui questi passaggi per tutte le attività che desideri pianificare come ore di straordinario, per esempio per Chiamate o Email, ma non per Malattia o Vacanza.

1. {% link_new Crea e configura l'attività | features/administration/activities.md %} **Chiamate**.
2. Duplica l’attività **Chiamate** e assegna alla nuova attività il nome **Chiamate - straordinari**. Non è necessario aggiungere qualifiche a questa attività.  
  - Spunta la casella **Trattamento speciale nella pianificazione ottimizzata**.
  - Assicurati che la casella **Richiedibile in Me** non sia selezionata.
3. Nell’attività **Chiamate - straordinari**, aggiungi **Chiamate** come subattività.  
  **Chiamate - straordinari** adesso è una multiattività.
4. Aggiungi entrambe le attività all’unità di pianificazione interessata. Non aggiungere l’attività di straordinario a nessun modello di orario.

Con questa configurazione, l’attività Chiamate - straordinari può essere pianificata solo manualmente, e non può essere sostituita durante l’ottimizzazione della pianificazione. I dipendenti non potranno richiedere quest’attività in injixo Me.

Aver inserito “- straordinari” nel nome della multiattività permette a te e ai dipendenti di vedere nella loro pianificazione quando stanno facendo degli straordinari, per quanto tempo e per quali compiti.

## Pianificare gli straordinari

È possibile pianificare manualmente gli straordinari in _Plan > Centro dei turni_{:.breadcrumbs} oppure in _Plan > Schedules_{:.breadcrumbs}.

Per aggiungere attività di straordinario nel Centro dei turni, segui questi passaggi:

1. Scegli l’unità di pianificazione e il gruppo di selezione (facoltativo) a cui appartiene il dipendente per cui vuoi pianificare del lavoro straordinario.
2. Clicca due volte sulla cella del dipendente corrispondente al giorno in cui dovrebbe fare gli straordinari. Clicca sulla scheda **Multiattività** e seleziona **Chiamate - straordinari**.
3. Imposta l’ora di inizio e l’ora di fine dell’attività.
4. Clicca su _OK_{:.doc-button}.

Gli straordinari pianificati sono immediatamente visibili nella finestra Pianificazione e nella scheda Attività nella {% link_new finestra dei parametri | features/scheduling/shiftcenter/shift-center-overview.md | #parameter-window %}. Se configuri la scheda Attività in modo da mostrare la copertura, la fascia delle attività in fondo alla schermata verrà aggiornata e rifletterà gli straordinari pianificati.

Per aggiungere attività di straordinario in _Plan > Schedules_{:.breadcrumbs}, segui questi passaggi:

1. Clicca due volte su una cella nella pianificazione per aprire la schermata di modifica.
2. Clicca su _Aggiungi una nuova attività_{:.doc-button}.  
  A destra viene aggiunta una nuova riga con l’attività.
3. Nella nuova riga, seleziona **Chiamate - straordinari** dal menu a tendina.
4. Imposta l’ora di inizio e l’ora di fine dell’attività.
5. Clicca su _Salva_{:.doc-button}.

## Report

Il report **Attività in ore...** rispecchierà gli straordinari del dipendente, dal momento che il nome dell’attività include tale informazione. In questo modo, tutte le ore di straordinario lavorate sono documentate e possono essere verificate dalle persone interessate, per esempio dal dipartimento contabilità che deve gestire la retribuzione straordinaria.
