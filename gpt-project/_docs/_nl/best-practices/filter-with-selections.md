---
title: Filteren met groepen
description: Lees hoe je groepen als een filter kunt gebruiken.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: true
---

Heb je nog weinig ervaring met groepen? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/administration/selections.md %}.

Om je team te beheren, moet je medewerkers vaak groeperen op basis van werkomstandigheden. Denk bijvoorbeeld aan medewerkers die rekening moeten houden met kinderopvang of medewerkers die aan een bepaalde leidinggevende rapporteren. Je kunt groepen aanmaken om je eigen groeperingscriteria te definiëren. Dit kan handig zijn als je groeperingsopties nodig hebt die verder gaan dan {% link_new eenheden | features/administration/create-and-manage-planning-units.md %} en {% link_new medewerkersfilters | features/administration/employee-filter.md %}.

Eenheden helpen je om medewerkers te groeperen op basis van je bedrijfsstructuur, bijvoorbeeld door medewerkers in verschillende tijdzones aan verschillende eenheden toe te wijzen, en medewerkersfilters te gebruiken die met configuratie-elementen werken, zoals contracten en activiteiten. Groepen helpen je om medewerkers te groeperen om aan de specifieke behoeften van je bedrijf te voldoen.

Je kunt een groep aanmaken om filters binnen een eenheid te verfijnen om medewerkers in meerdere eenheden te beheren. Zo kun je een groep aanmaken voor medewerkers die afhankelijk zijn van kinderopvang, zodat hun planningen afzonderlijk worden beheerd. Ook kun je de planningen van medewerkers in verschillende eenheden filteren voor een marketingcampagne in verschillende tijdzones.

## Gebruik groepen om medewerkers binnen eenheden te filteren.

injixo beschikt over filters voor eenheden en groepen in **Plan** en **Intraday**. Nadat je een eenheid hebt geselecteerd, kun je daarnaast medewerkers filteren op basis van groep.

Zo heb je drie eenheden en een van de eenheden bevat medewerkers die deelnemen aan een trainingsprogramma. Je kunt groepen gebruiken om ze te groeperen en hun planningen afzonderlijk te beheren, bijvoorbeeld om specifieke vergaderingen in te plannen.

## Gebruik groepen om medewerkers te beheren die in verschillende eenheden zijn ingedeeld.

In injixo zijn er drie manieren om groepen te gebruiken om medewerkers in verschillende eenheden te filteren. Onder deze sectie vind je een paar voorbeelden van filteropties met groepen.

De volgende tabel biedt een overzicht van de drie verschillende opties om over verschillende eenheden op groep te filteren. Je vindt deze opties in injixo-componenten of functionaliteiten.

| Component/functionaliteit | Filteroptie |
|-------------------------|----------------------------|
| Schedules               | Alle eenheden en een groep. |
| Vakantie/Afwezigheid                | Alle eenheden en een groep. |
| Real-Time Adherence     | Een selectie en geen eenheden. |
| Intraday Adherence      | Een selectie en geen eenheden. |
| Dienstrooster-Center            | Een groep (geen filter voor eenheden beschikbaar). |
| Medewerkers inlichten           | Een eenheid en een groep. Herhaal het filteren voor alle eenheden die je wilt filteren. |
| Planningsperioden  | Een eenheid en een groep. Herhaal het filteren voor alle eenheden die je wilt filteren. |
| Meetings                | Een eenheid en een groep. Herhaal het filteren voor alle eenheden die je wilt filteren. |
| Verlofperiodes        | Een eenheid en een groep. Herhaal het filteren voor alle eenheden die je wilt filteren. |
| Vakantierecht    | Een eenheid en een groep. Herhaal het filteren voor alle eenheden die je wilt filteren. |

Voor alle functionaliteiten onder _Plan > Schedules > Planningsacties_{:.breadcrumbs} moet je een eenheid en een groep selecteren. Vervolgens pas je de planningsactie toe op elke eenheid die je wilt filteren.

De volgende voorbeelden bevatten meer informatie over de drie filteropties voor groepen, zoals beschreven in de bovenstaande tabel.

## Voorbeelden

De onderstaande voorbeelden maken gebruik van een groep met de naam Onboarding. De Onboarding-groep is bedoeld om medewerkers te groeperen die zich binnen je bedrijf in de onboardingfase bevinden, ongeacht hun eenheid. Door de Onboarding-groep te gebruiken, kun je eenvoudiger hun planningen beheren en zien wat ze nodig hebben.

Met de volgende configuratie kun je de Onboarding-groep als filter gebruiken om medewerkers uit verschillende eenheden te filteren:

1. {% link_new Maak een sectie aan met de naam Onboarding en configureer hem | features/administration/selections.md | #groepen-aanmaken %}.
2. {% link_new Wijs de medewerkers | features/administration/selections.md | #medewerkers-aan-groepen-toewijzen %} die zich in de onboardingfase bevinden toe aan de Onboarding-groep.

### Filteroptie 1: Alle eenheden en een groep

In _Plan > Schedules_{:.breadcrumbs} kun je de planningen van medewerkers in de Onboarding-groep filteren met de volgende vervolgkeuzemenu's:

- **Eenheid**: Selecteer **Alle eenheden**.
- **Kies groep**: Selecteer **Onboarding**.  
   Als het vervolgkeuzemenu **Kies groep** niet wordt weergegeven, klik dan op het pictogram Groepenfilter {% icon selection-filter-u | icon-only %} linksboven.

### Filteroptie 2: Een groep en geen eenheid

In _Intraday > Real-Time Adherence_{:.breadcrumbs} kun je de ingeplande activiteiten van medewerkers in de Onboarding-groep filteren en realtime vergelijken met de werkelijke status van een medewerker. Dit is bijvoorbeeld handig om te controleren of medewerker de activiteiten uitvoeren die voor hun onboardingfase ingepland zijn.

Om op groep te filteren, kun je de volgende vervolgkeuzemenu's gebruiken:

- **Eenheid**: Zorg ervoor dat er geen eenheid is geselecteerd.
- **Groep**: Selecteer **Onboarding**.

### Filteroptie 3: Een groep en een eenheid

Als je speciale verlofvoorwaarden hebt voor medewerkers in de onboardingfase, dan kun je specifieke verlofperioden voor de Onboarding-groep instellen. Stel dat je de volgende eenheden hebt voor drie verschillende kantoren: Kantoor 1, Kantoor 2 en Kantoor 3. Deze drie kantoren hebben medewerkers in de onboardingfase die zijn toegewezen aan de Onboarding-selectie.

Ga als volgt te werk om specifieke verlofperiodes aan te maken voor de Onboarding-groep:

1. Klik in _Plan > Vakantie/Afwezigheid_{:.breadcrumbs} op _Verlofperiodes_{:.doc-button}.  
   Je komt nu op de pagina **Verlofperiodes** terecht.
2. Klik op _Verlofperiode aanmaken_{:.doc-button}.  
   Er wordt een dialoogvenster geopend.
3. Gebruik de vervolgkeuzemenu's om op groep te filteren:  
   - **Eenheid**: Selecteer **Kantoor 1**.
   - **Groep**: Selecteer **Onboarding**.
4. Vul de overige velden in.  
   Lees meer over de configuratie van {% link_new verlofperiodes | features/scheduling/time-off/time-off-periods.md %}.
5. Klik op _Opslaan_{:.doc-button}.
6. Herhaal de stappen 1 tot 5 voor de eenheden Kantoor 2 en Kantoor 3.
