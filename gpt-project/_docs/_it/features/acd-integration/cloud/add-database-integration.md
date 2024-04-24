---
title: Aggiungere un’integrazione con database
navigation_title: Database
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Connetti il tuo database a injixo per importare dati.
redirect_from: /it/add-odbc-integration/
redirect_reason: renamed article in September 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Che cos’è un’integrazione con database?

Un’integrazione con database è un tipo di integrazione on-premise. Utilizza un’integrazione con database se il tuo sistema non può connettersi a un’integrazione cloud o a un’altra integrazione on-premise.

È possibile definire una query SQL per leggere i dati da un database. Le integrazioni con database utilizzano {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

## Aggiungere un’integrazione con database

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nella sezione **Universal Interfaces**, clicca su _Seleziona modello_{:.doc-button}.
4. Nella sezione **Database**, clicca su _Aggiungi integrazione_{:.doc-button}.

## Configurare una nuova integrazione con database

1. Inserisci un nome unico per l’integrazione che identifichi l’origine dei dati.
2. Installa e connetti {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Seleziona il **Tipo di database**.
4. Inserisci le credenziali richieste, in funzione del tipo di database scelto.

   | Tipo di database                                  | Credenziali                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | MS SQL Server<br>MySQL<br>PostgreSQL | **Nome del database**<br>**Host**<br>**Porta**: Se utilizzi un’istanza denominata su una connessione MS SQL Server, non inserire nessuna porta. Piuttosto, apri la porta UDP 1434 nel tuo firewall per far sì che il servizio SQL Server Browser riesca a stabilire la porta per injixo Cloud Link.<br>**Nome utente**<br>**Password**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | Altro (ODBC)                                   | **Stringa di connessione** Le stringhe di connessione contengono i parametri necessari affinché l’integrazione si connetta al server del database. Consulta [www.connectionstrings.com](https://www.connectionstrings.com) per trovare una stringa di connessione adatta al tuo database e al tuo driver ODBC.<br><br>Esempio per un database InterSystem Caché:<br>`DRIVER={InterSystemsODBC};SERVER=myServerAddress;` `PORT=12345;DATABASE=myDataBase;UID=myUsername;PWD=myPassword;` <br><br>L’identificatore SQL nelle query sarà contenuto tra virgolette doppie. Aggiungi ulteriori opzioni alla stringa di connessione se il tuo driver ODBC non presenta questa possibilità per impostazione predefinita, per esempio per Informix.<br><br>Esempio per un database IBM Informix:<br>`DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=myServerAddress;DATABASE=myDatabase;HOST=myHost;SERVICE=myService;UID=myUsername;PWD=myPassword;PROTOCOL=onsoctcp;DELIMIDENT=y;`<br><br>È anche possibile creare una sorgente dati ODBC in cui configuri il driver, il server, il database, etc. In questo modo puoi aggiungere l'opzione DSN sottostante come stringa di connessione anziché includere i dettagli di connessione nella stringa di connessione. Dovrai comunque aggiungere le opzioni che non possono essere configurate nella sorgente dati ODBC, come, per esempio: `DELIMIDENT=y`.<br><br>Esempi DSN:<br> `DSN=myODBCDatasourceName;`<br>`DSN=myODBCDatasourceName;DELIMIDENT=y;` |

## Configurare i dati da importare

1. Nella sezione **Configurazione**, seleziona il tipo di dati che vuoi importare dal database:
   - **Basato sul contatto** per i dati storici sui contatti, con una riga per ogni contatto
   - **Per intervallo** per i dati storici sui contatti che sono aggregati in intervalli di 15 o 30 minuti (impostati come Lunghezza dell’intervallo)
   - **Stato dell’agente** per i dati sugli stati degli agenti. 
    Per impostazione predefinita, i dati vengono importati ogni 15 minuti, ma puoi modificare la frequenza delle importazioni grazie a due caselle aggiuntive:
        - **Importa i dati in tempo reale**: l’importazione di dati avviene ogni 10 secondi. Disponibile soltanto in injixo Advanced e injixo Enterprise.
        - **Riconciliazione dei dati**: definisce quale intervalli di dati sugli stati degli agenti vengono importati ogni 15 minuti. Per impostazione predefinita vengono considerati i dati delle ultime 24 ore (consigliata).  

2. Seleziona il **Fuso orario del database** dal menu a tendina.
3. Inserisci la **query SQL** che sarà utilizzata per importare i dati dal database. Scopri di più sulle [query SQL](#query-sql).
4. Per creare l’integrazione, clicca su _Salva integrazione_{:.doc-button}.  
   L’integrazione comincia a importare dati in injixo. La prima importazione può durare parecchio tempo.  
   Tutte le code provenienti dai sistemi connessi saranno automaticamente disponibili all’assegnazione nella {% link_new schermata di configurazione dei workload | features/forecast/injixo-forecast/create-workloads.md | #creare-un-workload %} in injixo Forecast.  
   Le attività esterne saranno disponibili nell'attività Presente (ID 1). Per importare i dati sugli stati degli agenti, devi {% link_new associare gli identificatori degli utenti esterni e le attività | features/acd-integration/cloud/import-agent-status-data.md %}.

### Riconciliazione dei dati

A volte potrebbe essere necessario modificare manualmente i dati sugli stati degli agenti già importati. Un caso di questo tipo si verifica quando un membro del team ha dimenticato di timbrare l’uscita, e tu hai corretto i dati nel database per far sì che riflettessero le ore effettivamente lavorate.

Per impostazione predefinita, la casella **Riconciliazione dei dati** è spuntata. injixo reimporta tutti i dati

- delle ultime 24 ore;
- ogni 15 minuti.

Avrai sempre accesso ai dati più aggiornati delle ultime 24 ore. Solo le modifiche ai dati che risalgono a più di 24 ore non saranno incluse nella reimportazione.

La reimportazione continua di dati potrebbe rallentare il database. Se vuoi disattivare la riconciliazione dei dati, injixo importa solo i dati successivi all'ultima importazione riuscita (di solito, i dati degli ultimi 15 minuti). In questo caso, potrebbe essere necessario aggiornare manualmente in injixo i dati che sono stati importati più di 15 minuti fa. Se è possibile, mantieni spuntata questa casella, perché gli aggiornamenti manuali dei dati comportano un notevole sforzo aggiuntivo e sono soggetti a errori.

Quando metti in pausa un’integrazione per meno di 24 ore, injixo reimporta tutti i dati non appena riavvii l’integrazione. Questo si verifica sia se la casella è spuntata, sia se la casella non è spuntata.  
Quando metti in pausa un’integrazione per un periodo più lungo, tutti i dati precedenti le 24 ore non verranno reimportati.

## Query SQL

La query SQL per un'integrazione con database deve contenere dei nomi di colonne specifici. Il tipo di dati da importare determina le colonne necessarie. Puoi definire il nome della tabella. Di seguito trovi le query SQL più semplici che puoi eseguire:

<style>
table th:first-of-type {
   width: 20%;
}
table th:nth-of-type(4) {
   width: 50%;
}
</style>

| Tipo di dati da importare | Esempio di query                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------- |
| Per intervallo   | SELECT queueidentifier, queuename, timestamp, offered, answered, handlingtime, channel FROM table |
| Per contatto    | SELECT queueidentifier, queuename, timestamp, answered, duration, channel FROM table              |
| Stati degli agenti     | SELECT agentidentifier, starttime, endtime, activity FROM table                                   |

> Nota 
> 
> Nella maggior parte dei casi, le colonne del tuo database non corrisponderanno ai nomi delle colonne richiesti. Per risolvere questo problema, utilizza i nomi delle colonne richiesti come alias delle colonne, oppure crea una vista nel tuo database.

Amplia le query di esempio per ottenere e filtrare i dati dalla tua tabella personalizzata:

```
SELECT
  Start as "timestamp",
  Id as queueidentifier,
  Name as queuename,
  SUM(CASE countId WHEN 1000 THEN val ELSE 0 END) as offered,
  SUM(CASE countId WHEN 1001 THEN val ELSE 0 END) as answered,
  SUM(CASE countId WHEN 1002 THEN val ELSE 0 END) as handlingtime,
  calls as channel
FROM table
WHERE countId IN (1000, 1001, 1002)
GROUP BY Start, Name
```

## Dettagli delle colonne

Le tabelle di seguito mostrano i dettagli per le colonne previste, separate in base al tipo di importazione.

### Stati degli agenti

<style>

table {
   width: 100%;
}  
table th:first-of-type {
   width: 20%;
}
table th:nth-of-type(4) {
   width: 50%;
}
</style>

| Colonna                    | Tipo di dato | Necessario | Dettagli                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| agentidentifier           | Stringa    | Sì      | Identificatore univoco per l’agente                                                                                                                                          |
| starttime                 | Datetime  | Sì      | Inizio dell’attività dello stato dell’agente                                                                                                                                       |
| endtime                   | Datetime  | No       | Fine dell’attività dello stato dell’agente<br>Non utilizzare se l’attività è in corso.                                                                                               |
| activity                  | Stringa    | Sì      | Identificatore dell’attività esterna                                                                                                                                     |

### Per intervallo

| Colonna                    | Tipo di dato | Necessario | Dettagli                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| queueidentifier           | Stringa    | Sì      | Identificatore unico per la coda.<br>È possibile rinominare la coda cambiando queuename, ma queueidentifier non sarà modificato.                                        |

| queuename                 | Stringa    | Sì      | Identificatore per la coda                                                                                                                                                 |
| timestamp                 | Datetime  | Sì      | Inizio dell’intervallo                                                                                                                                                    |
| offered                   | Numero intero   | Sì      | Quantità di contatti (per esempio, telefonate o email) nell’intervallo                                                                                                                 |
| answered                  | Numero intero   | Sì      | Quantità di contatti che sono stati gestiti nell’intervallo                                                                                                                |
| handlingtime              | Numero intero   | Sì      | Tempo di gestione totale per tutti i contatti nell’intervallo                                                                                                                       |
| channel                   | Stringa    | No       | Identificatore per il canale della coda sorgente in injixo.<br>Se è vuoto, utilizzerà calls<br>Valori validi: calls, chats, emails, social_media, documents, cases. |


### Per contatto

| Colonna                    | Tipo di dato | Necessario | Dettagli                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| queueidentifier           | Stringa    | Sì      | Identificatore unico per la coda.<br>È possibile rinominare la coda cambiando queuename, ma queueidentifier non sarà modificato.                                        |
| queuename                 | Stringa    | Sì      | Identificatore per la coda                                                                                                                                                 |
| timestamp                 | Datetime  | Sì      | Inizio dell’intervallo                                                                                                                                                    |
| answered                  | Numero intero   | Sì      | Contatto gestito (valore 1).<br>Nessun contatto gestito (valore 0).                                                                                                                |
| duration                  | Numero intero   | No      | Tempo di gestione totale di un singolo contatto                                                                                                                                    |
| channel                   | Stringa    | No       | Identificatore per il canale della coda sorgente in injixo.<br>Se è vuoto, utilizzerà calls.<br>Valori validi: calls, chats, emails, social_media, documents, cases. |

## Modificare un’integrazione con database

Se i dettagli del database o la struttura dei dati cambiano, puoi modificare la configurazione dell’integrazione con database. L'importazione dei dati successiva verrà effettuata come in precedenza. Se hai bisogno di reimportare tutti i dati disponibili del passato, crea una nuova integrazione.

## Problemi noti del driver ODBC

Per prevenire un incremento delle connessioni TCP in Cloud Link quando si effettuano query sui dati da Amazon Athena, utilizza il driver ODBC 2.x [](https://docs.aws.amazon.com/it_it/athena/latest/ug/odbc-v2-driver.html).

