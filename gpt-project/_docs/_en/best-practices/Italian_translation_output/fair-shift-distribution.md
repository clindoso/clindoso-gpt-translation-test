---
title: a
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: a
gpt_translation: true
---

Indipendentemente dal {% link_new metodo di pianificazione | features/scheduling/scheduling-methods.md %} che scegli, è possibile che alcuni dipendenti ricevano i turni impopolari più spesso di altri a causa della loro disponibilità o della rarità delle loro competenze. Questo può facilmente sfociare in insoddisfazione da parte dei dipendenti, riduzione del morale e aumento del turnover. <!-- GPT translation -->

Questo articolo offre dei consigli pratici che possono aiutarti a distribuire i turni in modo più uniforme ed essere percepito come più equo. <!-- GPT translation -->

## Cicli di turni per una distribuzione uniforme <!-- GPT translation -->

Utilizza le rotazioni per garantire una distribuzione uniforme dei compiti e dei turni. Con le rotazioni, crei delle pianificazioni che si ripetono con una certa regolarità. <!-- GPT translation -->

{{ 1 | image: 'Rotazioni'}} <!-- GPT translation -->

Le rotazioni sono consigliate, specialmente per i turni del fine settimana. Grazie a una rotazione i turni del fine settimana sono distribuiti in modo uniforme tra i dipendenti. I dipendenti possono inoltre prevedere quando lavoreranno nel fine settimana. <!-- GPT translation -->

### Combinare le rotazioni con l’ottimizzazione delle pianificazioni <!-- GPT translation -->

Se vuoi utilizzare l’ottimizzazione delle pianificazioni, ma vuoi anche distribuire in modo uniforme alcuni turni, è possibile combinare l’utilizzo delle rotazioni con l’ottimizzazione delle pianificazioni. <!-- GPT translation -->

Per esempio, se vuoi che i turni del fine settimana si alternino, procedi come di seguito: <!-- GPT translation -->

1. Crea un'{% link_new disponibilità modello di giorni | features/administration/availabilities.md %} che consiste in un blocco di un minuto che rende il giorno completamente non disponibile. <!-- GPT translation -->
2. Inserisci questa disponibilità modello di giorni in una rotazione quattordicale, alternando i fine settimana. Lascia vuoti tutti gli altri giorni. <!-- GPT translation -->

Prima di avviare l’ottimizzazione della pianificazione, puoi inserire la rotazione nella pianificazione. <!-- GPT translation -->

- Nelle settimane in cui il periodo di indisponibilità per confini sarà attivo, il dipendente non lavorerà nel fine settimana e la sua pianificazione durante la settimana verrà ottimizzata. <!-- GPT translation -->
- Nelle settimane in cui il periodo di indisponibilità per confini sarà attivo, il dipendente non lavorerà nel fine settimana e la sua pianificazione durante la settimana verrà ottimizzata. <!-- GPT translation -->

## Creare un modello di pianificazione <!-- TM 64 -->

Se vuoi ottimizzare i turni durante l’applicazione di modelli di pianificazione alternati, utilizza i _modelli di pianificazione_{:.menu-item}. <!-- GPT translation -->

I modelli di pianificazione ti consentono di pianificare i turni dei dipendenti in modo che durante le settimane si alternino turni mattutini, turni pomeridiani e turni serali (per esempio). Ogni settimana, i turni che possono essere svolti sono scelti da un elenco di **modelli di orario** che specifichi in un **modello settimanale**. L’ottimizzazione viene vincolata dal **tipo** che specifichi nel modello di pianificazione — _Rotazione flessibile_, _Rotazione fissa_, e così via. <!-- GPT translation -->

## Turni impopolari: Giorni atipici <!-- GPT translation -->

Se non vuoi assegnare turni o compiti impopolari per intere settimane, ma vuoi alternarli ogni settimana, puoi utilizzare i _modelli settimanali con giorni atipici_{:.menu-item} e dei **giorni con orari diversi dai soliti**. Per fare questo: <!-- GPT translation -->

1. Crea un **modello settimanale** con i tuoi turni standard. <!-- GPT translation -->
   {{ 4 | image: 'week time pattern with day models for standard shifts', '50%' }} <!-- GPT translation -->
2. Nella pianificazione settimanale, inserisci 1 nella casella **Numero massimo di giorni atipici per settimana** per definire quante pianificazioni disdicevoli un dipendente può avere in una settimana. <!-- GPT translation -->
   {{ 3 | image: 'Modello di pianificazione settimanale', '50%' }} <!-- GPT translation -->
3. Crea un secondo **modello settimanale** che includa i turni impopolari. <!-- GPT translation -->
4. In un modello di pianificazione, aggiungi il modello settimanale con i turni standard. <!-- GPT translation -->
   {{ 5 | image: 'work time pattern model with week time pattern(s) for standard shifts', '50%' }} <!-- GPT translation -->
5. Seleziona dal menu a tendina **Modello settimanale - Giorni atipici** il modello settimanale che include i turni impopolari. <!-- GPT translation -->
   {{ 2 | image: 'work time pattern model', '50%' }} <!-- GPT translation -->

## Offerta dei turni <!-- TM 65 -->

A breve termine, nel sistema di offerte dei turni potrebbe verificarsi che i dipendenti non ottengano i turni per i quali avevano espresso una preferenza. Per migliorare l'equità puoi scegliere di dare la precedenza a certi insiemi. In questo modo, a lungo termine, si otterrà una soluzione simile a quella ottenibile con il lancio a sorte, anche se non esattamente identica. <!-- GPT translation -->

Per fare ciò, assegna i dipendenti a insiemi diversi e alterna gli insiemi a partire dal primo ciclo di pianificazione. <!-- GPT translation -->

Esempio: <!-- TM 100 -->

- A giugno, la selezione A inizia con l’offerta, seguita dai gruppi B e C. <!-- GPT translation -->
- A luglio, la selezione B inizia con l’offerta, seguita da C e infine da A. <!-- GPT translation -->
- Ad agosto, il gruppo C inizia con l’offerta, seguito da A e infine da B. <!-- GPT translation -->
- etc. <!-- GPT translation -->