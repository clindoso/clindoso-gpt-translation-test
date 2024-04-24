---
title: Utilizzare l'autenticazione a due fattori (2FA)
product_label:
  - essential
  - advanced
  - enterprise
description: Scopri come attivare e disattivare l’autenticazione a due fattori per il tuo account.
---

## Che cos'è l'autenticazione a due fattori?

L'autenticazione a due fattori (2FA) aggiunge un ulteriore livello di sicurezza ai tuoi account online.  
Per accedere al tuo account quando è attiva la 2FA, ti serviranno:
- le tue credenziali di accesso;
- una password aggiuntiva, generata da un altro dispositivo.

> Attiva quanto prima la 2FA per il tuo account injixo per aumentare la sicurezza.

## Prerequisito: installare un'app di autenticazione

injixo è compatibile con le app di autenticazione elencate nella tabella qui sotto.  
Se utilizzi un dispositivo Android, scarica una delle app dal Google Play Store. Se utilizzi un iPhone, scaricala dall'Apple App Store.

|-------|--------|---------|
| Google Authenticator | [App Store di Apple](https://apps.apple.com/it/app/google-authenticator/id388497605) | [Google Play Store](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=it) |
| Microsoft Authenticator | [App Store di Apple](https://apps.apple.com/it/app/microsoft-authenticator/id983156458) | [Google Play Store](https://play.google.com/store/apps/details?id=com.azure.authenticator&hl=it) |
| Authy | [App Store di Apple](https://apps.apple.com/it/app/authy/id494168017) | [Google Play Store](https://play.google.com/store/apps/details?id=com.authy.authy&hl=it) |

## Attivare la 2FA per il tuo account

Per attivare la 2FA per il tuo account, devi avere accesso a un dispositivo principale (per esempio un computer) e al tuo dispositivo personale.  
Sul computer o dispositivo principale, procedi come di seguito:

1. Accedi a injixo e clicca sul tuo nome utente in alto a destra nella barra di navigazione.
2. Clicca sulla scheda **Sicurezza**.
3. Clicca su _Attiva la 2FA_{:.doc-button}.
4. Inserisci la tua password.
5. Clicca su _Continua_{:.doc-button}.  
   Si apre la pagina **Attiva l’autenticazione a due fattori (2FA)**. La pagina elenca i passaggi da seguire.

Sul tuo dispositivo personale, segui i passaggi elencati nella pagina Attiva l’autenticazione a due fattori (2FA)

1. Installa una delle [app di autenticazione compatibili](#prerequisito-installare-unapp-di-autenticazione).
2. Apri l’app di autenticazione sul tuo dispositivo e crea una nuova voce per injixo.  
   Per fare ciò, scegli una delle seguenti opzioni:
   - Scansiona il codice QR sulla pagina **Attiva l'autenticazione a due fattori (2FA)** con l'app di autenticazione.
   - Inserisci la chiave visualizzata nella pagina **Attiva l'autenticazione a due fattori (2FA)** nell’app di autenticazione.  
L'app di autenticazione è stata configurata e inizia a generare password monouso (OTP).

Sul computer o dispositivo principale, procedi come di seguito:

1. Nella pagina **Attiva l’autenticazione a due fattori (2FA)**, inserisci una password monouso nel campo **Password monouso**.
2. Clicca su _Continua_{:.doc-button}.
3. Conserva i codici di backup o scaricali come file. Clicca _Download_{:.doc-button} o _Copia_{:.doc-button}. Se non vedi i codici di backup, significa che sono stati disattivati per il tuo account. <!-- feature flag -->

   > Conserva i codici di backup in un luogo sicuro.
   >
   > Se perdi l'accesso al tuo dispositivo personale, potrai fare il login solo utilizzando un codice di backup.<br>Conserva i tuoi codici di backup in modo sicuro, ad esempio in un gestore di password, oppure stampali e assicurati che solo tu possa accedervi.

4. Seleziona la casella **Ho conservato in modo sicuro i miei codici di backup.**
5. Clicca su _Attiva la 2FA_{:.doc-button}.  
   Riceverai un'email che conferma l’attivazione della 2FA.  
D’ora in poi, per accedere a injixo avrai bisogno sia delle tue credenziali di accesso che di un'OTP.

## Fare il login quando la 2FA è attiva

1. Inserisci il tuo indirizzo email e la password nella pagina di login di injixo e clicca su _Login_{:.doc-button}.  
2. Inserisci l'OTP generata dalla tua app di autenticazione.  
   Ogni OTP è valida solo per 30 secondi, dopodiché l'app ne genera una nuova.
3. Clicca su _Verifica_{:.doc-button} per completare il login.

Se non riesci a fare il login, controlla sull'app di autenticazione che l'OTP che hai inserito sia ancora valida. Se così non fosse, ti basterà inserire una nuova OTP.
Se continui ad avere difficoltà, segui le istruzioni riportate di seguito per accedere con un codice di backup.

### Fare il login con un codice di backup

Durante la configurazione della 2FA per il tuo account, ricevi 10 codici di backup. Se non hai accesso al tuo dispositivo personale, puoi accedere a injixo utilizzando uno dei codici di backup.

> Nota
>
> Fai il login con un codice di backup solo in caso di emergenza. Ogni codice di backup può essere utilizzato una volta sola. Dovresti sempre fare il login usando un'OTP.

Per accedere con un codice di backup anziché con un'OTP, procedi come di seguito:

1. Inserisci il tuo indirizzo email e la password nella pagina di login di injixo e clicca su _Login_{:.doc-button}.
2. Clicca sul link al codice di backup sotto il campo **Password monouso**.
3. Inserisci uno dei codici di backup di 10 caratteri nel campo **Codice di backup**.
4. Clicca su _Verifica_{:.doc-button} per completare il login.

<!-- a tag required. configured name used in injixo UI link -->

### Fare il login senza il dispositivo personale né i codici di backup

Se non riesci ad accedere con la 2FA e non hai i codici di backup a portata di mano, contatta un utente con accesso amministratore, che potrà disattivare la 2FA per il tuo account. Potrai quindi fare il login senza un'OTP, e ripristinare le impostazioni della 2FA.

## Utilizzare la 2FA su un nuovo dispositivo personale

Se vuoi usare un altro dispositivo per generare le OTP, devi disattivare temporaneamente la 2FA per il tuo account e [attivarla di nuovo usando il nuovo dispositivo](#attivare-la-2fa-per-il-tuo-account).

Se non riesci a disattivare la 2FA per il tuo account, chiedi a un utente con accesso amministratore di farlo per te.

## Disattivare la 2FA per il tuo account

> Nota
>
> La disattivazione della 2FA è sconsigliata. Se l’attivazione della 2FA è stata imposta per il tuo account, non puoi disattivarla.

1. Accedi a injixo e clicca sul tuo nome utente in alto a destra nella barra di navigazione.
2. Clicca sulla scheda **Sicurezza**.  
   In alto nella pagina vedrai lo stato attuale delle impostazioni della 2FA.
3. Clicca su _Disattiva 2FA_{:.doc-button}.
4. Inserisci la tua password.
5. Clicca su _Continua_{:.doc-button} per confermare la disattivazione.

Riceverai un'email che conferma la disattivazione della 2FA. D'ora in poi, potrai nuovamente fare il login senza utilizzare un'OTP.

> Hai ricevuto l'email che conferma la disattivazione della 2FA, ma non avevi richiesto la disattivazione?
>
> Controlla il tuo account insieme a un utente con accesso amministratore della tua azienda. Valuta la possibilità di cambiare password.
