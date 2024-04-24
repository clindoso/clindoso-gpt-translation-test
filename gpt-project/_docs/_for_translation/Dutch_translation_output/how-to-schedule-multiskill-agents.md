---
title: Multiskill-agenten in te plannen <!-- GPT translation -->
product_label:
  - advanced
  - enterprise
  - classic
description: Plan multiskill-agents in met behulp van geoptimaliseerde planningen. <!-- GPT translation -->
toc: true
gpt_translation: true
---

Contactcenters bieden klanten meerdere communicatiekanalen, bijvoorbeeld telefoonnummers voor bestellingen en e-mail en chat om klachten af te handelen. Dit vraagt om meerdere vaardigheden. Niet alle agenten beschikken over alle vaardigheden, en alleen de agenten die over de benodigde vaardigheden beschikken, kunnen worden toegewezen aan contacten die een bepaalde vaardigheid vereisen. <!-- GPT translation -->

## Zendesk-gegevens in injixo <!-- TM 67 -->

In injixo worden multiactiviteiten die door geoptimaliseerde planning worden ondersteund voor het inplannen van multiskill- of multikanaal-taken gebruikt. <!-- GPT translation -->

Elk communicatiekanaal vertegenwoordigt een subactiviteit en elke medewerkerskwalificatie een overeenkomstige injixo-kwalificatie. Tijdens het plannen worden alle medewerkerskwalificaties tegelijkertijd opgenomen in de berekening van de personeelsbehoefte. Dit leidt tot een pooling-effect waarbij de totale personeelsbehoefte afneemt, omdat alle benodigde kwalificaties door minder medewerkers worden afgedekt. <!-- GPT translation -->

## Aanbevolen aanpak <!-- GPT translation -->

1. Een {% link_new meervoudige activiteit | features/administration/activity-types-and-properties.md | #meervoudige-activiteiten %} aan te maken. <!-- GPT translation -->

2. Maak de forecast aan. Voor multiactiviteit heb je een workload nodig voor elke kwalificatie en de contactkanalen. <!-- GPT translation -->

3. Bereken de personeelsbehoefte voor de multiactivity met behulp van het script `Oproepen - Multiactiviteit`. Voor multichannel zijn er meer parameters nodig, bijvoorbeeld voor chatsessies: het `% seq.`-parameter en het maximum aantal gelijktijdige sessies; zie {% link_new Multiactivity-behoefte | features/forecast/requirement-scripts/multiactivity-script.md %} en {% link_new Chat-behoefte | features/forecast/requirement-scripts/requirement-chat.md %}. <!-- GPT translation -->

5. Gebruik de functionaliteit **Geoptimaliseerde planning maken**. <!-- TM 93 -->

## Planningsregels <!-- TM 76 -->

In _Dienstrooster-Center_{:.menu-item} bevat het dienstrooster alleen de multiactiviteit. De deelactiviteiten worden weergegeven in het venster met de parameters: <!-- GPT translation -->

{{ 2 | image: "Dienstrooster-Center met parameters voor multiactiviteit" }} <!-- GPT translation -->

> Tip <!-- GPT translation -->
> <!-- TM 100 -->
> Je kunt de waarde voor het multiwerk niet berekenen door de planningswaarden voor elke deeltaak op te tellen. <!-- GPT translation -->
> <!-- TM 100 -->
> Bij de `MVK - één activiteit-selectie` is de diensteneenheid altijd gelijk aan het aantal ingeplande medewerkers. Het Dienstrooster-Center geeft het aantal medewerkers aan dat bevoegd is om deze taak uit te voeren, niet het absolute aantal dat voor activiteiten is ingepland. Als medewerkers voor meerdere deelactiviteiten zijn gekwalificeerd, dan kunnen de diensteneenheden van de deelactiviteiten hooguit zo hoog zijn als de diensteneenheid van de hoofdactiviteit. <!-- GPT translation -->

Om de toegewezen activiteiten voor een dag te bekijken, dubbelklik je op een dagcel en selecteer je het tabblad **Multi-Activiteiten**. <!-- GPT translation -->

{{ 1 | image: "Deelactiviteiten in het dienstencentrumvenster", '60%' }} <!-- GPT translation -->

Voor intraday management kunnen {% link_new Dashboards | features/monitoring/dashboards/manage-dashboards.md %} de dekking en de bezetting weergeven voor multiactiviteiten en hun deelactiviteiten. Integreer de bezetting voor de enkele deelactiviteiten en de multiactiviteit zelf in de grafiek. <!-- GPT translation -->

{{ 3 | image: "Dashboard voor workforceplanning van multiactiviteiten" }} <!-- GPT translation -->