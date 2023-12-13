---
title: Massa-update
product_label:
  - advanced
  - enterprise
  - classic
---

Gebruik massa-update om configuratiegegevens aan meerdere medewerkers tegelijkertijd toe te kennen.
Je kunt de functionaliteit massa-update gebruiken voor de volgende configuratie-elementen:

- Contracten
- Kwalificaties
- Eenheden
- Groepen
- Dienstenseries
- Planningsmodellen

## Vereisten

Voordat je de functionaliteit massa-update kunt gebruiken, moet je {% link_new je basisconfiguratie instellen | getting-started/set-up-base-configuration.md %}.

## Massa-update starten

> Opmerking
>
> Je kunt een massa-update niet terugdraaien of ongedaan maken. Om een foutieve massa-update te overschrijven, voer je een nieuwe massa-update uit. Je kunt ook de gegevens voor elke medewerker afzonderlijk wijzigen.  

Volg deze stappen om een massa-update te starten:

1. Ga naar _Plan > Configuratie > Medewerkers_{:.breadcrumbs}.
2. Om de medewerkers te selecteren van wie je de configuratiegegevens wilt wijzigen, selecteer je een groep of klik je op het pictogram Medewerkersfilter activeren {% icon employee-filter | icon-only %}.
3. Klik in de actiebalk op het pictogram Massa's bewerken {% icon mass-update | icon-only %}.<br>De pagina Massa's bewerken wordt geopend. 
4. In de sectie **Parameters** selecteer je in het vervolgkeuzemenu **Stamgegevens** het configuratie-element dat je voor meerdere medewerkers tegelijkertijd wilt bewerken.<br>(Optioneel): Gebruik de velden **geldig vanaf** en **geldig tot en met** om te beperken hoe lang een massa-update geldig is.
5. Selecteer een **Actie**.
6. Afhankelijk van je selectie, worden aan de rechterkant de volgende secties weergegeven: **Huidige toekenningen**, **Toekennen** of **Nieuwe geldigheidsperiode**. Selecteer in de secties de elementen die je wilt toevoegen, verwijderen of vervangen.
7. Klik op **OK** om de massa-update te starten.<br>Het venster Jobverwerking wordt geopend.<br>De pagina met het resultaat van je massa-update wordt geopend.

| Vraag                                                                          | Antwoord                                                                                                                                                                                      |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------- |
| Waarom is aan mijn medewerkers een kortere periode toegekend, nadat ik een massa-update heb uitgevoerd?                              | Als je een configuratie-item dat de verwerkingsperiode overschrijdt aan een medewerker toewijst, dan resulteert dat mogelijk in perioden zonder toekenning.<br>Voorbeeld: Een medewerker heeft een contracttoekenning van 1 maart tot 31 mei. Je voert een nieuwe geldigheidsperiode in van 1 maart tot 15 april. Na de massa-update is er geen toekenning meer tussen 16 april en 31 mei.                                                                                                                                           |


