---
title: Aggiungere gli eventi e i festivi
product_label:
  - advanced
  - enterprise
  - classic
description: Crea eventi e tipi di eventi per migliorare la precisione della tua previsione
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
---

Aggiungi degli eventi ai tuoi dati storici e alle previsioni generate per migliorare i risultati delle previsioni. Dopo i dati, gli eventi sono il fattore che influisce di più sulla qualità delle previsioni.

È la prima volta che utilizzi injixo Forecast? Meglio cominciare dalle {% link_new basi | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Che cosa sono gli eventi?

Gli eventi ti permettono di contrassegnare i giorni, sia passati che futuri, che deviano dallo standard. Per esempio:

- i giorni con volumi di contatto o con valori di tempo medio di gestione (AHT) insolitamente alti;
- i giorni con distribuzioni di volume che deviano da quelle di un giorno standard;
- i giorni con dati incompleti, difettosi o mancanti, per esempio a causa di un'interruzione del sistema ACD.

injixo Forecast analizza gli eventi aggiunti al workload per rilevare tendenze, fluttuazioni nel volume e altri schemi, al fine di migliorare la previsione generata.

## Creare un tipo di evento

Le categorie predefinite raggruppano tipi di eventi simili, per esempio le campagne di marketing o le newsletter.
Tutti i tipi di eventi che crei sono disponibili per tutti i workload. Ogni categoria può includere fino a sette tipi di eventi.

1. In _Forecast > Workload_{:.breadcrumbs}, scegli un workload.
2. Dal {% icon ellipsis_v %} in alto a destra, seleziona **Personalizza i tipi di eventi**.
3. Seleziona una **categoria** dal menu a tendina.
4. Clicca su **\+ Aggiungi tipo di eventi** e inserisci un nome.
5. Clicca su _Aggiungi tipo di eventi_{:.doc-button}.
6. Clicca su _Chiudi_{:.doc-button}.

## Eliminare un tipo di eventi

Elimina i tipi di eventi obsoleti o sostituisci un tipo di eventi con un altro, per esempio se hai raggiunto il limite di sette tipi di eventi per categoria.

> Attenzione
>
> Se elimini un tipo di eventi, tutti gli eventi corrispondenti  verranno eliminati da tutti i workload e da tutte le previsioni generate.

1. In _Forecast > Workload_{:.breadcrumbs}, scegli un workload.
2. Dal {% icon ellipsis_v %} in alto a destra, seleziona **Personalizza i tipi di eventi**.
3. Seleziona una **categoria** dal menu a tendina.
4. Clicca sull’icona Elimina {% icon trash | icon-only %} accanto al tipo di eventi che vuoi eliminare.
5. Clicca su _Elimina tipo di eventi_{:.doc-button} nella finestra.
6. Clicca su _Chiudi_{:.doc-button}.

## Aggiungere un evento o un’interruzione a un workload

Aggiungi tutti gli eventi conosciuti alle date, passate o future, corrispondenti. Ometti i periodi più lunghi che presentano schemi non comuni, poiché periodi e schemi di questo tipo influiscono negativamente sulla qualità della previsione nel tempo.

I workload del tipo Smart tengono conto dell'impatto degli eventi anche nei due giorni precedenti e nei due giorni successivi alla data dell'evento. I carichi di lavoro del tipo Basic considerano solo l'impatto degli eventi sul giorno effettivo.

Per aggiungere un evento o un’interruzione, procedi come di seguito:

1. In _Forecast > Workload_{:.breadcrumbs}, scegli un workload.
2. Dal {% icon ellipsis_v %} in alto a destra, seleziona **Gestisci gli eventi**.
3. Nella finestra, clicca su **\+ Aggiungi evento** o **\+ Aggiungi interruzione** e inserisci i dati corrispondenti:
   - **Data**: seleziona il giorno a cui vuoi aggiungere l’evento.
   - **Categoria**: seleziona una categoria dal menu a tendina.
   - **Evento**: seleziona un evento dal menu a tendina.
4. Clicca su _Crea evento_{:.doc-button} o su _Crea interruzione_{:.doc-button}.
5. Clicca su _Chiudi_{:.doc-button}.

> Nota
>
> Aggiungi un’interruzione per escludere un giorno nel passato dal calcolo della previsione.

## Modificare il calendario dei festivi

Aggiungi i giorni festivi da uno dei calendari dei festivi disponibili. injixo Forecast considera i giorni festivi come se fossero degli eventi, dal momento che possono influire sul volume. Puoi selezionare il calendario dei festivi per un workload durante la {% link_new sua creazione | features/forecast/injixo-forecast/create-workloads.md | #creare-un-workload %}. Per cambiare il calendario dei festivi, procedi come di seguito:

1. In _Forecast > Workload_{:.breadcrumbs}, scegli un workload.
2. Clicca su _Modifica workload_{:.doc-button} in alto a destra.
3. Seleziona un **calendario dei festivi** dal menu a tendina.
4. Clicca su _Salva workload_{:.doc-button}.

## Vedere gli eventi e i festivi

Puoi identificare facilmente gli eventi e i giorni festivi nei grafici. Gli eventi, le interruzioni e i giorni festivi sono mostrati con colori diversi. A ogni tipo di eventi è associato un colore. Nella legenda puoi vedere quali colori sono associati ai vari tipi di eventi.

1. In _Forecast > Workload_{:.breadcrumbs}, scegli un workload.
2. Seleziona un periodo dal selettore di data. Clicca sul numero della settimana per selezionare la settimana per intero, oppure clicca e trascina per selezionare un periodo più breve o più lungo.
3. Passa il mouse sopra i grafici per vedere eventi e giorni festivi.
  <!-- {{ 3 | image: "Viewing Events", '80%', 'gif' }} -->

## Eliminare un evento

1. In _Forecast > Workload_{:.breadcrumbs}, scegli un workload.
2. Seleziona un periodo dal selettore di data. Clicca sul numero della settimana per selezionare la settimana per intero, oppure clicca e trascina per selezionare un periodo più breve o più lungo.
3. Dal {% icon ellipsis_v %} in alto a destra, seleziona **Gestisci gli eventi**.
4. Clicca sull’icona Elimina {% icon trash | icon-only %} accanto all’evento che vuoi eliminare.
5. Clicca su _Chiudi_{:.doc-button}.