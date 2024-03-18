---
title: planningskalenders configureren <!-- GPT translation -->
description: Configureer planningscalenders om je standaardkantooruren automatisch aan te passen op dagen met afwijkende kantooruren. <!-- GPT translation -->
product_label:
- advanced
- enterprise
- classic
related_articles:
- overwrite_title: Add title for untranslated source
  filepath: features/administration/day-types.md
- overwrite_title: Add title for untranslated source
  filepath: features/administration/create-and-manage-planning-units.md
- overwrite_title: Add title for untranslated source
  filepath: best-practices/scheduling-public-holidays.md
redirect_from:
- "/planning-calendar/"
redirect_reason: Updated filename on 13 March 2024
---

In een planningskalender kun je {% link_new dagtypes | features/administration/day-types.md %} gebruiken om dagen met bijzondere openingstijden of personeelsbehoefte te markeren, denk aan campagnedagen, feestdagen, en dergelijke. Zo weet je zeker dat je bij het plannen ook met deze dagen rekening houdt. Als je een dagtype aan de planningskalender toevoegt, worden de standaard openingstijden voor die dag overschreven. Je kunt verschillende planningskalenders voor verschillende eenheden of regio's aanmaken, bijvoorbeeld als ze verschillende openingstijden of feestdagen hebben. <!-- GPT translation -->

## Een planningskalender configureren <!-- GPT translation -->

Voorwaarde: Je hebt de betreffende aangepaste {% link_new dagtypes | features/administration/day-types.md %} aangemaakt die je aan je planningskalender wilt toevoegen. <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Planningskalender_{:.breadcrumbs}. <!-- GPT translation -->
2. Klik in de actiebalk op het pictogram Nieuw {% icon item-add | icon-only %}. <!-- GPT translation -->
3. De planningskalender configureren: <!-- GPT translation -->
    - **Jaar**: Geef het jaar op waarvoor je de planningskalender wilt gebruiken.<br>Om een planningskalender aan te maken die meer dan een jaar omvat, bijvoorbeeld, als je roosters aanmaakt die meerdere jaren beslaan, gebruik dan _<_{:.doc-button} en _>_{:.doc-button} om naar een verstreken of toekomstig jaar te navigeren. Configureer vervolgens de kalender per jaar. <!-- GPT translation -->
    - **Kalendar sjabloon**: Selecteer de regio en klik op _Toepassen_{:.doc-button}.<br>De planningskalendar wordt automatisch gevuld met de nationale vrije dagen van de geselecteerde regio of het geselecteerde land.<br>Als je meerdere regio's aan dezelfde kalendar wilt toevoegen, herhaal deze stap dan voor elke regio die je wilt toevoegen.<br>Opmerking: Elk vakje in de kalendar kan alleen een nationale feestdag bevatten. Als je een sjabloon selecteert waarin een vrije dag op dezelfde datum voorkomt als een eerder geselecteerde sjabloon, dan worden vakjes die al een invoer bevatten overschreven. <!-- GPT translation -->
    - **Dagtype toevoegen**: Selecteer een aangepast dagtype in het vervolgkeuzemenu en klik vervolgens op elke kalendercel waar je het dagtype aan wilt toevoegen.<br>Opmerking: Je kunt slechts één dagtype per dag toewijzen. Als je een cel selecteert die al een dagtype bevat, dan wordt de waarde overschreven. Als je meerdere aangepaste dagtypen in één planningskalender wilt opnemen, herhaal deze stap dan voor elk dagtype dat je wilt toevoegen. <!-- GPT translation -->
4. Klik in de actiebalk op het pictogram Opslaan als _![save as button](/assets/img/common/saveas.gif)_{:.doc-button-icon}. <!-- GPT translation -->
5. Typ een naam voor de kalender in het bevestigingsvenster en klik op  _OK_{:.doc-button}. <!-- GPT translation -->

## Dagtypes uit de planningskalender verwijderen <!-- GPT translation -->

Indien je eenheden op bepaalde dagen gesloten zijn en je personeel geen beloning ontvangt voor deze dagen, zorg er dan voor dat deze dagen niet in je planningskalender zijn opgenomen als {% link_new feestdagtypes met rouwmodus | features/administration/day-types.md | #feestdagtype %}. Als je deze dagtypes niet uit je planningskalender verwijdert, dan vermindert injixo de nominale werktijd voor die week en worden je medewerkers op basis hiervan ingepland voor minder uren. Lees meer over hoe je {% link_new feestdagen plant | best-practices/scheduling-public-holidays.md | #gesloten-gebruik-de-planningskalender %}. <!-- GPT translation -->

Volg deze stappen om dagtypes uit de planningskalender te verwijderen: <!-- GPT translation -->
1. Ga naar _Plan > Configuratie > Planningskalender_{:.breadcrumbs}. <!-- Repetition of GPT translation -->
2. Klik op **Verwijderen** om afzonderlijke dagtypen te verwijderen. <!-- GPT translation -->
3. Klik op elke cel in de planningskalender die je dagtype wilt verwijderen. <!-- GPT translation -->
4. (Optioneel) Om alle vermeldingen in de kalender voor het jaar dat je momenteel hebt geselecteerd te verwijderen, klik op **Jaar wissen**{:.doc-button}. <!-- GPT translation -->
5. (Optioneel) Klik op _Alles verwijderen_{:.doc-button} om alle items in de kalender over de hele periode te verwijderen. <!-- GPT translation -->
5. Klik op het pictogram Opslaan _![save button](/assets/img/common/save.gif)_{:.doc-button-icon}. <!-- GPT translation -->


## Een bestaande planningskalender bewerken <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Planningskalender_{:.breadcrumbs}. <!-- Repetition of GPT translation -->
2. Selecteer in de sectie **Configuratie** in het menu de gewenste kalender. Klik vervolgens op **Een kopie opslaan** _![save as button](/assets/img/common/saveas.gif)_{:.doc-button-icon} in de actiebalk om het bedrijfsrooster te kopiëren voordat je het gaat bewerken. Zo kun je bijvoorbeeld hetzelfde sjabloon en dezelfde dagtypes, maar voor een ander jaar gebruiken. <!-- GPT translation -->
3. Als je alles hebt gewijzigd, klik je op het pictogram Opslaan _![save button](/assets/img/common/save.gif)_{:.doc-button-icon}. <!-- GPT translation -->

## Een planningskalender gebruiken voor het planningsproces <!-- GPT translation -->

Volg de volgende stappen om een planningskalender te gebruiken voor roosteren: <!-- GPT translation -->

1. Ga naar _Plan > Configuratie > Eenheden_{:.breadcrumbs}. <!-- GPT translation -->
2. Selecteer de eenheid waaraan je de planningskalender wilt toewijzen. <!-- GPT translation -->
2. Klik in de sectie **Planningkalender** op het pictogram Nieuwe toevoegen {% icon item-add | icon-only %}. <!-- GPT translation -->
3. In het **venster Planning Agenda** selecteer je een planningagenda.<br>Je kunt slechts één kalender selecteren die meerdere jaren beslaat, wanneer je bijvoorbeeld een planning aanmaakt die meerdere jaren beslaat. Wanneer je voor het toekennen van verschillende planningagenda's per jaar kiest, selecteer dan een voor een en bepaal met de velden **Geldig vanaf** en **Geldig tot** de periode waarvoor elke agenda moet gelden. Planningagenda's die slechts voor één jaar gelden, werken alleen voor oudere éénjaarsplanningen. <!-- GPT translation -->
4. Klik op _OK_{:.doc-button} <!-- GPT translation -->

> Opmerking <!-- TM 100 -->
> <!-- TM 100 -->
> Als je eenheden met ondergeschikte eenheden hebt, dan wordt de planningskalender niet automatisch voor de ondergeschikte eenheden overgenomen. Wijs de planningskalender zo nodig handmatig toe aan elke ondergeschikte eenheid. <!-- GPT translation -->