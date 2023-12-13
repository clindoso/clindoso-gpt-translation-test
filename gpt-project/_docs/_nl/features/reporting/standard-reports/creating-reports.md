---
title: Rapporten aanmaken
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Standaard rapporten maken in HTML- of PDF-formaat met verschillende parameters.
promote-service: enhanced-reporting
toc: false
related_articles:
  - overwrite_title: Rapporten per e-mail verzenden
    filepath: features/reporting/standard-reports/email-reports.md
  - overwrite_title: Rapporten per e-mail verzenden
    filepath: features/reporting/standard-reports/planning-unit-reports.md
  - overwrite_title: Rapporten per e-mail verzenden
    filepath: features/reporting/standard-reports/employee-reports.md
---

In dit artikel lees je:
- hoe je rapporten maakt met verschillende parameters en filters
- hoe tijdzones in rapporten worden weergegeven.

Rapporten bevatten verschillende gegevens zoals ingeplande diensten op verschillende niveaus en configuratiegegevens. Lees meer over {% link_new rapporten over eenheden | features/reporting/standard-reports/planning-unit-reports.md %} en {% link_new rapporten over medewerkers | features/reporting/standard-reports/employee-reports.md %}. Je kunt rapporten maken in HTML- en PDF-formaat.

> Een aantal rapporten zijn gebaseerd op groepen. Deze rapporten bevatten alleen gegevens als je minimaal één {% link_new groep | features/administration/selections.md %} toevoegt aan je medewerkers. 

## Rapporten maken

1. Ga naar *WFM > Controle > Reports*{:.breadcrumbs}.
2. Selecteer een **Startdatum** en een **Einddatum**.

3. Gebruik het **Filter** om de gegevens te selecteren die je in je rapport wilt opnemen.

    - **Via velden**: Selecteer een **Eenheid**, **Contract** of **Groep** om het aantal medewerkers in de lijst te beperken. Om meerdere items te selecteren, houd je **CTRL** of **Shift** ingedrukt terwijl je klikt.

        {{ 2 | image: 'Via velden', '90%' }}

    - **Medewerkersfilter**: Selecteer een {% link_new medewerkersfilter | features/administration/employee-filter.md %} om een aangepaste medewerkerslijst aan te maken, bijvoorbeeld op basis van skills. Klik op **Filtereditor** om een nieuw filter aan te maken.

      <br>Vink het selectievakje **Filterperiode hetzelfde als rapportperiode** aan om de start- en einddatum in de rapport-gebruikersinterface te overschrijven.  

      {{ 3 | image: 'Medewerkersfilter', '60%' }}  

      Medewerkersfilters zijn niet beschikbaar in injixo Essential WFM.

4. Klik op *Gebruiken*{:.doc-button}.

5. (Optioneel) Selecteer in de sectie **Medewerkers** afzonderlijke **Medewerkers**.

    {{ 5 | image: 'Sectie medewerkers', '60%' }}

6. In de sectie **Parameters** kun je:
    - het **Niveau** selecteren waaruit je gegevens uit wilt halen. 
    - het **Formaat** voor de gegevensuitvoer instellen (PDF of HTML).
    - ervoor kiezen om {% link_new rapporten per e-mail naar bepaalde gebruikers te verzenden | features/reporting/standard-reports/email-reports.md %}.
    - namen en persoonsnummers van medewerkers anonimiseren

    {{ 4 | image: 'Rapport parameters', '30%' }}

7. Selecteer een rapport in de sectie **rapporten over eenheden** of **rapporten over medewerkers** aan de rechterkant.

    {{ 6 | image: 'Lijst van rapporten met secties', '50%' }}

    <br>
    De documentpictogrammen naast de rapportnamen laten zien voor welke periode je een rapport kunt aanmaken:
    - _![pictogram met een enkel bestand](/assets/img/common/report-icon-single-file.png)_{:.doc-button-icon}: periode van maximaal een maand
    - _![pictogram met meerdere bestanden](/assets/img/common/report-icon-multiple-files.png)_{:.doc-button-icon}: periode van maximaal een jaar 

Er wordt een JobProcessor-venster geopend. Het gewenste rapport wordt gemaakt en weergegeven.

Je kunt meerdere rapporten maken met dezelfde parameters. Als je een filter of datum wijzigt, dan klik je op *Gebruiken*{:.doc-button}.

## Tijdzones in rapporten

De tijden in een rapport worden weergegeven in de lokale tijd van de eenheid. In de rapportkoptekst wordt het tijdsverschil tussen de tijdzone van de eenheid en UTC, en de tijdzone van de eenheid en die van de lokale gebruiker weergegeven.

Voorbeeld: Een medewerker in New York begint om 8:30 uur 's morgens met zijn dienst. In een rapport wordt de lokale tijd in Manchester (Verenigd Koninkrijk) weergegeven, de locatie van de eenheid.  Het tijdsverschil bedraagt +05:00 uur. De medewerker moet dit tijdsverschil van de weergegeven tijd aftrekken om te weten wanneer de dienst begint. In dit geval begint de dienst om 3:30 uur lokale tijd in New York.
