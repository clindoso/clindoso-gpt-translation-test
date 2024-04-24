---
title: Aggiungere un’integrazione Zendesk
description: Scopri come collegare il tuo sistema CRM Zendesk a injixo per importare dati.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Un'integrazione Zendesk è un'integrazione cloud che importa da Zendesk Support e Zendesk Talk i volumi di contatto relativi a email, moduli web, chat, chiamate e messaggi social. 

L’integrazione importa soltanto le chiamate in entrata (non quelle in uscita). Il tempo medio di gestione (AHT) è disponibile soltanto per Zendesk Talk.

È la prima volta che ti occupi di integrazioni? Meglio cominciare dalle {% link_new basi | features/acd-integration/cloud/how-integrations-work.md %}.

## Aggiungere un’integrazione Zendesk

Nel tuo account Zendesk, crea un token API per un utente con [Autorizzazioni amministrative](https://support.zendesk.com/hc/it/articles/4408843355290-Quali-autorizzazioni-sono-necessarie-per-il-profilo-per-l-integrazione-Zendesk-per-Salesforce-).

Per aggiungere un’integrazione Zendesk in injixo, segui questi passaggi:

1. Vai su _Account > Integrazioni_{:.breadcrumbs}.
2. Se ci sono già altre integrazioni, clicca su _Aggiungi integrazione_{:.doc-button}.
3. Nel riquadro di Zendesk, clicca su _Aggiungi integrazione_{:.doc-button}.
4. Inserisci un nome unico per la nuova ntegrazione che identifichi l’origine dei dati.
5. Nella sezione **Credenziali utente**, inserisci le tue credenziali Zendesk:
   * Inserisci il nome completo del tuo dominio Zendesk, incluso il sottodominio, per esempio: example.zendesk.com.
   * Inserisci il tuo nome utente Zendesk.
   * Inserisci il tuo token API.
6. Nella sezione **Configurazione**, seleziona una strategia di raggruppamento. Scegli l'opzione **IVR (Interactive Voice Response)** o **Numero di telefono**. La strategia determina il modo in cui [injixo assegna i nomi alle code di origine](#nomi-delle-code-per-zendesk-talk) per le viste di Zendesk Talk. L'opzione IVR utilizza il gruppo di destinazione. L’opzione Numero di telefono utilizza il numero di telefono del ricevente per generare il nome della coda di origine. Le chiamate senza le informazioni rilevanti verranno visualizzate come non raggruppate. Questo non riguarda le code di origine per Zendesk Support.

   > Dopo aver salvato la configurazione dell’integrazione in injixo, non sarà più possibile cambiare la strategia di raggruppamento.

7. Clicca su _Salva integrazione_{:.doc-button}.

## I dati Zendesk in injixo

### Ticket e interazioni

Un ticket Zendesk di solito comprende diverse interazioni tra i membri del tuo team e i clienti, avvenute tramite diversi canali di comunicazione.

Ogni interazione rappresenta un compito che i membri del tuo team devono portare a termine. Un’interazione può creare un nuovo ticket, oppure modificare un ticket esistente.

Esempio: un utente apre un ticket mandando un’email. Un membro del team risponde all’email e così facendo chiude il ticket. Due giorni dopo, l’utente manda un’email di risposta, il che riapre il ticket. Nonostante lo scambio di email sia incluso in un solo ticket, injixo conta due email.

### Viste

injixo genera code di origine in base alle viste Zendesk. Dopo la prima importazione, vedrai una coda di origine per ogni vista che hai creato in Zendesk. Se una vista contiene eventi da canali diversi (per esempio chat e email), questi verranno visualizzati in {% link_new canali | features/forecast/injixo-forecast/create-workloads.md | #code-e-canali %} separati in injixo.

Nota: aggiungere delle viste Zendesk dopo aver salvato l’integrazione genererà automaticamente delle nuove code di origine e relativa cronologia in injixo.

### Viste non supportate

injixo genera code di origine per la maggior parte delle viste, ma al momento non supporta le viste che utilizzano i seguenti campi ticket:

- Orari di attività
- SLA
- Canale
- Qualifiche
- Condizioni con valori specifici per l’utente (per esempio, Assignee è (current user))

Se utilizzi viste Zendesk con condizioni che si riferiscono almeno a uno dei campi ticket qui sopra, injixo ignorerà queste viste e non genererà le relative code.

### Mappatura dei canali Zendesk in injixo

Ogni evento che modifica un ticket Zendesk potrebbe essere contato in diversi canali in injixo.

Esempio: un’email creerà un ticket che verrà visualizzato in una coda di email in injixo. Se lo stesso ticket finisce in una vista chat, injixo lo includerà anche in una coda di chat.

| Canale Zendesk                           | injixo       |
| ----------------------------------------- | ------------ |
| email                                     | email        |
| mobile                                    | email        |
| web                                       | email        |
| chat                                      | chat         |
| native_messaging                          | chat         |
| sms                                       | social_media |
| any_channel                               | social_media |
| facebook                                  | social_media |
| twitter                                   | social_media |
| sunshine_conversations_facebook_messenger | social_media |
| instagram_dm                              | social_media |
| voice                                     | call         |
| api                                       | case         |
| answer_bot_for_web_widget                 | case         |
| chat_transcript                           | case         |
| mobile_sdk                                | case         |
| whatsapp                                  | social_media |

### Nomi delle code per Zendesk Support

I nomi delle code di origine per Zendesk Support seguono questa convenzione:

‘nome della vista (canale injixo)’

Esempio:

- Ticket di supporto (chat)

### Nomi delle code per Zendesk Talk

I nomi delle code di origine per Zendesk Talk seguono questa convenzione:

‘Calls Inbound For + strategia di raggruppamento’

Esempi:

- Calls Inbound For +49123456789 (Numero di telefono)
- Calls Inbound For Senior Agents (IVR)
- Calls Inbound Ungrouped
