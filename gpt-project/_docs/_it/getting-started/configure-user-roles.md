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

Un ruolo utente definisce i diritti di accesso di un gruppo di utenti:

- ai prodotti e alle funzionalità in injixo, per esempio _Forecast_{:.menu-item};
- ai componenti in WFM, come, per esempio, _WFM > Administration_{:.breadcrumbs}.

In injixo ci sono diverse categorie di ruoli, ognuna con un {% link_new ruolo utente prestabilito | getting-started/default-user-roles.md | #i-ruoli-utente-prestabiliti %} che ha dei diritti di accesso, cioè delle autorizzazioni, predefiniti. Quando crei un nuovo ruolo utente all'interno di una categoria di ruoli, gli verranno attribuiti i diritti di accesso ai prodotti e alle funzionalità del ruolo utente predefinito.<br>
La categoria di ruoli Altro non prevede un ruolo utente predefinito.

### Vedere e organizzare i ruoli utente

Vai su _Account > Ruoli utente_{:.breadcrumbs}.  
   I ruoli utente sono raggruppati in categorie di ruoli prestabilite (per esempio, la categoria di ruoli Pianificatore). Le categorie di ruoli sono utili per mantenere in ordine i diritti di accesso. Puoi spostare con il mouse un ruolo utente da una categoria a un’altra, oppure puoi digitare nella barra di ricerca il nome del ruolo utente che cerchi.
   
   > Le autorizzazioni per le nuove funzionalità sono concesse sulla base delle categorie di ruoli  
   >   
   >Le autorizzazioni per le nuove funzionalità di injixo sono concesse ai ruoli utente in modo automatico e in accordo con la categoria di ruoli a cui appartengono. Per esempio, a una nuova funzionalità per pianificatori potranno accedere tutti i ruoli utente della categoria di ruoli Pianificatore. Se hai spostato un ruolo utente dalla categoria di ruoli Pianificatore a un’altra categoria di ruoli, non avrà più accesso automatico alla nuova funzionalità per la categoria di ruoli Pianificatore. Se è necessario, un utente con accesso amministratore può aggiungere manualmente le autorizzazioni al ruolo utente. Lo stesso vale per i ruoli utente della categoria di ruoli Altro: le autorizzazioni per questi ruoli devono sempre essere impostate manualmente.

   {{ 1 | image: "Panoramica delle categorie di ruoli utente", '83%' }}

### Creare nuovi ruoli utente

1. Clicca sull’icona Crea un ruolo {% icon blue_plus | icon-only %} in una categoria di ruoli. Passa con il mouse sopra l’icona Informazioni {% icon info_circle | icon-only %} per avere informazioni aggiuntive su ciascuna categoria di ruoli.

   - Categoria Altro: crea un ruolo utente vuoto. Non prevede autorizzazioni prestabilite.
   - Categorie con {% link_new ruoli prestabiliti | getting-started/default-user-roles.md %}: le autorizzazioni prestabilite per le funzionalità in injixo sono preselezionate. I diritti di accesso alle funzionalità in WFM non sono impostati. 
  > Nota
  >
  > Quando crei un nuovo ruolo utente, devi impostare manualmente le [autorizzazioni per i componenti in WFM](#impostare-le-autorizzazioni-per-wfm).

2. Nella pagina **Crea ruolo utente**, configura il ruolo utente:

   - **Informazioni di base**: inserisci un **Nome**, un’**Abbreviazione** e una **Descrizione** (facoltativa).
   - **Categoria di ruoli**: mostra la **Categoria di ruoli** preselezionata.

3. (Facoltativo) Modifica le autorizzazioni prestabilite. Nella sezione **Autorizzazioni**, una spunta grigia accanto al nome di un modulo indica che tutte le autorizzazioni per quel modulo sono concesse di default. Un segno meno grigio indica che alcune autorizzazioni per quel modulo non sono concesse di default.  
   - Modulo: per concedere le autorizzazioni per tutte le funzionalità all’interno di un modulo, spunta la casella accanto al nome del modulo.
   - Funzionalità: per concedere le autorizzazioni per specifiche funzionalità, clicca sulla freccia in giù accanto al nome di un modulo. Spunta la/e casella/e accanto alla/e funzionalità.
   - Per vedere tutte le sezioni, clicca su **Espandi tutto**. Per chiudere tutte le sezioni, clicca su **Comprimi tutto**.
   - Per riportare le autorizzazioni selezionate al ruolo utente prestabilito, clicca su **Ripristina le autorizzazioni di default**.
4. Per salvare il nuovo ruolo utente, clicca su _Crea ruolo utente_{:.doc-button}. Per [impostare le autorizzazioni per WFM](#impostare-le-autorizzazioni-per-wfm) per il nuovo ruolo utente, clicca su _Crea e vai a Diritti per ruoli di utenti_{:.doc-button}.

   {{ 2 | image: "Pagina dei ruoli utente", '80%' }}

### Assegnare ruoli utente agli utenti

1. Vai su _Account > Utenti_{:.breadcrumbs}.
2. Clicca su un **Nome**.
3. In **Assegna ruolo(i) utente**, spunta una o più caselle. Per filtrare i ruoli utente visualizzati, utilizza il campo di ricerca **Cerca ruoli utente**.
4. Clicca su _Salva_{:.doc-button}.

   {{ 6 | image: 'Assegnare ruoli utente', '80%'}}

## Impostare le autorizzazioni per WFM

1. In _Account > Ruoli utente_{:.breadcrumbs}, seleziona un ruolo utente.
2. Nella sezione **Autorizzazioni**, clicca su **Vai a Diritti per ruoli di utenti**.  
   Verrai reindirizzato a _WFM > Administration > Sistema > Diritti per ruoli di utenti_{:.breadcrumbs}.
3. Nella sezione **Mappa di navigazione** a destra, seleziona o deseleziona le caselle per aggiungere o rimuovere diritti.

{{ 4 | image: "Sezione Mappa di navigazione in WFM Diritti per ruoli di utenti", '60%' }}

Ti consigliamo di utilizzare soltanto autorizzazioni basate sui ruoli utente. Se è necessario, puoi modificare le autorizzazioni per alcuni utenti specifici. Per modificare le autorizzazioni individuali, vai su _WFM > Administration > Sistema > Diritti utenti_{:.breadcrumbs}.

## Gestire l’accesso ai team: limitare l’accesso ai dati di configurazione

Se la tua organizzazione comprende molti team e vuoi limitare l’accesso ai dati dei team, puoi assegnare più di un ruolo utente a un utente. injixo combina le autorizzazioni previste dai diversi ruoli utente. È possibile limitare l’accesso a elementi come le unità di pianificazione, i modelli di orario, le attività e i report.

**Esempio**

Se vuoi che tutti i pianificatori abbiano accesso alla pianificazione ma vuoi che ogni pianificatore possa modificare soltanto i dati della sua unità di pianificazione, puoi assegnare due ruoli utente a ogni pianificatore.

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
3. Clicca su _Elimina_{:.doc-button} in basso a destra. I ruoli utente predefiniti non possono essere eliminati.
