---
title: Een Zendesk-integratie toevoegen
description: Lees hoe je je Zendesk-CRM verbindt met injixo om gegevens te importeren.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Een Zendesk-integratie is een cloudintegratie die contactvolumes voor e-mail, webformulieren, chats, oproepen en sociale mediaberichten uit Zendesk Support en Zendesk Talk importeert. 

De integratie importeert alleen oproepen (maar geen uitgaande gesprekken). De gemiddelde afhandeltijd (AHT) is alleen beschikbaar voor Zendesk Talk.

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Een Zendesk-integratie toevoegen

Maak in je Zendesk-account eerst een API-token aan voor een gebruiker met [admin-toegang](https://support.zendesk.com/hc/en-us/articles/4408843355290-Zendesk-for-Salesforce-integration-Required-profile-permissions).

Volg de onderstaande stappen om een nieuwe Zendesk-integratie aan te maken in injixo:

1. Ga naar _Account > Integraties_{:.breadcrumbs}.
2. Als je al een integratie hebt, klik dan op _Voeg integratie toe_{:.doc-button}.
3. Klik in de **Zendesk**-tegel op **Voeg integratie toe**{:.doc-button}.
4. Geef de nieuwe integratie een unieke naam die naar de gegevensbron verwijst.
5. Voer in de sectie **Gebruikersgegevens** je aanmeldgegevens voor Zendesk in:
   * Voer je volledige Zendesk-domeinnaam met subdomein in, bijvoorbeeld: voorbeeld.zendesk.com.
   * Voer je Zendesk-gebruikersnaam in.
   * Voer je API-token in.
6. Selecteer in de sectie **Configuratie** een groeperingskeuze. Selecteer de optie **IVR (Interactive Voice Response)** of **Telefoonnummer**. Deze keuze bepaalt hoe injixo [de betreffende bronqueues](#queuenamen-voor-zendesk-talk) voor Zendesk Talk-weergaven noemt. Bij de optie IVR wordt gebruik gemaakt van de bestemmingsgroep. Bij de optie Telefoonnummer wordt het ontvangende nummer gebruikt om de naam van de bronqueue te genereren. Een oproep zonder de relevante informatie wordt weergegeven als niet gegroepeerd. Bronqueues voor Zendesk Support zijn niet betroffen.

   > Je kunt de groeperingskeuze niet meer wijzigen zodra de configuratie van de injixo-integratie is opgeslagen.

7. Klik op _Integratie opslaan_{:.doc-button}.

## Zendesk-gegevens in injixo

### Tickets vs. contactgebeurtenissen

Een Zendesk-ticket bevat gewoonlijk meerdere interacties tussen je teamleden en je klanten via verschillende communicatiekanalen.

Elke interactie staat voor een taak die door je teamleden wordt uitgevoerd. Een interactie kan een nieuw ticket zijn of een wijziging aan een bestaand ticket.

Voorbeeld: Een gebruiker maakt een ticket aan door een e-mail te versturen. Het teamlid beantwoordt deze vervolgens en sluit het ticket. Twee dagen later antwoordt de gebruiker op de e-mail van je teamlid, waardoor het ticket opnieuw wordt geopend. In injixo zou dit als twee e-mails worden beschouwd, ook al komen ze binnen op één ticket.

### Weergaven

injixo genereert bronqueues op basis van je Zendesk-weergaven. Na de oorspronkelijke gegevensimport zie je een bronqueue voor elke ondersteunde weergave die je in Zendesk hebt aangemaakt. Als een weergave gebeurtenissen uit verschillende kanalen (zoals chat en e-mail) bevat, dan worden deze in injixo in aparte {% link_new kanalen | features/forecast/injixo-forecast/manage-workloads.md | #queues-en-kanalen %} weergegeven.

Opmerking: Als je nieuwe Zendesk-weergaven toevoegt nadat je de integratie hebt opgeslagen, dan genereert de integratie automatisch nieuwe injixo-bronqueues en de gerelateerde geschiedenis.

### Niet-ondersteunde weergaven

injixo kan voor de meeste weergaven bronqueues aanmaken, maar weergaven die de volgende ticketvelden bevatten worden momenteel niet ondersteund:

- Kantooruren
- SLA
- Kanaal
- Kwalificaties
- Voorwaarden met gebruikerspecifieke waarden (zoals Assignee is (current user))

Als je Zendesk-weergaven hebt met voorwaarden die naar een of meerdere bovenstaande velden verwijzen, negeert injixo deze weergaven. Er worden dan geen queues voor gegenereerd.

### Kanaaltoewijzing tussen Zendesk en injixo.

Een wijziging in een Zendesk-ticket kan in meerdere injixo-kanalen worden geteld.

Voorbeeld: Een e-mail genereert een ticket, dat vervolgens in een e-mailqueue in injixo verschijnt. Als datzelfde ticket in een chatweergave terechtkomt, wordt het in injixo ook in een chatqueue geteld.

| Zendesk-kanaal                           | injixo       |
| ----------------------------------------- | ------------ |
| email                                     | email        |
| mobile                                    | email        |
| web                                       | email        |
| chat                                      | chat         |
| native_messaging                          | chat         |
| sms                                       | social_media |
| any_channel                               | social_media |
| facebook                                  | social_media |
| twitter                                   | social_media |
| sunshine_conversations_facebook_messenger | social_media |
| instagram_dm                              | social_media |
| voice                                     | call         |
| api                                       | case         |
| answer_bot_for_web_widget                 | case         |
| chat_transcript                           | case         |
| mobile_sdk                                | case         |

### Queuenamen voor Zendesk Support

De resulterende naam van de bronqueue voor Zendesk Support-queues volgt de volgende conventie:

"weergavenaam + (injixo-kanaal)"

Voorbeelden:

- Supporttickets (chat)

### Queuenamen voor Zendesk Talk

De naam van de bronqueue voor Zendesk Talk-queues komt volgens de volgende conventie tot stand:

"Calls Inbound For + groeperingskeuze"

Voorbeelden:

- Calls Inbound For +49123456789 (telefoonnummer)
- Calls Inbound For Senior Agents (IVR)
- Calls Inbound Ungrouped
