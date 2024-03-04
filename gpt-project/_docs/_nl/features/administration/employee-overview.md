---
title: Medewerkers configureren
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Maak medewerkers aan en configureer ze voor het planningsproces.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/calculate-a-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/calculate-staff-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
---

In injixo kun je op drie plaatsen een medewerker aanmaken en bewerken. Welke plaats je kiest, is afhankelijk van je usecase. De onderstaande tabel bevat een overzicht van de verschillende plaatsen in injixo waar je medewerkers kunt configureren en wat je waar instelt.

| Plaats                                           | Beschrijving              |
| ----------------------------------------------- | ------------------------ |
| _Plan > Configuratie > Medewerkers_{:.breadcrumbs}   | {% link_new Een medewerker configureren voor het planningsproces | features/administration/employee-overview.md | #overzicht-van-medewerkerinstellingen %}. Medewerkers aan wie geen eenheid is toegewezen, worden niet in de lijst weergegeven.      |
| _Account > Gebruikers_{:.breadcrumbs}                                 | Toegangsrechten van gebruikers beheren via {% link_new gebruikersrollen | getting-started/configure-user-roles.md | #nieuwe-gebruikersrollen-aanmaken %}, {% link_new vergrendelde gebruikers deblokkeren | getting-started/manage-user-accounts.md | #een-gebruiker-deblokkeren %}, {% link_new een nieuw wachtwoord instellen voor een gebruiker | getting-started/manage-user-accounts.md | #een-nieuw-gebruikerswachtwoord-instellen %} en {% link_new controleren voor welke gebruikers je wordt gefactureerd | getting-started/how-does-billing-work.md | #gefactureerde-en-niet-gefactureerde-gebruikers-bekijken %} en voor welke niet. Je kunt ook {% link_new gebruikers verwijderen | getting-started/manage-user-accounts.md | #een-gebruikersaccount-verwijderen %} zodat je niet langer voor deze gebruikers wordt gefactureerd. |
| **People**                                                           | {% link_new Een account voor een medewerker aanmaken | features/people/manage-people.md %} en adres- en contactinformatie beheren. |

Onder  _Plan > Configuratie > Medewerkers_{:.breadcrumbs} kunnen gebruikers zonder admin-toegang alleen medewerkers bekijken die zijn toegewezen aan de eenheden waarvoor ze toegangsrechten hebben. Medewerkers die niet aan een eenheid zijn toegewezen, worden niet weergegeven in de lijst, zelfs als de optie Alle is geselecteerd in de vervolgkeuzemenu's Eenheid en Groep. Alleen gebruikers met admin-toegang kunnen alle medewerkers bekijken.

Medewerkers en gebruikers worden gesynchroniseerd, dus je hoeft een medewerker maar een keer aan te maken. Je wordt ook maar een keer voor ze gefactureerd.

> Voor elke medewerker die je op een van de drie plaatsen aanmaakt, wordt je organisatie {% link_new gefactureerd | getting-started/how-does-billing-work.md %} totdat je ze {% link_new deactiveert of verwijdert | features/administration/deactivate-employees.md %}.

## Een medewerker aanmaken

Om een medewerker met de basisinstellingen aan te maken, vereist injixo dat je alle verplichte velden invult. Voordat je de medewerker kunt configureren voor het planningsproces, moet je eerst verschillende andere [medewerkerinstellingen](#overzicht-van-medewerkerinstellingen) [configureren](#medewerkerinstellingen-configureren).
Volg deze stappen om een medewerker met basisisntellingen aan te maken:

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}.
2. Klik in de actiebalk op het {% icon item-add %}.
3. Voer in de sectie **Algemeen** een uniek **personeelsnummer** in.
4. Voer in de sectie **Persoonlijke gegevens** de **Achternaam** van de medewerker in.
5. Voer in het veld **injixo Inloggen (E-mail)** het e-mailadres in dat de medewerker voor injixo gaat gebruiken. Er wordt automatisch een account voor injixo Me aangemaakt. 
6. {% link_new Stel een wachtwoord in | features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md %} voor de medewerker, zodat zij zich bij injixo kunnen aanmelden.<br>Dit kun je doen nadat je de basisconfiguratie voor de medewerker hebt afgerond.
7. Klik op _OK_{:.doc-button}.<br>Het systeem stelt de datum van toetreding automatisch in op de huidige dag. Je kunt dit later handmatig wijzigen in de sectie [Dienstverband](#overige-instellingen).

Als je een medewerker aanmaakt, maakt injixo automatisch een gebruiker met de rol Agent aan.

<!-- In injixo Enterprise on-premise, you need to set the correct join date for the employee in the Employment Period section manually. To automatically create a linked user in the Users section, you need to add a User name and a Password in the Employee section. The injixo Login (Email) field is called Email 1 here and is not mandatory. --->

## Medewerkerinstellingen configureren

Nadat je een medewerker met de vereiste basisinstellingen hebt aangemaakt, kun je de planningsgerelateerde instellingen configureren. Volg hiervoor de onderstaande stappen:

Vereiste: Je hebt {% link_new alle elementen die vereist zijn voor het plannen | getting-started/set-up-base-configuration.md | #vereiste-configuratie-items %} ingesteld.

1. Klik op een medewerker in de lijst.<br>
Je kunt de blauwe snelkoppelingen rechtsboven gebruiken om snel naar een sectie te navigeren.
2. Klik op het {% icon item-add %} in een sectie om een nieuwe instelling toe te voegen. Klik op het {% icon item-edit %} om een bestaande instelling te wijzigen.<br>Lees meer over de [individuele configuratie-opties](#overzicht-van-medewerkerinstellingen).
3. (Optioneel) In een aantal secties kun je {% link_new geldig vanaf- en geldig tot en met-datums | features/administration/set-a-validity-period.md %} instellen, die de geldigheidsperiode van een instelling beperken.
4. Klik op _OK_{:.doc-button} om je wijzigingen op te slaan.

## Overzicht van medewerkerinstellingen

In de volgende secties vind je meer informatie over verplichte en optionele planningsinstellingen voor de configuratie van je medewerkers.

### Verplichte planningsinstellingen

In de volgende lijst worden de verplichte configuratie-items weergegeven die je aan je medewerkers moet toewijzen om ze in te kunnen plannen. Klik op de links voor meer informatie over elk configuratie-item.

> Opmerking
>
> Toewijzingen met overlappende {% link_new geldigheidsperioden | features/administration/set-a-validity-period.md %} zijn niet toegestaan.
> Toewijzingen die in het verleden en in de toekomst liggen, worden standaard verborgen. Klik op het pictogram Alles weergeven {% icon assignment-history | icon-only %} om ze zichtbaar te maken.


- {% link_new Contracten | features/administration/create-contracts.md %}: In het vervolgkeuzemenu worden alle beschikbare contracten weergegeven. Selecteer het juiste contract voor je medewerker en wijs het toe.
- {% link_new Kwalificatieniveaus | features/administration/work-with-skills.md %}: Kwalificatieniveaus geven aan in welke mate een medewerker gekwalificeerd is om een bepaalde taak uit te voeren. Selecteer in het vervolgkeuzemenu een of meerdere kwalificatieniveaus.
- {% link_new Activiteiten | features/administration/activities.md %}: Activiteiten zijn de taken waar medewerkers aan kunnen werken op basis van hun kwalificaties. De sectie Activiteiten wordt automatisch ingevuld zodra er een kwalificatieniveau aan een medewerker wordt toegewezen. Voor activiteiten waar alle medewerkers aan kunnen werken, is geen kwalificatie vereist, bijvoorbeeld voor de vooraf ingestelde activiteiten Aanwezigheid en Vakantie.
- {% link_new Eenheden | features/administration/create-and-manage-planning-units.md %}: Eenheden groeperen medewerkers. Een medewerker kan aan meerdere eenheden worden toegewezen, maar heeft minimaal een eenheid met prioriteit 1 nodig. Andere eenheden kunnen worden toegewezen met een waarde tussen 1 en 100 voor elke medewerker, waarbij 1 de hoogste prioriteit is.

### Optionele planningsinstellingen

De volgende instellingen zijn niet verplicht, maar kunnen handig zijn bij het plannen. Klik op de links voor meer informatie over elk configuratie-item.

- {% link_new Beschikbaarheid | features/administration/availabilities.md %}: Configureer op welke dagen en op welke tijden een medewerker beschikbaar en kan worden ingepland. Als je wilt dat een medewerker op een vaste weekdag nooit wordt ingepland, stel de beschikbaarheid voor het betreffende {% link_new dagtype | features/administration/day-types.md %} dan in op één minuut. Om dezelfde beschikbaarheid voor meerdere medewerkers tegelijkertijd in te stellen, gebruik je dagmodellen van het type {% link_new Beschikbaarheidskader | features/administration/daymodels/daymodel-creation.md | #beschikbaarheidskader %} in Dienstenseries. Als een medewerker zonder beperkingen beschikbaar is, hoef je geen beschikbaarheid toe te voegen.

- {% link_new Dagmodellen | features/administration/daymodels/daymodel-creation.md %}: Standaard gebruikt injixo alle dagmodellen die aan de eenheid zijn toegewezen om planningen te maken voor je medewerkers. Als je persoonlijke dagmodellen aan een medewerker hebt toegewezen, dan maakt Planningsoptimalisatie alleen gebruik van specifieke dagmodellen voor de medewerker. Als je wilt dat injixo alleen medewerkers inplant aan wie persoonlijke dagmodellen zijn toegewezen, dan kun je planningsregel _2661_{:.id-label} _Exclusief aan medewerker toegekende dagmodellen_ inschakelen.

- {% link_new Dienstenseries | features/administration/shift-sequences.md %}: Dienstenseries bevatten dagmodellen of activiteiten met een herhalend weekpatroon. Als je dienstenseries wilt gebruiken om planningen voor je medewerkers aan te maken, dan moet je eerst een [dienstenserie aan een medewerker toewijzen](#een-dienstenserie-toewijzen). Je kunt er ook voor kiezen om meerdere dienstenseries aan een medewerker toe te wijzen, bijvoorbeeld als je een andere dienstenserie wilt gebruiken voor weekenden en weekdagen. 

- {% link_new Groepen | features/administration/selections.md %}: Groepen dienen als een filter dat je kunt gebruiken om een gefilterde groep medewerkers weer te geven in een overzicht of om een actie uit te voeren voor een specifieke groep medewerkers tegelijkertijd. Je kunt een of meerdere groepen aanmaken met het vervolgkeuzemenu Groepen. Voorbeelden van groepen: een groep medewerkers die altijd op dezelfde manier wordt ingepland, hetzelfde contract heeft, in dienstenseries werkt, naar het werk carpoolt of die op basis van hun voltijds contract als eerste wordt ingepland.

- {% link_new Planningsmodellen | features/administration/work-time-pattern-models.md %}: Gebruik planningsmodellen om de automatische planning te beperken tot een beperkt aantal beschikbare dagmodellen. Je kunt slechts één planningsmodel aan een medewerker toewijzen. Voer een referentiedatum in als begindatum voor een planningsmodel.

- Externe systemen: Wijs {% link_new medewerkers-ID's van externe systemen toe  | features/acd-integration/cloud/import-agent-status-data.md | #medewerker-ids-van-externe-systemen-aan-medewerkers-toewijzen-in-injixo %}. Deze zijn nodig om agentstatussen uit je ACD te importeren.

### Overige instellingen

In de volgende sectie vind je een overzicht van de overige instellingen in de medewerkerconfiguratie. De meeste van deze instellingen zijn niet relevant voor het planningsproces. Beweeg je muis over de instellingen in de UI voor meer informatie.

- Dienstverband: Als je [een medewerker met basisinstellingen aanmaakt](#een-medewerker-aanmaken), dan wordt de datum van indiensttreding automatisch ingesteld. Hier kun je de datum van indiensttreding wijzigen, en eventueel ook een datum van uittrede instellen.

- Persoonlijke gegevens: Voer de persoonlijke gegevens van je medewerker in, zoals adresgegevens, telefoonnummer en land.

- Personeelspasnummers: Voer het nummer van de personeelspas van je medewerker of van een andere persoonlijke ID-kaart in.

- Overige gegevens

Een aantal instellingen in de sectie Overige instellingen zijn relevant voor het planningsproces, maar anderen zijn dat niet. In de volgende tabel vind je een overzicht van de instellingen met uitleg.

| Instelling        | Relevant voor het planningsproces | Beschrijving                |
|----------------| ------------------------|----------------------------|
|Kleur       | Nee                      | Kies een kleur om de werknemer snel in de planning te kunnen vinden.  |
|Geboorteplaats en geboortedatum  |       Nee | Voeg de geboortedatum en -plaats van de werknemer toe.  |
|Planningspositie | Ja | Geeft de sorteervolgorde aan voor de functionaliteit {% link_new Sorteren op planningspositie | features/scheduling/shiftcenter/sort-and-filter-items.md | #sort-the-items-of-a-level %} in het Dienstrooster-Center. De standaardwaarde is 0\. In het Dienstrooster-Center worden ze van laag naar hoog weergegeven.  |
|Diensten toewijzen | Ja | Dit selectievakje is standaard aangevinkt en is vereist als je medewerkers automatisch wilt inplannen. Als je dit niet wilt, vink het selectievakje dan uit. Je kunt nog steeds handmatig diensten toewijzen en dienstenseries invoegen voor deze medewerker.  |

## Massa-update gebruiken

In injixo Advanced en Enterprise WFM kun je de funtionaliteit {% link_new massa-update | features/administration/mass-update.md %} om meerdere medewerkers tegelijkertijd te bewerken.

## Een dienstenserie toewijzen

Een dienstenserie bestaat uit een reeks dagmodellen of activiteiten die regelmatig worden herhaald. Lees hoe je {% link_new dienstenseries aanmaakt | features/administration/shift-sequences.md %} en hoe je deze in je planning invoegt.

Volg deze stappen om een dienstenserie toe te voegen.

1. Klik in de sectie **Dienstenseries** op het {% icon item-add %}.
2. Selecteer een dienstenserie.
3. Selecteer in het vervolgkeuzemenu bij Medewerker de rij van de {% link_new dienstenserie | features/administration/shift-sequences.md %} die van toepassing is op de medewerker.
4. Specificeer de volgorde.<br>Deze instelling is alleen relevant als je meer dan één dienstenserie aan een medewerker wilt toewijzen. Dienstenseries met lagere waarden worden als eerste ingevoerd en kunnen door volgende dienstenseries worden overschreven.
5. Stel een Referentiedatum in voor de dag waarop de dienstenserie begint.
6. Klik op _OK_{:.doc-button}.
Je kunt nu {% link_new dienstenseries toevoegen | features/scheduling/schedules/schedules-insert-shift-sequences.md %} aan de planning.

## Medewerkers overplaatsen

Als je medewerkers regelmatig voor een bepaalde tijd in andere eenheden werkzaam zijn, dan kun je de fuctionaliteit Medewerkers overplaatsen gebruiken om medewerkers tijdelijk aan een andere eenheid toe te wijzen.

Tijdens de delegatieperiode krijgt de nieuwe eenheid automatisch prioriteit bij het plannen. Na afloop van de ingestelde periode wordt de medewerker automatisch weer in zijn oorspronkelijke eenheid ingepland. De functionaliteit Medewerkers overplaatsen is sneller dan het handmatig opnieuw toewijzen van de eenheid.

Volg deze stappen om een medewerker over te plaatsen.

1. Selecteer een medewerker.
2. Ga naar de sectie **Eenheden**.
3. Klik in de kop van de sectie op het pictogram Medewerker overplaatsen {% icon delegate-employees | icon-only %}.
4. Selecteer de eenheid waaraan de medewerker is toegewezen.
5. Voer een begin- en einddatum toe voor de delegatieperiode.
6. Klik op _OK_{:.doc-button}.

> Opmerking
>
> Een medewerker die aan meerdere eenheden tegelijkertijd is toegewezen, wordt altijd vanuit de eenheid met de hoogste prioriteit gedelegeerd.
