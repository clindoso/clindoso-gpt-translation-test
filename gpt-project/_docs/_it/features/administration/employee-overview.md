---
title: Configurare i dipendenti
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Crea e configura i dipendenti da includere nella pianificazione.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/calculate-a-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/staff-requirement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-job-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-optimized-schedules.md
---

In injixo è possibile creare e modificare un dipendente in tre sezioni diverse, a seconda delle esigenze specifiche. La tabella sottostante offre una panoramica delle diverse sezioni per la configurazione dei dipendenti, e descrive quali azioni sono possibili in ciascuna sezione.

| Sezione                                           | Descrizione              |
| ----------------------------------------------- | ------------------------ |
| _Plan > Configurazione > Dipendenti_{:.breadcrumbs}   | {% link_new Configurare un dipendente per la pianificazione | features/administration/employee-overview.md | #panoramica-delle-impostazioni-del-dipendente %}. I dipendenti ai quali non sono assegnate unità di pianificazione non saranno inclusi nell’elenco.      |
| _Account > Utenti_{:.breadcrumbs}                                 | Gestire le autorizzazioni degli utenti tramite i {% link_new ruoli utente | getting-started/configure-user-roles.md | #creare-nuovi-ruoli-utente %}, {% link_new sbloccare gli utenti bloccati | getting-started/manage-user-accounts.md | #sbloccare-gli-utenti %}, {% link_new impostare una nuova password per gli utenti | getting-started/manage-user-accounts.md | #impostare-una-nuova-password-per-lutente %}, e {% link_new controllare quali utenti sono inclusi nella fatturazione | getting-started/how-does-billing-work.md | #visualizzare-gli-utenti-fatturati-e-non-fatturati %}. È anche possibile {% link_new eliminare degli utenti | getting-started/manage-user-accounts.md | #eliminare-un-account-utente %}, così che non vengano più fatturati. |
| **Dipendenti**                                                           | {% link_new Creare e gestire | features/people/manage-people.md %} l’account di un utente, e gestire le informazioni di contatto e l’indirizzo. |

In _Plan > Configurazione > Dipendenti_{:.breadcrumbs}, gli utenti senza accesso amministratore possono visualizzare solo i dipendenti assegnati alle unità di pianificazione alle quali hanno accesso. I dipendenti che non sono assegnati a una unità di pianificazione non sono inclusi nell’elenco, anche se selezioni Tutte/Tutti nei menu a tendina dell’unità di pianificazione e del gruppo di selezione. Gli utenti con accesso amministratore visualizzano tutti i dipendenti.

I dipendenti e gli utenti sono sincronizzati, quindi è sufficiente creare ogni dipendente solo una volta. Ogni dipendente sarà conteggiato solo una volta nella fatturazione.

> Ogni dipendente o utente che crei in una delle tre sezioni verrà {% link_new fatturato | getting-started/how-does-billing-work.md %} alla tua organizzazione fino al momento in cui lo {% link_new disattivi oppure elimini | features/administration/deactivate-employees.md %}.

## Creare un dipendente

Per creare un dipendente con le impostazioni di base, devi compilare tutti i campi obbligatori in injixo. Prima di poter includere un dipendente nella pianificazione, devi [configurare](#configurare-le-impostazioni-del-dipendente) parecchie altre [impostazioni del dipendente](#panoramica-delle-impostazioni-del-dipendente).
Per creare un dipendente con le impostazioni di base, segui questi passaggi:

1. Vai su _Plan > Configurazione > Dipendenti_{:.breadcrumbs}.
2. Nella barra delle azioni, clicca sull’icona Nuovo {% icon item-add | icon-only %}.
3. Nella sezione **Generale** aggiungi un **N° di matricola** unico.
4. Nella sezione **Dati personali** aggiungi il **Cognome** del dipendente.
5. Nel campo **injixo Accedi (E-mail)** inserisci l’indirizzo email che il dipendente utilizzerà per accedere a injixo. Viene creato automaticamente un identificativo utente per l’accesso a injixo Me. 
6. {% link_new Imposta una password | features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md %} per il dipendente, così che possa fare il login in injixo.<br>Puoi farlo dopo aver concluso la configurazione di base del dipendente.
7. Clicca su _OK_{:.doc-button}.<br>La data d’assunzione viene impostata automaticamente sul giorno in corso. È possibile modificarla in seguito nella sezione [Appartenenza all’organico](#altre-impostazioni).

Quando crei un dipendente, injixo crea automaticamente un utente con il ruolo Agente.

<!-- In injixo Enterprise on-premise, you need to set the correct join date for the employee in the Employment Period section manually. To automatically create a linked user in the Users section, you need to add a User name and a Password in the Employee section. The injixo Login (Email) field is called Email 1 here and is not mandatory. --->

## Configurare le impostazioni del dipendente

Dopo aver creato un dipendente e configurato le impostazioni di base obbligatorie, puoi configurare le impostazioni relative alla pianificazione. Per farlo, segui questi passaggi:

Prerequisito: hai impostato {% link_new tutti gli elementi indispensabili per la pianificazione | getting-started/set-up-base-configuration.md | #elementi-della-configurazione-indispensabili %}.

1. Clicca su un dipendente nell’elenco.<br>
Utilizza i link rapidi blu in alto a destra per accedere velocemente alle varie sezioni.
2. Clicca sull’icona Aggiungi {% icon item-add | icon-only%} in una sezione per aggiungere una nuova impostazione. Per modificare un’impostazione già esistente, clicca sull’icona Modifica {% icon item-edit | icon-only %}.<br>Scopri di più sulle [opzioni delle impostazioni individuali](#panoramica-delle-impostazioni-del-dipendente).
3. (Facoltativo) In alcune sezioni, è possibile compilare i campi {% link_new Validità dal e fino al | features/administration/set-a-validity-period.md %} per circoscrivere il periodo di validità di un’impostazione.
4. Per salvare le modifiche, clicca su _OK_{:.doc-button}.


## Panoramica delle impostazioni del dipendente

Nelle sezioni seguenti troverai informazioni sulle impostazioni di pianificazione obbligatorie e facoltative per la configurazione dei dipendenti.

### Impostazioni di pianificazione obbligatorie

L’elenco che segue illustra gli elementi di configurazione obbligatori che devi assegnare ai dipendenti per poterli pianificare. Per avere più informazioni su ogni elemento della configurazione, clicca sui link.

> Nota
>
> Non è possibile aggiungere assegnazioni che hanno {% link_new periodi di validità | features/administration/set-a-validity-period.md %} sovrapposti.
> Per impostazione predefinita, le assegnazioni passate e quelle future non sono visibili. Per visualizzarle, clicca sull’icona Mostra tutto {% icon assignment-history | icon-only %}.


- {% link_new Contratti | features/administration/create-contracts.md %}: il menu a tendina mostra tutti i contratti disponibili. Scegli il contratto giusto per il dipendente e assegnaglielo.
- {% link_new Livelli di qualifica | features/administration/work-with-skills.md %}: i livelli di qualifica rispecchiano la competenza di un dipendente nello svolgimento di un compito specifico. Seleziona uno o più livelli di qualifica dal menu a tendina.
- {% link_new Attività | features/administration/activities.md %}: le attività sono i compiti che un dipendente può svolgere in base alle sue qualifiche. La sezione delle attività viene compilata automaticamente dopo che hai assegnato un livello di qualifica a un dipendente. Le attività che possono essere svolte da tutti i dipendenti non richiedono una qualifica, come, per esempio, le attività preconfigurate Presente e Ferie.
- {% link_new Unità di pianificazione | features/administration/create-and-manage-planning-units.md %}: le unità di pianificazione raggruppano i dipendenti. Un dipendente può essere assegnato a diverse unità di pianificazione, ma è necessaria almeno una unità di pianificazione con priorità 1. Le altre unità di pianificazione possono essere assegnate con un valore compreso tra 1 e 100, dove 1 rappresenta la priorità più alta.

### Impostazioni di pianificazione facoltative

Le impostazioni che seguono non sono obbligatorie ma possono essere utilizzate per la pianificazione. Per avere più informazioni su ogni elemento della configurazione, clicca sui link.

- {% link_new Disponibilità | features/administration/availabilities.md %}: definiscono i giorni e gli orari in cui un dipendente è disponibile a essere pianificato. Se vuoi escludere in via permanente un dipendente dalla pianificazione in un dato giorno della settimana, imposta la disponibilità per il rispettivo {% link_new tipo di giorno | features/administration/day-types.md %} a un minuto. Per configurare la stessa disponibilità per più dipendenti contemporaneamente, utilizza i modelli di orario del tipo
 {% link_new Margine di disponibilità | features/administration/daymodels/daymodel-creation.md | #margine-di-disponibilità %} nelle rotazioni. Se un dipendente è disponibile senza limitazioni, non è necessario aggiungere nessuna disponibilità.

- {% link_new Modelli di orario | features/administration/daymodels/daymodel-creation.md %}: per impostazione predefinita, injixo utilizza tutti i modelli di orario assegnati all’unità di pianificazione per creare pianificazioni per i dipendenti. Se assegni dei modelli di orario personali a un dipendente, l’ottimizzazione delle pianificazioni utilizzerà solo quegli specifici modelli di orario per il dipendente. Se vuoi che injixo pianifichi soltanto i dipendenti ai quali sono stati assegnati dei modelli di orario personali, puoi attivare la regole di pianificazione _2661_{:.id-label}_Osservare l'assegnazione di modelli di orario_.

- {% link_new Rotazioni | features/administration/shift-sequences.md %}: le rotazioni contengono modelli di orario oppure attività che si ripetono su base settimanale. Se vuoi utilizzare le rotazioni per creare pianificazioni per i tuoi dipendenti, devi prima creare e [assegnare le rotazioni a un dipendente](#assegnare-una-rotazione). Puoi anche decidere di assegnare più di una rotazione a un dipendente, se, per esempio, vuoi utilizzare una rotazione per i fine settimana e un’altra rotazione per gli altri giorni della settimana.

- {% link_new Gruppi di selezione | features/administration/selections.md %}: i gruppi di selezione funzionano come una sorta di filtro per visualizzare un gruppo ristretto di dipendenti in una panoramica, o per svolgere un’azione per un dato gruppo di dipendenti in contemporanea. Puoi creare uno o più gruppi di selezione dal menu a tendina Gruppi di selezione. Utilizza i gruppi di selezione, per raggruppare, per esempio, i dipendenti che sono pianificati sempre allo stesso modo, che hanno lo stesso contratto, che lavorano in rotazioni, che condividono un’auto per andare al lavoro, o che vengono pianificati per primi perché lavorano a tempo pieno.

- {% link_new Modelli di pianificazione | features/administration/work-time-pattern-models.md %}: utilizza i modelli di pianificazione per restringere la pianificazione automatica a un sottogruppo di tutti i modelli di orario disponibili. È possibile assegnare solo un modello di pianificazione a ciascun dipendente. Scegli una {% link_new data di riferimento | features/administration/reference-date.md %} per contrassegnare la data di inizio del modello di pianificazione.


- Sistemi esterni: assegna gli {% link_new identificatori degli utenti esterni | features/acd-integration/cloud/import-agent-status-data.md | #associare-gli-identificatori-degli-utenti-esterni-ai-dipendenti-in-injixo %} che sono necessari per importare i dati sugli stati degli agenti dal tuo sistema ACD.

### Altre impostazioni

La sezione seguente offre una panoramica delle altre impostazioni di configurazione del dipendente. La maggior parte di esse non è rilevante per la pianificazione. Per avere altre informazioni su queste impostazioni, passa con il mouse sopra di esse nell'interfaccia utente per vedere ulteriori dettagli.

- Appartenenza all’organico: quando [crei un dipendente con le impostazioni di base](#creare-un-dipendente), la data di assunzione viene impostata automaticamente. Qui puoi modificare la data di assunzione e impostare una data di licenziamento, se è necessario.

- Dati personali: inserisci i dati personali del dipendente, come, per esempio, l’indirizzo, il numero di telefono e il paese.

- Numeri tessera: inserisci il numero del tesserino di riconoscimento del dipendente, o i numeri di altri documenti personali.

- Ulteriori dati

Alcune delle impostazioni nella sezione Ulteriori dati sono rilevanti per la pianificazione, e altre no. La tabella seguente offre una panoramica delle impostazioni.

| Impostazione        | Rilevante per la pianificazione | Descrizione                |
|----------------| ------------------------|----------------------------|
|Colore       | No                      | Scegli un colore per identificare velocemente il dipendente nella pianificazione.  |
|Data e luogo di nascita  |       No |  Aggiungi la data e il luogo di nascita del dipendente.  |
|Posizione nel piano  | Sì | Definisce l’ordine per la funzionalità {% link_new Ordinamento in base alla posizione nel piano | features/scheduling/shiftcenter/sort-and-filter-items.md | #sort-the-items-of-a-level %} nel Centro dei turni. Il valore predefinito è 0 e il Centro dei turni ordinerà i dipendenti in ordine crescente.  |
|Assegnazione dei turni | Sì | Questa casella è spuntata per impostazione predefinita, ed è necessaria se vuoi che il dipendente venga pianificato in modo automatico. Se non vuoi che questo avvenga, devi deselezionare questa casella. Potrai comunque assegnare manualmente i turni e le rotazioni a questo dipendente.  |

## Utilizzare la modifica in blocco

In injixo Advanced e Enterprise WFM, puoi utilizzare la {% link_new funzionalità di modifica in blocco | features/administration/mass-update.md %} per modificare più dipendenti contemporaneamente.

## Assegnare una rotazione

Una rotazione è un insieme di modelli di orario o attività che si ripete regolarmente. Scopri come {% link_new creare le rotazioni | features/administration/shift-sequences.md %} e come inserirle nella tua pianificazione.

Per assegnare una rotazione, segui questi passaggi:

1. Nella sezione **Rotazioni**, clicca sull’icona Aggiungi {% icon item-add | icon-only %}.
2. Seleziona una rotazione.
3. Dal menu a tendina Riga dipendenti, seleziona la riga della {% link_new rotazione | features/administration/shift-sequences.md %} che vuoi assegnare al dipendente.
4. Specifica l’ordine di inserimento.<br>Questa impostazione è rilevante soltanto se hai bisogno di assegnare più di una rotazione a un dipendente. Le rotazioni con i valori più bassi vengono inserite per prime, e possono essere sovrascritte dalle rotazioni successive.
5. Imposta una {% link_new Data di riferimento | features/administration/reference-date.md %} che contrassegna il giorno d’inizio per la rotazione.
6. Clicca su _OK_{:.doc-button}.
Ora puoi {% link_new aggiungere delle rotazioni | features/scheduling/capacity/capacity-insert-shift-sequences.md %} alla pianificazione.

## Trasferire temporaneamente i dipendenti

Se i dipendenti lavorano spesso in altre unità di pianificazione per brevi periodi di tempo, puoi utilizzare la funzionalità Trasferisci temporaneamente per assegnare il dipendente a un’altra unità di pianificazione.

Durante il periodo di trasferimento, la nuova unità di pianificazione ha la priorità per la pianificazione. Al termine del periodo stabilito, il dipendente viene automaticamente pianificato nella sua vecchia unità di pianificazione. La funzionalità Trasferisci temporaneamente permette di risparmiare tempo, perché evita di dover riassegnare manualmente l’unità di pianificazione.

Per trasferire temporaneamente un dipendente, segui questi passaggi:

1. Seleziona un dipendente.
2. Vai alla sezione **Unità pianificative**.
3. Nell’intestazione della sezione, clicca sull’icona {% icon delegate-employees %}.
4. Seleziona l’unità di pianificazione alla quale vuoi trasferire il dipendente.
5. Inserisci la data di inizio e la data di fine del periodo di trasferimento.
6. Clicca su _OK_{:.doc-button}.

> Nota
>
> Un dipendente che è assegnato a diverse unità di pianificazione allo stesso tempo sarà sempre trasferito dall’unità di pianificazione con la priorità più alta.
