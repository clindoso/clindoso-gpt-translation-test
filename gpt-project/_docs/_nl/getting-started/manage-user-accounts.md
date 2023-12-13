---
title: Gebruikersaccounts beheren
description: Gefactureerde en niet gefactureerde gebruikers kunt bekijken. Gebruikers aanmaken, bewerken en verwijderen. gebruikerstoegang kunt beheren door gebruikersrollen toe te voegen.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-2fa.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
redirect_from:
  - nl/user-administration/
redirect_reason: page used in intercom, updated filename on 06 December 2022
---

Configureer gebruikersaccounts in injixo om de medewerkers in je organisatie te beheren. 

Onder _Account > Gebruikers_{:.breadcrumbs} vind je een compleet overzicht van alle gebruikers:
- Gefactureerde gebruikers: In dit tabblad vind je alle actieve gebruikers in je injixo-tenant.
- Niet gefactureerde gebruikers: In dit tabblad vind je alle {% link_new gedeactiveerde gebruikers | features/administration/deactivate-employees.md %} die zich niet meer in injixo kunnen aanmelden. Je organisatie wordt niet meer {% link_new gefactureerd | getting-started/how-does-billing-work.md %} voor gedeactiveerde gebruikers.

Gebruik het zoekveld boven de gebruikerslijst om een of meerdere individuele gebruikers te vinden. Gebruik komma's om de namen of e-mailadressen van elkaar te scheiden.
Klik op de kolomkop **Gebruikersrollen** om gebruikers op gebruikersrol te filteren. Er wordt een dialoogvenster geopend waarin je een of meerdere rollen kunt selecteren. Alle gebruikers die ten minste een van de geselecteerde rollen hebben, worden in de gebruikerslijst weergegeven.

## Een gebruiker aanmaken

Gebruikers worden ook medewerkers genoemd. Er zijn drie plaatsen in injixo waar je gebruikers kunt aanmaken:
- _Account > Gebruikers_{:.breadcrumbs}
- _WFM > Administratie > Planning > Medewerkers_{:.breadcrumbs}
- {% link_new People | features/people/manage-people.md | #een-nieuwe-medewerker-aanmaken %}

> Opmerking
> 
> Je hoeft een gebruiker maar op een van deze plaatsen aan te maken. injixo synchroniseert deze gebruikersgegevens automatisch op de twee overige plaatsen.

Volg deze stappen om een gebruiker aan te maken:

1. Ga naar _Account > Gebruikers_{:.breadcrumbs}.
2. Klik op _Gebruiker aanmaken_{:.doc-button}.
3. Vul de gegevens van de gebruiker in en klik op _Aanmaken_{:.doc-button}.

## Een gebruikersaccount bewerken

Je kunt op twee plaatsen een gebruiker aanmaken. Welke plaats je kiest, is afhankelijk van je doel. In de onderstaande tabel vind je een overzicht van de verschillende configuratie-opties en waar je deze in injixo aantreft. Beide plaatsen zijn toegankelijk vanuit People.

| Ik wil                                          | Plaats in injixo                                                                             |
| -------------------------------------------------- | ------------------------------------------------------------------------------------- |
| {% link_new Planningsrelevante instellingen configureren voor een gebruiker | features/administration/employee-overview.md | #overzicht-van-medewerkerinstellingen %} (bijvoorbeeld activiteiten toewijzen, kwalificatieniveaus toewijzen, beschikbaarheid instellen) | _WFM > Administratie > Planning > Medewerkers_{:.breadcrumbs} |
| {% link_new Informatie over het dienstverband bewerken | getting-started/manage-user-accounts.md | #een-gebruikersaccount-deactiveren %} voor een gebruiker       | _WFM > Administratie > Planning > Medewerkers_{:.breadcrumbs} |   
| Taal en tijdzone wijzigen voor een medewerker | _Account > Gebruikers_{:.breadcrumbs} |
| {% link_new Een gebruikersrol toewijzen aan een medewerker | getting-started/configure-user-roles.md | #gebruikersrollen-aan-gebruikers-toewijzen %} | _Account > Gebruikers_{:.breadcrumbs} |
| {% link_new Twee-factor-authenticatie verplicht stellen | getting-started/manage-2fa.md %}   | _Account > Gebruikers_{:.breadcrumbs} |

Als je een gebruikersaccount wilt bewerken, bijvoorbeeld een e-mailadres wijzigen, volg dan de volgende stappen:

1. Ga naar _Account > Gebruikers_{:.breadcrumbs}.
2. Klik op de gebruikersnaam van een bestaande gebruiker.
3. Wijzig de gebruikersinstellingen.
4. Klik op _Opslaan_{:.doc-button}.

### Een gebruiker admin-toegang geven

1. Ga naar _Account > Gebruikers_{:.breadcrumbs}.
2. Klik op de gebruikersnaam van een bestaande gebruiker.
3. Vink in de sectie **Admin-toegang** het selectievakje **Geef admin-toegang** aan.
4. Klik op _Opslaan_{:.doc-button}.

### Een gebruiker deblokkeren

Na drie aanmeldpogingen met een onjuist wachtwoord worden gebruikersaccounts geblokkeerd. Volg deze stappen om geblokkeerde gebruikers te deblokkeren:

1. Ga naar _Account > Gebruikers_{:.breadcrumbs}.<br>
In de gebruikerslijst wordt naast de naam van de geblokkeerde gebruiker een geel {% icon lock %} weergegeven.
2. Klik op de gebruikersnaam van de geblokkeerde gebruiker.
3. Klik aan de rechterkant in de sectie **Beveiliging** op _Ontgrendel gebruiker_{:.doc-button}.

Als je een gebruiker hebt gedeblokkeerd, is het raadzaam om voor de betreffende gebruiker een nieuw wachtwoord in te stellen. 

### Een nieuw gebruikerswachtwoord instellen

Als gebruikers hun wachtwoord zijn vergeten, dan kunnen ze dit zelf resetten door op de startpagina op **Wachtwoord vergeten?** te klikken. Je kunt ook zelf een nieuw wachtwoord voor hen instellen, bijvoorbeeld nadat hun account is geblokkeerd.
Volg deze stappen om een nieuw wachtwoord in te stellen voor een gebruiker:

> Opmerking
>
> Gebruikers worden niet over wachtwoordwijzigingen geïnformeerd. Je moet ze hiervan zelf op de hoogte stellen.

1. Ga naar _Account > Gebruikers_{:.breadcrumbs}.
2. Klik op de gebruikersnaam van een bestaande gebruiker.
3. Klik aan de rechterkant in de sectie **Beveiliging** op _Stel nieuw wachtwoord in_{:.doc-button}.
4. Voer een nieuw wachtwoord in voor de gebruiker.
5. Klik op _Opslaan_{:.doc-button}.

## Een gebruikersaccount deactiveren

Lees {% link_new dit artikel | features/administration/deactivate-employees.md %} voor meer informatie over de gevolgen van het deactiveren van gebruikersaccounts.

1. Ga naar _Account > Gebruikers_{:.breadcrumbs}.
2. Klik op de gebruikersnaam van een bestaande gebruiker.
3. Klik rechtsonder op _Verwijderen_{:.doc-button}. Er wordt een venster geopend.
4. Klik op _Medewerkers_{:.doc-button} en voer een Datum van uittrede in. Zo blijven alle planningsgegevens behouden. Je kunt de gebruiker later weer opnieuw activeren.

Lees hoe je {% link_new een gebruiker opnieuw activeert | features/administration/deactivate-employees.md | #medewerkers-opnieuw-activeren %}.

## Een gebruikersaccount verwijderen

> Waarschuwing
>
> Je kunt een verwijderd gebruikersaccount niet opnieuw activeren. De gebruikersaccount wordt uit alle actuele en toekomstige planningen verwijderd waarin de gebruiker was ingepland.

Volg de volgende stappen om een gebruikersaccount permanent te verwijderen:

1. Ga naar _Account > Gebruikers_{:.breadcrumbs}.
2. Klik op de gebruikersnaam van een bestaande gebruiker.
3. Klik rechtsonder op _Verwijderen_{:.doc-button}.  
   Er wordt een venster geopend.
4. Vink het selectievakje **Ik begrijp dat het gebruikersprofiel en alle planningsgegevens voor \<gebruikersnaam\> zullen worden verwijderd** aan.
5. Klik op _Verwijderen_{:.doc-button}. 

## De gebruikerslijst als CSV-bestand exporteren

Je kunt de volledige of een gefilterde versie van de gebruikerslijst als CSV-bestand exporteren. Zo kun je dit CSV-bestand in externe databases en tools importeren, zoals Data Warehouse-databases, en SAP- en HR-systemen.

1. Ga naar _Account > Gebruikers_{:.breadcrumbs}.
2. (Optioneel) Om de lijst met weergegeven gebruikers te verfijnen, kun je het zoekveld of het rollenfilter gebruiken.
3. Klik rechtsboven op _Exporteer naar CSV_{:.doc-button}.  
   Het CSV-bestand wordt naar je computer gedownload.

Het CSV-bestand waarin de inhoud met komma's van elkaar is gescheiden, bevat de achternaam, voornaam en het e-mailadres van de gebruiker. De exportfunctie gebruikt een vaste bestandsextensie die niet kan worden gewijzigd.
