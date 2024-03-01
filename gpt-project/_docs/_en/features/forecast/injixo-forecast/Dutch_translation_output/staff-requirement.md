---
title: De personeelsbehoefte berekenen
redirect_from:
  - nl/staff-requirement/
redirect_reason: used in intercom forecast product tour
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: De personeelsbehoefte berekenen voor oproepen, chats, e-mail en meer.
related_articles:
  - overwrite_title: Oproepenscript voor multiactiviteiten
    filepath: features/forecast/requirement-scripts/requirement-multiactivity.md
  - overwrite_title: Uitgaande oproepen
    filepath: features/forecast/requirement-scripts/requirement-outbound.md
  - overwrite_title: Constante behoefte
    filepath: features/forecast/requirement-scripts/requirement-constant.md
  - overwrite_title: De personeelsbehoefte bewerken of verwijderen
    filepath: features/scheduling/employee-requirement.md
---

Nadat je een forecast hebt gegenereerd, kun je de personeelsbehoefte berekenen. Je hebt de keuze uit verschillende behoeftescripts en berekeningsmethoden in injixo. Als het nodig is, kun je ook constant personeelsbehoeften bepalen zonder een forecast.

Ben je nog niet zo vertrouwd met injixo Forecast? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Berekeningsmethoden en behoeftescripts

injixo biedt berekeningsmethoden en behoeftescripts.
Kom te weten welk {% link_new behoefte-script of welke berekeningsmethode | best-practices/requirement-scripts.md %} optimaal is voor je specifieke gebruikssituatie.<br>
In de volgende sectie lees je hoe je de [berekeningsmethoden](#berekeningsmethoden-configureren) configureert.<br>
Klik op de volgende links voor instructies over hoe je de vereiste scripts instelt:

- {% link_new Multiactivity-script | features/forecast/requirement-scripts/requirement-multiactivity.md %};

- {% link_new Uitboundscript | features/forecast/requirement-scripts/requirement-outbound.md %}
- {% link_new Constant behoefte script | features/forecast/requirement-scripts/requirement-constant.md %}

## De berekeningsmethoden configureren

De berekeningsmethoden berekenen personeelsplanningsbehoeften op basis van nieuwe data-imports, gewijzigde berekeningsparameters of {% link_new handmatige aanpassingen | features/forecast/injixo-forecast/manual-adjustments.md %}.
Je kunt je berekeningsmethode altijd wijzigen.

1. Selecteer in _Forecast > Workloads_{:.breadcrumbs} een workload.
2. Klik op **Behoefte medewerkers** op _Behoefte bewerken_{:.doc-button}.
3. Selecteer in het vervolgkeuzemenu **Berekeningsmethode** een optie:
   - **Erlang-C**
   - **Chat**
   - **Lineair**
4. Configureer in de sectie **Rekenkundige parameters** de [rekenkundige parameters](#rekenkundige-parameters).
5. Selecteer in de sectie **Gekoppelde eenheid en activiteit** de eenheid en de activiteit waarvoor je de personeelsbehoefte wilt gebruiken.   
  Lees meer over [Het gebruik van personeelsbehoefte voor planningen](#use-staff-requirements-for-scheduling).
6. Klik op _Opslaan_{:.doc-button}.

De grafiek in de sectie **Personeelsbehoefte** toont de berekende personeelsbehoefte.<br> Onder de grafiek kun je de geconfigureerde waarden voor de parameters zien en de totale personeelsbehoefte (in persoon-uren) voor de ingestelde periode.<br> Beweeg de cursor over de grafiek om gedetailleerde informatie te zien over het volume, de AHT, de personeelsbehoefte en handmatige aanpassingen en toegevoegde evenementen per interval.

### Berekeningsparameters

De volgende tabel bevat de parameters die je kunt configureren voor elk berekeningsmethode:

| Parameter                         | Beschrijving                                                                                                                                                                                                                                                                                                           | Instelbaar in Erlang-C | Instelbaar in Chat | Instelbaar in Linear |
| Parameter                         | Beschrijving                                                                                                                                                                                                                                                                                                           | Configureerbaar in Erlang-C | Configureerbaar in Chat | Configureerbaar in Lineair |
| Gewenst serviceniveau              | Percentage van binnenkomende oproepen of chats die binnen de beoogde antwoordtijd moeten worden afgehandeld.                                                                                                                                                                                                                                                                          | Ja | Ja | Nee |
| Gewenste antwoordtijd              | De periode waarin het percentage oproepen of chats wordt gespecificeerd in de targetservicekwaliteitparameter| Yes | Yes | No |
| Krimp                         | Het percentage betaalde werktijd waarin medewerkers niet kunnen werken, bijvoorbeeld door toiletbezoeken, (te laat) komen, ongepland ziekteverlof opnemen of technische problemen. | Ja | Ja | Ja |
| Minimum vereist personeel            | Voer een waarde in om intervallen met lagere personeelsbehoefte te overschrijven.                                                                                                                                                                                                                                                     | Ja | Ja | Ja |
| Maximale bezetting                        | Voer een waarde in om intervallen met lagere behoeftecijfers te overschrijven.                        | Ja | Ja | Ja |
| Gefixeerde gemiddelde afhandeltijd (AHT)        | Voer een waarde in om de AHT-voorspelling te overschrijven.<br>Vink het selectievakje **Toepassen van gefixeerde AHT alleen wanneer geen AHT-waarde is ingevoerd** aan om de gefixeerde AHT-waarde alleen voor periodes zonder AHT-gegevens te gebruiken. Voor de berekening van het personeelsvereiste worden standaard de AHT-waarden uit de prognose gebruikt.                                 | Yes | Yes | Yes |
| Max. sessies                  | Het maximum aantal parallelle chatsessies dat medewerkers gelijktijdig kunnen afhandelen.                                                                                                                                                                                                                                                                                   | Nee | Ja | Nee |
| Overhead                          | AHT-percentage dat een medewerker aan taken moet besteden die ze niet gelijktijdig kunnen uitvoeren, zoals after-call-notes in het CRM-systeem invoeren. Deze parameter wordt niet overwogen als je een 1 invoert in het veld **Gelijktijdige sessies max**.                                                                                                                                          | No | Ja | Nee |

## Behoefte van medewerkers gebruiken voor het plannen

Om een planning op basis van personeelsbehoefte te maken, moet je deze eerst opslaan. Volg de onderstaande stappen om personeelsbehoefte op te slaan.

Je kunt alleen de personeelsbehoeftek
Lees meer over {% link_new forecastversies | features/forecast/injixo-forecast/store-forecast-versions.md %} of over hoe je een {% link_new forecast importeert | features/forecast/injixo-forecast/import-forecast.md %}.

1. Selecteer in _Forecast > Workloads_{:.breadcrumbs} een workload.
2\. Selecteer de periode voor welke je behoefte aan personeel wilt gebruiken.
3. Selecteer in de sectie **Personeelsbehoefte** een forecastversie in het vervolgkeuzemenu aan de linkerzijde.
4. Klik op _Behoefte personeel opslaan_{:.doc-button}.
5. Klik in het venster **Behoefte opslaan** op _Opslaan_{:.doc-button}.

injixo slaat de personeelsbehoefte op voor de eenheid en activiteit die je hebt geselecteerd terwijl je de rekeneenheid configureerde.

> Opmerking
>
> Je kunt de personeelsbehoefte gebruiken voor een ander eenheid. <br> Herhaal de procedure om de [berekeningsmethode te configureren](#berekeningsmethoden-configureren) en selecteer een andere eenheid. Volg vervolgens de procedure om [de personeelsbehoefte te gebruiken voor plannen](#de-personeelsbehoefte-gebruiken-voor-het-plannen).