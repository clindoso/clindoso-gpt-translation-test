---
title: Aggiungere un’integrazione cloud
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: false
description: Connetti il tuo sistema ACD cloud a injixo per importare dati.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Aggiungere un’integrazione Five9
    filepath: features/acd-integration/cloud/add-five9-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Che cosa sono le integrazioni cloud?

Le integrazioni cloud ottengono dati direttamente da un sistema cloud. injixo supporta molte integrazioni cloud.

## Aggiungere un’integrazione cloud

1. Vai su *Account > Integrazioni*{:.breadcrumbs}. La pagina include tutte le integrazioni disponibili.
2. Clicca su *Aggiungi integrazione*{:.doc-button} e inserisci le informazioni richieste. In questo esempio, imposteremo un’integrazione Five9, ma il processo per impostare le altre integrazioni cloud è simile.
3. Scegli un nome unico per l’integrazione. Il nome dovrebbe rispecchiare l’origine dei dati.
4. Inserisci il **nome utente** e la **password** di un utente che ha un ruolo di amministratore nel tuo account Five9.
5. Configura gli ulteriori dettagli specifici dell’integrazione (per esempio, la regione del tuo account Five9 e il modo di raggruppamento delle code).
6. Clicca su _Salva integrazione_{:.doc-button} per creare l’integrazione con le informazioni fornite.

{{ 1 | image: 'Integrazione Five9', '80%' }}

L’integrazione adesso importa dati in injixo. La prima importazione può richiedere fino a 15 minuti. Tutte le code provenienti dai sistemi connessi saranno automaticamente disponibili all’assegnazione nella {% link_new schermata di configurazione dei workload | features/forecast/injixo-forecast/manage-workloads.md | #creare-un-workload %} in injixo Forecast.

Se la tua integrazione supporta l’importazione di dati sugli stati agente, dovrai {% link_new mappare gli identificatori degli utenti esterni e le attività esterne | features/acd-integration/cloud/import-agent-status-data.md %} prima di poter importare i dati sugli stati agente.
