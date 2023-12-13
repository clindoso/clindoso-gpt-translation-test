---
title: 2FA beheren
product_label:
  - essential
  - advanced
  - enterprise
description: Lees hoe je 2FA in- en uitschakelt voor de accounts van je medewerkers.
redirect_from:
  - nl/2fa/
redirect_reason: Updated filename on 14 July 2023
---

> Alleen gebruikers met admin-toegang kunnen twee-factor-authenticatie (2FA) voor andere gebruikers beheren.

## 2FA-instellingen van andere gebruikers bekijken

Volg de volgende stappen om de huidige 2FA-status van andere gebruikers te bekijken:
1. Ga naar _Account > Gebruikers_{:.breadcrumbs}.
2. In de kolom **2FA** aan de rechterkant wordt de 2FA-status van elke gebruiker weergegeven in de vorm van een schildpictogram. Beweeg de cursor over het schildpictogram voor meer informatie.
  - Rood pictogram {% icon 2FA-red | icon-only %}: 2FA is niet ingeschakeld.
  - Oranje pictogram met uitroepteken {% icon 2FA-orange | icon-only %}: Het gebruik van 2FA is verplicht gesteld voor de gebruiker. De gebruiker moet 2FA bij de volgende aanmelding inschakelen.
  - Groen pictogram met vinkje {% icon 2FA-green | icon-only %}: 2FA is ingeschakeld.

## Het gebruik van 2FA verplicht stellen voor andere gebruikers
Je kunt gebruikers ook verplichten tot het gebruik van 2FA. Het verplicht stellen van 2FA heeft twee consequenties:

- Gebruikers kunnen zich niet meer aanmelden als zij 2FA niet inschakelen.
- Gebruikers kunnen 2FA niet meer zelf uitschakelen voor hun persoonlijke accounts.

Voordat je het gebruik van 2FA voor andere gebruikers verplicht stelt, dien je ervoor te zorgen dat zij toegang hebben tot een van de {% link_new ondersteunde authenticator-apps | getting-started/use-two-factor-authentication.md | #basisvereiste-installeer-eerst-een-authenticator-app %}.

### Het gebruik van 2FA verplicht stellen voor individuele gebruikers

1. Ga naar _Account > Gebruikers_{:.breadcrumbs}.
2. Klik op de naam van de gebruiker voor wie je het gebruik van 2FA wilt verplichten.
   De pagina met gebruikersgegevens wordt geopend.
3. Vink in de sectie **Beveiliging** het selectievakje **2FA-activering verplichten** aan.
4. Klik op _Opslaan_{:.doc-button} om het inschakelen te bevestigen.

### Het gebruik van 2FA verplicht stellen voor alle gebruikers

1. Ga naar _Account > Beveiliging_{:.breadcrumbs}. Op deze pagina kun je het actuele gebruik van 2FA onder je gebruikers zien.
2. Klik op _2FA voor alle gebruikers verplicht stellen_{:.doc-button}.
   Je krijgt een groene bevestigingsmelding te zien. De tekst in de knop verandert in _Verplichting intrekken_{:.doc-button}.

### 2FA uitschakelen voor individuele gebruikers

Het is mogelijk om 2FA voor individuele gebruikers tijdelijk uit te schakelen. Ook kun je gebruikers vrijstellen van het verplichte gebruik van 2FA.

1. Ga naar _Account > Gebruikers_{:.breadcrumbs}.
2. Klik op de naam van de gebruiker voor wie je 2FA wilt uitschakelen.
   De pagina met gebruikersgegevens wordt geopend.
3. Vink in de sectie **Beveiliging** het selectievakje **2FA-activering verplichten** uit.
4. Klik op _Opslaan_{:.doc-button} om het uitschakelen te bevestigen.
