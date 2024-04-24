---
title: Filtro IP
product_label:
  - enterprise
  - advanced
description: Scopri come impostare il filtro IP per il tuo tenant injixo.
toc: true
---

Il filtro IP è una funzionalità a pagamento. Non è incluso automaticamente nel tuo piano Enterprise o Advanced WFM.
Se la tua organizzazione è interessata ad avere questa funzionalità, contatta il tuo consulente.

Il filtro IP fa sì che i tuoi utenti possano accedere al tenant injixo soltanto da specifici intervalli di indirizzi IP. Gli utenti con indirizzi IP diversi non saranno in grado di accedere a injixo. injixo offre una [lista di controllo degli accessi di rete](https://docs.aws.amazon.com/it_it/vpc/latest/userguide/vpc-network-acls.html) (ACL di rete). Attiva l’ACL di rete se desideri consentire l'accesso a injixo solo da reti selezionate (ad esempio, la rete della tua organizzazione).

## Attivare il filtro IP

Soltanto gli utenti con accesso amministratore possono attivare il filtro IP.

> Nota
> 
> Quando attivi il filtro IP, tutti gli utenti attivi vengono disconnessi. A seconda dell'area del programma, il periodo varia:
> - Il logout può essere immediato.
> - Il logout avviene al successivo caricamento o salvataggio di dati.
> - Il logout è programmato (solo nel Centro dei turni, accessibile tramite _Plan > Centro dei turni_{:.breadcrumbs}).
> 
> Per continuare a lavorare con injixo, gli utenti dovranno fare di nuovo il login.

1. Vai su _Account > Sicurezza_{:.breadcrumbs} e scorri fino alla sezione **Filtro IP**.
2. Nei campi denominati **Intervallo di indirizzi IP** inserisci gli intervalli di indirizzi IP nel [formato CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#:~:text=CIDR%20notation%20specifies%20an%20IP,bits). Puoi inserire fino a tre intervalli di indirizzi IP.
3. Clicca su _Attiva filtro_{:.doc-button}.

Il filtro IP influisce solo sulle interazioni dell'interfaccia utente. Per il momento non influisce sul Centro dei turni disponibile in via opzionale tramite URL diretto.
 
## Modificare gli intervalli di indirizzi IP

> Nota
> 
> Se modifichi gli intervalli di indirizzi IP, tutti gli utenti verranno disconnessi al loro successivo utilizzo di injixo. Per continuare a lavorare con injixo, gli utenti dovranno fare di nuovo il login.

1. Vai su _Account > Sicurezza_{:.breadcrumbs} e scorri fino alla sezione **Filtro IP**.
2. Modifica gli intervalli di indirizzi IP.
3. Clicca su _Salva_{:.doc-button}.

## Disattivare il filtro IP

1. Vai su _Account > Sicurezza_{:.breadcrumbs} e scorri fino alla sezione **Filtro IP**.
2. Cancella gli intervalli di indirizzi IP.
3. Clicca su _Disattiva filtro_{:.doc-button}.

Dopo aver disattivato il filtro IP, gli utenti potranno accedere a injixo da qualsiasi indirizzo IP.

> Nota
> 
> Se disattivi il filtro IP, tutti gli utenti vengono disconnessi. Per continuare a lavorare con injixo, gli utenti dovranno fare di nuovo il login.
