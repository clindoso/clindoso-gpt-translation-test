---
title: Esempi di configurazione delle attività
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: false
description: Imposta le attività standard con l’aiuto di esempi.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

Per configurare il modo in cui injixo gestisce le attività durante la pianificazione e la creazione di report, utilizza i {% link_new tipi e le proprietà delle attività | features/administration/activity-types-and-properties.md %} in _Plan > Configurazione > Attività_{:.breadcrumbs}.

Qui di seguito trovi degli esempi di configurazione per le attività utilizzate più spesso, il loro tipo e le proprietà corrispondenti.

## Presenze, pause, malattie e ferie

Questa tabella include degli esempi di configurazione per le attività di tipo Presenza, Pausa, Malattia e Ferie.
L’attività Presente è un’attività standard preconfigurata in injixo. Puoi utilizzarla per tutte le attività svolte dai dipendenti e che hanno un fabbisogno di personale, come, per esempio, le chiamate.

<div class="table__wrapper" markdown="1">

<style>
table {
   width: 100%;
}
</style>

|                                        |  Presente  | Pausa pranzo |         Malattia         |  Ferie |
| ------------------------------------------- | :---------------------: | :----------------------: | :---------------------: | :---------------------: |
| **Tipo**                                        |         Presenza         |          Pausa           |         Malattia         |        Ferie         |
| Retribuita                                        | <i class="fa fa-check"> |                          | <i class="fa fa-check"> | <i class="fa fa-check"> |
| Rispettare ore di riposo                     | <i class="fa fa-check"> |                          |                         |
| Pianificabile                                   | <i class="fa fa-check"> |                          |                         |
| Richiedibile in Me                                 |                         | <i class="fa fa-check">  |                         | <i class="fa fa-check"> |
| Sostituibile                                 | <i class="fa fa-check"> |                          |                         |
| Scambiabile con scambio turni            | <i class="fa fa-check"> | <i class="fa fa-check">  |                         |
| Attività di un giorno intero                  |                         |                          | <i class="fa fa-check"> | <i class="fa fa-check"> |

</div>

A seconda delle politiche della tua organizzazione, dei contratti e delle normative sul lavoro, alcune pause potrebbero non essere retribuite. In questo caso, deseleziona la casella Retribuita.

## Assenze e riunioni

Questa tabella include degli esempi di configurazione per le attività di tipo Assenza e Meeting.
Le assenze retribuite sono usate generalmente per compensare le ore di straordinario o come blocco per {% link_new pianificare i giorni festivi | best-practices/scheduling-public-holidays.md %}.
Se ci sono dei giorni in cui un dipendente non può lavorare in nessuna circostanza, puoi bloccare quei giorni configurandoli come Assenza non retribuita.

<div class="table__wrapper" markdown="1">

|                                          | Assenza retribuita | Assenza non retribuita |    Riunione di un giorno intero     |  Formazione  |
| --------------------------------------------- | :-----------------------: | :-------------------------: | :---------------------: | :---------------------: |
| **Tipo**                                          |          Assenza          |           Assenza           |         Meeting         |         Meeting         |
| Retribuita                                          |  <i class="fa fa-check">  |                             | <i class="fa fa-check"> | <i class="fa fa-check"> |
| Rispettare ore di riposo                       |                           |                             | <i class="fa fa-check"> |
| Pianificabile                                     |                           |                             |                         |
| Richiedibile in Me                                   |  <i class="fa fa-check">  |   <i class="fa fa-check">   |                         |
| Sostituibile                                   |                           |                             |                         |
| Scambiabile con scambio turni              |                           |                             |                         |
| Attività di un giorno intero                    |  <i class="fa fa-check">  |   <i class="fa fa-check">   |                         | <i class="fa fa-check"> |

</div>

Puoi anche utilizzare le assenze retribuite per compensare gli straordinari, oppure come attività retribuite quando {% link_new pianifichi le festività nazionali | best-practices/scheduling-public-holidays.md %}.<br>
L’attività Assenza non retribuita può essere utilizzata per determinare in modo flessibile i giorni in cui un dipendente non può lavorare per nessun motivo.