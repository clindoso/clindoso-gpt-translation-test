---
title: Multiskill-agents in te plannen <!-- GPT translation -->
product_label:
  - advanced
  - enterprise
  - classic
description: Plan multiskill-medewerkers in met Geoptimaliseerde Scheduling. <!-- GPT translation -->
toc: true
gpt_translation: true
---

Contactcenters beschikken over meerdere kanalen, bijvoorbeeld telefoonlijnen voor bestellingen, e-mail en chat voor klachten, wat verschillende vaardigheden vereist. Niet alle agenten hebben op alle gebieden ervaring, en zij kunnen alleen met contacten omgaan waarvoor zij de juiste skills hebben. <!-- GPT translation -->

## Rapportage in injixo <!-- GPT translation -->

In injixo pronkt Geoptimaliseerde planning met ondersteuning voor multiactiviteiten. Zo kun je taken met meerdere kwalificaties of meerdere kanalen inplannen. <!-- GPT translation -->

Elk kanaal staat voor een subactiviteit en elke kwalificatie voor een betreffende injixo-kwalificatie. Tijdens het planningsproces worden alle medewerkerskwalificaties tegelijkertijd meegenomen in de berekening van de personeelsbehoefte. Dit zorgt voor een pooling-effect, waardoor de totale behoefte aan medewerkers afneemt omdat alle benodigde kwalificaties door minder medewerkers gedekt worden. <!-- GPT translation -->

## Aanbevolen aanpak <!-- GPT translation -->

1. Een {% link_new Multiactiviteit | features/administration/activity-types-and-properties.md | #deelactiviteiten %} aanmaken. <!-- GPT translation -->

2. Maak de forecast aan. Voor Multiactiviteit vervolgactviteiten heb je een workload voor elke kwalificatie en elk contactkanaal nodig. <!-- GPT translation -->

3. Bereken de personeelsbehoefte voor multiactivity door het script `Gesprekken - Multiactivity` te gebruiken. Voor multichannel zijn er verdere parameters nodig, bijvoorbeeld voor chat de parameters `seq. (%)` en het maximum aantal gelijktijdige sessies; zie {% link_new Multiactivity-behoefte | features/forecast/requirement-scripts/multiactivity-script.md %} en {% link_new Chat-behoefte | features/forecast/requirement-scripts/requirement-chat.md %}. <!-- GPT translation -->

4. Voer de functionaliteit**Geoptimaliseerde planning maken** uit. <!-- GPT translation -->

### Planningsresultaat <!-- GPT translation -->

Het _Dienstrooster-Center_{:.menu-item} bevat alleen de meerdere activiteiten. De deelactiviteiten zijn te vinden in het venster Parameters: <!-- GPT translation -->

{{ 2 | image: "Dienstrooster-Center met parameters voor multiactiviteit" }} <!-- GPT translation -->

> Tip <!-- GPT translation -->
>
> Het is niet mogelijk om de waarden voor de bezetting in elke deelactiviteit toe te voegen om de waarde voor de overkoepelende multiactiviteit te berekenen. <!-- GPT translation -->
>
> De bezetting in de multiactiviteit is altijd gelijk aan het aantal ingeplande medewerkers. Het Dienstrooster-centrum toont bij de subactiviteiten eerst en vooral het aantal medewerkers dat gekwalificeerd is voor deze activiteit. Wanneer medewerkers voor meerdere subactiviteiten zijn gekwalificeerd, kunnen de bezettingswaarden van de afzonderlijke activiteiten maximaal gelijk zijn aan die van de multiactiviteit. <!-- GPT translation -->

Om alle toegewezen activiteiten van een medewerker voor een dag te bekijken, dubbelklik je op een dagcel en selecteer je het tabblad **Multi-Activities**. <!-- GPT translation -->

{{ 1 | image: "deelactiviteiten in het dialoogvenster Dienstencentrum", '60%' }} <!-- GPT translation -->

Voor Intraday Management kunnen {% link_new Dashboards | features/monitoring/dashboards/manage-dashboards.md %} de dekking en bezetting weergeven voor multiactiviteiten en hun deelactiviteiten. Trek de bezetting van de individuele deelactiviteiten en de multiactiviteit zelf in de grafiek bij elkaar op. <!-- GPT translation -->

{{ 3 | image: "Weergave multiactiviteiten: bezetting-dashboard" }} <!-- GPT translation -->