---
title: Single sign-on (SSO)
product_label:
  - advanced
  - enterprise
description: Lees hoe je SSO configureert en gebruikt in injixo.
---

SSO is een authenticatieproces waarmee gebruikers zich met slechts één paar aanmeldgegevens bij meerdere toepassingen kunnen aanmelden. Er wordt een vertrouwensrelatie tot stand gebracht tussen een centrale identiteitsbeheerservice (identiteitsprovider = IdP) en een toepassing (service provider = SP), in dit geval injixo.

De IdP is een product van een externe aanbieder, zoals OneLogin, Microsoft Azure AD, Okta of Google. Door SSO te gebruiken, profiteert je organisatie van een uniform beveiligingsbeleid, zoals twee-factor-authenticatie en wachtwoordrotatie. Gebruikers authenticeren zich bij de IdP, die ze vervolgens naar injixo leidt.

De IdP-configuratie is getest met de bovenstaande identiteitsproviders. Als je je specifieke IdP niet kunt integreren, neem dan contact met ons op.

## Vereisten

Om injixo met de door jou gekozen IdP te integreren, moet aan de volgende vereisten zijn voldaan:

- Ondersteuning van SAML 2.0-protocol
- Toegang tot federatiemetadata via internet 
- Het e-mailadres dat bij injixo is geregistreerd en je IdP moeten met een mailbox zijn verbonden.

> Activeer versleutelde aanmeldgegevens / token encryption voor een betere beveiliging (sterk aanbevolen).

## SSO inschakelen voor je account

Alleen gebruikers met admintoegang kunnen SSO inschakelen.

1. Registreer injixo als een nieuwe SAML- of SSO-toepassing in je IdP.  
   Je kunt [dit injixo-logo](/assets/img/common/injixo-logo.png) downloaden en aan de pagina van de webtoepassing toevoegen.

2. Ga in injixo naar _Account > Beveiliging_{:.breadcrumbs} en configureer SSO onder **Single sign-on**.

3. In de sectie **injixo SAML-metagegevens** heb je twee opties, afhankelijk van het feit of je IdP bestanduploads ondersteunt:

   - Ondersteunde bestanduploads: Klik op _{% icon download | icon-only %} Download_{:.doc-button} en sluit de IdP-configuratie af met het gedownloade XML-bestand.
   - Niet-ondersteunde bestanduploads: Klik op **Gegevens dienstverlener** en voeg de weergegeven URL's toe aan je IdP-configuratie.

4. (Optioneel) Als je versleutelde SAML-asserties gebruikt, klik je op _{% icon download | icon-only %} Download_{:.doc-button} in de sectie **Token Encryption**. Voeg de gedownloade certificaten toe aan je IdP-configuratie.
5. Afhankelijk van het feit of je IdP een URL voor federatiemetadata biedt, rond je de configuratie als volgt af:

   - IdP biedt een federatiemetadata-URL: Kopieer je federatiemetadata-URL voor de geregistreerde toepassing van je IdP. Plak de URL in het veld **Federatieve metagegevens-URL** in de sectie **Identity Provider**.
   - IdP biedt geen federatiemetadata-URL:  In dit geval dien je het metagegevens-XML-bestand van de federatie zelf te downloaden en te hosten. Leer bijvoorbeeld hoe je je eigen aangepaste [SAML-toepassing configureert met Google](https://support.google.com/a/answer/6087519?hl=nl).

6. Klik op _Configuratie opslaan_{:.doc-button}.  
   > SSO is nu actief  
   >  
   > Gebruikers kunnen zich nog steeds aanmelden met hun gebruikersnaam en wachtwoord. Klik op _Uitschakelen_{:.doc-button} om SSO opnieuw in te schakelen.  
   > nog hoger beveiligingsniveau, kun je [SSO voor alle gebruikers verplicht stellen](#het-gebruik-van-sso-voor-alle-gebruikers-verplicht-stellen) nadat je de configuratie bij de volgende stap hebt getest.
   
## De SSO-configuratie testen

Klik op _Configuratie testen_{:.doc-button} om het aanmelden via de IdP te testen. De IdP genereert een SAML-reactie die naar injixo wordt gestuurd. Je wordt teruggeleid naar de aanmeldpagina van je IdP, waar je de IdP-aanmeldgegevens invoert. Als de IdP-configuratie correct is en het authenticatieproces succesvol is, word je ingelogd bij injixo.

{{ 4 | image: 'Geslaagde test van de SSO- configuratie voor de huidige gebruiker', '80%' }}

### Test niet geslaagd? Configureer de SAML-reactie.
<!-- A valid SubjectConfirmation was not found on this Response in our internal server logs -->

De SAML-reactie van de IdP bevat de bevestiging van de geauthenticeerde gebruiker met attributen en profielinformatie. Als de test niet is geslaagd en je een foutmelding ziet, controleer dan de configuratie van de toepassing, de configuratie van de gebruiker en de attributen Recipient, InResponseTo, NotBefore en NotOnOrAfter die in de IdP zijn ingesteld. 

Je kunt het SubjectConfirmation-XML-element in de SAML-reactie in de ontwikkelaarstools van je browser of in de externe SAML-tools debuggen. Deactiveer de versleutelde beweringen om de reactie niet-versleuteld in platte tekst te bekijken.

Voorbeeld van een SubjectConfirmation-XML-element in een SAML-reactie:

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

## Het gebruik van SSO voor alle gebruikers verplicht stellen

Om te testen of de configuratie juist is, kun je alle aanmeldingen met gebruikersnaam en wachtwoord deactiveren door SSO voor alle gebruikers verplicht te stellen. Zorg er wel voor dat:

- alle injixo-gebruikers in de IdP en in injixo bestaan.
- het injixo-e-mailadres in de juiste IdP-identifier is ingevoerd.
- alle injixo-gebruikers zijn aan de IdP-toepassing voor SSO in injixo toegewezen.

Zodra SSO verplicht is gesteld, is het niet meer mogelijk om:

- je aan te melden met een gebruikersnaam en wachtwoord (alle bestaande wachtwoorden worden ongeldig).
- wachtwoorden te resetten in injixo (zowel door gebruikers als door beheerders).
- toegang tot injixo buiten de IdP te beheren.

Stel het gebruik van SSO verplicht in sectie **3\. Verplicht stellen**. De knop Verplicht stellen{:.doc-button} wordt geactiveerd nadat de test van de SSO-configuratie is geslaagd.

{{ 5 | image: 'Knop om SSO voor alle gebruikers verplicht te stellen', '80%' }}

## E-mailadressen wijzigen nadat SSO verplicht is gesteld

Zodra je SSO verplicht hebt gesteld, kunnen gebruikers hun e-mailadressen zelf niet meer wijzigen, omdat het injixo-e-mailadres overeen moet komen met de juiste IdP-identifier.

Alleen gebruikers met beheerdersrechten kunnen e-mailadressen in injixo wijzigen.

## Aanmelden met SSO

Zodra SSO is geconfigureerd, kunnen je gebruikers zich aanmelden via [https://www.injixo.com/login/sso](https://www.injixo.com/login/sso). Ze voeren hun e-mailadres in en komen vervolgens op de aanmeldpagina van de IdP terecht. Als gebruikers al zijn aangemeld, dan worden ze automatisch teruggeleid naar injixo. Als ze nog niet zijn aangemeld, dan dienen zij hun IdP-wachtwoord in te voeren.

## Toegang tot injixo intrekken

Om de injixo-toegangsrechten van een gebruiker via SSO in te trekken, dien je de injixo-gebruikerstoewijzing in de IdP te verwijderen. Opmerking: Als de gebruiker in injixo nog steeds bestaat, dan ontvangt deze nog steeds facturen. Om kosten te voorkomen, dien je {% link_new de gebruiker ook te deactiveren of verwijderen | features/administration/deactivate-employees.md %}.

## SSO uitschakelen

Om SSO uit te schakelen en aanmelden met gebruikersnaam en wachtwoord weer toe te staan, kan een gebruiker met adminrechten SSO uitschakelen. De IdP-verbinding en alle ingevoerde configuratiegegevens worden dan verwijderd. Nadat SSO is uitgeschakeld, ontvangen alle actieve gebruikers een e-mail om een nieuw wachtwoord voor injixo in te stellen. Daarna kunnen zij zich weer met hun gebruikersnaam en wachtwoord aanmelden bij [https://www.injixo.com/login](https://www.injixo.com/login).

## SSO op meerdere tenants gebruiken

Als je organisatie meerdere tenants heeft, en je (een aantal van) je gebruikers toegang wilt geven tot meer dan een tenant, dan werkt de standaard SSO-configuratie niet. Neem contact op met je consultant om een configuratie in te stellen voor deze specifieke usecase.

<!-- SSO for multiple tenants can be activated by the feature flag multi_tenant_sso, see also https://github.com/ivx/internal-support-documentation/tree/main/Cortex-->
