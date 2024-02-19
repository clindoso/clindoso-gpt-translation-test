---
title: Modifica massiva
product_label:
  - advanced
  - enterprise
  - classic
---

Utilizza le modifiche massive per modificare le assegnazioni dei dati di configurazione per più dipendenti contemporaneamente.
Puoi utilizzare la funzionalità di modifica massiva per i seguenti elementi di configurazione:

- Contratti
- Qualifiche
- Unità di pianificazione
- Gruppi di selezione
- Rotazioni
- Modelli di pianificazione

## Prerequisiti

Per poter utilizzare la funzionalità di modifica massiva, devi prima {% link_new impostare la configurazione di base | getting-started/set-up-base-configuration.md %}.

## Avviare una modifica massiva

> Nota
>
> Non è possibile annullare una modifica massiva. Avvia un’altra modifica massiva per sovrascrivere i dati che sono stati modificati in modo errato, oppure modifica i dati per ogni dipendente individualmente.  

Per avviare una modifica massiva, segui questi passaggi: 

1. Vai su _Plan > Configurazione > Dipendenti_{:.breadcrumbs}.
2. Per selezionare i dipendenti di cui vuoi modificare i dati di configurazione, scegli un gruppo di selezione o clicca sul filtro personalizzato {% icon employee-filter | icon-only %}.
3. Nella barra delle azioni, clicca sull’icona Modifica massiva{% icon mass-update | icon-only %}.<br>Si aprirà la pagina della modifica massiva. 
4. Nella sezione **Parametri**, utilizza il menu a tendina **Dati fissi** per selezionare l’elemento di configurazione che vuoi modificare contemporaneamente per più dipendenti.<br>Facoltativo: utilizza i campi **dal** e **al** per delimitare il periodo di validità della modifica massiva.
5. Seleziona una **Operazione**.
6. In base alla tua scelta, a destra verranno visualizzate le seguenti sezioni: **Assegnazioni esistenti**, **Nuova assegnazione** o **Nuovo periodo di validità**. Nelle sezioni, seleziona gli elementi che vuoi aggiungere, eliminare o sostituire.
7. Per avviare la modifica massiva, clicca su **OK**.<br>Si aprirà la pagina di elaborazione del processo.<br>Si aprirà una pagina con i risultati della modifica massiva.

| Domanda                                                                          | Risposta                                                                                                                                                                                      |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------- |
| Dopo una modifica massiva, ai dipendenti risultano assegnati dei contratti per un periodo più breve rispetto a prima. Perché?                             | Se assegni a un dipendente un elemento di configurazione che eccede il periodo di elaborazione, alcuni periodi potrebbero restare senza assegnazione.<br>Esempio: a un dipendente è assegnato un contratto dall’1 marzo al 31 maggio. Tu inserisci un nuovo periodo di validità, che va dall’1 marzo al 15 aprile. Dopo la modifica massiva, non ci sarà nessuna assegnazione per il periodo compreso tra il 16 aprile e il 31 maggio.                                                                                                                                           |
