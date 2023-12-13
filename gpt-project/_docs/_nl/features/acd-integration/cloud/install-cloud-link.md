---
title: injixo Cloud Link installeren
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Installeer de injixo Cloud Link-client om gegevens naar injixo te importeren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Heb je nog weinig ervaring met integraties? Maak je dan eerst vertrouwd met de {% link_new basisprincipes | features/acd-integration/cloud/how-integrations-work.md %}.

## Wat is injixo Cloud Link?

injixo Cloud Link is clientsoftware die nodig is voor de configuratie van on-premise-integraties. injixo Cloud Link importeert in regelmatige afstanden gegevens in injixo. Je kunt injixo Cloud Link ook installeren als je je CSV-integraties zo configureert, dat ze regelmatig nieuwe CSV-bestanden uit een map importeren.

De installatiemap van de client bevat:

- het uitvoerbare injixo-cloud-link-bestand.
- een of meerdere injixo-cloud-link.*.log-bestanden.
- het injixo-cloud-link.toml-configuratiebestand.
- een map voor licenties met licenties voor de open-source-bibliotheek.

## Vereisten

- Windows: injixo Cloud Link draait op Windows 10 en hoger en op Windows Server 2016 en hoger. <!-- what about Linux -->
- Linux: Het unixODBC-pakket moet worden geïnstalleerd.
- Firewall/Proxy: Poort 443 moet open zijn voor uitgaand verkeer. injixo Cloud Link gebruikt TLS-versleuteling met TCP via poort 443.

Opmerking: On-premise-integraties hebben toegang tot een lokaal systeem om gegevens te extraheren, zoals een ACD of CRM. Afhankelijk van het type database moet je hiervoor een databasestuurprogramma installeren.

## injixo Cloud Link installeren

Als je een {% link_new on-premise-integratie | features/acd-integration/cloud/add-on-premise-integration.md %}, {% link_new een CSV-integratie | features/acd-integration/cloud/add-csv-integration.md %} of {% link_new een database-integratie | features/acd-integration/cloud/add-database-integration.md %} toevoegt, dan vind je in de sectie **injixo Cloud Link** links om de clientinstaller (voor Windows) of het archief (voor Linux) te downloaden.

### Een Windows-service installeren

Installeer de eerste service via de Windows-client-installer:

1. Klik op **Download voor Windows 64-bit** en voer de installer uit.
2. Klik op **Next**.
3. (Optioneel) Wijzig de installatiemap.
4. Klik op **Next** en vervolgens op **Install**.  
   In een consolevenster wordt een PIN weergegeven die slechts 5 minuten geldig is.  
   Volg de instructies in het consolevenster om [Cloud Link met je integratie te verbinden](#cloud-link-met-je-integratie-verbinden).
5. Klik in de installer op **Finish**.  
   De installer maakt de Windows-service **injixo Cloud Link** aan.

### Meerdere Windows-services installeren

Je kunt maximaal acht aanvullende services installeren voor afzonderlijke integraties. Installeer services in afzonderlijke mappen om te voorkomen dat bestaande services worden overschreven.

Om een tweede Cloud Link-service op Windows te installeren, voeg je een nieuwe integratie toe en volg je de volgende stappen:

1. Klik op **Download voor Windows 64-bit**.
2. Open een Windows-opdrachtprompt (cmd).
3. Voer voor een tweede service de volgende opdracht uit:

   ```
   msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS=":instance.1"
   ```

   > Verhoog het nummer dat in de TRANSFORMS-parameter na 'instance' volgt telkens wanneer je een volgende service installeert.
   >
   > Zo vul je voor de derde service `":instance.2"` in en voor de vierde `":instance.3"`, enzovoort.
  
4. Volg de instructies in de installatieprocedure.  
   De installer stelt een nieuwe standaard installatiemap voor die de instance bevat, bijvoorbeeld: (Instance 1).  
   Tip: Om aan te geven bij welke integratie de installatie hoort, kun je de ACD en gegevens van het importtype toevoegen, bijvoorbeeld: (ACD - agent import) aan de standaard installatiemap.  
   De nieuwe map en de nieuwe Windows-service met de naam injixo Cloud Link (Instance {id}) zijn nu zichtbaar.

### Een Linux-service installeren

Installeer de eerste service op basis van het volgende voorbeeld:

1. Klik op **Download voor Linux 64-bit** en kopieer het archief naar een installatiemap naar keuze.
2. Open een terminal.
3. Installeer de injixo Cloud Link-service:  
   `sudo ./injixo-cloud-link service install`
4. Start de geïnstalleerde service:  
   `sudo ./injixo-cloud-link service start`
5. Geef een PIN weer methet commando:  
   `sudo ./injixo-cloud-link pin`  
   In een consolevenster wordt een PIN weergegeven die slechts 5 minuten geldig is.  
   Volg de instructies in het consolevenster om [Cloud Link met je integratie te verbinden](#cloud-link-met-je-integratie-verbinden).

### Meerdere Linux-services installeren

Je kunt meerdere services voor verschillende integraties installeren. Om te voorkomen dat eerder geïnstalleerde services worden onderschreven, is het van belang dat je verschillende mappen gebruikt.

Om meer services op Linux te installeren, voeg je een nieuwe integratie toe en ga je als volgt verder:

1. Maak een nieuwe map aan en kopieer de bestanden uit de originele installatiemap.
2. Open het bestand injixo-cloud-link.toml.
3. Verander de waarde voor **naam** in de sectie **[app]** in een nieuwe ID:

   ```
   [app]
naam = "com.injixo.cloud-link.instance.1"
   ```

4. Installeer en start de nieuwe service vanuit de nieuwe map, zoals hierboven beschreven.

## Cloud Link met je integratie verbinden

De Cloud Link-installatie geeft het volgende bericht weer, inclusief PIN:

```
** Before you are able to run the client,
** link it to your injixo account:
**  1) Log in to injixo.com
**  2) Visit https://www.injixo.com/account/integrations
**  3) Select an integration you want to connect the client to
**  4) Enter your pin: 424242 (expires in 5 minutes)
```

1. Ga in je browser terug naar de pagina **Voeg een nieuwe integratie toe** in je browser.
2. Voer in de sectie **injixo Cloud Link** je PIN in het zescijferige invoerveld **PIN die tijdens de installatie wordt weergegeven** in.
3. Klik op _Verbinden_{:.doc-button}.
   Cloud Link maakt verbinding met injixo. Je kunt doorgaan met het instellen van je {% link_new on-premise integratie | features/acd-integration/cloud/add-on-premise-integration.md %} of {% link_new CSV-integratie | features/acd-integration/cloud/add-csv-integration.md %}.

## Verbinding maken via een proxyserver

Om verbinding te maken via een proxyserver, dien je de hostnaam of het IP-adres van de proxy toe te voegen aan de omgevingsvariabele van de **https_proxy**:

- Windows: Voer de omgevingsvariabele toe aan de sectie **Systeemvariabelen**. Als services niet worden uitgevoerd met het LocalSystem-account, configureer dan een gebruikersvariabele.
- Linux: Stel in /etc/environment or in /etc/profile.d de omgevingsvariabele in.

Voorbeeld: `https_proxy=http://your.proxy.example`

Indien nodig kun je het poortnummer (indien niet 80) en gebruikersgegevens voor authenticatie toevoegen:

Voorbeeld: `https_proxy=http://username:password@your.proxy.example:8080`

## IP-adressen van het doel delen <!-- rethink the name -->

Deel de volgende URL's, zodat injixo Cloud Link verbinding kan maken met de cloudservers van injixo.

- injixo-*.s3-eu-west-1.amazonaws.com
- www.injixo.com

Het is niet mogelijk om één IP-adres te delen. De implementatie- en updateprocessen veranderen periodiek de IP-adressen van de servers. Overweeg om injixoCloud Link ook in de DMZ te installeren. Als de verbinding met de server niet werkt, dan worden in het logbestand [Windows socket-foutmeldingen](https://docs.microsoft.com/en-us/windows/win32/winsock/windows-sockets-error-codes-2) weergegeven.

## Loggen

injixo Cloud Link roteert logbestanden dagelijks en na een herstart, maar verwijdert geen logbestanden. De actuele logbestanden bevinden zich in injixo-cloud-link.log. Geroteerde logbestanden hebben de rotatiedatum in hun bestandsnaam. Je dient je eigen regelmatige verwijderprocedure in te stellen, of ze handmatig te verwijderen.

### Uitgebreide logboekregistratie activeren

Voor database-integraties ondersteunt injixo Cloud Link een uitgebreide logboekregistratiemodus. Indien deze is geactiveerd, geeft het logbestand het totale aantal opgehaalde rijen en de eerste tien rijen met gegevens voor elke aanvraag weer.

Je kunt uitgebreide logboekregistratie als volgt uitschakelen:

1. injixo Cloud Link uitschakelen.
2. Open het bestand injixo-cloud-link.toml in de installatiemap.
3. In de sectie **[app]** stel je **verbose** in op 'true'

   ```
   [app]
verbose = true
   ```

4. Sla het bestand op en start injixo Cloud Link opnieuw op.

## Importmap configureren

injixo uploadt Cloud Link-bestanden die zijn opgeslagen standaard in zijn installatiemap. Voor CSV-integraties kun je als volgt een aangepaste importmap instellen:

1. injixo Cloud Link uitschakelen.
2. Open het bestand injixo-cloud-link.toml in de installatiemap.
3. Stel in de sectie **[app]** de waarde voor **importDirectory** in op je importmap.
   - Gebruik relatieve of absolute paden.
   - Escape backslashes met een tweede backslash.
4. Sla het bestand op en start injixo Cloud Link opnieuw op.

## Veelgestelde vragen

<style>
table th:first-of-type {
    width: 25%;
}
table th:nth-of-type(2) {
    width: 75%;
}
</style>

| Vraag                                                                        | Antwoord                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hoe krijg ik een nieuwe PIN als de oude is verlopen?                              | Start injixo Cloud Link opnieuw op. Voer de nieuwe PIN uit het logbestand in het zescijferige invoerveld in de sectie **injixo Cloud Link** op de configuratiepagina in.                                                                                                                                                                                                                                                      |
| Hoe verwijder ik Cloud Link uit mijn systeem?                                      | 1\. Voer de injixo Cloud Link-installer nogmaals uit of ga naar _Programma's > Programma's en onderdelen_{:.breadcrumbs} in Windows.<br>2\. Klink met je rechtermuisknop op **injixo Cloud Link** in de lijst en selecteer **Verwijderen** of **Verwijderen/wijzigen**.<br>3\. Volg de instructies op het scherm.<br><br>Om dit op andere locaties te verwijderen, ga je naar _Programma's > Programma's en onderdelen_{:.breadcrumbs} in Windows en volg je de stappen 2 en 3. |
| Hoe verplaats ik injixo Cloud Link naar een nieuwe server?                                | 1\. Klik op het pictogram Bewerken {% icon pencil | icon-only %} rechts naast een integratie om het te bewerken.<br>2\. Klik op **Een nieuwe installatie met injixo Cloud Link verbinden**.<br>3\. Download injixo Cloud Link indien nodig opnieuw en installeer de software op de nieuwe server.                                                                                                                                                                          |
| Hoe kan ik de integratie voor een bestaande injixo Cloud Link-installatie wijzigen? | 1\. Ga naar de installatiemap en kopieer de PIN uit het logbestand.<br>2\. Verwijder de bestaande integratie en maak een nieuwe integratie aan.<br>3\. Verbind je actieve Cloud Link met de nieuwe integratie. Voer hiervoor de PIN in tijdens het configuratieproces voor de nieuwe integratie.                                                                                                               |
