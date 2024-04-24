---
title: Creare e utilizzare i tipi di giorno
description: Crea tipi di giorno per rappresentare i giorni festivi e altri giorni speciali che modificano l’orario di apertura
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Creare e gestire le unità di pianificazione
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Creare e utilizzare i calendari di pianificazione
    filepath: features/administration/configure-planning-calendars.md
  - overwrite_title: Pianificare i giorni festivi
    filepath: best-practices/scheduling-public-holidays.md
---

I tipi di giorno definiscono i giorni con un orario di apertura standard e quelli con un orario di apertura diverso.

Aggiungi i tipi di giorno alla tua {% link_new unità di pianificazione | features/administration/create-and-manage-planning-units.md | #aggiungere-gli-orari-di-apertura %} per impostare l’orario di apertura per i giorni della settimana standard e per i giorni speciali, per esempio se le tua organizzazione è aperta nei giorni festivi. injixo prenderà in considerazione gli orari di apertura definiti per quei giorni durante l’ottimizzazione delle pianificazioni.

In _Plan > Configurazione > Tipi di giorno_{:.breadcrumbs} puoi compiere le seguenti azioni:

- Vedere i tipi di giorno preconfigurati.
- Creare, modificare, ed eliminare i tipi di giorno personalizzati.

## Creare un tipo di giorno personalizzato

In certi giorni, l’orario di apertura della tua organizzazione potrebbe differire dall’orario standard, per esempio durante una promozione speciale o nei giorni festivi. Per creare dei tipi di giorno personalizzati per quei giorni, procedi come segue:

1. Clicca sull’icona Nuovo {% icon item-add | icon-only %} nella barra delle azioni.
2. Inserisci un **Nome** (massimo 50 caratteri).
3. Inserisci un’**Abbreviazione** (massimo 25 caratteri).  
   L’abbreviazione verrà utilizzata nel calendario pianificativo.
4. (Facoltativo) Spunta la casella **Modalità festività**.<br>[Scopri](#modalità-festività) come configurare i tipi di giorno per i festivi.
5. Clicca su _OK_{:.doc-button}.

## Modalità festività

Per contrassegnare un giorno come festivo, spunta la casella **Modalità festività** nella finestra di configurazione del tipo di giorno.

### Creare tipi di giorno per le festività nazionali

Hai due opzioni per creare i tipi di giorno per le festività nazionali:

- Creare tipi di giorno con modalità festività e {% link_new aggiungerli al calendario pianificativo | features/administration/configure-planning-calendars.md | #configurare-un-calendario-pianificativo %}.

- Aggiungere un {% link_new modello di calendario | features/administration/configure-planning-calendars.md | #configurare-un-calendario-pianificativo %} al tuo calendario pianificativo. Quest’azione creerà automaticamente dei tipi di giorno con modalità festività attiva per i giorni festivi inclusi nel modello di calendario.

La modalità festività comporterà una riduzione delle ore di lavoro dei dipendenti. Se decidi di pianificare un giorno festivo come un normale giorno lavorativo, puoi sempre disattivare la modalità festività, {% link_new modificando il tipo di giorno | features/administration/day-types.md | #modificare-un-tipo-di-giorno %}.

## Modificare un tipo di giorno

> Attenzione
>
> Se modifichi la modalità festività di un tipo di giorno attualmente in uso, devi ricalcolare i saldi delle ore o i {% link_new conti delle ore dovute | features/scheduling/planning-periods/target-work-accounts.md %}.
   
1. Seleziona un tipo di giorno dall’elenco.
2. Modifica i dati che vuoi cambiare.
3. Clicca su _OK_{:.doc-button}.

## Eliminare un tipo di giorno

> Nota
> 
> Prima di eliminare un tipo di giorno, {% link_new rimuovilo da tutti i calendari pianificativi | features/administration/configure-planning-calendars.md | #eliminare-i-tipi-di-giorno-dal-calendario-pianificativo %}. Non è possibile eliminare i tipi di giorno preconfigurati.

1. Seleziona un tipo di giorno dall’elenco.
2. Clicca sull'{% icon item-delete %} nella barra delle azioni.

## I tipi di giorno nella pianificazione

injixo tiene in considerazione i tipi di giorno durante la pianificazione.
- Se durante una festività la tua unità di pianificazione è aperta, dovrai solamente {% link_new aggiungere gli orari di apertura all’unità di pianificazione | features/administration/create-and-manage-planning-units.md | #aggiungere-gli-orari-di-apertura %}.  
- Se durante una festività la tua unità di pianificazione è chiusa, o se è aperta con un orario diverso, vai all’articolo {% link_new Pianificare i giorni festivi | best-practices/scheduling-public-holidays.md %}.
