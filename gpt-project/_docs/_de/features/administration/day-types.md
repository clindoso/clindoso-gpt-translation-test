---
title: Tagestypen erstellen und verwenden
description: Erfahre, was Tagestypen sind, wofür sie verwendet werden und wie Du sie erstellen, bearbeiten und löschen kannst.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/planning-calendar.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/scheduling-public-holidays.md
---

Tagestypen definieren die Standard-Wochentage und Tage mit unterschiedlichen Öffnungszeiten oder abweichendem Mitarbeiterbedarf. Verwende Tagestypen in der Konfiguration deiner Planungseinheit und im Planungskalender.

Unter _WFM > Administration > Scheduling > Tagestypen_{:.breadcrumbs} findest du die Standard-Wochentage (Montag-Sonntag), die nicht gelöscht werden können. Du kannst eigene Tagestypen hinzufügen, z.&nbsp;B. Tage mit Werbeaktionen oder Feiertage.

## Feiertagsmodus

Wenn du einen benutzerdefinierten Tagestyp mit aktiviertem Feiertagsmodus in einen Planungskalender einfügst, wird die Sollarbeitszeit der Mitarbeiter an diesem Tag reduziert. Wenn der Feiertagsmodus nicht aktiviert ist, verhält sich der Tag wie ein normaler Arbeitstag, aber du kannst trotzdem unterschiedliche Öffnungszeiten für diesen Tag in der Planungseinheit festlegen.

Hinweis: Wenn du den Feiertagsmodus eines bereits verwendeten Tagestyps ändern, musst du die Zeitkonten oder Richtzeitkonten neu berechnen.

## Tagestypen für Feiertage automatisch erstellen

{% link_new Füge eine Kalendervorlage in einen Planungskalender ein | features/administration/planning-calendar.md %}, um automatisch die in der Vorlage enthaltenen Feiertage als Tagestypen zu erstellen. Für diese Tagestypen ist der Feiertagsmodus standardmäßig aktiviert.

## Eigene Tagestypen erstellen

1. Gehe zu _WFM > Administration > Scheduling > Tagestypen_{:.breadcrumbs}.
2. Klicke auf das {% icon item-add %} in der Aktionsleiste.
3. Gib einen **Namen** ein.
4. Gib eine **Abkürzung** ein. Diese wird im Planungskalender verwendet.
5. (Optional) Aktiviere die Checkbox **Feiertagsmodus**, um den Tagestyp als Feiertag zu markieren.
6. Klicke auf _Ok_{:.doc-button}.

## Tagestypen in der Planung berücksichtigen

Bei der Planung werden nur diejenigen Tagestypen berücksichtigt, die Du in der Planungseinheit mit {% link_new Öffnungszeiten | features/administration/create-and-manage-planning-units.md %}#öffnungszeiten-hinzufügen) hinterlegt hast. Zusätzlich musst Du alle Tagestypen mit Ausnahme der voreingestellten Standard-Wochentage im {% link_new Planungskalender | features/administration/planning-calendar.md %} an den jeweiligen Tagen einfügen. Damit der Planungskalender bei der Planung berücksichtigt wird, musst Du ihn der Planungseinheit hinzufügen.

## Tagestypen bearbeiten oder löschen

Klicke auf den Tagestyp in der Liste. Ein Bearbeitungsfenster öffnet sich auf der rechten Seite. Um einen Tagestyp zu löschen, benutze _![delete button](/assets/img/common/item-delete.gif)_{:.doc-button-icon} in der Aktionsleiste.

> Bevor Du einen Tagestyp löschst, entferne den Tagestyp aus allen Planungskalendern.
