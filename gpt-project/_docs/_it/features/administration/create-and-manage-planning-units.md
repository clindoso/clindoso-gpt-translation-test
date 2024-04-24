---
title: Creare e gestire le unità di pianificazione
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Scopri come creare, configurare ed eliminare le unità di pianificazione.
related_articles:
  - overwrite_title: Creare e utilizzare i calendari di pianificazione
    filepath: features/administration/configure-planning-calendars.md
  - overwrite_title: Pianificare i dipendenti in diverse sedi
    filepath: best-practices/how-to-use-virtual-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
redirect_from:
  - it/planning-unit-configuration/
redirect_reason: Updated filename on 21 July 2023
---

Le unità di pianificazione raggruppano i dipendenti e i dati di configurazione ai fini della pianificazione. Le sedi della tua organizzazione non devono necessariamente corrispondere alle unità di pianificazione. Per esempio, dei dipendenti che lavorano in due sedi diverse possono essere {% link_new assegnati | features/administration/employee-overview.md | #configurare-le-impostazioni-del-dipendente %} alla stessa unità di pianificazione.

## Quante unità di pianificazione dovrei utilizzare?
	
Per ottimizzare il lavoro, puoi pianificare i dipendenti che lavorano in sedi o team diversi in una sola unità di pianificazione utilizzando i {% link_new gruppi di selezione | features/administration/selections.md %}. Utilizza più unità di pianificazione nei seguenti casi:
-  I dipendenti si trovano in fusi orari diversi.
-  I pianificatori sono responsabili soltanto per gruppi distinti di dipendenti, per esempio i vari dipartimenti dell’azienda. In injixo Advanced e Enterprise WFM, utilizza i ruoli utente personalizzati per {% link_new limitare l’accesso alle unità di pianificazione | getting-started/configure-user-roles.md | #gestire-laccesso-ai-team-limitare-laccesso-ai-dati-di-configurazione %}.
- Hai un fabbisogno di personale condiviso, per esempio per gestire il sovraccarico.
- Se vuoi generare report che includono dati provenienti da diverse unità di pianificazione.
	
> Consigli per lavorare con più unità di pianificazione
>
> - Per poter analizzare i numeri riguardanti unità di pianificazione diverse, aggiungi un’unità di pianificazione superiore a tutte le unità di pianificazione rilevanti.
> - È possibile modificare temporaneamente l’assegnazione di un dipendente da un’unità di pianificazione a un’altra.<br>Scopri come {% link_new trasferire temporaneamente un dipendente | features/administration/employee-overview.md | #trasferire-temporaneamente-i-dipendenti %} a un’altra unità di pianificazione.
	
<!-- Typically, you assign one planning unit to a person at a time. Reassign a planning unit using valid from and valid to dates in the employee configuration. In rare cases, you will need to assign more than one planning unit to a person. The person's main planning unit is assigned with priority 1. The person is scheduled in this main planning unit. A person's schedule will be displayed in other planning units with lower priority. You can also manually reschedule people in other planning units if needed. -->

## Creare un’unità di pianificazione

1. Vai su _Plan > Configurazione > Unità di pianificazione_{:.breadcrumbs}.
2. Clicca sull’icona Nuovo {% icon item-add | icon-only %} in alto a sinistra.  
   Si aprirà un pannello di configurazione a destra.
3. Compila i campi seguenti:

   - **Nome**: nome dell’unità di pianificazione (massimo 50 caratteri).
   - **Abbreviazione**: abbreviazione del nome (massimo 25 caratteri).
   - **Colore**: colore facoltativo per l’unità di pianificazione. Il colore sarà utilizzato in Schedules.
   - **Intervallo di tempo**: influisce sul livello di dettaglio con cui sono visualizzati i dati in Schedules, per esempio la copertura e il fabbisogno di personale. L’intervallo di tempo dell'unità di pianificazione non dovrebbe essere più lungo dell’intervallo di importazione dei dati sui contatti e sugli stati degli agenti. Il menu a tendina mostra gli intervalli dell’unità di pianificazione in minuti. Consigliamo di utilizzare intervalli da **15 minuti**. Non sarà possibile modificare l’intervallo dopo il salvataggio. Scopri di più sulle {% link_new importazioni di dati tramite le integrazioni | features/acd-integration/cloud/how-integrations-work.md %}.
   - **Unità di pianificazione superiore**: unità di pianificazione facoltativa che contiene l’unità di pianificazione che stai creando. Scopri di più sulle {% link_new unità di pianificazione superiori | best-practices/how-to-use-virtual-planning-units.md %}.
   - **Fuso orario**: il fuso orario dell’unità di pianificazione. Non sarà possibile modificare il fuso orario dopo aver salvato l’unità di pianificazione. Scopri come {% link_new lavorare con i fusi orari | best-practices/working-with-timezones.md %}.

     > Nota
     >
     > Il fuso orario selezionato deve corrispondere al fuso orario dei tuoi workload in Forecast. In caso contrario non sarà possibile utilizzare il fabbisogno di personale per la pianificazione. Le integrazioni modificheranno i dati importati in funzione del fuso orario dei workload.

4. Clicca su _OK_{:.doc-button}.  
   Adesso puoi aggiungere gli orari di apertura e le attività, oppure {% link_new limitare i modelli di orario | features/administration/create-and-manage-planning-units.md | #limitare-i-modelli-di-orario %}.

### Aggiungere gli orari di apertura

Per poter aggiungere degli orari di apertura a un’unità di pianificazione, è necessario prima {% link_new crearla | features/administration/create-and-manage-planning-units.md | #creare-ununità-di-pianificazione %}.

Per la pianificazione è necessario aggiungere gli orari di apertura ai tipi di giorno inclusi nell’unità di pianificazione. Gli orari di apertura definiscono le ore per le quali puoi {% link_new calcolare il fabbisogno di personale | features/forecast/injixo-forecast/calculate-staff-requirements.md %} e {% link_new creare pianificazioni ottimizzate | features/scheduling/schedules/schedules-optimized-schedules.md %}. <!-- special public holiday day types or part of the linked article? -->

1. Nella sezione **Orari di apertura** del pannello di configurazione, clicca sull’icona Aggiungi {% icon item-add | icon-only %}.  
   Si aprirà una finestra.
2. Nella sezione **Tipo di giorno**, seleziona uno o più {% link_new tipi di giorno | features/administration/day-types.md %}.
3. Inserisci gli orari di inizio e di fine nei campi **dalle** e **alle** (nel formato 24 ore). Se l’unità di pianificazione è aperta 24 ore su 24, inserisci 00:00 in entrambi i campi.
4. (Facoltativo) Nei campi **Validità dal** e **fino al**, inserisci il periodo durante il quale gli orari di apertura sono validi. Se gli orari di apertura sono sempre validi, lascia vuoti i campi. Scopri di più sui {% link_new periodi di validità | features/administration/set-a-validity-period.md %}.
5. Clicca su _OK_{:.doc-button}.

Per modificare o rimuovere gli orari di apertura, clicca sull’{% icon item-edit %} o sull’{% icon item-delete %}.

### Aggiungere le attività

Per poter aggiungere delle attività a un’unità di pianificazione, è necessario prima {% link_new creare l’unità di pianificazione | features/administration/create-and-manage-planning-units.md | #creare-ununità-di-pianificazione %}.

Prima di creare le pianificazioni, devi aggiungere tutte le relative attività del tipo Presenza alle unità di pianificazione. Puoi pianificare i dipendenti soltanto per le attività che sono state aggiunte alla loro unità di pianificazione. Per impostazione predefinita, tutte le unità di pianificazione includono l’attività Presente, che non può essere eliminata.
Per includere attività di qualsiasi tipo nei report, aggiungi le attività alle relative unità di pianificazione.

Per aggiungere delle attività all’unità di pianificazione, procedi come di seguito:

1. Nella sezione **Attività** del pannello di configurazione dell’unità di pianificazione, clicca sull’icona Aggiungi {% icon item-add | icon-only %}.  
   Si aprirà una finestra.
2. Clicca sull’attività che vuoi aggiungere.
3. Inserisci un intervallo di tempo nei campi **dalle** e **alle**. La funzionalità {% link_new Crea una pianificazione ottimizzata | features/scheduling/schedules/schedules-optimized-schedules.md %} terrà conto di quest’attività all’interno dell’intervallo che hai configurato. Se entrambi i campi hanno il valore 00:00, injixo terrà conto degli orari di apertura dell’unità di pianificazione. Gli utenti con accesso amministratore possono modificare questo comportamento con l’impostazione _48408_{:.id-label} _Osservare gli orari di apertura dell'unità pianificativa_.
4. (Facoltativo) Inserisci un periodo nei campi **Validità dal** e **fino al** per definire il periodo in cui l’attività può essere utilizzata per la pianificazione.<br>Per rendere l’attività sempre disponibile per la pianificazione, lascia vuoti i campi **Validità dal** e **fino al**.
5. Clicca su _OK_{:.doc-button}.

Per modificare un'attività clicca sull’{% icon item-edit %}; per eliminarla, clicca sull’{% icon item-delete %}.

### Aggiungere le multiattività

Per aggiungere una {% link_new multiattività | features/administration/activity-types-and-properties.md | #subattività %} a un’unità di pianificazione, devi prima aggiungere tutte le relative subattività. Nell’elenco delle attività, la multiattività è evidenziata in grassetto. Le multiattività non sono disponibili in injixo Essential WFM.

### Limitare i modelli di orario

Per impostazione predefinita, alle unità di pianificazione sono assegnati tutti i {% link_new modelli di orario | features/administration/daymodels/daymodel-creation.md %}. Se per una unità di pianificazione non utilizzi tutti i modelli di orario, puoi limitare il numero di modelli di orario per quell’unità di pianificazione.

Limitare i modelli di orario può velocizzare il processo di pianificazione con la funzionalità Crea una pianificazione ottimizzata. Però potrai utilizzare soltanto i modelli di orario che sono assegnati all’unità di pianificazione per creare turni, generare report o creare pianificazioni ottimizzate. Questo potrebbe comportare una manutenzione più impegnativa per gli altri dati di configurazione, per esempio i modelli settimanali. Eliminare un modello di orario non influisce sulle pianificazioni e sui turni creati con quel modello di orario.

> Nota
>
> Se elimini tutti i modelli di orario dall’unità di pianificazione, potrai pianificare le attività solo manualmente, oppure {% link_new inserendole nelle rotazioni | features/administration/shift-sequences.md %}. Non potrai più utilizzare la funzionalità **Crea una pianificazione ottimizzata**.

Per limitare il numero di modelli di orario, procedi come di seguito:

1. Vai su _Plan > Configurazione > Unità di pianificazione_{:.breadcrumbs}.
2. Seleziona l’unità di pianificazione che vuoi modificare e scorri fino alla sezione **Modelli di orario** del pannello di configurazione.
3. Per limitare il numero di modelli di orario, sostituisci o elimina l’assegnazione prestabilita dei modelli di orario.
   - Clicca sull’{% icon item-edit %} accanto all’opzione **[Tutti]** e seleziona un modello di orario.
   - Clicca sull’{% icon item-delete %} per deselezionare l’opzione **[Tutti]**.
4. Clicca sull’icona Aggiungi {% icon item-add | icon-only %} per assegnare uno o più modelli di orario. Non è possibile assegnare due volte lo stesso modello di orario. Per modificare o eliminare un modello di orario in uso, clicca sull’{% icon item-edit%} o sull’{% icon item-delete %}.
5. Clicca su _Ok_{:.doc-button}.

## Eliminare un’unità di pianificazione

> Attenzione
>
> Se elimini un’unità di pianificazione non avrai più accesso alle relative pianificazioni.

1. Vai su _Plan > Configurazione > Unità di pianificazione_{:.breadcrumbs}.
2. Seleziona l’unità di pianificazione che vuoi eliminare.
3. Clicca sull’{% icon item-delete %} in alto a sinistra.
4. Per confermare, clicca su _Sì_{:.doc-button}.
