---
title: Öffnungszeiten aktivieren
product_label:
  - advanced
  - enterprise
  - classic
toc: false
description: Verstehe, wie du Öffnungszeiten aktivieren kannst und wie sie sich auf den Forecast auswirken.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

Neu in injixo Forecast? Lerne zuerst {% link_new die Grundlagen | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

Standardmäßig beachten Workloads keine Öffnungszeiten und Forecasts berücksichtigen das gesamte Tagesvolumen.

injixo Classic unterstützt Öffnungszeiten nur in Smart-Workloads.

## Wie wirken sich Öffnungszeiten auf die Forecast-Berechnung aus?

Wenn Du Öffnungszeiten in einem Workload aktivierst:

- nutzt injixo die sich überschneidenden Öffnungszeiten der zugeordneten Planungseinheit und Aktivität. Jedes Intervall innerhalb dieses Zeitraums gilt als offen.
- werden alle Volumen außerhalb der Öffnungszeiten auf einen Zeitraum innerhalb der Öffnungszeiten verteilt. Das tägliche Gesamtvolumen ändert sich nicht. Die Verteilung erfolgt relativ zu den bestehenden Intervallwerten und folgt damit dem prognostizierten Intraday-Muster. Volumen außerhalb der Öffnungszeiten erhalten den Wert 0.
- werden alle prognostizierten AHT-Werte außerhalb der Öffnungszeiten auf 0 gesetzt.

## Öffnungszeiten aktivieren

Um alle Volumen außerhalb der Öffnungszeiten in die Forecast-Berechnung einzubeziehen, aktiviere die Öffnungszeiten in jedem Workload einzeln.

1. Gehe zu _Forecast_{:.menu-item}.
2. Wähle einen Workload mit einer der folgenden Optionen:
   - Wähle einen Workload aus dem Dropdown-Menü am oberen Bildschirmrand.
   - Gib den Workload-Namen in das Suchfeld ein.
   - Klicke auf einen Workload in der Liste
3. Klicke auf _Workload bearbeiten_{:.doc-button}.
4. Wähle eine **Planungseinheit** und **Aktivität**.
5. Aktiviere die Checkbox **Forecast nur innerhalb der Öffnungszeiten**.
6. Klicke auf _Workload speichern_{:.doc-button}.
   injixo berechnet einen neuen Forecast. Dies kann einige Zeit in Anspruch nehmen.

Wichtig: Konfiguriere für den Forecast-Zeitraum gültige Öffnungszeiten und Aktivitäten in der ausgewählten Planungseinheit, um die Forecast-Erstellung zu gewährleisten. Entferne/ändere ggf. {% link_new Gültig von- bzw. Gültig bis-Angaben | features/administration/set-a-validity-period.md %}.

## Wie werden Öffnungszeiten angezeigt?

injixo Forecast zeigt die Öffnungszeiten in der Tagesansicht mit einem orangefarbenen Balken an:

{{ 1 | image: "Oranger Balken zur Anzeige der aktivierten Öffnungszeiten in einem Workload", '80%' }}

Hinweis: Zusätzliche {% link_new Benutzerrechte | getting-started/configure-user-roles.md %} für den Planungskalender der Planungseinheit können erforderlich sein, um den orangefarbenen Balken für die Öffnungszeiten anzuzeigen. Gehe zu _WFM > Administration > System > Rollenrechte_{:.breadcrumbs} und füge dem betroffenen Benutzer oder der Benutzergruppe Rechte für den Planungskalender hinzu.
