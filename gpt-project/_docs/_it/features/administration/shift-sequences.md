---
title: Creare le rotazioni
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Utilizza le rotazioni per impostare pianificazioni che si ripetono.
redirect_from:
  - it/shift-sequence-overview/
redirect_reason: filename used in old product onboarding
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Inserire le rotazioni
    filepath: features/scheduling/schedules/schedules-insert-shift-sequences.md
---

Una rotazione è uno ciclo settimanale di modelli di orario o di attività. Con le rotazioni puoi inserire rapidamente questi cicli che si ripetono nella pianificazione. injixo ottimizzerà il resto della pianificazione.

Con le rotazioni puoi risparmiare molte ore di lavoro, dal momento che non devi pianificare i cicli manualmente.

Le rotazioni possono essere utili nei quattro casi seguenti:

- Caso 1: specificare quando alcuni turni devono essere pianificati.
- Caso 2: pianificare attività ricorrenti.
- Caso 3: specificare i giorni in cui i dipendenti non lavorano.
- Caso 4: specificare quando i turni possono essere pianificati in base alle disponibilità dei dipendenti.

Le rotazioni consistono di una o più righe. Ogni riga è un ciclo a sé stante che può essere inserito nella pianificazione.<br>
Ogni riga contiene delle caselle che rappresentano i giorni della settimana. Nelle caselle devi inserire i modelli di orario o le attività che vuoi utilizzare per pianificare usando la rotazione.<br>
Ogni riga rappresenta un ciclo settimanale per la pianificazione: per questo motivo, il numero di caselle in ogni riga deve essere un multiplo di sette. Una rotazione può avere un massimo di 53 righe perché non può proseguire per più di un anno.

## Prerequisiti

Per poter creare delle rotazioni, devi prima creare le {% link_new attività | features/administration/activities.md %} o i {% link_new modelli di orario | features/administration/daymodels/daymodel-creation.md %}.<br>
Dopo aver creato le rotazioni, devi {% link_new assegnarle ai dipendenti | features/administration/employee-overview.md | #assegnare-una-rotazione %} prima di poterle inserire nella pianificazione.<br>
Quando assegni una rotazione a un dipendente, devi impostare una data di riferimento. La data di riferimento è il primo giorno in cui la rotazione viene pianificata. A partire da quella data, la rotazione si ripete senza interruzioni finché è valida.<br>
Dato che le rotazioni sono cicli settimanali, scegli come data di riferimento un lunedì, o il giorno della settimana in cui comincia la vostra settimana lavorativa.

>Nota
>
>Per impostazione predefinita la settimana lavorativa comincia di lunedì.
>
>Puoi cambiare il primo giorno della settimana con l’impostazione _48420_{:.id-label} _Inizio della settimana pianificativa_.

## Creare le rotazioni

Prima di creare la prima rotazione, stabilisci quante rotazioni ti servono e il numero di righe e di caselle in ogni rotazione. Questo dipende esclusivamente dalle esigenze della tua organizzazione, per esempio da quanti turni diversi pianifichi, se pianifichi riunioni ricorrenti, etc.

Per creare una rotazione, vai su _Plan > Configurazione > Rotazioni_{:.breadcrumbs} e segui questi passaggi:

1. Clicca sull’icona Nuovo {% icon item-add | icon-only %} in alto a sinistra.
2. Configura i parametri della rotazione:<br>
  **Nome**: inserisci un nome unico (massimo 50 caratteri).<br>
  **Abbreviazione**: inserisci il nome o una sua versione più breve (massimo 25 caratteri).<br>
  **Righe**: inserisci il numero di righe della rotazione (massimo 53).<br>A ogni riga verrà assegnato un numero. Fai doppio clic su una riga per rinominarla. Avrai bisogno del numero o del nome della riga per poter assegnarla a un dipendente in seguito.<br>
  **Giorni**: inserisci la durata della rotazione: deve essere un multiplo di sette compreso tra 7 e 371.
6. Clicca su _OK_{:.doc-button}.

>Nota
>
>I giorni di una rotazione devono sempre essere un multiplo di sette, anche se la tua organizzazione è aperta solo cinque o sei giorni la settimana. Le rotazioni si ripetono automaticamente. Una rotazione di cinque giorni inserirebbe il turno di lunedì nella casella di un sabato, il turno di martedì nella casella di una domenica, etc.
>
>Se vuoi pianificare dei cicli con durate diverse (per esempio uno per le riunioni settimanali e uno per le riunioni quindicinali), devi creare delle rotazioni separate.

Dopo aver creato una rotazione, puoi impostare i suoi {% link_new periodi di validità | features/administration/set-a-validity-period.md %}:

1. Clicca sull’{% icon item-edit %} sopra la tabella.
2. Inserisci o scegli le date nei campi **Validità dal** e **fino al**.
3. Clicca su _OK_{:.doc-button}.

### Inserire i modelli di orario

1. Nel riquadro **Opzioni**, seleziona **Inserimento di un modello di orario** dal menu a tendina a sinistra.
2. Seleziona il modello di orario che vuoi inserire nel menu a tendina **Modello di orario**.
3. Inserisci un **numero**. Questo numero sarà il totale di giorni consecutivi in cui inserisci il modello di orario.
4. Nella tabella, clicca sulla prima casella nella quale vuoi inserire il modello di orario.<br>
  Se hai inserito un numero maggiore di uno, il modello di orario sarà inserito in quella casella e in tutte le caselle alla sua destra, fino a raggiungere il numero inserito.

La rotazione viene salvata automaticamente.

> Consiglio
>
> Utilizza attività o modelli di orario fissi. Se in una rotazione inserisci modelli di orario variabili, il turno comincerà sempre il prima possibile.

### Inserire le attività

1. Nel riquadro **Opzioni**, seleziona **Inserimento di attività** dal menu a tendina a sinistra.
2. Scegli l’attività che vuoi inserire dal menu a tendina **Attività**.
3. Inserisci un **numero**. Questo numero sarà il totale di giorni consecutivi in cui inserisci l’attività.
4. Per specificare l’ora in cui l’attività è pianificata, inserisci un intervallo di tempo (nel formato 24 ore) nei campi **dalle** e **alle**, oppure spunta la casella **Giorni interi**.
5. Nella tabella, clicca sulla prima casella nella quale vuoi inserire l’attività.<br>
  Se hai inserito un numero maggiore di uno, l’attività sarà inserita in quella casella e in tutte le caselle alla sua destra, fino a raggiungere il numero che hai inserito.

> Attività che finiscono dopo la mezzanotte
>
> Se vuoi inserire attività che finiscono dopo la mezzanotte, aggiungi 24 all’ora di fine. Per esempio, se l’attività deve finire all’una di notte del giorno successivo, inserisci 25:00.

## Modificare le rotazioni

1. Nel riquadro **Rotazione**, seleziona una rotazione dal menu a tendina.
2. Clicca su _Applica_{:.doc-button}.
3. Clicca sull’{% icon item-edit %} nella barra delle azioni in alto per modificare il nome, l’abbreviazione, il numero delle righe, o i giorni.<br>Quando hai finito con le modifiche, clicca su _OK_{:.doc-button}.
4. Clicca sull’{% icon item-edit %}nella barra delle azioni sopra la griglia per modificare i periodi di validità.<br>Quando hai finito con le modifiche, clicca su _OK_{:.doc-button}.

### Eliminare elementi da una rotazione

Per eliminare uno o più elementi da una rotazione, segui questi passaggi:
1. Nel riquadro **Rotazione**, seleziona una rotazione dal menu a tendina.
2. Clicca su _Applica_{:.doc-button}.
3. Nel riquadro **Opzioni**, seleziona **Eliminazione** dal menu a tendina.
4. Clicca sulle caselle per eliminare gli elementi al loro interno.<br>
  Gli elementi vengono eliminati automaticamente.

Per eliminare tutti gli elementi da una rotazione, segui questi passaggi:

1. Nel riquadro **Rotazione**, seleziona una rotazione dal menu a tendina.
2. Clicca su _Applica_{:.doc-button}.
3. Nel riquadro **Opzioni**, seleziona **Eliminazione** dal menu a tendina.
4. Spunta la casella **Elimina tutto** e clicca su _Applica_{:.doc-button}.<br>
  Gli elementi vengono eliminati automaticamente.

## Eliminare una rotazione

1. Nel riquadro **Rotazione**, seleziona una rotazione dal menu a tendina.
2. Clicca su _Applica_{:.doc-button}.
3. Clicca sull’{% icon item-delete %} nella barra delle azioni in alto.
4. Nella finestra di conferma, clicca su _Sì_{:.doc-button}.

## Esempi di utilizzo

Puoi utilizzare le rotazioni in diversi casi.

### Caso 1: specificare quando alcuni turni devono essere pianificati

Questo è il tuo caso se, per esempio, devi pianificare dei turni per la mattina presto e per la sera tardi per gruppi diversi di dipendenti. Questo caso si verifica anche se c’è un membro del team che non può cominciare a lavorare prima delle 11 il lunedì, ma è disponibile a cominciare prima tutti gli altri giorni della settimana. 
 
Per capire se questo caso ti riguarda, e per scoprire come configurare le rotazioni di conseguenza, guarda questo video di Academy (in inglese):

<div class="inline-video-container">
  <video class="inline-video-player-v" controls> 
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-1.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-1.vtt" kind="subtitles" srclang="en" label="Inglese" default>
   </video>
</div>
<br>

### Caso 2: pianificare attività ricorrenti

Questo è il tuo caso se, per esempio, devi pianificare delle riunioni che si ripetono ogni settimana, oppure se vuoi pianificare un dipendente per fare un’ora di back-office ogni giorno a un orario ben preciso. 

Per capire se questo caso ti riguarda, e per scoprire come configurare le rotazioni di conseguenza, guarda questo video di Academy (in inglese):

<div class="inline-video-container">
  <video class="inline-video-player-v" controls>
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-2.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-2.vtt" kind="subtitles" srclang="en" label="Inglese" default>
  </video>
</div>
<br>

### Caso 3: specificare i giorni in cui i dipendenti non lavorano

Questo è il tuo caso se, per esempio, devi definire dei cicli specifici di giorni liberi per i singoli dipendenti. 

Per capire se questo caso ti riguarda, e per scoprire come configurare le rotazioni di conseguenza, guarda questo video di Academy (in inglese):

  <div class="inline-video-container">
    <video class="inline-video-player-v" controls> 
     <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-3.mp4" type="video/mp4">
     <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-1.vtt" kind="subtitles" srclang="en" label="Inglese" default>
    </video>
  </div>
<br>

### Caso 4: specificare quando i turni possono essere pianificati in base alle disponibilità dei dipendenti

Questo è il tuo caso se devi pianificare dei dipendenti con disponibilità variabili.

Per capire se questo caso ti riguarda, e per scoprire come configurare le rotazioni di conseguenza, guarda questo video di Academy (in inglese):

<div class="inline-video-container">
  <video class="inline-video-player-v" controls>
   <source src="../../../assets/video/step-2-determine-how-to-organize-your-results/use-case-4.mp4" type="video/mp4">
   <track src="../../assets/video/step-2-determine-how-to-organize-your-results/subtitles/use-case-4.vtt" kind="subtitles" srclang="en" label="English" default>
  </video>
</div>
<br>

## Creare un report

È possibile creare un report nel formato PDF che include tutti i dati di una rotazione. Per creare il report, procedi come di seguito:

1. Nel riquadro **Rotazioni** a sinistra, inserisci la rotazione per la quale vuoi creare un report.
2. Clicca su _Applica_{:.doc-button}.
3. Clicca su _Report_{:.doc-button} sopra la tabella.
4. Nella finestra che si apre, puoi spuntare la casella per mandare il report all’indirizzo email che usi per il tuo account injixo.

Il report contiene gli orari di inizio e di fine delle attività e dei modelli di orario inclusi nella rotazione, e la loro durata netta, espressa in ore. Il report è strutturato in settimane.
Inoltre, il report include i totali e le medie della durata netta, come spiegato di seguito:

- Riga Totale: durata netta di tutte le attività o modelli di orario nella rotazione.
- Colonna Totale: somma della durata netta delle attività o dei modelli di orario per settimana.
- Riga Media organico: valore medio di tutti i valori inclusi nella riga Totale.
