---
title: Aggiungere un'integrazione Genesys Engage
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Scopri come collegare il tuo sistema CMS Genesys Engage a injixo per importare dati.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Un'integrazione Genesys Engage è un'integrazione on-premise che importa la cronologia delle chiamate e i dati sugli stati degli agenti.

L’integrazione utilizza {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Aggiungere un'integrazione Genesys Engage

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nel riquadro **Genesys**, clicca su _Seleziona modello_{:.doc-button}.
4. Nella sezione **Genesys Engage**, clicca su _Aggiungi integrazione_{:.doc-button}.

## Configurare la nuova integrazione Genesys Engage

1. Inserisci un nome unico per la nuova integrazione che identifichi l’origine dei dati.
2. Installa e connetti {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Nella sezione **Credenziali database**, configura l’integrazione:
 - Seleziona il database adapter.
 - Inserisci l'host e la porta del tuo database.
 - Inserisci il nome utente e la password del tuo database.
 - Inserisci il nome del database ETL.
 - Inserisci il nome del database di configurazione.
4. Se vuoi importare i dati sugli stati degli agenti, spunta la casella **Importa i dati sugli stati degli agenti** nella sezione **Configurazione**.<br>
Nota: per importare i dati sugli stati degli agenti, devi prima {% link_new associare gli identificatori degli utenti esterni e le attività esterne | features/acd-integration/cloud/import-agent-status-data.md | #associare-gli-identificatori-degli-utenti-esterni-ai-dipendenti-in-injixo %}.
5. Clicca su _Salva integrazione_{:.doc-button}.

L’integrazione comincia a importare dati in injixo.

## Modificare un'integrazione Genesys Engage

Se i dettagli dell’integrazione, come, per esempio, le credenziali del server del database, cambiano, è possibile modificare e aggiornare la configurazione dell’integrazione. L’importazione dei dati continuerà utilizzando la configurazione aggiornata.
