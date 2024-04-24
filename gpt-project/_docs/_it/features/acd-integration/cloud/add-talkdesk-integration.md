---
title: Aggiungere un’integrazione Talkdesk
description: Scopri come connettere il tuo sistema ACD Talkdesk a injixo per importare dati.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
---

Un'integrazione Talkdesk è un'integrazione cloud che importa la cronologia delle chiamate e i dati sugli stati degli agenti.

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Aggiungere un’integrazione Talkdesk

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.  
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nella sezione **Talkdesk**, clicca su _Aggiungi integrazione_{:.doc-button}.
4. Inserisci un nome unico per l’integrazione che identifichi l’origine dei dati.
5. Nella sezione **Credenziali utente**, compila il modulo con le informazioni su Talkdesk:

   - Inserisci il nome del tuo account Talkdesk.
   - Inserisci il Client ID e il Client secret di un client Talkdesk OAuth.

     > Per il Client ID e il Client secret, [crea un nuovo client OAuth](https://docs.talkdesk.com/docs/creating-a-new-oauth-client) in Talkdesk.
     >
     > Puoi anche utilizzare un client OAuth esistente che è stato configurato come segue:
     >
     > - Tipo di concessione: client-credentials
     > - Ambiti: data-reports:read e data-reports:write

6. Nella sezione **Configurazione**, seleziona la regione del tuo account.

7. Clicca su _Salva integrazione_{:.doc-button}.  
   L’integrazione testerà la connessione e riporterà eventuali problemi.  
   Al termine dei controlli, l’integrazione comincerà a importare dati in injixo.

<!-- ## Talkdesk Data in injixo -->

## E adesso che cosa succede?

Dopo che i dati sulle chiamate sono stati importati nelle code, potrai creare il primo workload. Per ulteriori informazioni sulla configurazione degli stati agente, leggi gli articoli collegati.
