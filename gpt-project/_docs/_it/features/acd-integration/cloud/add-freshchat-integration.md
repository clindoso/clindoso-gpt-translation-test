---
title: Aggiungere un'integrazione Freshchat
description: Impara come collegare il tuo sistema CRM Freshchat a injixo per importare dati.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
redirect_from:
  - /it/add-freshdesk-messaging-integration/
redirect_reason: Updated filename on 15 September 2023
---

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Aggiungere un'integrazione Freshchat

Per aggiungere una nuova integrazione Freshchat in injixo, devi avere un account Freshchat del tipo Pro o Enterprise.

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nel riquadro **Freshworks**, clicca su _Seleziona modello_{:.doc-button}.
4. Nella sezione **Freshchat**, clicca su _Aggiungi integrazione_{:.doc-button}.

## Configurare una nuova integrazione Freshchat

1. Inserisci un nome unico per l’integrazione che identifichi l’origine dei dati.
2. Nella sezione **Credenziali**, inserisci il nome completo del tuo dominio Freshchat, incluso il sottodominio, per esempio: esempio.freshchat.com.
3. Vai su Freshchat e copia una chiave API valida di un utente con il ruolo di Account Administrator.
4. Torna su injixo e incolla la chiave API nel campo **Chiave API**.
5. Clicca su _Salva integrazione_{:.doc-button}.

### Installare l’app injixo

L'integrazione Freshchat richiede un'applicazione client. Dopo aver salvato la configurazione, potrai accedere alla sezione **Installare l'app injixo** in fondo alla pagina.

Genera la **chiave API di injixo** e incollala in questa sezione.

Per impostare l’app injixo nel tuo account Freshchat, segui le istruzioni sullo schermo. Per altre informazioni, consulta il [Freshworks marketplace](https://www.freshworks.com/apps/injixo_connect).

## I dati Freshchat in injixo

### Contatti

In Freshchat, una chat di solito contiene diverse conversazioni che avvengono tra i tuoi colleghi e i clienti. In injixo, ogni chat risolta viene contata come un contatto, indipendentemente dal numero di conversazioni.

Esempio: un cliente apre una chat sul sito, un collega risponde, ma risolve il problema e la conversazione il giorno dopo, perché non aveva tutte le informazioni necessarie. injixo considera queste interazioni come un contatto solo.

### Convenzione sul nome delle code di origine

Le code di origine che injixo crea dalle chat seguono questa convenzione:

"nome del gruppo"

Esempi:

- Customer Support
- Undefined_Queue

### Chat eliminate e chat spam

Una chat può essere eliminata o contrassegnata come spam quando viene aggiornata. In questo caso, l’integrazione non può determinare il nome del gruppo. Le code di origine che contano queste chat sono etichettate come Undefined_Queue. Generalmente, queste code sono irrilevanti ai fini della pianificazione del workload dei dipendenti.

## Domande frequenti

| Domanda                                                                                                                                                                       | Risposta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| injixo smette improvvisamente di mostrare nuovi dati di Freshchat ma in **Account > Integrazioni** l’integrazione Freshchat ha ancora lo stato Operativo. Che cosa posso fare? | L'app injixo ottiene dati da Freshchat e invia eventi a injixo. In caso di errori di comunicazione tra l'app injixo e injixo, i dati di Freshchat potrebbero non essere più visualizzati. L'integrazione Freshchat non è in grado di rilevare eventuali errori di comunicazione.<br><br>Verifica che la chiave API di injixo che hai inserito durante la configurazione dell'app injixo nel tuo account Freshchat sia ancora valida. Se la chiave API non è più valida, aggiorna la chiave API di injixo nella pagina di installazione dell'app injixo. Se la chiave API è ancora valida, contatta l’assistenza di injixo. |
