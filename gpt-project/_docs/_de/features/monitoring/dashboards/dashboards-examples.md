---
title: Beispiele für Dashboards
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lerne einige praktische Dashboards kennen, die Du vielleicht in Deiner Planung verwenden möchtest.
---

In diesem Artikel lernst Du einige praktische Dashboards für Deine Planung kennen.

Neu in Dashboards? Lerne zuerst {% link_new die Grundlagen | features/monitoring/dashboards/dashboards-overview.md %}.

Wenn Du die folgenden Dashboards erstellen willst, rufe das **Dashboards-Modul** in der Hauptnavigation auf. Klicke dann auf _![Kontextmenü](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon} und **Neues Dashboard erstellen**.

## Besetzung vs. Bedarf für eine Aktivität

Du willst wissen, ob der berechnete Bedarf für eine Aktivität ausreichend gedeckt wird?

1. Navigiere im Menü links zu *Planungseinheiten > Name Deiner Planungseinheit > Aktivitäten > Anwesenheit*{:.breadcrumbs}.
2. Klicke auf die **Aktivität**, für die Du Daten anzeigen möchtest.
3. Ziehe **Bedarf** und **Besetzung** per Drag and Drop in das Diagramm auf der rechten Seite. Für jede Ebene gibt es eine eigene Version der Kennzahl *Besetzung*. Wähle die Kennzahl für die Ebene, die Du verwendest.

{{ 1 | image: 'requirement vs staffing weekly' }}

## Gesamtwerte Anwesenheit vs. Bedarf

Du möchtest wissen, wie exakt Deine Planung den Bedarf abdeckt?

1. Navigiere im Menü links zu *Planungseinheiten > Name Deiner Planungseinheit > Aktivitäten > Anwesenheit > Gesamtwerte Anwesenheit*{:.breadcrumbs}.
2. Ziehe **Bedarf** und **Besetzung** per Drag and Drop in das Diagramm auf der rechten Seite. Für jede Ebene gibt es eine eigene Version der Kennzahl *Besetzung*. Wähle die Kennzahl für die Ebene, die Du verwendest.
3. Optional kannst Du auch die Kennzahl **Deckung** in das Diagramm ziehen.

{{ 5 | image: 'Gesamtwert Anwesenheit gegen Bedarf mit Deckung' }}

## Prognostizierte vs. tatsächlich eingehende Anrufe

Überprüfe, wie genau Dein zuvor gespeicherter Forecast im Vergleich zum tatsächlichen Tagesanrufvolumen war. Die Kennzahl *Deckung* wird ebenfalls hinzugefügt, um zu visualisieren, ob Du genügend Mitarbeiter zur Verfügung hast, um zusätzliche Anrufe bearbeiten zu können.

1. Klicke links im Menü auf **Workloads** und dann auf den Workload, für den Du Daten anzeigen möchtest.
2. Ziehe **Eingehende Anrufe** und **Eingehende Anrufe - Operative Version** per Drag and Drop in das Diagramm auf der rechten Seite.
3. Navigiere zu *Planungseinheiten > Name Deiner Planungseinheit > Aktivitäten > Anwesenheit*{:.breadcrumbs} und klicke auf die Anrufaktivität, für die Du Daten anzeigen möchtest.
4. Ziehe **Deckung** in das Diagramm. Für jede Ebene gibt es eine eigene Version der Kennzahl *Deckung*. Wähle die Kennzahl für die Ebene, die Du verwendest.
5. Erstelle die gleichen Graphen mit **AHT** und **AHT - Operative Version**, um auch die prognostizierte und tatsächliche durchschnittliche Bearbeitungszeit (AHT) vergleichen zu können.

{{ 2 | image: 'Anrufe Forecast', '50%' }}

## Abwesenheiten je Planungseinheit

Du möchtest wissen, wie viele Mitarbeiter im Urlaub, in Meetings oder in der Pause sind?

Das Dashboards-Modul liefert Werte für Abwesenheiten, Urlaub, Pausen, Meetings und Krankheit je Planungseinheit. Ganztägige Aktivitäten und Urlaub werden als horizontale Linien dargestellt, während kürzere Aktivitäten wie Pausen oder Meetings als Balken angezeigt werden.

1. Navigiere links im Menü zu *Planungseinheiten > Name Deiner Planungseinheit > Aktivitäten*{:.breadcrumbs}.
2. Klicke auf die Aktivitäten, für die Du Daten anzeigen möchtest, und suche die Kennzahl *Besetzung*. Für jede Ebene gibt es eine eigene Version der Kennzahl *Besetzung*. Ziehe die Kennzahl für die Ebene, die Du verwendest, per Drag & Drop in das Diagramm auf der rechten Seite.
3. Füge so alle *Besetzungs*-Kennzahlen hinzu, die Du anzeigen möchtest.

{{ 3 | image: 'Abwesenheiten, Pausen, Urlaub, Krankheiten', '50%' }}

## Eingehende vs. angenommene Anrufe

Du möchtest sehen, wie viele Anrufe eingegangen sind und wie viele Du davon bearbeiten konntest?

{{ 4 | image: 'Vergleich eingehende und angenommene Anrufe', '50%' }}

1. Klicke links im Menü auf **Workloads** und dann auf den Workload, für den Du Daten anzeigen möchtest.
2. Ziehe **Eingehende Anrufe** und **Angenommene Anrufe** per Drag and  Drop in das Diagramm auf der rechten Seite.
