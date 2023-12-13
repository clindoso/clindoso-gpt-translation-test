---
title: Aggiungere un’integrazione Freshdesk
description: Scopri come collegare il tuo sistema CRM Freshdesk a injixo per importare dati.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Un'integrazione Freshdesk è un'integrazione cloud che importa i volumi di contatto relativi a email, moduli web, chat e messaggi social.

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Aggiungere un’integrazione Freshdesk

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nel riquadro **Freshworks**, clicca su _Seleziona modello_{:.doc-button}.
4. Nella sezione **Freshdesk**, clicca su _Aggiungi integrazione_{:.doc-button}.

## Impostare un’integrazione Freshdesk

1. Inserisci un nome unico per l’integrazione che identifichi l’origine dei dati.
2. Nella sezione **Credenziali**, inserisci il nome completo del tuo dominio Freshdesk, incluso il sottodominio, per esempio: esempio.freshdesk.com.
3. Vai su Freshdesk e copia una chiave API valida di un utente con il ruolo di Account Administrator.
4. Torna su injixo e incolla la chiave API nel campo **API key**.
5. Clicca su _Salva integrazione_{:.doc-button}. 

## Installare l’app injixo

L’integrazione Freshdesk richiede un’applicazione client. Dopo aver salvato la configurazione, potrai accedere alla sezione **Installare l'app injixo** in fondo alla pagina.

Per generare e copiare la**chiave API injixo**, clicca su _Generare_{:.doc-button}.

Per impostare l’app injixo nel tuo account Freshdesk, segui le istruzioni sullo schermo. Per altre informazioni, consulta il [Freshworks marketplace](https://www.freshworks.com/apps/freshdesk/injixo_connect).

## I dati Freshdesk in injixo

injixo importa da Freshdesk tutti i dati sui ticket. I ticket di solito contengono diverse conversazioni che avvengono tra i tuoi colleghi e i clienti.<br>
Nota: injixo non può importare da Freshdesk la durata dei ticket. Ecco perché in injixo Forecast non vedrai il grafico AHT per i workload con code Freshdesk.

### Ticket e conversazioni

In injixo, tutte le conversazioni vengono raggruppate in base al canale di comunicazione di Freshdesk (Source). Una conversazione può essere un nuovo ticket, oppure la risposta a un ticket esistente.

In injixo, le conversazioni in un ticket Freshdesk vengono contate separatamente come contatto in entrata.

Esempio: un utente apre un ticket mandando un’email. Una persona risponde all’email e così facendo chiude il ticket. Due giorni dopo, il ticket viene riaperto grazie a un’altra email, che apre una nuova conversazione.

Il numero di contatti in entrata in injixo di solito sarà maggiore rispetto al numero di ticket riportati in Freshdesk.

### Eventi da origini diverse

In un ticket Freshdesk, le risposte possono essere incluse in code injixo diverse utilizzando il canale Casi.

Esempio: quando c’è una risposta via email a un ticket, vedrai il contatto in una coda injixo che corrisponde al gruppo Freshdesk e al nome dell’origine. Una chat nello stesso ticket verrà inclusa in una coda separata.

### Convenzione sul nome delle code di origine

injixo crea le code di origine dai ticket. Le convenzioni sui nomi di queste code dipendono dalla fase dell’importazione dei dati (iniziale o continua). Durante l’importazione iniziale, il nome della coda di origine segue questa convenzione:

- "nome del gruppo + nome dell’origine + Tickets"
- "nome del gruppo + nome dell’origine + Replies"

Esempi:

- CustomerService chat Tickets
- CustomerService email Replies
- Unknown group/source Tickets

Un nuovo ticket creerà una nuova coda. La risposta a un ticket creerà una coda di risposte che registrerà anche tutte le altre risposte. Per ottenere tutte le informazioni su un ticket, è necessario prendere in considerazione sia il ticket che la coda delle risposte.

### Ticket eliminati e ticket spam

Quando un ticket che è già stato eliminato o contrassegnato come spam viene modificato, non è possibile determinare il nome del gruppo e il nome dell’origine. La coda di origine che conta questi ticket sarà etichettata come Unknown group/source Tickets o Unknown group/source Replies. Generalmente, queste code sono irrilevanti ai fini della pianificazione del workload dei dipendenti.
