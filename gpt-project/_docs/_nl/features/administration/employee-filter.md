---
title: Medewerkersfilters configureren
description: Gebruik de medewerkersfilter-editor om medewerkers te filteren op basis van een combinatie van criteria.
product_label:
  - advanced
  - enterprise
  - classic
---

Met medewerkersfilters kun je lijsten maken van medewerkers die aan meerdere criteria voldoen. De bewerkingsmogelijkheden zijn afhankelijk van je gebruikersrechten.

Medewerkersfilters werken op dezelfde manier als {% link_new groepen | features/administration/selections.md %}. Het verschil tussen medewerkersfilters en groepen is:

- Bij medewerkersgroepen zijn de groeperingscriteria gebaseerd op configuratie-elementen, zoals eenheid, kwalificatie en contract.
- Bij groepen kun je je eigen groeperingscriteria aanmaken.

Medewerkersfilters zijn alleen beschikbaar in injixo Classic, Advanced en Enterprise.
  
Om de filter-editor te openen, ga je naar _Plan > Dienstrooster-Center_{:.breadcrumbs} en klik je op **Filter editor**.

   {{ 1 | image: 'Medewerkersfilter', '70%' }}

## Een filter aanmaken

1. Klik in de sectie **Medewerkersfilter** op het pictogram Filter aanleggen {% icon item-add | icon-only %}.
2. Selecteer een type **Periode**:<br>
    - **Vrij kiesbaar**: Voer handmatig een periode in. Selecteer een datum in **vanaf** en **tot en met**.<br>
    - **Relatief**: Geef een periode aan voor de volgende, huidige of vorige week, maand of jaar.<br>
    - **Van menupunt overnemen**: De periode wordt automatisch ingesteld op de huidige dag.
3. Maak een [**filterdefinitie**](#een-filterdefinitie-aanmaken) aan.
4. Klik op _Weergeven_{:.doc-button} om de resultaten weer te geven.
5. Klik op _Gebruiken_{:.doc-button}.
6. Klik op het pictogram Filter opslaan {% icon save | icon-only %} om op te slaan.<br>Klik op het pictogram Filter opslaan als {% icon saveas | icon-only %} om je bestaande filter onder een andere naam op te slaan.

## Een filterdefinitie aanmaken

Een filterdefinitie bestaat uit een reeks voorwaarden om gegevens uit een grotere dataset te filteren en op te halen. Je kunt criteria definieren en een lijst met medewerkers ophalen die aan deze criteria voldoen.

1. Klik in de sectie **Filterdefinitie** op het {% icon item-add %}.
2. Selecteer in het **eerste vervolgkeuzemenu** een configuratiegegevenstype.
3. Selecteer in het **tweede vervolgkeuzemenu** een status.
4. (Optioneel) Selecteer [opties en relationele operators](#prioriteit-en-relationele-bewerkingstekens-gebruiken) voor groepen, medewerkerscategorieen of kwalificaties.
5. Klik op _Gebruiken_{:.doc-button}.

Klik op het {% icon item-edit %} om een filterdefinitie te bewerken.

## Een status gebruiken

### IS IN

De voorwaarde **IS IN** geeft resultaten weer die exact overeenkomen met de filterdefinitie.
 
1. Selecteer een een configuratiegegevenstype in het **eerste vervolgkeuzemenu**.
2. Selecteer **IS IN** in het **tweede vervolgkeuzemenu**.
3. Klik op _Criteria_{:.doc-button} om alle beschikbare criteria te bekijken en een criterium uit de lijst te selecteren.
4. Klik op de {% icon right-arrow-blue %} om criteria aan je groep toe te wijzen.
5. Klik in het venster **Criteria kiezen** op _Gebruiken_{:.doc-button}.
6. (Optioneel) Selecteer [opties en relationele operators](#prioriteit-en-relationele-bewerkingstekens-gebruiken) voor groepen, medewerkerscategorieen of kwalificaties.
7. Klik op _Gebruiken_{:.doc-button}.

### IS LIKE

De voorwaarde **IS LIKE** geeft resultaten weer die exact overeenkomen met de filterdefinitie.

1. Selecteer een een configuratiegegevenstype in het **eerste vervolgkeuzemenu**.
2. Selecteer **IS LIKE** in het **tweede vervolgkeuzemenu**.
3. Voer de tekst in die in het **tekstveld** moet verschijnen.
    - Gebruik * als placeholder om een willekeurige aantal tekens te vervangen.
    - Gebruik ? als placeholder om exact één teken te vervangen.
4. (Optioneel) Selecteer [opties en relationele operators](#prioriteit-en-relationele-bewerkingstekens-gebruiken) voor groepen, medewerkerscategorieen of kwalificaties.
7. Klik op _Gebruiken_{:.doc-button}.

## Prioriteit en relationele bewerkingstekens gebruiken

Met het selectievakje prioriteit en de relationele bewerkingstekens kun je medewerkers opnemen op basis van hun prioriteit en toewijzing aan de geselecteerde eenheid/medewerkergroep.  

1. Selecteer **Eenheid** of **Boekingsgroep** in het eerste vervolgkeuzemenu.
2. Vink het selectievakje **Prioriteit** aan.
3. Selecteer een relationeel bewerkingsteken in de lijst.
4. Voer in het invoerveld een prioriteitswaarde in.

Met het kwalificatie-configuratie-element kun je relationele bewerkingstekens gebruiken om alleen gekwalificeerde medewerkers met een bepaald kwalificatieniveau op te nemen:  

1. Selecteer in het vervolgkeuzemenu **Kwalificatie**.
2. Vink het selectievakje **Kwalificatieniveau** aan.
3. Selecteer een relationeel bewerkingsteken in de lijst.
4. Voer in het invoerveld de waarde van het kwalificatieniveau in.

## Filterdefinities koppelen

Je kunt individuele filterdefinities aan elkaar koppelen:

1. Maak of selecteer een [filter](#een-filter-aanmaken).
2. Maak een [filterdefinitie](#een-filterdefinitie-aanmaken) aan.
3. Selecteer een voorwaardelijk bewerkingsteken:<br>
  - **AND**: Neem medewerkers op die aan alle voorwaarden voldoen.  
  - **OR**: Neem medewerkers op die aan ten minste een van de voorwaarden voldoet.  
  - **NOT**: Sluit medewerkers uit die aan de voorwaarde NOT voldoen.
4. Maak een tweede filterdefinitie aan.
5. Klik op _Gebruiken_{:.doc-button}.

Om een groep aan te maken, begin je met een openingshaakje. Om de groep te sluiten, gebruik je een sluitingshaakje. Gebruik de pijlen naar boven en beneden om de verschillende filterdefinities te verplaatsen en sorteren.

## Voorbeeld van een filterdefinitie

Om medewerkers uit de eenheid New York te filteren die geen voltijdscontract van 40 uur hebben en geen deel uitmaken van de groep Extra uren, zou de filterdefinitie er als volgt uit zien:


```
Eenheid IS IN "New York"
AND
NOT
(
Contract IS IN "Voltijds 40u"
AND
Eenheid IS IN "Extra Uren"
)
```

Deze filterdefinitie selecteert alle medewerkers uit de eenheid New York en sluit vervolgens alle medewerkers uit die een voltijdscontract met 40 uren hebben en in de groep Extra Uren zitten:

- **IS IN** geeft de voorwaarde voor de eenheid aan.
- **AND** combineert de voorwaarden voor de filterdefinitie.
- **NOT** sluit de volgende voorwaarden uit.
- De haakjes openen en sluiten de groep van voorwaarden voor uitsluiting.
- **IS IN** selecteert medewerkers die een voltijdscontract met 40 uren hebben.
- **AND** combineert de voorwaarden binnen de haakjes.
- **IS IN** selecteert medewerkers die deel uitmaken van de groep Extra Uren.

## Filters bewerken

1. Selecteer een filter in het vervolgkeuzemenu **Medewerkersfilter**.
2. Bewerk de informatie die je wilt wijzigen.
3. (Optioneel) Om je filter een andere naam te geven, klik je op het {% icon item-edit %}.
4. Klik op het pictogram Filter opslaan {% icon save | icon-only %} om op te slaan.<br>Klik op het pictogram Filter opslaan als {% icon saveas | icon-only %} om je bestaande filter onder een andere naam op te slaan.
