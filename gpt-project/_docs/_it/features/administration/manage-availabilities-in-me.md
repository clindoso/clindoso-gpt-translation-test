---
title: Gestire le disponibilità in injixo Me
description: Impedisci ai dipendenti di aggiungere o modificare le loro disponibilità uniche prima di una certa data.
product_label:
  - essential
  - advanced
  - enterprise
toc: true
---

In injixo, le disponibilità definiscono quando un dipendente è disponibile per la pianificazione in date o orari specifici. In quanto pianificatore, puoi configurare le disponibilità in due modi:
- utilizzando le {% link_new disponibilità settimanali | features/administration/availabilities.md | #configurare-le-disponibilità %};
- utilizzando i {% link_new modelli di orario | features/administration/availabilities.md | #alternare-le-disponibilità-tra-le-settimane %}.

Inoltre, i dipendenti possono aggiungere delle [disponibilità uniche in injixo Me](/add-availabilities-in-me#add-an-availability). Se hai già configurato delle disponibilità settimanali, le disponibilità uniche le sostituiranno.

## Dare ai dipendenti l’accesso alle disponibilità

Per permettere ai dipendenti di accedere alle disponibilità in injixo Me, configura il loro ruolo utente:

1. Vai su _Account > Ruoli utente_{:.breadcrumbs}.
2. Clicca sul ruolo utente rilevante.
3. Nella sezione **Autorizzazioni**, espandi il menu a tendina **Me**.
4. Spunta la casella **Disponibilità**.
5. Clicca su _Salva modifiche_{:.doc-button}.

A partire dal giorno successivo il dipendente potrà inserire le sue disponibilità in Me.

## Impedire ai dipendenti di modificare le loro disponibilità

La disponibilità dei tuoi dipendenti può variare da un giorno all’altro o da una settimana all’altra. Per permettere ai dipendenti di aggiungere le loro disponibilità in injixo Me, e al tempo stesso evitare conflitti di pianificazione, puoi impedire ai dipendenti di aggiungere o modificare le disponibilità uniche prima di una certa data.

Esempio: vuoi creare le pianificazioni con due settimane di anticipo. Per impedire che i dipendenti aggiungano o modifichino le loro disponibilità durante quelle due settimane, seleziona una data alla fine del periodo pianificato. Se crei una pianificazione il 2 gennaio per la settimana a partire dal 15 gennaio, seleziona il 22 gennaio. In questo modo i dipendenti non potranno aggiungere o modificare le loro disponibilità fino al 22 gennaio.

Per impedire ai dipendenti di modificare le loro disponibilità in injixo Me prima di una certa data, procedi come di seguito:

1. Vai su _Plan > Configurazione > Dipendenti_{:.breadcrumbs}.
2. Seleziona una data con il selettore di date.
3. Clicca su _Salva modifiche_{:.doc-button}.

Prima della data specificata i dipendenti potranno vedere le loro disponibilità ma non potranno modificarle. Se non inserisci nessuna data, i dipendenti possono aggiungere o modificare le loro disponibilità uniche in qualsiasi momento.
