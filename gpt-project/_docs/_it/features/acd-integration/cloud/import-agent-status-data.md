---
title: Importare i dati sugli stati degli agenti
product_label:
  - advanced
  - enterprise
  - classic
description: Configura injixo per importare correttamente i dati relativi agli stati degli agenti.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-on-premise-integration.md
---

I sistemi esterni, come i sistemi ACD, registrano quando i dipendenti passano da un’attività a un’altra. injixo può utilizzare questi dati a supporto della gestione intraday.

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Prerequisiti

Per importare i dati sugli stati degli agenti, devi {% link_new aggiungere un’integrazione | features/acd-integration/cloud/how-integrations-work.md %}. L’integrazione deve supportare le importazioni dei dati sugli stati degli agenti.

Per vedere se la tua integrazione supporta le importazioni dei dati sugli stati degli agenti, vai su _Account > Integrazioni_{:.breadcrumbs}. Se le importazioni sono supportate, vedrai le etichette Stati degli agenti (dati storici) e/o RTA (tempo reale).

Dopo aver aggiunto l’integrazione, dovrai aggiungere ai dipendenti in injixo gli identificatori degli utenti esterni. Hai anche la possibilità di riassegnare le attività dei sistemi esterne alle attività corrispondenti in injixo.

## Identificatori degli utenti esterni

Gli identificatori degli utenti sono specifici per ogni sistema esterno. Identificano gli utenti nei sistemi esterni in base all’indirizzo email, al nome utente o all’ID dell’agente.

Per evitare che le importazioni non vadano a buon fine, presta attenzione alla corretta grafia, ai caratteri maiuscoli e minuscoli e agli spazi.

| Sistema esterno                 | Identificatore utente necessario              |
| ---------------------- | ------------------------------------- |
| Five9                  | Nome utente in Five9                  |
| Genesys Cloud          | Nome utente in PureCloud              |
| Genesys Engage         | Nome utente in PureEngage             |
| Talkdesk               | Indirizzo email utilizzato in Talkdesk        |
| UJET                   | Indirizzo email utilizzato in UJET            |
| Sikom                  | Nome utente in Sikom                  |
| Mitel MiVoice Business | Nome utente in Mitel MiVoice Business |
| Vonage                 | ID agente in Vonage                  |
| Avaya CMS              | Nome utente in Avaya CMS              |

## Associare gli identificatori degli utenti esterni ai dipendenti in injixo

Per importare dati, devi associare gli identificatori degli utenti esterni ai dipendenti. È possibile associarli a tutti i dipendenti oppure solo ai dipendenti per i quali vuoi importare dati sugli stati degli agenti.

1. Vai su _WFM > Administration > Scheduling > Dipendenti_{:.breadcrumbs} e seleziona un dipendente.
2. In alto, clicca su **Sistemi esterni**, o scorri fino alla sezione **Sistemi esterni**.
3. Clicca sull’icona Aggiungi{% icon item-add | icon-only %} per aggiungere un sistema esterno.  
   Si aprirà una finestra.
4. Nel menu a tendina **Sistema esterno**, seleziona l’integrazione che hai impostato in precedenza.
5. Nel campo **ID del dipendente nel sistema esterno**, aggiungi un numero che identifichi il dipendente in modo univoco, come, per esempio, il suo numero di matricola.
6. Nel campo **Estensione**, inserisci l’identificatore utente del sistema esterno, come, per esempio, l’indirizzo email del dipendente.
7. Clicca su _OK_{:.doc-button}.

Dopo che avrai aggiornato le sezioni dei dipendenti, l’importazione successiva importerà i dati sugli stati degli agenti.

## Riassociare le attività esterne

Le attività esterne sono le attività che il sistema esterno registra quando i dipendenti fanno il login e il logout, o quando passano da un’attività a un’altra, per esempio, dalle email alle chiamate.

È possibile riassociare le attività esterne ad attività già esistenti. Se invece decidi di {% link_new creare nuove attività | features/administration/activities.md | #creare-unattività %}, aggiungile alla tua {% link_new unità di pianificazione | features/administration/create-and-manage-planning-units.md | #add-activities %} per visualizzarle correttamente in seguito.

Per impostazione predefinita, le integrazioni registrano le attività nell’attività Presente (ID 1) e lo stato dell’agente sarà Presente per tutte le attività. injixo può mostrare le stesse attività del tuo sistema esterno. Per far questo, devi riassociare le attività esterne ad altre attività in injixo seguendo la procedura qui di seguito.


Per riassociare le attività, devi prima mettere in pausa l'integrazione:

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Nell'elenco delle integrazioni, clicca sull'icona Sospendi l'importazione {% icon pause_circle | icon-only %} accanto all'integrazione per la quale desideri riassociare le attività.

Dopo aver messo in pausa l’integrazione, segui questi passaggi:

1. Vai su _Plan > Configurazione > Attività_{:.breadcrumbs}.
2. Seleziona l'attività che desideri riassociare.
3. Nella sezione **Sistemi Esterni**, clicca su _Modifica in WFM_{:.doc-button}.
4. Vai alla sezione **Sistemi esterni**.
5. Fare clic sull'icona Aggiungi {% icon item-add | icon-only %}.
6. Nella finestra **Sistemi Esterni**, segui questi passaggi:<br>
   - Nel menu a tendina **Sistema esterno**, seleziona l’integrazione.
   - Nel menu a tendina **Denominazione nel sistema esterno**, seleziona l’attività esterna che vuoi associare all’attività attualmente selezionata in injixo.
   - Nel menu a tendina **Classificazione**, seleziona il valore 1.
7. Clicca su _OK_{:.doc-button}.

Per riassociare altre attività, clicca sull’attività successiva e procedi dal menu di configurazione sulla destra.

Dopo aver terminato l’associazione delle attività, vai su _Account > Integrazioni_{:.breadcrumbs} e clicca sull’icona Riprendi l’importazione {% icon play_circle | icon-only %} accanto all’integrazione per riavviare l’importazione.
