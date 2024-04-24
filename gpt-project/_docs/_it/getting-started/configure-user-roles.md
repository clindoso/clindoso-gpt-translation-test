---
title: Configurare i ruoli utente
redirect_from:
  - /it/user-and-role-authorization/
redirect_reason: renamed file in June 2021
description: Scopri quali ruoli utente sono disponibili, modifica le autorizzazioni, crea nuovi ruoli utente e assegna ruoli agli utenti.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-user-accounts.md
---

## Che cosa sono i ruoli utente?

Un gruppo di utenti con le stesse autorizzazioni e livello di accesso ai prodotti e alle funzionalità in injixo, per esempio _Forecast_{:.menu-item}, o alle funzionalità in WFM, per esempio _WFM > Administration_{:.breadcrumbs}, ha lo stesso ruolo utente.

injixo offre delle categorie di ruoli, ognuna con un {% link_new ruolo utente prestabilito | getting-started/default-user-roles.md | #i-ruoli-utente-prestabiliti %} che ha delle autorizzazioni predefinite. Quando crei un nuovo ruolo utente all'interno di una categoria di ruoli, il ruolo utente riceverà le stesse autorizzazioni ai prodotti e alle funzionalità del ruolo utente prestabilito di quella categoria di ruoli.<br>
La categoria di ruoli **Altro** non ha un ruolo utente prestabilito.

### Vedere e organizzare i ruoli utente

Vai su _Account > Ruoli utente_{:.breadcrumbs}.

   I ruoli utente sono raggruppati in categorie di ruoli (per esempio, la categoria di ruoli **Pianificatore**). Le categorie di ruoli sono utili per mantenere in ordine le autorizzazioni. Puoi spostare con il mouse un ruolo utente da una categoria a un’altra, oppure digitare nella barra di ricerca il nome del ruolo utente che cerchi.
   
   > Auotorizzazioni per le nuove funzionalità 
   >   
   > Le autorizzazioni per le nuove funzionalità di injixo sono concesse ai ruoli utente in modo automatico in base alla categoria di ruoli a cui appartengono. Per esempio, a una nuova funzionalità per pianificatori potranno accedere tutti i ruoli utente della categoria di ruoli **Pianificatore**. Se hai spostato un ruolo utente dalla categoria di ruoli **Pianificatore** a un’altra categoria di ruoli, il ruolo utente non riceverà più automaticamente le autorizzazioni per le nuove funzionalità della categoria di ruoli **Pianificatore**. Se è necessario, un utente con accesso amministratore può aggiungere manualmente le autorizzazioni al ruolo utente.<br> Vale lo stesso per i ruoli utente della categoria di ruoli **Altro**: le autorizzazioni per questi ruoli utente devono sempre essere aggiunte manualmente.

### Creare un nuovo ruolo utente

1. Clicca sull’icona Crea un ruolo {% icon blue_plus | icon-only %} in una categoria di ruoli.

   - Categoria di ruoli **Altro**: crea un ruolo utente vuoto. Non ci sono autorizzazioni prestabilite.
   - Categorie con {% link_new ruoli prestabiliti| getting-started/default-user-roles.md %}: le autorizzazioni prestabilite per i componenti in injixo sono preselezionate. Le autorizzazioni per le funzionalità WFM non sono impostate.
  > Nota
  >
  > Quando crei un nuovo ruolo utente, devi impostare manualmente le [autorizzazioni per le funzionalità in WFM](#impostare-le-autorizzazioni-per-wfm).

2. Nella pagina **Crea ruolo utente**, configura il ruolo utente:

   - **Informazioni di base**: inserisci un **Nome**, un’**Abbreviazione** e una **Descrizione** (facoltativa).
   - **Categoria di ruoli**: mostra la **Categoria di ruoli** preselezionata.

3. (Facoltativo) Modifica le autorizzazioni prestabilite. Nella sezione **Autorizzazioni**, una spunta grigia accanto al nome di un componente indica che tutte le autorizzazioni per quel componente sono concesse per impostazione predefinita. Un segno meno in grigio indica che alcune autorizzazioni per quel componente non sono concesse per impostazione predefinita.
   - Componente: per concedere le autorizzazioni per tutte le funzionalità all’interno di un componente, spunta la casella accanto al nome del componente.
   - Funzionalità: per concedere le autorizzazioni per le singole funzionalità, clicca sulla freccia in giù accanto al nome di un componente. Spunta la casella o le caselle accanto alle funzionalità.
   -  Per vedere tutte le sezioni, clicca su **Espandi tutto**. Per chiudere tutte le sezioni, clicca su **Comprimi tutto**.
   - Per ripristinare le autorizzazioni selezionate al ruolo utente prestabilito, clicca su **Ripristina le autorizzazioni di default**.
4.  Per salvare il nuovo ruolo utente, clicca su _Crea ruolo utente_{:.doc-button}. Per [impostare le autorizzazioni per WFM ](#impostare-le-autorizzazioni-per-wfm) per il nuovo ruolo utente, clicca su _Crea e vai a Diritti per ruoli di utenti_{:.doc-button}.

### Assegnare ruoli utente agli utenti

1. Vai su _Account > Utenti_{:.breadcrumbs}.
2. Clicca su un **Nome**.
3. In **Assegna ruolo(i) utente**, spunta una o più caselle. Per filtrare i ruoli utente visualizzati, utilizza il campo di ricerca **Cerca ruoli utente**.
4. Clicca su _Salva_{:.doc-button}.

## Impostare le autorizzazioni per WFM

1. In _Account > Ruoli utente_{:.breadcrumbs}, seleziona un ruolo utente.
2. Nella sezione **Autorizzazioni**, clicca su **Vai a Diritti per ruoli di utenti**.  
   Verrai reindirizzato a _WFM > Administration > Sistema > Diritti per ruoli di utenti_{:.breadcrumbs}.
3. Nella sezione **Mappa di navigazione** a destra, seleziona o deseleziona le caselle per aggiungere o rimuovere autorizzazioni.

{{ 4 | image: "Sezione Mappa di navigazione in WFM Diritti per ruoli di utenti", '60%' }}

> Nota
>
> Le autorizzazioni degli utenti singoli possono sovrascrivere le autorizzazioni basate sui ruoli (anche per gli utenti con accesso amministratore).
>
> Se possibile, utilizza soltanto autorizzazioni basate sui ruoli. Puoi modificare le autorizzazioni per singoli utenti in _WFM > Administration > Sistema > Diritti utenti_{:.breadcrumbs} ma tali modifiche sovrascriveranno le autorizzazioni basate sui ruoli. 
>
> Per ripristinare le autorizzazioni specifiche dell'utente, potrebbe essere necessario rimuovere temporaneamente l'accesso amministratore per attivare le caselle di controllo disattivate sulla pagina con le autorizzazioni dell'utente. Clicca sull’icona con l’asterisco {% icon asterisk | icon-only %} per ripristinare le autorizzazioni prestabilite del ruolo.

## Gestire l’accesso ai team: limitare l’accesso ai dati di configurazione

Se la tua organizzazione comprende molti team, e vuoi limitare l’accesso ai dati dei team, puoi assegnare a un utente diversi ruoli utente. injixo combina le autorizzazioni previste dai diversi ruoli utente. È possibile limitare l’accesso a elementi come le unità di pianificazione, i modelli di orario, le attività e i report.

**Esempio**

Se vuoi che tutti i pianificatori abbiano accesso alla pianificazione, ma vuoi che ogni pianificatore possa modificare soltanto i dati della sua unità di pianificazione, puoi assegnare due ruoli utente a ogni pianificatore.

Puoi creare un nuovo ruolo utente senza accesso a nessuna specifica unità di pianificazione, oppure rimuovere l’accesso a tutte le unità di pianificazione da un ruolo utente già esistente. Per rimuovere l’accesso a tutte le unità di pianificazione da un ruolo utente già esistente, segui i passaggi elencati di seguito.

1. Vai su _Account > Ruoli utente_{:.breadcrumbs}.
2. Seleziona il ruolo utente.
3. Clicca su **Vai a Diritti per ruoli di utenti**.
4. Scorri fino alla sezione **Unità pianificative** (o clicca sul link in alto).
5. Clicca sull’icona {% icon item-delete %} accanto alla voce [Tutte] per eliminare l’accesso a tutte le unità di pianificazione.
6. Clicca su _OK_{:.doc-button}.

Per aggiungere ad altri ruoli l’accesso a una specifica unità di pianificazione, segui i passaggi elencati di seguito.

1. Seleziona il secondo ruolo utente.
2. Nella sezione **Unità pianificativa**, clicca sull’icona Aggiungi {% icon item-add | icon-only %}.
3. Seleziona la/le unità pianificativa/e dall’elenco. Per aggiungere più unità di pianificazione, selezionale con il mouse mentre tieni premuto il tasto **CTRL** o **Shift**.
4. In **Diritti di accesso**, imposta i diritti di **Lettura**, **Modifica** ed **Eliminazione** spuntando le caselle corrispondenti.
5. Clicca su _OK_{:.doc-button}.

Per completare la configurazione, vai su _Account > Utenti_{:.breadcrumbs} e [assegna i ruoli agli utenti](#assegnare-ruoli-utente-agli-utenti).

## Modificare i ruoli utente personalizzati o predefiniti

1. Vai su _Account > Ruoli utente_{:.breadcrumbs}.
2. Seleziona il ruolo utente che vuoi modificare.
3. Apporta le modifiche desiderate, e clicca su _Salva modifiche_{:.doc-button}.

## Eliminare i ruoli utente personalizzati

1. Vai su _Account > Ruoli utente_{:.breadcrumbs}.
2. Seleziona il ruolo utente.
3. Clicca su _Elimina_{:.doc-button} in basso a destra. Non è possibile eliminare i ruoli utente prestabiliti.
