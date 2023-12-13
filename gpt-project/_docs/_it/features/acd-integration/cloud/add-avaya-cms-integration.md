---
title: Aggiungere un’integrazione Avaya CMS
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Scopri come connettere il tuo database Avaya per importare dati.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Un’integrazione Avaya CMS è un’integrazione on-premise che importa dati sulle chiamate e sugli stati degli agenti.

L’integrazione utilizza {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Aggiungere un’integrazione Avaya CMS

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nel riquadro di **Avaya CMS** clicca su _Aggiungi integrazione_{:.doc-button}.

## Impostare una nuova integrazione Avaya CMS

1. Inserisci un nome unico per l’integrazione.
   Il nome ti aiuterà a identificare la sorgente dei dati e a determinare a quali integrazioni appartengono le diverse code.<br>Esempio: Avaya integration - Customer Support Team.
1. Installa e connetti {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
1. Nella sezione **Configurazione**, configura la nuova integrazione:
 - Inserisci la [stringa di connessione](#stringa-di-connessione) che definisce i parametri necessari per connettersi al database del CMS. 
 - Seleziona il fuso orario del database dal menu a tendina.
 - Spunta la casella **Importa i dettagli sugli stati degli agenti** per aggiungere le informazioni sulle skills (profilo dell’agente) e sugli splits (indirizzamento delle chiamate) agli stati agente importati.
 - Per importare i dati sugli stati degli agenti in tempo reale, spunta la casella **Importa i dati in tempo reale**. In questo caso, inserisci un numero di porta alla voce **Porta**.<br>
   injixo Cloud Link aprirà un socket TCP in ascolto sulla porta specificata. Il servizio Avaya Generic RTA si collegherà a questa porta e inizierà a trasmettere i dati sugli stati degli agenti in tempo reale. Il servizio Avaya Generic RTA è concesso in licenza e configurato in Avaya.
1. Clicca su _Salva integrazione_{:.doc-button} per creare l’integrazione.

L’integrazione comincia a importare dati in injixo. Se vuoi importare i dati sugli stati degli agenti, devi {$1$2$3 $4 features/acd-integration/cloud/import-agent-status-data.md %} dopo aver configurato l’integrazione Avaya. Se in precedenza hai attivato l'opzione **Importa i dati in tempo reale**, metti in pausa l’integrazione.

## Stringa di connessione

L'integrazione di Avaya CMS richiede la stringa di connessione per collegarsi al tuo database di Avaya CMS. Poiché Avaya CMS di solito utilizza un database IBM Informix, è necessario utilizzare una stringa di connessione speciale. 

Esempi di stringhe di connessione che utilizzano il driver ODBC di IBM Informix:<br>
- `DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=myServerAddress;DATABASE=myDatabase;HOST=myHost;SERVICE=myService;UID=myUsername;PWD=myPassword;PROTOCOL=onsoctcp;DELIMIDENT=y;` (accesso nativo tramite driver ODBC)
- `DSN=AvayaCMS;DELIMIDENT=y;` (richiede una connessione ODBC denominata AvayaCMS)
Se il tuo Avaya CMS non utilizza un database IBM Informix, devi ottenere la stringa di connessione specifica per il tuo database e driver ODBC. Avaya supporta solo la connettività ODBC.

## Modificare un’integrazione Avaya CMS

Se i dettagli dell’integrazione, come, per esempio, le credenziali del server del database, cambiano, è possibile modificare e aggiornare la configurazione dell’integrazione. L’importazione dei dati continuerà utilizzando la configurazione aggiornata.
