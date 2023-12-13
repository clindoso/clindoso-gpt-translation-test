---
title: Importare dati con l’API injixo
navigation_title: injixo API
product_label:
  - advanced
  - enterprise
description: Aggiungi un’integrazione con l’API injixo per importare dati sui contatti e sugli status agenti dal tuo sistema esterno.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
  - overwrite_title: Gestire le dashboard
    filepath: features/monitoring/dashboards/dashboards-overview.md
---

injixo utilizza integrazioni specifiche per alcuni sistemi esterni e integrazioni universali per importare dati sui contatti e sugli status agenti da sistemi esterni.

## Che cos’è un’integrazione API injixo?

In injixo Advanced ed Enterprise WFM, le integrazioni API injixo permettono di inviare richieste API per importare dati (per esempio, nel caso in cui non esista un’integrazione standard per il tuo sistema esterno). Per poter fare questo, l’API di injixo fornisce le seguenti risorse:

- [Risorsa per gli eventi di contatto](https://api.injixo.com/resources/integration_contact_event/): gli eventi di contatto vengono registrati quando i clienti contattano la tua organizzazione via telefono, email o chat. injixo archivia questi dati in code che sono raggruppate in base al nome della coda e al canale.
- [Risorsa per gli stati degli agenti](https://api.injixo.com/resources/integration_agent_status/): i dati sugli stati degli agenti vengono registrati quando i dipendenti passano da un’attività a un’altra, come, per esempio, login, elaborazione post-chiamata, logout.

## Aggiungere un’integrazione API injixo

Gli utenti con accesso amministratore possono aggiungere un’integrazione API injixo seguendo questa procedura:

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nella sezione **Universal Interfaces**, clicca su _Seleziona modello_{:.doc-button}.
4. Nella sezione **injixo API** clicca su **Aggiungi integrazione**.
5. Inserisci un nome unico per l’integrazione.
6. Clicca su **Salva integrazione**.<br>La sezione **Accedi all’API di injixo** diventa disponibile.
7. Per generare la chiave API di injixo, clicca su _Generare_{:.doc-button}.

L’autenticazione funziona anche con i token di accesso personali che sono stati creati nei profili utenti nella sezione {% link_new **Personal access tokens** | features/reporting/injixo-api/injixo-api.md | #authorization-personal-access-token %}.

> In seguito non sarà più possibile accedere alla chiave API. 
>
> - Salva la chiave API in un luogo sicuro, come, per esempio, in un gestore di password.
> - La chiave API attuale scade se un altro utente genera una nuova chiave API per l’integrazione o se elimina l’integrazione.

## Importare dati <a id="import-contact-or-agent-status-data">

Per identificare l’integrazione API e per autenticarti, includi la chiave API di injixo e l’ID della configurazione dell’integrazione nelle richieste API:

1. Aggiungi la chiave API di injixo all’intestazione della richiesta di autorizzazione.
2. Trova o copia l'ID della configurazione dell'integrazione:
    - Vai su _Account > Integrazioni_{:.breadcrumbs}.
    - Nella sezione dell’integrazione API, clicca sull’{% icon pencil %}.
    - Nella sezione **Accedi all’API di injixo** clicca sull’_{% icon clone | icon-only %} Copia_{:.doc-button}.
3. Aggiungi l’ID della configurazione dell’integrazione all’oggetto **meta** nel corpo della richiesta.

Per importare regolarmente dati dal sistema esterno verso injixo, dovrai avviare una tua applicazione. Trovi degli script di esempio in Ruby e Python nella guida utente della [documentazione sull’API injixo](https://api.injixo.com) (in inglese).

## Testare le importazioni di dati

Per i test, puoi inviare singole richieste POST all’API. L’array di dati negli esempi che seguono contiene un solo punto dati, ma puoi modificarlo se è necessario. Sostituisci almeno la chiave API di injixo di esempio (abc123456=) e il valore di integrationConfigurationId (1234) con i tuoi valori.

L’API supporta soltanto HTTPS. Invia le richieste a https://api.injixo.com per evitare errori del tipo `not_found`.

### cURL sulla riga di comando

L’esempio seguente mostra come inviare dati all’API utilizzando [cURL](https://curl.se/). cURL è uno strumento a riga di comando che scambia dati con un server tramite un terminal.

Eventi di contatto:

```
curl -X POST \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer abc123456=" \
 -d '{"data":[{"properties":{"offered":true,"handled":false,"duration":124.6},"queueName":"Level 1 support","queueIdentifier":"1337_99","timestamp":"2021-12-06T10:34:22Z","channel":"calls"}],"meta":{"integrationConfigurationId":1234}}' \
 https://api.injixo.com/external-systems/contact-events
```

Nota: ogni nuova combinazione di `queueIdentifier`, `queueName`, e `integrationConfigurationId` creerà una nuova coda. Per evitare duplicati tra i nomi delle code, assicurati di aggiungere lo stesso queueIdentifier o lo stesso integrationConfigurationId per ogni richiesta con lo stesso nome di coda. 

Stati degli agenti:

```
curl -X POST \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer abc123456==" \
 -d '{"data":[{"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2021-12-06T10:00:00Z","endTime":"2021-12-06T15:00:00Z"}],"meta":{"integrationConfigurationId":8431,"externalSystem":"My ACD"}}' \
 https://api.injixo.com/external-systems/agent-statuses
```

### Client REST

L’esempio seguente mostra come inviare dati utilizzando un client REST, come [Postman](https://www.postman.com/downloads/).

1. Includi un’intestazione di richiesta JSON:

   ```
   {
  "Content-type": "application/json",
  "Authorization": "Bearer abc123456="
}
   ```

2. Includi un corpo di richiesta JSON diverso per i dati sugli eventi di contatto e per i dati sugli stati degli agenti.<br><br>

   Esempio di corpo della richiesta per gli eventi di contatto: `/external-systems/contact-events`:

   ```
   {
  "data": [
    {
      "properties": { "offered": true, "handled": false, "duration": 124.6 },
      "queueName": "Level 1 support",
      "queueIdentifier": "1337_99",
      "timestamp": "2021-12-06T10:34:22Z",
      "channel": "calls"
    },
    {
      "properties": { "offered": true, "handled": true, "duration": 200.1 },
      "queueName": "Level 1 support",
      "queueIdentifier": "1337_99",
      "timestamp": "2021-12-06T10:46:22Z",
      "channel": "calls"
    }
  ],
  "meta": { "integrationConfigurationId": 1234 }
}
   ```

   Esempio di corpo della richiesta per gli stati degli agenti: `/external-systems/agent-statuses`:

   ```
   {
  "data": [
    {"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2022-12-06T08:00:00Z","endTime":"2022-12-06T13:00:00Z"},
    {"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2022-12-07T09:00:00Z","endTime":"2022-12-07T10:00:00Z"}
  ],
  "meta": {
    "integrationConfigurationId": 1234,
    "externalSystem": "My ACD"
  }
}
   ```

## La prima richiesta API, e dopo?

Dopo aver inviato la prima richiesta API, è necessario aspettare prima di poter vedere i dati in injixo. Puoi lavorare con i dati importati come descritto di seguito:

- Richieste di eventi di contatto: in Forecast, le pagine Nuovo workload e Modifica workload mostreranno le code importate dopo che i dati saranno stati processati.
- Richieste di dati sugli stati degli agenti: la prima richiesta con nuovi ID agente non genererà dati effettivi sugli stati degli agenti nel Centro dei turni. Per visualizzare dei dati, devi {% link_new associare almeno un identificatore esterno | features/acd-integration/cloud/import-agent-status-data.md | #associare-gli-identificatori-degli-utenti-esterni-ai-dipendenti-in-injixo %} (inviato come agentIdentifier) a un dipendente. Per poter visualizzare i dati è necessario inviare un'altra richiesta.
