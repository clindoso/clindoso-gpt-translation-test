---
title: Gestire gli account utente
description: Visualizzare gli utenti fatturati e non fatturati. Creare, modificare ed eliminare gli utenti. Gestire l’accesso degli utenti con l’aggiunta di ruoli utente.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-2fa.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
redirect_from:
  - /it/user-administration/
redirect_reason: page used in intercom, updated filename on 06 December 2022
---

Configura gli account utente in injixo per gestire i dipendenti della tua organizzazione. 

In _Account > Utenti_{:.breadcrumbs} vedrai una panoramica completa di tutti gli utenti:
- Utenti fatturati: questa scheda mostra tutti gli utenti attivi nel tuo tenant injixo.
- Utenti non fatturati: questa scheda mostra tutti gli {% link_new utenti disattivati | features/administration/deactivate-employees.md %} che non possono più accedere a injixo. Gli utenti disattivati non vengono più conteggiati nella {% link_new fatturazione | getting-started/how-does-billing-work.md %} della tua organizzazione.

Per trovare uno o più utenti, utilizza il campo di ricerca sopra l’elenco degli utenti. Utilizza una virgola per separare le parole chiave per la ricerca.
Per filtrare gli utenti in base al ruolo utente, clicca sulla colonna **Ruoli utente**. Si aprirà una finestra dove potrai selezionare uno o più ruoli. Tutti gli utenti che hanno almeno uno dei ruoli selezionati verranno visualizzati nell’elenco degli utenti.

## Creare gli utenti

Gli utenti sono anche chiamati dipendenti. In injixo, puoi creare gli utenti in tre moduli diversi:
- in _Account > Utenti_{:.breadcrumbs};
- in _WFM > Administration > Scheduling > Dipendenti_{:.breadcrumbs};
- in {% link_new People | features/people/manage-people.md | #creare-un-nuovo-dipendente %}.

> Nota
> 
> È sufficiente creare un utente una volta sola, in uno di questi moduli. injixo sincronizzerà automaticamente i dati dell’utente negli altri due moduli.

Per creare un utente, segui questi passaggi:

1. Vai su _Account > Utenti_{:.breadcrumbs}.
2. Clicca su _Crea utente_{:.doc-button}.
3. Compila i dati dell'utente e clicca su _Crea_{:.doc-button}.

## Modificare un account utente

In injixo, puoi modificare l’account di un utente in due moduli diversi, a seconda di ciò che vuoi fare. La tabella qui sotto fornisce una panoramica delle diverse opzioni di configurazione e dei relativi moduli in injixo. Puoi accedere a entrambi i moduli anche da People.

| Che cosa voglio fare                                          | Dove posso farlo in injixo                                                                             |
| -------------------------------------------------- | ------------------------------------------------------------------------------------- |
| {% link_new Configurare le impostazioni relative alla pianificazione di un utente, | features/administration/employee-overview.md | #panoramica-delle-impostazioni-del-dipendente %} (per esempio, assegnare le attività, aggiungere le qualifiche, definire le disponibilità). | _WFM > Administration > Scheduling > Dipendenti_{:.breadcrumbs} |
| {% link_new Modificare le informazioni sul periodo di assunzione di un utente |  getting-started/manage-user-accounts.md | #disattivare-un-account-utente %}.       | _WFM > Administration > Scheduling > Dipendenti_{:.breadcrumbs} |   
| Modificare la lingua e il fuso orario di un utente. | _Account > Utenti_{:.breadcrumbs} |
| {% link_new Assegnare un ruolo utente a un utente | getting-started/configure-user-roles.md | #assegnare-ruoli-utente-agli-utenti %}. | _Account > Utenti_{:.breadcrumbs} |
| {% link_new  Imporre l’autenticazione a due fattori (2FA) | getting-started/manage-2fa.md %}.   | _Account > Utenti_{:.breadcrumbs} |

Se vuoi modificare un utente, per esempio cambiare il suo indirizzo email, segui questi passaggi:

1. Vai su _Account > Utenti_{:.breadcrumbs}.
2. Clicca sul nome utente di un utente esistente.
3. Cambia le impostazioni dell’utente.
4. Clicca su _Salva_{:.doc-button}.

### Concedere a un utente l’accesso come amministratore

1. Vai su _Account > Utenti_{:.breadcrumbs}.
2. Clicca sul nome utente di un utente esistente.
3. Nella sezione **Accesso amministratore**, spunta la casella **Concedi l'accesso come amministratore**.
4. Clicca su _Salva_{:.doc-button}.

### Sbloccare gli utenti

Gli account utente vengono bloccati dopo tre tentativi di accesso con password sbagliate. Per sbloccare gli utenti bloccati, segui questi passaggi:

1. Vai su _Account > Utenti_{:.breadcrumbs}.<br>
L’elenco degli utenti presenta un’icona con un lucchetto giallo{% icon lock | icon-only %} accanto al nome dell’utente bloccato.
2. Clicca sul nome utente dell’utente bloccato.
3. Nella sezione **Sicurezza** a destra, clicca su _Sblocca utente_{:.doc-button}.

Dopo aver sbloccato un utente, ti consigliamo di impostare una nuova password per l’utente.

### Impostare una nuova password per l’utente

Se un utente ha dimenticato la sua password, può resettarla cliccando sul link **Password dimenticata?** nella pagina di accesso. In alternativa, puoi impostarla per l’utente, per esempio se il suo account è stato bloccato.
Per impostare una nuova password per un utente, segui questi passaggi:

> Nota
>
> Gli utenti non vengono informati automaticamente delle modifiche alla loro password. Dovrai informarli dell’impostazione della nuova password.

1. Vai su _Account > Utenti_{:.breadcrumbs}.
2. Clicca sul nome utente di un utente esistente.
3. nella sezione **Sicurezza** a destra, clicca su _Imposta nuova password_{:.doc-button};
4. digita la nuova password dell’utente;
5. clicca su _Salva_{:.doc-button}.



## Disattivare un account utente

Per scoprire le conseguenze della disattivazione di un account utente, leggi {% link_new quest’articolo | features/administration/deactivate-employees.md %}.

1. Vai su _Account > Utenti_{:.breadcrumbs}.
2. Clicca sul nome utente di un utente esistente.
3. Clicca su _Elimina_{:.doc-button} in basso a destra.  
   Si aprirà una finestra.
4. Per disattivare l’utente, clicca _Appartenenza all’organico_{:.doc-button} e imposta una data di fine impiego. Tutti i dati relativi alla pianificazione verranno mantenuti. In futuro, l’utente potrà essere riattivato.

Scopri come {% link_new riattivare un account utente | features/administration/deactivate-employees.md | #riattivare-un-dipendente %}.

## Eliminare un account utente

> Attenzione
>
> Non è possibile riattivare un account utente che è stato eliminato. L’account utente verrà eliminato da tutte le pianificazioni presenti e future per le quali era stato pianificato.

Per eliminare definitivamente un account utente, segui questi passaggi:

1. Vai su _Account > Utenti_{:.breadcrumbs}.
2. Clicca sul nome utente di un utente esistente.
3. Clicca su _Elimina_{:.doc-button} in basso a destra.  
   Si aprirà una finestra.
4. Spunta la casella **Comprendo che il record dell'utente e tutti i dati di pianificazione di &lt;nome utente&gt; verranno eliminati.**
5. Clicca su _Elimina_{:.doc-button}. 

## Esportare l’elenco degli utenti in un file CSV

È possibile esportare l’elenco completo, oppure un elenco degli utenti filtrato, in un file CSV. Questo file CSV può essere importato, per esempio, in database e software esterni, come i database Data Warehouse, SAP e i sistemi di gestione delle risorse umane.

1. Vai su _Account > Utenti_{:.breadcrumbs}.
2. (Facoltativo) Utilizza il campo di ricerca oppure il filtro ruoli per restringere l’elenco di utenti visualizzati.
3. Clicca su _Esporta in CSV_{:.doc-button} in alto a destra.  
   Il file CSV viene scaricato sul tuo computer.

Il file in formato CSV contiene il cognome, il nome e l’indirizzo email degli utenti. I valori sono separati da virgole. La funzione di esportazione utilizza un formato prestabilito che non può essere modificato.
