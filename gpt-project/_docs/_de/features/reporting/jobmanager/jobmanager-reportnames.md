---
title: JobManager Parameter für Reportnamen
toc: false
product_label:
  - enterprise
description: Erfahre mehr über dem cmd Parameter für die Definition von Reportnamen im JobManager.
---

Über den JobManager erstellte Reports benötigen in den {% link_new Jobverarbeitungsparametern | features/reporting/jobmanager/jobmanager.md %} einen Parameter *cmd*. Dieser definiert den jeweiligen Report. In diesem Artikel findest Du eine komplette Liste der Werte für den *cmd* Parameter zur Reporterstellung mit dem JobManager.

{{ 1 | image: 'JobManager Report per E-Mail versenden', '55%' }}

Einige Reports akzeptieren neben dem Namen zusätzliche Parameter:
- *showconsel* (Show Contracts And Selections)
- *hidefda* (Hide Full Day Activities)
- *showbreaks* (Show Breaks)

Diese Parameter sind dazu da, in einem Report bei gleichem *cmd* bestimmte Parameter ein- oder auszublenden. Nicht alle Reports unterstützen diese zusätzlichen Parameter.

<div class="table__wrapper table__with-subsections" markdown="1">

Report | CMD Parameter
------- | -------
Wochenpläne  |  
Wochenplan I | cmd=shiftplan
Wochenplan I mit Filter | cmd=shiftplan showconsel=1
Wochenplan I (ohne Ganztagsaktivitäten) | cmd=shiftplansel hidefda=1
Wochenplan II (ohne Ganztagsaktivitäten) | cmd=shiftplansel showbreaks=1 hidefda=1
Wochenplan II (ohne Pausen) | cmd=shiftplansel
Wochenplan (ohne Pausen) (ohne Ganztagsaktivitäten) | cmd=shiftplansel hidefda=1
Wochenplan III | cmd=weeklyworkplan
Wochenplan III (ohne Ganztagsaktivitäten) | cmd=weeklyworkplan hidefda=1
------- | -------
Tagespläne    |  
Tagesplan I | cmd=staffworkpubar
Tagesplan I mit Pausen | cmd=staffworkpubarbreaks
Tagesplan I (ohne Abwesenheiten, Krankheiten und Urlaub) | cmd=staffworkpubarabsences
Tagesplan II | cmd=staffworktimebar
Tagesplan II mit Pausen | cmd=staffworktimebarbreaks
Tagesplan II mit Schichtzusammenfassung | cmd=staffworktimebartotal
Tagesplan II mit Schichtzusammenfassung und mit Pause | cmd=staffworktimebartotalbreaks
Tagesplan III | cmd=staffworkactbar
Tagesplan III mit Pausen | cmd=staffworkactbarbreaks
Tagesplan IV | cmd=staffworkpubarsel
Tagesplan V | cmd=staffworktimebarsel
Tagesplan VI | cmd=staffworkactbarsel
------- | -------   
Urlaubs und Abwesenheitspläne |
Abwesenheitsplan | cmd=absence
Allgemeiner Abwesenheitsplan | cmd=realabsence
Abwesenheitsplan mit Tagesstatus und Ganztagsaktivitäten | cmd=orgabscalendar
Urlaubsplan I | cmd=holiday
Urlaubsplan I mit Vollzeitäquivalent | cmd=vacation_fte
Urlaubsplan II | cmd=vacationwithunpaid
------- | -------
Statistiken |
Abwesenheitsstatistik | cmd=absence_c
Abwesenheitsstatistik mit Summenspalte | cmd=absence_t
Abwesenheitsstatistik mit Vollzeitäquivalent | cmd=absence_fte
Urlaubsstatistik | cmd=holiday_c
Urlaubsstatistik mit Summenspalte | cmd=holiday_t
Urlaubsstatistik mit Vollzeitäquivalent | cmd=holiday_fte
Krankheitsstatistik | cmd=illness_c
Krankheitsstatistik mit Summenspalte | cmd=illness_t
Krankheitsstatistik mit Vollzeitäquivalent | cmd=illness_fte
------- | -------
Arbeitszeitreports |
Arbeitszeiten pro Planungseinheit | cmd=diff_pu
Aktivitäten in Stunden | cmd=activ_st
Aktivitäten in Prozent | cmd=activ_per
Aktivitätsstatistik | cmd=activity_stat
Nettoarbeitszeit | cmd=realized_hours
Aktivitätsanalyse | cmd=state_train
------- | -------
Pausenpläne |
Pausenplan I | cmd=pause
Pausenplan II | cmd=pausetwo
Pausenplan III | cmd=pausethree
------- | -------
Sonstige Reports |
Arbeitszeitdifferenz zwischen Ebenen | cmd=worktimes
Zeitkontenreport | cmd=timeacount
Schichten mit Bedarf | cmd=genshifts
Kapazitäten nach Vertragsart | cmd=capacity
Trainingsmodelle | cmd=train_camp_summary
Mindestbesetzung | cmd=minimalcoverage
Einstellungen der Planungsregeln | cmd=schedulingrules
Urlaubsübersicht | cmd=vacationoverview
Schichtübersicht | cmd=monthlyshiftplan
Jährliche Arbeitszeitanalyse | cmd=work_time_analysis
Planeinhaltung (Arbeitszeit) | cmd=conformance
Planeinhaltung (Aktivität) | cmd=adherence
------- | -------
Reports zu Tauschaktionen |
Tauschaktionen I | cmd=shiftexchdetails
Tauschaktionen II | cmd=shiftexchnodetails
Tauschstatistik | cmd=shiftexchstats
------- | -------
Mitarbeiterarbeitspläne |
Mitarbeiterarbeitsplan I (Liste) | cmd=staffwork showbreaks=1
Mitarbeiterarbeitsplan I (Liste) (ohne Pausen) | cmd=staffwork
Mitarbeiterarbeitsplan II (Liste) | cmd=staffworkabsill
Mitarbeiterarbeitsplan III (Grafik) | cmd=staffworkbar
Mitarbeiterarbeitsplan IV (6 Wochen) | cmd=staffsixweeksnobreaks
Mitarbeiterarbeitsplan IV (6 Wochen) (Aktivitäten) | cmd=staffsixweeks
Mitarbeiterarbeitsplan IV (6 Wochen) (ohne Pausen) | cmd=staffsixweekstwo
------- | -------
Weitere Mitarbeiterreports |
Mitarbeiterwunschplan I (Liste) | cmd=staff_wish
Arbeitszeiten je Mitarbeiter I | cmd=diff_st
Arbeitszeiten je Mitarbeiter II | cmd=diff_st_two
Monatsjournal Mitarbeiter | cmd=journal
Organigramm | cmd=organ
Wochenendarbeitsreport I | cmd=weekendwork
Wochenendarbeitsreport II | cmd=weekendwork2
Wochenendarbeitsreport III (Verlosung und Zuteilung) | cmd=weekendwork3
Jubiläumsreport | cmd=jubilee |
Urlaubsschein | cmd=hd_list
Mitarbeiter pro Vertragsart | cmd=read
Fluktuationsreport I | cmd=fluct
Fluktuationsreport II | cmd=detailfluctuation
Jahresübersicht | cmd=absencejob_cal |
Ausgleichstage für Wochenendarbeit | cmd=comp_week_work
Mitarbeiterschichtfolgen | cmd=staffshiftseq
Arbeitszeitplan | cmd=monthly_work_sched
Arbeitsplatz | cmd=assignedworkplaces
Feiertagsarbeit (Verlosung und Zuteilung) | cmd=laaholidaywork
Mindestbelegung nach Standort | cmd=deskminstaffing
Arbeitsplatzbelegung | cmd=deskalloc
Stammdatengültigkeit | cmd=masterdatavalidity
Coach/Trainee - Plandifferenz | cmd=coach_trainee
Stammdatenübersicht | cmd=employeemasterdata
Benutzergruppenrechte | cmd=group_auth
Stammdatenänderungen | cmd=audit

</div>