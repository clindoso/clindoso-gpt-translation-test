---
title: Beschikbare planningsmethoden
promote-service: new-planner-training
description: Lees meer over de verschillende planningsmethoden in injixo.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Planningsmethoden combineren
    filepath: features/scheduling/combined-scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/set-a-validity-period.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/configure-injixo-me.md
---

Je kunt elke planningsmethode zowel afzonderlijk als {% link_new in combinatie | features/scheduling/combined-scheduling-methods.md %} met andere planningsmethoden gebruiken.

De planningsmethoden houden rekening met de informatie uit de {% link_new contracten | features/administration/create-contracts.md %} die aan medewerkers zijn toegewezen. In contracten vind je onder meer het aantal werkdagen, het aantal werkuren per dag, week of maand, en andere planningsparameters.

## Gefixeerde planning

De gefixeerde planning biedt de minste flexibiliteit. Deze planningsmethode is gebaseerd op {% link_new dienstenseries | features/administration/shift-sequences.md %}.

Dienstenseries bepalen:

- de weekdagen waarop een medewerker werkt;
- de exacte begin- en eindtijden van de dienst voor elke werkdag.

Planningen die worden gemaakt op basis van deze dienstenseries zijn elke week hetzelfde of veranderen in intervallen van 2 tot 53 weken.

Na het maken van de planning kun je de volgende elementen optimaliseren:

- de plaats van pauzes in {% link_new corridors | features/administration/daymodels/daymodel-basics.md | #gefixeerde-elementen-versus-corridors %}
- {% link_new vervangbare activiteiten | features/administration/activity-types-and-properties.md | #activiteiteneigenschappen %}

## Geoptimaliseerde planning

Een geoptimaliseerde planning biedt de meeste flexibiliteit. Gebruik {% link_new Geoptimaliseerde planningen aanmaken | features/scheduling/schedules/schedules-optimized-schedules.md %} om automatisch een complete planning te maken. injixo zorgt voor de best mogelijke dekking van de verschillende activiteiten met zo min mogelijk medewerkers.

Maak gebruik van {% link_new planningsmodellen | features/administration/work-time-pattern-models.md %} om aan te geven welke diensten beschikbaar zijn om te worden ingepland.

### Volledig flexibele diensten

Voor volledig flexibele diensten wijs je {% link_new planningsmodellen van type A | features/administration/work-time-pattern-models.md | #planningsmodeltypen %} toe aan je medewerkers.

Alle diensten die beschikbaar zijn volgens het planningsmodel en compatibel zijn met het contract van de medew0erker, kunnen op elke dag worden gepland.

Om te zorgen dat je medewerkers hun planningen beter accepteren, kun je bepaalde diensten uitsluiten door persoonlijke dagmodellen toe te wijzen aan medewerkers of door [beschikbaarheden](#beschikbaarheden) te gebruiken. 

### Roulerende flexibele diensten

Voor roulerende flexibele diensten wijs je {% link_new planningsmodellen van type B, C of D | features/administration/work-time-pattern-models.md | #planningsmodeltypen %} toe aan je medewerkers.

Diensten die beschikbaar zijn volgens het geselecteerde planningsmodel en die in overeenstemming zijn met het contract van de medewerker, worden in een vaste volgorde gepland. Ze kunnen zelfs elke dag op hetzelfde tijdstip beginnen.

### Beschikbaarheden

{% link_new Beschikbaarheden | features/administration/availabilities.md %} kunnen in geoptimaliseerde planningen worden gebruikt om het aantal mogelijke diensten te beperken.

## Inschrijven op diensten

Bij {% link_new inschrijven op diensten | features/scheduling/schedules/schedules-shift-bidding.md %} wordt de definitieve planning pas gemaakt nadat je medewerkers erbij zijn betrokken. In injixo Me kunnen ze van tevoren voorkeursdiensten aanvragen.

Overzicht van de workflow:

1. Bepaal hoeveel diensten je nodig hebt.
2. Genereer diensten op basis van de voorspelde personeelsbehoefte.
3. Zet de status van je planningsperiode op **gepubliceerd**. Je medewerkers kunnen maximaal twee diensten per dag aanvragen (in totaal maximaal 10).
4. Start een {% link_new dienstenverloting | features/scheduling/schedules/schedules-shift-bidding.md | #diensten-verloten-starten %} voor de aangevraagde diensten.
5. Wijs de overgebleven diensten toe. Medewerkers die hun voorkeursdiensten tijdens de dienstenverloting niet hebben gekregen, worden in deze stap ingepland.

## Overzicht van planningsmethoden en configuratie-elementen

Op basis van elke planningsmethode configureer je in _Plan > Configuratie_{:.breadcrumbs} specifieke configuratie-elementen. De volgende tabel geeft een overzicht van de vereiste en optionele configuratie-elementen voor planningsmethoden.

|                          | Gefixeerde planning  | Geoptimaliseerde planning | Diensten verloten |
|--------------------------| ----------------  | ---- ----------------| --------------|
| Kwalificaties            | vereist          | vereist              | vereist       |
| Activiteiten            | vereist          | vereist              | vereist       |
| Dagmodellen             | vereist          | vereist              | vereist       |
| Eenheden                 | vereist         | vereist              | vereist       |
| Contracten               | vereist          | vereist              | vereist       |
| Medewerkers              | vereist          | vereist              | vereist      |
| Dienstenseries           | vereist          | --                   | optioneel      |
| Planningskalender        | optioneel          | optioneel             | optioneel      |  
| Groepen                  | optioneel          | optioneel             | optioneel      | 
| Weekmodellen             | --                | optioneel             | --            |
| Planningsmodellen        | --                | optioneel             | --            |