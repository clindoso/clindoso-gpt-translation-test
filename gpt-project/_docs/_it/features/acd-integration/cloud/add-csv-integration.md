---
title: Aggiungere un’integrazione CSV
navigation_title: CSV
description: Importare in injixo dati storici da file CSV.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /it/csv-format/
redirect_reason: /csv-format/ used on in injixo UI (injixo.com/csv-importer)
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
---

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Che cos’è un’integrazione CSV?

Un’integrazione CSV importa dati storici sui contatti o sugli stati degli agenti da file CSV. Utilizza un’integrazione CSV se il tuo sistema non può connettersi con nessun’altra integrazione.

Per configurare un’integrazione CSV, segui questi passaggi:

- Crea un'integrazione CSV in injixo.
- Crea uno schema CSV.
- Associa le colonne (tramite il menu a tendina o con una query SQL).
- Importa i file CSV tramite importazione automatica o manuale.

## Aggiungere un’integrazione CSV

Per importare file CSV con formati diversi (per esempio, file con separatori, formati di date o nomi di colonne diversi), imposta un’integrazione distinta per ogni formato di file. A seconda del file CSV generato dal tuo sistema esterno, injixo potrebbe aspettarsi colonne diverse rispetto a quelle del tuo file CSV. [Scopri di più](#mappare-le-colonne) sulle colonne previste da injixo e su come mapparle se il tuo file CSV contiene colonne o nomi di colonne diversi.

Per aggiungere un'integrazione CSV in injixo, segui questi passaggi:

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nella sezione **Universal Interfaces**, clicca su _Seleziona modello_{:.doc-button}.
4. Nella sezione **CSV**, clicca su _Aggiungi integrazione_{:.doc-button}.

## Configurare una nuova integrazione CSV

1. Assegna all’integrazione un nome unico che identifichi l’origine dei dati.
2. Nella sezione **injixo Cloud Link**, installa e connetti {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md | #installare-injixo-cloud-link %}. Se preferisci [caricare i dati manualmente](#importazione-manuale-dei-file), puoi saltare questo passaggio.
3. Nella sezione **Configurazione dello schema CSV**, seleziona il **Tipo di dati da importare**:
   - **Dati sui contatti**: i dati caricati comprendono tutti i volumi di contatto in entrata e gestiti, registrati dal tuo sistema esterno, come chiamate, chat, social media, ticket, email, o documenti.
   - **Stati degli agenti**: i dati caricati comprendono tutte le attività degli agenti registrate dal tuo sistema esterno, come login, logout, in chiamata, elaborazione post-chiamata, pausa, in attesa, etc.
4. Clicca su _Crea un nuovo schema CSV_{:.doc-button}.
5. Configura i parametri dello schema CSV. Tra questi, ci sono:
   - la configurazione e le opzioni di pre-elaborazione;
   - la mappatura delle colonne (per impostazione predefinita con i [menu a tendina](#mappare-le-colonne), oppure tramite una [query SQL](#mappare-le-colonne-query-sql)).  
      Leggi come [creare uno schema CSV](#creare-uno-schema-csv) utilizzando le opzioni di configurazione elencate qui sopra.
6. Clicca su _Salva integrazione_{:.doc-button} per creare l’integrazione.

Dopo aver salvato l’integrazione, puoi [importare i dati manualmente](#importazione-manuale-dei-file), oppure impostare l’[importazione automatica](#importazione-automatica-dei-file).

## Creare uno schema CSV

Ogni integrazione CSV ha il suo schema CSV. Lo schema CSV descrive il formato e la mappatura delle colonne del file CSV. Se il tuo sistema esterno genera un file CSV che non contiene i nomi esatti delle colonne mostrate in injixo, puoi mapparli in injixo utilizzando il [menu a tendina (impostazione predefinita)](#mappare-le-colonne) oppure una [query SQL](#mappare-le-colonne-query-sql).  
[Scopri di più](#mappare-le-colonne) sulle colonne previste da injixo e su come mapparle se il tuo file CSV contiene colonne o nomi di colonne diversi.

Prima di creare lo schema CSV, è necessario [aggiungere un’integrazione CSV](#aggiungere-unintegrazione-csv) e selezionare il tipo di dati da importare. I parametri che configuri per lo schema CSV saranno diversi a seconda del tipo di dati di importazione selezionato (dati sui contatti o stati degli agenti).

### Configurazione e opzioni di pre-elaborazione

1. Nella sezione **Configurazione**, carica un file CSV di esempio generato dal tuo sistema esterno. Così potrai vedere in che modo injixo tratterà i file del tuo sistema esterno durante l'importazione.
2. Imposta i parametri seguenti. I parametri da impostare saranno diversi a seconda del tipo di dati da importare:<br><br>

   | Parametro                                                     | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Separatore di colonna del file CSV**                              | Il carattere utilizzato come separatore nel file CSV, come, per esempio, il punto e virgola.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | **Fuso orario**                                                 | Il fuso orario nel quale il sistema esterno registra i dati, come, per esempio Europe/Rome (UTC+01:00).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | **Layout dei dati**<br>(Solo per i dati sui contatti)                     | Il layout dei dati dipende dal metodo di creazione del file CSV.<br>**Per contatto**: per i file che contengono una riga per ogni contatto. Dal momento che i dati sui contatti importati vengono aggregati in intervalli di 15 minuti, l’intervallo dell’unità di pianificazione deve essere 15 minuti. Le nuove importazioni di dati sovrascriveranno i dati che sono stati importati in precedenza per l'intervallo. Se il tuo file contiene lo stesso timestamp più volte, questi data verranno sommati per l’intervallo.<br><br>**Per intervallo**: per dati aggregati che contengono una riga con tutta le informazioni di contatto per intervallo. Seleziona la lunghezza dell’intervallo che corrisponde a quella del tuo file CSV. Se selezioni un intervallo più lungo rispetto agli intervalli dei file caricati, vedrai un messaggio di errore. Se invece selezioni un intervallo più breve rispetto a quelli dei file, per esempio un intervallo di 15 minuti per un file con intervalli di 30 minuti, ogni intervallo mancante (in questo caso, ogni secondo intervallo) verrà riempito con 0 o con le parole "no data", in base all'opzione che hai scelto alla voce **Gestione dei valori mancanti negli intervalli**. |
   | **Gestione dei valori mancanti negli intervalli**<br>(Solo per i dati sui contatti) | Definisci il modo in cui i valori mancanti nella coda di arrivo verranno visualizzati in altre sezioni di injixo:<br>**Riempire con zero**: i valori mancanti saranno sostituiti da uno zero.<br>**Lasciare vuoto**: i valori mancanti saranno sostituiti dal testo “no data”.<br>L’opzione **Lasciare vuoto** è la migliore nella maggior parte dei casi. Le importazioni sovrascriveranno i dati già esistenti.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

3. (Facoltativo) Tra le **Opzioni di pre-elaborazione**, seleziona una o più opzioni rilevanti per il formato del tuo file CSV:<br><br>

   | Opzioni di pre-elaborazione       | Descrizione                                                                                                                                                                                             |
   | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Aggiungi riga di intestazione**         | Nel caso di file senza una riga di intestazione, injixo etichetterà le colonne con A, B, C, etc., nella pagina di [mappatura delle colonne](#mappare-le-colonne).                                                                        |
   | **Salta le righe vuote**        | injixo ignorerà le righe che contengono solo separatori.                                                                                                                                                  |
   | **Salta le prime righe**        | injixo eliminerà le righe aggiuntive all’inizio del file. Inserisci il numero di righe che devono essere ignorate.                                                                                               |
   | **Salta le righe contenenti** | injixo ignorerà le righe che contengono dei caratteri specifici. Inserisci una stringa (che distingua tra maiuscole e minuscole). injixo ignorerà le righe che contengono questa stringa. Puoi aggiungere più di una stringa cliccando su _Aggiungi stringa_{:.doc-button}. |

4. Per procedere con la mappatura delle colonne, clicca su _Mappa le colonne_{:.doc-button}.

### Mappare le colonne

Per impostazione predefinita, puoi utilizzare i menu a tendina nella sezione **Mappare le colonne** per stabilire come le colonne dei tuoi file CSV verranno associate alle colonne necessarie in injixo. Per mappare le colonne, è necessario aver completato la [configurazione](#configurazione-e-opzioni-di-pre-elaborazione).
Se il tuo sistema esterno genera file CSV che non includono le colonne previste, puoi [mapparle utilizzando una query SQL](#mappare-le-colonne-query-sql).

È possibile vedere un’anteprima del file CSV che hai caricato.

1. Utilizzando i menu a tendina, mappa le colonne e i formati del file CSV.

2. Compila tutti i campi.  
   Per ulteriori informazioni sulle opzioni per i [dati sui contatti](#menu-a-tendina-relativi-ai-dati-sui-contatti) e per i [dati sugli stati degli agenti](#menu-a-tendina-relativi-agli-stati-degli-agenti), vedi le tabelle qui di seguito.

3. Per salvare la configurazione, clicca su _Salva schema_{:.doc-button}.

#### Menu a tendina relativi ai dati sui contatti

Se hai scelto di importare i dati del tipo **Dati sui contatti**, per impostazione predefinita la pagina della mappatura comprende gli elementi seguenti:

| Campo          | Descrizione                                                                                                                                                                                                                                          | Necessario per i dati raggruppati per intervallo | Necessario per i dati raggruppati per contatto |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------: | :-----------------------------: |
| **Nome Coda** | Il nome della coda da cui i dati sono importati.                                                                                                                                                                                                        |               Sì                |               Sì               |
| **Data**       | Formato e valori della data.<br>Per impostazione predefinita, è possibile selezionare dal menu a tendina un formato di data che corrisponda al formato CSV. Per configurare un [formato di data personalizzato](#formato-di-data-personalizzato), clicca sull’{% icon gear %} e inserisci il formato nel campo di testo. |               Sì                |               Sì               |
| **Ora**       | Formato e valori dell’ora.                                                                                                                                                                                                                          |               Sì                |               Sì               |
| **Timestamp**  | Valori del timestamp secondo un [formato di timestamp personalizzato](#formato-di-timestamp-data-e-ora-personalizzato).<br>Questa colonna compare se attivi l'opzione **Date e ora nella stessa colonna**.                                                                              |               Sì                |               Sì               |
| **Entranti**    | Contatti entranti (per intervallo nel caso di dati raggruppati per intervallo).<br>Accetta numeri interi oppure decimali separati da un punto.                                                                                                                                            |               Sì                |               Sì               |
| **Gestiti**    | Contatti a cui è stata data una risposta (per intervallo nel caso di dati raggruppati per intervallo).<br>Accetta numeri interi e numeri decimali separati dal punto.<br>Per i dati raggruppati per contatto, il valore dei contatti gestiti può essere soltanto 0 oppure 1 (oppure decimali).                                              |               Sì                |               Sì               |
| **AHT**        | Tempo medio di gestione per intervallo.<br> I formati supportati sono i secondi (numeri interi), oppure hh:mm:ss (per esempio 00:05:00).<br>Se la colonna AHT non esiste, seleziona **Nessuna colonna**.<br>Questo campo è disponibile solo per i dati raggruppati per intervallo.                           |                No                |               No                |
| **Durata**   | Durata del dato registrato in secondi (numeri interi).<br>Questo campo è disponibile solo per i dati raggruppati per contatto.                                                                                                                                                                        |                No                |               Sì               |
| **Canale**    | Nome prestabilito del canale (primo menu a tendina) oppure colonna selezionabile che include il nome del canale (secondo menu a tendina).<br>Valori ammessi: calls, emails, chats, documents, cases, social_media.                                                           |               Sì                |               Sì               |

#### Menu a tendina relativi agli stati degli agenti

Se hai scelto di importare i dati del tipo **Stati degli agenti**, per impostazione predefinita la pagina della mappatura comprende gli elementi seguenti:

| Campo                   | Descrizione                                                                                                                                                                                                                                                                          | Necessario |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| **Identificativo agente**    | Identificativo unico per l’agente come, per esempio, il numero identificativo o il nome.                                                                                                                                                                                                                                     | Sì      |
| **Identificativo attività** | L’attività nella quale l’agente è impegnato.                                                                                                                                                                                                                                                     | Sì      |
| **Data di inizio**          | La data in cui l’agente ha cominciato l’attività.<br>Per impostazione predefinita, è possibile selezionare dal menu a tendina un formato che corrisponde al formato del tuo file CSV. Per configurare un [formato di data personalizzato](#formato-di-data-personalizzato), clicca sull’{% icon gear %} e inserisci il formato nel campo di testo.   | Sì      |
| **Ora di inizio**          | L’ora in cui l’agente ha cominciato l’attività.                                                                                                                                                                                                                                         | Sì      |
| **Timestamp inizio**     | [Timestamp con formato personalizzato](#formato-di-timestamp-data-e-ora-personalizzato) che contiene la data e l’ora in cui l’agente ha cominciato l’attività.<br>Questa colonna compare se attivi l'opzione **Date e ora nella stessa colonna**.                                                                 | Sì      |
| **Data di fine**            | La data in cui l’agente ha interrotto l’attività.<br>Per impostazione predefinita, è possibile selezionare dal menu a tendina un formato di data prestabilito che corrisponde al formato del tuo file CSV. Per configurare un [formato di data personalizzato](#formato-di-data-personalizzato), clicca sull’{% icon gear %} e inserisci il formato nel campo di testo. | No       |
| **Ora di fine**            | L’ora in cui l’agente ha interrotto l’attività.                                                                                                                                                                                                                                         | No       |
| **Timestamp fine**       | [Timestamp con formato personalizzato](#formato-di-timestamp-data-e-ora-personalizzato) che contiene la data e l’ora in cui l’agente ha interrotto l’attività.<br>Questa colonna compare se attivi l'opzione **Date e ora nella stessa colonna**.                                                                 | No       |

#### Formato di data personalizzato

Puoi configurare un formato di data personalizzato che corrisponde alla data nei tuoi file CSV. Inserisci nel campo **Formato data personalizzato** i caratteri specificati di seguito:

- per il giorno: **D** (cifre singole, da 1 a 9) oppure **DD** (per cifre precedute da zero);
- per il mese: **M** (cifre singole, da 1 a 9) oppure **MM** (per cifre precedute da zero);
- per l’anno: **YY** oppure **YYYY**.

Tutti gli altri caratteri sono interpretati come separatori.

Esempi:

| Data     | Formato di data personalizzato |
| -------- | ------------------ |
| 13/1,22  | D/M,YY             |
| 010122   | DDMMYY             |
| 13012022 | DDMMYYYY           |

#### Formato di timestamp data e ora personalizzato

Per aggiungere un formato di timestamp personalizzato, attiva l’opzione **Date e ora nella stessa colonna**.
Oltre al [formato di data personalizzato](#formato-di-data-personalizzato), devi impostare il formato dell’ora utilizzando lettere minuscole:

- per le ore: **h** (cifre singole, da 1 a 9) oppure **hh** (per cifre precedute da zero);
- per i minuti: **m** (cifre singole, da 1 a 9) oppure **mm** (per cifre precedute da zero);
- (facoltativo) per i secondi: **s** (cifre singole, da 1 a 9) oppure **ss** (per cifre precedute da zero).

Esempi:

| Data e ora  | Formato timestamp |
| -------------- | ---------------- |
| 13/1,22 9:15:8 | D/M,YY h:m:s     |
| 010122 09-15   | DDMMYY hh-mm     |

### Mappare le colonne (query SQL)

Per la maggior parte dei file CSV, puoi utilizzare la mappatura prestabilita tramite i menu a tendina. Se il tuo sistema esterno genera dei file CSV che non contengono le colonne richieste dal modulo di mappatura prestabilito (per esempio, se richiedono dei calcoli supplementari), oppure se contengono dei formati non supportati, il [metodo di mappatura delle colonne prestabilito](#mappare-le-colonne) potrebbe non essere adatto. In questo caso, puoi mappare le colonne utilizzando una query SQL (SQLite). In questo modo, puoi convertire i valori totali in medie, oppure calcolare il volume delle chiamate utilizzando i dati contenuti in più colonne, per esempio. Questo metodo di mappatura è disponibile soltanto per i dati sui contatti. Non può essere utilizzato per i dati sugli stati degli agenti.

#### Requisiti

Tieni in considerazioni i seguenti requisiti quando scrivi una query SQL per la mappatura delle colonne:

- Utilizza `uploaded_file` come nome della tabella.
- Utilizza solo lettere minuscole per i nomi delle colonne.
- Utilizza datetime come tipo di dati per la colonna timestamp (nel formato `YYYY-MM-DD hh:mm:ss`).
- Utilizza la sintassi [SQLite](https://www.sqlite.org) per le query.

Le query [SQLite](https://www.sqlite.org) supportano le operazioni matematiche, le conversioni di date, e gli alias delle colonne (per mappare nomi di colonne diversi). Per ulteriori informazioni sulle limitazioni che riguardano gli elementi seguenti, vai su sqlite.org:

- [precisione numerica](https://www.sqlite.org/datatype3.html);
- [funzioni matematiche](https://www.sqlite.org/lang_mathfunc.html);
- [conversioni implicite di dati](https://www.sqlite.org/datatype3.html#affinity);
- [funzioni di data e ora](https://www.sqlite.org/lang_datefunc.html);
- [modifica di stringhe](https://www.sqlite.org/lang_corefunc.html#string_functions).

Per mappare le colonne con una query SQL, procedi come di seguito:

> Se cambi il metodo di mappatura, lo schema CSV esistente verrà sovrascritto.
>
> Se hai già creato uno schema CSV, cambiare il metodo di mappatura e salvare il nuovo schema sovrascriverà lo schema precedente. Non è possibile ripristinare uno schema CSV una volta che è stato sovrascritto.

1. Attiva l'opzione **Utilizza una query SQL per mappare le colonne** nell'angolo in alto a destra della pagina di mappatura delle colonne.
2. Inserisci una query SQL (SQLite) nel campo di testo. Suggerimento: copia e incolla gli esempi di query qui di seguito in base alle tue esigenze.

Se desideri caricare sia dei dati di contatto basati su intervalli che dei dati di contatto basati su contatti, dovrai aggiungere un'altra integrazione e scrivere una query SQL separata.

### Colonne necessarie nella query SQL

La seguente tabella offre una panoramica delle colonne necessarie nella query SQL:

> In base al tuo [piano WFM](https://www.injixo.com/pricing/), potrebbero non essere disponibili tutti i canali per la coda di origine di injixo.

| Nome colonna | Tipo di dato | Necessario | Dettagli                                                                                                                                                                                                  |
| ----------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| queue       | Stringa    | Sì      | Identificatore per la coda.                                                                                                                                                                                 |
| timestamp   | Datetime  | Sì      | Inizio dell'intervallo nel formato YYYY-MM-DD hh:mm:ss.                                                                                                                                                  |
| offered     | Numero intero   | Sì      | Quantità di contatti (per esempio, telefonate o email) nell’intervallo.                                                                                                                                                 |
| answered    | Numero intero   | Sì      | Per intervallo: Quantità di contatti che sono stati processati nell’intervallo<br>Per contatto: Il valore 1 indica che il contatto è stato processato. Il valore 0 indica che il contatto non è stato processato. |
| aht         | Float     | No       | Tempo di gestione medio per tutti i contatti nell’intervallo.                                                                                                                                                   |
| duration    | Numero intero   | Sì      | Tempo di gestione per un singolo contatto.                                                                                                                                                                  |
| channel     | Stringa    | Sì      | Identificatore per il canale della coda sorgente in injixo.<br>Valori ammessi: calls, chats, email, social_media, documents, cases.                                                                            |

#### Esempi di query semplici

Dati sui contatti (per intervallo):

```sql
SELECT
   queue, timestamp,
   offered, handled, aht,
   channel
FROM uploaded_file
```

Dati sui contatti (per contatto):

```sql
SELECT
   queue, timestamp,
   offered, handled, duration,
   channel
FROM uploaded_file
```

I seguenti esempi avanzati illustrano come applicare delle funzioni matematiche e delle funzioni SQLite.

#### Esempio di query complessa 1

- Dividere HandleTime per HandledCalls per il tempo medio di gestione (AHT) richiesto.
- Combinare Date e Time utilizzando SUBSTR per il formato di timestamp richiesto YYYY-MM-DD HH:MM:SS.

|   Queue    |    Data    | Time  | Received | HandledCalls | Aband | HandleTime | HoldTime |
| :--------: | :--------: | :---: | :------: | :----------: | :---: | :--------: | :------: |
| test queue | 06/03/2023 | 07:30 |    5     |      5       |   -   |   1324.6   |    -     |
| test queue | 06/03/2023 | 08:00 |    2     |      2       |   -   |    1548    |    -     |

```
SELECT
  Queue as queue,
  SUBSTR(Date, 7, 4) || '-'|| SUBSTR(Date, 1, 2) || '-' || SUBSTR(Date, 4,2) || ' ' || Time || ':00' as timestamp,
  Received as offered,
  HandledCalls as handled,
  HandleTime/HandledCalls as aht,
  'chats' as channel
FROM uploaded_file
```

#### Esempio di query complessa 2

- Utilizzare `date('now')` di SQLite per ottenere la data attuale e combinarla con l’ora proveniente dal file.
- Eliminare i decimali e convertirli in numeri interi.
- Combinare Date e Time utilizzando SUBSTR per il formato di timestamp richiesto YYYY-MM-DD HH:MM:SS.

In questo esempio, le intestazioni delle colonne contengono dei caratteri vuoti. 

| Queue Name | Hour in hh:mm | Offered Calls | Handled Calls | Average Handling Time       |
| :--------: | :-----------: | :-----------: | :-----------: | :-------------------------: |
| coda demo |     07:00     |      3.4      |      2.9      |          00:05:30           |
| coda demo |     08:30     |      5.7      |      5      |          00:10:15           |

Puoi sostituire la riga d’intestazione utilizzando le opzioni di pre-elaborazione dell’integrazione:

- Salta le prime 1 righe: rimuove l’intestazione originale
- Aggiungi riga di intestazione: aggiunge intestazioni di colonne con lettere

```
 SELECT
   A as queue,
   DATE('now')||' '|| "B"||':00' as timestamp,
   FLOOR(C) as offered,
   FLOOR (D) as handled,
   (CAST(substr(E, 1, 1) AS INTEGER) * 3600) +
   (CAST(substr(E, 3, 2) AS INTEGER) * 60) +
   CAST(substr(E, 6, 2) AS INTEGER) as aht,
   'calls' as channel
FROM uploaded_file
```

Se non sostituisci la riga d’intestazione, devi riportare i nomi effettivi delle colonne utilizzando le virgolette doppie: 

```
 SELECT
   "Queue Name" as queue,
   DATE('now')||' '|| "Hour in hh:mm"||':00' as timestamp,
   FLOOR("Offered Calls") as offered,
   FLOOR ("Handled Calls") as handled,
   (CAST(substr("Average Handling Time", 1, 1) AS INTEGER) * 3600) +
   (CAST(substr("Average Handling Time", 3, 2) AS INTEGER) * 60) +
   CAST(substr("Average Handling Time", 6, 2) AS INTEGER) as aht,
   'calls' as channel
FROM uploaded_file
```

#### Esempio di query complessa 3

- Calcolare le chiamate gestite sottraendo AbandonedCalls da OfferedCalls.
- Convertire la stringa Start con un formato speciale nel formato di timestamp richiesto YYYY-MM-DD HH:MM:SS.

|  Name  |       Start       | OfferedCalls | AbandonedCalls | AverageHandlingTime |
| :----: | :---------------: | :----------: | :------------: | :-----------------: |
| queue1 | 20230613 15:30:00 |      10      |       2        |         300         |
| queue2 | 20230613 15:35:00 |      15      |       3        |         450         |
| queue3 | 20230613 15:40:00 |      12      |       2        |         350         |

<!-- notes for database integrations -->
<!-- In this example, the date time format in the Start column is not supported by built-in SQLite `datetime()` and `strftime()` functions. You need to change the string first. -->
<!-- changed the example from datetime(substr(Start, 1, 4) || '-' || to substr(Start, 1, 4) || '-' || -->
<!-- `datetime` is not required here, but in database integrations it would be needed due to the reqiured datetime datatype in the table around line 210 -->

```
SELECT
  Name as queue,
    substr(Start, 1, 4) || '-' ||
    substr(Start, 5, 2) || '-' ||
    substr(Start, 7, 2) || ' ' ||
    substr(Start, 10, 8) as timestamp,
  Offered as offered,
  (Offered - Abandoned) as handled,
  AverageHandlingTime as aht,
  'calls' as channel
FROM uploaded_file
```

<!-- do not change the heading, used in the integrations UI -->

## Modificare uno schema CSV

Quando la struttura dei dati di un file CSV cambia, è necessario modificare lo schema CSV di un’integrazione CSV.

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Clicca sull’{% icon pencil %} accanto all’integrazione che vuoi modificare.
3. Clicca su _Modifica schema CSV_{:.doc-button}.
   Puoi cambiare le opzioni nella sezione **Configurazione**. Per modificare le opzioni di pre-elaborazione, clicca su _Caricare nuovamente il file_{:.doc-button} e carica un file CSV modificato oppure il file originale.
4. Clicca su _Mappa le colonne_{:.doc-button}. Se è necessario, puoi modificare la mappatura delle colonne.
5. Clicca su _Salva schema_{:.doc-button}.

> Il layout dei dati non può essere modificato.
>
> Quando modifichi uno schema CSV, non puoi cambiare il layout dei dati che avevi impostato (per contatto o per intervallo).

## Esempi di mappature

In questa sezione troverai esempi di file CSV e relative mappature. Puoi utilizzare questi esempi come modelli per i tuoi file CSV.

### Dati sui contatti (per intervallo)

File CSV:

```

Queue;Date;Time;IncomingCalls;AnsweredCalls;AHT
My Inbound Queue;25/05/2020;08:00;15;14;230
My Inbound Queue;25/05/2020;08:15;16;15;210
My Inbound Queue;25/05/2020;08:30;20;18;235
My Inbound Queue;25/05/2020;08:45;18;15;215

```

<!-- left-align all tables -->
<style>
table {
   margin-left: 0px;
}
</style>

Mappatura delle colonne:

| Colonna      | Colonna mappata/valore |
| ----------- | ------------------- |
| Nome della coda  | Queue               |
| Data        | Date                |
| Formato della data | dd/mm/yyyy          |
| Ora        | Time                |
| Formato dell’ora | hh:mm               |
| In entrata     | IncomingCalls       |
| Gestiti     | AnsweredCalls       |
| AHT         | AHT                 |
| Formato AHT  | Seconds             |

Questo esempio non comprende una colonna per il Canale. Nella configurazione dello schema CSV, seleziona l’opzione **Canale**. Per esempio, per impostare il canale per le chiamate, seleziona **Chiamate** dal menu a tendina.

### Dati sui contatti (per contatto)

File CSV:

```

Queue;Date;Time;Offered;Answered;Duration
My Inbound Queue;25/05/2020;08:00;1;1;100
My Inbound Queue;25/05/2020;08:03;1;0;0
My Inbound Queue;25/05/2020;08:04;1;1;120
My Inbound Queue;25/05/2020;08:07;1;0;0

```

Mappatura delle colonne:

| Colonna      | Colonna mappata/valore |
| ----------- | ------------------- |
| Nome della coda  | Queue               |
| Data        | Date                |
| Formato della data | dd/mm/yyyy          |
| Ora        | Time                |
| Formato dell’ora | hh:mm               |
| In entrata     | Offered             |
| Gestiti     | Answered            |
| Durata    | Duration            |

Questo esempio non comprende una colonna per il Canale. Nella configurazione dello schema CSV, seleziona l’opzione **Canale**. Per esempio, per impostare il canale per le chiamate, seleziona **Chiamate** dal menu a tendina.

### Stati degli agenti

File CSV:

```

StartDate;StartTime;AgentID;AgentActivityID
2022-04-22;08:34:29;816;1013;
2022-04-22;08:34:42;816;1015;
2022-04-22;08:34:48;816;1015;
2022-04-22;08:39:11;816;1015;

```

Mappatura delle colonne:

| Colonna              | Colonna mappata/valore |
| ------------------- | ------------------- |
| Identificativo agente    | AgentID             |
| Identificativo attività | AgentActivityID     |
| Data di inizio          | StartDate           |
| Formato della data         | yyyy-mm-dd          |
| Ora di inizio          | StartTime           |
| Formato dell’ora         | hh:mm:ss            |

## Importare file CSV

Dopo aver salvato l’integrazione CSV, puoi cominciare a importare file CSV.
I seguenti sistemi di codifica dei file sono supportati:

- UTF-8;
- ISO-8859-1/Latin-1;
- ISO-8859-9;
- Windows-1252.

Utilizza il sistema di codifica UTF-8 per evitare i messaggi di errore generici.

### Importazione automatica dei file

[Configura un’integrazione CSV](#configurare-una-nuova-integrazione-csv) e connetti injixo Cloud Link. injixo Cloud Link caricherà i nuovi dati in injixo. Per impostazione predefinita, ogni volta che salvi un nuovo file CSV nella cartella di installazione di injixo Cloud Link, viene avviato un nuovo caricamento. Durante l’installazione puoi modificare la cartella di installazione predefinita, che è C:\\Program Files\\injixo Cloud Link.

In alternativa, puoi configurare una {% link_new cartella per le importazioni | features/acd-integration/cloud/install-cloud-link.md | #configurare-la-cartella-di-importazione %} separata per il caricamento dei file. Salva i nuovi file nella cartella di impostazione.

Dopo che i dati sono stati caricati, puoi {% link_new aggiungere delle nuove code a un workload | features/forecast/injixo-forecast/manage-workloads.md %} in Forecast, oppure vedrai i dati aggiornati nei workload esistenti. Se non vengono caricati dei dati, utilizza l’importazione manuale descritta qui di seguito per verificare che il formato del file sia valido.

### Importazione manuale dei file

Puoi caricare manualmente i dati in injixo tramite una pagina web.

Dopo aver [aggiunto un’integrazione CSV](#configurare-una-nuova-integrazione-csv), puoi caricare i dati manualmente (puoi saltare l’installazione di injixo Cloud Link).

1. Vai su [www.injixo.com/csv-importer](https://www.injixo.com/csv-importer).
2. Clicca su **apri il tuo file explorer** e seleziona un file CSV o TXT da importare (oppure trascina il file nel browser).
3. Nel menu in basso a sinistra, seleziona la tua integrazione CSV.
4. Clicca su _Importa file_{:.doc-button}.
   Per evitare messaggi di errore, il formato del file deve corrispondere allo [schema CSV](#creare-uno-schema-csv).
5. Per caricare i dati, clicca su _Applica i dati_{:.doc-button}.

Dopo che i dati sono stati elaborati, potrai {% link_new aggiungere le code a un workload | features/forecast/injixo-forecast/manage-workloads.md %} in injixo Forecast. Le dimensioni massime del file sono 7 MB.

## Domande frequenti

| Domanda                                                                  | Risposta                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Posso importare due volte lo stesso file?                                         | Sì, se importi i dati manualmente. No, se utilizzi Cloud Link.<br>Per identificare file duplicati, injixo calcola i checksum durante l’importazione. I file importati con lo stesso checksum non saranno importati di nuovo. Se il file ha lo stesso nome ma un contenuto diverso, verrà importato. |
| Dopo l’importazione, i file CSV importati automaticamente vengono eliminati da injixo? | No. I file importati restano all’interno della cartella del client injixo Cloud Link. Puoi eliminarli manualmente o impostare un compito ricorrente.                                                                                                                                              |
| Posso importare un file CSV che contiene dati futuri?                        | Sì, ma consigliamo di non importare file che contengono dati futuri. injixo non ignorerà i dati futuri, ma li archivierà come dati storici. Puoi comunque calcolare una previsione, ma il grafico con i dati storici e quello con la previsione si sovrapporranno.                                               |
