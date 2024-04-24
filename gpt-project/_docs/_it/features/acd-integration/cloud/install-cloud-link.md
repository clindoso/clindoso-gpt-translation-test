---
title: Installare injixo Cloud Link
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Installare il client injixo Cloud Link per importare dati in injixo.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Che cos’è injixo Cloud Link?

injixo Cloud Link è un programma client che deve essere installato durante la configurazione delle integrazioni on-premise. injixo Cloud Link importa dati in injixo con cadenza regolare. Puoi anche installare injixo Cloud Link quando configuri le integrazioni CSV per importare regolarmente nuovi file CSV da una cartella.

La directory per l’installazione del client contiene:

- l’eseguibile injixo-cloud-link;
- uno o più file di registro injixo-cloud-link.*.log;
- il file di configurazione injixo-cloud-link.toml;
- una cartella di licenze con le licenze della library open source.

## Prerequisiti

- Windows: injixo Cloud Link gira su Windows 10 e versioni superiori, e su Windows Server 2016 e superiori. <!-- what about Linux -->
- Linux: è necessario installare il pacchetto unixODBC.
- Firewall/Proxy: la porta 443 deve essere aperta al traffico in uscita. injixo Cloud Link utilizza una crittografia TLS con TCP sulla porta 443.

Nota: le integrazioni on-premise accedono a un sistema locale da cui estraggono dati, come, per esempio, un sistema ACD o CRM. In base al tipo di database, sarà necessario installare un driver specifico.

## Installare injixo Cloud Link

Quando aggiungi un’{% link_new integrazione on-premise | features/acd-integration/cloud/add-on-premise-integration.md %}, un’{% link_new integrazione CSV | features/acd-integration/cloud/add-csv-integration.md %}, o un’{% link_new integrazione database | features/acd-integration/cloud/add-database-integration.md %}, la sezione **injixo Cloud Link** fornisce i link per scaricare il pacchetto di installazione del client (per Windows) o l’archivio (per Linux).

### Installazione del servizio Windows

Installa il primo servizio utilizzando il programma di installazione del client di Windows.

1. Clicca su **Scarica per Windows 64-bit** e avvia il programma di installazione.
2. Clicca su **Next**.
3. (Facoltativo) Modifica la directory d’installazione.
4. Clicca su **Next**, poi su **Install**.  
   Una finestra della console mostra un PIN che è valido per 5 minuti.  
   Per [connettere Cloud Link all’integrazione](#connettere-cloud-link-allintegrazione), segui le istruzioni nella finestra della console.
5. Clicca su **Finish** nel programma di installazione.  
   Il programma di installazione crea il servizio Windows **injixo Cloud Link**.

### Installare servizi Windows aggiuntivi

È possibile installare fino a otto servizi aggiuntivi che servono integrazioni distinte. Per evitare di sovrascrivere le istanze di servizio precedenti, installale in directory separate.

Per installare un secondo servizio Cloud Link su Windows, aggiungi una nuova integrazione e procedi come di seguito:

1. Clicca su **Scarica per Windows 64 bit**.
2. Apri il prompt dei comandi di Windows (cmd).
3. Per la seconda istanza, lancia il comando seguente:

   ```
   msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS=":instance.1"
   ```

   > Incrementa l'ID dell'istanza nel parametro TRANSFORMS quando installi più istanze.
   >
   > Per esempio, la terza istanza richiede `":instance.2"`, la quarta istanza `":instance.3"`, e così via.

  
4. Segui le istruzioni nella procedura di installazione.  
   Il programma di installazione suggerirà una nuova directory di installazione predefinita che include l'istanza, per esempio: (Istanza 1).  
   Suggerimento: per identificare a quale integrazione appartiene l’installazione, puoi aggiungere dei dettagli sul sistema ACD e sul tipo di importazione, per esempio: (ACD - importazione agenti) alla directory di installazione predefinita.  
   Al termine dell’installazione, vedrai un nuovo servizio Windows chiamato injixo Cloud Link (Instance {id}).

### Installazione del servizio Linux

Installa il primo servizio come nell’esempio di seguito:

1. Clicca su **Scarica per Linux 64-bit** ed estrai l’archivio nella cartella di installazione che preferisci.
2. Apri il terminal.
3. Installa il client di injixo Cloud Link:  
   `sudo ./injixo-cloud-link service install`
4. Avvia il servizio installato:  
   `sudo ./injixo-cloud-link service start`
5. Mostra un PIN con il comando:  
   `sudo ./injixo-cloud-link pin`  
   Una finestra della console mostra un PIN che è valido per 5 minuti.  
   Per [connettere Cloud Link all’integrazione](#connettere-cloud-link-allintegrazione), segui le istruzioni nella finestra della console.

### Installare servizi Linux aggiuntivi

È possibile installare più servizi, che servono integrazioni distinte. Per non sovrascrivere i servizi già installati, utilizza directory separate.

Per installare ulteriori servizi su Linux, aggiungi una nuova integrazione e procedi come di seguito:

1. Crea una nuova directory e copia i file dalla directory di installazione originale.
2. Apri il file injixo-cloud-link.toml.
3. Sostituisci il valore di **name** nella sezione **[app]** con un nuovo ID:

   ```
   [app]
name = "com.injixo.cloud-link.instance.1"
   ```

4. Installa e avvia il nuovo servizio dalla nuova directory come descritto in precedenza.

## Connettere Cloud Link all’integrazione

L’installazione di Cloud Link mostra il seguente messaggio, che include un PIN:

```
** Before you are able to run the client,
** link it to your injixo account:
**  1) Log in to injixo.com
**  2) Visit https://www.injixo.com/account/integrations
**  3) Select an integration you want to connect the client to
**  4) Enter your pin: 424242 (expires in 5 minutes)
```

1. Torna alla pagina **Aggiungi una nuova integrazione** nel browser.
2. Nella sezione **injixo Cloud Link**, inserisci il PIN a sei cifre nel campo **PIN mostrato durante l’installazione**.
3. Clicca su _Collega_{:.doc-button}.
   Cloud Link si connette a injixo. Continua a configurare la tua {% link_new integrazione on-premise | features/acd-integration/cloud/add-on-premise-integration.md %} o l’{% link_new integrazione CSV | features/acd-integration/cloud/add-csv-integration.md %}.

## Connettersi tramite un server proxy

Per connettersi tramite un server proxy, è necessario aggiungere il nome host o l’indirizzo IP del proxy alla variabile d’ambiente **https_proxy**:

- Windows: aggiungi la variabile d’ambiente alla sezione Variabili di sistema. Se i servizi non girano con l’account LocalSystem, configura una variabile utente.
- Linux: imposta la variabile d’ambiente in /etc/environment oppure in etc/profile.d

Esempio: `https_proxy=http://your.proxy.example`

Se è necessario, puoi aggiungere il numero della porta (se non si tratta della porta 80) e le credenziali dell’utente per l’autenticazione.

Esempio:`https_proxy=http://username:password@your.proxy.example:8080`

## Condividere gli indirizzi IP di destinazione <!-- rethink the name -->

Per permettere a injixo Cloud Link di connettersi ai server cloud di injixo, condividi le URL seguenti:

- injixo-*.s3-eu-west-1.amazonaws.com
- www.injixo.com

Non è possibile condividere un indirizzo IP individuale. I processi di distribuzione e aggiornamento modificano periodicamente gli indirizzi IP dei server. Valuta l’idea di installare injixo Cloud Link nella rete DMZ. Se la connessione al server non riesce, il file di registro conterrà dei [messaggi di errore socket Windows](https://docs.microsoft.com/it-it/windows/win32/winsock/windows-sockets-error-codes-2).

## Registrazione

injixo Cloud Link ruota i file di registro ogni giorno e dopo ogni riavvio, ma non li elimina. I registri attuali sono contenuti in injixo-cloud-link.log. I registri che vengono ruotati includono la data di rotazione nel nome del file. Dovrai impostare un’eliminazione regolare oppure procedere manualmente.

### Attivare la registrazione dettagliata

Per le integrazioni con database, injixo Cloud Link supporta la modalità di registrazione dettagliata. Quando questa modalità è attivata, il file di registro include il numero totale delle righe estratte e le prime 10 righe di dati per ogni richiesta.

Per attivare la registrazione dettagliata, segui questi passaggi:

1. Metti in pausa injixo Cloud Link.
2. Nella directory di installazione, apri il file injixo-cloud-link.toml.
3. Nella sezione **[app]**, imposta **verbose** come true:

   ```
   [app]
verbose = true
   ```

4. Salva il file e riavvia injixo Cloud Link.

## Configurare la cartella di importazione

Per impostazione predefinita, injixo Cloud Link carica i file che sono salvati nella sua cartella di installazione. Per le integrazioni CSV, è possibile configurare una cartella di importazione personalizzata seguendo questi passaggi:

1. Metti in pausa injixo Cloud Link.
2. Nella directory di installazione, apri il file injixo-cloud-link.toml.
3. Nella sezione **[app]**, imposta la tua cartella d’importazione come valore per **importDirectory**.
   - Utilizza percorsi relativi o assoluti.
   - Utilizza una seconda barra rovesciata come sequenza di escape per le barre rovesciate.
4. Salva il file e riavvia injixo Cloud Link.

## Domande frequenti

<style>
table th:first-of-type {
    width: 25%;
}
table th:nth-of-type(2) {
    width: 75%;
}
</style>

| Domanda                                                                        | Risposta                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Come posso ottenere un nuovo PIN se il primo è scaduto?                              | Metti in pausa injixo Cloud Link. Inserisci il nuovo PIN dal file di registro nell’apposito campo a sei cifre della sezione **injixo Cloud Link** della pagina di configurazione.                                                                                                                                                                                                                                                      |
| Come posso eliminare Cloud Link dal mio sistema?                                      | 1\. Avvia di nuovo il programma di installazione Cloud Link, oppure vai su _Programmi > Programmi e funzionalità_{:.breadcrumbs} in Windows.<br>2\. Fai clic con il tasto destro sulla voce **injixo Cloud Link** nell’elenco e seleziona **Disinstalla** o **Disinstalla/Cambia**.<br>3\. Segui le istruzioni sullo schermo.<br><br>Per disinstallare altre istanze, vai su _Programmi > Programmi e funzionalità_{:.breadcrumbs} in Windows e segui i passaggi 2 e 3. |
| Come posso spostare injixo Cloud Link su un nuovo server?                                | 1\. Clicca sull’{% icon pencil %} a destra di un’integrazione per modificarla.<br>2\. Clicca su **Collega una nuova installazione di injixo Cloud Link**.<br>3\. Scarica di nuovo injixo Cloud Link, se è necessario, e installa il programma sul nuovo server.                                                                                                                                                                          |
| Come posso modificare l’integrazione per un’installazione di injixo Cloud Link esistente? | 1\. Vai nella directory di installazione e copia il PIN dal file di registro.<br>2\. Elimina l’integrazione esistente e crea una nuova integrazione.<br>3\. Connetti il servizio injixo Cloud Link in corso alla nuova integrazione. Per farlo, inserisci il PIN durante la configurazione della nuova integrazione.                                                                                                               |
