---
title: Configurazione del browser
description: Impara a configurare il browser per utilizzare injixo.
product_label:
  - on-premise
  - classic
related_articles:
  - overwrite_title: Risolvere gli errori durante l’installazione del client
    filepath: support/faq/client-installer-errors.md
  - overwrite_title: Sessione scaduta durante l’accesso a WFM
    filepath: support/faq/session-timeout-message.md
redirect_from:
  - /it/setup-guide/
redirect_reason: Updated filename on 27 July 2023
---

Leggendo questo articolo imparerai a configurare il browser per injixo.

Per lavorare con i componenti basati su ActiveX in WFM, utilizza {% link_new Microsoft Edge in modalità Internet Explorer (IE) | support/faq/configure-edge-internet-explorer-mode.md %}. Trovi l’elenco dei browser compatibili nell’articolo sui {% link_new requisiti di sistema | getting-started/system-requirements.md | #requisiti-del-browser %}.

Se non hai le autorizzazioni necessarie per modificare le impostazioni del browser o installare un nuovo software, contatta il reparto informatico della tua azienda.

## Configurare i siti affidabili e le impostazioni di sicurezza

injixo Classic e injixo Enterprise WFM includono dei controlli ActiveX. Dovrai consentire al browser (Edge in modalità IE) di eseguire questi controlli ActiveX.

Nelle impostazioni del browser, aggiungi all’elenco dei siti affidabili tutte le pagine injixo (_*.injixo.com_):

1. Apri il menu avvio di Windows, digita Opzioni Internet, e premi Invio.
2. Nella scheda **Protezione**, seleziona l’area **Siti attendibili**, e clicca su _Siti_{:.doc-button}.
3. Nel campo **Aggiungi il sito Web all’area**, inserisci https://\*.injixo.com.
4. Spunta la casella **Richiedi verifica server (https:) per tutti i siti in questa area**.
5. Clicca su **Aggiungi**.
6. Clicca su **Chiudi**.

{{ 1 | image: 'impostazioni-di-protezione', '40%', 'jpg' }}

Regola il livello di sicurezza per i siti affidabili:

1. Clicca sul menu avvio di Windows, digita Opzioni Internet, e premi Invio.
2. Nella scheda **Protezione**, seleziona l’area **Siti attendibili**.
3. Deseleziona la casella **Abilita modalità protetta**.  
   Nota: questa casella non è più disponibile a partire da Windows 11.
4. Nella scheda **Protezione**, imposta la protezione per **Siti attendibili** su **Media** o **Medio-bassa**. Medio-bassa ti consente di saltare i passaggi dal 6 al 9.
5. Clicca su _OK_{:.doc-button}.
6. Clicca su _Livello personalizzato..._{:.doc-button}.
7. Nella finestra **Impostazioni di sicurezza**, modifica le seguenti impostazioni:

   | Impostazione                                           | Stato             |
   | ------------------------------------------------- | ----------------- |
   | Esegui script controlli ActiveX contrassegnati come sicuri | ABILITATO           |
   | Esegui controlli ActiveX e Plug-in                  | ABILITATO           |
   | Scarica controlli ActiveX firmati                  | CHIEDI CONFERMA o ABILITATO |
   | Richiesta di conferma automatica per controlli ActiveX          | ABILITATO           |

8. Clicca su _OK_{:.doc-button}.
   Verrà visualizzato il seguente messaggio: Modificare le impostazioni per questa area?
9. Clicca su _Sì_{:.doc-button}.
10. Per chiudere la finestra, clicca _OK_{:.doc-button}.

## Installazione del client injixo

injixo Classic e injixo Enterprise WFM comprendono controlli ActiveX, che richiedono {% link_new Microsoft Edge in modalità IE | support/faq/configure-edge-internet-explorer-mode.md %} e il client injixo.

Se visualizzi un messaggio di errore durante o dopo l'accesso a injixo:

- utilizza uno dei {% link_new browser compatibili | getting-started/system-requirements.md | #requisiti-del-browser %}.
- installa il client injixo (come descritto di seguito).

### Installazione automatica del client (pagina iniziale di WFM)

Se utilizzi le impostazioni del browser descritte in precedenza, il client viene installato automaticamente quando si accede a WFM.

1. Vai su _WFM_{:.menu-item}.
2. Aspetta che il download sia terminato e che l’installazione del client cominci.
3. Il browser mostra il messaggio _Questa pagina web vuole eseguire il seguente add-on 'injixo Enterprise' di 'InVision AG'_. Se il messaggio non viene visualizzato, contatta il reparto informatico della tua azienda.
4. Clicca su _Installa_{:.doc-button} per installare gli add-on necessari.
5. Clicca su _Installa_{:.doc-button} per installare il client.

Se l’installazione si è conclusa senza errori, potrai accedere ai componenti ActiveX.

### Installazione manuale del client

Installa il client manualmente se utilizzi injixo WFM Enterprise on-premise o se l’installazione automatica non funziona.

Nota: se utilizzi un sistema di distribuzione del software, lancia il programma di installazione per l’utente che effettuerà l’accesso al computer in seguito, utilizzando, per esempio, _msiexec.exe_ di Microsoft con l’opzione _runas /user_.

1. Scarica la [versione più recente del client injixo](https://downloads.injixo.com/en#client-components).
2. Per lanciare il programma di installazione MSI, clicca su _Esegui_{:.doc-button}.
3. Per continuare, clicca su _Avanti_{:.doc-button}.
4. (Facoltativo) Modifica il percorso di installazione.
5. Se al computer hanno accesso diversi utenti, seleziona **Tutti**.
6. Per continuare, clicca su _Avanti_{:.doc-button}.
7. Per lanciare l’installazione, clicca su _Installa_{:.doc-button}.
   Verrà visualizzato il seguente messaggio: Consentire al programma seguente con autore sconosciuto di apportare modifiche al computer?
8. Clicca su _Sì_{:.doc-button} per confermare.

Se l’installazione si è conclusa senza errori, potrai accedere ai componenti ActiveX.
