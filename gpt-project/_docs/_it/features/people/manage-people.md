---
title: Gestire i dipendenti
product_label:
  - advanced
  - enterprise
description: Scopri come creare, visualizzare, modificare ed eliminare i dipendenti.
beta-feature: true
redirect_from:
  - /it/people-overview/
redirect_reason: Renamed from /people-overview/ to /manage-people/ in Jan 2023
---

In People puoi gestire i dati principali dei dipendenti nella tua organizzazione:

- Creare, modificare ed eliminare i profili dei dipendenti.
- Invitare i nuovi dipendenti ad accedere a injixo (inviare l’email di benvenuto).
- Accedere alle impostazioni dell’account utente del dipendente.
- Accedere ai dati di configurazione del dipendente in WFM.

> Gli utenti con accesso amministratore possono accedere a People per impostazione predefinita.
>
> Per {% link_new consentire ad altri utenti l’accesso a People | getting-started/configure-user-roles.md %}, vai su _Account > Ruoli utente_{:.breadcrumbs}.

## Creare un nuovo dipendente

1. Vai su _People_{:.breadcrumbs}.
2. Clicca su _\+ Nuovo dipendente_{:.doc-button}.
3. Nella sezione **Informazioni di base**, inserisci le informazioni indispensabili relative al dipendente:
   - **Nome** e **Cognome**, e il **Secondo nome** (facoltativo).
   - **Numero di matricola**: codice che identifica in modo univoco il dipendente nella tua organizzazione.
   - **Email (per il login in injixo)**: inserisci l’indirizzo email che il dipendente usa per accedere a injixo.
4. Per invitare il dipendente ad accedere a injixo, spunta la casella **Invia email di benvenuto**.  
   Puoi inviare l’email di benvenuto soltanto durante la creazione del dipendente. L’email include le istruzioni per impostare una password e il link alla pagina di login di injixo.
5. (Facoltativo) Puoi inserire altre informazioni relative al dipendente, come il numero di telefono o altre informazioni di contatto.
Il valore che inserisci alla voce **Titolo** non viene utilizzato da nessuna funzionalità di injixo. Puoi utilizzarlo per rivolgerti al dipendente, per esempio nelle newsletter.
6. Clicca su _Crea dipendente_{:.doc-button}.  
   Se hai spuntato la casella **Invia email di benvenuto** injixo manderà al dipendente l’email di benvenuto.

## Invitare un dipendente a fare il login in injixo

È possibile {% link_new inviare l’email con l’invito a fare il login in injixo | features/people/manage-people.md | #creare-un-nuovo-dipendente %} soltanto durante la creazione del dipendente.

## Vedere o modificare un dipendente

1. Vai su _People_{:.breadcrumbs}.
2. (Facoltativo) Per cercare un dipendente utilizza il campo **Cerca**.
3. Clicca su un dipendente nell’elenco.  
   I dettagli del dipendente verranno visualizzati sulla destra. Per chiudere i dettagli, clicca su _Annulla_{:.doc-button}, o premi il tasto **Esc**.
4. Modifica i dettagli del dipendente.

   > Nota
   >
   > Se cambi l’indirizzo email, il dipendente non potrà più accedere a injixo con l’indirizzo email precedente. Assicurati di comunicare al dipendente il nuovo indirizzo email. injixo non informa i dipendenti del cambio di indirizzo email.

5. Clicca su _Salva modifiche_{:.doc-button}.

## Eliminare un dipendente

> Attenzione
>
> Non è possibile riattivare un dipendente che è stata eliminato. Il dipendente verrà eliminato da tutte le pianificazioni presenti e future per le quali era stato pianificato. Eliminare un dipendente non influisce sui dati storici sull’aderenza in {% link_new Intraday | features/intraday/adherence-intraday.md %}.

1. Vai su _People_{:.breadcrumbs}.
2. Clicca su un dipendente nell’elenco.  
   I dati del dipendente vengono visualizzati.
3. Clicca su _Elimina dipendente_{:.doc-button}.
4. Nella finestra di conferma, clicca su _Elimina dipendente_{:.doc-button}.

Per assicurarti che la pianificazione sia aggiornata dopo aver eliminato un dipendente, avvia l’ottimizzazione delle mansioni.
