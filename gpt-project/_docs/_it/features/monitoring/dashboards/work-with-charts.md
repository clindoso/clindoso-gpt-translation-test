---
title: Lavorare con i grafici
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Scopri come lavorare con i grafici nei pannelli di controllo.
related_articles:
  - overwrite_title: Esempi di pannelli di controllo
    filepath: features/monitoring/dashboards/dashboards-examples.md
---

In _Analyze > Dashboards_{:.breadcrumbs}, puoi lavorare con i grafici e le serie temporali per analizzare i tuoi dati. Per cominciare, seleziona un pannello di controllo dal menu a tendina in alto.

È la prima volta che utilizzi Dashboards? Meglio cominciare dalle {% link_new basi | features/monitoring/dashboards/manage-dashboards.md %}.

## Orientarsi tra i grafici

In **Dashboards** sono disponibili le seguenti azioni:

- Per cambiare il periodo per cui visualizzare i dati, seleziona un periodo dal selettore di data nella parte superiore destra di ogni grafico.
- Per ingrandire un grafico, clicca e trascina per selezionare l’area che ti interessa. 
- Per rimpicciolire il grafico, clicca su _Ripristina zoom_{:.doc-button}.
- Per passare alla modalità tabella, clicca sull’{% icon table-list %} nella parte superiore destra del grafico.
- Per tornare alla modalità grafico, clicca sull’{% icon chart-view %}.
- Per copiare i dati negli appunti, clicca sull’{% icon clone %}.

> Nota
>
> Le informazioni sulla data e sull’ora sono localizzate in base alle impostazioni della lingua di injixo. Questo potrebbe causare dei problemi se copi dei dati da injixo a un foglio Excel o Google Sheets che utilizza una lingua diversa.

## Lavorare con le serie temporali

Le serie temporali sono sequenze di dati registrati in intervalli di tempo regolari. Le sottosezioni seguenti spiegano come utilizzare le serie temporali in **Dashboards** per utilizzare, personalizzare e analizzare i tuoi dati, e prendere così decisioni consapevoli.

### Evidenziare le serie temporali

Per evidenziare temporaneamente una specifica serie temporale nella modalità grafico, passa il mouse sopra il nome della serie temporale nella legenda. Tutte le altre serie temporali scompariranno sullo sfondo.

### Mostrare e nascondere le serie temporali

Per nascondere e mostrare le altre serie temporali, clicca rispettivamente sull’{% icon eye %} e sull’{% icon eye_slash %} accanto al nome della serie nella legenda.

### Personalizzare le serie temporali

1. Vai su _Analyze > Dashboards_{:.breadcrumbs}.
2. Dal {% icon ellipsis_v %} seleziona **Modifica**.
3. Passa il mouse sopra la serie temporale nella legenda e clicca sull’{% icon pencil %}.
4. Nella finestra **Personalizza il grafico**, modifica le proprietà della serie temporale.
   - Modifica il **Nome** mostrato nella legenda.
   - Scegli tra **Passo** e **Istogramma** (grafico a barre) nel menu a tendina **Tipo**.
   - Seleziona un altro **Colore** predefinito.
   - Seleziona il modo in cui i dati sono aggregati nel grafico. Scegli **Per intervallo** (disponibile per periodi di massimo otto giorni) per mostrare i valore degli intervalli o **giornaliero** per mostrare i valori giornalieri.
   - Scegli se visualizzare l’asse y a **sinistra (impostazione predefinita)** o a **destra**.
5. Clicca su _Salva_{:.doc-button}.<br>Clicca su _Chiudi la modalità Modifica_{:.doc-button} per tornare alla modalità di visualizzazione.

### Eliminare le serie temporali

1. Vai su _Analyze > Dashboards_{:.breadcrumbs}.
2. Dal {% icon ellipsis_v %} seleziona **Modifica**.
3. Passa il mouse sopra la serie temporale nella legenda e clicca sull’{% icon pencil %}.
4. Nella finestra **Personalizza il grafico**, clicca su _Elimina_{:.doc-button}.
5. Clicca su _Salva_{:.doc-button}.<br>Clicca su _Chiudi la modalità Modifica_{:.doc-button} per tornare alla modalità di visualizzazione.
