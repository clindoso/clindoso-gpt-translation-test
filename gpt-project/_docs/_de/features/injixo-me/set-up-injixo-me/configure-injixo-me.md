---
title: injixo Me konfigurieren
description: Konfiguriere injixo Me, um Mitarbeitern z.B. zu ermöglichen, Schichtwünsche abzugeben, Schichten mit Teamkollegen zu tauschen und Abwesenheiten zu beantragen.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/use-injixo-me/explore-injixo-me.md
  - overwrite_title: Add title for untranslated source
    filepath: features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md
redirect_from:
  - /de/injixo-me-administration/
  - /de/configure-injixo-me/
redirect_reason: Updated filename on 03 July 2023
---

In diesen Artikel lernst Du, wie Du Deinen Mitarbeitern ermöglichst:

- Schichtwünsche abzugeben.
- Schichten mit anderen Mitarbeitern zu tauschen.
- Urlaub oder andere Abwesenheiten zu beantragen.
- Den eigenen Schichtplan einzusehen.
- Die Schichtpläne von Teamkollegen einzusehen.
- Eigene Verfügbarkeiten für bestimmte Zeiträume anzugeben.

Als Benutzer mit _Admin-Zugriff_, klicke auf _Me_{:.menu-item} in der Hauptnavigation, um die verfügbaren Mitarbeiterportal-Features zu aktivieren/deaktivieren. Klicke auf einen **Schalter**, um das entsprechende Feature an- oder auszuschalten.

> Hinweis
>
> Mitarbeiter benötigen für den Zugriff auf injixo Me einen eigenen injixo Account, um die beschriebenen Funktionen nutzen zu können. Erfahre, wie Du {% link_new Accounts für Deine Mitarbeiter erstellst | features/injixo-me/set-up-injixo-me/give-employees-access-to-injixo-me.md %}.

## Schichtwünsche

Mitarbeiter können sich Schichten aus einem Schicht-Pool wünschen, der zuvor basierend auf dem Mitarbeiterbedarf und Schichtbedarf erstellt wurde. Die Schichten werden dann in einer Verlosung verteilt und verbleibende Schichten können manuell zugeteilt werden. Lerne mehr über das {% link_new Schichtwunsch-Verfahren | features/scheduling/schedules/schedules-shift-bidding.md %}.

{{ 1 | image: 'Shift bidding', '70%' }}

## Schichttauschbörse

Mitarbeiter können Schichten oder freie Tage eigenständig mit anderen Mitarbeitern tauschen. Das funktioniert folgendermaßen:

1. Eine Schicht wird von einem Mitarbeiter zum Tausch angeboten.
2. Ein anderer Mitarbeiter sieht das Angebot und akzeptiert den Schichttausch.
3. Die Schichten werden getauscht.

Lerne darüber {% link_new wie Du Deinen Mitarbeitern den Schichttausch ermöglichst | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %}. Über den [Team Kalender](#team-kalender) können die Mitarbeiter die Arbeitszeiten ihrer Teamkollegen sehen. Abhängig von Deiner injixo-Konfiguration, musst Du auch {% link_new offene Tauschanträge genehmigen | features/scheduling/view-approve-shift-swap-requests.md %}.

{{ 2 | image: 'Schichttausch', '50%' }}

## Abwesenheitsanträge

Mitarbeiter können Abwesenheiten für {% link_new Aktivitäten | features/administration/activity-types-and-properties.md | #aktivitätstypen %} des Typ _Abwesenheit_, _Urlaub_ oder _Krankheit_ für Zeiträume von ein paar Stunden bis hin zu mehreren Wochen beantragen. Sie können außerdem ihren jährlichen Urlaubsanspruch und die verbleibenden Urlaubstage einsehen.

Lerne mehr darüber, wie {% link_new Deine Mitarbeiter Abwesenheiten beantragen können | features/scheduling/time-off/time-off-periods.md %}. Steuere die Art und Weise, wie Mitarbeiter Abwesenheitsanträge einreichen können mit Einstellungen zum {% link_new Urlaubsanspruch | features/scheduling/time-off/vacation-entitlement.md %}, {% link_new Genehmigungsregeln | features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md %} und {% link_new Quoten | features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md %}.

{{ 3 | image: 'Dialog um einen Abwesenheitsantrag einzugeben', '50%' }}

> Nur Aktivitäten vom Typ _Urlaub_ beeinflussen den Urlaubsanspruch.

## Team Kalender

Mitarbeiter können über den Menüpunkt **Team Kalender** die Arbeitszeiten ihrer Teamkollegen sehen, die zur selben {% link_new Auswahl | features/administration/selections.md %} gehören. Der Kalender zeigt die Anwesenheitszeiten, Pausen und Urlaubstage, aber nicht die Namen der Aktivitäten.

{{ 4 | image: 'Team Kalendar', '80%' }}

## Verfügbarkeiten

Mitarbeiter können über den Menüpunkt **Verfügbarkeiten** spezielle Zeiten definieren, an denen sie für die Planung verfügbar oder nicht verfügbar sind. Dabei ist es möglich, Zeiträume von beliebiger Länge zu definieren, unabhängig z.B. von den vertraglich festgelegten Arbeitsstunden. Lerne mehr über die Planung mit {% link_new Verfügbarkeiten | features/scheduling/scheduling-methods.md | #verfügbarkeiten %}.

Falls Deine Mitarbeiter zu kurze Zeitfenster eintragen, können evtl. Teile des Schichtplans nicht erstellt werden. Prüfe daher im letzten Schritt vor der Planerstellung, welche Verfügbarkeiten Deine Mitarbeiter eingetragen haben.

{{ 5 | image: 'Dialog zum Eintragen von Verfügbarkeiten', '50%' }}

## Urlaubsanspruch in Stunden

Durch diese Einstellung wird der Urlaub des Mitarbeiters in Stunden statt wie üblicherweise in Tagen angezeigt. Dies betrifft den gewünschten, verbleibenden und genehmigten Urlaub. Mitarbeiter können sich ihren Urlaub unter dem Menüpunkt **Abwesenheit** ansehen.

Diese Einstellung beeinflusst nicht die Anzeige von Tages- und Stundenwerten in anderen Bereichen von injixo wie z.B. den Bereichen **Urlaubs-/Abwesennheitsverwaltung** und **Urlaubsanspruch**.

{{ 6 | image: 'Urlaubsanspruch in Stunden', '40%' }}
