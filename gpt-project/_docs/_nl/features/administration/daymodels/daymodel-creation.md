---
title: Dagmodellen configureren
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lees hoe je dagmodellen aanmaakt van het type gefixeerde dienst, variabele dienst en beschikbaarheidskader en hoe je activiteiten aan dagmodellen toevoegt.
related_articles:
  - overwrite_title: Dagmodellen begrijpen
    filepath: features/administration/daymodels/daymodel-basics.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/set-a-validity-period.md
---

Ben je nog niet zo vertrouwd met dagmodellen? Lees dan eerst de {% link_new basisbeginselen | features/administration/daymodels/daymodel-basics.md %}.

## Dagmodellen aanmaken

Je kunt dagmodellen aanmaken en bewerken onder _Plan > Configuratie > Dagmodellen_{:.breadcrumbs}.

> Opmerking
> 
> - Dagmodellen van het type Gefixeerde dienst worden ook wel gefixeerde dagmodellen genoemd.<br> 
> - Dagmodellen van het type Variabele dienst worden ook wel variabele dagmodellen genoemd.

1. Klik op het {% icon item-add %} om een nieuw dagmodel toe te voegen.
2. Selecteer in het vervolgkeuzemenu **Type** het dagmodeltype dat je wilt configureren.
3. Configureer je dagmodel.<br>Zie de volgende secties voor meer informatie over de configuratieopties van elk dagmodeltype.
4. Klik op _OK_{:.doc-button} om het dagmodel op te slaan.

Nu kun je {% link_new activiteiten toevoegen | features/administration/daymodels/daymodel-creation.md | #activiteiten-aan-dagmodellen-toevoegen %} aan het nieuwe dagmodel. 

> Opmerking
> 
> Als je met een {% link_new beperkt aantal dagmodellen in je eenheid | features/administration/create-and-manage-planning-units.md | #dagmodellen-beperken %} werkt, dan is het wellicht nodig dat je nieuwe dagmodellen aan je eenheid toewijst. Als je gebruik maakt van planningsmodellen, werk dan je weekmodel(len) bij.

### Gefixeerde dienst
   
| **Parameter** | **Beschrijving** |
|:-----|:-----|
| Naam | Unieke naam om het dagmodel te beschrijven. We raden aan om het dagmodeltype op te nemen, samen met de begin- en eindtijd. Bijvoorbeeld: 8-16:30-fix. |
| Afkorting | Deze versie van de naam wordt weergegeven in rapporten en in Schedules. We raden aan om de gespecificeerde naam of een kortere versie ervan te gebruiken. |
| Sneltoets | Optionele sneltoets die je helpt om het dagmodel sneller in het Dienstrooster-Center in te voeren. Lees meer over {% link_new sneltoetsen | best-practices/tips-on-shift-center-usage.md %}. |
| Kleur |  De kleur wordt in de planning en op de pagina met configuratiegegevens weergegeven.<br>De kleur kan je helpen om de lengte, het dagmodeltype of opgenomen activiteiten sneller te herkennen. |
| geldig vanaf/geldig tot en met | Optionele periode tijdens welke het dagmodel gebruikt kan worden.<br>Lees meer over {% link_new geldig vanaf/geldig tot en met-datums | features/administration/set-a-validity-period.md %}. |
| Begin | Tijd waarop de gefixeerde dienst begint. |
| Eind | Tijd waarop de gefixeerde dienst eindigt. |
| Brutoduur Dienst | Dienstduur in uren.<br>Als je deze waarde configureert, dan vervangt deze de geconfigureerde eindtijd.<br>Opmerking: Dagmodellen van het type Gefixeerde dienst tot twee dagen beslaan. Om een nachtdienst in te plannen, voeg je bij het aanmaken van het dagmodel tot 24 uur aan de eindtijd toe, of gebruik totale duur van de dienst. De maximale waarde is 48:00 (uur). |
| Activiteit | De eerste activiteit is de {% link_new basisactiviteit | features/administration/daymodels/daymodel-basics.md | #basisactiviteit-en-dienstduur %}.<br>Opmerking: Je kunt de basisactiviteit niet meer veranderen nadat je het dagmodel hebt opgeslagen. |


### Variabele dienst
   
| **Parameter** | **Beschrijving** |
|:---------------------|:---------------------|
| Naam | Unieke naam om het dagmodel te beschrijven. We raden aan om het dagmodeltype op te nemen, samen met de begin- en eindtijd, bijvoorbeeld: var-8-20-8. |
| Afkorting | Deze versie van de naam wordt weergegeven in rapporten en in Schedules. We raden aan om de gespecificeerde naam te gebruiken. |
| Kleur | De kleur wordt in de planning en op de pagina met configuratiegegevens weergegeven.<br>De kleur kan je helpen om de lengte, het dagmodeltype of opgenomen activiteiten sneller te herkennen. |
| geldig vanaf/geldig tot en met | Optionele periode tijdens welke het dagmodel gebruikt kan worden.<br>Lees meer over {% link_new geldig vanaf/geldig tot en met-datums | features/administration/set-a-validity-period.md %}. |
| Begin | Vroegstmogelijke tijd waarop de dienst kan beginnen. |
| Eind | Laatst mogelijke tijd waarop de dienst kan eindigen. |
| Duur | Aantal uren tussen de vroegste begintijd en de laatste eindtijd van de dienst.<br>Deze vervangt het einde van het tijdframe. |
| Brutoduur Dienst | Totale tijdsduur van de dienst inclusief pauzes. De duur moet korter zijn dan de tijdsspanne. Als de dienstduur overeenkomt met de tijdsspanne, wordt het dagmodel een dagmodel van het type Gefixeerde dienst. |
| Interval | Interval waarmee een dienst binnen de tijdsspanne kan beginnen |
| Activiteit | De eerste activiteit is de {% link_new basisactiviteit | features/administration/daymodels/daymodel-basics.md | #basisactiviteit-en-dienstduur %}.<br>Opmerking: Je kunt de basisactiviteit niet meer veranderen nadat je het dagmodel hebt opgeslagen. |

### Beschikbaarheidskader

Gebruik dit dagmodeltype bijvoorbeeld in dienstenseries om beschikbaarheid voor verschillende medewerkers tegelijkertijd te configureren. Houd er rekening mee dat beschikbaarheid uit dagmodellen de beschikbaarheid die door medewerkers in injixo Me en beschikbaarheid die handmatig is ingevoerd in het Dienstrooster-Center is ingevoerd, overschrijft. Lees meer over {% link_new beschikbaarheden | features/administration/availabilities.md %}.

| **Parameter** | **Beschrijving** |
|:---------------------|:---------------------|
| Naam | Unieke naam om het dagmodel te beschrijven. We raden aan om het dagmodeltype op te nemen, samen met de begin- en eindtijd, bijvoorbeeld: var-8-16. |
| Afkorting | Deze versie van de naam wordt weergegeven in rapporten en in Schedules. We raden aan om de gespecificeerde naam te gebruiken. |
| Kleur | De kleur wordt in de planning en op de pagina met configuratiegegevens weergegeven.<br>De kleur kan bijvoorbeeld handig zijn bij het aanmaken van dienstenseries. |
| geldig vanaf/geldig tot en met | Optionele periode tijdens welke het dagmodel gebruikt kan worden.<br>Lees meer over {% link_new geldig vanaf/geldig tot en met-datums | features/administration/set-a-validity-period.md %}. |
| Begin Beschikbaarheidskader | Vroegstmogelijke tijd waarop de dienst kan beginnen. |
| Einde Beschikbaarheidskader | Laatst mogelijke tijd waarop de dienst kan eindigen. |
| Duur Beschikbaarheidskader | Aantal uren tussen de vroegste begintijd en de laatste eindtijd van de dienst. De maximale waarde is 48 uur.<br>Het einde van het beschikbaarheidskader wordt hierdoor vervangen. |

## Activiteiten aan dagmodellen toevoegen

Om een bestaand dagmodel verder te definiëren, kun je er pauzes of andere activiteiten aan toevoegen. Configureer andere activiteiten als je bepaalde taken moet invoeren waar medewerkers op een bepaald moment tijdens een dienst moeten werken. Deze speciale activiteiten kunnen bijvoorbeeld zijn: het controleren van de social media-accounts van het bedrijf of het uitvoeren van backoffice-taken. 

Om activiteiten toe te voegen, moet je eerst een {% link_new dagmodel aanmaken | features/administration/daymodels/daymodel-creation.md | #dagmodellen-aanmaken %}.

De planningsoptimalisatie kan activeiten van het type Aanwezigheid die als Vervangbaar zijn geconfigureerd, vervangen. Als je medewerkers niet wilt inplannen voor speciale activiteiten, dan is de basisactiviteit de enige activiteit van het type Aanwezigheid in je dagmodel. Houd er rekening mee dat het configureren van activiteiten in dagmodellen de flexibiliteit van optimalisatiefeatures (bijvoorbeeld volledige optimalisatie, extra activiteiten, vergaderingen) beperkt. Om de optimalisatie zo flexibel mogelijk te houden en planningsfouten te voorkomen, raden we aan om de configuratie van activiteiten van het type Aanwezigheid in dagmodellen tot een minimum te beperken.

> Opmerking
> 
> De eerste activiteit die je aan een dagmodel toevoegt, is automatisch de basisactiviteit. Je kunt de basisactiviteit niet meer wijzigen of verwijderen nadat je het dagmodel hebt opgeslagen.
> Wij raden aan om de activiteit Aanwezigheid als basisactiviteit te gebruiken. Lees meer over de {% link_new basisactiviteit | features/administration/daymodels/daymodel-basics.md | #basisactiviteit-en-dienstduur %}.

### Een activiteit van het type aanwezigheid of afwezigheid toevoegen

Ga als volgt te werk om een activiteit van het type aanwezigheid of afwezigheid aan een bestaand dagmodel toe te voegen:

1. Selecteer een dagmodel.
2. Klik in de sectie **Aan- en afwezigheid** op het {% icon item-add %}.<br>Er wordt een dialoogvenster geopend.
3. Configureer de activiteit:
- **Begin** en **Einde**:<br>Als het selectievakje the **In relatie tot het begin van de dienst** is aankgevinkt: Geef het aantal uren/minuten na het begin van de dienst aan waarop je de activiteit wilt laten beginnen en eindigen (voor 1,5 uur voor je bijvoorbeeld 1:30 in).<br>Als het selectievakje the **In relatie tot het begin van de dienst** niet is aankgevinkt: Voer de exacte tijd na het begin van de dienst in waarop je de activiteit wilt starten en eindigen (voer voor 2pm bijvoorbeeld 14:00 uur in).
- **Duur**: Als je een tijdsduur hebt geconfigureerd die langer is dan de tijd tussen de geconfiureerde begin- en eindtijd, maak dan een {% link_new corridor | features/administration/daymodels/daymodel-basics.md | #gefixeerde-elementen-versus-corridors %} aan waarbinnen de activiteit kan worden verschoven.
- **Interval**: We raden aan om dezelfde interval te gebruiken als voor je ACD. De lengte van de activiteit moet deelbaar zijn door het geselecteerde interval.<br>Als je 0 invoert, wordt de begintijd van de activiteit gefixeerd en de activiteit kan niet worden verschoven binnen de corridor.
- **In relatie tot het gegin van de dienst**:<br>Indien aangevinkt (standaard), begint de activiteit na het gedefinieerde aantal uren/minuten na het begin van de dienst. Als de dienst wordt verschoven, wordt de activiteit ook verschoven.<br>Indien niet aangevinkt, begint de activiteit exact op de geconfigureerde tijd. Als je een variabele dienst verschuift, dan worden de elementen niet verschoven. Dit kan handig zijn, bijvoorbeeld als medewerkers met verschillende diensten tegelijkertijd aan een teamvergadering moeten deelnemen.
4. Selecteer aan **Activiteit** in het vervolgkeuzemenu.
5. Klik op _OK_{:.doc-button}.

### Voeg een pauzeactiviteit toe

Zowel in flexibele als vaste dagmodellen kun je pauzes toevoegen voor geoptimaliseerd plannen en inschrijven op diensten.  
Ga als volgt te werk om een pauze-activiteit aan een dagmodel toe te voegen:

1. Selecteer een dagmodel.
2. Klik in de sectie **Pauzes (gecreëerde diensten)** op het {% icon item-add %}.<br>Er wordt een dialoogvenster geopend.
3. Configureer de pauze:
- **Begin** en **Einde**:<br>Als het selectievakje the **In relatie tot het begin van de dienst** is aankgevinkt: Geef het aantal uren/minuten na het begin van de dienst aan waarop je de pauze wilt laten beginnen en eindigen (voor 4,5 uur voor je bijvoorbeeld 4:30 in). Pauzes worden standaard relatief ten opzichte van het begin van de dienst ingevoerd, omdat ze meestal beginnen nadat er een bepaalde tijd is gewerkt.<br>Als het selectievakje the **In relatie tot het begin van de dienst** niet is aankgevinkt: Voer de exacte tijd na het begin van de dienst in waarop je de pauze wilt laten beginnen en eindigen (voor 1pm voer je bijvoorbeeld 13:00 uur in).
- **Duur**: Als je een tijdsduur hebt geconfigureerd die langer is dan de tijd tussen de geconfiureerde begin- en eindtijd, maak dan een {% link_new corridor | features/administration/daymodels/daymodel-basics.md | #gefixeerde-elementen-versus-corridors %} aan waarbinnen de pauze kan worden verschoven.
- **Interval**: We raden aan om dezelfde interval te gebruiken als voor je ACD. Houd er rekening mee dat de lengte van de pauze deelbaar moet zijn door het geselecteerde interval.<br>Als je 0 invoert, wordt de begintijd van de pauze gefixeerd en de activiteit kan niet worden verschoven binnen de corridor.
- **In relatie tot het begin van de dienst**:<br>Indien aangevinkt (standaard), begint de pauze na het gedefinieerde aantal uren/minuten na het begin van de dienst. Als de dienst wordt verschoven, dan wordt de pauze ook verschoven.<br>Indien niet aangevinkt, begint de activiteit exact op de geconfigureerde tijd. Als je een variabele dienst verschuift, dan worden de pauzes niet verschoven. Dit kan handig zijn, bijvoorbeeld als kantine van je contactcenter alleen gedurende een beperkte tijd geopend is.
4. Selecteer in het vervolgkeuzemenu een **Pauze**.
5. Klik op _OK_{:.doc-button}.

Opmerking: In injixo Enterprise WFM on-premise bepaalt instelling _48134_{:.id-label} of pauzecorridors blijven of dat ze worden omgezet in vaste elementen.

## Effecten van het wijzigen van dagmodellen die in gebruik zijn

Het wijzigen van dagmodellen die al in je planningen worden gebruikt, kan verschillende gevolgen hebben. Configuratiegegevens die niet relevant zijn voor het plannen, zoals de naam, afkorting of kleur, kunnen altijd probleemloos worden gewijzigd.

We raden je echter aan om alleen wijzigingen aan planningsrelevante gegevens aan te brengen, zoals begin- en eindtijden, de totale duur van een dienst, aanwezigheid en afwezigheid of pauzes, voordat je de volgende planning aanmaakt. Als je een bestaand dagmodel wijzigt, maakt injixo intern een kopie van het oorspronkelijke dagmodel. Zo blijven diensten die je al hebt ingepland behouden. Ze worden nog steeds weergegeven.

Na het wijzigen van een bestaand dagmodel of het toevoegen van een nieuw dagmodel raden we aan om opnieuw te beginnen met het planningsproces, zodat nieuwe en gewijzigde dagmodellen juist worden gebruikt.

De betreffende dagmodellen worden vervangen in het Dienstrooster-Center en in weekmodellen. Reeds ingeplande dagmodellen worden in het Dienstrooster-Center en in Schedules onderstreept met een stippellijn. Diensten met dit dagmodel kunnen niet meer worden ingepland of bewerkt. Ze kunnen alleen uit de planning worden verwijderd.

Als je diensten hebt aangemaakt op basis van een dagmodel en medewerkers dergelijke diensten al in injixo Me via Bieden op ploegendienst hebben aangevraagd, dan kunnen je medewerkers diensten met dat dagmodel niet meer zien of aanvragen.
Diensten die al zijn aangevraagd, worden niet gebruikt in de eerstvolgende verloting of het toewijzingsproces.

Opmerking: De minimum- en maximumwaarden die als dienstenbehoefte zijn ingevuld, worden op het gewijzigde dagmodel toegepast.
