---
title: Aggiungere un'integrazione Cisco ICM
description: Scopri come connettere a injixo il tuo sistema Cisco ICM per importare dati.
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

L'integrazione Cisco ICM importa dati sull’aderenza in tempo reale. L’integrazione utilizza {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Aggiungere un'integrazione Cisco ICM

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nella scheda **Cisco ICM**, clicca su _Aggiungi integrazione_{:.doc-button}.

## Configurare l’integrazione Cisco ICM

1. Inserisci un **Nome** unico per la nuova integrazione che identifichi l’origine dei dati.
2. Nella sezione **injixo Cloud Link**, clicca sul **link di download** per il tuo sistema operativo.<br>
   > Nota
   >
   > Se hai già scaricato Cloud Link per un'altra integrazione, dovrai comunque scaricare da questa pagina la versione specifica per Cisco.
3. Installa e connetti {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.<br>
4. Nella sezione **Configurazione**, configura la nuova integrazione:

   - Inserisci una **Stringa di connessione** con i parametri richiesti per connetterti al tuo database Cisco:   
   `DRIVER={MS SQL Server};Server=myServerAddress;Database=myDataBase;UserId=myUsername;Password=myPassword;`
   - Seleziona il **Fuso orario del database** dal menu a tendina.
   - Inserisci il tuo **ID client** e la **Password** per Cisco ICM.
   - Inserisci il **Gateway periferico 1**.
   - (Facoltativo) Inserisci il **Gateway periferico 2**.

4. Clicca su _Salva integrazione_{:.doc-button}.

injixo inizierà a importare i dati sull’aderenza in tempo reale, ma i dati saranno visibili solo dopo aver mappato gli identificatori degli utenti esterni ai dipendenti.

## Associare gli utenti esterni ai dipendenti

1. Vai su _WFM > Administration > Scheduling > Dipendenti_{:.breadcrumbs}.
2. Associa gli identificatori degli utenti esterni ai dipendenti.
   > Nota
   >
   > Gli identificatori degli utenti esterni sono gli "Unified CCE Skill Target IDs" di Cisco.

Scopri di più su come {% link_new mappare gli identificatori degli utenti esterni | features/acd-integration/cloud/import-agent-status-data.md | #associare-gli-identificatori-degli-utenti-esterni-ai-dipendenti-in-injixo %} ai dipendenti in injixo.

## Associare gli stati degli agenti alle attività di injixo

1. Vai su _WFM > Administration > Scheduling > Attività_{:.breadcrumbs}.
2. Associa le attività di Cisco ICM alle attività di injixo.

Scopri come {% link_new associare le attività esterne | features/acd-integration/cloud/import-agent-status-data.md | #riassociare-le-attività-esterne %} alle attività in injixo.
