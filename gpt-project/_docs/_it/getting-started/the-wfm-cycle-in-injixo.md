---
title: Il ciclo WFM in injixo
description: Scopri in che modo injixo può accompagnarti lungo tutto il ciclo WFM
product_label:
  - essential
  - advanced
  - enterprise
  - classic
---

L’obiettivo del workforce management (WFM) è ottimizzare la gestione del personale per raggiungere gli obiettivi aziendali e il servizio di livello desiderato. injixo ti aiuta a essere più efficiente in tutte le fasi del ciclo WFM.

  {{ 1 | image: "Ciclo WFM: previsione, programmazione, pianificazione, gestione intraday, analisi", '60%' }}

- Previsione: prevedi il carico di lavoro a breve, medio e lungo termine.
- Programmazione: imposta le strategie di assunzione, budget e formazione per il futuro.
- Pianificazione: crea le pianificazioni migliori per i dipendenti e per le esigenze della tua organizzazione.
- Gestione intraday: adatta le pianificazioni agli imprevisti in tempo reale.
- Analisi: comprendi, prevedi e migliora le prestazioni della tua organizzazione.

In questo articolo troverai una panoramica dei modi in cui injixo può accompagnarti lungo tutte le fasi del ciclo WFM.
Il primo passo è fornire a injixo i dati necessari per generare una previsione affidabile. Per farlo, è necessario configurare un'integrazione con i tuoi sistemi di distribuzione automatica delle chiamate (ACD) o di gestione delle relazioni con i clienti (CRM).

È la prima volta che ti occupi di workforce management? Scopri i concetti chiave e le definizioni nel nostro [glossario](https://help.injixo.com/it/glossary/overview).

## 1. Previsione

### Impostare un’integrazione

Per prevedere il carico di lavoro che la tua organizzazione affronterà in qualsiasi momento futuro, injixo deve accedere ai dati sui contatti e/o ai dati sugli stati degli agenti provenienti da sistemi esterni (per esempio, sistemi ACD o CRM). Per consentire a injixo di importare e elaborare questi dati, devi {% link_new integrare i tuoi sistemi esterni con injixo | features/acd-integration/cloud/how-integrations-work.md %}. injixo offre integrazioni native, specifiche per alcuni sistemi, e integrazioni universali. A seconda dell’integrazione, injixo importa dati ogni 15, 30, o 60 minuti (importazione di dati storici), oppure entro pochi secondi (importazione di dati in tempo reale). 

Dopo aver aggiunto un’integrazione, questa invierà dati a injixo, automaticamente e in modo continuo.
I dati sui contatti importati vengono archiviati in code, che sono sempre associate a un canale. Le code sono indispensabili per creare dei workload su cui basare le tue previsioni.

Puoi configurare le integrazioni in _Account > Integrazioni_{:.breadcrumbs}.

### Creare un workload  

Per utilizzare injixo Forecast, devi prima creare un {% link_new workload | features/forecast/injixo-forecast/manage-workloads.md | #creare-un-workload %} utilizzando le code importate dall’integrazione. I workload contengono tutti i dati storici e le relative previsioni. Per creare un workload, il tuo sistema ACD deve essere collegato correttamente e le code importate devono essere disponibili.

Puoi creare i workload in _Forecast > Workloads_{:.breadcrumbs}. 

### Generare una previsione

{% link_new injixo Forecast | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %} combina i dati storici con gli algoritmi più adatti per generare previsioni di alta qualità per periodi lunghi fino a 365 giorni.

Ogni nuova importazione di dati aggiorna la previsione generata. Puoi anche {% link_new aggiungere degli eventi | features/forecast/injixo-forecast/events-and-holidays.md %} che influiranno sulla previsione.

### Calcolare il fabbisogno di personale

Dopo aver generato una previsione, puoi {% link_new calcolare il fabbisogno di personale | features/forecast/injixo-forecast/staff-requirement.md %}, cioè il numero di dipendenti che devono essere pianificati per far fronte al carico di lavoro previsto. Puoi utilizzare diversi {% link_new metodi di calcolo | best-practices/requirement-scripts.md %} per calcolare il tuo fabbisogno di personale. I metodi di calcolo tengono conto di fattori come il livello di servizio desiderato, il tempo di risposta desiderato, i cali di efficienza (shrinkage), etc. Se è necessario, è possibile anche definire il fabbisogno di personale di personale costante senza previsioni.

Puoi utilizzare il fabbisogno di personale durante il processo di pianificazione per creare pianificazioni ottimizzate per specifici intervalli di tempo, unità di pianificazione e attività.

## 2. Programmazione

Utilizza i dati generati da injixo Forecast per confrontare il tuo fabbisogno di personale con le risorse attualmente disponibili. Le previsioni a lungo termine ti consentono di prendere tempestivamente le decisioni migliori, per esempio riguardo le richieste di permesso, il momento migliore per pubblicare un annuncio di lavoro, o la scelta del tipo di formazione necessaria per preparare i dipendenti ai progetti futuri.

## 3. Pianificazione

### Creare le pianificazioni

Dopo aver calcolato il fabbisogno di personale, injixo mette a tua disposizione diversi {% link_new metodi di pianificazione | features/scheduling/scheduling-methods.md %}. Puoi utilizzarli singolarmente o in combinazione per pianificare i dipendenti in modo da soddisfare al meglio le esigenze della tua organizzazione.

In _Plan > Schedules_{:.breadcrumbs}, puoi configurare regole di pianificazione e vincoli per rispettare le normative sul lavoro, gli accordi contrattuali e le preferenze dei dipendenti.

injixo offre diverse funzionalità di pianificazione, come la {% link_new pianificazione ottimizzata | features/scheduling/schedules/schedules-optimized-schedules.md %}, la {% link_new notifica delle modifiche alla pianificazione | features/scheduling/schedules/schedules-notify-scheduling-changes.md %} o la possibilità di {% link_new consentire ai dipendenti di scambiare turni | features/scheduling/planning-periods/enable-employees-to-swap-shifts.md %} con i colleghi.

### Pianificare le assenze

{% link_new Ferie/Assenze | features/scheduling/time-off/vacation-absences-management.md %} ti consente di gestire i saldi dei permessi e le richieste di ferie, permessi per motivi personali, congedi per malattia e assenze di altri tipi. I dipendenti possono presentare le richieste di permesso tramite {% link_new injixo Me | features/injixo-me/use-injixo-me/explore-injixo-me.md %}. Puoi approvare o rifiutare le richieste in base al fabbisogno di personale, alla disponibilità dei dipendenti, e a eventuali regole o vincoli predefiniti.

Per configurare le assenze, vai su _Plan > Ferie/Assenze_{:.breadcrumbs}.

## 4. Gestione intraday

In {% link_new Aderenza Intraday | features/intraday/adherence-intraday.md %}, puoi confrontare le attività pianificate con le attività effettivamente svolte e identificare eventuali discrepanze. Puoi visualizzare statistiche dettagliate e un punteggio di aderenza.

È possibile fare lo stesso in tempo reale in {% link_new Aderenza in Tempo Reale | features/intraday/real-time-adherence.md %}, che offre una panoramica completa, opzioni per filtrare i dati e un punteggio di aderenza target regolabile.

Con queste informazioni, puoi apportare modifiche dell'ultimo minuto alla pianificazione per fronteggiare eventi imprevisti ed evitare sia carenze che eccedenze di personale.

## 5. Analisi

injixo ti offre la possibilità di {% link_new creare dashboard | features/monitoring/dashboards/dashboards-overview.md %} con grafici per visualizzare meglio diversi indicatori, per esempio il confronto tra il fabbisogno di personale e la copertura effettiva, o quello tra le chiamate in arrivo previste e quelle effettive, per diversi periodi.

injixo può anche {% link_new generare diversi tipi di report | features/reporting/standard-reports/creating-reports.md %} che ti aiutano a monitorare gli indicatori più importanti, come la capacità in base al tipo di contratto, le ore lavorate per unità di pianificazione, o la panoramica delle ferie.
