---
title: Aggiungere un’integrazione on-premise
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Connetti il tuo database on-premise con injixo per importare volumi di contatto, AHT, e dati sugli stati degli agenti.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Che cosa sono le integrazioni on-premise?

Le integrazioni on-premise utilizzano {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} per connettersi a un sistema sulla tua rete locale. Dopo la connessione, le integrazioni on-premise proveranno a importare fino a tre anni di dati storici.

## Aggiungere un’integrazione on-premise

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Seleziona il tuo sistema esterno e clicca su _Aggiungi integrazione_{:.doc-button}. Se il tuo sistema esterno esiste in diversi modelli, clicca su _Seleziona modello_{:.doc-button} e poi su _Aggiungi integrazione_{:.doc-button}.
3. Compila il modulo con le informazioni richieste. Per poter identificare facilmente l’origine dei dati, scegli un nome unico per l’integrazione.
4. Installa il {% link_new client di injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
5. Clicca su _Salva integrazione_{:.doc-button}.

{{ 1 | image: 'Integrazione Genesys Engage', '85%' }}

L’integrazione adesso importa in injixo i dati sui contatti. La prima importazione può richiedere parecchio tempo. Tutte le code provenienti dai sistemi connessi saranno automaticamente disponibili per essere associate nella {% link_new schermata di configurazione dei workload | features/forecast/injixo-forecast/manage-workloads.md | #creare-un-workload %} in injixo Forecast.

Se la tua integrazione supporta l’importazione dei dati sugli stati degli agenti, {% link_new associa gli identificatori degli utenti esterni e le attività | features/acd-integration/cloud/import-agent-status-data.md %}. L’integrazione potrà così importare i dati sugli stati degli agenti.
