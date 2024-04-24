---
title: Come funzionano le integrazioni?
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Scopri come funzionano le integrazioni, quali integrazioni esistono, e come aggiungerle o eliminarle.
promote-service: acd-integration-support
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Per aiutarti nel workforce management, injixo ha bisogno di importare dati sui contatti e sugli stati degli agenti da sistemi esterni, come il sistema di distribuzione automatica delle chiamate (sistema ACD) o il sistema CRM. Integrare il sistema ACD e/o il sistema CRM in injixo consente di ricevere i dati e di processarli.

injixo offre integrazioni native, specifiche per alcuni sistemi, e integrazioni universali, per sistemi cloud e sistemi on-premise. A seconda dell’integrazione, injixo importa dati ogni 15, 30, o 60 minuti (importazione di dati storici), oppure entro pochi secondi (importazione di dati in tempo reale).

## Modi di consegna

Il modo di consegna di un’integrazione determina il modo in cui injixo si connette al sistema esterno:

- Le integrazioni cloud si connettono a un sistema cloud, per esempio Five9 o Vonage, e importano i dati direttamente.
- Le integrazioni on-premise utilizzano {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} per connettersi a un sistema nella tua rete locale, per esempio, Genesys Engage o Sikom. Una volta stabilita la connessione, le integrazioni on-premise cominceranno a importare fino a tre anni di dati storici.

## Integrazioni specifiche e integrazioni universali

Le integrazioni specifiche del fornitore sono personalizzate per il sistema specifico e sono l’opzione consigliata. Se non è disponibile un'integrazione specifica del fornitore, è possibile utilizzare una delle integrazioni universali.

- Database: integrazione on-premise che utilizza una interrogazione (o query) SQL per leggere dati da un database.
- CSV: integrazione basata su file per importare file in formato CSV con injixo Cloud Link.
- API injixo: integrazione cloud necessaria per l’invio di richieste HTTP all’API injixo.

## Quali dati vengono importati?

A seconda dell’integrazione, injixo importa dati sui contatti o dati sugli stati degli agenti, o entrambi.

- I dati sui contatti (chiamate, chat, social media, ticket, email, documenti) comprendono i volumi di contatti che sono stati ricevuti e ai quali è stata data risposta, e il tempo medio di gestione. Questi dati sono utilizzati per generare le previsioni.
- I dati sugli stati degli agenti (login, logout, elaborazione post-chiamata, pause, etc.) contengono informazioni sulle attività dei dipendenti, come, per esempio, quando passano da un’attività a un’altra. Questi dati sono utilizzati per la gestione intraday.

## Aggiungere un’integrazione

Per imparare a configurare un’integrazione, leggi i seguenti articoli:

- {% link_new Aggiungere un’integrazione cloud | features/acd-integration/cloud/add-cloud-integration.md %}
- {% link_new Aggiungere un’integrazione on-premise | features/acd-integration/cloud/add-on-premise-integration.md %}
- {% link_new Aggiungere un’integrazione CSV | features/acd-integration/cloud/add-csv-integration.md %}
- {% link_new Aggiungere un’integrazione database | features/acd-integration/cloud/add-database-integration.md %}
- {% link_new Importare dati con l’API injixo | features/acd-integration/cloud/import-data-with-injixo-api.md %}

Dopo aver aggiunto un’integrazione, questa comincerà a inviare dati a injixo.

I dati sui contatti vengono importati automaticamente. Per lavorare con i dati sui contatti, aggiungi delle code importate a un (nuovo) workload per {% link_new generare una previsione | getting-started/calculate-a-forecast.md %}. In seguito, calcola il fabbisogno di personale e crea la pianificazione.

> Prerequisiti per visualizzare i dati sugli stati degli agenti
>
> Per vedere i dati sugli stati degli agenti nel modulo Intraday, {% link_new mappa gli ID degli utenti e delle attività esterne | features/acd-integration/cloud/import-agent-status-data.md %}. Per farlo, sospendi l’importazione dei dati dell’integrazione.

## Sospendere l’importazione dei dati

La mappatura delle attività viene sovrascritta dall’integrazione in corso. Per non perdere la mappatura e per evitare che alcune attività vengano duplicate, sospendi l’importazione dei dati da parte dell’integrazione cliccando sull’icona Sospendi l'importazione{% icon pause_circle | icon-only %} accanto all’integrazione nella pagina della panoramica.

Per riprendere l’importazione dei dati al termine della mappatura, clicca sull’icona Riprendi l'importazione{% icon play_circle | icon-only %}. I dati mancanti verranno reimportati.

## Eliminare un’integrazione

L’eliminazione di un’integrazione non elimina i dati importati. Le code restano assegnate ai workload. Non è possibile eliminare le code create da un’integrazione.

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Clicca sull’{% icon pencil %} accanto all’integrazione che vuoi eliminare.
3. Nell’angolo in basso a destra, clicca su _Elimina integrazione_{:.doc-button}.
4. Nella finestra di conferma, clicca su _Sì, elimina_{:.doc-button}.
