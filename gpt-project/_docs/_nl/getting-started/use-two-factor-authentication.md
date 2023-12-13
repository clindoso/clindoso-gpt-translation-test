---
title: Twee-factor-authenticatie (2FA) gebruiken
product_label:
  - essential
  - advanced
  - enterprise
description: Lees hoe je twee-factor-authenticatie voor je account in- en uitschakelt.
---

## Wat is twee-factor-authenticatie?

Twee-factor-authenticatie (2FA) voegt een extra beveiligingslaag toe aan je online accounts.  
Om je met je account met 2FA aan te melden, heb je het volgende nodig:

- je aanmeldgegevens
- een extra wachtwoord, dat met een ander apparaat wordt gegenereerd

> Schakel 2FA zo snel mogelijk in om je account beter te beveiligen.

## Basisvereiste: installeer eerst een authenticator-app

injixo ondersteunt de authenticator-apps die in de tabel hieronder worden genoemd.  
Als je een Android-apparaat gebruikt, dan download je de app in de Google Play Store. Heb je een Apple-apparaat, dan vind je de app in de Apple App Store.

|-------|--------|---------|
| Google Authenticator | [Apple App Store](https://apps.apple.com/us/app/google-authenticator/id388497605) | [Google Play Store](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) |
| Microsoft Authenticator | [Apple App Store](https://apps.apple.com/us/app/microsoft-authenticator/id983156458) | [Google Play Store](https://play.google.com/store/apps/details?id=com.azure.authenticator) |
| Authy | [Apple App Store](https://apps.apple.com/us/app/authy/id494168017) | [Google Play Store](https://play.google.com/store/apps/details?id=com.authy.authy) |

## 2FA inschakelen voor je account

Om 2FA in te schakelen voor je account, heb je toegang nodig tot een hoofdapparaat (bijvoorbeeld een computer) en je persoonlijke apparaat. Volg op je hoofdapparaat de volgende stappen uit:

1. Meld je aan bij injixo en klik rechtsboven in de navigatiebalk op je **gebruikersnaam**.
2. Klik op het tabblad **Beveiliging**. Bovenaan de pagina zie je de actuele status van je 2FA-instellingen.
3. Klik op _2FA inschakelen_{:.doc-button}.
4. Voer je wachtwoord in.
5. Klik op _Verder_{:.doc-button}.  
    De pagina Twee-factor authenticatie inschakelen wordt geopend. Hier worden de vervolgstappen weergegeven.

Voer op je persoonlijke apparaat de stappen uit die op de pagina Twee-factor authenticatie inschakelen worden weergegeven:

1. Installeer een van de [ondersteunde authenticator-apps](#basisvereiste-installeer-eerst-een-authenticator-app).
2. Open de **authenticator-app** op je apparaat en voeg een nieuw account voor injixo toe.
   Kies een van de volgende opties om verder te gaan:
   - Scan met de authenticator-app de **QR-code** die op de pagina Twee-factor authenticatie inschakelen wordt weergegeven.
   - Voer in de authenticator-app de **key** in die op de pagina Twee-factor authenticatie inschakelen wordt weergegeven.
Je authenticator-app is ingesteld en genereert vanaf nu eenmalige wachtwoorden (OTP).

Voer op je hoofdapparaat de volgende stappen uit:

1. Voer op de pagina Twee-factor authenticatie inschakelen in het veld **Eenmalig wachtwoord** een OTP in.
2. Klik op _Verder_{:.doc-button}.
3. Sla de back-upcodes op of download ze als bestand. Klik op _Downloaden_{:.doc-button} of _Kopiëren_{:.doc-button}. Als je geen back-upcodes ziet, dan zijn deze uitgeschakeld voor je bedrijfsaccount. <!-- feature flag -->

   > Bewaar je back-upcodes op een veilige plaats.
   >
   > Als je geen toegang meer hebt tot je persoonlijke apparaat, dan kun je je bij je account alleen nog met een back-upcode aanmelden.<br>Bewaar je back-upcodes op een veilige plaats, bijvoorbeeld in een wachtwoordmanager, of print ze uit. Zorg ervoor dat alleen jijzelf toegang hebt tot deze codes.

4. Vink het selectievakje **Ik heb mijn back-upcodes veilig opgeborgen** aan.
5. Klik op _2FA inschakelen_{:.doc-button}.  
   Je ontvangt een e-mail waarin de inschakeling van 2FA wordt bevestigd.  
Vanaf nu heb je zowel je aanmeldgegevens als een OTP nodig om je bij injixo aan te melden.

## Aanmelden terwijl 2FA is ingeschakeld

1. Voer op de aanmeldpagina van injixo je **e-mailadres** en **wachtwoord** in en klik op _Aanmelden_{:.doc-button}.  
2. Voer het **OTP** in dat door je authenticator-app is gegenereerd.  
   Elk OTP is slechts 30 seconden geldig. Daarna genereert de app een nieuw OTP.
3. Klik op _Controleer_{:.doc-button} om de aanmeldprocedure af te ronden.

Als je je niet kunt aanmelden, controleer dan in de authenticator-app of het OTP dat je hebt ingevoerd nog geldig is. Is de code niet meer geldig, voer dan een nieuw OTP in.  
Als je je nog steeds niet kunt aanmelden, volg dan de onderstaande instructies om je met een back-upcode aan te melden.

### Aanmelden met een back-upcode

Tijdens de configuratie van 2FA voor je account, ontvang je 10 back-upcodes. Als je geen toegang meer hebt tot je persoonlijke apparaat, dan kun je je met een van deze back-upcodes bij injixo aanmelden.

> Opmerking
>
> Gebruik alleen een back-upcode in geval van nood. Je kunt elke back-upcode slechts eenmaal gebruiken. Maak standaard altijd gebruik van een OTP.

Volg de volgende stappen om je met een back-upcode aan te melden in plaats van met een OTP:

1. Voer op de aanmeldpagina van injixo je **e-mailadres** en **wachtwoord** in en klik op _Aanmelden_{:.doc-button}.
2. Klik op de link **backup-code** onder het veld Eenmalig wachtwoord.
3. Voer in het veld **Back-upcode** een van je 10-cijferige back-upcodes in.
4. Klik op _Controleer_{:.doc-button} om de aanmeldprocedure af te ronden.

<!-- a tag required. configured name used in injixo UI link -->

### Aanmelden zonder je persoonlijke apparaat en back-upcodes

Als je je niet met 2FA kunt aanmelden en geen toegang hebt tot je back-upcodes, neem dan contact op met een gebruiker met adminrechten. Gebruikers met deze rol kunnen 2FA uitschakelen voor je account. Je kunt je dan zonder OTP aanmelden en je 2FA-instellingen resetten.

## 2FA gebruiken op een nieuw persoonlijk apparaat

Om op een ander apparaat OTP's te kunnen genereren, moet je 2FA voor je account tijdelijk uitschakelen, om het vervolgens op je nieuwe apparaat weer in te schakelen.

Als je 2FA niet zelf kunt uitschakelen, vraag dan een gebruiker met adminrechten om dit voor je account te doen.

## 2FA uitschakelen voor je account

> Opmerking
>
> Het uitschakelen van 2FA wordt niet aanbevolen. Als het gebruik van 2FA verplicht is gesteld voor je account, dan kun je het niet uitschakelen.

1. Meld je aan bij injixo en klik rechtsboven in de navigatiebalk op **je naam**.
2. Klik op het tabblad **Beveiliging**. Bovenaan de pagina zie je de actuele status van je 2FA-instellingen.
3. Klik op _2FA uitschakelen_{:.doc-button}.
4. Voer je **wachtwoord** in.
5. Klik op _Verder_{:.doc-button} om het uitschakelen te bevestigen.

Je ontvangt een e-mail waarin het uitschakelen van 2FA wordt bevestigd. Vanaf nu kun je je weer aanmelden zonder een OTP te gebruiken.

> Heb je de 2FA-uitschakelingsmail ontvangen, maar 2FA zelf niet uitgeschakeld?
>
> Controleer je account dan samen met een admin van je bedrijf. Overweeg je wachtwoord te wijzigen.
