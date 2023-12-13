---
title: Overwerkbeheer
product_label:
  - advanced
  - enterprise
  - classic
description: Lees hoe je activiteiten het best configureert om overwerk in te plannen en op een transparante manier te documenteren.
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/importance-for-activities.md
---

Soms is het nodig dat medewerkers overwerk verrichten om het service level op peil te houden. Redenen voor overwerk kunnen zijn: een onverwacht hoge workload of onderbezetting door een hoge afwezigheid door ziekte of verlof.  
Vaak geven de contracten van je medewerkers voor dat overwerk tegen een hoger tarief moet worden vergoed, of dat overuren als extra verlof moeten worden toegekend. Het is belangrijk om contractuele beperkingen na te leven, zoals de rusttijd tussen diensten als medewerkers overwerken. Als je een dienstverlener bent, dan ben je mogelijk verplicht om klanten over extra ingepland werk te informeren. 

In dit artikel vind je tips over hoe je activiteiten en multiactiviteiten zo configureert, dat overwerk eenvoudig kan worden ingepland en correct in je dekkings-heatmap en in je rapporten wordt weergegeven.

Overwerk moet in Shift Center of Schedules handmatig als aanvulling op de bestaande planning worden ingepland.

## Activiteiten aanmaken voor overwerk

In het onderstaande voorbeeld nemen we een activiteit met de naam Gesprekken. Volg deze stappen voor alle activiteiten die je als overwerk wilt kunnen inplannen, bijvoorbeeld voor Gesprekken of E-mails, maar niet voor Ziek of Vakantie.

1. {% link_new Maak de activiteit | features/administration/activities.md %} **Gesprekken** aan en voer de configuratie uit. 
2. Dupliceer de activiteit **Gesprekken** en geef de kopie de naam **Gesprekken overwerk**. Je hoeft geen kwalificaties aan deze activiteit toe te voegen.  
  - Vink het selectievakje **Speciale behandeling in geoptimaliseerde planning** aan.
  - Zorg dat het selectievakje **Aanvraagbaar in Me** is uitgevinkt.
3. Voeg in **Gesprekken overwerk** **Gesprekken** toe als deelactiviteit.  
  **Gesprekken overwerk** is nu een multiactiviteit.
4. Voeg beide activiteiten toe aan de relevante eenheid. Voeg de overwerkactiviteit niet aan een dagmodel toe.

Met deze configuratie kan de actviteit Gesprekken overtijd alleen handmatig worden ingepland. Zo voorkom je dat de activiteit tijdens planningsoptimalisatie wordt vervangen. Medewerkers kunnen deze activiteit niet aanvragen in injixo Me.

Door "overwerk" op te nemen in de naam van de multiactiviteit, zien jij en je medewerkers eenvoudig in de planning wanneer, voor hoe lang en aan welke taak je medewerkers overwerk verrichten.

## Overwerk inplannen

Je kunt overwerk handmatig inplannen in _Plan > Dienstrooster-Center_{:.breadcrumbs} of in _Plan > Schedules_{:.breadcrumbs}.

Volg deze stappen om overwerkactiviteiten in Dienstrooster-Center toe te voegen:

1. Selecteer de eenheid en optioneel de selectie waartoe de medewerker die je voor overwerk wilt inplannen, behoort,
2. Dubbelklik op de cel van de medewerker voor de betreffende dag waarop zij over moeten werken. Klik op het tabblad **Multi-activiteiten** en selecteer **Gesprekken overwerk**.
3. Stel een begin- en eindtijd in voor de activiteit.
4. Klik op _OK_{:.doc-button}.

De ingeplande overtijd wordt direct weergegeven in het planningsvenster en het tabblad Activiteiten in het {% link_new parametervenster | features/scheduling/shiftcenter/shift-center-overview.md | #parameter-window %}. Als je het tabblad Activiteiten zo configureert dat dekking wordt weergegeven, wordt de heatmap bijgewerkt conform het ingeplande overwerk.

Volg deze stappen om overwerkactiviteiten in _Plan > Schedules_{:.breadcrumbs} toe te voegen:

1. Dubbelklik op een cel in de planning om het bewerkingsaanzicht te openen.
2. Klik op _Nieuwe activiteit toevoegen_{:.doc-button}.  
  Aan de rechterkant wordt een nieuwe rij met de activiteit toegevoegd.
3. Selecteer in de nieuwe rij **Gesprekken overwerk** in het vervolgkeuzemenu.
4. Stel een begin- en eindtijd in voor de activiteit.
5. Klik op _Opslaan_{:.doc-button}.

## Rapporteren

Het rapport **Activiteiten in uren** laat zien dat de medewerker overwerk heeft verricht, dankzij de naam van de activiteit die deze informatie in zich draagt. Zo wordt al het overwerk gedocumenteerd en is het inzichtelijk voor alle betrokkenen, zoals de financiële afdeling die het extra salaris moet uitbetalen.
