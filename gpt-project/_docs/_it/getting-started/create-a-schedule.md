---
title: Creare una pianificazione
description: Segui i passaggi necessari per creare una pianificazione
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
related_articles:
  - overwrite_title: Risolvere i problemi di ottimizzazione
    filepath: best-practices/resolve-optimization-issues.md
  - overwrite_title: Fare copie di backup e confrontare le pianificazioni
    filepath: best-practices/why-level-copy.md
  - overwrite_title: Che cos'è Meetings?
    filepath: features/scheduling/meetings/meetings-overview.md
  - overwrite_title: Pianificare attività extra
    filepath: features/scheduling/schedules/schedules-extra-activities.md
  - overwrite_title: Sostituire un'attività in blocco
    filepath: features/scheduling/schedules/schedules-replace-activities.md
  - overwrite_title: Pianificare le festività nazionali
    filepath: best-practices/scheduling-public-holidays.md
redirect_from:
  - /it/quickstart-scheduling/
redirect_reason: Updated filename on 27 July 2023
---

La creazione delle pianificazioni è una parte essenziale del {% link_new ciclo del WFM | getting-started/the-wfm-cycle-in-injixo.md %}. Le pianificazioni contengono i turni e le attività programmate per i dipendenti.  

Utilizza questo articolo come riferimento per i passaggi da seguire durante l’onboarding.

Nota: in injixo Essential WFM, non è possibile fare un backup delle richieste di permesso o della pianificazione definitiva.

## Prerequisiti

Prima di creare una pianificazione, assicurati di aver {% link_new avere impostato la configurazione di base | getting-started/set-up-base-configuration.md %} e {% link_new  calcolato una previsione | getting-started/calculate-a-forecast.md %} correttamente. 

## Ordine della configurazione

Consigliamo di configurare gli elementi di configurazione nell'ordine presentato qui di seguito. Ogni configurazione è unica, e l’ordine migliore per la tua organizzazione potrebbe essere diverso da quello proposto qui. In caso di dubbi, contatta il tuo consulente.

## Configurare i permessi

I dipendenti possono richiedere permessi in injixo Me. Per configurare il tempo libero, vai su _Plan > Ferie/Assenze_{:.breadcrumbs}:

1. Inserisci il totale delle {% link_new ferie spettanti | features/scheduling/time-off/vacation-entitlement.md %} dei tuoi dipendenti per l’anno in corso.
2. Crea un {% link_new periodo di permesso | features/scheduling/time-off/time-off-periods.md %} e pubblicalo. Un periodo di permesso definisce l'intervallo di tempo in cui i dipendenti possono richiedere ferie e assenze di altri tipi. I dipendenti riceveranno una notifica in injixo Me e potranno iniziare a creare richieste di permesso per quel periodo.

## Inserire attività del tipo Malattia o Assenza

In {% link_new Schedules | features/scheduling/schedules/schedules-overview.md %} e nel {% link_new Centro dei turni | features/scheduling/shiftcenter/shift-center-overview.md %}, puoi gestire la pianificazione del tuo team. Inserisci nella pianificazione tutte le {% link_new attività | features/administration/activity-types-and-properties.md | #tipi-di-attività %} del tipo Assenza o Malattia di cui sei già a conoscenza.

## Gestire le richieste di permesso

In _Plan > Ferie/Assenze_{:.breadcrumbs}, approva o rifiuta le {% link_new richieste in sospeso | features/scheduling/time-off/vacation-absences-management.md %}.

> Crea una copia di backup della pianificazione attuale in un altro livello
>
> Utilizza {% link_new Copia contenuto livello | features/scheduling/schedules/schedules-copy-level-content.md %} per salvare una copia della pianificazione. In questo modo, se cancelli la pianificazione e ricominci dall’inizio, non perderai le richieste di permesso approvate e le assenze che sono già state inserite.

## Creare una pianificazione

In {% link_new Schedules | features/scheduling/schedules/schedules-overview.md %}, nel {% link_new Centro dei turni | features/scheduling/shiftcenter/shift-center-overview.md %} o in {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %}, verifica che il {% link_new fabbisogno di personale | features/forecast/injixo-forecast/staff-requirement.md | #view-calculated-staff-requirements %} sia impostato correttamente per le tue attività.

1. Inserisci {% link_new rotazioni | features/scheduling/capacity/capacity-insert-shift-sequences.md %} per i tuoi dipendenti.
2. Configura e applica ulteriori {% link_new metodi di pianificazione | features/scheduling/scheduling-methods.md %} per completare la pianificazione.
3. Lancia l’{% link_new ottimizzazione delle mansioni | features/scheduling/schedules/schedules-job-optimization.md %}. Puoi saltare questo passaggio se {% link_new crei una pianificazione ottimizzata | features/scheduling/schedules/schedules-optimized-schedules.md %}.

Suggerimento: se stai creando una pianificazione di prova, puoi utilizzare {% link_new Svuota livelli | features/scheduling/schedules/schedules-empty-levels.md %}. Prima di ogni test, copia di nuovo le assenze salvate e le richieste di permesso nel livello Piano.

## Fare una copia di backup della pianificazione definitiva

Prima di apportare {% link_new modifiche manuali | features/scheduling/shiftcenter/modify-items.md %} alla pianificazione originale, {% link_new salva una copia di backup | features/scheduling/schedules/schedules-copy-level-content.md %} nel livello Stato effettivo. In questo modo potrai confrontare la qualità della pianificazione originale con quella delle versioni successive.

## Pubblicare la pianificazione e consentire lo scambio di turni

1. Crea un periodo di pianificazione per {% link_new permettere ai dipendenti di visualizzare la loro pianificazione | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %} in injixo Me.
2. (Facoltativo) {% link_new Consenti ai dipendenti di scambiarsi i turni | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}.  
    Per impostazione predefinita, devi {% link_new visualizzare e approvare gli scambi in sospeso | features/scheduling/view-approve-shift-swap-requests.md %}, ma puoi permettere gli scambi automatici tra dipendenti con l’impostazione _48152_{:.id-label} **Modalità di scambio**.
3. Invia ai dipendenti l’articolo {% link_new Esplorare injixo Me | features/injixo-me/use-injixo-me/explore-injixo-me.md %}.
