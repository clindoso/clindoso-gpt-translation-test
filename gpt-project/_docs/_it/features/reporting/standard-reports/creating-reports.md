---
title: Generare report
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Generare report standard in formato HTML o PDF con diversi parametri.
toc: false
related_articles:
  - overwrite_title: Inviare report via email
    filepath: features/reporting/standard-reports/email-reports.md
  - overwrite_title: Report sulle unità pianificative
    filepath: features/reporting/standard-reports/planning-unit-reports.md
  - overwrite_title: Report sui dipendenti
    filepath: features/reporting/standard-reports/employee-reports.md
---

Leggendo questo articolo, scoprirai:
- come generare report basati su diversi parametri e filtri;
- come vengono mostrati i fusi orari nei report.

I report contengono diversi tipi di dati, come, per esempio, i turni pianificati sulla base di diversi livelli, o i dati di configurazione. Scopri di più sui {% link_new report sulle unità di pianificazione | features/reporting/standard-reports/planning-unit-reports.md %} e i {% link_new report sui dipendenti | features/reporting/standard-reports/employee-reports.md %}. È possibile generare report in formato HTML e in formato PDF.

> Alcuni report sono basati su gruppi di selezione. Questi report avranno un contenuto solo se assegni almeno un {% link_new gruppo di selezione | features/administration/selections.md %} ai dipendenti. 

## Generare report

1. Vai su *WFM > Monitoring > Report*{:.breadcrumbs}.
2. Seleziona una **Data d’inizio** e una **Data di fine**.

3. Utilizza la sezione **Filtro** per scegliere che cosa verrà incluso nel report:

    - **Filtro standard**: seleziona una **Unità pianificativa**, un **Contratto**, o un **Gruppo di selezione** per sfoltire l’elenco dei dipendenti. Per selezionare più voci, clicca con il mouse mentre tieni premuto il tasto **CTRL** oppure **Shift**.

        {{ 2 | image: 'Filtro standard', '90%' }}

    - **Filtro personalizzato**: seleziona un {% link_new filtro personalizzato | features/administration/employee-filter.md %} per creare una lista personalizzata di dipendenti, per esempio in base alle qualifiche. Per creare un nuovo filtro, clicca su **Editor filtri**.

      <br>Spunta la casella **Filtra nel periodo scelto per il report** per sovrascrivere la data d’inizio e la data di fine selezionate nella schermata principale Report.  

      {{ 3 | image: 'Filtro personalizzato', '60%' }}  

      I filtri personalizzati non sono disponibili in injixo Essential WFM.

4. Clicca su *Applica*{:.doc-button}.

5. (Facoltativo) Nella sezione **Dipendenti**, seleziona dei singoli **Dipendenti**.

    {{ 5 | image: 'Sezione Dipendenti', '60%' }}

6. Nella sezione **Parametri**, è possibile:
    - selezionare il **Livello** dal quale verranno estratti i dati; 
    - impostare il **Formato** del report (PDF oppure HTML);
    - scegliere di {% link_new inviare report via email | features/reporting/standard-reports/email-reports.md %} a utenti specifici;
    - rendere anonimi i nomi e i numeri di matricola dei dipendenti.

    {{ 4 | image: 'Parametri dei report', '30%' }}

7. A destra, nella sezione **Report sulle unità pianificative** oppure **Report sui dipendenti**, seleziona un tipo di report.

    {{ 6 | image: 'Sezioni con elenchi di report', '30%' }}

    <br>
    Le icone accanto ai report indicano per quale periodo è possibile generare il report:
    - _![icon showing a single file](/assets/img/common/report-icon-single-file.png)_{:.doc-button-icon}: periodo massimo di un mese;
    - _![icon showing multiple files](/assets/img/common/report-icon-multiple-files.png)_{:.doc-button-icon}: periodo massimo di un anno. 

Si apre la finestra di Elaborazione del processo. Il report richiesto viene generato e mostrato.

È possibile creare più di un report con gli stessi parametri. Se modifichi un filtro oppure una data, clicca su *Applica*{:.doc-button}.

## Fusi orari nei report

Gli orari nei report si riferiscono al fuso orario dell’unità di pianificazione. L’intestazione del report mostra la differenza tra il fuso orario dell’unità di pianificazione e il fuso orario UTC, e la differenza tra il fuso orario dell’unità di pianificazione e il fuso orario locale dell’utente.

Esempio: Un dipendente a New York comincia il turno alle 8:30. Un report utilizza l’ora di Manchester (Regno Unito), che è l’ora dell’unità di pianificazione. La differenza di fuso orario è +05:00. Il dipendente deve sottrarre questa differenza all’orario mostrato sul report per sapere a che ora comincia il suo turno. 
