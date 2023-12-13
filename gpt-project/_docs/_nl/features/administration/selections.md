---
title: Groepen aanmaken en beheren
description: Maak groepen aan en wijs medewerkers aan groepen toe.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: true
related_articles:
  - overwrite_title: Filteren met groepen
    filepath: best-practices/filter-with-selections.md
---

Groepen zijn groeperingscriteria waaraan je medewerkers kunt toewijzen om ze te filteren. Groepen werken op dezelfde manier als {% link_new medewerkersfilters | features/administration/employee-filter.md %}. Het verschil tussen medewerkersfilters en groepen is:

- Bij groepen kun je je eigen groeperingscriteria aanmaken.
- Bij medewerkergroepen zijn de groeperingscriteria gebaseerd op configuratie-elementen, zoals eenheid, kwalificatie en contract.

Daarnaast zijn medewerkersfilters alleen beschikbaar in injixo Classic, Advanced en Enterprise.

Groepen worden vaak gebruikt om medewerkers te groeperen die:

- aan een bepaalde supervisor rapporteren;
- thuiswerken;
- onlangs zijn aangenomen en extra ondersteuning of begeleiding nodig hebben;
- op korte termijn kunnen invallen voor andere medewerkers;
- extra verantwoordelijkheden hebben die niet relevant zijn voor het plannen, maar wel belangrijk kunnen zijn, bijvoorbeeld medewerkers die EHBO-vaardigheden hebben.

Als je injixo Essential gebruikt, kun je groepen gebruiken om medewerkers op basis van configuratie-elementen te groeperen, bijvoorbeeld op eenheid, kwalificatie of contract.

## Groepen aanmaken

1. Ga naar _Plan > Configuratie > Groepen_{:.breadcrumbs}.
2. Klik op het pictogram Nieuw {% icon item-add | icon-only %} in de linker bovenhoek.  
    Aan de rechterkant verschijnt een configuratievenster.
3. Vul de volgende velden in:
    - **Naam**: Unieke naam voor de groep (max. 50 tekens).
    - **Afkorting**: Afkorting voor de naam (max. 25 tekens).
    - **Beschrijving**: Optionele beschrijving zodat andere gebruikers begrijpen waar de groep voor staat.
4. Klik op _OK_{:.doc-button}.

## Medewerkers aan groepen toewijzen

Om medewerkers aan groepen toe te wijzen, moet je eerst {% link_new een groep aanmaken | features/administration/selections.md | #groepen-aanmaken %}.

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}.
2. Klik op de medewerker die je aan een groep wilt toewijzen.  
   Aan de rechterkant verschijnt een configuratievenster.
3. Klik in de sectie **Groepen** op het pictogram Toevoegen {% icon item-add | icon-only %}
4. Vul de volgende velden in:  
   - **Groep**: Klik op de selectie die je aan de medewerker wilt toewijzen.
   - (Optioneel) **geldig vanaf/geldig tot en met**: Datumbereik om de geldigheidsperiode van de groep te beperken. Als je deze velden leeg laat, is de groep onbeperkt geldig. Lees meer over {% link_new geldigheidsperiodes | features/administration/set-a-validity-period.md %}.
5. Klik op _OK_{:.doc-button}.

Klik op het pictogram Bewerken {% icon item-edit | icon-only %} om een groep te bewerken waaraan een medewerker is toegewezen. Klik op het {% icon item-delete %} om de groepstoewijzing te verwijderen.

## Medewerkers beheren in een groep

In _Plan > Configuratie > Medewerkers_{:.breadcrumbs} kun je een overzicht weergeven van de medewerkers in een groep en hun instellingen bewerken.

Je kunt de volgende vervolgkeuzemenu's gebruiken om medewerkers te filteren:

- **Eenheid**: Selecteer alle eenheden.
- **Groep**: Selecteer een groep.  
   Als het vervolgkeuzemenu **Groep** niet wordt weergegeven, klik dan op het pictogram **Filter activeren** {% icon selection | icon-only %} bovenaan de pagina.

injixo geeft alle medewerkers in de groep weer. Klik op de rij van een medewerker in de lijst om de instellingen van de betreffende medewerker aan te passen.

## Groepen combineren

injixo Classic-, Advanced- en Enterprise-klanten kunnen groepen aan een bestaande groep toevoegen. De groep waaraan andere groepen worden toegewezen, wordt een superieure groep. De toegewezen groepen zijn ondergeschikte groepen. Zo kun je in een keer medewerkers uit alle ondergeschikte groepen filteren door alleen de superieure groep te gebruiken.

Om voor een groepenhierarchie tussen superieure en ondergeschikte groepen te zorgen, klik je eerst op {% link_new de superieure en daarna op ondergeschikte groepen | features/administration/selections.md | #groepen-aanmaken %}.

Ga als volgt te werk om een groep aan andere groep toe te wijzen:

1. Ga naar _Plan > Configuratie > Groepen_{:.breadcrumbs}.
2. Klik op de groep in de groepenlijst die je als superieure groep wilt gebruiken.  
   Aan de rechterkant verschijnt een configuratievenster.
3. Klik in de sectie **Groepen** op het pictogram Nieuw {% icon item-add | icon-only %}.
4. Vul de volgende velden in:  
   - **Groepen**: Klik op de groep die je als ondergeschikte groep wilt toewijzen.
   - **geldig vanaf/geldig tot en met**: Datumreeks om de periode waarin ondergeschikte groepen aan de superieure groep wordt toegewezen. Als je deze velden leeg laat, is de groep onbeperkt geldig.
5. Klik op _OK_{:.doc-button}.

Klik op het pictogram Bewerken {% icon item-edit | icon-only %} of het pictogram Verwijderen {% icon item-delete | icon-only %} om een ondergeschikte groep te bewerken of verwijderen.

> Groepenhiërarchie
>
> De hiërarchie tussen superieure en ondergeschikte groepen is niet zichtbaar in _Plan > Configuratie > Medewerkers_{:.breadcrumbs}. Om te zien of een groep een superieure groep is, ga je naar _Plan > Configuratie > Groepen_{:.breadcrumbs} en klik je op een groep in de sectie **Groepen**. Je kunt superieure groepen een naam geven waaruit de groepenhiërarchie duidelijk wordt.

## Een groep verwijderen

1. Ga naar _Plan > Configuratie > Groepen_{:.breadcrumbs}.
2. Klik in de lijst op een groep die je wilt verwijderen.
3. Klik op het pictogram Verwijderen {% icon item-delete | icon-only %} in de linker bovenhoek.
4. Klik op _Ja_{:.doc-button} om te bevestigen.
