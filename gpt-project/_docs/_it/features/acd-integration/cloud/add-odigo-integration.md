---
title: Aggiungere un'integrazione Odigo
description: Scopri come connettere il tuo sistema ACD Odigo a injixo per importare dati.
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

L'integrazione Odigo importa gli stati degli agenti in tempo reale e i dati sull’aderenza in tempo reale.

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Aggiungere un'integrazione Odigo

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nel riquadro di **Odigo** clicca su _Aggiungi integrazione_{:.doc-button}.
4. Inserisci un nome unico per l’integrazione che identifichi l’origine dei dati.
5. (Facoltativo) Configura l’importazione dei dettagli sugli stati degli agenti in pausa:
- Spunta la casella **Importa i dettagli sugli stati degli agenti in pausa**.<br>Durante l'importazione degli stati di pausa, injixo includerà informazioni sul tipo di pausa.<br>Nota: se spunti questa casella, dovrai anche aggiornare la {% link_new mappatura delle attività | features/acd-integration/cloud/import-agent-status-data.md | #riassociare-le-attività-esterne %}.
- Inserisci la tua URL di Odigo che include l’ID del tenant.
- Inserisci il nome utente e la password per il servizio web.
6. Clicca su _Salva integrazione_{:.doc-button}.

## Configurare l’integrazione Odigo

1. Nella sezione **Genera token URL injixo**, clicca su _Generare_{:.doc-button}.
2. Copia il token URL di injixo negli appunti.<br>
Il token URL injixo viene mostrato solo una volta. Se non riesci a completare subito la configurazione, conservalo in un luogo sicuro, per esempio un gestore di password.
3. Nella sezione Amministrazione dell'interfaccia di Odigo, attiva l'invio di notifiche a un server esterno. Per farlo, contatta Odigo.
4. Incolla il **token URL injixo** che hai copiato come URL di notifica.
5. Salva le impostazioni in Odigo e torna a injixo.

Per attivare l'integrazione, è necessario riavviare il server. Per farlo, contatta Odigo.<br>
injixo inizierà a importare i dati sull’aderenza in tempo reale, ma i dati saranno visibili solo dopo aver mappato gli identificatori degli utenti esterni ai dipendenti.

## Associare gli utenti esterni ai dipendenti

1. Vai su _WFM > Administration > Scheduling > Dipendenti_{:.breadcrumbs}.
2. Mappa gli identificatori degli utenti esterni ai dipendenti.

Scopri come {% link_new associare gli identificatori degli utenti esterni | features/acd-integration/cloud/import-agent-status-data.md | #associare-gli-identificatori-degli-utenti-esterni-ai-dipendenti-in-injixo %} ai dipendenti.

## Associare gli stati degli agenti alle attività di injixo

1. Vai su _WFM > Administration > Scheduling > Attività_{:.breadcrumbs}.
2. Associa le attività di Odigo alle attività di injixo.

Scopri come {% link_new associare le attività esterne | features/acd-integration/cloud/import-agent-status-data.md | #riassociare-le-attività-esterne %} alle attività in injixo.
