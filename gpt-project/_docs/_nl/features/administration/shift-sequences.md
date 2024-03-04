---
title: Dienstenseries aanmaken
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Dienstenseries gebruiken om zich herhalende planningen aan te maken.
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Dagmodellen aanmaken
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Dienstenseries toevoegen
    filepath: features/scheduling/schedules/schedules-insert-shift-sequences.md
---

Een dienstenserie is een weekpatroon van verschillende dagmodellen of activiteiten. Met dienstenseries kun je deze zich herhalende patronen snel aan je planning toevoegen. Laat de optimalisering van de resterende planning aan injixo over.

Dienstenseries besparen je uren werk, want je hoeft patronen die zich steeds herhalen niet meer handmatig aan je planning toe te voegen.

Er zijn vier usecases voor het gebruik van dienstenseries:

- Usecase 1: Je wilt dagen aangeven waarop bepaalde diensten moeten worden ingepland
- Usecase 2: Je wilt activiteiten inplannen die vaker worden herhaald
- Usecase 3: Je wilt aangeven op welke dagen medewerkers niet werken
- Usecase 4: Je wilt aangeven wanneer diensten kunnen worden ingepland op basis van de beschikbaarheid van medewerkers

Dienstenseries bestaan uit een of meerdere regels. Elke regel bevat een afzonderlijk patroon dat aan de planning kan worden toegevoegd.<br>
Elke regel bevat cellen die de dagen van de week aangeven. In deze cellen voer je de dagmodellen of activiteiten in die je met de dienstenserie wilt inplannen.<br>
Elke regel staat voor een weekpatroon voor je planning. Daarom moet het aantal cellen op een regel deelbaar zijn door zeven. Een dienstenserie kan maximaal 53 rijen bevatten, omdat de maximale lengte van een dienstenserie één jaar is.

## Vereisten

Om dienstenseries aan te maken, moet je eerst {% link_new activiteiten | features/administration/activities.md %} of {% link_new dagmodellen | features/administration/daymodels/daymodel-creation.md %} aanmaken.<br>
Nadat je dienstenseries hebt aangemaakt, moet je ze {% link_new toewijzen aan je medewerkers | features/administration/employee-overview.md | #een-dienstenserie-toewijzen %} voordat je ze aan de planning kunt toevoegen.

>Opmerking
>
>De werkweek begint standaard op maandag.
>
>Je kunt de dag waarop de week begint wijzigen met de instelling _48420_{:.id-label} _Weekbegin (planning)_.

## Dienstenseries aanmaken

Voordat je je eerste dienstenserie aanmaakt, moet je bepalen hoeveel dienstenseries, regels en aantal cellen op een regel je nodig hebt. Dit is geheel afhankelijk van de behoeften van je bedrijf, bijvoorbeeld van het aantal verschillende diensten dat je inplant, of je vergaderingen instelt die telkens terugkomen, etc.

Om dienstenseries aan te maken, ga je naar _Plan > Configuratie > Dienstenseries_{:.breadcrumbs} en volg je deze stappen:

1. Klik op het pictogram Nieuw {% icon item-add | icon-only %} in de linker bovenhoek.
2. Configureer de gegevens van de dienstenserie:<br>
  **Naam**: Voer een unieke naam in (max. 50 tekens).<br>
  **Afkorting**: Voer de naam in of een kortere versie hiervan (max. 25 tekens).<br>
  **Medewerkersregel(s)**: Voer het aantal regels in voor de dienstenserie (max. 53).<br>Aan elke rij wordt een nummer toegewezen. Dubbelklik op een rij om deze een andere naam te geven. Je hebt het rijnummer of de naam nodig om deze alter aan een medewerker toe te wijzen.<br>
  **Lengte**: Voer een waarde in tussen 7 en 371 dagen. De lengte moet deelbaar zijn door zeven.
6. Klik op _OK_{:.doc-button}.

>Opmerking
>
>De lengte van een dienstenserie moet altijd deelbaar zijn door zeven, zelfs als je bedrijf maar vijf of zes dagen per week geopend is. Dienstenseries worden automatisch herhaald. Bij een dienstenserie van 5 dagen zou de maandagdienst in een zaterdagcel terechtkomen, de dinsdagdienst in een zondagcel, etc.
>
>Als je van plan bent om patronen met verschillende lengtes in te plannen (bijvoorbeeld een voor wekelijkse vergaderingen en een voor tweewekelijkse vergaderingen), dan moet je hiervoor verschillende dienstenseries aanmaken.

Nadat je een dienstenserie hebt aangemaakt, kun je de {% link_new geldigheidsperioden | features/administration/set-a-validity-period.md %} voor deze dienstenseries instellen:

1. Klik op {% icon item-edit %} boven de tabel.
2. Selecteer de datums in de velden **geldig vanaf** en **geldig tot en met**.
3. Klik op _OK_{:.doc-button}.

### Dagmodellen toevoegen

1. Selecteer in het vervolgkeuzemenu links in de **Opties**-tegel **Dagmodel toevoegen**.
2. Selecteer in het vervolgkeuzemenu **Dagmodel** het dagmodel dat je wilt toevoegen.
3. Voer een **Aantal** in. Dit is het aantal opeenvolgende dagen waarop je het dagmodel toevoegt.
4. Klik op de eerste cel in de tabel waarin je het dagmodel wilt toevoegen.<br>
  Als je een aantal hebt ingevoerd dat hoger is dan een, dan wordt het dagmodel toegevoegd in die cel en in het aantal cellen rechts daarvan dat nodig is om dat nummer te bereiken.

De dienstenserie wordt automatisch opgeslagen.

> Tip
>
> Gebruik activiteiten of vaste dagmodellen. Als je variabele dagmodellen aan een dienstenserie toevoegt, dan begint de dienst altijd op het vroegst mogelijke tijdstip.

### Activiteiten toevoegen

1. Selecteer in het vervolgkeuzemenu links in de **Opties**-tegel **Activiteit toevoegen**.
2. Selecteer in het vervolgkeuzemenu **Activiteit** de activiteit die je wilt toevoegen.
3. Voer een **Aantal** in. Dit is het aantal opeenvolgende dagen waarop je de activiteit toevoegt.
4. Om de tijd in te stellen waarop de activiteit is gepland, voer je in de velden **vanaf** en **tot en met** een tijdsperiode (in 24-uurformaat) in, of vink je het selectievakje **Over de hele dag** aan.
5. Klik op de eerste cel in de tabel waarin je de activiteit wilt toevoegen.<br>
  Als je een aantal hebt ingevoerd dat hoger is dan een, dan wordt de activiteit toegevoegd in die cel en in het aantal cellen rechts daarvan dat nodig is om dat nummer te bereiken.

> Activiteiten die na middernacht eindigen
>
> Als je activiteiten wilt invoeren die na middernacht eindigen, tel dan 24 bij de eindtijd op. Bijvoorbeeld: als de activiteit op maandag om 1:00 uur 's nachts (dus op de volgende dag) eindigt, dan voer je 25:00 in.

## Dienstenseries bewerken

1. Selecteer in de **Dienstenserie**-tegel een dienstenserie in het vervolgkeuzemenu.
2. Klik op _Gebruiken_{:.doc-button}.
3. Klik op het pictogram Bewerken {% icon item-edit | icon-only %}. in de actiebalk bovenaan om de naam, de afkorting, het aantal medewerkersegels of de lengte aan te passen.<br>Klik op _OK_{:.doc-button} zodra je klaar bent met bewerken.
4. Klik op het pictogram Bewerken {% icon item-edit | icon-only %}. in de actiebalk boven de tabel om de geldigheidsperiodes te bewerken.<br>Klik op _OK_{:.doc-button} zodra je klaar bent met bewerken.

### Elementen uit een dienstenserie verwijderen

Volg deze stappen om een of meerdere elementen uit de dienstenserie te verwijderen:
1. Selecteer in de **Dienstenserie**-tegel een dienstenserie in het vervolgkeuzemenu.
2. Klik op _Gebruiken_{:.doc-button}.
3. Selecteer in de **Opties**-tegel **Verwijderen** in het vervolgkeuzemenu.
4. Klik op de cellen met elementen die je wilt verwijderen.<br>
  De elementen worden automatisch verwijderd.

Volg deze stappen om alle elementen uit een dienstenserie te verwijderen:

1. Selecteer in de **Dienstenserie**-tegel een dienstenserie in het vervolgkeuzemenu.
2. Klik op _Gebruiken_{:.doc-button}.
3. Vink in de **Opties**-tegel het selectievakje **Alles verwijderen** aan en klik op _Gebruiken_{:.doc-button}.

De elementen worden automatisch verwijderd.

## Een dienstenserie verwijderen

1. Selecteer in de **Dienstenserie**-tegel een dienstenserie in het vervolgkeuzemenu.
2. Klik op _Gebruiken_{:.doc-button}.
3. Klik op het pictogram Verwijderen {% icon item-delete | icon-only %}. in de actiebalk bovenaan.
4. Klik op _Ja_{:.doc-button} in het bevestigingsvenster.

## Usecases

Je kunt dienstenseries voor verschillende scenario's gebruiken.

### Usecase 1: Je wilt dagen aangeven waarop bepaalde diensten moeten worden ingepland.

Deze usecase gebruik je bijvoorbeeld als je vroege en late diensten moet inplannen voor verschillende groepen medewerkers. Of als een van je medewerkers op maandagen niet voor 11:00 uur kan beginnen, maar op andere weekdagen wel vroeger beschikbaar is. 
 
Bekijk onze Academy-instructievideo hieronder om te zien of deze usecase op jou van toepassing is en hoe je je dienstenseries dan instelt:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls> 
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-1.mp4" type="video/mp4">
   Je browser ondersteunt de videotag niet. Je kunt de <a href="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-1.mp4">video downloaden</a> en offline bekijken.
   </video>
</div>
<br>

### Usecase 2: Je wilt activiteiten inplannen die vaker worden herhaald

Deze usecase is bijvoorbeeld van toepassing als je vergaderingen moet inplannen die elke week plaatsvinden, of als je een medewerker elke week op een bepaalde tijd wilt inplannen om een uur backoffice-taken uit te voeren.

Bekijk onze Academy-instructievideo hieronder om te zien of deze usecase op jou van toepassing is en hoe je je dienstenseries dan instelt:

<div class="inline-video-container">
  <video class="inline-video-player-v" controls>
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-2.mp4" type="video/mp4">
  </video>
</div>
<br>

### Usecase 3: Je wilt aangeven op welke dagen medewerkers niet werken

Deze usecase is van toepassing als je bijvoorbeeld bepaalde dagpatronen voor vrije dagen voor individuele medewerkers moet inplannen. 

Bekijk onze Academy-instructievideo hieronder om te zien of deze usecase op jou van toepassing is en hoe je dienstenseries dan configureert: 

  <div class="inline-video-container">
    <video class="inline-video-player-v" controls> 
     <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-3.mp4" type="video/mp4">
    </video>
  </div>
<br>

### Usecase 4: Je wilt aangeven wanneer diensten kunnen worden ingepland op basis van de beschikbaarheid van medewerkers

Deze usecase is van toepassing als je medewerkers met een wisselende beschikbaarheid wilt inplannen.

Bekijk onze Academy-instructievideo hieronder om te zien of deze usecase op jou van toepassing is en hoe je dienstenseries dan configureert: 

<div class="inline-video-container">
  <video class="inline-video-player-v" controls>
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-4.mp4" type="video/mp4">
  </video>
</div>
<br>

## Een rapport genereren

Je kunt een rapport in PDF-formaat genereren met alle gegevens van een dienstenserie. Ga als volgt te werk om het rapport te genereren:

1. Selecteer in de **Dienstenseries**-tegel aan de rechterkant de dienstenserie waarvoor je een rapport wilt genereren.
2. Klik op _Gebruiken_{:.doc-button}.
3. Klik op _Rapport_{:.doc-button} boven de tabel.
4. In het dialoogvenster kun je het selectievakje aanvinken om het rapport naar het e-mailadres te verzenden dat voor je injixo-account wordt gebruikt.

In het rapport worden de begin- en eindtijden van de activiteiten of dagmodellen weergegeven die in de dienstenserie zijn opgenomen, samen met de nettoduur in uren. Het rapport is ingedeeld in weken.
Daarnaast vind je in het rapport de volgende totalen en gemiddelden van de nettoduur:

- Rij Totaal: Netto duur van alle activiteiten of dagmodellen in de dienstenserie
- Kolom Som: Totaal van de nettoduur van de activiteiten of dagmodellen per week
- Rij Gemiddelde: Gemiddelde waarde voor alle waarden in de kolom Totaal
