---
title: Autenticazione unica (SSO)
product_label:
  - advanced
  - enterprise
description: Scopri come configurare e utilizzare l’SSO in injixo.
---

L’autenticazione unica, single-sign on o SSO, è un sistema di autenticazione che permette agli utenti di accedere a diverse applicazioni e siti web utilizzando un solo set di credenziali. Viene stabilito un rapporto di fiducia tra un servizio centrale di gestione delle identità (provider di identità,<i> </i>o IdP), e un’applicazione (provider di servizi, o SP), che in questo caso è injixo.

L'IdP è un prodotto di terze parti, come per esempio OneLogin, Microsoft Azure AD, Okta o Google. Utilizzando l’SSO, la tua organizzazione può beneficiare di politiche di sicurezza allineate, come l'autenticazione a due fattori e la rotazione delle password. Gli utenti si autenticano presso l'IdP, che reindirizza a injixo.

La configurazione dell'IdP è stata testata con i provider di identità sopra elencati. Se non riesci a integrare il tuo IdP, contattaci.

## Requisiti

I requisiti qui di seguito devono essere soddisfatti per poter integrare injixo nell'IdP:

- supporto al protocollo SAML 2.0;
- accesso via web all’URL di metadati di federazione;
- l’indirizzo email registrato in injixo e il tuo IdP devono essere collegati a una casella di posta.

> Per incrementare la sicurezza, consigliamo caldamente di attivare le asserzioni crittografate/la crittografia token.

## Attivare l’SSO per il tuo account

Soltanto gli utenti con accesso amministratore possono attivare l’SSO.

1. Registra injixo come nuova applicazione SAML o SSO nel tuo IdP.  
   Puoi scaricare [questo logo injixo](/assets/img/common/injixo-logo.png) e aggiungerlo alla pagina delle applicazioni web.

2. In injixo, vai su _Account > Sicurezza_{:.breadcrumbs} e configura l’SSO in **Single Sign-On**.

3. Nella sezione **Metadati SAML injixo** hai due opzioni, che dipendono dalla capacità del tuo IdP di supportare il caricamento di file.

   - Caricamento di file supportato: clicca su _{% icon download | icon-only %} Scarica_{:.doc-button} e completa la configurazione dell’IdP con il file XML scaricato.
   - Caricamento di file non supportato: clicca su **Dettagli del provider di servizi** e aggiungi gli URL mostrati alla configurazione dell’IdP.

4. (Facoltativo) Se utilizzi asserzioni SAML crittografate, clicca su _{% icon download | icon-only %} Scarica_{:.doc-button} nella sezione **Crittografia token**. Aggiungi i certificati scaricati alla configurazione dell’IdP.
5. In base al fatto che il tuo IdP fornisca o meno un URL con i metadati di federazione, completa la configurazione come esposto di seguito:

   - L’IdP fornisce l’URL con i metadati di federazione: copia dal tuo IdP l’URL con i metadati di federazione per l’applicazione registrata. Incolla l’URL nel campo **URL metadati di federazione** nella sezione **Identity Provider**.
   - L’IdP non fornisce l’URL con i metadati di federazione: scarica il file XML con i metadati di federazione. Per esempio, scopri come configurare un’[applicazione SAML personalizzata con Google](https://support.google.com/a/answer/6087519?hl=it&sjid=3388768136264341184-EU).

6. Clicca su _Salvare configurazione_{:.doc-button}.  
   Il sistema SSO è adesso attivo, ma gli utenti possono ancora fare il login con username e password.

> Per garantire un livello di sicurezza più elevato, puoi [imporre l’SSO a tutti gli utenti](#imporre-lsso-a-tutti-gli-utenti).

## Testare la configurazione del sistema SSO

Clicca su _Testa la configurazione_{:.doc-button} per testare il login tramite IdP. L'IdP genera una risposta SAML che viene inviata a injixo. Verrai reindirizzato alla pagina di login del tuo IdP, dove inserirai le credenziali dell'IdP. Se la configurazione dell'IdP è corretta e il procedimento di autenticazione va a buon fine, accederai a injixo.

{{ 4 | image: 'Test della configurazione SSO completato correttamente per l’utente attuale', '80%' }}

<!-- A valid SubjectConfirmation was not found on this Response in our internal server logs -->

La risposta SAML dall'IdP contiene l'asserzione dell'utente autenticato con attributi e informazioni del profilo. Se il procedimento non va a buon fine, e compare un messaggio di errore, controlla la configurazione dell’applicazione, la configurazione dell’utente, e gli attributi Recipient, InResponseTo, NotBefore, and NotOnOrAfter impostati nell’IdP. 

Puoi fare il debug dell'elemento XML SubjectConfirmation nella risposta SAML con gli strumenti per sviluppatori web del tuo browser o con strumenti SAML esterni. Per vedere la risposta non crittografata come testo semplice, disattiva le asserzioni crittografate.

Esempio di elemento XML SubjectConfirmation in una risposta SAML:

```
<saml:Subject>
    <saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">email@company.org</saml:NameID>
    <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
        <saml:SubjectConfirmationData NotOnOrAfter="2022-08-11T08:25:25Z"
            Recipient="https://www.injixo.com/sso/saml/acs"
            InResponseTo="_abcdefgh-0444-4567-abcd-abcdabcdabcd"
    />
    </saml:SubjectConfirmation>
</saml:Subject>
```

## Imporre l’SSO a tutti gli utenti

Per verificare se la configurazione è andata a buon fine, puoi disattivare il login con username e password imponendo l’SSO a tutti gli utenti. Prima di procedere, assicurati che:

- tutti gli utenti injixo siano presenti sia nell’IdP che in injixo;
- l’email injixo corrisponda all’identificatore IdP appropriato;
- tutti gli utenti injixo siano assegnati all’applicazione SSO di injixo nell’IdP.

Dopo che l’SSO è stato imposto a tutti gli utenti, non sarà più possibile:

- accedere con username e password (tutte le password esistenti verranno disattivate);
- resettare le password in injixo (né da parte degli utenti, né da parte degli amministratori);
- gestire l’accesso a injixo al di fuori dell’IdP.

Rendi l’SSO obbligatorio per tutti gli utenti nella sezione **3\. Rafforzamento**. Il tasto _Rafforza_{:.doc-button} diventa selezionabile solo dopo che il test della configurazione è andato a buon fine.

{{ 5 | image: 'Tasto per l’imposizione dell’SSO a tutti gli utenti', '80%' }}

## Cambiare l’indirizzo email dopo l’imposizione dell’SSO

In seguito all’imposizione dell’SSO, gli utenti non possono modificare da soli il loro indirizzo email perché quest’ultimo deve corrispondere all’identificatore dell’IdP.

Soltanto gli utenti con accesso amministratore potranno modificare gli indirizzi email in injixo.

## Fare il login utilizzando l’SSO

Dopo che l’SSO è stato attivato, gli utenti possono accedere da [https://www.injixo.com/login/sso](https://www.injixo.com/login/sso). Dovranno inserire il loro indirizzo email e verranno rediretti alla schermata di login dell’IdP. Se gli utenti hanno già fatto il login, saranno rediretti automaticamente su injixo. Altrimenti, dovranno inserire la password dell’IdP.

## Revocare l’accesso a injixo

Per revocare l’accesso di un utente a injixo tramite SSO, devi eliminare l’assegnazione dell’utente injixo nell’IdP. Attenzione: se l’utente è ancora presente in injixo, verrà incluso nella fatturazione. Per evitare costi inaspettati, è necessario anche {% link_new disattivare o rimuovere l’utente | features/administration/deactivate-employees.md %}.

## Disattivare l’SSO

Per disattivare l’SSO e permettere di nuovo il login con username e password, gli utenti con accesso amministratore devono disattivare l’SSO. Questa azione eliminerà il collegamento con l’IdP e tutti i dettagli di configurazione inseriti. Dopo che l’SSO è stato disattivato, tutti gli utenti attivi riceveranno un’email che li invita a impostare una nuova password per injixo. In seguito, sarà di nuovo possibile fare il login con username e password su [https://www.injixo.com/login](https://www.injixo.com/login).
