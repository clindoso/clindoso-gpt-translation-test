---
title: Impostare la configurazione di base
description: Dati di configurazione necessari per creare una pianificazione.
redirect_from:
  - /it/configuration-hints/
  - /it/quickstart-base-configuration/
redirect_reason: Updated filename on 24 July 2023
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
---

Prima di poter iniziare a pianificare, è necessario impostare la configurazione di base di injixo. Alcuni degli elementi di configurazione di base sono indispensabili per creare una pianificazione, mentre altri sono facoltativi, e dipendono dai {% link_new metodi di pianificazione | features/scheduling/scheduling-methods.md %} che vuoi seguire.

## Ordine della configurazione

Consigliamo di configurare gli elementi di configurazione nell'ordine presentato qui di seguito. Gli elementi di configurazione sono interdipendenti, e alcuni possono essere assegnati ad altri. Segui i link nella tabella per avere più informazioni su ogni elemento della configurazione e imparare a configurarli.
Ogni configurazione è unica, e l’ordine migliore per la tua organizzazione potrebbe essere diverso da quello proposto qui. Utilizza questo articolo come elenco dei passaggi necessari per aiutarti durante l’onboarding. In caso di dubbi, contatta il tuo consulente.

### Elementi della configurazione indispensabili

La tabella di seguito offre una panoramica degli elementi di configurazione che sono indispensabili in injixo, a prescindere dal metodo di pianificazione che vuoi seguire.

<table>
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 75%;">
  </colgroup>
  <thead>
    <tr>
      <th>Elemento di configurazione</th>
      <th>Descrizione</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{% link_new Qualifiche | features/administration/work-with-skills.md %}</td>
      <td>Le qualifiche rappresentano le competenze dei tuoi dipendenti. Se assegni delle qualifiche ai dipendenti, li rendi qualificati allo svolgimento di certe attività. In injixo, è necessario assegnare qualifiche alle attività che possono essere svolte solo da alcuni dipendenti. Non è necessario aggiungere qualifiche alle attività che possono essere svolte da tutti.</td>
    </tr>
    <tr>
      <td>{% link_new Attività | features/administration/activities.md %}</td>
      <td>Le attività sono i compiti, le riunioni e i permessi che pianifichi e che sono inclusi nei report della tua azienda.<br> Le attività vengono aggiunte ai modelli di orario e alle unità di pianificazione.</td>
    </tr>
    <tr>
      <td>{% link_new Modelli di orario | features/administration/daymodels/daymodel-creation.md %}</td>
      <td>I modelli di orario sono sequenze di turni. I modelli di orario definiscono l’ora di inizio e di fine di un turno, e il numero di ore lavorative giornaliere di un dipendente. Contengono tutte le attività di presenza, pausa e assenza di un turno.<br>I modelli di orario vengono assegnati alle unità di pianificazione. Possono anche essere raggruppati in modelli settimanali.</td>
    </tr>
    <tr>
      <td>{% link_new Unità di pianificazione | features/administration/create-and-manage-planning-units.md %}</td>
      <td>Le unità di pianificazione rappresentano i luoghi (reali o virtual) in cui si trovano i tuoi dipendenti. Vengono utilizzate per raggruppare le persone per la pianificazione.</td>
    </tr>
    <tr>
      <td>{% link_new Contratti | features/administration/create-contracts.md %}</td>
      <td>I contratti contengono informazioni sugli accordi contrattuali dei dipendenti, incluso il numero previsto, il numero massimo e il numero minimo di ore lavorative al giorno, alla settimana, o al mese.<br>I contratti vengono assegnati ai dipendenti.</td>
    </tr>
    <tr>
      <td>{% link_new Dipendenti | features/administration/employee-overview.md %}</td>
      <td>In Dipendenti inserisci le informazioni su ogni dipendente che pianifichi. Sulla base di tali informazioni e delle assegnazioni (modelli di orario, unità di pianificazione, contratti, qualifiche), injixo sa quando e su quali attività i tuoi dipendenti possono lavorare.</td>
    </tr>
  </tbody>
</table>


### Elementi della configurazione facoltativi

La tabella di seguito offre una panoramica degli elementi di configurazione che hai la possibilità di configurare in injixo, in base alla struttura della tua organizzazione e al metodo di pianificazione che vuoi seguire.

<table>
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 75%;">
  </colgroup>
  <thead>
    <tr>
      <th>Elemento di configurazione</th>
      <th>Descrizione</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{% link_new Rotazioni | features/administration/shift-sequences.md %} (necessarie per la pianificazione fissa)</td>
      <td>Una rotazione è un insieme di modelli di orario o di attività che si ripete regolarmente.<br>Le rotazioni vengono assegnate ai dipendenti.</td>
    </tr>
    <tr>
      <td>{% link_new Gruppi di selezione | features/administration/selections.md %}</td>
      <td>Con i gruppi di selezione puoi filtrare e raggruppare i dipendenti, o pianificarli, in base a qualsiasi criterio desideri, per esempio in base al tipo di contratto, o in base al team di appartenenza.<br> I gruppi di selezione vengono assegnati ai dipendenti.</td>
    </tr>
    <tr>
      <td>{% link_new Modelli di pianificazione e modelli settimanali | features/administration/work-time-pattern-models.md %}</td>
      <td>I modelli di pianificazione e i modelli settimanali ti aiutano a organizzare i turni garantendo una distribuzione equa dei turni (a rotazione) tra i dipendenti. I modelli di pianificazione contengono almeno un modello settimanale. I modelli settimanali raggruppano i turni di lavoro in base a parametri come l'orario di inizio, la durata del turno o le attività. Contengono insiemi di modelli di orario.<br>I modelli settimanali vengono assegnati ai modelli di pianificazione. I modelli di pianificazione vengono assegnati ai dipendenti.</td>
    </tr>
    <tr>
      <td>{% link_new Calendari pianificativi e tipi di giorno | features/administration/configure-planning-calendars.md %}</td>
      <td>I calendari pianificativi contengono giorni con orari lavorativi e fabbisogno di personale diversi dai soliti (per esempio, giorni di campagne di marketing o festività nazionali). Questi giorni speciali vengono configurati come tipi di giorno. In questo modo, verranno presi automaticamente in considerazione durante la pianificazione, senza nessun altro intervento manuale.<br> I calendari pianificativi vengono assegnati alle unità di pianificazione.</td>
    </tr>
  </tbody>
</table>


## E adesso?

Congratulazioni! È tutto pronto per {% link_new creare la prima previsione | getting-started/calculate-a-forecast.md %}. Buona pianificazione!
