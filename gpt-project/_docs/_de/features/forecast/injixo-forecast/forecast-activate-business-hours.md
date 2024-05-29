---
title: Öffnungszeiten aktivieren
product_label:
  - advanced
  - enterprise
  - classic
toc: true
description: Erfahre, wie du Öffnungszeiten aktivieren kannst und wie sie sich auf den Forecast auswirken.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
---

Neu bei injixo Forecast? Lerne zuerst {% link_new die Grundlagen| features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

Standardmäßig berücksichtigen Workloads keine Öffnungszeiten und Forecasts basieren auf dem Gesamtvolumen pro Tag. In der Workload-Konfiguration kannst du konfigurieren, dass injixo Öffnungszeiten berücksichtigt und sie im Forecast anzeigt. Standardmäßig berücksichtigt der Mitarbeiterbedarf die Öffnungszeiten.

Wenn du für deine Planungseinheit keine Öffnungszeiten konfigurierst, zeigt die Forecast-Seite keinen Mitarbeiterbedarf an.

injixo Classic unterstützt Öffnungszeiten nur bei Smart Workloads.

## Voraussetzungen

Stelle sicher, dass folgendes zutrifft:

- Du hast für die Planungseinheit, für die du Öffnungszeiten aktivieren möchtest, bereits gültige {% link_new Öffnungszeiten | features/administration/create-and-manage-planning-units.md | #öffnungszeiten-hinzufügen %} und {% link_new Aktivitäten | features/administration/activities.md %} konfiguriert.
- Du hast die Einträge in den Feldern {% link_new **Gültig vom**/**Gültig bis** | features/administration/set-a-validity-period.md %} für die dem Workload zugewiesene Planungseinheit und Aktivität überprüft und ggf. entfernt bzw. angepasst.
- Du hast die nötigen Berechtigungen, um die entsprechenden Planungseinheiten sehen und bearbeiten zu können.
- Falls der Planungseinheit ein Planungskalender zugewiesen ist, hast du dafür ebenfalls die nötigen {% link_new Berechtigungen | getting-started/configure-user-roles.md | #berechtigungen-für-wfm-konfigurieren %}, um die Öffnungszeiten anzuzeigen.

## Öffnungszeiten aktivieren

Um alle Volumen außerhalb der Öffnungszeiten in die Forecast-Berechnung einzubeziehen, aktiviere die Öffnungszeiten für jeden Workload einzeln.

1. Wähle unter _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Klicke auf _Bearbeiten_{:.doc-button}.
3. Wähle im Abschnitt **Grundkonfiguration** eine Planungseinheit und eine Aktivität aus.
4. Aktiviere die Checkbox **Forecast nur innerhalb der Öffnungszeiten**.
5. Klicke auf _Workload speichern_{:.doc-button}.
   injixo berechnet einen neuen Forecast. Dies kann einige Zeit in Anspruch nehmen.

Wenn du die Öffnungszeiten aktiviert hast, zeigt der Graph auf der **Forecast**-Seite Zeiträume außerhalb der Öffnungszeiten als graue Bereiche an.

## Auswirkungen auf den Forecast

Wenn du Öffnungszeiten aktivierst, wirkt sich das wie folgt auf den Forecast aus:

- injixo liest die Öffnungszeiten aus der Planungseinheit und der Aktivität, die dem Workload zugewiesen sind und zeigt nur die Zeiten als Öffnungszeiten an, die bei beiden identisch sind. Jedes Intervall innerhalb dieses Zeitraums wird im Forecast-Graphen berücksichtigt und als offen angezeigt.
- injixo verteilt Volumen außerhalb der Öffnungszeiten innerhalb der Öffnungszeiten um. Das tägliche Gesamtvolumen ändert sich nicht. Die Verteilung erfolgt relativ zu den vorhandenen Intervallwerten und folgt damit dem prognostizierten Intraday-Muster. Volumen außerhalb der Öffnungszeiten erhalten den Wert 0.
- injixo setzt alle prognostizierten AHT-Werte außerhalb der Öffnungszeiten auf 0.
