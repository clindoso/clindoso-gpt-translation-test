---
title: Scaricare le previsioni
toc: true
product_label:
  - advanced
  - enterprise
  - classic
description: Scarica le previsioni in formato CSV da injixo Forecast. Scopri il formato dei file.
---

In _Forecast > Workloads_{:.breadcrumbs} puoi scaricare i dati delle previsioni in formato CSV.

Puoi esportare dati fino a un massimo di un anno. Puoi scaricare i dati della {% link_new versione | features/forecast/injixo-forecast/save-forecast-versions.md | #salvare-una-versione-della-previsione %} Forecast soltanto, oppure scaricare anche i dati delle versioni Operativa e Strategica.

## Scaricare una previsione

1. In _Forecast > Workloads_{:.breadcrumbs}, seleziona un workload.
2. Seleziona il periodo nel selettore di data. Clicca sul numero della settimana per selezionare la settimana per intero, oppure clicca e trascina per selezionare un periodo più breve o più lungo.
3. Dal {% icon ellipsis_v %} in alto a destra, seleziona **Scarica come CSV**.
4. Seleziona i dati di previsione che vuoi scaricare.<br>Per selezionare tutte le versioni disponibili, spunta la casella **Tutto**.
5. Clicca su _Scarica come CSV_{:.doc-button}.<br>
   Le versioni delle previsioni scaricate vengono salvate in un unico file.

## Esempio di file CSV

Il nome del file CSV include il nome del workload e il nome del canale. Per esempio, il nome del file CSV per il workload delle chiamate Ordini sarà `Ordini-Chiamate.csv`. Le intestazioni delle colonne mostrano la versione della previsione. Il file contiene i timestamp (nel formato AAAA-MM-GG) e i valori per ogni previsione, e utilizza il fuso orario e l'intervallo del workload. Il file non contiene nessuna informazione sui giorni festivi, sugli eventi aggiunti al workload o sui dati storici.

Se selezioni **Forecast** e **Operativa**, il file sarà strutturato come questo esempio:

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
...
2020-05-17 16:30;40;180;35;175
2020-05-17 16:45;41;181;37;183
2020-05-17 17:00;40;180;35;175
2020-05-17 17:15;41;181;37;183
...
```

> L'opzione per scaricare il file è disponibile soltanto per i workload di tipo Smart in modalità Live.
>
> Attiva la modalità Live per il workload per poter scaricare il file. Leggi l’articolo {% link_new Creare i workload | features/forecast/injixo-forecast/create-workloads.md %} per saperne di più sulla modalità Live e sulla modalità Test. I workload di tipo Smart sono disponibili soltanto per i piani WFM Enterprise e Advanced.
