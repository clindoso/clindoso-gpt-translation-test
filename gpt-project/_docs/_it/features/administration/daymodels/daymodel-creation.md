---
title: Configurare i modelli di orario
redirect_from:
  - it/day-models-overview/
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Scopri come creare modelli di orario del tipo turno fisso, turno variabile e periodo di disponibilità, e come aggiungere attività ai modelli di orario.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-basics.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/set-a-validity-period.md
---

È la prima volta che ti occupi di modelli di orario? Meglio cominciare dalle {% link_new basi  | features/administration/daymodels/daymodel-basics.md %}.

## Creare modelli di orario

Puoi creare e modificare i modelli di orario in _Plan > Configurazione > Modelli di orario_{:.breadcrumbs}.

> Nota
> 
> - I modelli di orario del tipo Turno fisso sono anche chiamati modelli di orario fissi.<br> 
> - I modelli di orario del tipo Turno variabile sono anche chiamati modelli di orario variabili.

1. Per aggiungere un nuovo modello di orario, clicca sull’icona Nuovo {% icon item-add | icon-only %}.
2. Dal menu a tendina **Tipo**, seleziona il tipo di modello di orario che vuoi configurare.
3. Configura il modello di orario.<br>Continua a leggere per scoprire altri dettagli sulle opzioni di configurazione di ogni tipo di modello di orario.
4. Per salvare il modello di orario, clicca su _OK_{:.doc-button}.

Adesso puoi {% link_new aggiungere delle attività | features/administration/daymodels/daymodel-creation.md | #aggiungere-attività-ai-modelli-di-orario %} al nuovo modello di orario. 

> Nota
> 
> Se utilizzi un {% link_new numero limitato di modelli di orario nella tua unità di pianificazione | features/administration/create-and-manage-planning-units.md | #limitare-i-modelli-di-orario %}, potrebbe essere necessario assegnare nuovi modelli di orario alla tua unità di pianificazione. Se utilizzi dei modelli di pianificazione, aggiorna i modelli settimanali.

### Turno fisso
   
| **Parametro** | **Descrizione** |
|:-----|:-----|
| Nome | Nome unico che descrive il modello di orario. Consigliamo di specificare il tipo del modello di orario, e le ore di inizio e di fine, per esempio: 8-16:30-fisso. |
| Abbreviazione | Questa versione del nome viene visualizzata nei report e in Schedules. Consigliamo di utilizzare il nome specificato o una sua versione più breve. |
| Comando di scelta rapida | Scorciatoia facoltativa che ti permette di inserire più rapidamente il modello di orario nel Centro dei turni. Scopri di più sui {% link_new comandi di scelta rapida | best-practices/tips-on-shift-center-usage.md %}. |
| Colore |  Il colore appare nella pianificazione e nelle schermate dei dati di configurazione.<br>Ti può aiutare a identificare rapidamente la lunghezza, il tipo di modello di orario o le attività incluse. |
| Validità dal/fino al | Periodo facoltativo durante il quale il modello di orario può essere utilizzato.<br>Scopri di più sui {% link_new periodi di validità | features/administration/set-a-validity-period.md %}. |
| Inizio | L’ora di inizio del turno fisso. |
| Fine | L’ora di fine del turno fisso. |
| Durata lorda del turno | Durata del turno espressa in ore.<br>Se lo configuri, questo valore sostituirà l’ora di fine configurata.<br>Nota: i modelli di orario del tipo Turno fisso possono estendersi fino a due giorni. Per creare un turno notturno, aggiungi fino a 24 ore all’ora di fine durante la creazione del modello di orario, oppure utilizza la durata lorda del turno. Il valore massimo è 48:00 (ore) |
| Attività | La prima attività è l’{% link_new attività di base | features/administration/daymodels/daymodel-basics.md | #attività-di-base-e-durata-del-turno %}.<br>Nota: dopo aver salvato il modello di orario non sarà più possibile cambiare l’attività di base. |


### Turno variabile
   
| **Parametro** | **Descrizione** |
|:---------------------|:---------------------|
| Nome | Nome unico che descrive il modello di orario. Consigliamo di specificare il tipo del modello di orario, e le ore di inizio e di fine, per esempio: 8-20-8-var. |
| Abbreviazione | Questa versione del nome viene visualizzata nei report e in Schedules. Consigliamo di utilizzare il nome specificato o una sua versione più breve. |
| Colore |  Il colore appare nella pianificazione e nelle schermate dei dati di configurazione.<br>Il colore ti può aiutare a identificare rapidamente la lunghezza, il tipo di modello di orario o le attività incluse. |
| Validità dal/fino al | Periodo facoltativo durante il quale il modello di orario può essere utilizzato.<br>Scopri di più sui {% link_new periodi di validità | features/administration/set-a-validity-period.md %}. |
| Inizio margine temporale | La prima ora possibile per l’inizio del turno. |
| Fine margine temporale | L’ultima ora possibile per la fine del turno. |
| Durata margine temporale | Il numero di ore tra la prima ora di inizio possibile e l’ultima ora di fine possibile.<br>Sostituisce l’ora di Fine margine temporale. |
| Durata lorda del turno | La durata complessiva del turno, incluse le pause. La durata deve essere inferiore rispetto al margine temporale. Se la durata del turno è uguale al margine temporale, il modello di orario diventa automaticamente un modello di orario del tipo Turno fisso. |
| Intervallo di tempo | L’intervallo di tempo, compreso nel margine temporale stabilito, all’interno del quale il turno può cominciare. Per esempio, con un intervallo di 30, il turno può cominciare ogni 30 minuti all’interno del margine temporale stabilito. |
| Attività | La prima attività è l’{% link_new attività di base | features/administration/daymodels/daymodel-basics.md | #attività-di-base-e-durata-del-turno %}.<br>Nota: dopo aver salvato il modello di orario non sarà più possibile cambiare l’attività di base. |

### Margine di disponibilità

Utilizza questo tipo di modello di orario, per esempio, nelle rotazioni, per configurare contemporaneamente la disponibilità di molti dipendenti. Tieni in considerazione che le disponibilità nei modelli di orario sovrascrivono sia le disponibilità inserite dai dipendenti in injixo Me che le disponibilità aggiunte manualmente nel Centro dei turni. Scopri di più sulle {% link_new disponibilità | features/administration/availabilities.md %}.

| **Parametro** | **Descrizione** |
|:---------------------|:---------------------|
| Nome | Nome unico che descrive il modello di orario. Consigliamo di specificare il tipo del modello di orario, e le ore di inizio e di fine, per esempio: 8-16-dispo. |
| Abbreviazione | Questa versione del nome viene visualizzata nei report e in Schedules. Consigliamo di utilizzare il nome specificato o una sua versione più breve. |
| Colore |  Il colore appare nella pianificazione e nelle schermate dei dati di configurazione.<br>Può essere utile quando si impostano le rotazioni, per esempio. |
| Validità dal/fino al | Periodo facoltativo durante il quale il modello di orario può essere utilizzato.<br>Scopri di più sui {% link_new periodi di validità | features/administration/set-a-validity-period.md %}. |
| Inizio del margine di disponibilità | La prima ora possibile per l’inizio del turno. |
| Fine del margine di disponibilità | L’ultima ora possibile per la fine del turno. |
| Durata del margine di disponibilità | Il numero di ore tra la prima ora di inizio possibile e l’ultima ora di fine possibile. Il massimo valore consentito è 48 ore.<br>Sostituirà la fine del margine di disponibilità. |

## Aggiungere attività ai modelli di orario

Per definire meglio un modello di orario è possibile aggiungere ad esso pause o altre attività. Configura altre attività se devi rappresentare dei compiti specifici che devono essere svolti dai dipendenti in un preciso momento durante un turno. Esempi di attività speciali sono, per esempio, controllare i social media dell’organizzazione o svolgere i compiti di back-office.

Per poter aggiungere delle attività, devi prima {% link_new creare il modello di orario | features/administration/daymodels/daymodel-creation.md | #creare-modelli-di-orario %}.

L’ottimizzazione della pianificazione sostituisce le attività del tipo Presenza configurate come sostituibili. Se non vuoi che i dipendenti svolgano delle attività speciali, l’attività di base sarà l’unica attività del tipo Presenza nel tuo modello di orario. Ricorda che configurare delle attività nei modelli di orario limiterà la flessibilità delle funzionalità di ottimizzazione (per esempio l’ottimizzazione completa, le attività extra, le riunioni). Per mantenere l'ottimizzazione il più flessibile possibile e per evitare errori di programmazione, consigliamo di mantenere al minimo la configurazione delle attività del tipo Presenza nei modelli di orario.

> Nota
> 
> La prima attività che aggiungi a un modello di orario diventa automaticamente l’attività di base. Non puoi cambiare o eliminare l’attività di base dopo aver salvato il modello di orario.
> Consigliamo di utilizzare l’attività Presente come attività di base. Scopri di più sull’{% link_new attività di base | features/administration/daymodels/daymodel-basics.md | #attività-di-base-e-durata-del-turno %}.

### Aggiungere un’attività del tipo Presenza o Assenza

Per aggiungere un’attività di presenza o assenza a un modello di orario esistente, prosegui come di seguito:

1. Seleziona un modello di orario.
2. Nella sezione **Presenze e assenze**, clicca sull’icona Aggiungi {% icon item-add | icon-only %}.<br>Si aprirà una finestra.
3. Configura l’attività:
- **Inizio** e **Fine**:<br>Se la casella **Relativo all’inizio del turno** è spuntata: definisci il numero di ore o minuti che deve trascorrere dall’inizio del turno per l’inizio e il termine dell’attività (per esempio, per un’ora e mezza, inserisci 1:30).<br>Se la casella **Relativo all’inizio del turno** non è spuntata: definisci l’ora esatta, successiva all’inizio del turno, per l’inizio e la fine dell’attività (per esempio, per le 2 del pomeriggio, inserisci 14:00).
- **Durata**: se configuri una durata superiore all’arco di tempo tra l’ora di inizio e l’ora di fine configurate, crei un {% link_new corridoio | features/administration/daymodels/daymodel-basics.md | #elementi-fissi-e-corridoi %} nell’ambito del quale l’attività può essere spostata.
- **Intervallo di tempo**: consigliamo di utilizzare lo stesso intervallo del sistema ACD. Tieni in considerazione che la durata dell’attività deve essere divisibile per l’intervallo selezionato.<br>Se inserisci 0, l’ora di inizio dell’attività è fissa, e l’attività non può essere spostata nell’ambito del corridoio.
- **Relativo all’inizio del turno**:<br>Se questa casella è spuntata (come è per impostazione predefinita), l’attività comincia dopo che il lasso di tempo definito è trascorso dall'inizio del turno. Se il turno viene spostato, anche l’attività viene spostata.<br>Se la casella non è spuntata, l’attività comincia esattamente all’ora che è stata configurata. Quando sposti un turno variabile, le attività non vengono spostate. Questo può essere utile, per esempio, quando dipendenti con turni diversi devono partecipare a una riunione alla stessa ora.
4. Seleziona un’**attività** dal menu a tendina.
5. Clicca su _OK_{:.doc-button}.

### Aggiungere un’attività di pausa

Nei modelli di orario variabili e fissi, è possibile aggiungere delle pause per la pianificazione ottimizzata e l’offerta dei turni.  
Per aggiungere un’attività di pausa a un modello di orario esistente, procedi come di seguito:

1. Seleziona un modello di orario.
2. Nella sezione **Pause pianificabili**, clicca sull’icona Aggiungi {% icon item-add | icon-only %}.<br>Si aprirà una finestra.
3. Configura la pausa:
- **Inizio** e **Fine**:<br>Se la casella **Relativo all’inizio del turno** è spuntata: definisci il numero di ore o minuti che deve trascorrere dall’inizio del turno per l’inizio e il termine della pausa (per esempio, per 4 ore e mezza, inserisci 4:30). Per impostazione predefinita, le pause sono inserite in relazione all’inizio del turno, perché solitamente cominciano dopo un dato lasso di tempo al lavoro.<br>Se la casella **Relativo all’inizio del turno** non è spuntata: definisci l’ora esatta, successiva all’inizio del turno, per l’inizio e la fine della pausa (per esempio, per l’una del pomeriggio, inserisci 13:00).
- **Durata**: se configuri una durata superiore all’arco di tempo tra l’ora di inizio e l’ora di fine configurate, crei un {% link_new corridoio | features/administration/daymodels/daymodel-basics.md | #elementi-fissi-e-corridoi %} all’interno del quale la pausa può essere spostata.
- **Intervallo di tempo**: consigliamo di utilizzare lo stesso intervallo del sistema ACD. Tieni in considerazione che la durata della pausa deve essere divisibile per l’intervallo selezionato.<br>Se inserisci 0, l’ora di inizio della pausa è fissa, e la pausa non può essere spostata nell’ambito del corridoio.
- **Relativo all’inizio del turno**:<br>Se questa casella è spuntata (come è per impostazione predefinita), la pausa comincia dopo che il lasso di tempo definito è trascorso dall'inizio del turno. Se il turno viene spostato, anche la pausa viene spostata.<br>Se la casella non è spuntata, la pausa comincia esattamente all’ora che è stata configurata. Quando sposti un turno variabile, le pausa non vengono spostate. Questo può essere utile se, per esempio, la mensa del tuo contact center è aperta solo per un certo lasso di tempo.
4. Seleziona una pausa dal menu a tendina **Pausa**.
5. Clicca su _OK_{:.doc-button}.

Nota: in injixo Enterprise WFM on-premise, il parametro _48134_{:.id-label} determina se i corridoi di pausa restano, o se vengono trasformati in elementi fissi.

## Conseguenze delle modifiche ai modelli di orario attualmente in uso

Modificare i modelli di orario che sono già in uso nelle tue pianificazioni può avere diverse conseguenze. È possibile modificare i dati di configurazione che non sono rilevanti per la pianificazione, come il nome, l’abbreviazione, e il colore.

Consigliamo però di modificare i dati rilevanti per la pianificazione, come le ore di inizio e di fine, la durata lorda del turno, le presenze, le assenze e le pause, soltanto prima di creare la pianificazione successiva. Quando modifichi un modello di orario esistente, injixo crea una copia interna del modello di orario originale. In questo modo, i turni che sono già stati pianificati vengono mantenuti e saranno visualizzati.

Dopo aver modificato un modello di orario esistente, o averne aggiunto uno nuovo, avvia il processo di pianificazione dall’inizio, in modo che i modelli di orario nuovi o modificati vengano utilizzati correttamente.

I modelli di orario interessati saranno sostituiti nelle rotazioni e nei modelli settimanali. I modelli di orario già pianificati saranno visualizzati con una linea punteggiata in basso nel Centro dei turni e in Schedules. I turni con questo modello di orario non potranno più essere pianificati o modificati. Potranno soltanto essere eliminati dalla pianificazione.

Se hai generato dei turni a partire da un modello di orario, e i dipendenti hanno già richiesto questi turni in injixo Me nell’ambito dell’offerta dei turni, i dipendenti non saranno più in grado di visualizzare o richiedere dei turni con quel modello di orario.
I turni già richiesti non verranno utilizzati nella lotteria e nelle assegnazioni successive.

Nota: i valori minimi e massimi inseriti come fabbisogno per il turno restano validi per il modello di orario modificato.
