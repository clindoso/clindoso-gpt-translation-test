---
title: IP-filter
product_label:
  - enterprise
  - advanced
description: Lees hoe je het IP-filter instelt voor je injixo-tenant.
toc: true
---

Het IP-filter is een betaalde functie. Deze wordt niet automatisch opgenomen in je Enterprise- of Advanced WFM-plan.
Als je organisatie geïnteresseerd is in deze feature, neem dan contact op met je consultant.

Met het IP-filter zorg je ervoor dat je gebruikers alleen vanaf bepaalde IP-adresbereiken toegang hebben tot je injixo-tenant. Gebruikers met andere IP-adressen hebben geen toegang tot injixo. injixo beschikt over een [netwerktoegangsbeheerlijst](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) (netwerk-ACL). Activeer de netwerk-ACL als je wilt dat gebruikers alleen vanaf geselecteerde netwerken (bijvoorbeeld dat van je organisatie) toegang hebben tot injixo.

## Het IP-filter inschakelen

Alleen gebruikers met admintoegang kunnen het IP-filter inschakelen.

> Opmerking
> 
> Als je het IP-filter inschakelt, worden alle actieve gebruikers afgemeld. De tijdsperiode varieert afhankelijk van de plaats in het product:
> - Gebruikers worden direct afgemeld
> - Gebruikers worden afgemeld zodra gegevens opnieuw worden geladen of opgeslagen
> - Afmelding is getimed (alleen toegankelijk in het Dienstrooster-Center via _Plan > Dienstrooster-Center_{:.breadcrumbs})
> 
> Om verder te werken met injixo, moeten alle gebruikers zich opnieuw aanmelden.

1. Ga naar _Account > Beveiliging_{:.breadcrumbs} en scrol naar de sectie **IP-filter**.
2. Voer in de velden voor het **IP-adresbereik** de IP-adresbereiken in [CIDR-formaat](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#:~:text=CIDR%20notation%20specifies%20an%20IP,bits) in. Je kunt maximaal drie IP-adresbereiken invoeren.
3. Klik op _Filter inschakelen_{:.doc-button}.

Het IP-filter heeft alleen invloed op UI-interacties. Het optioneel beschikbare Dienstrooster-Center via de directe URL wordt momenteel niet door het IP-filter beïnvloed.
 
## De IP-adresbereiken bewerken

> Opmerking
> 
> Als je de IP-adresbereiken bewerkt, worden alle gebruikers uitgelogd zodra ze injixo de volgende keer openen. Om verder te werken met injixo, moeten alle gebruikers zich opnieuw aanmelden.

1. Ga naar _Account > Beveiliging_{:.breadcrumbs} en scrol naar de sectie **IP-filter**.
2. Bewerk de IP-adresbereiken.
3. Klik op _Opslaan_{:.doc-button}.

## Het IP-filter uitschakelen

1. Ga naar _Account > Beveiliging_{:.breadcrumbs} en scrol naar de sectie **IP-filter**.
2. Bewerk de IP-adresbereiken.
3. Klik op _Filter uitschakelen_{:.doc-button}.

Nadat je het IP-filter hebt uitgeschakeld, kunnen gebruikers injixo vanaf elk IP-adres bereiken.

> Opmerking
> 
> Als je het IP-filter uitschakelt, worden alle gebruikers afgemeld. Om verder te werken met injixo, moeten alle gebruikers zich opnieuw aanmelden.
