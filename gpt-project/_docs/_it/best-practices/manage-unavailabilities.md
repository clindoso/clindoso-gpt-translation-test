---
title: Gestire le indisponibilità dei dipendenti
description: Scopri come utilizzare un’attività del tipo Assenza per permettere ai dipendenti di definire le loro indisponibilità.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: true
---

Crea un’attività richiedibile del tipo Assenza per permettere ai dipendenti di definire i periodi durante i quali non sono disponibili a lavorare.

Gestisci le indisponibilità dei dipendenti con le richieste di permesso per raggiungere i seguenti obiettivi:

- definire i periodi durante i quali i dipendenti possono aggiungere le loro indisponibilità;
- impostare una scadenza per le richieste di indisponibilità, e approvarle o rifiutarle;
- monitorare lo storico delle richieste dei dipendenti e verificare che i loro contratti siano compatibili con le loro esigenze di permessi;
- permettere ai dipendenti di impostare un numero illimitato di indisponibilità;
- permettere ai dipendenti di impostare indisponibilità per giorni parziali.

Questo articolo presenta una panoramica del procedimento. Puoi utilizzarlo per tenere traccia dei passaggi necessari.

## 1. Creare l’attività Non disponibile

1. In _Plan > Configuration_{:.breadcrumbs} crea una {% link_new nuova attività | features/administration/activities.md | #creare-unattività %}.
2. Configura l’attività come di seguito:
   - **Nome**: inserisci Non disponibile. Un’abbreviazione viene generata automaticamente.
   - **Tipo**: seleziona **Assenza**.
   - Spunta la casella **Richiedibile in Me**.
   - (Facoltativo) Spunta la casella **Attività di un giorno intero**.
3. Clicca su _Crea attività_{:.doc-button}.

## 2. Creare un periodo di permesso

1. In _Plan > Ferie/Assenze_{:.breadcrumbs}, crea un {% link_new periodo di permesso | features/scheduling/time-off/time-off-periods.md | #create-a-time-off-period %}.
2. Inserisci le informazioni generali per il periodo di permesso:
   - **Unità di pianificazione**.
   - (Facoltativo) **Selezione**.
   - **Attività**: seleziona **Non disponibile**.
   - Facoltativo: **Deadline**.
   - **Stato**: seleziona **Pubblicato**.
3. Clicca su _Crea periodo di permesso_{:.doc-button}.

## 3. I dipendenti inviano le loro richieste

In _Me > Permessi_{:.breadcrumbs} i dipendenti possono {% link_new inviare richieste | features/injixo-me/use-injixo-me/explore-injixo-me.md | #chiedere-un-permesso %} per l’attività Non disponibile.

## 4. Approvare o rifiutare le richieste

In _Plan > Ferie/Assenze_{:.breadcrumbs}, {% link_new approva o rifiuta le richiesta di permesso | features/scheduling/time-off/vacation-absences-management.md %} per l’attività Non disponibile.<br>
Dopo che avrai approvato la richiesta di un dipendente, la finestra della pianificazione nel Centro dei turni mostra una cella rossa con l’abbreviazione dell’attività Indisponibile nella fascia di tempo della richiesta approvata. Se utilizzi la funzionalità **Crea una pianificazione ottimizzata** o **Ottimizzazione delle mansioni**, injixo non pianifica il dipendente durante la fascia di tempo occupata.

## Monitorare le richieste

In _Plan > Centro dei turni_{:.breadcrumbs} puoi vedere i dettagli delle richieste di permesso per l’attività Non disponibile che sono state approvate.

1. Clicca sulla scheda **Attività - Fabbisogno** sotto la tabella. In alto, seleziona un intervallo di date dal selettore di data e clicca su _Applica_{:.doc-button}.
2. Espandi l’unità di pianificazione che ti interessa nella tabella in alto.
3. Fai doppio clic su una casella rossa etichettata come Non disponibile.  
4. Clicca sulla scheda **Andamento storico**.  
    Vedrai i dettagli dell’approvazione della richiesta di permesso:
    - Data/Ora: la data e l’ora dell’approvazione.
    - Operazione: l’azione eseguita. In questo caso, Autorizza richiesta.
    - Utente: il dipendente che ha approvato la richiesta.
5. Clicca su _OK_{:.doc-button}.
  
Vai su _Plan > Ferie/Assenze_{:.breadcrumbs} per {% link_new vedere le richieste approvate, in sospeso e rifiutate | features/scheduling/time-off/vacation-absences-management.md | #view-requests %}.
