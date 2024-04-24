---
title: Che cos’è injixo Forecast?
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Utilizza injixo Forecast per calcolare automaticamente le previsioni per il volume di contatto e l’AHT.
related_articles:
  - overwrite_title: Creare i workload
    filepath: features/forecast/injixo-forecast/create-workloads.md
  - overwrite_title: Modificare manualmente una previsione
    filepath: features/forecast/injixo-forecast/manual-adjustments.md
  - overwrite_title: Salvare le versioni di una previsione
    filepath: features/forecast/injixo-forecast/save-forecast-versions.md
  - overwrite_title: Scaricare le previsioni in formato CSV
    filepath: features/forecast/injixo-forecast/download-forecast.md
---

injixo Forecast combina i dati storici con gli algoritmi per generare previsioni di alta qualità. Gli algoritmi riconoscono le tendenze, i pattern e le oscillazioni inclusi nei tuoi dati. injixo Forecast utilizza molti tipi di algoritmi, come ARIMA, Holt-Winters, livellamento esponenziale, regressione, potenziamento del gradiente. 

injixo Forecast seleziona automaticamente l’algoritmo più adatto ai tuoi dati. injixo genera una previsione per 365 giorni a partire dall’ultima importazione di dati.

injixo Essential WFM utilizza un algoritmo semplice che usa i valori medi dei dati storici per riconoscere una tendenza lineare a lungo termine e dei pattern settimanali.

## Generare una previsione

Leggi la guida rapida per imparare a {% link_new generare una previsione | getting-started/calculate-a-forecast.md %}. Ogni nuova importazione di dati aggiorna la previsione generata. injixo Essential WFM genera una nuova previsione solo una volta alla settimana.

Nota: anche se la previsione generata include solo pattern settimanali ricorrenti, potrebbe comunque trattarsi della previsione ottimale. In questo caso, l’algoritmo prende in considerazione i pattern a breve termine (per le oscillazioni non ricorrenti) e considera irrilevanti i pattern a lungo termine. Le oscillazioni nei dati storici non sono sempre dei pattern.

## Dati necessari

injixo Forecast richiede l’importazione dei contatti in arrivo, del tempo medio di gestione (AHT) e dei contatti gestiti.

I workload Basic in injixo Classic richiedono almeno due settimane di dati storici. I workload Smart possono generare previsioni sulla base di un solo giorno di dati storici. Per dati che coprono due anni o più, i workload Smart tengono in considerazione le oscillazioni mensili e annuali, come, per esempio, le variazioni stagionali.

I tipi di workload disponibili dipendono dal tuo piano WFM (Classic, Essential, Advanced or Enterprise WFM).

## Come gestire dati di bassa qualità

Per generare una previsione accurata, i dati storici devono essere sia completi (quantità sufficiente di dati, con meno interruzioni possibili) che accurati (senza pattern irrilevanti). Per esempio, {% link_new eventi o festività | features/forecast/injixo-forecast/events-and-holidays.md %} contrassegnati in modo errato influiranno sulla qualità della previsione.

I dati storici potrebbero includere periodi prolungati di inattività, o mancanza di dati per certi intervalli di tempo. Più sono recenti i periodi con mancanza di dati, meno influiranno sulla qualità della previsione. 

A seguire ti proponiamo dei consigli per gestire i dati di bassa qualità in base alla durata del periodo in questione:

| Periodo con dati di bassa qualità     | Consiglio                                                                                                                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Pochi giorni | Utilizza gli {% link_new eventi | features/forecast/injixo-forecast/events-and-holidays.md %} per contrassegnare i giorni come interruzioni ed escluderli dai calcoli.                                  |
| Un paio di settimane    | Carica dei dati aggiuntivi senza interruzioni o pattern irrilevanti. |
| Parecchie settimane o mesi  | Rimuovi i dati precedenti al periodo in cui mancano i dati. Importa solo i dati successivi al periodo in cui mancano i dati.                            |

Nota: se non puoi caricare dati aggiuntivi, o se non hai abbastanza dati successivi a un periodo di mancanza di dati, gli algoritmi di Smart Forecast tenteranno automaticamente di minimizzare l’impatto negativo della mancanza di dati.

> Controlla e pulisci i dati prima di importarli
>
> Non è possibile rimuovere dati storici. Contatta il tuo consulente di riferimento se è necessario.

## Prevedere volumi bassi

injixo Forecast è in grado di generare previsioni per volumi di contatto alti e bassi. Durante la generazione di previsioni basate su volumi di contatto bassi, injixo potrebbe non riconoscere i pattern giornalieri. Questa eventualità è rara, ma potrebbe causare la mancata generazione di previsioni per alcuni giorni specifici. Per giorni singoli, modifica la previsione manualmente. Se si tratta di una situazione ricorrente, è possibile:

- aggiungere più di una coda al workload (questo causerà volumi più alti);
- usare un altro approccio per generare il fabbisogno di personale per la pianificazione, come, per esempio, {% link_new generare fabbisogno costante | features/forecast/requirement-scripts/requirement-constant.md %}.
