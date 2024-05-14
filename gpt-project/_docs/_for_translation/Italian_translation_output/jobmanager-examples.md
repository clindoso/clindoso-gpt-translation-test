---
title: Esempi di JobManager <!-- GPT translation -->
product_label:
  - enterprise
description: Scopri i tipi di attività più importanti in injixo, e come sono utilizzati. <!-- GPT translation -->
gpt_translation: true
---

In _WFM > Administration > System > JobManager_{:.breadcrumbs}, puoi pianificare l’avvio dei processi più lunghi, come la creazione di report o l’inserimento di rotazioni. Durante la creazione di un modello di processo, dovrai {% link_new impostare dei parametri specifici | features/reporting/jobmanager/jobmanager.md | #set-job-processing-parameters %}. <!-- GPT translation -->

Questo articolo mostra come impostare diversi tipi di processi in JobManager. <!-- GPT translation -->


<style> <!-- TM 100 -->
table { <!-- TM 100 -->
   width: 20%; <!-- TM 79 -->
} <!-- TM 100 -->

table th:first-of-type { <!-- TM 100 -->
   width: 20%; <!-- TM 87 -->
} <!-- TM 100 -->
table th:nth-of-type(2) { <!-- TM 100 -->
   width: 20%; <!-- TM 87 -->
} <!-- TM 100 -->
</style> <!-- TM 100 -->

## Creare un workload <!-- TM 68 -->

<!-- {{ 1 | image: 'Sending Job Manager Report via Email', '50%' }} -->


| Proprietà                                    | Effetto                 | <!-- TM 68 -->
| --------------- | -------------------------------------------------------------------- |
| Proprietà                                    | Effetto                 | <!-- TM 62 -->
| Proprietà                                    | Effetto                 | <!-- TM 63 -->
| e               | Dipendenti<br>Valori: all, ID dipendente singolo, ID dipendente singolo delimitato dal trattino (-)     | <!-- GPT translation -->
| c               | Contratti<br>Valori: all, ID contratto singolo, ID contratto singolo delimitato dal trattino (-)     | <!-- GPT translation -->
| se              | Gruppi di selezione<br>Valori: all, ID selezione delimitati dal trattino (-)    | <!-- GPT translation -->
| Proprietà                                    | Effetto                 | <!-- TM 61 -->
| lid             | [ID della lingua](#id-lingua)                                          | <!-- GPT translation -->
| targethtml      | Formato di output<br>Valori: 0 (PDF), 1 (HTML)                           | <!-- GPT translation -->
| targetanonymous | Standard o Anonimo<br>Valori: 0 (standard), 1 (anonimo) | <!-- GPT translation -->
| jobnameid       | (Facoltativo) ID del report interno che può essere in bianco                      | <!-- GPT translation -->


Tutti i report che automatizzi con JobManager richiedono il parametro cmd. Espandi l’elenco qui sotto per vedere che valore devi assegnare al parametro cmd per ogni tipo di report: <!-- GPT translation -->

<details style="padding-bottom: 20px;">
<summary><strong>Weekly schedule reports</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Descrizione</th> <!-- TM 65 -->
      <th>Valore del parametro del comando</th> <!-- GPT translation -->
    </tr>
  </thead>
  <tr>
    <td>Orario settimanale I</td> <!-- GPT translation -->
    <td>shiftplan</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>shiftplan con filtro</td> <!-- GPT translation -->
    <td>shiftplan showconsel=1</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Pianificazione settimanale I (senza attività di giorno intero)</td> <!-- GPT translation -->
    <td>shiftplansel hidefda=1</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Piano settimanale II (senza FDA)</td> <!-- GPT translation -->
    <td>shiftplansel showbreaks=1 hidefda=1</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Piano settimanale II (senza interruzioni) (solo per l’installazione in locali)</td> <!-- GPT translation -->
    <td>shiftplansel</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Piano settimanale (senza interruzioni) (senza attività a giornata intera)</td> <!-- GPT translation -->
    <td>shiftplansel hidefda=1</td> <!-- GPT auto-propagation -->
  </tr>
  <tr>
    <td>shiftplansel hidefda=1</td> <!-- GPT translation -->
    <td>shiftplansel hidefda=1</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Weekly Schedule III (senza attività a giornata completa)</td> <!-- GPT translation -->
    <td>weeklyworkplan hidefda=1</td> <!-- GPT translation -->
  </tr>
</table>
</details>  

<details style="padding-bottom: 20px;">
<summary><strong>Daily schedule reports</strong>
</summary> <!-- GPT translation -->
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Descrizione</th> <!-- TM 65 -->
      <th>Valore del parametro del comando</th> <!-- GPT auto-propagation -->
    </tr>
  </thead>
  <tr>
    <td>	Fascia oraria (1)</td> <!-- GPT translation -->
    <td>staffworkpubar</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Orario tipo I con pause</td> <!-- GPT translation -->
    <td>staffworkpubarbreaks</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Orario tipo I (senza assenze, malattie e ferie) </td> <!-- GPT translation -->
    <td>staffworkpubarabsences</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Orario settimanale II</td> <!-- GPT translation -->
    <td>staffworktimebar</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Programmazione giornaliera con pause – II</td> <!-- GPT translation -->
    <td>staffworktimebarbreaks</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Orario giornaliero II con sommario dei turni</td> <!-- GPT translation -->
    <td>staffworktimebartotal</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Calendario giornaliero II con sommario dei turni e pause</td> <!-- GPT translation -->
    <td>staffworktimebartotalbreaks</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Pianificazione giornaliera III</td> <!-- GPT translation -->
    <td>stafffworkactbar</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Orario La <nobr>III</nobr> con pause</td> <!-- GPT translation -->
    <td>staffworkactbarbreaks</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Piano di attività IV</td> <!-- GPT translation -->
    <td>staffworkpubarsel</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Orario settimanale flessibile</td> <!-- GPT translation -->
    <td>staffworktimebarsel</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>staffworktimebarsel</td> <!-- GPT translation -->
    <td>staffworkactbarsel</td> <!-- GPT translation -->
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Vacation and absence schedule</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Descrizione</th> <!-- TM 65 -->
      <th>Valore del parametro del comando</th> <!-- GPT auto-propagation -->
    </tr>
  </thead>
  <tr>
    <td>Pianificazione assenze</td> <!-- GPT translation -->
    <td>assenza</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Pianificazione assenze flessibili</td> <!-- GPT translation -->
    <td>realabsence</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Real-time riepiloghi_</td> <!-- GPT translation -->
    <td>orgabscalendar</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Calendario ferie I</td> <!-- GPT translation -->
    <td>festività</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Polizza dei permessi I con orario pieno</td> <!-- GPT translation -->
    <td>ferie_fte</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Calendario per le ferie II</td> <!-- GPT translation -->
    <td>staffworktimebartotal</td> <!-- GPT auto-propagation -->
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Absence, illness- and vacation statistics</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Descrizione</th> <!-- TM 65 -->
      <th>Valore del parametro del comando</th> <!-- GPT auto-propagation -->
    </tr>
  </thead>
  <tr>
    <td>Statistica assenze</td> <!-- GPT translation -->
    <td>ass_c</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Statistiche sulle assenze con la somma totale</td> <!-- GPT translation -->
    <td>absence_t</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Statistiche sulle assenze in formato FTE</td> <!-- GPT translation -->
    <td>assenza_fte</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Statistiche sulle ferie</td> <!-- GPT translation -->
    <td>holiday_c</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Statistiche sui permessi con la colonna dell’importo totale</td> <!-- GPT translation -->
    <td>festivi_t</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Statistica sulle ferie con l’equivalente a tempo pieno</td> <!-- GPT translation -->
    <td>holiday_fte</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Statistiche assenze per malattia</td> <!-- GPT translation -->
    <td>illness_c</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Statistiche sulle malattie con colonna dell’importo totale</td> <!-- GPT translation -->
    <td>illness_t</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Statistiche sulle malattie con equivalente a tempo pieno (ETP)</td> <!-- GPT translation -->
    <td>malattia_etp</td> <!-- GPT translation -->
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Work time reports</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Descrizione</th> <!-- TM 65 -->
      <th>Valore del parametro del comando</th> <!-- GPT auto-propagation -->
    </tr>
  </thead>
  <tr>
    <td>Tempo lavorato Volte per unità di pianificazione</td> <!-- GPT translation -->
    <td>diff_pu</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Attività in ore</td> <!-- GPT translation -->
    <td>activ_st</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>attività_st</td> <!-- GPT translation -->
    <td>attività_st</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>attività_st</td> <!-- GPT translation -->
    <td>attività\_st</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Attività lavorative nette (solo per on-premise)</td> <!-- GPT translation -->
    <td>realized_hours</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Analisi delle attività</td> <!-- GPT translation -->
    <td>state_train</td> <!-- GPT translation -->
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Break schedules</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Descrizione</th> <!-- TM 65 -->
      <th>Valore del parametro del comando</th> <!-- GPT auto-propagation -->
    </tr>
  </thead>
  <tr>
    <td>Break Schedule I</td> <!-- GPT translation -->
    <td>pausa</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>pausa</td> <!-- GPT translation -->
    <td>pausetwo</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>pausetwo</td> <!-- GPT translation -->
    <td>pausethree</td> <!-- GPT translation -->
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Other reports</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Descrizione</th> <!-- TM 65 -->
      <th>Valore del parametro del comando</th> <!-- GPT auto-propagation -->
    </tr>
  </thead>
  <tr>
    <td>Differenza tra i livelli nel tempo di lavoro</td> <!-- GPT translation -->
    <td>worktimes</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Rapporti sui conti del tempo</td> <!-- GPT translation -->
    <td>Rapporto sul conto del tempo</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Turni con fabbisogno</td> <!-- GPT translation -->
    <td>genshifts</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Numero di giorni fino alla fine del mese con turni notturni, turni del fine settimana e turni festivi (disponibile solo per l'installazione locale)</td> <!-- GPT translation -->
    <td>shifttype</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Quantità secondo il tipo di contratto</td> <!-- GPT translation -->
    <td>capacity</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Training Programs (Solo On-premise)</td> <!-- GPT translation -->
    <td>train_camp_summary</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Organico minimo (solo On-premise)</td> <!-- GPT translation -->
    <td>minimalcoverage</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Configurazione delle regole di pianificazione</td> <!-- GPT translation -->
    <td>schedulingrules</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Pianificazione delle ferie</td> <!-- GPT translation -->
    <td>vacationoverview</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Processi programmati: panoramica dei turni</td> <!-- GPT translation -->
    <td>monthlyshiftplan</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Ore di lavoro annuali</td> <!-- GPT translation -->
    <td>work_time_analysis</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Compliance Report</td> <!-- GPT translation -->
    <td>conformità</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Report di conformità</td> <!-- GPT translation -->
    <td>aderenza</td> <!-- GPT translation -->
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Exchange reports</strong>
</summary> <!-- GPT auto-propagation -->
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Descrizione</th> <!-- TM 65 -->
      <th>Valore del parametro del comando</th> <!-- GPT auto-propagation -->
    </tr>
  </thead>
  <tr>
    <td>Exchanges I (Solo su infrastruttura locale)</td> <!-- GPT translation -->
    <td>shiftexchdetails</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Scambi II (solo per on-premise)</td> <!-- GPT translation -->
    <td>shiftexchnodetails</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>shiftexchnodetails</td> <!-- GPT translation -->
    <td>shiftexchstats</td> <!-- GPT translation -->
  </tr>
</table>
</details>

<details style="padding-bottom: 20px;">
<summary><strong>Employee work schedules</strong></summary>
<br>
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Descrizione</th> <!-- TM 65 -->
      <th>Valore del parametro del comando</th> <!-- GPT auto-propagation -->
    </tr>
  </thead>
  <tr>
    <td>Ciclo orario dei dipendenti I (elenco)</td> <!-- GPT translation -->
    <td>staffwork showbreaks=1</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Orario di lavoro dei dipendenti I (elenco) (senza interruzioni)</td> <!-- GPT translation -->
    <td>staffwork</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Orario di lavoro del dipendente II (elenco)</td> <!-- GPT translation -->
    <td>staffworkabsill</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Orario di lavoro dipendente — Assillo</td> <!-- GPT translation -->
    <td>staffworkbar</td> <!-- GPT translation -->
  </tr>  
  <tr>
    <td>Cronologia orario IV (6 sett.)</td> <!-- GPT translation -->
  <td>staffsixweeksnobreaks</td> <!-- GPT translation -->
  </tr>  
  <tr>
    <td>Tabellone dei dipendenti IV (6 settimane) (Attività)</td> <!-- GPT translation -->
    <td>dipendentisixweeks</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Employee Work Schedule IV (6 Weeks) (No Breaks)</td> <!-- GPT translation -->
    <td>staffsixweekstwo</td> <!-- GPT translation -->
  </tr>
</table>
</details>

<details style="padding-bottom: 40px;">
<summary><strong>Other employee reports</strong></summary>
<br>
<table>
  <thead>
    <tr>
      <th>Descrizione</th> <!-- TM 65 -->
      <th>Valore del parametro <strong>cmd</strong></th> <!-- GPT translation -->
    </tr>
  </thead>
  <tr>
    <td>Dipendente richiede pianificazione I (elenco) (Solo on-premise)</td> <!-- GPT translation -->
    <td>staff_wish</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>staff_wish</td> <!-- GPT translation -->
    <td>diff_st</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Ore lavorate per dipendente II</td> <!-- GPT translation -->
    <td>diff_st_two</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Registro mensile del dipendente (solo per on-premise)</td> <!-- GPT translation -->
    <td>registro</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Organigramma</td> <!-- GPT translation -->
    <td>organ</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Weekend Lavorativo I</td> <!-- GPT translation -->
    <td>weekendwork</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>weekendwork</td> <!-- GPT translation -->
    <td>weekendwork2</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>weekendwork3</td> <!-- GPT translation -->
    <td>weekendwork3</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Anniversaries</td> <!-- GPT translation -->
    <td>jubileo</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Cedolino vacanze (solo per l’installazione su server locale)</td> <!-- GPT translation -->
    <td>hd_list</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Elenco del personale</td> <!-- GPT translation -->
    <td>read</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Fluttuazione I</td> <!-- GPT translation -->
    <td>fluct</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>fluct II</td> <!-- GPT translation -->
    <td>dettaglifluttuazione</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Sguardo d’insieme annuale (Solo per l'installazione in locale)</td> <!-- GPT translation -->
    <td>absencejob_cal</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>assenzaind_ric.comp</td> <!-- GPT translation -->
    <td>comp_week_work</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>comp_week_work</td> <!-- GPT translation -->
    <td>staffshiftseq</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>staffshiftseq</td> <!-- GPT translation -->
    <td>monthly_work_sched</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Workplace (solo per on-premise)</td> <!-- GPT translation -->
    <td>assignedworkplaces</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Permessi (estrazione e assegnazione)</td> <!-- GPT translation -->
    <td>laaholidaywork</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Occupazione minima siti (solo On-premise)</td> <!-- GPT translation -->
    <td>deskminstaffing</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Occupazione Postazione (Solo on-premise)</td> <!-- GPT translation -->
    <td>deskalloc</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Validità dei dati di base (solo per on-premise)</td> <!-- GPT translation -->
    <td>masterdatavalidity</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Discrepanze tra pianificazioni dei supervisor e dei dipendenti (solo On-premise)</td> <!-- GPT translation -->
    <td>coach_trainee</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Master Data Overview</td> <!-- GPT translation -->
    <td>employeemasterdata</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Autorizzazione per i gruppi (disponibile solo per l'installazione locale)</td> <!-- GPT translation -->
    <td>group_auth</td> <!-- GPT translation -->
  </tr>
  <tr>
    <td>Modificare i dati principali</td> <!-- GPT translation -->
    <td>audit</td> <!-- GPT translation -->
  </tr>
</table>
</details>


## Inserire le rotazioni <!-- TM 100 -->

<!-- {{ 2 | image: 'Insert Shift Sequences', '50%' }} -->

| Parametro        | Descrizione                                                                                                                                                                                                      | <!-- TM 64 -->
| ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
   | Opzione                           | Descrizione                                                                                             | <!-- TM 64 -->
   | Opzione                           | Descrizione                                                                                             | <!-- TM 62 -->
   | Opzione                           | Descrizione                                                                                             | <!-- TM 60 -->
| Periodo con dati di bassa qualità     | Consiglio                                                                                                                                                         | <!-- TM 63 -->
| Periodo con dati di bassa qualità     | Consiglio                                                                                                                                                         | <!-- TM 61 -->
   | Opzione                           | Descrizione                                                                                             | <!-- TM 61 -->
| Periodo con dati di bassa qualità     | Consiglio                                                                                                                                                         | <!-- TM 62 -->
| Periodo con dati di bassa qualità     | Consiglio                                                                                                                                                         | <!-- TM 65 -->
| selection_id | ID del gruppo di selezione                                                                                                                  | <!-- GPT translation -->
| shiftseq_id  | Elenco degli ID delle rotazioni assegnate ai dipendenti selezionati, separati da un trattino (-). É richiesto, a meno che il campo type sia impostato.                   | <!-- GPT translation -->
| tipo         | (Facultativo) Se utilizzato, seleziona tutte le rotazioni per i dipendenti selezionati. Seleziona questo valore Se utilizzato, il parametro shiftseq_id deve essere vuoto.<br>Valore: all. | <!-- GPT translation -->

### Estrazione e assegnazione <!-- GPT translation -->

<!-- {{ 3 | image: 'Lottery or Assignment', '50%' }} -->

| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 84 -->
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 77 -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 73 -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 78 -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 72 -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 69 -->
| periodid    | L’ID di un periodo di pianificazione, o più ID, separati da virgola. L’ID corretto è visibile nel codice sorgente della pagina tramite gli strumenti per gli sviluppatori (è la prima parte del valore dell’elemento data-flip-id), oppure può essere ricavato tramite l’[API](https://legacy-api.injixo.com/#tag/Planning-Periods/operation/getV1PlanningPeriodsStartDate). Se il periodo di tempo per l’elaborazione delle attività è impostato come periodo relativo, verrà preso in considerazione solo il periodo di pianificazione rilevante. | <!-- GPT translation -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 81 -->
| Valutazione collegamento parte giusta (%) (tasso di connessioni riuscite) | La percentuale di chiamate alle quali rispondono gli interlocutori desiderati. Seleziona **fisso** e inserisci un valore nel campo sottostante, o seleziona **variabile** e seleziona un tipo di valore con una previsione sul tasso di connessioni riuscite.                                                                                                                                                                                                                                                             | <!-- TM 64 -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 63 -->

### Copia del livello <!-- GPT translation -->

La funzionalità **Copia il contenuto del livello** si trova in _Plan > Schedules > Azioni di pianificazione_{:.breadcrumbs}. <!-- GPT translation -->

| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 84 -->
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| copystartdate | La data di inizio per l’inserimento dei dati in [formato data giuliana](https://www.onlineconversion.com/julian_date.htm). I dati vengono spostati se la data non è la data di inizio del periodo di pianificazione. | <!-- GPT translation -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 69 -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 76 -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 74 -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 73 -->
| periodid      | ID interno del periodo di pianificazione, o un elenco di ID separati da virgola. Puoi trovare l’ID di un periodo di pianificazione nella sorgente di pagina utilizzando gli strumenti di sviluppo (è la prima parte del valore dell’elemento data-flip-id) oppure utilizzare l'[API](https://legacy-api.injixo.com/#tag/Planning-Periods/operation/getV1PlanningPeriodsStartDate). Se il periodo per l’elaborazione dei processi di pianificazione è impostato come relativo, vengono presi in considerazione solo i periodi di pianificazione rilevanti. | <!-- GPT translation -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 71 -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 77 -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 78 -->
| Valutazione collegamento parte giusta (%) (tasso di connessioni riuscite) | La percentuale di chiamate alle quali rispondono gli interlocutori desiderati. Seleziona **fisso** e inserisci un valore nel campo sottostante, o seleziona **variabile** e seleziona un tipo di valore con una previsione sul tasso di connessioni riuscite.                                                                                                                                                                                                                                                             | <!-- TM 62 -->
| Parametro                    | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <!-- TM 70 -->

### Parametri di calcolo <!-- TM 62 -->

I parametri email sono facoltativi. Se i parametri email non sono configurati, i report saranno disponibili soltanto nel JobProcessor. <!-- GPT translation -->

| Parametro        | Descrizione                                                                      | <!-- TM 65 -->
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Parametro        | Descrizione                                                                                                                                                                                                      | <!-- TM 72 -->
| Parametro        | Descrizione                                                                                                                                                                                                      | <!-- TM 71 -->
| sendperemp | Invio di un’email separata al dipendente selezionato. Non è disponibile per tutti i report <!-- quali? -->.<br>Valori: 1 (sì), 0 (no)                                                                                                       | <!-- GPT translation -->
| email      | L’indirizzo email del destinatario. Non sono supportati indirizzi email multipli. Utilizza, se necessario, un gruppo di distribuzione per l’invio interno a più destinatari. Il parametro email non viene utilizzato quando le richieste del servizio v2/be/em specificano degli ID. | <!-- GPT translation -->
| tipoemail  | Indirizzo email del dipendente<br>Valori: 1 (email 1), 3 (email 2), 2 (entrambi). Le versioni di injixo Cloud non supportano l’email 2.                                                                                                             | <!-- GPT translation -->
| fisso/variabile   | Seleziona **fisso** e inserisci dei valori fissi nei campi sottostanti, oppure seleziona **variabile** e inserisci dei tipi di valori nei campi sottostanti.                                                                                                                                                                                                                         | <!-- TM 61 -->

## ID dell’interfaccia <!-- GPT translation -->

Il parametro **lid** definisce l’ID della lingua del report scaricato e accetta i seguenti valori: <!-- GPT translation -->

Inglese (Stati Uniti, 1033)<br> <!-- GPT translation -->
Tedesco (1031)<br> <!-- GPT translation -->
Francese (1036)<br> <!-- GPT translation -->
Italiano (1040)<br> <!-- GPT translation -->
Spagnolo moderno (3082)<br> <!-- GPT translation -->
Spagnolo standard (1034)<br> <!-- GPT translation -->
Olandese (1043)<br> <!-- GPT translation -->
Svedese (1053)<br> <!-- GPT translation -->
Inglese (Regno Unito) (2057)<br> <!-- GPT translation -->
Polacco (1045) <!-- GPT translation -->

## ID del livello <!-- GPT translation -->

Il parametro **level** definisce il livello a partire dal quale vengono letti i dati e accetta i seguenti ID: <!-- GPT translation -->

1000 (plan)<br> <!-- GPT translation -->
3000 (stato attuale)<br> <!-- GPT translation -->
5000 (sistema esterno)<br> <!-- GPT translation -->
4000 (fascia di tempo)<br> <!-- GPT translation -->
2000 (richiesta)<br> <!-- GPT translation -->
2001 (richiesta alternativa)<br> <!-- GPT translation -->
2002 (richiesta di permesso/vacanza)<br> <!-- GPT translation -->
6000 (disponibilità)<br> <!-- GPT translation -->
6001 (turni di reperibilità)<br> <!-- GPT translation -->
4001 (diversificazione)<br> <!-- GPT translation -->
8000 (versione 1)<br> <!-- GPT translation -->
8001 (versione 2)<br> <!-- GPT translation -->
8002 (versione 3)<br> <!-- GPT translation -->