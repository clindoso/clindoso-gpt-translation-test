---
title: Utilizzare le qualifiche
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Scopri come le qualifiche di injixo rispecchiano le competenze dei dipendenti. Crea, modifica ed elimina qualifiche e livelli di qualifica.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/configure-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
redirect_from:
  - /it/skills/
redirect_reason: Updated filename on 24 July 2023
---

Le qualifiche assicurano che i dipendenti svolgano soltanto le attività per le quali hanno le competenze necessarie. Le qualifiche associano le competenze dei dipendenti (per esempio la conoscenza del prodotto, le lingue conosciute, i canali di comunicazione, etc.) alle attività che i dipendenti possono svolgere, e che possono essere pianificate in injixo.

Per configurare le qualifiche, vai su _Plan > Configurazione > Qualifiche_{:.breadcrumbs}.

## Creare una qualifica

Crea almeno una qualifica per ogni attività che richiede una competenza specifica. Quando crei una qualifica, injixo imposta un livello di qualifica predefinito del 100%. I livelli di qualifica indicano quanto devono essere esperti i dipendenti per poter svolgere una certa attività, per esempio 100% di competenza in inglese, ma solo 50% di competenza in spagnolo. Per ogni qualifica puoi creare diversi livelli di qualifica. 

> Non è necessario creare qualifiche per le attività che non richiedono competenze specifiche.

1. Clicca su _Nuova qualifica_{:.doc-button}.
2. Inserisci un **nome**.
   L'abbreviazione viene generata automaticamente, ma puoi modificarla.
3. (Facoltativo) Clicca su _Aggiungi livello di qualifica_{:.doc-button} per modificare il **punteggio** predefinito di un livello di qualifica, o per aggiungere altri livelli di qualifica, se ci sono dipendenti che sono meno esperti in quell’attività. Vedi anche: [Calcolare l’idoneità utilizzando il punteggio e la ponderazione](#calcolare-lidoneità-utilizzando-il-punteggio-e-la-ponderazione).
4. Clicca su _Crea qualifica_{:.doc-button}.  

 In seguito, puoi [assegnare un livello di qualifica a un dipendente](#assegnare-i-livelli-di-qualifica-a-un-dipendente) e [assegnare la qualifica a un’attività](#assegnare-le-qualifiche-alle-attività).

## Duplicare una qualifica

Per creare una nuova qualifica con gli stessi livelli di qualifica di una qualifica già esistente, segui questi passaggi:

1. Nell’elenco delle **qualifiche**, clicca sulla qualifica che vuoi duplicare.
2. Clicca su **Duplica qualifica** sotto il nome della qualifica.  
   Si aprirà la finestra **Crea nuova qualifica** con i livelli di qualifica precompilati.
3. Inserisci un **nome** per la nuova qualifica.
4. (Facoltativo) Modifica i livelli di qualifica.
5. Clicca su _Crea qualifica_{:.doc-button}.

## Modificare una qualifica e i livelli di qualifica

1. Seleziona una qualifica dall’elenco.
2. Modifica la qualifica o i livelli di qualifica.
   Per eliminare un livello di qualifica, clicca sull’{% icon trash %} corrispondente.
3. Clicca su _Salva modifiche_{:.doc-button}.

## Eliminare una qualifica

1. Seleziona una qualifica dall’elenco.
2. Clicca su _Elimina qualifica_{:.doc-button} e conferma.

## Assegnare le qualifiche alle attività

1. Vai su _Plan > Configurazione > Attività_{:.breadcrumbs}.
2. Seleziona un'attività dalla lista e scorri fino alla sezione **Qualifiche**.
3. Seleziona una qualifica dal menu a tendina.
4. (Facoltativo) Modifica la **Ponderazione**. Se aggiungi soltanto una qualifica, mantieni il valore prestabilito del 100%.  
   Per le attività che richiedono più di una qualifica, puoi [utilizzare la ponderazione](#calcolare-lidoneità-utilizzando-il-punteggio-e-la-ponderazione) per determinare quale qualifica è più importante.
7. Clicca su _Salva modifiche_{:.doc-button}.

## Assegnare i livelli di qualifica a un dipendente

1. Vai su _Plan > Configurazione > Dipendenti_{:.breadcrumbs}.
2. Seleziona un dipendente dall’elenco e vai alla sezione **Livelli di qualifica**.
3. Clicca sull’{% icon item-add %} e seleziona uno o più livelli di qualifica dall’elenco.
   Per selezionare più voci, clicca con il mouse mentre tieni premuto il tasto **Shift** oppure **CTRL**.
4. (Facoltativo) Aggiungi un {% link_new periodo di validità | features/administration/set-a-validity-period.md %} per il livello di qualifica, impostando le date nei campi **Validità dal** e **fino al**.
   Non puoi assegnare a un dipendente diversi livelli di una stessa qualifica per uno stesso periodo di validità.
 5. Clicca su _OK_{:.doc-button}.  
   Le attività che richiedono la qualifica assegnata saranno visibili nella sezione **Attività** per quel dipendente.

Un’attività può richiedere una o più qualifiche. Per svolgere un'attività che richiede diverse qualifiche, i dipendenti devono possederle tutte.

Suggerimento: per assegnare una qualifica a diversi dipendenti contemporaneamente, puoi utilizzare la {% link_new funzionalità di modifica in blocco | features/administration/employee-overview.md | #utilizzare-la-modifica-in-blocco %}. 

## Calcolare l’idoneità utilizzando il punteggio e la ponderazione

injixo è in grado di calcolare un valore di idoneità che si basa sui seguenti elementi:

- il punteggio del livello di qualifica di un dipendente;
- il valore della ponderazione, nel caso di attività che richiedono più di una qualifica.

Esempio: l’attività Chiamate in spagnolo richiede due qualifiche: Spagnolo e Chiamate. La qualifica Spagnolo ha un’importanza doppia rispetto alla qualifica Chiamate. Il valore di ponderazione è 100 per Spagnolo è 50 per Chiamate.

- Il dipendente A ha un livello di qualifica 50% per Spagnolo e 100% per Chiamate.
- Il dipendente B ha un livello di qualifica 100% per Spagnolo e 50% per Chiamate.

Questo significa che il dipendente A ha un valore di idoneità del 66,66% e il dipendente B ha un valore di idoneità dell’83,33%.

Il valore di idoneità viene calcolato con questa formula: `(Somma(Ponderazione di ogni qualifica * livello di qualifica del dipendente per questa qualifica) / (Somma delle ponderazioni di tutte le qualifiche)`

Se un’attività richiede solo una qualifica, il valore di idoneità di un dipendente corrisponde al suo livello di qualifica.

Se vuoi che durante la {% link_new pianificazione ottimizzata | features/scheduling/schedules/schedules-optimized-schedules.md %} injixo tenga conto del valore di idoneità, anziché del numero totale dei dipendenti, configura l’impostazione _48069_{:.id-label} _Osservare la percentuale dell'idoneità per le attività_. Nel {% link_new Centro dei turni | features/scheduling/shiftcenter/analyze-coverage-staffing-requirement.md %} e in {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %}, la copertura e l’occupazione non possono essere mostrate in funzione dell’idoneità dei dipendenti. In questi casi, la copertura e l’occupazione sono sempre mostrate come 100% per indicare il numero totale dei dipendenti.
