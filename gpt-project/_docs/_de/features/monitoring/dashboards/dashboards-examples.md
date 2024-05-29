---
title: Beispiele für Dashboards
description: Sieh dir einige praktische Beispiele für Dashboards an.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre mehr über praktische Anwendungsbeispiele für Dashboards, die für deine Planung hilfreich sein können.
---

Unter _Analyze > Dashboards_{:.breadcrumbs} kannst du deine Daten in Diagrammen visualisieren und organisieren, um wichtige Kennzahlen im Blick zu behalten, zu vergleichen und zu analysieren, um auf dieser Grundlage informierte Entscheidungen treffen zu können. Die folgenden Beispiele beschreiben hilfreiche Dashboard-Konfigurationen.

Neu bei Dashboards? Lerne zuerst die Grundlagen und {% link_new wie du Dashboards erstellst | features/monitoring/dashboards/manage-dashboards.md | #dashboards-erstellen %}.

## Mitarbeiterbedarf und Besetzung je Aktivität vergleichen

Um ein Dashboard zu erstellen, das den berechneten Mitarbeiterbedarf für eine Aktivität mit der tatsächlichen Besetzung vergleicht, gehe wie folgt vor:

1. Erstelle unter _Analyze > Dashboards_{:.breadcrumbs} {% link_new ein neues Dashboard | features/monitoring/dashboards/manage-dashboards.md | #dashboards-erstellen %}.
2. Wähle aus dem Dropdown-Menü **Planungseinheiten** auf der linken Seite eine Planungseinheit aus.
3. Wähle aus der Liste **Aktivitäten** die Option **Anwesenheit**.
4. Klappe die Aktivität aus, für die du dir Daten anzeigen lassen möchtest.
5. Ziehe **Bedarf** in ein leeres Diagramm.
6. Ziehe **Besetzung** in dasselbe Diagramm.<br>Jede Planungsebene hat ihre eigene Version für Besetzung und Deckung. Wähle die Version aus, die deiner verwendeten Ebene entspricht.
7. Klicke auf _Speichern_{:.doc-button}.

## Mitarbeiterbedarf und Besetzung insgesamt vergleichen

Um ein Dashboard zu erstellen, das den berechneten Mitarbeiterbedarf für eine gesamte Planungseinheit mit der tatsächlichen Besetzung vergleicht, gehe wie folgt vor:

1. Erstelle unter _Analyze > Dashboards_{:.breadcrumbs} {% link_new ein neues Dashboard | features/monitoring/dashboards/manage-dashboards.md | #dashboards-erstellen %}.
2. Wähle aus dem Dropdown-Menü **Planungseinheiten** auf der linken Seite eine Planungseinheit aus.
3. Wähle aus der Liste **Aktivitäten** die Option **Anwesenheit**.
4. Klappe die Metrik **Gesamtwerte Anwesenheit** aus.
5. Ziehe **Bedarf** in ein leeres Diagramm.
6. Ziehe **Besetzung** in dasselbe Diagramm.<br>Jede Planungsebene hat ihre eigene Version für Besetzung und Deckung. Wähle die Version aus, die deiner verwendeten Ebene entspricht.
7. Klicke auf _Speichern_{:.doc-button}.

## Prognostizierte und tatsächlich eingehende Anrufe vergleichen

Um ein Dashboard zu erstellen, das prognostizierte Anrufe mit den tatsächlich eingehenden Anrufen vergleicht, gehe wie folgt vor:

1. Erstelle unter _Analyze > Dashboards_{:.breadcrumbs} {% link_new ein neues Dashboard | features/monitoring/dashboards/manage-dashboards.md | #dashboards-erstellen %}.
2. Klicke im Dropdown-Menü **Workloads** auf der linken Seite auf einen Workload.
3. Ziehe die Metriken **Eingehende Anrufe Prognose** und **Eingehende Anrufe - Operativ** in ein leeres Diagramm.
4. Wähle aus dem Dropdown-Menü **Planungseinheiten** auf der linken Seite eine Planungseinheit aus.
5. Wähle aus der Liste **Aktivitäten** die Option **Anwesenheit** und klappe die Aktivität aus, für die du dir Daten anzeigen lassen möchtest.
6. Ziehe **Deckung** in das Diagramm.<br>Jede Planungsebene hat ihre eigene Version für Besetzung und Deckung. Wähle die Version aus, die deiner verwendeten Ebene entspricht.
7. Klicke auf _Speichern_{:.doc-button}.

Um die prognostizierte und tatsächliche durchschnittliche Bearbeitungszeit (AHT) zu vergleichen, erstelle ein neues Diagramm und verwende die Metriken **AHT Anrufe Prognose** und **AHT Anrufe - Operativ**.

## Abwesenheiten je Planungseinheit anzeigen

Um ein Dashboard zu erstellen, das Abwesenheiten, Urlaub, Pausen, Meetings und Krankheiten je Planungseinheit anzeigt, gehe wie folgt vor:

1. Erstelle unter _Analyze > Dashboards_{:.breadcrumbs} {% link_new ein neues Dashboard | features/monitoring/dashboards/manage-dashboards.md | #dashboards-erstellen %}.
2. Wähle aus dem Dropdown-Menü **Planungseinheiten** auf der linken Seite eine Planungseinheit aus.
3. Klappe in der Liste **Aktivitäten** die Aktivitäten aus, für die du dir Daten anzeigen lassen möchtest.
4. Wähle für jede Aktivität die Metrik **Besetzung** aus und ziehe sie in ein Diagramm.
5. Klicke auf _Speichern_{:.doc-button}.

Ganztägige Aktivitäten und Urlaub werden als horizontale Linien dargestellt, während kürzere Aktivitäten wie Pausen oder Meetings als Balken angezeigt werden.

## Eingehende und angenommene Anrufe vergleichen

Um ein Dashboard zu erstellen, das eingehende und angenommene Anrufe für einen bestimmten Workload anzeigt, gehe wie folgt vor:

1. Erstelle unter _Analyze > Dashboards_{:.breadcrumbs} {% link_new ein neues Dashboard | features/monitoring/dashboards/manage-dashboards.md | #dashboards-erstellen %}.
2. Klicke im Dropdown-Menü **Workloads** auf der linken Seite auf einen Workload.
3. Ziehe die Metriken **Eingehende Anrufe Historie** und **Angenommene Anrufe Historie** in ein leeres Diagramm.
4. Klicke auf _Speichern_{:.doc-button}.
