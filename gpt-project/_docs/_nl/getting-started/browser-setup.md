---
title: Browserconfiguratie
description: Lees hoe je je browser configureert om met injixo te werken.
product_label:
  - on-premise
  - classic
related_articles:
  - overwrite_title: Fouten tijdens de installatie van de client oplossen
    filepath: support/faq/client-installer-errors.md
  - overwrite_title: Time-out van sessie bij het openen van WFM
    filepath: support/faq/session-timeout-message.md
redirect_from:
  - nl/setup-guide/
redirect_reason: Updated filename on 27 July 2023
---

Gebruik {% link_new Microsoft Edge in Internet Explorer (IE)-modus | support/faq/configure-edge-internet-explorer-mode.md %} om in WFM met features te werken die gebruik maken van ActiveX. Onder {% link_new Systeemvereisten | getting-started/system-requirements.md | #browservereisten %} vind je een lijst met compatibele browsers.

Als je geen rechten hebt om de browserinstellingen te wijzigen of software te installeren, neem dan contact op met je IT-afdeling.

## Instellingen voor vertrouwde sites en beveiligingszone configureren

injixo Classic en injixo Enterprise WFM bevatten ActiveX-besturingselementen. Je moet de browser toestemming geven (Edge in IE-modus) om deze ActiveX-besturingselementen te gebruiken.

Ga naar de browserinstellingen en voeg alle injixo-pagina's (_*.injixo.com_) toe aan de vertrouwde websites:

1. Open het startmenu van Windows, typ internetopties en druk op de Enter-toets.
2. Selecteer in het tabblad **Beveiliging** de optie **Vertrouwde websites** en klik op _Websites_{:.doc-button}.
3. Voer in het veld **Deze website aan de zone toevoegen** https://\*.injixo.com in.
4. Vink het selectievakje **Serververificatie (https:) voor alle websites in deze zone vereist** aan.
5. Klik op **Toevoegen**.
6. Klik op **Sluiten**.

{{ 1 | image: 'beveiligingsinstellingen', '45%', 'jpg' }}

Pas het beveiligingsniveau voor vertrouwde websites aan:

1. Open het startmenu van Windows, typ internetopties en druk op de Enter-toets.
2. Selecteer in het tabblad **Beveiliging** de zone **Vertrouwde websites.**
3. Vink het selectievakje **Beveiligde modus inschakelen** uit.  
   Opmerking: Dit selectievakje is niet meer beschikbaar vanaf Windows 11.
4. Pas in het tabblad **Beveiliging** het beveiligingsniveau voor **Vertrouwde sites** aan naar **Medium** of **Medium-laag**. Als je Medium-laag selecteert, kun je de stappen 6 tot 9 overslaan.
5. Klik op _OK_{:.doc-button}.
6. Klik op _Aangepast niveau..._{:.doc-button}.
7. Wijzig in het dialoogvenster **Beveiligingsinstellingen** de volgende instellingen:

   | Instelling                                           | Status             |
   | ------------------------------------------------- | ----------------- |
   | ActiveX-besturingselementen die zijn gemarkeerd als veilig voor uitvoeren van scripts | INGESCHAKELD           |
   | ActiveX-besturingselementen en -invoegtoepassingen uitvoeren                  | INGESCHAKELD           |
   | ActiveX-besturingselementen met handtekening downloaden                  | VRAGEN of INGESCHAKELD |
   | Automatisch vragen bij het uitvoeren van ActiveX-besturingselementen          | INGESCHAKELD           |

8. Klik op _OK_{:.doc-button}.
   De volgende melding wordt weergegeven: Weet u zeker dat u de instellingen voor deze zone wilt wijzigen?
9. Klik op _Ja_{:.doc-button}.
10. Klik op _OK_{:.doc-button} om het dialoogvenster te sluiten.

## Installatie van injixo-client

injixo Classic en injixo Enterprise WFM bevatten ActiveX-besturingselementen, waarvoor {% link_new Microsoft Edge in IE-modus | support/faq/configure-edge-internet-explorer-mode.md %} en de injixo client vereist zijn.

Als je een foutmelding ziet bij het aanmelden of in injixo:

- gebruik dan een {% link_new compatibele browser | getting-started/system-requirements.md | #browservereisten %}.
- installeer de injixo-client (zoals hieronder beschreven).

### Automatische installatie van de client (startpagina WFM)

Als je de bovengenoemde browserinstellingen gebruikt, dan wordt de client automatisch geïnstalleerd als WFM wordt ingevoerd.

1. Ga naar _WFM_{:.menu-item}.
2. Wacht totdat de download is afgesloten en de installatie van de client wordt gestart.
3. In de browser wordt de volgende melding weergegeven: Deze webpagina wil de volgende add-on uitvoeren: 'injixo Enterprise' van 'InVision AG'.<br>Als de melding niet verschijnt, vraag je IT-afdeling dan om ondersteuning.
4. Klik op _Installeren_{:.doc-button} om de vereiste add-ons te installeren.
5. Klik op _Installeren_{:.doc-button} om de client te installeren.

Na een succesvolle installatie heb je toegang tot de ActiveX-componenten.

### Handmatige installatie van de client

Installeer de client handmatig, bijvoorbeeld in injixo WFM Enterprise on-premise of als de automatische installatie niet werkt.

Opmerking: Als je een softwaredistributietool gebruikt, voer dan het installatieprogramma uit voor de gebruiker die zich later op de computer gaat aanmelden. Gebruik bijvoorbeeld msiexec.exe van Microsoft met de optie runas /user.

1. Download de meest recente [injixo-client](https://downloads.injixo.com/en#client-components).
2. Klik op _Uitvoeren_{:.doc-button} om het MSI-installatieprogramma uit te voeren.
3. Klik op _Volgende_{:.doc-button} om verder te gaan.
4. (Optioneel) Bewerk het installatiepad.
5. Selecteer **Iedereen** als de computer door meerdere gebruikers wordt gedeeld.
6. Klik op _Volgende_{:.doc-button} om verder te gaan.
7. Klik op _Installeren_{:.doc-button} om de installatie te starten.
   De volgende melding wordt weergegeven: Wilt u het volgende programma van een onbekende uitgever toestaan wijzigingen aan deze computer aan te brengen?
8. Klik op _Ja_{:.doc-button} om de melding te bevestigen.

Na een succesvolle installatie heb je toegang tot de ActiveX-componenten.
