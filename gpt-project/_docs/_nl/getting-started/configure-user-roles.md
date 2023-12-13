---
title: Gebruikersrollen configureren
redirect_from:
  - /nl/gebruikers- en-rolautorisatie/
redirect_reason: renamed file in June 2021
description: Lees welke gebruikersrollen er zijn, wijzig hun rechten, maak nieuwe rollen aan en wijs gebruikersrollen aan gebruikers toe).
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-user-accounts.md
---

## Wat zijn gebruikersrollen?

Een gebruikersrol bepaalt welke rechten een groep gebruikers heeft:

- voor de producten en features in injixo, bijvoorbeeld voor _Forecast_{:.menu-item}.
- voor de features in WFM, bijvoorbeeld voor _WFM > Administratie_{:.breadcrumbs}.

injixo heeft rolcategorieen, elk met een {% link_new standaard gebruikersrol | getting-started/default-user-roles.md | #standaard-gebruikersrollen %} met vooraf ingestelde toegangsrechten. Als je in een rolcategorie een nieuwe gebruikersrol toevoegt, dan krijgt deze de toegangsrechten van de standaard gebruikersrol voor de producten en features.<br>
De rolcategorie Overigen heeft geen standaard gebruikersrol.

### Gebruikersrollen bekijken en beheren

Ga naar _Account > Gebruikersrollen_{:.breadcrumbs}.  
   Gebruikersrollen worden gegroepeerd in vooraf gedefinieerde rolcategorieën (zoals de rolcategorie Planner). Rolcategorieën zijn handig om toegangsrechten te beheren. Je kunt een gebruikersrol ook van de ene rolcategorie naar een andere slepen of de zoekfunctie gebruiken om gebruikersrollen op  naam te zoeken.
   
   > Rechten voor nieuwe functionaliteiten worden toegekend op basis van de rolcategorie.  
   >   
   >Rechten voor nieuwe injixo-functionaliteiten worden automatisch aan gebruikersrollen toegewezen op basis van hun rolcategorie. Zo is een nieuwe functionaliteit voor planners toegankelijk voor alle gebruikersrollen in de rolcategorie Planner. Als je een gebruikersrol van de rolcategorie Planner naar een andere rolcategorie verplaatst, dan heeft deze niet automatisch meer de rechten voor de nieuwe Planner-functionaliteit. Indien nodig kan een gebruiker met adminrechten handmatig rechten aan de gebruikersrol toekennen. Datzelfde geldt voor gebruikersrollen in de rolcategorie Overigen. De rechten voor deze categorie moeten altijd handmatig worden toegevoegd.

   {{ 1 | image: "Categorieën in overzicht gebruikersrollen", '80%' }}

### Nieuwe gebruikersrollen aanmaken

1. Klik op het blauwe {% icon plus %} van een van de rolcategorieën. Beweeg je cursor over de **i** pictogrammen voor meer informatie over elke rolcategorie.

   - Categorie Overigen: Er wordt een blanco gebruikersrol aangemaakt. Er zijn geen ingestelde standaardrechten.
   - Categorieën voor {% link_new standaard gebruikersrollen | getting-started/default-user-roles.md %}: De standaardrechten voor injixo-features worden vooraf ingesteld.  De toegangsrechten voor WFM-features zijn niet ingesteld. 
  > Opmerking
  >
  > Als je een nieuwe gebruikersrol aanmaakt, moet je handmatig [toegangsrechten toekennen voor de features in WFM](#wfm-rechten-instellen).

2. Op de pagina **Een gebruikersrol aanmaken** kun je de gebruikersrol configureren:

   - **Basisinformatie**: Voer een **naam**, een **afkorting** en een optionele **omschrijving** in.
   - **Rolcategorie**: Geeft de vooraf geselecteerde **rolcategorie** weer.

3. (Optioneel) Bewerk de standaardrechten. In de sectie **Rechten** geeft een grijs vinkje naast een sectie aan die alle rechten voor deze module standaard worden toegekend. Een grijs minpictogram geeft aan dat sommige rechten voor deze feature niet standaard worden toegekend.  
   - Product: Om aan alle features in een product rechten toe te kennen, vink je het selectievakje naast de modulenaam aan.
   - Feature: Om rechten voor afzonderlijke features toe te kennen, klik je op de pijl naar beneden vóór de betreffende productnaam. Vink het/de selectievakje(s) naast de feature(s) aan.
   - Om alle secties te bekijken of te sluiten, klik je op **Alles inklappen**/**alles uitklappen**.
   - Klik op **Terugzetten naar de standaardinstelling** om de geselecteerde rechten voor de standaard gebruikersrol terug te zetten.
4. Klik vervolgens op _Gebruikersrol aanmaken_{:.doc-button} om de nieuwe gebruikersrol op te slaan. Om [WFM-rechten](#wfm-rechten-instellen) voor de nieuwe gebruikersrol in te stellen, klik je op _Aanmaken en naar rolautorisatie gaan_{:.doc-button}.

   {{ 2 | image: "Pagina gebruikersrol aanmaken", '80%' }}

### Gebruikersrollen aan gebruikers toewijzen

1. Ga naar _Account > Gebruikers_{:.breadcrumbs}.
2. Klik op een **naam**.
3. Vink onder **Gebruikersrol(len) toewijzen** een of meerdere selectievakjes aan. Om de weergegeven gebruikersrollen te filteren, gebruik je het invoerveld **Gebruikersrollen zoeken**.
4. Klik op _Opslaan_{:.doc-button}.

   {{ 6 | image: 'Gebruikersrollen toewijzen', '80%'}}

## WFM-rechten instellen

1. Selecteer een gebruikersrol in _Account > Gebruikersrollen_{:.breadcrumbs}.
2. Klik in de sectie **Rechten** op _Ga naar Rolautorisatie_{:.doc-button}.  
   Je komt automatisch in _WFM > Administratie > Systeem > Rolrechten_{:.breadcrumbs} terecht.
3. Vink in de sectie **Navigator** aan de rechterkant  de selectievakjes aan of uit om rechten toe te voegen of te verwijderen.

{{ 4 | image: "Navigatorsectie in WFM-rolautorisatie", '60%' }}

We raden aan om alleen rechten op gebruikersrolniveau te gebruiken. Indien nodig kun je de rechten voor individuele gebruikers wijzigen. Ga naar _WFM > Administratie > Systeem > Gebruikersautorisatie_{:.breadcrumbs} om rechten voor individuele gebruikers te wijzigen.

## Toegangsrechten van teams beheren: Toegang tot configuratiegegevens beperken

Als je organisatie uit verschillende teams bestaat en je de toegang tot gegevens van de teams wilt beperken, dan kun je meerdere gebruikersrollen aan een gebruiker toewijzen. injixo combineert de rechten die bij de verschillende gebruikersrollen horen. Je kunt de toegang tot bepaalde elementen zoals eenheden, dagmodellen, activiteiten of rapporten beperken.

**Voorbeeld**

Als al je planners toegang moeten hebben tot de planning, maar alleen de gegevens van hun eigen eenheid mogen bewerken, dan kun je aan elke planner twee gebruikersrollen toewijzen.

Je kunt een nieuwe gebruikersrol aanmaken zonder toegang tot bepaalde eenheden, of de toegangsrechten tot alle eenheden uit een bestaande gebruikersrol verwijderen. Volg de volgende stappen om de toegangsrechten tot alle eenheden voor een bestaande gebruikersrol te verwijderen:

1. Ga naar _Account > Gebruikersrollen_{:.breadcrumbs}.
2. Selecteer de gebruikersrol.
3. Klik op _Ga naar rolautorisatie_{:.doc-button}.
4. Scrol naar de sectie **Eenheden** (of gebruik de snelkoppeling bovenaan).
5. Klik op het {% icon item-delete %} naast [ALLE] om de toegang tot alle eenheden te verwijderen.
6. Klik op _OK_{:.doc-button}.

Volg de volgende stappen om aan andere rollen toegangsrechten tot de specifieke eenheid toe te kennen: 

1. Selecteer de tweede gebruikersrol.
2. Klik in de sectie **Eenheden** op het {% icon item-add %}.
3. Selecteer de eenheid of eenheden in de lijst. Houd **CTRL** of **Shift** ingedrukt terwijl je verschillende planningseenheden selecteert.
4. Vink onder **Toegangsrechten** een of meerdere selectievakjes aan rechten voor **lezen**, **bewerken** en **verwijderen** te verlenen.
5. Klik op _OK_{:.doc-button}.

Om de configuratie af te ronden, ga je naar _Account > Gebruikers_{:.breadcrumbs}, waar je [de rollen aan je gebruikers kunt toewijzen](#gebruikersrollen-aan-gebruikers-toewijzen).


## Aangepaste of standaard gebruikersrollen bewerken

1. Ga naar _Account > Gebruikersrollen_{:.breadcrumbs}.
2. Selecteer de gebruikersrol die je wilt wijzigen.
3. Breng wijzigingen aan de gebruikersrol aan en klik op _Wijzigingen opslaan_{:.doc-button}.

## Aangepaste gebruikersrollen verwijderen

1. Ga naar _Account > Gebruikersrollen_{:.breadcrumbs}.
2. Selecteer de gebruikersrol.
3. Klik rechtsonder op _Gebruikersrol verwijderen_{:.doc-button}. Standaard gebruikersrollen kunnen niet worden verwijderd.
