---
title: Systeemvereisten
description: Browser- en desktopvereisten voor integraties, agenten en planner-workstations.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/browser-setup.md
---

injixo is een browser-gebaseerde Workforce Management SaaS-software en is beschikbaar in meerdere [WFM-plannen](https://www.injixo.com/nl/pricing): injixo Essential WFM, injixo Advanced WFM en injixo Enterprise WFM.

## Browservereisten

injixo ondersteunt de twee nieuwste versies van de volgende browsers:

- Microsoft Edge
- Google Chrome
- Mozilla Firefox
- Apple Safari

## Pop-upblokkering

injixo gebruikt pop-ups om aanvullende dialoogvensters weer te geven. Volg de volgende stappen om pop-ups toe te staan voor injixo:

- Schakel je pop-upblokkering in [Microsoft Edge](https://support.microsoft.com/nl-nl/microsoft-edge/pop-ups-blokkeren-in-microsoft-edge-1d8ba4f8-f385-9a0b-e944-aa47339b6bb5) uit.
- Stel in [Google Chrome](https://support.google.com/chrome/answer/95472?hl=nl&co=GENIE.Platform%3DDesktop#zippy=%2Callow-pop-ups-and-redirects-from-a-site), [Mozilla Firefox](https://support.mozilla.org/nl/kb/instellingen-pop-upblokkering-uitzonderingen-probleemoplossing) en [Apple Safari](https://support.apple.com/nl-nl/guide/safari/sfri40696/mac) een uitzondering in voor de pop-upblokkering.

## Microsoft Edge in Internet Explorer (IE)-modus

Voor ActiveX-gebaseerde features in WFM is {% link_new Microsoft Edge in IE-modus | support/faq/configure-edge-internet-explorer-mode.md %} vereist. Om de IE-modus te configureren, heb je een [sitelist-XML-bestand](https://learn.microsoft.com/en-us/deployedge/edge-ie-mode-local-site-list) nodig.

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

| WFM-plan                               | Microsoft Edge in IE-modus vereist         |
| -------------------------------------- | ------------------------------------------ |
| Essential WFM                          | Nee                                         |
| Advanced WFM                           | Nee                                         |
| Enterprise WFM                         | Alleen als er aangepaste features worden gebruikt            |
| Classic <sup>1</sup>                   | Ja                                        |
| Enterprise WFM on-premise <sup>1</sup> | Ja. Indien niet geconfigureerd, kun je je niet aanmelden. |

<sup>1</sup> Legacysoftware (oude WFM-plannen die momenteel nog in gebruik zijn)

Als je de verkeerde browser of een verkeerde configuratie van de IE-modus gebruikt, dan geeft het IE-logo in de WFM-navigatie aan voor welke features de IE-modus vereist is (Classic/Enterprise WFM).

{% link_new injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} werkt met alle vermelde browsers, op computers, smartphones en tablets.

## injixo-clientsoftware

Voor ActiveX-gebaseerde features in WFM is de {% link_new injixo client | getting-started/browser-setup.md %} vereist.

Je vindt de vereisten voor het besturingssysteem in de downloadbeschrijving onder [downloads.injixo.com](https://downloads.injixo.com).

| WFM-plan                      | injixo-client vereist?                |
| ------------------------- | ----------------------------------------- |
| Essential WFM             | Nee                                        |
| Advanced WFM              | Nee                                        |
| Enterprise WFM            | Alleen als er aangepaste features worden gebruikt           |
| Classic                   | Ja                                       |
| Enterprise WFM on-premise | Ja. Indien deze niet is geïnstalleerd, kun je je niet aanmelden. |

Als de injixo client niet is geïnstalleerd, dan geeft het IE-logo links in de navigatie aan voor welke features de IE-modus vereist is (Classic/Enterprise WFM).

Voor {% link_new injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} is de injixo-client niet vereist.

## Firewall-uitzonderingen

Om toegang te krijgen tot de webpagina's van injixo, moet internetverkeer van en naar *.injixo.com via poort 443 zijn toegestaan.

Voeg nog een firewall-uitzondering toe als je ActiveX-gebaseerde features of aangepaste SDK-toepassingen gebruikt. Deze toepassingen gebruiken poort 45054 voor uitgaand verkeer (poort 80 voor injixo-hosts tot 2019) en vereisen directe internettoegang via het Transmission Control Protocol (TCP). Proxyservers die in de browser zijn geconfigureerd worden niet ondersteund.

Klik op _WFM_{:.menu-item} om het adres voor de firewall-uitzondering te vinden en gebruik de naam van je injixo-host die zichtbaar is in de adresbalk van de browser, bijvoorbeeld wfm-123abc.injixo.com.

Raadpleeg de [Microsoft-documentatie](https://support.microsoft.com/en-us/windows/add-an-exclusion-to-windows-security-811816c0-4dfd-af4a-47e4-c301afe13b26#:~:text=Go%20to%20Start%20%3E%20Settings%20%3E%20Update,%2C%20file%20types%2C%20or%20process) voor meer informatie over firewall-uitzonderingen.

### URL's delen voor WebSockets

Om realtime updates naar gebruikers te sturen, bijvoorbeeld in het {% link_new Dienstrooster-Center | features/scheduling/shiftcenter/shift-center-overview.md %} of Real-Time Adherence, gebruikt injixo het WebSocket-protocol (op basis van TCP) via poort 443\. injixo opent een webpagina die een WebSocket-verbinding tot stand brengt. Voeg daarvoor de volgende URL's toe aan de acceptatielijst:

- https://shiftcenter.injixo.com
- wss://shiftcenter.injixo.com
- https://www.injixo.com
- wss://ws.injixo.com

In injixo Advanced en injixo Enterprise WFM heeft het Dienstrooster-Center WebSockets nodig om op maximale snelheid te werken. De onderliggende technologie zorgt voor een langzamer terugmechanisme als WebSockets niet beschikbaar zijn. Andere features hebben geen terugvalmechanisme.

## Vereiste netwerkbandbreedte

injixo is ontworpen en geoptimaliseerd voor een sterke performance en een laag verbruik van resources. Bij de eerste aanmelding worden afbeeldingen lokaal opgeslagen in tijdelijke bestanden. Daarna wordt uitsluitend basisinformatie veilig naar de desktop overgedragen.

Een contactcenter met 200 werkplekken kan rekenen op ongeveer 25-50 MB aan gegevensoverdracht per uur wanneer alle gebruikers zijn ingelogd.

## Integratievereisten

Stel {% link_new integraties | features/acd-integration/cloud/how-integrations-work.md %} in, zodat injixo contact- en agentstatusgegevens van externe systemen kan verwerken, zoals automatic call distributors (ACD) of customer relationship management (CRM)-systemen.
injixo ondersteunt een breed scala aan cloud- en on-premise-integraties.

Installeer {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} om regelmatig gegevens van on-premise- en CSV-integraties te downloaden.

Dataverzoeken hebben geen negatieve invloed op de belangrijkste functies van communicatiesoftware, zoals telefonie- of e-mailplatforms.

Verzoeken om realtime agentstatusgegevens kunnen een directe socket feed gebruiken. Deze feeds geven alleen veranderingen van activiteiten van agenten door (met tijdstempel, een agent-ID en een statuscode). Ze zijn elk ongeveer 1 kB groot.

## Datacenter- en beveiligingsvoorschriften

injixo werkt vanuit datacentra in de Amazon EC2-infrastructuur. Daarom is het [beveiligingsbeleid van Amazon](https://aws.amazon.com/security/) van toepassing op injixo, bijvoorbeeld SOC 1 type 2, ISO 27001 en PCI DSS Level 1.

Alle gegevens worden opgeslagen in de EU (Europese klanten) en in de Verenigde Staten (klanten uit de Verenigde Staten). injixo voldoet dus aan alle relevante wetgeving op het gebied van gegevensbescherming, waaronder de AVG in Europa. Lees meer over [injixo's cloudbeveiliging en compliance](https://www.injixo.com/uk/security/).
