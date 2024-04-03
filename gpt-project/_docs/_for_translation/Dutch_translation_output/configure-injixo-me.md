---
title: injixo Me configureren <!-- GPT translation -->
description: Stel injixo Me zo in dat medewerkers zich kunnen inschrijven op diensten, diensten kunnen ruilen met andere medewerkers, en verlof kunnen aanvragen. <!-- GPT translation -->
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/use-injixo-me/explore-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md
redirect_from:
  - /injixo-me-administration/
  - /configure-injixo-me/
redirect_reason: Updated filename on 03 July 2023
gpt_translation: true
---

In dit artikel lees je hoe je het volgende voor medewerkers mogelijk maakt: <!-- GPT translation -->

- zich inschrijven op diensten via Diensten ruilen en Ruilpool. <!-- GPT translation -->
- diensten met andere medewerkers ruilen. <!-- GPT translation -->
- verlof aanvragen. <!-- GPT translation -->
- zijn eigen planning in te zien. <!-- GPT translation -->
- de planningen van de teamleden te bekijken. <!-- GPT translation -->
- aangepaste beschikbaarhheidskaders instellen voor bepaalde periodes. <!-- GPT translation -->

Als je toegang hebt tot _Admin-rechten_, kun je injixo Me-functies in- en uitschakelen. Ga hiervoor naar **Me** in de hoofdnavigatie en klik op de **schakelaar** bij de betreffende functie. <!-- GPT translation -->

> Opmerking <!-- TM 100 -->
> <!-- TM 100 -->
> Om toegang te krijgen tot injixo Me en gebruik te kunnen maken van de beschreven features, hebben medewerkers een injixo-account nodig. Lees hoe je {% link_new een account voor hen aanmaakt | features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md %}. <!-- GPT translation -->

## Inschrijven op diensten <!-- TM 100 -->

Medewerkers kunnen zich op basis van de behoeften van medewerkers en dienstroosters inschrijven op diensten die van tevoren zijn aangemaakt. Diensten worden dan verloot en eventueel overgebleven diensten kunnen achteraf handmatig worden toegewezen. Lees meer over {% link_new inschrijven op diensten | features/scheduling/schedules/schedules-shift-bidding.md %}. <!-- GPT translation -->

{{ 5 | image: 'Inschrijven op diensten', '80%' }} <!-- GPT translation -->

## Diensten ruilen <!-- GPT translation -->

Medewerkers kunnen zelfstandig diensten of vrije dagen ruilen met andere medewerkers. De procedure verloopt als volgt: <!-- GPT translation -->

1. Een medewerker biedt een dienst aan. <!-- GPT translation -->
2. Een andere medewerker ziet de dienst en accepteert deze. <!-- GPT translation -->
3. De diensten zijn geruild. <!-- GPT translation -->

Lees meer over {% link_new hoe je medewerkers de mogelijkheid geeft om diensten met elkaar te ruilen | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}. In de [Teamkalender](#team-calendar) kunnen medewerkers de diensten van hun collega's bekijken. Afhankelijk van je injixo-configuratie moet je {% link_new dienstruilverzoeken handmatig goedkeuren | features/scheduling/view-approve-shift-swap-requests.md %}. <!-- GPT translation -->

{{ 6 | image: 'Dienstruiling', '50%' }} <!-- GPT translation -->

## Aanvragen verlof <!-- GPT translation -->

Medewerkers kunnen verlofaanvragen indienen voor activiteiten van het type Afwezigheid, Vakantie of Ziekte voor periodes die variëren van een aantal uur tot weken. Ze kunnen ook hun jaarlijkse vakantieaanspraak en het resterende aantal vakantiedagen zien. <!-- GPT translation -->

Lees meer over hoe je het aanvragen van verlof voor je medewerkers {% link_new activeert | features/scheduling/time-off/time-off-periods.md %}. Beheer de manier waarop medewerkers verlof kunnen aanvragen met {% link_new instellingen voor de vakantierechten | features/scheduling/time-off/vacation-entitlement.md %}, {% link_new goedkeuringsregels | features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md %} en {% link_new quota | features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md | #quoota-instellingen %}. Goedkeuren of afwijzen doe je in {% link_new Verlof | features/scheduling/time-off/vacation-absences-management.md %}. <!-- GPT translation -->

{{ 1 | image: 'Schermafbeelding om een verlofaanvraag in te dienen', '50%' }} <!-- GPT translation -->

> Alleen activiteiten van het type _vakantie_ beïnvloeden de vakantieaanspraken. <!-- GPT translation -->

## Teamkalender <!-- GPT translation -->

In het **Teamkalender** kunnen collega's (`HK professionals`, `leidinggevenden` en `accountmanagers`) de werktijden van alle collega's bekijken die in dezelfde {% link_new groep | features/administration/selections.md %} zijn geplaatst: acitiviteiten worden hier samen met de diensten van al je collega's aangegeven als gekleurde balken met afbeeldingen. Als je een planningsperiode hebt aangemaakt en de status `Ongepubliceerd`, dan worden in de teamkalender alleen diensten en privé-verlof weergegeven. Opmerking: Als je calendarView een andere kleurcodering bevat, worden je activiteiten grijs weergegeven (in plaats van gekleurd). <!-- GPT translation -->

{{ 7 | image: 'Team calendar', '80%' }} <!-- GPT translation -->

## Beschikbaarheden <!-- GPT translation -->

Medewerkers kunnen in het menu **Beschikbaarheid** persoonlijke kaders instellen waarin ze al dan niet kunnen werken. Ze kunnen tijdsbestekken van elke lengte instellen, ongeacht de uren die in hun contract zijn vastgelegd. Lees meer over het plannen met {% link_new beschikbaarheid | features/scheduling/scheduling-methods.md %}. <!-- GPT translation -->

Als je medewerkers uiterst korte tijdsbestekken invullen, worden mogelijk niet alle diensten aangemaakt. Controleer daarom altijd eerst welke beschikbaarheden door je medewerkers zijn ingevoerd, voordat je de planning maakt. <!-- GPT translation -->

{{ 2 | image: 'Beschikbaarheid instellen', '50%' }} <!-- GPT translation -->

## Verlofsaldo in uren <!-- GPT translation -->

Dit zorgt ervoor dat het vakantietegoed in plaats van in dagen in uren wordt weergegeven. Dit is van toepassing op alle aangevraagde, resterende en goedgekeurde verlofaanvragen die de medewerkers in het menu-item **Verlof** kunnen bekijken. <!-- GPT translation -->

Deze instelling heeft geen invloed op de weergave van overige dag- en uurwaarden, bijvoorbeeld in secties als **Vakantie/Afwezigheidsadministratie** of **Vakantierecht** in injixo. <!-- GPT translation -->

{{ 4 | image: 'Vakantiesaldo In uren', '40%' }} <!-- GPT translation -->