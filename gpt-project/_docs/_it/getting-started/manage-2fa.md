---
title: Gestire l’autenticazione a due fattori (2FA)
product_label:
  - essential
  - advanced
  - enterprise
description: Scopri come attivare e disattivare la 2FA per gli account dei tuoi dipendenti.
redirect_from:
  - /it/2fa/
redirect_reason: Updated filename on 14 July 2023
---

> Solo gli utenti con accesso amministratore possono gestire l'autenticazione a due fattori (2FA) per gli altri utenti.

## Visualizzare le impostazioni della 2FA di altri utenti

Per visualizzare lo stato attuale della 2FA degli altri utenti, procedi come di seguito:
1. Vai su _Account > Utenti_{:.breadcrumbs}.
2. Nella colonna **2FA** a destra, un'icona a forma di scudo indica lo stato della 2FA per ogni utente. Passa il mouse sopra l’icona per ottenere altre informazioni.
  - Icona rossa {% icon 2FA-red | icon-only %}: la 2FA non è attiva.
  - Icona arancione con il punto esclamativo {% icon 2FA-orange | icon-only %}: la 2FA è stata imposta a quest’utente. L'utente dovrà attivare la 2FA la prossima volta che farà il login.
  - Icona verde con il segno di spunta {% icon 2FA-green | icon-only %}: la 2FA è attiva.

## Imporre la 2FA ad altri utenti
Puoi imporre l’attivazione della 2FA ad altri utenti. Imporre la 2FA agli altri utenti ha le seguenti conseguenze:

- Gli utenti non potranno fare il login se non attivano la 2FA.
- Gli utenti non potranno più disattivare la 2FA per il loro account personale.

Prima di imporre la 2FA ad altri utenti, assicurati che abbiano accesso a una delle {% link_new app di autenticazione supportate | getting-started/use-two-factor-authentication.md | #prerequisito-installare-unapp-di-autenticazione %}.

### Imporre l’attivazione della 2FA a singoli utenti

1. Vai su _Account > Utenti_{:.breadcrumbs}.
2. Clicca sul nome dell’utente al quale vuoi imporre l’attivazione della 2FA.  
   Si aprirà la pagina con i dettagli dell’utente.
3. Nella sezione **Sicurezza**, spunta la casella **Imponi l’attivazione della 2FA**.
4. Clicca su _Salva_{:.doc-button} per confermare l’attivazione.

### Imporre l’attivazione della 2FA a tutti gli utenti

1. Vai su _Account > Sicurezza_{:.breadcrumbs}. In questa pagina vedrai la distribuzione attuale della 2FA tra gli utenti.
2. Clicca su _Imponi la 2FA a tutti gli utenti_{:.doc-button}.  
   Vedrai un messaggio verde di conferma. Il testo del pulsante diventerà _Revoca l'obbligatorietà della 2FA_{:.doc-button}.

### Disattivare l'autenticazione a due fattori per singoli utenti

In alcuni casi, potresti voler disattivare temporaneamente la 2FA solo per alcuni utenti, o escluderli totalmente dall’obbligo della 2FA.

1. Vai su _Account > Utenti_{:.breadcrumbs}.
2. Clicca sul nome dell'utente per il quale desideri disattivare la 2FA.  
   Si aprirà la pagina con i dettagli dell’utente.
3. Nella sezione **Sicurezza**, deseleziona la casella **Imponi l'attivazione della 2FA**.
4. Clicca su _Salva_{:.doc-button} per confermare la disattivazione.
