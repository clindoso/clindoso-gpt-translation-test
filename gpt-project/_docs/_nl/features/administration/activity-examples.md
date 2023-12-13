---
title: Configuratievoorbeelden van activiteiten
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: false
description: Configureer standaard activiteiten aan de hand van voorbeelden.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

Om te configureren hoe injixo tijdens het plannen en rapporteren omgaat met activiteiten, gebruik je de {% link_new activiteitentypen en -eigenschappen | features/administration/activity-types-and-properties.md %} onder _Plan > Configuratie > Activiteiten_{:.breadcrumbs}.

Hier volgen een paar aanbevelingen voor veel gebruikte activiteiten, de typen en bijbehorende eigenschappen.

## Aanwezigheid, pauze, ziek en vakantie

Deze tabel bevat configuratievoorbeelden voor de activiteitentypen Aanwezigheid, Pauze, Ziek en Vakantie.
De activiteit Aanwezigheid is een vooraf geconfigureerde standaardactiviteit in injixo. Je gebruikt hem voor alle activiteiten waar je medewerkers aan werken en die gebaseerd zijn op personeelsbehoeften, bijvoorbeeld gesprekken. 

<div class="table__wrapper" markdown="1">

<style>
table {
   width: 100%;
}
</style>

|                                        |  Aanwezig  | Middagpauze |         Ziek         |  Vakantie |
| ------------------------------------------- | :---------------------: | :----------------------: | :---------------------: | :---------------------: |
| **Type**                                        |         Aanwezigheid         |          Pauze           |         Ziek         |        Vakantie         |
| Betaald                                        | <i class="fa fa-check"> |                          | <i class="fa fa-check"> | <i class="fa fa-check"> |
| Rusttijd aanhouden                     | <i class="fa fa-check"> |                          |                         |
| Planbaar                                   | <i class="fa fa-check"> |                          |                         |
| Aanvraagbaar in Me                                 |                         | <i class="fa fa-check">  |                         | <i class="fa fa-check"> |
| Vervangbaar                                 | <i class="fa fa-check"> |                          |                         |
| Ruilbaar met Diensten ruilen            | <i class="fa fa-check"> | <i class="fa fa-check">  |                         |
| Toestaan als Activiteit over de hele dag                  |                         |                          | <i class="fa fa-check"> | <i class="fa fa-check"> |

</div>

Afhankelijk van het beleid van je bedrijf, contracten of arbeidswetgeving kunnen sommige pauzes onbetaald zijn. Vink in dat geval het selectievakje Betaald uit.

## Afwezigheid en vergaderingen

Deze tabel bevat configuratievoorbeelden voor de activiteitentypen Afwezigheid en Vergadering.
Betaalde afwezigheid wordt gewoonlijk gebruikt om overwerk te compenseren of als blocker om  {% link_new feestdagen | best-practices/scheduling-public-holidays.md %} in te plannen.
Als er dagen zijn waarop een medewerker absoluut niet kan werken, dan kun je deze dagen blocken in de configuratie-instellingen onder Onbetaalde afwezigheid.

<div class="table__wrapper" markdown="1">

|                                          | Betaalde afwezigheid | Onbetaalde afwezigheid |    Vergadering over de hele dag     |  Training  |
| --------------------------------------------- | :-----------------------: | :-------------------------: | :---------------------: | :---------------------: |
| **Type**                                          |          Afwezigheid          |           Afwezigheid           |         Vergadering         |         Vergadering         |
| Betaald                                          |  <i class="fa fa-check">  |                             | <i class="fa fa-check"> | <i class="fa fa-check"> |
| Rusttijd aanhouden                       |                           |                             | <i class="fa fa-check"> |
| Planbaar                                     |                           |                             |                         |
| Aanvraagbaar in Me                                   |  <i class="fa fa-check">  |   <i class="fa fa-check">   |                         |
| Vervangbaar                                   |                           |                             |                         |
| Ruilbaar met Diensten ruilen              |                           |                             |                         |
| Toestaan als Activiteit over de hele dag                    |  <i class="fa fa-check">  |   <i class="fa fa-check">   |                         | <i class="fa fa-check"> |

</div>

Je kunt betaalde afwezigheid ook als compensatiedagen voor overwerk gebruiken, of als een betaalde blocker bij het {% link_new inplannen van feestdagen | best-practices/scheduling-public-holidays.md %}.<br>
De activiteit Onbetaalde afwezigheid kan ook worden gebruikt om flexibel te bepalen op welke dagen een medewerker absoluut niet kan werken.
