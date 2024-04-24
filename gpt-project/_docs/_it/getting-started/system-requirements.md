---
title: Requisiti di sistema
description: Requisiti della versione browser e desktop per le integrazioni, gli agenti, e le postazioni di lavoro dei pianificatori.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/browser-setup.md
---

injixo è un software SaaS di workforce management (WFM) su browser, disponibile in diversi [piani WFM](https://www.injixo.com/it/pricing): injixo Essential WFM, injixo Advanced WFM e injixo Enterprise WFM.

## Requisiti del browser

injixo è compatibile con le ultime due versioni dei seguenti browser:

- Microsoft Edge
- Google Chrome
- Mozilla Firefox
- Apple Safari

## Blocco pop-up

injixo utilizza i pop-up per mostrare finestre di dialogo aggiuntive. Per consentire i pop-up per injixo, segui questi passaggi:

- Disattiva il blocco dei pop-up in [Microsoft Edge](https://support.microsoft.com/it-it/microsoft-edge/blocca-i-popup-in-microsoft-edge-1d8ba4f8-f385-9a0b-e944-aa47339b6bb5).
- Imposta un'eccezione per il blocco dei pop-up in [Google Chrome](https://support.google.com/chrome/answer/95472?hl=it&co=GENIE.Platform%3DDesktop&sjid=6714871772694331970-EU#zippy=%2Callow-pop-ups-and-redirects-from-a-site), [Mozilla Firefox](https://support.mozilla.org/it/kb/Controllare%20le%20finestre%20pop-up), e [Apple Safari](https://support.apple.com/it-it/guide/safari/sfri40696/mac).

## Microsoft Edge in modalità Internet Explorer (IE)

Le funzionalità basate su ActiveX in WFM richiedono {% link_new Microsoft Edge in modalità IE | support/faq/configure-edge-internet-explorer-mode.md %}. Per configurare la modalità IE, è necessario un [file XML di elenco di siti](https://learn.microsoft.com/it-it/deployedge/edge-ie-mode-local-site-list).

<style>
table {
  width: 100%;
}
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

| Piano WFM                               | È necessario Microsoft Edge in modalità IE       |
| -------------------------------------- | ------------------------------------------ |
| Essential WFM                          | No                                         |
| Advanced WFM                           | No                                         |
| Enterprise WFM                         | Soltanto quando si utilizzano componenti personalizzati.            |
| Classic <sup>1</sup>                   | Sì                                        |
| Enterprise WFM on-premise <sup>1</sup> | Sì. Se non è configurata, non sarà possibile fare il login. |

<sup>1</sup>Versione obsoleta del software (piani WFM che vengono ancora utilizzati da alcuni clienti).

Se utilizzi un browser non supportato o se non hai configurato correttamente la modalità IE, il logo IE nella navigazione del modulo WFM indicherà i componenti che richiedono la modalità IE (Classic/Enterprise WFM).

{% link_new injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} funziona con tutti i browser elencati, su computer, smartphone e tablet.

## Client injixo

I componenti basati su ActiveX richiedono il {% link_new client injixo | getting-started/browser-setup.md %}.

Trovi i requisiti per il sistema operativo nella descrizione del client nella pagina [downloads.injixo.com](https://downloads.injixo.com).

| Piano WFM                      | È necessario il client injixo               |
| ------------------------- | ----------------------------------------- |
| Essential WFM             | No                                        |
| Advanced WFM              | No                                        |
| Enterprise WFM            | Soltanto quando si utilizzano componenti personalizzati.           |
| Classic                   | Sì                                       |
| Enterprise WFM on-premise | Sì. Se il client injixo non è installato, non sarà possibile fare il login. |

Se il client injixo non è installato, il logo IE nel menu di navigazione a sinistra identifica i componenti che richiedono la modalità IE (Classic/Enterprise WFM).

{% link_new injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} non richiede il client injixo.

## Eccezioni del firewall

Per poter accedere alle pagine web injixo, consenti il traffico web in uscita e in entrata da *.injixo.com tramite la porta 443.

Se utilizzi componenti ActiveX o applicazioni SDK personalizzate, aggiungi un’altra eccezione del firewall. Queste applicazioni utilizzano la porta 45054 per il traffico in uscita (porta 80 per gli host injixo precedenti al 2019) e richiedono l’accesso diretto a internet tramite TCP (Transmission Control Protocol). I server proxy configurati nel browser non sono supportati.

Per ottenere l'indirizzo per l'eccezione del firewall, clicca su _WFM_{:.menu-item} e usa il nome dell’host injixo visibile nella barra degli indirizzi del browser, ad esempio wfm-123abc.injixo.com.

Per saperne di più sulle eccezioni del firewall in Windows, consulta la [documentazione di Microsoft.

### URL di condivisione per WebSocket

Per inviare agli utenti aggiornamenti in tempo reale, come, per esempio, nel {% link_new Centro dei turni | features/scheduling/shiftcenter/shift-center-overview.md %} o in Aderenza in Tempo Reale, injixo si serve del protocollo WebSocket (basato su TCP) sulla porta 443\. injixo apre una pagina web che stabilisce una connessione WebSocket. Aggiungi le seguenti URL all’elenco delle URL consentite:

- https://shiftcenter.injixo.com
- wss://shiftcenter.injixo.com
- https://www.injixo.com
- wss://ws.injixo.com

In injixo Advanced e injixo Enterprise WFM, il Centro dei turni richiede i WebSocket per poter funzionare alla massima velocità. La tecnologia su cui è fondato prevede un meccanismo di fallback più lento se i WebSocket non sono disponibili. Altri componenti injixo non prevedono un meccanismo di fallback.

## Larghezza di banda necessaria

injixo è stato progettato e ottimizzato per ottenere prestazioni elevate mantenendo basso il consumo di risorse. Al primo accesso, le componenti grafiche vengono scaricate e archiviate localmente in file temporanei. In seguito, soltanto le informazioni di base vengono trasferite, in modo sicuro, alle postazioni locali.

Per un contact center con 200 postazioni puoi aspettarti un trasferimento dati orario di circa 25-50 MB quando tutti gli utenti sono connessi.

## Requisiti per le integrazioni

Imposta le {% link_new integrazioni | features/acd-integration/cloud/how-integrations-work.md %} per consentire a injixo di importare e processare dati sui contatti e sugli stati degli agenti dai sistemi esterni, come i sistemi di distribuzione automatica delle chiamate (ACD) e i sistemi di gestione dei rapporti con la clientela (CRM).
injixo supporta una vasta gamma di integrazioni su cloud e on-premise.

Installa {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} per importare regolarmente dati dalle integrazioni on-premise e CSV.

Le richieste di dati non interferiscono con le funzioni principali del software di comunicazione, come le piattaforme telefoniche o di posta elettronica.

Le richieste di informazioni sugli stati degli agenti in tempo reale potrebbero utilizzare feed di socket diretto. Questi feed trasmettono soltanto i cambiamenti di attività degli agenti (compresi timestamp, ID agente e codice di stato) e sono circa 1kB ciascuno.

## Centri elaborazione dati e misure di sicurezza

injixo opera da centri elaborazione dati che fanno parte dell’infrastruttura Amazon EC2. Per questo motivo, a injixo si applicano le [politiche di sicurezza Amazon](https://aws.amazon.com/it/security/?nc1=h_ls), per esempio SOC 1 di tipo 2, ISO 27001 e PCI DSS di livello 1.

Tutti i dati vengono archiviati nell’Unione Europea (per i clienti europei) e negli Stati Uniti (per i clienti con sede negli USA). injixo rispetta le normative vigenti sulla protezione dei dati, incluso il Regolamento generale sulla protezione dei dati (GDPR) in Europa. Scopri di più su [sicurezza e conformità del cloud di injixo](https://www.injixo.com/it/security/).
