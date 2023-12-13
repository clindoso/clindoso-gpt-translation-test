---
title: Beschikbaarheden
product_label:
  - advanced
  - enterprise
  - classic
description: Maak herbruikbare beschikbaarheden aan om tijdsperiodes te definiëren, tijdens welke medewerkers kunnen worden ingepland.
related_articles:
  - overwrite_title: Dienstenseries
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Dienstenseries
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Planningsmethoden
    filepath: features/administration/employee-overview.md
  - overwrite_title: Planningsmethoden
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
---

In dit artikel lees je:

- wat beschikbaarheden zijn.
- hoe je beschikbaarheden instelt.

## Wat zijn beschikbaarheden?

Bbeschikbaarheden gebruik je als een medewerker op een bepaalde dag niet (of slechts gedeeltelijk) beschikbaar is. Door beschikbaarheden te gebruiken, kun je de beperkingen door kantooruren en contractuele beperkingen van je eenheid nog verder beperken.

Alleen als een dienst of activiteit binnen de ingestelde tijdsperiode past, kan deze in het rooster worden opgenomen. Medewerkers zonder beschikbaarheid gelden als volledig beschikbaar tijdens je kantooruren.

## Usecases

Beschikbaarheden kunnen voor verschillende doeleinden worden gebruikt. De onderstaande usecases gelden slechts als voorbeeld.

| Usecase                              | Voorbeeld                                                                                              |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Vaste werkdagen/-tijden tijdens elke week. | Medewerkers worden alleen voor vroege diensten of voor diensten met een vroegere eindtijd, zodat zij de zorg voor hun kinderen op zich kunnen nemen.         |
| Weekenden blokkeren                        | Medewerkers worden niet in weekenden ingepland. Beschikbaarheden van één minuut zorgen ervoor dat een medewerker niet wordt ingepland.              |
| Beschikbaarheden over verschillende weken roteren    | 50% van het team werkt slechts tot 14:00 uur; de rest werkt langer door vanwege uitgebreide telefonische support.       |
| Kernwerktijden visualiseren          | Medewerkers hebben een beschikbaarheid op basis van hun contract die door een dienstenserie kan worden overschreven. |
| Tijdelijk (on)beschikbare medewerkers   | Als de beschikbaarheid van medewerkers tijdelijk verandert, kun je deze overschijven met dienstenseries.        |

<!-- just a test if people read carefully :) What do you think? -->

We komen graag meer te weten over jouw speciale usecases. Voeg deze toe in een commentaar in de feedbacksurvey voor dit artikel.

## Planningsimpact

injixo houdt bij het maken van geoptimaliseerde planningen standaard rekening met beschikbaarheden.  Beschikbaarheden worden niet gecontroleerd tijdens het aanmaken van diensten, maar pas als de planning tijdens een loterij/toewijzingsproces wordt opgeslagen.

injixo controleert alleen op beschikbaarheid als de planningsregel _2611_{:.id-label} _Medewerkersbeschikbaarheid controleren_ is ingeschakeld.

Tip: Als je wilt dat je medewerkers diensten kunnen aanvragen die langer zijn dan hun beschikbaarheid, dan kun je deze planningsregel uitschakelen.

## Beschikbaarheden instellen

Beschikbaarheden kunnen op twee manieren worden ingesteld:

| Naam                     | Details                                                                                             |
| ------------------------ | --------------------------------------------------------------------------------------------------- |
| Medewerkersbeschikbaarheden  | Stel in de medewerkerconfiguratie tijdelijke of permanente beschikbaarheden in voor afzonderlijke medewerkers.  |
| Dagmodelbeschikbaarheden | Voeg beschikbaarheden toe aan dienstenseries om dezelfde beschikbaarheid voor meerdere medewerkers toe te voegen.           |

Opmerking: Dagmodelbeschikbaarheden overschrijven de medewerkersbeschikbaarheden en beschikbaarheden die je handmatig hebt ingevoerd.

Indien je dit toestaat, {% link_new kunnen medewerkers hun eigen beschikbaarheid invoeren | features/injixo-me/use-injixo-me/explore-injixo-me.md | #je-beschikbaarheid-instellen-beschikbaarheid %} in het medewerkersportaal. De beschikbaarheden worden als medewerkersbeschikbaarheden ingevoerd (max. 14). Medewerkers of planners dienen verouderde items zelf regelmatig uit de lijst te verwijderen. Aangezien deze feature geen automatisch beoordelingsproces bevat, is het raadzaam om deze beschikbaarheden handmatig te controleren voordat de planning wordt gemaakt, om fouten in de planning te voorkomen.

### Tips voor het instellen van tijdsperioden

Je kunt de exacte werktijden van je medewerkers in kaart brengen, bijvoorbeeld 8:00 uur tot 17:00 uur.

Voor meer flexibiliteit kun je de tijdsperiode van de beschikbaarheden (begin- of eindtijd) aanpassen aan de kantooruren van je eenheid, bijvoorbeeld:

- 0:00 uur - 20:00 uur: Medewerkers kunnen voor 20:00 uur werken.
- 16:00 uur - 0:00 uur: Medewerkers kunnen niet voor 16:00 uur beginnen.

Om medewerkers op bepaalde weekdagen niet in te plannen, plan je beschikbaarheden van een minuut voor hen in, bijvoorbeeld van 0:00 uur 0:01 uur.

### Medewerkersbeschikbaarheden aanmaken

In de medewerkersconfiguratie kun je voor afzonderlijke medewerkers tijdelijke of permanente beschikbaarheden toevoegen.  Het is niet mogelijk om medewerkersbeschikbaarheden voor meerdere medewerkers tegelijk in te stellen.  Gebruik daarvoor dagmodelbeschikbaarheden in dienstenseries.

1. Ga naar _WFM > Administratie > Planning > Medewerkers_{:.breadcrumbs}.
2. Klik op een **medewerker** in de lijst.
3. Scroll naar de sectie _Beschikbaarheid_ aan de rechterkant (of klik op de snelkoppeling _Beschikbaarheid_ bovenaan).
4. Klik op het {% icon item-add %} om een nieuwe beschikbaarheid toe te voegen.
5. (Optioneel) Voer een datum toe voor **Geldig vanaf** en **Geldig tot en met**. Als de beschikbaarheid alleen voor een bepaald datumbereik geldt, is deze limiet de {% link_new geldigheidsperiode | features/administration/set-a-validity-period.md %}.
6. Selecteer een of meer **dagtypes** om de weekdag in te stellen. Houd CTRL ingedrukt om meerdere items te selecteren.
7. Voer in het veld **Vanaf** een starttijd en in het veld **Tot** een eindtijd in. De tijden gelden voor alle geselecteerde dagen.
8. (Optioneel) Als de tijdperiode middernacht overschrijdt, bijvoorbeeld bij nachtdiensten, vink dan het selectievakje **Beschikbaarheidsperiode eindigt op de volgende dag** aan.
9. Klik op _OK_{:.doc-button}.

De nieuwe medewerkersbeschikbaarheid is nu actief.

### Dagmodelbeschikbaarheden

Je kunt dagmodelbeschikbaarheden aanmaken en deze handmatig of in dienstenseries toevoegen.

1. Ga naar _WFM > Administratie > Planning > Dagmodellen_{:.breadcrumbs}.
2. Selecteer het type _Beschikbaarheidsperiode_.
3. Voer een unieke **Naam** en een **Afkorting** in, bijvoorbeeld _Beschikbaarheid 8:30 uur - 19:00 uur_ en _Beschikb 8:30-19u_.
4. (Optioneel) Selecteer een **kleur**. De kleur kan bijvoorbeeld handig zijn bij het aanmaken van dienstenseries.
5. Voer het **Begin van de beschikbaarheidsperiode** in. Dit is het vroegst mogelijke begin van de dienst.
6. Voer het **Einde van de beschikbaarheidsperiode** in. Dit is het laatst mogelijke begin van de dienst. Je kunt ook een **Tijdsduur beschikbaarheidsperiode** instellen. De maximale waarde is 48 uur.
7. Klik op _OK_{:.doc-button}.

Je kunt het nieuwe dagmodel nu handmatig in het Diensten-Center of {% link_new dienstenseries | features/administration/shift-sequences.md | #dagmodellen-toevoegen %} uploaden.

## Beschikbaarheden in het Diensten-Center/Schedules

Het Diensten-Center geeft beschikbaarheden op elk niveau weer met het symbool `<>`. Beweeg de cursor over het symbool om een tooltip met meer informatie te zien.

Op het niveau _Beschikbaarheid_ kun je {% link_new Beschikbaarheden toevoegen | features/scheduling/shiftcenter/add-and-delete-items.md | #add-an-availability %}. In de dagcellen worden alle beschikbaarheden als oranje elementen weergegeven. In uitgeklapte dagcellen worden medewerkerbeschikbaarheden weergegeven als oranje onderstreepte witte balken.

Opmerking: Om de symbolen `<>` in injixo Enterprise WFM on-premise weer te geven, moet je eerst instelling _48188_{:.id-label} _Weergave van beschikbaarheidsinformatie in het Diensten-Center_ inschakelen.

De Schedules-feature kan beschikbaarheden alleen weergeven als _Aanwezigheidsactiviteit_. Dit kan niet worden aangepast.

## Beschikbaarheden bewerken en verwijderen

Je kunt de begin- en eindtijd of handmatig toegevoegde beschikbaarheden wijzigen of verwijderen op het niveau _Beschikbaarheid_ in het Diensten-Center. Dubbelklik op een **dagcel** om het dialoogvenster te openen. Je kunt ook je muis gebruiken om een item te wijzigen.

Lees meer over de mogelijkheden om {% link_new items in het Diensten-Center te wijzigen | features/scheduling/shiftcenter/modify-items.md %}.

Tip: Voor tijdelijke wijzigingen kun je medewerkers- en dagmodel-beschikbaarheden naar een andere (of dezelfde) cel kopieren om ze om te zetten in handmatig toegevoegde beschikbaarheden.

Wijzig de dienstenserie om permanente wijzigingen aan te brengen. Om dagmodel-beschikbaarheden uit dienstenseries te verwijderen, kun je ook de feature {% link_new Lege nvieaus | features/scheduling/schedules/schedules-empty-levels.md %} gebruiken.  Voor medewerkersbeschikbaarheden ga je naar de sectie _Beschikbaarheden_ in de [medewerkersconfiguratie](/employee-overview#configure-employee-settings). In plaats van het beschikbaarheidsitem te verwijderen, kun je de toewijzing ook verwijderen door een geldig tot en met-datum toe te voegen.
