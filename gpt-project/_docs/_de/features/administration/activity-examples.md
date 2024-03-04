---
title: Konfigurationsbeispiele für Aktivitäten
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: false
description: Richte mit Hilfe von Beispielen Standardaktivitäten ein.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

Um zu konfigurieren, wie injixo mit Aktivitäten während der Schichtplanung und beim Reporting umgeht, verwende die {% link_new Aktivitätstypen und -eigenschaften | features/administration/activity-types-and-properties.md %} unter _Plan > Konfiguration > Aktivitäten_{:.breadcrumbs}.

Im folgenden findest du einige Konfigurationsbeispiele für häufig verwendete Aktivitäten, ihren Typ und passende Eigenschaften.

## Anwesenheit, Pause, Krankheit und Urlaub

Diese Tabelle enthält Konfigurationsbeispiele für die Aktivitätstypen Anwesenheit, Pause, Krankheit und Urlaub.
Die Aktivität Anwesend ist eine vorkonfigurierte Standardaktivität in injixo. Du kannst sie für alle Aktivitäten verwenden, an denen deine Mitarbeiter arbeiten und die auf Mitarbeiterbedarf basieren, z.&nbsp;B. Anrufe. 

<div class="table__wrapper" markdown="1">

<style>
table {
   width: 100%;
}
</style>

|                                        |  Anwesend  | Mittagspause |         Krankheit         |  Urlaub |
| ------------------------------------------- | :---------------------: | :----------------------: | :---------------------: | :---------------------: |
| **Typ**                                        |         Anwesenheit         |          Pause           |         Krankheit         |        Urlaub         |
| Bezahlt                                        | <i class="fa fa-check"> |                          | <i class="fa fa-check"> | <i class="fa fa-check"> |
| Ruhezeit einhalten                     | <i class="fa fa-check"> |                          |                         |
| Planbar                                   | <i class="fa fa-check"> |                          |                         |
| Wünschbar in Me                                 |                         | <i class="fa fa-check">  |                         | <i class="fa fa-check"> |
| Ersetzbar                                 | <i class="fa fa-check"> |                          |                         |
| Tauschbar beim Schichttausch            | <i class="fa fa-check"> | <i class="fa fa-check">  |                         |
| Ganztägig erlauben                  |                         |                          | <i class="fa fa-check"> | <i class="fa fa-check"> |

</div>

Je nachdem, was in deinen Unternehmensrichtlinien, Verträgen oder Arbeitsgesetzen festgehalten ist, können manche Pausen auch unbezahlt sein. Deaktiviere in diesem Fall die Checkbox **Bezahlt**.

## Abwesenheiten und Meetings

Diese Tabelle enthält Konfigurationsbeispiele für die Aktivitätstypen Abwesenheit und Meeting.
Bezahlte Abwesenheiten werden in der Regel verwendet, um Überstunden auszugleichen oder als Blocker für die {% link_new Planung von Feiertagen | best-practices/scheduling-public-holidays.md %}.
Wenn ein Mitarbeiter an manchen Tagen keinesfalls arbeiten kann, kannst du diese Tage blockieren, indem du die Konfiguration entsprechend der Spalte Unbezahlte Abwesenheit einrichtest.

<div class="table__wrapper" markdown="1">

|                                          | Bezahlte Abwesenheit | Unbezahlte Abwesenheit |    Ganztägiges Meeting     |  Schulung  |
| --------------------------------------------- | :-----------------------: | :-------------------------: | :---------------------: | :---------------------: |
| **Typ**                                          |          Abwesenheit          |           Abwesenheit           |         Meeting         |         Meeting         |
| Bezahlt                                          |  <i class="fa fa-check">  |                             | <i class="fa fa-check"> | <i class="fa fa-check"> |
| Ruhezeit einhalten                       |                           |                             | <i class="fa fa-check"> |
| Planbar                                     |                           |                             |                         |
| Wünschbar in Me                                   |  <i class="fa fa-check">  |   <i class="fa fa-check">   |                         |
| Ersetzbar                                   |                           |                             |                         |
| Tauschbar beim Schichttausch              |                           |                             |                         |
| Ganztägig erlauben                    |  <i class="fa fa-check">  |   <i class="fa fa-check">   |                         | <i class="fa fa-check"> |

</div>

Du kannst bezahlte Abwesenheiten auch als Ausgleichstage für Überstunden oder als bezahlte Blocker verwenden, wenn du {% link_new Feiertage planst | best-practices/scheduling-public-holidays.md %}.<br>
Mit der Aktivität Unbezahlte Abwesenheit kannst du flexibel festlegen, dass ein Mitarbeiter an bestimmten Tagen keinesfalls geplant wird.