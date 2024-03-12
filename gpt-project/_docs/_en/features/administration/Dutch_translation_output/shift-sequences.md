---
title: dienstenseries aanmaken <!-- GPT translation -->
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Gebruik dienstenseries om zich herhalende planningen aan te maken. <!-- GPT translation -->
redirect_from:
  - /shift-sequence-overview/
redirect_reason: filename used in old product onboarding
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-insert-shift-sequences.md
---

Een dienstenserie is een weekpatroon met dagmodellen of activiteiten. Met dienstenseries kun je deze herhalende patronen snel in je planning toevoegen, en injixo de rest van de planning laten optimaliseren. <!-- GPT translation -->

Dankzij dienstenseries bespaar je talloze uren werk die anders zouden gaan zitten in het handmatig inplannen van herhalende patronen. <!-- GPT translation -->

Dienstenseries kunnen in de volgende vier gevallen van pas komen: <!-- GPT translation -->

- Usecase 1: Geef dagen aan waarop bepaalde diensten ingepland moeten worden <!-- GPT translation -->
- Usecase 2: Het inplannen van terugkerende activiteiten <!-- GPT translation -->
- Usecase 3: Aangeven op welke dagen medewerkers niet werken. <!-- GPT translation -->
- Usecase 4: Aangeven wanneer diensten op basis van de beschikbaarheden van medewerkers kunnen worden ingepland <!-- GPT translation -->

>Demo-jobnoad: De rijen {1, 2} worden met verschillende grijstinten weergegeven. In de volgende stanimatievormen wordt dit als voorbeeld gebruikt. <!-- GPT translation -->
Elke rij bevat cellen die weekdagen vertegenwoordigen. Voer dagmodellen, activiteiten of diensten in deze cellen in om te plannen met de dienstenserie. <!-- GPT translation -->
Elke rij staat voor een weekpatroon in je planning. Daarom moet het aantal cellen in een rij een meervoud van zeven zijn. Een dienstenserie kan maximaal 53 rijen krijgen, omdat deze nooit langer kan zijn dan een jaar. <!-- GPT translation -->

## Vereisten <!-- TM 100 -->

Om dienstreeksen aan te maken, dien je eerst {% link_new activiteiten | features/administration/activities.md %} of {% link_new dagmodellen | features/administration/daymodels/daymodel-creation.md %} aan te maken.<br> <!-- GPT translation -->
Nadat je dienstenseries hebt aangemaakt, moet je deze eerst {% link_new toewijzen aan je medewerkers | features/administration/employee-overview.md | #een-dienstenserie-toewijzen %} voordat je ze in je planning kunt toevoegen.<br> <!-- GPT translation -->
Wanneer je een dienstenserie toewijst aan een medewerker, moet je een referentiedatum instellen. De referentiedatum is de eerste dag waarop de dienstenserie wordt ingepland. Vanaf de datum herhaalt de dienstenserie zich zonder onderbreking zo lang hij geldig is.<br> <!-- GPT translation -->
Omdat je dienstenseries configureert als weekpatronen, stel je de referentiedatum in op een maandag, of op de weekdag waarop jouw werkweek begint. <!-- GPT translation -->

>Note
>
>By default, the working week starts on Monday.
>
>You can change the first day of the week with the setting _48420_{:.id-label} _First day of the scheduling week_.

## Dienstenseries aanmaken <!-- GPT translation -->

Voordat je begint met het aanmaken van dienstenseries, is het belangrijk om te bepalen hoeveel series je nodig hebt en hoeveel rijen en cellen deze elke serie moet hebben. Het aantal dienstenseries hangt uitsluitend van de behoeften van je bedrijf af, denk bijvoorbeeld aan het aantal verschillende diensten dat je wilt inplannen, of je regelmatig terugkerende afspraken inplant, enz. <!-- GPT translation -->

Ga naar _Plan > Configuratie > Dienstenseries_{:.breadcrumbs} en volg deze stappen om dienstenseries aan te maken: <!-- GPT translation -->

1. Klik op het pictogram **Nieuw** {% icon item-add | icon-only %} linksboven. <!-- GPT translation -->
2. Stel de volgende sequentie-instellingen in:<br> <!-- GPT translation -->
  **Naam**: Voer een unieke naam in (max. 50 tekens).<br> <!-- GPT translation -->
  **Afkorting**: Voer de naam of een kortere versie ervan in (50 tekens).<br> <!-- GPT translation -->
  **Medewerkerrij(en)**: Voer het aantal rijen in voor de dienstenserie (max. 53).<br>Aan elke rij wordt een nummer toegewezen. Dubbelklik op een rij om deze een andere naam te geven. Je hebt het nummer of de naam van een rij later nodig om deze aan een medewerker toe te wijzen.<br> <!-- GPT translation -->
  **Tijdsduur**: Voer een waarde in tussen 7 en 371 dagen. De tijdsduur moet een meervoud van zeven zijn. <!-- GPT translation -->
6. Klik op _OK_{:.doc-button}. <!-- GPT translation -->

>Note
>
>The duration of a shift sequence must always be a multiple of seven, even if your organization only opens five or six days a week. Shift sequences repeat automatically. A shift sequence of 5 days would insert the Monday shift in a Saturday cell, the Tuesday shift in a Sunday cell, etc.
>
>If you want to plan patterns with different durations (e.g. one for weekly meetings, and one for biweekly meetings), you need to create separate shift sequences.

Als je een dienstenserie hebt aangemaakt, dan kun je {% link_new geldigheidsperiodes | features/administration/set-a-validity-period.md %} voor deze serie instellen. <!-- GPT translation -->

1. Klik op het pictogram Bewerken {% icon item-edit | icon-only %} boven de tabel. <!-- GPT translation -->
2. Voer in de velden **Geldig vanaf** en **Geldig tot en met** de datums in. <!-- GPT translation -->
3. Klik op _OK_{:.doc-button}. <!-- TM 100 -->

### Dagmodellen toevoegen <!-- GPT translation -->

1. Selecteer in de sectie **Opties** in het vervolgkeuzemenu aan de linkerkant de optie **Dagmodel toevoegen**. <!-- GPT translation -->
2. Selecteer het dagmodel dat je wilt toevoegen in het vervolgkeuzemenu **Dagmodel**. <!-- GPT translation -->
3. Voer een **nummer** in. Dit is het aantal opeenvolgende dagen waarin je het dagmodel wilt invoeren. <!-- GPT translation -->
4. Klik in de tabel op de eerste cel waarin je het dagmodel wilt toevoegen. <!-- GPT translation -->
  Als je een nummer hoger dan één hebt ingevoerd, dan wordt het dagmodel in die cel toegevoegd en in het aantal daaropvolgende cellen rechts dat nodig is om dit aantal te bereiken. <!-- GPT translation -->

De dienstenserie wordt automatisch opgeslagen. <!-- GPT translation -->

> Tip
>
> Use activities or fixed day models. If you insert variable day models in a shift sequence, the shift will always start at the earliest possible time.

### Activiteiten toevoegen <!-- GPT translation -->

1. Selecteer in de sectie **Instellingen** de optie **Activiteit toevoegen** in het vervolgkeuzemenu links. <!-- GPT translation -->
2. Selecteer de activiteit die je wilt toevoegen in het vervolgkeuzemenu **Activiteit**. <!-- GPT translation -->
3. Voer een **aantal** in. Dit is het aantal opeenvolgende dagen waarop je de activiteit toevoegt. <!-- GPT translation -->
4. Voer om aan te geven wanneer de activiteit is gepland een tijdsmarge in (in 24-uursformaat) in de velden **vanaf** en **tot** in, of vink het selectievakje **Hele dag** aan. <!-- GPT translation -->
5. Klik in de tabel op de eerste cel waarin je de activiteit wilt toevoegen.<br> <!-- GPT translation -->
  Als je een getal hoger dan 1 hebt ingevoerd, dan wordt de activiteit in dat cel ingevoegd en in zoveel cellen naar rechts als nodig is om dat getal te bereiken. <!-- GPT translation -->

> Activities that end after midnight
>
> If you want to insert activities that end past midnight, add 24 to the end time, i.e. if the activity should end at 1 AM on the next day, enter 25:00.

## Dienstenseries bewerken <!-- GPT translation -->

1. In de sectie **Dienstenseries** selecteer je een dienstenserie in het vervolgkeuzemenu. <!-- GPT translation -->
2. Klik op **Toepassen**{:.doc-button}. <!-- GPT translation -->
3. Klik op het pictogram Bewerken {% icon item-edit | icon-only %} in de actiebalk bovenaan om de naam, afkorting, aantal rijen of de duur van het tijdvenster te bewerken.<br>Klik na het bewerken op _OK_{:.doc-button}. <!-- GPT translation -->
4. Klik op het pictogram Item bewerken in de actiebalk boven de tabel om de geldigheidsperiodes aan te passen.<br>Klik op _OK_{:.doc-button} als je klaar bent met bewerken. <!-- GPT translation -->

### Elementen uit een dienstenserie verwijderen <!-- GPT translation -->

Volg deze stappen om een of meerdere elementen van de dienstenserie te verwijderen: <!-- GPT translation -->
1. In de sectie **Dienstenseries** selecteer je een dienstenserie in het vervolgkeuzemenu. <!-- Repetition of GPT translation -->
2. Klik op **Toepassen**{:.doc-button}. <!-- Repetition of GPT translation -->
3. Selecteer in de sectie **Opties** de optie **Verwijderen** in het vervolgkeuzemenu. <!-- GPT translation -->
4. Klik op de cellen waarvan je de elementen wilt verwijderen. <!-- GPT translation -->
  De elementen worden automatisch verwijderd. <!-- GPT translation -->

Volg deze stappen om alle elementen in een dienstenserie te verwijderen: <!-- GPT translation -->

1. In de sectie **Dienstenseries** selecteer je een dienstenserie in het vervolgkeuzemenu. <!-- Repetition of GPT translation -->
2. Klik op **Toepassen**{:.doc-button}. <!-- Repetition of GPT translation -->
3. Selecteer in de sectie **Opties** de optie **Verwijderen** in het vervolgkeuzemenu. <!-- Repetition of GPT translation -->
4. Vink het selectievakje **Alles verwijderen** aan en klik op _Toepassen_{:.doc-button}.<br> <!-- GPT translation -->
  De elementen worden automatisch verwijderd. <!-- Repetition of GPT translation -->

## Een dienstenserie verwijderen <!-- GPT translation -->

1. In de sectie **Dienstenseries** selecteer je een dienstenserie in het vervolgkeuzemenu. <!-- Repetition of GPT translation -->
2. Klik op **Toepassen**{:.doc-button}. <!-- Repetition of GPT translation -->
3. Klik op het pictogram Verwijderen (prullenbak) in de bovenste actiebalk. <!-- GPT translation -->
4. Klik in het bevestigingsvenster op _Ja_{:.doc-button}. <!-- GPT translation -->

## Usecases <!-- TM 100 -->

Je kunt dienstenseries voor uiteenlopende scenario's gebruiken. <!-- GPT translation -->

### Usecase 1: Specificeer dagen waarop bepaalde diensten moeten worden ingepland <!-- GPT translation -->

Deze usecase is bijvoorbeeld van toepassing als je vroege en late diensten moet plannen voor verschillende groepen mensen. Of als een teamlid pas om 11:00 uur aan het werk kan op maandagen, terwijl hij op alle andere weekdagen eerder beschikbaar is. <!-- GPT translation -->

Je kunt meer te weten komen of deze usecase op jou van toepassing is en hoe je dienstenseries dienstenseries configureert in de volgende Academy-training: <!-- GPT translation -->

<div class="inline-video-container"> <!-- GPT translation -->
  <video class="inline-video-player-v" controls>  <!-- GPT translation -->
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-1.mp4" type="video/mp4"> <!-- GPT translation -->
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-1.vtt" kind="subtitles" srclang="en" label="Engels" default> <!-- GPT translation -->
   </video> <!-- GPT translation -->
</div> <!-- TM 100 -->
<br> <!-- GPT translation -->

### Usecase 2: Het plannen van terugkerende activiteiten <!-- GPT translation -->

Deze use-case is van toepassing wanneer je bijvoorbeeld bijeenkomsten die elke week plaatsvinden moet plannen, of wanneer je een medewerker dagelijkse back-office-werk voor perioden van een uur moet inplannen op een vast tijdstip. <!-- GPT translation -->

Je kunt meer te weten komen of deze usecase op jou van toepassing is en hoe je dienstenseries dienstenseries configureert in de volgende Academy-training: <!-- Repetition of GPT translation -->

<div class="inline-video-container"> <!-- Repetition of GPT translation -->
  <video class="inline-video-player-v" controls> <!-- GPT translation -->
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-2.mp4" type="video/mp4"> <!-- GPT translation -->
        <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-2.vtt" kind="subtitles" srclang="en" label="Engels" default> <!-- GPT translation -->
  </video> <!-- GPT translation -->
</div> <!-- TM 100 -->
<br> <!-- Repetition of GPT translation -->

### Usecase 3: Dagen instellen waarop werknemers niet werken <!-- GPT translation -->

Deze usecase geldt bijvoorbeeld als je specifieke patronen nodig hebt om de vrije dagen van individuele teamleden vast te leggen. <!-- GPT translation -->

Meer informatie over of dit usecase op jou van toepassing is en over het configureren van dienstenseries vind je in onze academy-training: <!-- GPT translation -->

  <div class="inline-video-container"> <!-- GPT translation -->
    <video class="inline-video-player-v" controls> <!-- GPT translation -->
  <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-3.mp4" type="video/mp4"> <!-- GPT translation -->
      <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-3.vtt" kind="subtitles" srclang="en" label="English" default> <!-- GPT translation -->
    </video> <!-- GPT translation -->
  </div> <!-- GPT translation -->
<br> <!-- Repetition of GPT translation -->

### Usecase 4: Aangeven wanneer diensten buit mensen beschikbaarheden kunnen worden ingepland <!-- GPT translation -->

Deze usecase is van toepassing als je medewerkers wilt inplannen die verschillende beschikbaarheden hebben. <!-- GPT translation -->

Meer informatie over of dit usecase op jou van toepassing is en over het configureren van dienstenseries vind je in onze academy-training: <!-- Repetition of GPT translation -->

<div class="inline-video-container"> <!-- Repetition of GPT translation -->
  <video class="inline-video-player-v" controls> <!-- Repetition of GPT translation -->
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-4.mp4" type="video/mp4"> <!-- GPT translation -->
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-4.vtt" kind="subtitles" srclang="en" label="Engels" default> <!-- GPT translation -->
  </video> <!-- Repetition of GPT translation -->
</div> <!-- TM 100 -->
<br> <!-- Repetition of GPT translation -->

## Een rapport genereren <!-- GPT translation -->

Je kunt een rapport in PDF-formaat genereren met alle gegevens van een dienstenserie. Zo genereer je het rapport: <!-- GPT translation -->

1. Selecteer in het blok **Dienstenseries** aan de linkerkant de dienstenserie waarvan je een rapport wilt genereren. <!-- GPT translation -->
2. Klik op **Toepassen**{:.doc-button}. <!-- Repetition of GPT translation -->
3. Klik boven de tabel op _Report aanmaken_{:.doc-button}. <!-- GPT translation -->
4. In het dialoogvenster kun je het selectievakje aankruisen om het rapport naar het e-mailadres te sturen dat je voor je injixo-account hebt gebruikt. <!-- GPT translation -->

Het rapport bevat de begintijden, eindtijden en netto tijdsduur in uren van alle activiteiten of dagmodellen uit de dienstenserie. Het rapport is geordend per week. <!-- GPT translation -->
Bovendien worden de volgende totalen en gemiddelden van de netto tijdsduur weergegeven: <!-- GPT translation -->

- Tabel: Nettoduur van alle activiteiten of dagmodellen in de dienstenserie. <!-- GPT translation -->
- Kolom Totaal (opgeteld): Totaal toegevoegde nettowaarde van de activiteiten of dagmodellen per week. <!-- GPT translation -->
- Gemiddelde rij: Gemiddelde waarde voor alle waarden in de Rij totaal. <!-- GPT translation -->