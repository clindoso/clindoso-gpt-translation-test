---
title: Beschikbare plantypen
promote-service: new-planner-training
description: Lees meer over de verschillende plantypen in injixo.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: De plantypen combineren
    filepath: features/scheduling/combined-scheduling-methods.md
  - overwrite_title: Contracten aanmaken
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/set-a-validity-period.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: injixo Me configureren
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
---

In dit artikel lees je:

- welke plantypen er zijn.
- in welke gevallen je welk plantype het beste kunt gebruiken.

Je kunt elk van de volgende plantypen afzonderlijk gebruiken, of je kunt ze {% link_new combineren | features/scheduling/combined-scheduling-methods.md %}.

De plantypen houden rekening met de informatie uit de {% link_new contracten | features/administration/create-contracts.md %} die aan medewerkers zijn toegewezen. In contracten vind je onder meer het aantal werkdagen, het aantal werkuren per dag, week of maand, en andere planparameters.

## Vaste planning

De vaste planning biedt de minste flexibiliteit. Dit plantype is gebaseerd op {% link_new ploegendienstreeksen | features/administration/shift-sequences.md %}.

Met ploegendienstreeksen wordt er gewerkt met:

- de ploegendienstdagen van een medewerker
- het exacte begin- en eindpunt van de dienst op ploegendienstdagen

Planningen die worden gemaakt op basis van deze ploegendienstreeksen zijn elke week hetzelfde of veranderen op basis van intervallen van 2 tot 53 weken.

Na het maken van de planning kun je de volgende elementen optimaliseren:

- de plaats van pauzes in [doorgangen](/daymodel-basics#vaste-elementen-vs-doorgangen)
- {% link_new inzetbare activiteiten | features/administration/activity-types-and-properties.md | #activiteiteigenschappen %}

## Geoptimaliseerde planning

Een geoptimaliseerde planning biedt de meeste flexibiliteit. Gebruik {% link_new Geoptimaliseerde planningen aanmaken | features/scheduling/schedules/schedules-optimized-schedules.md %} om automatisch een complete planning te maken. injixo zorgt zo voor de best mogelijke dekking van de verschillende activiteiten met zo min mogelijk medewerkers.

Om aan te geven welke diensten er volgens je dienstenpatronen beschikbaar zijn om te plannen, kan je {% link_new weekpatroonmodellen | features/administration/work-time-pattern-models.md %} gebruiken.

### Volledig flexibele diensten

Wijs je medewerkers {% link_new weekpatroonmodellen van type A | features/administration/work-time-pattern-models.md | #typen-tijdmodellen %} toe.

Alle diensten die beschikbaar zijn volgens het weekpatroonmodel en die compatibel zijn met het contract van de medewerker, kunnen op elke dag worden gepland.

Om te zorgen dat je medewerkers je planningen beter accepteren, kun je bepaalde diensten uitsluiten door persoonlijke dagmodellen toe te wijzen aan medewerkers of door [beschikbaarheidspatronen](#beschikbaarheidspatronen) te gebruiken. 

### Roulerende flexibele diensten

Wijs je medewerkers {% link_new weekpatroonmodellen van type B, C of D | features/administration/work-time-pattern-models.md | #types-weekpatroonmodellen %} toe.

Diensten die beschikbaar zijn volgens het geselecteerde weekpatroonmodel en die in overeenstemming zijn met het contract van de medewerker, worden in een vaste volgorde gepland. Ze kunnen zelfs elke dag op hetzelfde tijdstip beginnen.

### Beschikbaarheidspatronen

{% link_new Beschikbaarheidspatroon | features/administration/availabilities.md %} kunnen in geoptimaliseerde planningen worden gebruikt om de planningsmogelijkheden te beperken.

## Dienstenveiling

Bij {% link_new inzetten in de veiling | features/scheduling/schedules/schedules-shift-bidding.md %} wordt de definitieve planning pas gemaakt nadat medewerkers erbij zijn betrokken. In injixo Me kunnen ze van tevoren specifieke diensten aanvragen.

Zo gaat de workflow in zijn werk:

1. Bepaal hoeveel diensten je nodig hebt.
2. Genereer diensten op basis van de ingeschatte personeelsbehoefte.
3. Zet de status van je planningsperiode op **gepubliceerd**. Je medewerkers kunnen maximaal twee diensten per dag aanvragen (tot maximaal 10).
4. Start een {% link_new inzetten loting | features/scheduling/shift-bidding.md | #loting-van-aangevraagde-diensten %} voor de aangevraagde diensten.
5. Wijs de overige diensten toe. Medewerkers van wie de aanvraag tijdens de loting niet zijn ingewilligd, worden in deze stap gepland.

## Overzicht van plantypen en configuratie-instellingen

Op basis van elk plantype stel je in _Plan > Configuratie_{:.breadcrumbs} specifieke configuratie-instellingen in. De volgende tabel geeft een overzicht van de verplichte en optionele configuratie-instellingen voor plantypen.

|                          | Vaste planning  | Geoptimaliseerde planning | Dienstenveiling |
|--------------------------| ----------------  | ---- ----------------| --------------|
| Vaardigheden            | verplicht          | verplicht              | verplicht       |
| Activiteiten            | verplicht          | verplicht              | verplicht       |
| Dagmodellen             | verplicht          | verplicht              | verplicht       |
| Organisatorische eenheden| verplicht         | verplicht              | verplicht       |
| Contracten               | verplicht          | verplicht              | verplicht       |
| Medewerkers              | verplicht          | verplicht              | verplicht      |
| Ploegendienstreeksen     | verplicht          | --                   | optioneel      |
| Planningskalender        | optioneel          | optioneel             | optioneel      |  
| Selecties                | optioneel          | optioneel             | optioneel      | 
| Weekmodellen             | --                | optioneel             | --            |
| Weekpatroonmodellen      | --                | optioneel             | --            |
