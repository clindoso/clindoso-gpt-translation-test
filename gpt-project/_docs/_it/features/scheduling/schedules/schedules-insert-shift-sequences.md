---
title: Inserire le rotazioni
product_label:
  - essential
  - advanced
  - enterprise
description: In Schedules, utilizza le rotazioni per inserire ripetizioni di turni, attività o disponibilità.
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
---

Le rotazioni sono sequenze ripetute di turni, attività o disponibilità. Puoi inserire rotazioni per i dipendenti selezionati, per esempio per pianificare attività o disponibilità ricorrenti.

## Prerequisiti

Prima di poter inserire le rotazioni nella pianificazione, devi completare le azioni seguenti:

- {% link_new Creare | features/administration/shift-sequences.md %} almeno una rotazione.
- {% link_new Assegnare | features/administration/employee-overview.md | #assegnare-una-rotazione %} la rotazione o le rotazioni a un dipendente.

## Filtrare le rotazioni

1. Vai su _Plan > Schedules_{:.breadcrumbs}.
2. Dal menu a tendina **Azioni di pianificazione** a destra seleziona _Inserire le rotazioni_{:.doc-button}.
3. Seleziona un’unità di pianificazione.
4. (Facoltativo) Scegli una selezione.
5. Imposta un periodo di tempo.

   > Puoi inserire rotazioni per un massimo di due anni.


   La sezione **Riepilogo** mostra le rotazioni che corrispondono ai tuoi criteri di ricerca. La tabella mostra i dati che sono impostati quando assegni una rotazione esistente a un dipendente:

   | Opzione                 | Descrizione                                                                                                                                                                                                                                                                       |
   | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
   | Numero di matricola       | Numero che identifica il dipendente in modo univoco.                                                                                                                                                                                                                                               |
   | Nome                   | Il nome del dipendente a cui la rotazione è assegnata.                                                                                                                                                                                                                                                                 |
   | Rotazione         | Il nome della rotazione assegnata.                                                                                                                                                                                                                                                    |
   | Ordine di inserimento               | Definisce l’ordine in cui le rotazioni sono inserite se un dipendente ha più rotazioni. Le rotazioni con i valori più bassi vengono inserite per prime, e potrebbero essere sovrascritte dalle rotazioni successive.                                                                  |
   | Riga dipendenti           | Definisce quale riga della rotazione è utilizzata per il dipendente.                                                                                                                                                                                                               |
   | Data di riferimento         | Giorno di inizio della rotazione. Se utilizzi una rotazione che dura più di sette giorni per pianificare diversi dipendenti, imposta per ogni dipendente una data di riferimento diversa. In questo modo ai dipendenti verrà assegnata la prima settimana della rotazione in settimane diverse, e non avranno tutti lo stesso turno in contemporanea.
   | Validità dal<br>Fino al | Il periodo per il quale la rotazione è stata assegnata al dipendente. Al di fuori del periodo di validità configurato, la rotazione non sarà inserita nella pianificazione del dipendente. Se il periodo di validità della rotazione rientra completamente nel periodo di tempo selezionato, non verrà visualizzato. |

## Inserire le rotazioni

1. Per selezionare un dipendente, spunta la casella accanto al suo nome. Per selezionare tutti i dipendenti, spunta la casella nella riga di intestazione della tabella.
2. (Facoltativo) Dal menu a tendina **Opzioni** in fondo alla tabella di riepilogo, scegli il modo in cui le pianificazioni esistenti devono essere gestite quando si inseriscono le rotazioni.

   | Opzione                           | Descrizione                                                                                             |
   | -------------------------------- | --------------------------------------------------------------------------------------------------- |
   | Elimina attività di giorni interi       | Le attività di giorno intero sono eliminate. Le altre attività sono mantenute.                              |
   | Elimina margini di disponibilità      | I margini di disponibilità sono eliminati.                                                                   |
   | Elimina tutte le attività e tutti i turni | Tutte le attività e tutti i turni sono eliminati dal livello di destinazione. I margini di disponibilità sono mantenuti. |

   > Le opzioni selezionate sono applicate solo durante l’inserimento della prima rotazione di un dipendente.

3. (Facoltativo) Modifica il livello di destinazione. Per impostazione predefinita è selezionato il livello Piano.
4. Clicca su _Inserire le rotazioni_{:.doc-button}.

> Nota  
>  
> Se una rotazione contiene ancora dei modelli di orario eliminati, questi vengono ancora inseriti nella pianificazione (in Schedules e nel Centro dei turni sono contrassegnati da un bordo tratteggiato).

## Accedere ai report con i risultati

Nella sezione **Cronologia** puoi accedere ai report per i processi di inserimento di rotazioni presenti e passati.  Clicca su **Visualizza dettagli** per scoprire perché non è stato possibile inserire dei turni o delle attività. Un numero con quattro cifre all’inizio della riga indica la regola di pianificazione che blocca l’inserimento della rotazione.

Per eliminare delle voci dalla **Cronologia**, spunta le caselle accanto alla voce o alle voci e clicca su _Elimina voci_{:.doc-button}. Per eliminare tutte le voci contemporaneamente spunta la casella in alto.

## Impedire la sovrascrittura di attività pianificate

Per impostazione predefinita, quando inserisci attività di giorno intero nella pianificazione utilizzando le rotazioni, injixo sovrascrive altre attività di giorno intero nella pianificazione, per esempio i permessi. Per impedire che questo accada, attiva la regola di pianificazione _2645_{:.id-label} _Sostituzione di attività di giorni interi con turni e attività_.

Per impedire che attività del tipo Assenza, Malattia, Ferie o Riunione che non sono attività di giorno intero vengano sovrascritte, attiva la regola di pianificazione _2648_{:.id-label} _Protezione dalla scrittura per le attività nel Centro dei turni_.

> Nota  
>
> Le rotazioni sono inserite con l’account utente attualmente connesso. Le regole di pianificazione possono essere configurate diversamente in base all'utente. Se hai diversi account, verifica di aver fatto il login con l’account corretto.

## Periodi di validità

Quando inserisci delle rotazioni, i periodi di validità potrebbero influire sui risultati.

Per determinare il periodo di tempo durante il quale un modello di orario può essere pianificato, puoi restringere il periodo di validità dei tuoi modelli di orario impostando le date nei campi **Validità dal** e **Fino al**. Dopo aver inserito le rotazioni, potresti vedere il seguente messaggio di errore nel report con i risultati: [2151] Al giorno di registrazione gg/mm/aaaa il modello di orario per il turno 'nome del modello di orario' non è valido e non può quindi essere pianificato.

In ogni rotazione puoi impostare un periodo durante il quale la rotazione può essere inserita. Per impostazione predefinita, le rotazioni sono sempre valide. Se restringi il periodo, la rotazione non sarà inserita al di fuori del periodo definito. In quel caso non riceverai nessun messaggio di errore.

I periodi di validità nei modelli di orario personali (modelli di orario assegnati ai dipendenti) non influiscono sulle rotazioni. Questi modelli di orario nelle rotazioni vengono inseriti comunque.

Nota: i modelli di orario eliminati che fanno ancora parte di una rotazione vengono inseriti e contrassegnati da un bordo tratteggiato nel Centro dei turni e in Schedules. In quel caso non riceverai nessun messaggio di errore.
