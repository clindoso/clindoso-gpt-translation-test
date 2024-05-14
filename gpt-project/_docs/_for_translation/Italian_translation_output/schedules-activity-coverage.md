---
title: Analizzare la copertura, il fabbisogno di personale e l’occupazione in Schedules <!-- GPT translation -->
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Scopri come analizzare la copertura, il fabbisogno di personale e l’occupazione per le tue attività e tipi di attività. <!-- GPT translation -->
gpt_translation: true
---

In _Plan > Schedules_{:.breadcrumbs}, puoi analizzare la copertura, il fabbisogno di personale e l'occupazione per le attività pianificate e i tipi di attività. <!-- GPT translation -->

## Prerequisiti <!-- TM 100 -->

- Hai calcolato il {% link_new fabbisogno di personale | features/forecast/injixo-forecast/calculate-staff-requirements.md %}. <!-- GPT translation -->
- Hai creato una {% link_new pianificazione | getting-started/create-a-schedule.md %}. <!-- GPT translation -->

È la prima volta che utilizzi Dashboards? Meglio cominciare dalle {% link_new basi | features/monitoring/dashboards/manage-dashboards.md %}. <!-- TM 64 -->

## Visualizzare l’area delle attività <!-- GPT translation -->

1. In _Plan > Schedules_{:.breadcrumbs}, imposta i {% link_new filtri | features/scheduling/schedules/schedules-overview.md | #dati-filtrati %} e le {% link_new opzioni di visualizzazione | features/scheduling/schedules/schedules-overview.md | #area-delle-attivita %}. <!-- GPT translation -->
2\. Nell’area delle attività, espandi le unità di pianificazione che vuoi analizzare. <!-- GPT translation -->
3. Nell'[attività](#attività-tabella) area delle attività, seleziona una scheda: <!-- GPT translation -->
   - **Attività - copertura**: La differenza tra il numero di dipendenti pianificati e il fabbisogno di personale. <!-- GPT translation -->
   - **Attività - copertura**: il numero di dipendenti pianificati e <!-- GPT translation -->
   - **Attività - copertura**: il fabbisogno di personale pianificato e salvato.<br> <!-- GPT translation -->
4. Per selezionare le attività e i tipi di attività, utilizza l’icona del filtro {% icon filter | icon-only %} nell’intestazione della colonna **Attività**.<br>Le attività multiple hanno un’icona <em class="multiactivity-icon"></em>. Le subattività sono indentate sotto le multiattività.<br>Se elimini un’attività in _Plan > Configurazione > Attività_{:.breadcrumbs} e non la togli dalle unità di pianificazione a cui era stata assegnata, l’attività eliminata viene mostrata in corsivo. <!-- GPT translation -->
   - Spunta le caselle accanto alle voci che vuoi mostrare. Puoi selezionare multiattività o attività che non sono subattività. Non puoi selezionare specifiche subattività. Utilizza il campo di ricerca per cercare specifiche subattività, multiattività o altre attività per nome. <!-- GPT translation -->
   - (Facoltativo) Utilizza il campo di ricerca. Per cercare diversi termini contemporaneamente, inserisci una virgola tra un termine e l’altro. <!-- GPT translation -->
5. Clicca in un punto esterno all’area con le attività per aggiornare i dati visualizzati. <!-- GPT translation -->

### Tabella con i dati sulle attività <!-- GPT translation -->

### Tabella con i dati sulle attività

La tabella in ogni scheda include le colonne seguenti: <!-- GPT translation -->

- **Attività**: le attività o tipi di attività per i quali vuoi visualizzare i dati. <!-- GPT translation -->
- **Livello**: I livelli che hai selezionato nell’{% link_new area della pianificazione | features/scheduling/schedules/schedules-overview.md | #sezione-pianificazione %}. <!-- GPT translation -->
- **Sum**: La somma dei valori di copertura, fabbisogno di personale o pianificato per il periodo visualizzato. <!-- GPT translation -->
- Columna con la línea de tiempo: un resumen del marco temporal seleccionado con los valores de cobertura, ocupación y necesidad de personal por intervalo. <!-- GPT translation -->

Passa il mouse sopra a una cella per visualizzare i valori, per intervallo di 15 minuti, della copertura, dell’occupazione e del fabbisogno di personale. <!-- GPT translation -->

Selezionando uno o due giorni inserendo le date nel selettore di data nell’area della pianificazione, o cliccando la data nella colonna con l’indicazione delle ore, la tabella mostra una colonna per ogni ora del giorno o dei giorni scelti. <!-- GPT translation -->
Per visualizzare i dati con intervalli di 30 minuti, passa il mouse tra due ore piene nell’intestazione della tabella. Quando apparirà l’{% icon magnifying_glass %}, cliccaci sopra.<br>Per visualizzare i dati con intervalli di 15 minuti, passa il mouse sopra l’ora che termina in .30, e clicca sull’{% icon magnifying_glass %} quando apparirà.<br>Per tornare agli intervalli di 30 minuti, clicca su una delle ore che termina in .45. Per tornare a visualizzare le colonne per le ore piene, clicca su una delle ore piene in qualsiasi momento.<br> <!-- GPT translation -->
  <!-- GPT translation -->

Una cella è vuota se per l'intervallo mancano sia il fabbisogno di personale che i valori di occupazione, oppure manca uno dei due. <!-- GPT translation -->
Le caselle sono colorate in base al sistema mostrato nella tabella in basso. Più intenso è il colore, maggiore è la differenza fra il fabbisogno di personale e l’occupazione. <!-- GPT translation -->

<!-- left-align table -->
<style> <!-- TM 100 -->
table { <!-- TM 100 -->
   margin-left: 0px; <!-- TM 100 -->
} <!-- TM 100 -->
</style> <!-- TM 100 -->

| Colore     | Copertura     | Descrizione                                 | <!-- GPT translation -->
| -------- | ------------------------ |-------------------------------------------------- |
| Rosso | Insufficiente numero di dipendenti                 | Sono stati pianificati meno dipendenti di quanti ne servono. | <!-- GPT translation -->
| Blu | Eccesso di personale                 | Sono stati pianificati più dipendenti di quanti ne servono. | <!-- GPT translation -->
| Verde | Copertura ottimale                 | Il numero di dipendenti pianificati corrisponde al fabbisogno di personale. | <!-- GPT translation -->