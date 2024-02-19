---
title: Einen Schichtplan erstellen
description: Führe die grundlegenden Schritte aus, um einen Schichtplan zu erstellen.
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/resolve-optimization-issues.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/why-level-copy.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/meetings/meetings-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-extra-activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-replace-activities.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/scheduling-public-holidays.md
redirect_from:
  - /de/quickstart-scheduling/
redirect_reason: Updated filename on 27 July 2023
---

Das Erstellen von Schichtplänen ist ein grundlegender Bestandteil des {% link_new WFM-Kreislaufs | getting-started/the-wfm-cycle-in-injixo.md %}. In Schichtplänen sind die für deine Mitarbeiter geplanten Schichten und Aktivitäten enthalten.  

Verwende diesen Artikel als ergänzende Checkliste für dein Onboarding.

Hinweis: In injixo Essential WFM kannst du weder Urlaubsanträge noch den finalen Schichtplan als Backup sichern.

## Voraussetzungen

Bevor du einen Schichtplan erstellst, stelle sicher, dass du deine {% link_new Grundkonfiguration korrekt eingerichtet | getting-started/set-up-base-configuration.md %} und einen {% link_new Forecast erstellt | getting-started/calculate-a-forecast.md %} hast. 

## Konfigurationsreihenfolge

Wir empfehlen, die Konfigurationselemente in der Reihenfolge einzurichten, die in diesem Artikel vorgestellt wird. Keine Konfiguration ist wie die andere. Deshalb kann die optimale Reihenfolge für dein Unternehmen anders aussehen. Besprich dich mit deinem Consultant, falls du Fragen hast.

## Abwesenheiten konfigurieren

Deine Mitarbeiter können in injixo Me Abwesenheiten beantragen. Konfiguriere Abwesenheiten unter _Plan > Urlaub/Abwesenheiten_{:.breadcrumbs}.

1. Gib den {% link_new Urlaubsanspruch | features/scheduling/time-off/vacation-entitlement.md %} deiner Mitarbeiter für das laufende Jahr ein.
2. Lege eine {% link_new Abwesenheitsperiode | features/scheduling/time-off/time-off-periods.md %} an und veröffentliche diese. Eine Abwesenheitsperiode legt den Zeitraum fest, in dem deine Mitarbeiter Urlaub und andere Abwesenheiten beantragen können. Deine Mitarbeiter erhalten eine Benachrichtigung in injixo Me und können ab dann Abwesenheitsanträge für diesen Zeitraum erstellen.

## Krankheit oder Abwesenheitsaktivitäten eintragen

Unter {% link_new Schedules | features/scheduling/schedules/schedules-overview.md %} und im {% link_new Schicht Center | features/scheduling/shiftcenter/shift-center-overview.md %} kannst du den Schichtplan deines Teams verwalten. Gib bereits bekannte {% link_new Aktivitäten | features/administration/activity-types-and-properties.md | #aktivitätstypen %} vom Typ Abwesenheit oder Krankheit in den Schichtplan ein.

## Abwesenheitsanträge verwalten

Unter _Plan > Urlaub/Abwesenheiten_{:.breadcrumbs} kannst du {% link_new offene Anträge genehmigen oder ablehnen | features/scheduling/time-off/vacation-absences-management.md %}.

> Erstelle ein Backup des aktuellen Schichtplans in einer anderen Ebene
>
> Verwende die Funktion {% link_new Ebeneninhalte kopieren | features/scheduling/schedules/schedules-copy-level-content.md %}, um eine Kopie deines Schichtplans zu sichern. So stellst du sicher, dass du keine genehmigten Abwesenheitsanträge oder kürzlich eingetragenen Abwesenheiten verlierst, wenn du den Schichtplan löschst und erneut erstellst.

## Den Schichtplan erzeugen

Sieh unter {% link_new Schedules | features/scheduling/schedules/schedules-overview.md %},  im {% link_new Schicht Center | features/scheduling/shiftcenter/shift-center-overview.md %} oder unter {% link_new Dashboards | features/monitoring/dashboards/dashboards-overview.md %} nach, ob der {% link_new Mitarbeiterbedarf | features/forecast/injixo-forecast/staff-requirement.md %}, für deine Aktivitäten korrekt eingetragen ist.

1. Füge {% link_new Schichtfolgen | features/scheduling/schedules/schedules-insert-shift-sequences.md %} für deine Mitarbeiter hinzu.
2. Konfiguriere zusätzliche {% link_new Planungsmethoden | features/scheduling/scheduling-methods.md %} und verwende diese, um den Schichtplan fertigzustellen.
3. Führe die {% link_new Joboptimierung | features/scheduling/schedules/schedules-job-optimization.md %} aus. Du kannst diesen Schritt überspringen, wenn du {% link_new einen optimierten Schichtplan erstellst | features/scheduling/schedules/schedules-optimized-schedules.md %}.

Tipp: Wenn du zu Testzwecken einen Schichtplan erstellst, kannst du die Funktion {% link_new Ebenen leeren | features/scheduling/schedules/schedules-empty-levels.md %} verwenden. Kopiere die gespeicherten Urlaubs- und Abwesenheitsanträge vor jedem Testlauf zurück in die Ebene Plan.

## Deinen fertigen Schichtplan sichern

Bevor du {% link_new manuelle Änderungen | features/scheduling/shiftcenter/modify-items.md %} an deinem ursprünglichen Schichtplan vornimmst, {% link_new erstelle ein Backup | features/scheduling/schedules/schedules-copy-level-content.md %} in der Ebene Aktueller Stand. So kannst du  deinen ursprünglichen Schichtplan später mit geänderten Versionen abgleichen und die Qualität bewerten.

## Den Schichtplan veröffentlichen und Schichttausch erlauben

1. Erstelle eine {% link_new Planperiode | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-see-their-schedules.md %}, damit deine Mitarbeiter ihren Schichtplan in injixo Me einsehen können.
2. (Optional) {% link_new Erlaube Mitarbeitern, Schichten zu tauschen | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}.  
    Standardmäßig musst du {% link_new offene Schichttauschanfragen einsehen und genehmigen | features/scheduling/view-approve-shift-swap-requests.md %}. Mit der Einstellung _48152_{:.id-label} **Tauschmodus** kannst du den automatischen Tausch zwischen Mitarbeitern aktivieren.
3. Teile den Artikel {% link_new Finde dich zurecht | features/injixo-me/use-injixo-me/explore-injixo-me.md %} mit deinen Mitarbeitern.
