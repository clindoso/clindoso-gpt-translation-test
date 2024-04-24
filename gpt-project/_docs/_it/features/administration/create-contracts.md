---
title: Creare i contratti
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Crea i contratti per definire le ore lavorative settimanali e altre regole per i dipendenti.
redirect_from:
  - /it/contract-creation/
redirect_reason: Updated filename on 08 December 2023
---

In _Plan > Configurazione > Contratti_{:.breadcrumbs} puoi inserire i contratti per i dipendenti che vuoi pianificare. Puoi creare un numero illimitato di contratti. I contratti ti permettono di definire dei vincoli temporali per la pianificazione:

- il numero minimo e massimo di giorni lavorativi alla settimana;
- il numero minimo, nominale e massimo di ore lavorative al giorno;
- il numero minimo, nominale e massimo di ore lavorative alla settimana;
- il numero massimo di ore lavorative al mese.

I contratti rispecchiano anche le politiche che regolano l'orario di lavoro nella tua organizzazione, per esempio il numero di giorni di riposo tra un turno e l’altro. Puoi anche definire i parametri di pianificazione per la funzionalità **Crea una pianificazione ottimizzata**.

## Creare un contratto

Per creare un nuovo contratto, vai su _Plan > Configurazione > Contratti_{:.breadcrumbs} e segui i passaggi elencati di seguito:

1. Clicca sull'icona Nuovo {% icon item-add | icon-only %} in alto a sinistra.
2. Nella sezione **Generale**, inserisci le informazioni di base del contratto:<br>
    - **Nome**: inserisci un nome unico (massimo 50 caratteri).
    - **Abbreviazione**: inserisci il nome o una sua versione più breve (massimo 25 caratteri).
    - **Colore**: il colore ti può servire a identificare velocemente il contratto.
3. Alla voce **Giorni lav. alla settimana** inserisci il numero di giorni lavorativi per settimana.
4. Alla voce **Calcolo dei giorni lavorativi**, scegli un metodo di calcolo. <br>
    - **Standard**: rispetta l’ordine dei giorni nella settimana di pianificazione.<br>
    - **Flessibile**: sceglie liberamente i giorni lavorativi all’interno dell’orario di apertura dell’unità di pianificazione.
5. Inserisci l’[**Orario di lavoro di riferimento**](#orario-di-lavoro-di-riferimento) e la [**Distribuzione orario lavorativo**](#distribuzione-orario-lavorativo).
6. (Facoltativo) Configura i [**Parametri per l'AutoScheduler**](#parametri-per-lautoscheduler) e i [**Parametri di pianificazione**](#regole-di-pianificazione).
7. Per salvare il contratto, clicca su _OK_{:.doc-button}.

## Orario di lavoro di riferimento

L’orario di lavoro di riferimento per il numero minimo, nominale e massimo di ore lavorative è indispensabile per la pianificazione. L’orario di lavoro di riferimento agisce in combinazione con i parametri di configurazione e i parametri per l’AutoScheduler.

### Giorno

- **Minimo**: inserisci il numero minimo di ore lavorative al giorno. Se non inserisci nessun valore, il valore nominale che configuri sarà utilizzato come valore minimo. Questo parametro viene verificato dalla regola di pianificazione _2615_{:.id-label}&nbsp;.
- **Nominale**: inserisci il numero ottimale di ore lavorative al giorno. Inserisci un valore compreso tra 0 e 24 ore e prendi in considerazione gli orari di lavoro standard.
- **Massimo**: inserisci il numero massimo di ore lavorative al giorno. Se non inserisci nessun valore, il valore nominale sarà utilizzato come valore massimo. Questo parametro viene verificato dalla regola di pianificazione _2614_{:.id-label}&nbsp;.

### Settimana

- **Minimo**: inserisci il numero minimo di ore lavorative alla settimana. Puoi impostare l’inizio della settimana di pianificazione con l’impostazione _48420_{:.id-label}&nbsp;. Puoi definire il numero di giorni del fine settimana con l’impostazione _48421_{:.id-label}&nbsp;.
- **Nominale**: inserisci il numero ottimale di ore lavorative alla settimana. Questo valore è indispensabile se non inserisci nessun valore nella sezione **Distribuzione orario lavorativo**. Puoi impostare l’inizio della settimana di pianificazione con l’impostazione _48420_{:.id-label}&nbsp;.
- **Massimo**: inserisci il numero massimo di ore lavorative alla settimana. Questo parametro viene verificato dalle regole di pianificazione _2618_{:.id-label} e _2629_{:.id-label}&nbsp;.

### Mese

- **Massimo**: inserisci il numero massimo di ore lavorative al mese. Questo parametro viene verificato dalla regola di pianificazione _2619_{:.id-label}&nbsp;.

## Distribuzione orario lavorativo

Puoi definire il numero di ore lavorative giornaliere per i dipendenti che hanno questo contratto. Nella configurazione dell’**Orario di lavoro di riferimento** questa sezione è facoltativa. Tuttavia, questo valore è utile per calcolare le assenze retribuite, come le ferie o le malattie.

Esempio:
un dipendente lavora 40 ore alla settimana per 8 ore al giorno e non lavora il mercoledì e la domenica. Per garantire che le ore lavorative siano ben distribuite lungo la settimana, inserisci 8:00 nei campi del lunedì, del martedì, del giovedì, del venerdì e del sabato. Inserisci 0:00 nei campi del mercoledì e della domenica. Se questo dipendente prende un giorno di malattia o di ferie retribuite, le sue ore lavorative saranno comunque calcolate sulla base delle ore che hai inserito qui.

Se lasci il campo vuoto, per impostazione predefinita verrà applicata la seguente formula: [numero di ore nominali settimanali/numero di giorni lavorativi]. Questo potrebbe causare degli errori di calcolo perché injixo darà per scontata una distribuzione uniforme delle ore lavorative su tutti i giorni lavorativi.

## Parametri per l’AutoScheduler

- **Numero massimo di giorni lavorativi consecutivi**: compila questo campo se la tua unità di pianificazione è aperta 7 giorni su 7. inserisci il numero massimo di giorni non lavorativi consecutivi che la funzionalità **Crea una pianificazione ottimizzata** deve tenere in considerazione. Per esempio, se un dipendente lavora 5 giorni alla settimana, utilizza questo parametro per evitare che lavori per 10 giorni consecutivi.
- **Numero minimo di giorni liberi a settimana**: compila questo campo se la tua unità di pianificazione è aperta durante i fine settimana. Inserisci il numero minimo di giorni non lavorativi che la funzionalità **Crea una pianificazione ottimizzata** deve tenere in considerazione per ogni settimana di pianificazione.
- **Numero minimo di giorni liberi consecutivi a settimana**: compila questo campo per far sì che i dipendenti abbiano dei giorni liberi consecutivi ogni settimana. Inserisci il numero minimo di giorni non lavorativi consecutivi alla settimana che la funzionalità **Crea una pianificazione ottimizzata** deve rispettare per ogni settimana di pianificazione.
- **Numero massimo di giorni liberi consecutivi**: compila questo campo se vuoi limitare il numero di giorni liberi consecutivi dei dipendenti per garantire livelli di personale consistenti ed evitare pause lunghe. Inserisci il numero massimo di giorni non lavorativi consecutivi che la funzionalità **Crea una pianificazione ottimizzata** deve tenere in considerazione. Questo valore non viene verificato per ogni settimana, ma in rapporto a tutte le settimane.
- **Numero minimo di ore di riposo tra due turni**: compila questo campo per rispettare le leggi sul lavoro in materia di riposo tra un turno e l’altro. Inserisci il numero minimo di ore di riposo tra due turni consecutivi che la funzionalità **Crea una pianificazione ottimizzata** deve tenere in considerazione.	
- **Numero minimo di giorni lavorativi alla settimana**: compila questo campo per mantenere un livello minimo di personale su base settimanale nella tua unità di pianificazione, per garantire che ci siano sempre dipendenti sufficienti a gestire il volume di chiamate previsto. Inserisci il numero minimo di giorni lavorativi che devono essere pianificati per ogni settimana di pianificazione.
- **Conto delle ore dovute anziché valore nominale alla settimana previsto dal contratto**: spunta questa casella se vuoi che la funzionalità **Crea una pianificazione ottimizzata** utilizzi i valori provenienti dai conti delle ore dovute. Scopri di più sui {% link_new conti delle ore dovute | features/scheduling/planning-periods/target-work-accounts.md %}.
- **Max. un sabato lavorativo ogni N settimane**: compila questo campo se vuoi garantire una distribuzione equa del lavoro nei fine settimana ed evitare che siano sempre gli stessi dipendenti a lavorare di sabato. Inserisci il numero massimo di settimane (da 1 a 5) nelle quali un dipendente può lavorare di sabato. Per esempio, il valore 2 significa un sabato sì e uno no.
- **Pianifica turno dopo un giorno intero di ferie**: compila questo campo se vuoi che la funzionalità **Crea una pianificazione ottimizzata** pianifichi un giorno lavorativo dopo un giorno intero di ferie. Se il dipendente ha più giorni di ferie consecutivi, il giorno lavorativo viene pianificato dopo l’ultimo giorno di ferie.

## Regole di pianificazione

Le regole di pianificazione stabiliscono un insieme di regole generali e legate ai contratti per il processo di pianificazione. Nella configurazione del contratto, le regole di pianificazione sono chiamate parametri di pianificazione.

Per vedere l’elenco delle regole di pianificazione disponibili, vai su _WFM > Administration > Sistema > Regole di pianificazione_{:.breadcrumbs}. Per vedere la descrizione di una regola, clicca sulla rispettiva regola nell’elenco. Le regole di pianificazione solitamente vengono configurate insieme al consulente injixo durante l’onboarding.

Gli utenti con accesso amministratore possono modificare le regole, impostare le eccezioni e persino riportare i valori specifici degli utenti ai valori preimpostati.

> Possibile rischio di errori di pianificazione
>
> Le modifiche alle regole di pianificazione sono complesse e possono causare errori di pianificazione se vengono fatte in modo errato. Non modificare le regole di pianificazione se non hai la certezza assoluta delle conseguenze. Se devi modificare una regola di pianificazione, contatta il tuo consulente.

Le regole di pianificazione specifiche per i contratti garantiscono che le condizioni di ogni contratto siano prese in considerazione durante la pianificazione. Per esempio, se un contratto specifica la durata del periodo di riposo o il numero massimo di ore lavorative al giorno, le regole di pianificazione garantiscono che queste condizioni vengano rispettate. Violare queste regole può causare conflitti nella pianificazione, insoddisfazione dei dipendenti e potenziali violazioni contrattuali.

### Indicatore di stato

È possibile vedere lo stato di ogni regola di pianificazione nell’elenco:

  - Grigio: la regola è disattivata e non verrà tenuta in considerazione durante la pianificazione.
  - Giallo: la regola è attiva in modalità trasgredibile. La violazione di questa regola causa un avvertimento durante la pianificazione, ma l’azione continua.
  - Rosso: la regola è attiva in modalità intrasgredibile. Ogni violazione del contratto causa un messaggio di errore che contiene dettagli sulla violazione della regola.
  