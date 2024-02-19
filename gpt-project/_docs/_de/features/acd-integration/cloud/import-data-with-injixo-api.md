---
title: Daten über injixo API importieren
navigation_title: injixo API
product_label:
  - advanced
  - enterprise
description: Füge eine injixo API-Integration hinzu, um Kontakt- und Agentenstatus-Daten von deinem externen System zu importieren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/dashboards-overview.md
---

In injixo findest du herstellerspezifische und universelle Integrationen, um Kontakt- und Agentenstatus-Daten aus externen Systemen zu importieren.

## Was ist eine injixo API-Integration?

In injixo Advanced und Enterprise WFM kannst du mit injixo API-Integrationen API-Anfragen senden, um Daten zu importieren (wenn es z.&nbsp;B. keine Standardintegration für dein externes System gibt). Dafür stellt die injixo API folgende Ressourcen bereit:

- [Ressource für Kontaktereignisse](https://api.injixo.com/resources/integration_contact_event/): Kontaktereignisse werden aufgezeichnet, wenn Kunden dein Unternehmen per Anruf, E-Mail oder Chat kontaktieren. injixo speichert diese Daten in Queues, die nach Queue-Name und Kanal gruppiert werden.
- [Ressource für Agentenstatus](https://api.injixo.com/resources/integration_agent_status/): Agentenstatus-Daten werden aufgezeichnet, wenn deine Mitarbeiter von einer Aktivität zur nächsten wechseln, z.&nbsp;B. Anmeldung, Nachbearbeitungszeit oder Abmeldung.

## injixo API-Integration hinzufügen

Benutzer mit Admin-Zugriff können eine injixo API-Integration wie folgt hinzufügen:

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Wenn es bereits eine Integration gibt, klicke auf _Integration hinzufügen_{:.doc-button}.
3. Klicke in der Kachel **Universal Interfaces** auf _Modell auswählen_{:.doc-button}.
4. Klicke im Abschnitt **injixo API** auf **Integration hinzufügen**.
5. Gib einen eindeutigen Namen für die neue Integration ein.
6. Klicke auf **Integration speichern**.<br>Der Abschnitt **Zugriff auf die injixo API** wird verfügbar.
7. Um den injixo API-Schlüssel zu erzeugen, klicke auf _Generieren_{:.doc-button}.

Die Authentifizierung funktioniert auch mit persönlichen Zugangstoken, die in Benutzerprofilen im Abschnitt {% link_new **Persönliche Zugangstoken** | features/reporting/injixo-api/injixo-api.md | #autorisierung-persönlicher-zugangstoken %} erstellt wurden.

> Du kannst den API-Schlüssel später nicht mehr abrufen. 
>
> - Lege den API-Schlüssel an einem sicheren Ort ab, z.&nbsp;B. in deinem Passwort-Manager.
> - Der aktuelle API-Schlüssel läuft ab, wenn ein Benutzer einen neuen API-Schlüssel für die Integration erzeugt oder die Integration löscht.

## Importdaten <a id="import-contact-or-agent-status-data">

Zur Identifikation der API-Integration und zur Authentifizierung, füge den injixo API-Schlüssel und die Konfigurations-ID der Integration zu deinen API-Anfragen hinzu:

1. Füge deinen injixo API-Schlüssel zum Header deiner Authentifizierungsanfrage hinzu.
2. Suche oder kopiere die Konfigurations-ID deiner Integration:
    - Gehe zu _Account > Integrationen_{:.breadcrumbs}.
    - Klicke in der Kachel mit deiner API-Integration auf das {% icon pencil %}.
    - Klicke im Abschnitt **Zugriff auf die injixo API** auf _{% icon clone | icon-only %} Kopieren_{:.doc-button}.
3. Füge die Konfigurations-ID deiner Integration zum Objekt **meta** im Body deiner Anfrage hinzu.

Damit regelmäßig Daten von deinem externen System zu injixo importiert werden, musst du deine eigene Anwendung ausführen. Sieh dir die [injixo API-Dokumentation](https://api.injixo.com) an, um Beispielskripte in Ruby und Python zu finden.

## Datenimport testen

Zum Testen kannst du einzelne POST-Anfragen an die API senden. Das Datenarray in den folgenden Beispielen enthält einen einzelnen Datenpunkt, den du bei Bedarf ändern kannst. Ersetze mindestens den Beispiel API-Schlüssel (abc123456=) und den Beispielwert integrationConfigurationId (1234) mit deinen eigenen Werten.

Die API unterstützt nur HTTPS. Sende deine Anfragen an https://api.injixo.com, um Fehler der Kategorie `not_found`zu vermeiden.

### cURL auf der Befehlszeile

Die folgenden Beispiele zeigen, wie Daten mit [cURL](https://curl.se/) an die API gesendet werden können. cURL ist ein Befehlszeilentool, das über ein Terminal Daten mit einem Server austauscht.

Kontaktereignisse:

```
curl -X POST \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer abc123456=" \
 -d '{"data":[{"properties":{"offered":true,"handled":false,"duration":124.6},"queueName":"Level-1-Support","queueIdentifier":"1337_99","timestamp":"2021-12-06T10:34:22Z","channel":"calls"}],"meta":{"integrationConfigurationId":1234}}' \
 https://api.injixo.com/external-systems/contact-events
```

Hinweis: Jede neue Kombination von `queueIdentifier`, `queueName` und `integrationConfigurationId` erzeugt eine neue Queue. Um zu vermeiden, dass Queue-Namen mehrfach verwendet werden, stelle sicher, dass derselbe queueIdentifier bzw. dieselbe integrationConfigurationId in jeder Anfrage mit demselben Queue-Namen verwendet wird. 

Agentenstatus:

```
curl -X POST \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer abc123456==" \
 -d '{"data":[{"agentIdentifier":"tina@meinunternehmen.de","activityIdentifier":"Test","startTime":"2021-12-06T10:00:00Z","endTime":"2021-12-06T15:00:00Z"}],"meta":{"integrationConfigurationId":8431,"externalSystem":"Meine ACD"}}' \
 https://api.injixo.com/external-systems/agent-statuses
```

### REST-Clients

Die folgenden Beispiele zeigen, wie du mit einem REST-Client wie [Postman](https://www.postman.com/downloads/) Daten an die API senden kannst.

1. Füge einen JSON-Anfrage-Header hinzu:

   ```
   {
  "Content-type": "application/json",
  "Authorization": "Bearer abc123456="
}
   ```

2. Füge jeweils einen JSON-Anfrage-Body für Kontaktereignisse bzw. Agentenstatus-Daten hinzu.<br><br>

   Beispiel für einen Anfrage-Body für Kontaktereignisse: `/external-systems/contact-events`

   ```
   {
  "data": [
    {
      "properties": { "offered": true, "handled": false, "duration": 124.6 },
      "queueName": "Level-1-Support",
      "queueIdentifier": "1337_99",
      "timestamp": "2021-12-06T10:34:22Z",
      "channel": "calls"
    },
    {
      "properties": { "offered": true, "handled": true, "duration": 200.1 },
      "queueName": "Level-1-Support",
      "queueIdentifier": "1337_99",
      "timestamp": "2021-12-06T10:46:22Z",
      "channel": "calls"
    }
  ],
  "meta": { "integrationConfigurationId": 1234 }
}
   ```

   Beispiel für einen Anfrage-Body für Agentenstatus: `/external-systems/agent-statuses`

   ```
   {
  "data": [
    {"agentIdentifier":"tina@meinunternehmen.de","activityIdentifier":"Test","startTime":"2022-12-06T08:00:00Z","endTime":"2022-12-06T13:00:00Z"},
    {"agentIdentifier":"tina@meinunternehmen.de","activityIdentifier":"Test","startTime":"2022-12-07T09:00:00Z","endTime":"2022-12-07T10:00:00Z"}
  ],
  "meta": {
    "integrationConfigurationId": 1234,
    "externalSystem": "Meine ACD"
  }
}
   ```

## Deine erste API-Anfrage - und jetzt?

Nachdem du eine erfolgreiche API-Anfrage gesendet hast, dauert es etwas, bevor du Daten in injixo sehen kannst. Du kannst mit den importierten Daten wie folgt arbeiten:

- Anfragen für Kontaktereignisse: Unter **Forecast** zeigen die Seiten **Neuer Workload** und **Workload bearbeiten** die importierten Queues an, wenn Daten verarbeitet wurden.
- Anfragen für Agentenstatus-Daten: Aus der ersten Anfrage mit neuen Agentenkennungen ergeben sich keine tatsächlichen Agentenstatus-Daten im Schicht Center. Damit du Daten sehen kannst, {% link_new ordne einem Mitarbeiter mindestens eine externe Benutzerkennung zu | features/acd-integration/cloud/import-agent-status-data.md | #mitarbeitern-externe-benutzerkennungen-in-injixo-zuordnen %}. Diese wurden in der Anfrage als agentIdentifier gesendet. Du musst dann eine weitere Anfrage senden, um Daten anzuzeigen.
