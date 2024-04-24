---
title: Vedere e approvare le richieste di scambio dei turni
product_label:
  - essential
  - advanced
  - enterprise
description: Vedi e approva oppure rifiuta le richieste di scambio dei turni in sospeso. Vedi gli scambi di turni passati.
---

In injixo Me, gli utenti con il ruolo di agente possono {% link_new scambiarsi i turni | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #scambiare-i-turni %} o i giorni liberi, sia nello stesso giorno che in giorni diversi.

Ecco come funziona lo scambio dei turni:

1. Un dipendente offre un turno in injixo Me.
2. Gli altri dipendenti possono vedere il turno offerto e offrire in cambio uno dei loro turni.
3. Il dipendente che offre il turno accetta la controfferta che risponde meglio alle sue esigenze.
4. injixo conferma automaticamente la scelta e, se necessario, crea la richiesta di approvazione.
5. Un utente con accesso amministratore o con il ruolo di pianificatore rivede, approva o rifiuta lo scambio richiesto. Per attivare le approvazioni automatiche, cambia l’impostazione _48152_{:.id-label} da 0 a 1.

Per scoprire come i dipendenti possono scambiarsi i turni in injixo Me, leggi l’articolo {% link_new Scambiare i turni con i colleghi | features/injixo-me/use-injixo-me/swap-shifts-with-your-colleagues.md | #scambiare-i-turni %}.

> Consiglio
>
> Nel {% link_new Calendario del team | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} in injixo Me, i dipendenti possono vedere gli orari di lavoro dei loro colleghi.

## Prerequisiti

I dipendenti con il ruolo di agente possono offrire un turno se si verificano le seguenti condizioni:

- Lo {% link_new scambio dei turni è attivato | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} in injixo Me.
- Tutte le attività in un turno sono {% link_new scambiabili con scambio turni | features/administration/activity-types-and-properties.md %}.
- Esiste un {% link_new periodo di pianificazione | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %} con lo stato Offerte turni attivata, Pubblicato o Finito.
- La scadenza configurata per il periodo di pianificazione non è ancora stata raggiunta.
- Il valore configurato nell’impostazione _48151_{:.id-label} stabilisce il numero di giorni, a partire dal giorno in corso, per i quali lo scambio di turni non è permesso. Per esempio, se inserisci 0 lo scambio di turni è permesso a partire da oggi. Se inserisci 1, lo scambio di turni è permesso a partire da domani.
- I dipendenti hanno accesso in modalità visualizzazione a injixo Me.

## Approvare o rifiutare gli scambi di turni

Soltanto gli utenti con accesso amministratore o con il ruolo di pianificatore possono rivedere, approvare e rifiutare gli scambi di turni.

Per rivedere, approvare o rifiutare le richieste di scambio di turni, procedi come di seguito:

1. Vai su _Plan > Schedules_{:.breadcrumbs}.
2. Dal menu _Azioni di pianificazione_{:.doc-button}, seleziona **Approvare gli scambi di turni**.
3. Seleziona una **unità di pianificazione** e una **selezione** dai menu a tendina.
4. Seleziona un **intervallo di date**.<br>Se non hai già selezionato un intervallo di date in _Schedules_{:.menu-item}, l’intervallo di date inizia nella data attuale e finisce sette giorni dopo.
6. Spunta le caselle accanto alle voci che vuoi approvare o rifiutare. Usa la casella in alto per selezionare tutte le voci contemporaneamente.
7. Clicca su _Approva selezionate_{:.doc-button} o su _Rifiuta selezionate_{:.doc-button}.  
   Dopo essere state approvate o rifiutate, le richieste vengono spostate nella scheda **Informazione**.

Il report Operazioni di scambio (statistica) _WFM > Monitoring > Report_{:.breadcrumbs} elenca gli stati degli scambi di turni (incompleti, in attesa di approvazione, rifiutati e approvati).

## Generare un elenco degli scambi di turni passati

Nella pagina **Approvare gli scambi di turni**, la scheda **Informazione** mostra quale dipendente ha scambiato quale turno e a che ora. L’elenco mostra le richieste approvate, rifiutate e annullate. Per avere maggiori informazioni sulle richieste annullate, passa il mouse sopra l’{% icon info_circle %}.

## Impostazioni dello scambio di turni

In _WFM > Administration > Sistema > Impostazioni_{:.breadcrumbs} ci sono diverse impostazioni per allineare il procedimento dello scambio di turni alle esigenze della tua organizzazione:

- _48151_{:.id-label} _Fine del periodo di sbarramento_: il numero di giorni a partire dalla data attuale durante i quali gli scambi di turni non sono consentiti (impostazione predefinita: 3 giorni).
- _48152_{:.id-label} _Modalità di scambio_: stabilisci se un utente con accesso amministratore o con il ruolo di pianificatore deve approvare gli scambi di turni tra dipendenti (il valore prestabilito è 0 e indica che è necessaria un’approvazione. Scegli 1 per far sì che gli scambi di turni vengano approvati automaticamente).
- _48153_{:.id-label} _Abilitazione allo scambio_: consenti gli scambi tra i dipendenti assegnati a un’unità di pianificazione (valore 0, prestabilito), tra i dipendenti assegnati a un gruppo di selezione (valore 1), o tra i dipendenti assegnati a unità di pianificazione diverse (valore 2).
- _48555_{:.id-label} _Autorizzazione allo scambio fra giorni di lavoro e giorni liberi_: consenti ai dipendenti di scambiare dei turni con dei giorni liberi (valore prestabilito: 0, lo scambio non è consentito).
- _48556_{:.id-label} _Autorizzazione allo scambio fra giorni diversi_: consenti ai dipendenti di scambiarsi turni in giorni diversi (valore prestabilito:  0, lo scambio non è consentito).
- _48999_{:.id-label} _Abilita verifiche specifiche per subattività di multiattività in relazione alla regola di pianificazione 2605_: injixo verifica le qualifiche per ogni subattività durante lo scambio di multiattività (valore predefinito: 0, la verifica non avviene).

## Perché gli scambi di turni sono bloccati?

I dipendenti possono vedere e scambiarsi i turni offerti in injixo Me se la loro richiesta di scambio di turni rispetta le ore lavorative configurate nel loro contratto e se hanno le qualifiche richieste.

Per scoprire perché lo scambio di turni in injixo Me è bloccato, simula lo scambio nel _Centro dei turni_{:.menu-item}. Quando copi e incolli i turni, la {% link_new finestra dei messaggi | features/scheduling/shiftcenter/shift-center-overview.md | #message-window %} in fondo alla schermata mostrerà la {% link_new regola di pianificazione | features/administration/create-contracts.md | #regole-di-pianificazione %} e il motivo per i quali lo scambio di turni è bloccato, per esempio qualifiche incorrette o altri vincoli contrattuali.
