---
title: Aggiungere un’integrazione Freshdesk Contact Center
description: Impara come collegare il tuo sistema CRM Freshdesk Contact Center a injixo per importare dati.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Un'integrazione Freshdesk Contact Center è un'integrazione cloud che importa la cronologia delle chiamate e i dati sull’aderenza in tempo reale.

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Aggiungere un’integrazione Freshdesk Contact Center 

Per aggiungere una nuova integrazione di Freshdesk Contact Center in injixo, devi avere un account Freshdesk Contact Center del tipo Pro o Enterprise.

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nel riquadro **Freshworks**, clicca su _Seleziona modello_{:.doc-button}.
4. Nella sezione **Freshdesk Contact Center**, clicca su _Aggiungi integrazione_{:.doc-button}.

## Configurare un’integrazione Freshdesk Contact Center

1. Inserisci un nome unico per l’integrazione che identifichi l’origine dei dati.
2. Nella sezione **Credenziali**, inserisci il nome completo del tuo dominio Freshdesk Contact Center, incluso il sottodominio, per esempio: esempio.freshcaller.com.
3. Vai su Freshdesk Contact Center e copia una chiave API valida di un utente con il ruolo di Account Administrator.
4. Torna su injixo e incolla la chiave API nel campo **API key**.
5. Seleziona la [strategia di raggruppamento per le code importate](#nomi-delle-code-in-base-alla-strategia-di-raggruppamento).
6. Clicca su _Salva integrazione_{:.doc-button}. 

Dopo aver salvato la configurazione, è possibile accedere alla sezione **Installare l’app injixo**.

## Installare l’app injixo

1. Nella sezione **Installare l’app injixo**, genera e copia la **chiave API di injixo**.
2. Imposta l’app injixo necessaria nel tuo account Freshdesk nel [Freshworks marketplace](https://www.freshworks.com/apps/freshcaller/injixo_1/).
3. Nella pagina di installazione dell’app injixo, incolla la chiave API che hai copiato.
4. Per importare dati in tempo reale, spunta la casella **Export real-time agent status data** nella pagina di installazione dell’app injixo del Freshworks marketplace.

## Nomi delle code in base alla strategia di raggruppamento

Durante l’importazione dei dati, la strategia di raggruppamento influisce sul nome delle code che vengono create in injixo:

| Strategia di raggruppamento   | Nome coda                               | Esempio           |
| ------------------- | ---------------------------------------- | ----------------- |
| Numero di telefono        | Numero di telefono                             | +49123456789      |
| Instradamento (team/agente) | Nome del team                                | Team supporto tecnico |
| Instradamento (team/agente) | Nome dell’agente (se il nome del team non è assegnato) | Agente 1           |

Per le chiamate che non hanno nessun gruppo in Freshdesk Contact Center, il nome della coda è Undefined_Queue.
