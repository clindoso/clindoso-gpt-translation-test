---
title: Creare i modelli di pianificazione
product_label:
  - advanced
  - enterprise
  - classic
description: Utilizza i modelli di pianificazione nell’ottimizzazione della pianificazione per evitare che ai dipendenti vengano assegnati i turni in modo casuale.
related_articles:
  - overwrite_title: Ottimizzare la pianificazione
    filepath: features/scheduling/scheduling-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/scheduling-split-shifts.md
---

Un modello di pianificazione è composto da [modelli settimanali](#creare-un-modello-settimanale) e definisce il modo in cui i {% link_new modelli di orario | features/administration/daymodels/daymodel-basics.md %} vengono assegnati ai dipendenti.

L’immagine seguente mostra la struttura dei modelli di orario e dei modelli settimanali all’interno di un modello di pianificazione.

{{ 1 | image: 'Struttura di un modello di pianificazione' }}

I modelli di pianificazione ti permettono di creare degli schemi di turni che si ripetono e di stabilire dei vincoli per la pianificazione per la funzionalità **Crea una pianificazione ottimizzata**.<br>
I modelli di pianificazione offrono i seguenti vantaggi:

- Definiscono i modelli di orario che possono essere utilizzati per pianificare un dipendente.
- Fanno sì che i dipendenti non ricevano turni in combinazioni che sembrano casuali.
- Definiscono l’ora di inizio dei turni.
- Stabiliscono un ordine per l’assegnazione dei modelli di orario.

In alternativa ai modelli di pianificazione, puoi utilizzare le rotazioni o configurare le {% link_new disponibilità | features/administration/availabilities.md %} per i dipendenti.

## Prerequisiti

Per poter utilizzare i modelli di pianificazione, assicurati che le seguenti condizioni siano soddisfatte:
- Hai creato i {% link_new modelli di orario | features/administration/daymodels/daymodel-creation.md %} e i [modelli settimanali](#creare-un-modello-settimanale), e hai assegnato i modelli di orario ai modelli settimanali.
- Ogni modello di pianificazione contiene almeno un modello settimanale.
- Ogni modello settimanale contiene almeno un {% link_new modello di orario | features/administration/daymodels/daymodel-basics.md %}.
- Hai assegnato i modelli di pianificazione ai dipendenti.

## Creare un modello settimanale

Un modello settimanale è un gruppo di modelli di orario. Puoi raggruppare i modelli di orario in base a qualsiasi criterio, per esempio la durata dei turni, le attività coinvolte, l’ora di inizio, etc.<br>

Puoi utilizzare i modelli settimanali soltanto come parte di un modello di pianificazione. Per una settimana lavorativa, injixo pianificherà i dipendenti in base ai modelli di orario inclusi nel modello settimanale. In questo modo puoi far sì che i dipendenti abbiano orari di lavoro più equi e più uniformi.

Per creare un modello settimanale, segui questi passaggi:

1. Vai su _Plan > Configurazione > Modelli settimanali_{:.breadcrumbs}.
2. Clicca sull’icona Nuovo {% icon item-add | icon-only %} in alto a sinistra.
    Si aprirà un pannello di configurazione a destra.
3. Configura i parametri del modello settimanale:<br>
  **Nome**: inserisci un nome unico (massimo 50 caratteri).<br>
  **Abbreviazione**: inserisci il nome o una sua versione più breve (massimo 25 caratteri).<br>
  **Colore**: il colore ti permette di identificare più facilmente il modello settimanale nell’elenco.<br>
  **N° max. di giorni atipici a settimana**: i [giorni atipici](#giorni-atipici) permettono a injixo di violare le regole del modello di pianificazione per rispondere meglio al fabbisogno di personale.
4. Clicca su _OK_{:.doc-button}.

Adesso puoi aggiungere i modelli di orario al modello settimanale.

### Aggiungere modelli di orario a un modello settimanale

1. Nel pannello di configurazione del modello settimanale, vai alla sezione **Modelli di orario** e clicca sull’icona Aggiungi {% icon item-add | icon-only %}.
2. Seleziona dall’elenco uno o più modelli di orario.
3. Clicca su _OK_{:.doc-button}.

È possibile aggiungere {% link_new sia modelli di orario fissi che modelli di orario variabili | features/administration/daymodels/daymodel-basics.md | #tipi-di-modelli-di-orario %} a un modello settimanale. Se utilizzi dei modelli di orario variabili, la funzionalità **Crea una pianificazione ottimizzata** può stabilire l’ora ottimale di inizio dei turni che rispetti i vincoli definiti dal modello di orario.

> Nota
>
> injixo può pianificare soltanto i modelli di orario che sono assegnati all’unità di pianificazione alla quale il dipendente è assegnato. Se hai {% link_new limitato i modelli di orario | features/administration/create-and-manage-planning-units.md | #limitare-i-modelli-di-orario %} per la tua unità di pianificazione, i modelli di orario che ti aspetteresti in base al modello di pianificazione potrebbero non essere utilizzati.
>
> injixo può sostituire le attività sostituibili con attività pianificabili all’interno di un turno. Perché questo accada, devi utilizzare modelli di orario variabili per ogni durata di turno richiesta da un contratto, e utilizzare l’attività di sistema Presente (ID: 1) come {% link_new attività di base | features/administration/daymodels/daymodel-basics.md | #attività-di-base-e-durata-del-turno %}. Non definire modelli di orario per ogni singola attività.

## Creare un modello di pianificazione

1. Vai su _Plan > Configurazione > Modelli di pianificazione_{:.breadcrumbs}.
2. Clicca sull’icona Nuovo {% icon item-add | icon-only %} nella barra delle azioni.
3. Configura i parametri del modello di pianificazione:<br>
  **Nome**: inserisci un nome unico (massimo 50 caratteri).<br>
  **Abbreviazione**: inserisci il nome o una sua versione più breve (massimo 25 caratteri).<br>
  **Colore**: il colore ti permette di identificare più facilmente il modello di pianificazione nell’elenco.<br>
  **Tipo**: il [tipo](#tipi-di-modelli-di-pianificazione) determina il modo in cui injixo utilizza il modello di pianificazione.<br>
  **Modello settimanale per giorni atipici**: seleziona il modello settimanale che dovrà essere pianificato per i [giorni atipici](#giorni-atipici).
4. Clicca su _OK_{:.doc-button}.

Adesso puoi aggiungere i modelli settimanali al modello di pianificazione.

### Aggiungere modelli settimanali a un modello di pianificazione

1. Nel pannello di configurazione del modello di pianificazione, clicca sull’icona Aggiungi {% icon item-add | icon-only %} nella sezione **Modelli settimanali**.
2. Scegli un **Modello settimanale** dall’elenco.
3. Imposta una **Posizione**.<br>
  Se aggiungi più modelli settimanali, clicca sulle frecce Sposta in alto {% icon down-arrow-blue | icon-only %} e Sposta in basso {% icon up-arrow-blue | icon-only %} per modificare la posizione.
4. Clicca su _OK_{:.doc-button}.

### Posizione

La posizione del modello settimanale all’interno del modello di pianificazione è rilevante quando utilizzi modelli di pianificazione del [tipo B o D](#tipi-di-modelli-di-pianificazione). injixo assegnerà i modelli settimanali nell’ordine configurato qui.

Utilizza le frecce Sposta in alto {% icon down-arrow-blue | icon-only %} e Sposta in basso {% icon up-arrow-blue | icon-only %} per stabilire la posizione dei modelli settimanali.

## Tipi di modelli di pianificazione

| Tipo | Nome               | Utilizzo dei modelli settimanali                                                      | Assegnazione dei modello di orario | Ora di inizio del turno              | Conseguenze             |
| ---- | ------------------ | -------------------------------------------------------------------------- | -------------------- | ----------------------------- | --------------------------------- |
| A    | Flessibile | injixo può scegliere qualunque modello di orario da qualunque modello settimanale incluso per ogni giorno della settimana. | injixo può utilizzare qualunque modello di orario da qualunque modello settimanale. | Flessibile    | A seconda dell’orario di apertura della tua organizzazione, il tipo A può causare una distribuzione dei turni che sembra casuale o risulta stressante per i dipendenti. Per esempio, un dipendente potrebbe dover lavorare presto il lunedì, di notte il martedì, e di sera il mercoledì, etc. |
| B    | Alternanza fissa     | injixo pianifica i modelli settimanali nell’ordine definito dalle loro posizioni. | Per ogni settimana, injixo sceglierà il modello di orario che copre meglio il fabbisogno di personale. | Fisso    | A ogni dipendente viene assegnato lo stesso modello di orario per tutta la settimana, per esempio con inizio alle 9 di mattina dal lunedì al venerdì. Definisci dei [giorni atipici](#giorni-atipici) se vuoi pianificare un modello di orario diverso. L’alternanza fissa è il modello di pianificazione che genera l’assegnazione di turni più uniforme. |
| C    | Alternanza flessibile  | injixo non rispetta la posizione dei modelli settimanali. | injixo sceglie un modello di orario per tutta la settimana. | Fisso    | Ai dipendenti può essere assegnato qualunque modello settimanale per fronteggiare meglio il fabbisogno di personale. Dal momento che i turni cominciano tutti alla stessa ora, i dipendenti hanno orari di lavoro uniformi durante tutta la settimana. |
| D    | Alternanza mista (A/B) | injixo rispetta la posizione definita per i modelli settimanali. | injixo sceglie un modello di orario per tutta la settimana.| Flessibile (all’interno di un periodo)    |  Sulla base del fabbisogno di personale, injixo può pianificare i dipendenti con turni mattutini in modo che comincino a lavorare tra le 8 e le 10. Con il tipo D, injixo può pianificare in modo più flessibile per soddisfare al meglio il fabbisogno di personale, e allo stesso tempo assegnare ai dipendenti pianificazioni alquanto uniformi. |


Il grafico seguente mostra come i vari tipi di modelli di pianificazione influiscono sulla pianificazione. Questo esempio include un modello di pianificazione con quattro modelli settimanali e tre modelli di orario per ogni modello settimanale.


{{ 2 | image: 'Esempio di pianificazione con i vari tipi di modelli di pianificazione' }}

## Giorni atipici

I giorni atipici permettono a injixo di infrangere le regole stabilite dal [tipo di modello di pianificazione](#tipi-di-modelli-di-pianificazione) attualmente in uso. Per esempio, puoi utilizzare i giorni atipici per pianificare un turno notturno in una settimana durante la quale un dipendente di solito lavora di mattina.<br>

I giorni atipici danno la priorità al fabbisogno di personale e garantiscono una copertura migliore. Tuttavia, hanno come conseguenza pianificazione meno uniformi.

Per pianificare dei giorni atipici, segui questi passaggi:

1. [Crea un modello settimanale separato](#creare-un-modello-settimanale) e aggiungilo ai modelli di orario che vuoi utilizzare come eccezioni.
2. Nel pannello di configurazione dei modelli settimanali che vuoi utilizzare per il turno standard, stabilisci il numero di giorni atipici per settimana.
3. Nel pannello di configurazione del modello di pianificazione, seleziona il modello settimanale che vuoi utilizzare per i giorni atipici.

Quando selezioni un modello di orario per la settimana, injixo non può utilizzare i modelli di orario definiti per i giorni atipici. Assicurati che tutti i dati di configurazione necessari per la pianificazione (per esempio, i modelli di orario utilizzati e il modello di pianificazione) rispettino l’{% link_new orario di lavoro di riferimento | features/administration/create-contracts.md | #orario-di-lavoro-di-riferimento %} stabilito nel contratto del dipendente. Se il modello di orario utilizzato per la settimana corrisponde al contratto, injixo può sostituire il modello di orario originale con quello definito per i giorni atipici, per soddisfare meglio il fabbisogno di personale.

## Assegnare i modelli di pianificazione dipendenti

1. Vai su _Plan > Configurazione > Dipendenti_{:.breadcrumbs}.
2. Seleziona un dipendente dall’elenco.
3. Clicca sull’icona Aggiungi {% icon item-add | icon-only %} nella sezione **Modelli di pianificazione**.<br>
   Si aprirà un pannello di configurazione a destra.
4. Configura i parametri:<br>
  **Validità dal/fino al**: imposta un {% link_new periodo di validità | features/administration/set-a-validity-period.md %}.<br>
  **Modello di pianificazione**<br>
  **Data di riferimento**: imposta una data di riferimento che stabilisce il primo giorno del modello di pianificazione.
5. Clicca su _OK_{:.doc-button}.

Utilizza la funzionalità di {% link_new modifica in blocco | features/administration/mass-update.md %} per assegnare un modello di pianificazione a molti dipendenti contemporaneamente.

> Fai attenzione se vuoi utilizzare la modifica in blocco per l’assegnazione dei modelli di pianificazione del tipo B
>
> Se utilizzi la funzionalità di modifica in blocco e imposti la stessa data di riferimento per tutti, tutti i dipendenti verranno pianificati con lo stesso modello settimanale allo stesso tempo.
>
> Seleziona piuttosto gruppi più piccoli per la modifica in blocco, e scegli dei lunedì in successione come date di riferimento. In questo modo, ogni gruppo comincerà l’alternanza in una settimana diversa.

## Esempi

### Esempio A: alternanza fissa con turni mattutini e serali

Configura un modello di pianificazione del tipo B (alternanza fissa), e assegnagli tre modelli settimanali diversi. Ricordati di definire la posizione per i modelli settimanali.

- Il modello settimanale 1 (posizione 1) contiene modelli di orario per i turni mattutini (turni che cominciano tra le 7 e le 9).
- Il modello settimanale 2 (posizione 2) contiene modelli di orario per i turni serali (turni che finiscono alle 23).
- Il modello settimanale 3 (posizione 3) contiene modelli di orario per i turni pomeridiani (turni che cominciano tra le 11 e mezzogiorno).

Con questo modello di pianificazione, i dipendenti alternano in modo uniforme una settimana con turni mattutini, una settimana con turni serali e una settimana con turni pomeridiani.

Sebbene questo richieda un certo grado di flessibilità, permette ai dipendenti di avere orari di lavoro uniformi durante la settimana.

### Esempio B: giorni atipici per turni notturni

Configura un modello di pianificazione con tre diversi modelli settimanali. Configura al massimo due giorni atipici alla settimana.

- Il modello settimanale 1 contiene i modelli di orario per i turni mattutini.
- Il modello settimanale 2 contiene i modelli di orario per i turni serali.
- Il modello settimanale 3 contiene i modelli di orario per i turni notturni (seleziona questo modello settimanale dal menu a tendina **Modello settimanale per giorni atipici**).

Con questo modello di pianificazione, i dipendenti avranno turni mattutini nella prima settimana e turni serali nella settimana successiva. Tuttavia, dal momento che hai definito due giorni atipici, ai dipendenti potranno essere assegnati anche due turni notturni alla settimana, se questa è la soluzione migliore per soddisfare il fabbisogno di personale.

<!-- TODO: very special example, add some more context  -->
<!-- ### Example: Performance-Based Scheduling With WTPMs and Preferred Day Models

Use Work Time Pattern Models and preferred day models  for Performance-Based Shift Assignment.

* Within the Week Time Patterns, assign the shifts according to agents' performance.
* Assign the Work Time Pattern Model to an agent with a validity period. Adjust it regularly according to performance scores.

For your high achievers you can pick some of the day models and assign them directly to these employees as personal day models. The AutoScheduler will only use these day models while generating schedules. This ensures that out-of-favor shifts are not assigned to high performing agents. -->

<!-- TODO: Example: normal use case scheduling different hours or working days in different weeks -->
<!-- ### Example: Scheduling Different Number of Working Days or Hours in Different Weeks -->
<!-- There is a bad German article /de/scheduling-different-wtm/ using WTPM Type B with two WTMs 4x10 and 5x8 hour shifts, with Autoscheduler contract parameter. minimum days per week with value 4 and scheduling parameter 2602 with value 10:00 -->
