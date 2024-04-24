---
title: Combinare i metodi di pianificazione
product_label:
  - advanced
  - enterprise
  - classic
description: Combina i diversi metodi di pianificazione per soddisfare le esigenze della tua organizzazione.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/availabilities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-time-pattern-models.md
---

Puoi combinare tutti {% link_new i metodi di pianificazione | features/scheduling/scheduling-methods.md %} in modi diversi per creare pianificazioni che rispondono sia alle esigenze dei dipendenti che a quelle della tua azienda.

Gli esempi seguenti illustrano alcuni casi tipici in cui è possibile combinare i metodi di pianificazione. Puoi anche utilizzare altre combinazioni per soddisfare al meglio le esigenze della tua organizzazione.

## Caso 1: dipendenti con turni flessibili e dipendenti con orari o giorni di lavoro specifici  

In questo caso puoi combinare la pianificazione fissa con turni flessibili alternati oppure con turni totalmente flessibili.

Per pianificare i dipendenti utilizzando questa combinazione, devi prima configurare i dati di configurazione mostrati nella tabella di seguito, e assegnarli ai dipendenti interessati:


| Dipendenti con turni flessibili            | Dipendenti con orari o giorni di lavoro specifici                                                                                                                |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Assegna loro i modelli di pianificazione che vuoi utilizzare. | Crea rotazioni specifiche che definiscono le ore o i giorni in cui dovrebbero lavorare, e lascia vuoto il resto della settimana.<br>Assegna loro la rotazione e i modelli di pianificazione pertinenti.                                    |

Per pianificare i dipendenti, segui questi passaggi:

1. Inserisci le rotazioni.
2. Utilizza la funzionalità **Crea una pianificazione ottimizzata**.<br>injixo pianificherà i turni flessibili alternati e i turni totalmente flessibili per integrare la copertura fornita dalle rotazioni.


## Caso 2: dipendenti con turni alternati e dipendenti con turni flessibili

In questo caso puoi combinare turni flessibili alternati e turni totalmente flessibili.

Per pianificare i dipendenti utilizzando questa combinazione, devi prima assegnare i dati di configurazione ai dipendenti interessati, come mostrato nella tabella di seguito:

| Dipendenti con turni flessibili alternati           | Dipendenti con turni totalmente flessibili                                                                                                                |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Assegna loro modelli di pianificazione del tipo B o D. | Assegna loro modelli di pianificazione del tipo A.                                   |


Utilizza la funzionalità **Crea una pianificazione ottimizzata**.<br>Ai dipendenti con i turni flessibili alternati verrà assegnata la rotazione definita dai loro modelli di pianificazione, e i dipendenti con turni totalmente flessibili copriranno il resto della pianificazione.

## Caso 3: dipendenti con turni alternati e limiti alla disponibilità

Questo caso riguarda i dipendenti che fanno turni flessibili alternati, ma che non sono disponibili in determinati orari, per esempio il mercoledì non possono lavorare oltre le 17:00.

In questo caso puoi combinare disponibilità e turni flessibili alternati.

1. Configura per i dipendenti le {% link_new disponibilità | features/administration/availabilities.md %} che definiscono quando non possono lavorare. In questo esempio, i dipendenti sono disponibili solo il mercoledì fino alle 17:00.
2. Assegna loro i modelli di pianificazione pertinenti.

Nelle settimane in cui lavorano di mattina, i dipendenti saranno pianificati il mercoledì.<br>Nelle settimane in cui lavorano di sera, i dipendenti non saranno pianificati il mercoledì, e saranno pianificati negli altri giorni della settimana.

## Caso 4: dipendenti con turni fissi e limiti specifici alla disponibilità

Questo caso riguarda i dipendenti che fanno turni fissi, ma che hanno una disponibilità limitata in alcuni giorni particolari, per esempio lavorano di notte, o durante il fine settimana, ma solo un fine settimana su due.

In questo caso puoi aggiungere {% link_new modelli di orario del tipo Margine di disponibilità | features/administration/daymodels/daymodel-basics.md | #tipi-di-modelli-di-orario %} alle {% link_new rotazioni | features/administration/shift-sequences.md %} per influire sul risultato della pianificazione di giorni specifici.<br>Vedi i due esempi qui sotto.

Per pianificare i dipendenti in modo che lavorino un fine settimana su due, segui questi passaggi:

1. Crea un modello di orario del tipo Margine di disponibilità con un intervallo di tempo da mezzanotte (0:00) alle 0:01 come blocco.
2. Aggiungi il modello di orario a un fine settimana in una rotazione di 14 giorni, e lascia vuoti tutti gli altri giorni.
3. Assegna la rotazione ai dipendenti interessati.
4. Inserisci la rotazione nella pianificazione.
5. Utilizza la funzionalità **Crea una pianificazione ottimizzata**.

injixo lascia libero un fine settimana su due, e ottimizza gli altri giorni.

Per pianificare i dipendenti in modo che lavorino di notte un fine settimana su due, segui questi passaggi:

1. Crea un modello di orario del tipo Margine di disponibilità con un intervallo di tempo da mezzanotte (0:00) a mezzogiorno (12:00) come blocco.
2. Aggiungi il modello di orario a tutti i giorni di una settimana in una rotazione con 14 giorni, e lascia vuoti tutti gli altri giorni.
3. Assegna la rotazione ai dipendenti interessati.
4. Inserisci la rotazione nella pianificazione.
5. Utilizza la funzionalità **Crea una pianificazione ottimizzata**.

injixo pianifica il turno di notte nelle settimane in cui i dipendenti sono disponibili, seguendo il modello di pianificazione assegnato a ogni dipendente. Per le altre settimane, injixo può pianificare qualsiasi turno che sia compatibile con il modello di pianificazione.
