---
title: De basisconfiguratie instellen
description: Vereiste configuratiegegevens om een planning te maken.
redirect_from:
  - nl/configuration-hints/
  - nl/quickstart-base-configuration/
redirect_reason: Updated filename on 24 July 2023
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
---

Voordat je kunt gaan plannen, moet je de basisconfiguratie in injixo instellen. Een aantal items in de basisconfiguratie zijn per se nodig om een planning aan te maken, terwijl andere optioneel zijn. Dit is onder meer afhankelijk van de {% link_new planningsmethoden | features/scheduling/scheduling-methods.md %} die je wilt gebruiken.

## Configuratievolgorde

We raden je aan om de configuratie-items in de volgorde in te stellen zoals hieronder wordt weergegeven. De configuratie-items zijn deels van elkaar afhankelijk en kunnen aan elkaar worden toegewezen. Klik op de links in de tabel voor meer informatie over elk configuratie-item en hoe je deze instelt.
Elke configuratie-instelling is anders, daarom kan de optimale volgorde voor jouw organisatie afwijken. Gebruik dit artikel als checklist als aanvulling op je onboarding. Als je vragen hebt, neem dan contact op met je consultant.

### Vereiste configuratie-items

De tabel hieronder geeft een overzicht van de vereiste configuratie-items die in injixo moeten worden ingesteld, ongeacht de planningsmethode die je wilt gebruiken.

<table>
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 75%;">
  </colgroup>
  <thead>
    <tr>
      <th>Configuratie-item</th>
      <th>Beschrijving</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{% link_new Kwalificaties | features/administration/work-with-skills.md %}</td>
      <td>Kwalificaties staan voor de vaardigheden van je medewerkers. Door kwalificaties aan je medewerkers toe te wijzen, worden ze gekwalificeerd om aan bepaalde activiteiten te werken. In injixo moeten kwalificaties worden toegewezen aan activiteiten waar alleen bepaalde medewerkers aan kunnen werken.  Aan activiteiten die door iedereen kunnen worden uitgevoerd, hoeven geen kwalificaties worden toegewezen.</td>
    </tr>
    <tr>
      <td>{% link_new Activiteiten | features/administration/activities.md %}</td>
      <td>Activiteiten zijn de taken, vergaderingen en afwezigheid die je inplant en rapporteert binnen je bedrijf.<br> Activiteiten worden toegevoegd aan dagmodellen en eenheden.</td>
    </tr>
    <tr>
      <td>{% link_new Dagmodellen | features/administration/daymodels/daymodel-creation.md %}</td>
      <td>Dagmodellen zijn dienstsjablonen. Dagmodellen geven de begin- en eindtijden van een dienst aan, en het aantal uren dat een medewerker per dag werkt. Ze bevatten alle aanwezigheids-, pauze- en afwezigheidsactiviteiten tijdens een dienst.<br>Dagmodellen worden toegewezen aan eenheden. Ze kunnen ook gegroepeerd worden in weekmodellen (optioneel).</td>
    </tr>
    <tr>
      <td>{% link_new Eenheden | features/administration/create-and-manage-planning-units.md %}</td>
      <td>Eenheden staan voor je echte of virtuele locaties. Ze worden gebruikt om mensen te groeperen voor planningsdoeleinden.</td>
    </tr>
    <tr>
      <td>{% link_new Contracten | features/administration/create-contracts.md %}</td>
      <td>Contracten bevatten informatie over de contractuele werkafspraken met je medewerkers, inclusief het afgesproken, minimale en maximale aantal werkuren per dag, week of maand.<br>Contracten worden toegewezen aan medewerkers.</td>
    </tr>
    <tr>
      <td>{% link_new Medewerkers | features/administration/employee-overview.md %}</td>
      <td>In Medewerkers voer je informatie in voor elke medewerker die je inplant. Op basis van deze informatie en de toewijzingen (van dagmodellen, eenheden, contracten en kwalificaties), weet injixo wanneer en aan welke taken je medewerkers kunnen werken.</td>
    </tr>
  </tbody>
</table>


### Optionele configuratie-items

De onderstaande tabel bevat een overzicht van de optionele configuratie-items die je in injixo kunt instellen op basis van de opzet van je bedrijf en de planningsmethode die je wilt gebruiken.

<table>
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 75%;">
  </colgroup>
  <thead>
    <tr>
      <th>Configuratie-item</th>
      <th>Beschrijving</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{% link_new Dienstenseries | features/administration/shift-sequences.md %} (vereist voor vaste planning)</td>
      <td>Een dienstenserie bestaat uit een aantal dagmodellen of activiteiten met een herhalend patroon.<br>Dienstenseries worden toegewezen aan medewerkers.</td>
    </tr>
    <tr>
      <td>{% link_new Groepen | features/administration/selections.md %}</td>
      <td>Met groepen kun je medewerkers filteren en groeperen of inplannen op basis van bepaalde criteria, bijvoorbeeld medewerkers die hetzelfde type contract hebben of in hetzelfde team zitten.<br> Groepen worden toegewezen aan medewerkers.</td>
    </tr>
    <tr>
      <td>{% link_new Planningsmodellen en weekmodellen | features/administration/work-time-pattern-models.md %}</td>
      <td>Planningsmodellen en weekmodellen helpen je bij het organiseren van je diensten door ervoor te zorgen dat (roterende) diensten eerlijk worden verdeeld onder de mensen die je inplant. Planningsmodellen bevatten ten minste één weekmodel. Weekmodellen groeperen diensten op parameters als begintijd, duur van de dienst of activiteiten. Ze bevatten sets van dagmodellen.<br>Weekmodellen worden aan planningsmodellen toegewezen. Planningsmodellen worden aan medewerkers toegewezen.</td>
    </tr>
    <tr>
      <td>{% link_new Planningskalenders en dagtypes | features/administration/planning-calendar.md %}</td>
      <td>Planningkalenders bevatten dagen met afwijkende openingstijden en personeelsbehoefte (bijvoorbeeld marketingcampagnedagen of nationale feestdagen). Deze speciale dagen worden geconfigureerd met behulp van dagtypes. Zo worden deze dagen automatisch en zonder handmatige ingrepen opgenomen in de planning.<br> Planningskalenders worden toegewezen aan eenheden.</td>
    </tr>
  </tbody>
</table>


## En nu?

Gefeliciteerd! Je bent nu klaar om je {% link_new eerste forecast aan te maken | getting-started/calculate-a-forecast.md %}. Veel succes bij het plannen!
