---
title: Aggiungere un'integrazione Mitel
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Scopri come collegare il tuo sistema CRM Mitel a injixo per importare dati.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Un'integrazione Mitel è un'integrazione on-premise che importa la cronologia delle chiamate, delle email, delle chat e dei social media, e i dati sugli stati degli agenti.

L’integrazione utilizza {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Aggiungere un'integrazione Mitel

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nel riquadro di **Mitel** clicca su _Aggiungi integrazione_{:.doc-button}.

## Configurare la nuova integrazione Mitel

1. Inserisci un nome unico per la nuova integrazione che identifichi l’origine dei dati.
2. Installa e connetti {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Nella sezione **Impostazioni regionali**, seleziona il **Fuso orario ACD**.
4. Nella sezione **Credenziali database**, configura l’integrazione:
 - Inserisci l'host e la porta del tuo database.
 - Inserisci il nome utente e la password del tuo database.
5. Se vuoi importare i dati sugli stati degli agenti, spunta la casella **Importa i dati sugli stati agente** nella sezione **Configurazione**.<br>Nota: per importare i dati sugli stati degli agenti, devi prima {% link_new mappare gli identificatori degli utenti esterni e le attività esterne | features/acd-integration/cloud/import-agent-status-data.md %}.
6. Clicca su _Salva integrazione_{:.doc-button}.

L’integrazione comincia a importare dati in injixo. 

## Modificare un'integrazione Mitel

Se i dettagli dell’integrazione, come, per esempio, le credenziali del server del database, cambiano, è possibile modificare e aggiornare la configurazione dell’integrazione. L’importazione dei dati continuerà utilizzando la configurazione aggiornata.
