---
title: Aggiungere un’integrazione Interactive Intelligence CIC
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Impara a connettere Interactive Intelligence CIC a injixo per importare dati.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Un’integrazione Interactive Intelligence CIC è un’integrazione on-premise che importa i dati sull’aderenza in tempo reale.

L’integrazione utilizza {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Aggiungere un’integrazione Interactive Intelligence CIC

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nel riquadro **Genesys**, clicca su _Seleziona modello_{:.doc-button}.
4. Nella sezione **Interactive Intelligence CIC**, clicca su _Aggiungi integrazione_{:.doc-button}.

## Impostare un’integrazione Interactive Intelligence CIC

1. Inserisci un nome unico per l’integrazione.
   Il nome ti aiuterà a identificare la sorgente dei dati e a determinare a quali integrazioni appartengono le diverse code.<br>Esempio: CIC - Team assistenza clienti
2. Installa e connetti {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Nella sezione **Configurazione**, configura la nuova integrazione:
 - **Fuso orario**: seleziona il fuso orario del tuo sistema ACD dal menu a tendina.
 - **Indirizzi del server dell’ACD**: inserisci il nome DSN or l’indirizzo IP e la porta del tuo ACD, separati dai due punti, per esempio: acd.example.com:8080.<br>Per inserire gli indirizzi di diversi ACD, separali con le virgole.
4. Clicca su _Salva integrazione_{:.doc-button} per creare l’integrazione.

L’integrazione comincia a importare dati in injixo. Per importare i dati sugli stati degli agenti, devi {% link_new associare gli identificatori degli utenti esterni e le attività | features/acd-integration/cloud/import-agent-status-data.md %} dopo aver configurato l’integrazione Interactive Intelligence CIC.

## Modificare un’integrazione Interactive Intelligence CIC

Se i dettagli dell’integrazione, come, per esempio, la porta dell’ACD, cambiano, è possibile modificare e aggiornare la configurazione dell’integrazione. L’importazione dei dati continuerà utilizzando la configurazione aggiornata.
