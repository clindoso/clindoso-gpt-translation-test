---
title: Disattivare, riattivare ed eliminare i dipendenti
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Scopri quando e come disattivare, riattivare o eliminare i dipendenti.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/how-does-billing-work.md
---

Se un dipendente non viene più incluso nella pianificazione o non ha più bisogno di accedere a injixo, puoi disattivarlo o eliminarlo. Queste azioni hanno due conseguenze:

- I dipendenti disattivati perdono la possibilità di accedere a injixo.
- Questi dipendenti non verranno più {% link_new fatturati | getting-started/how-does-billing-work.md %} alla tua organizzazione (a partire dal mese successivo).

## Disattivare un dipendente

I dipendenti che non lavorano per un periodo prolungato, per esempio perché vanno in aspettativa, in maternità o in congedo parentale, possono essere disattivati temporaneamente. I dipendenti disattivati non verranno fatturati alla tua organizzazione. Puoi riattivare i dipendenti quando rientrano al lavoro. In alcuni casi, il regolamento generale sulla protezione dei dati (GDPR) potrebbe richiedere l’eliminazione dei dati di un dipendente. In questi casi, [elimina](#eliminare-un-dipendente) il dipendente.

Per disattivare un dipendente, segui questi passaggi:

1. Vai su _Plan > Configurazione > Dipendenti_{:.breadcrumbs}.
2. Nell’elenco dei dipendenti, clicca sul dipendente che vuoi disattivare.
3. Nella sezione **Appartenenza all’organico** del pannello di configurazione del dipendente, clicca sull’icona Modifica {% icon item-edit | icon-only %}.
4. Alla voce **Data di licenziamento**, inserisci la data di disattivazione.<br>Una data passata disattiverà immediatamente il dipendente. Una data futura disattiverà il dipendente in quella data.
5. Clicca su _OK_{:.doc-button}.<br>Apparirà un messaggio di conferma.
6. Per eliminare le pianificazioni future ma mantenere lo storico dei dati di pianificazione, clicca su _Sì_{:.doc-button}. Per mantenere tutti i dati di pianificazione relativi al dipendente disattivato, clicca su _No_{:.doc-button}.

### Visualizzare i dipendenti disattivati

1. Vai su _Account > Utenti_{:.breadcrumbs}.
2. Clicca sulla scheda **Utenti non fatturati**.<br>La tabella comprende tutti gli utenti disattivati che non vengono fatturati alla tua organizzazione.

### Riattivare un dipendente

Per riattivare un dipendente, per esempio quando rientra dopo una lunga assenza, segui questi passaggi:

1. Vai su _Plan > Configurazione > Dipendenti_{:.breadcrumbs}.
2. Utilizza il campo di ricerca nell’angolo in alto a sinistra per trovare il dipendente che vuoi riattivare.<br>Si aprirà una finestra. Se hai inserito il nome completo del dipendente e la ricerca restituisce un solo risultato, la finestra mostrerà il pannello per la configurazione del dipendente. Se la ricerca restituisce più di un risultato, la finestra mostrerà un elenco di dipendenti.
3. Se la finestra mostra un elenco, clicca sul dipendente che vuoi riattivare.
4. Nella sezione **Appartenenza all’organico** del pannello di configurazione del dipendente, clicca sull’icona Aggiungi {% icon item-add | icon-only %}.
5. Alla voce **Data d’assunzione**, inserisci la data di ritorno del dipendente.
6. Clicca su _OK_{:.doc-button}.

## Eliminare un dipendente

> Attenzione
>
> Non è possibile riattivare un dipendente che è stato eliminato. Il dipendente verrà eliminato da tutte le pianificazioni presenti e future per le quali era stato pianificato. Eliminare un dipendente non influisce sui dati dell'aderenza storica in {% link_new Intraday | features/intraday/adherence-intraday.md %}.

Elimina i dipendenti soltanto se il loro periodo di impiego presso la tua organizzazione si è concluso definitivamente. Se i dipendenti si assentano per un periodo prolungato, per esempio per un’aspettativa, una maternità o un congedo parentale, puoi invece [disattivarli](#disattivare-un-dipendente).

Per eliminare un dipendente, segui questi passaggi:

1. Vai su _Plan > Configurazione > Dipendenti_{:.breadcrumbs}.
2. Nell’elenco dei dipendenti, clicca sul dipendente che vuoi eliminare.
3. Nella barra delle azioni, clicca sull’{% icon item-delete %}.<br>Apparirà un messaggio di conferma.
4. Clicca su _Sì_{:.doc-button}.<br>Il dipendente e tutte le sue pianificazioni presenti e future vengono eliminate da injixo.

Quando elimini un dipendente da injixo, i suoi dati personali vengono anonimizzati per garantire la protezione della privacy. injixo mantiene l’ID del dipendente ma lo contrassegna come eliminato, e sostituisce il nome del dipendente con degli asterischi. Inoltre, injixo modifica i dettagli personali per rimuovere tutte le informazioni identificabili, come il nome, il numero di matricola, gli indirizzi, i numeri di telefono e gli indirizzi email. Se la configurazione del dipendente includeva i numeri dei suoi documenti di riconoscimento, injixo li elimina del tutto.
