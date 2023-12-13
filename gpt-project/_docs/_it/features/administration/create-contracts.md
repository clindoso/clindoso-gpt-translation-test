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

In _WFM > Administration > Scheduling > Contratti_{:.breadcrumbs}, è possibile inserire i contratti per i dipendenti che vuoi pianificare. Puoi creare un numero illimitato di contratti. Con i contratti è possibile definire dei vincoli temporali per la pianificazione:

- il numero minimo e massimo di giorni lavorativi alla settimana;
- il numero minimo, nominale e massimo di ore lavorative al giorno;
- il numero minimo, nominale e massimo di ore lavorative alla settimana.

I contratti rispecchiano anche le politiche che regolano il tempo lavorativo nella tua organizzazione, per esempio il numero di giorni di riposo tra i turni. Puoi definire anche i parametri di pianificazione per la funzionalità Crea una pianificazione ottimizzata.

## Creare un contratto

1. Clicca sull’icona Nuovo {% icon item-add | icon-only %}.
2. Nella sezione **Generale**, inserisci le informazioni di base per il contratto:<br>
    - Inserisci un **Nome** (massimo 50 caratteri).
    - Inserisci un’**Abbreviazione** (massimo 25 caratteri).
    - Seleziona un **colore**.
3. Alla voce **Giorni lav. alla settimana**, inserisci il numero di giorni lavorativi per settimana.
4. Alla voce **Calcolo dei giorni lavorativi**, scegli un metodo di calcolo. <br>
    - **Standard**: rispetta l’ordine dei giorni nella settimana di pianificazione.<br>
    - **Flessibile**: sceglie liberamente i giorni lavorativi all’interno dell’orario di apertura dell’unità di pianificazione.
5. Inserisci l’[**Orario di lavoro di riferimento**](#orario-di-lavoro-di-riferimento) e la [**Distribuzione orario lavorativo**](#distribuzione-orario-lavorativo).
6. (Facoltativo) Configura i [**Parametri per l'AutoScheduler**](#parametri-per-lautoscheduler) e i **Parametri di pianificazione**.
7. Per salvare il contratto, clicca su _OK_{:.doc-button}.

## Orario di lavoro di riferimento

L’orario di lavoro di riferimento per il numero minimo, nominale e massimo di ore lavorative è indispensabile per la pianificazione. L’orario di lavoro di riferimento agisce in combinazione con le Regole di pianificazione e le Impostazioni.

### Giorno

- **Minimo**: inserisci il numero minimo di ore lavorative al giorno. Se non inserisci nessun valore, il valore nominale che configuri sarà considerato come valore minimo. Questo parametro viene verificato dalla regola di pianificazione _2615_{:.id-label}.
- **Nominale**: inserisci il numero ottimale di ore lavorative al giorno. Inserisci un valore compreso tra le 0 e le 24 ore e prendi in considerazione gli orari di lavoro standard.
- **Massimo**: inserisci il numero massimo di ore lavorative al giorno. Se non inserisci nessun valore, il valore nominale che configuri sarà considerato come valore massimo. Questo parametro viene verificato dalla regola di pianificazione _2614_{:.id-label}.

### Settimana

- **Minimo**: inserisci il numero minimo di ore lavorative alla settimana. Puoi impostare l’inizio della settimana di pianificazione con l’impostazione _48420_{:.id-label}. Puoi definire il numero di giorni del fine settimana con l’impostazione _48421_{:.id-label}.
- **Nominale**: inserisci il numero ottimale di ore lavorative alla settimana. Questo valore è indispensabile se non inserisci nessun valore alla voce Distribuzione orario lavorativo. Puoi impostare l’inizio della settimana di pianificazione con l’impostazione _48420_{:.id-label}.
- **Massimo**: inserisci il numero massimo di ore lavorative alla settimana. Questo parametro viene verificato dalle regole di pianificazione _2618_{:.id-label} e _2629_{:.id-label}. 

### Mese

- **Massimo**: inserisci il numero massimo di ore lavorative al mese. Questo parametro viene verificato dalla regola di pianificazione _2619_{:.id-label}.

## Distribuzione orario lavorativo

Puoi definire il numero di ore lavorative giornaliere per i dipendenti con questo contratto. Se hai configurato l’orario di lavoro di riferimento, qui non è necessario inserire nessun valore. Ad ogni modo, questo valore è utile per calcolare le assenze retribuite, come le ferie o le malattie.

Esempio:
un dipendente ha un permesso retribuito un venerdì, e il suo contratto prevede 8 ore lavorative il venerdì. Per quel giorno verranno conteggiate 8 ore lavorative.

Inserisci il numero massimo di ore lavorative per ogni giorno lavorativo. Per i giorni non lavorativi inserisci 0:00 ore. Se lasci il campo vuoto, per impostazione predefinita verrà applicata la seguente formula: [numero di ore nominali settimanali/numero di giorni lavorativi]. Questo potrebbe causare degli errori di calcolo.

## Parametri per l’AutoScheduler


- **Numero massimo di giorni lavorativi consecutivi**: inserisci il numero massimo di giorni lavorativi consecutivi che la funzionalità Crea una pianificazione ottimizzata deve tenere in considerazione. Questo campo può restare vuoto per le unità di pianificazione senza un orario di apertura nei fine settimana. Per esempio, se un dipendente lavora 5 giorni alla settimana, utilizza questo parametro per evitare che lavori per 10 giorni consecutivi.
- **Numero minimo di giorni liberi a settimana**: inserisci il numero minimo di giorni non lavorativi che la funzionalità Crea una pianificazione ottimizzata deve tenere in considerazione per ogni settimana di pianificazione. Questo campo può restare vuoto per le unità di pianificazione senza un orario di apertura nei fine settimana.
- **Numero minimo di giorni liberi consecutivi a settimana**: inserisci il numero minimo di giorni non lavorativi consecutivi per settimana che la funzionalità Crea una pianificazione ottimizzata deve rispettare per ogni settimana di pianificazione.
- **Numero massimo di giorni liberi consecutivi**: inserisci il numero massimo di giorni non lavorativi consecutivi che la funzionalità Crea una pianificazione ottimizzata deve tenere in considerazione. Questo valore non viene controllato per ogni settimana, ma in rapporto a tutte le settimane.
- **Numero minimo di ore di riposo tra due turni**: inserisci il numero minimo di ore di riposo tra due turni consecutivi che la funzionalità Crea una pianificazione ottimizzata deve tenere in considerazione.	
- **Numero minimo di giorni lavorativi alla settimana**: inserisci il numero minimo di giorni lavorativi che devono essere pianificati per ogni settimana di pianificazione.
- **Conto delle ore dovute anziché valore nominale alla settimana previsto dal contratto**: spunta questa casella se vuoi utilizzare i valori provenienti dai conti delle ore dovute nella funzionalità Crea una pianificazione ottimizzata. Scopri di più sui {% link_new conti delle ore dovute | features/scheduling/planning-periods/target-work-accounts.md %}.
- **Max. un sabato lavorativo ogni N settimane**: inserisci il numero massimo di settimane (da 1 a 5) nelle quali un dipendente può lavorare di sabato. Per esempio, il valore 2 significa che il dipendente può lavorare di sabato a settimane alterne.
- **Pianifica turno dopo un giorno intero di ferie**: impone alla funzionalità Crea una pianificazione ottimizzata di pianificare un giorno lavorativo dopo un giorno intero di ferie. Se il dipendente ha più giorni di ferie consecutivi, il giorno lavorativo viene pianificato dopo l’ultimo giorno di ferie.