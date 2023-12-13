---
title: Aggiungere un'integrazione Genesys Cloud
description: Scopri come collegare il tuo sistema CRM Genesys Cloud a injixo per importare dati.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Un'integrazione Genesys Cloud è un'integrazione cloud che importa la cronologia delle chiamate, delle email e delle chat, gli stati degli agenti e i dati sull’aderenza in tempo reale.

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Aggiungere un'integrazione Genesys Cloud

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nel riquadro **Genesys**, clicca su _Seleziona modello_{:.doc-button}.
4. Nella sezione **Genesys Cloud**, clicca su _Aggiungi integrazione_{:.doc-button}.

## Configura l'integrazione Genesys Cloud

1. Inserisci un nome unico per la nuova integrazione che identifichi l’origine dei dati.
Nella sezione **Credenziali API**, copia e incolla l’API key e l’API secret di Genesys Cloud.
3. Nella sezione **Configurazione**, seleziona la regione del tuo account.
4. (Facoltativo) Spunta la casella **Importa stati agente On Queue dettagliati**.<br>Lo stato dell'agente «on-queue» include diversi stati, per esempio «communication», «interacting», «idle»,«not responding». Durante l'importazione degli stati degli agenti, injixo differenzierà tra gli stati individuali raggruppati sotto «on-queue».
5. Clicca su _Salva integrazione_{:.doc-button}.
