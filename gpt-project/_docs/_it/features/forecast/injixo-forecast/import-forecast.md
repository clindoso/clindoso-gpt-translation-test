---
title: Importare le previsioni
description: Importa una previsione da un sistema esterno in injixo Forecast.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
---

Se vuoi utilizzare i dati storici provenienti da un sistema esterno, per esempio i dati forniti da un’applicazione esterna o dai tuoi clienti, puoi importare le previsioni esterne in injixo Forecast.

È la prima volta che utilizzi injixo Forecast? Meglio cominciare dalle {% link_new basi | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Preparare l'importazione

### Prerequisiti

Per importare una previsione, ti serviranno almeno:

- un'{% link_new integrazione | features/acd-integration/cloud/how-integrations-work.md %} che importa dei dati;
- un workload con una {% link_new coda | features/forecast/injixo-forecast/create-workloads.md | #code-e-canali %}.
 
### Creare una coda

Per creare una coda è necessario importare dei dati sui contatti storici utilizzando un'integrazione. Le integrazioni creano automaticamente le code.

Se non hai un’integrazione che importa dati storici in modo continuo, puoi creare una coda importando un file CSV:

1. {% link_new Crea un’integrazione CSV | features/acd-integration/cloud/add-csv-integration.md | #configurare-una-nuova-integrazione-csv %}.
   - Salta l’installazione di Cloud Link.
   - Nella sezione **Configurazione dello schema CSV**, seleziona **Dati sui contatti**.
2. Crea un file CSV per i dati sui contatti. Il file deve contenere almeno una riga per un intervallo, per esempio:
   ```
   Queue;Date;Time;IncomingCalls;AnsweredCalls;AHT
ForecastImportQueue;22/02/2022;02:02;2;2;2
   ```
3. {% link_new Importa manualmente il file CSV | features/acd-integration/cloud/add-csv-integration.md | #importazione-manuale-dei-file %}.  
   La coda viene creata al termine dell’importazione.
   Utilizza questa coda per importare le previsioni in tutti i tuoi workload.

### Assegnare la coda al workload

Quando crei un workload, devi assegnargli una coda. Questo passaggio è parte integrante del processo di creazione, ed è un prerequisito per [importare una previsione](#importare-una-previsione). Scopri come {% link_new creare un carico di lavoro | features/forecast/injixo-forecast/create-workloads.md | #creare-un-workload %}.

Puoi importare una previsione in un workload esistente, oppure aggiungere una delle tue code a un nuovo workload.

### Requisiti dei dati importati

I dati importati devono rispettare le seguenti condizioni:

| Condizione                          | Dettagli                                                                                                                            |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Formato timestamp                     | YYYY-MM-DD HH:MM                                                                                                                   |
| Dati sul volume                          | Numeri interi                                                                                                        |
| Dati sull’AHT                             | Numeri interi oppure numeri decimali (con un decimale)                                                                  |
| Formato dell’intestazione                   | `Timestamp;Offered;AHT` o un testo personalizzato (per esempio, `Timestamp;Offered_customtext;AHT_customtext`).                                 |
| Separatori                 | Punto e virgola o virgola (riconosciuto automaticamente)                                                                                                 |
| Dimensione massima del file                    | 20 MB.<br>Il file non dovrebbe avere più di 20.000 righe.                                                                         |
| Fuso orario                            | Deve corrispondere al fuso orario della coda.                                                                                            |
| Durata dell'intervallo                      | Deve corrispondere alla durata dell’intervallo della coda (15, 30, o 60 minuti).                                                               |


In alternativa, è possibile {% link_new scaricare una previsione (o una versione della previsione) | features/forecast/injixo-forecast/download-forecast.md %} in formato CSV e usarla come modello per il tuo file di importazione. La previsione legge solo le colonne `Timestamp`, `Offered` e `AHT`. Altre colonne, come `Offered_operational` e `AHT_operational` nell’esempio sottostante, vengono ignorate.

```
Timestamp;Offered_auto;AHT_auto;Offered_operational;AHT_operational
2020-05-17 16:30;40;180;50;170
```

### Gestire i dati mancanti

I file di importazione possono avere degli intervalli senza dati. Il grafico del volume e il grafico del tempo medio di gestione (AHT) ottenuti mostreranno i valori importati come zero (0). Le righe o i valori vuoti non verranno importati.

Se non sono disponibili dati per uno o più intervalli, è possibile modificare il file CSV come segue:

- Lascia vuoti i campi del volume e dell’AHT:

  ```
  Timestamp;Offered;AHT
2020-05-17 15:00;30;210
2020-05-17 15:15;;
2020-05-17 15:30;40;180
  ```

- Importa delle colonne di zeri:

  ```
  Timestamp;Offered;AHT
2020-05-17 15:00;30;210
2020-05-17 15:15;0;0
2020-05-17 15:30;40;180
  ```

- Ometti l'intera riga:

  ```
  Timestamp;Offered;AHT
2020-05-17 15:00;30;210
2020-05-17 15:30;40;180
  ```

## Importare una previsione

1. In _Forecast > Workloads_{:.breadcrumbs}, seleziona il workload per il quale vuoi importare la previsione esterna.
2. Dal menu con i tre punti verticali {% icon ellipsis_v | icon-only %} in alto a sinistra, seleziona **Importa dati di previsione**.
3. Clicca su _Scegli file_{:.doc-button} e scegli il file in formato CSV che vuoi importare.
4. Clicca su _Importa dati_{:.doc-button}.<br>
   La finestra verrà aggiornata e mostrerà l'esito dell'importazione.
7. Clicca su _Fatto_{:.doc-button}.<br>
Aggiorna la pagina per vedere il grafico aggiornato per il periodo di importazione. I valori importati sono rappresentati da una linea marrone nei grafici delle sezioni del volume e dell'AHT.
   Per nascondere dal grafico la previsione importata, clicca sull'icona Mostra/nascondi {% icon eye | icon-only %} nella legenda accanto alla voce **Importata**.
