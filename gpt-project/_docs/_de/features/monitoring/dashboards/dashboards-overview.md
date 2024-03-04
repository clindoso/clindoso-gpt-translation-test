---
title: Dashboards verwalten
permalink: /de/dashboards-overview/
promote-service: team-leader-training
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Verwende Dashboards, um Daten zu deinem Kontaktvolumen und deiner Besetzung zu analysieren.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/work-with-charts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/monitoring/dashboards/dashboards-examples.md
---

Unter _Analyze > Dashboards_{:.breadcrumbs} kannst du Dashboards mit bis zu vier Diagrammen erstellen und anzeigen. Jedes Diagramm kann Graphen für mehrere Zeitreihen und Zeiträume darstellen. Wenn du noch kein Dashboard hast, zeigt die Seite den Bearbeitungsmodus an und du kannst [ein Dashboard erstellen](#dashboards-erstellen).

- Um ein vorhandenes Dashboard anzuzeigen, wähle ein Dashboard aus dem Dropdown-Menü aus oder gib einen Suchbegriff in das Feld ein.  
- Um die Werte für ein bestimmtes Intervall anzuzeigen, bewege den Mauszeiger über einem Graphen im Dashboard.
- Um zum Vollbildmodus zu wechseln, klicke auf das {% icon maximize %} oben rechts.

Du kannst auch zwischen der {% link_new Diagrammansicht und Tabellenansicht | features/monitoring/dashboards/work-with-charts.md | #diagramme-im-überblick %} wechseln, indem du auf das Tabelle-anzeigen-Icon {% icon table-list | icon-only %} bzw. das Diagramm-anzeigen-Icon {% icon chart-view | icon-only %} klickst.

## Dashboards erstellen

1. Gehe zu _Analyze > Dashboards_{:.breadcrumbs}.
2. Klicke rechts auf das {% icon ellipsis_v %} und wähle die Option **Erstellen**.
3. Konfiguriere folgende Felder:
  - **Name**: Eindeutiger Name für dein Dashboard.
  - **Layout**: Wähle die Anzahl und das Layout deiner Diagramme aus.
  - **Unbenanntes Diagramm**: Hier kannst du jedes Diagramm benennen. Die Namen müssen nicht eindeutig sein.
4. Wähle einen **Datumsbereich** für jedes Diagramm aus.
5. (Optional) Aktiviere die Option **Rollierender Zeitraum**, um das Startdatum jeden Tag um einen Tag zu verschieben.
6. Ziehe aus der Baumansicht links Zeitreihen in die Diagramme, um verschiedene Kennzahlen darzustellen:
   - **Workloads**: Historie, Prognose, Import und {% link_new Forecast-Versionen | features/forecast/injixo-forecast/store-forecast-versions.md %}. 
   - **Planungseinheiten**: Besetzung, Mitarbeiterbedarf und Deckung für geplante Schichten und Aktivitäten sowie Schichten, auf die in Me Schichtwünsche abgegeben wurden.
   - **WFM Queues**: Workload-Daten in WFM-Queues, die du gespeichert hast, wenn du auf der Workload-Seite auf _Forecast verwenden_{:.doc-button} geklickt hast. Die Option ist möglicherweise nicht verfügbar, je nach WFM-Plan. 

      > Hinweis
      >
      > - Das {% icon circle_exclamation %} in der Legende eines Diagramms wird angezeigt, wenn für einen ausgewählten Zeitraum keine Daten vorliegen.
      > - Unter Workloads siehst du je nach Integration möglicherweise besondere Kennzahlen. Wenn deine Workloads z.&nbsp;B. ausschließlich Queues aus einer [Genesys Cloud-Integration](/add-genesys-cloud-integration/) enthalten, siehst du Informationen zu abgebrochenen Anrufen, durchschnittlicher Antwortzeit und Anrufen, die gemäß Service-Level beantwortet wurden. 

7. Klicke auf _Speichern_{:.doc-button}.<br>Um zum Anzeigemodus zurückzukehren, klicke auf _Bearbeitungsmodus verlassen_{:.doc-button}.

### Dashboards duplizieren

Um ein neues Dashboard mit denselben allgemeinen Eigenschaften wie ein vorhandenes Dashboard zu erstellen, gehe wie folgt vor:
1. Gehe zu _Analyze > Dashboards_{:.breadcrumbs}.
2. Wähle aus dem Dropdown-Menü ein Dashboard aus.
3. Klicke auf das {% icon ellipsis_v %} und wähle die Option _Dashboard duplizieren_{:.doc-button}.
4. Falls nötig, bearbeite den Namen und die Konfigurationsdetails.
5. Klicke auf _Speichern_{:.doc-button}.

### Dashboards automatisch aktualisieren

Du kannst das ausgewählte Dashboard automatisch aktualisieren. Wähle dazu aus dem Dropdown-Menü rechts ein Intervall aus und klicke auf _{% icon arrows-rotate | icon-only %} Autom. Aktualisierung_{:.doc-button}.<br>Unten links auf der Seite kannst du sehen, wann das Dashboard zuletzt aktualisiert wurde.

## Dashboards bearbeiten

1. Gehe zu _Analyze > Dashboards_{:.breadcrumbs}.
2. Wähle aus dem Dropdown-Menü ein Dashboard aus.
3. Klicke rechts auf das {% icon ellipsis_v %} und wähle die Option **Bearbeiten**.
4. Bearbeite das Dashboard, {% link_new passe Zeitreihen an | features/monitoring/dashboards/work-with-charts.md | #zeitreihen-anpassen %} oder {% link_new lösche | features/monitoring/dashboards/work-with-charts.md | #zeitreihen-löschen %} sie.
5. Klicke auf _Speichern_{:.doc-button}. Um zum Anzeigemodus zurückzukehren, klicke auf _Bearbeitungsmodus verlassen_{:.doc-button}.

## Dashboards löschen

1. Gehe zu _Analyze > Dashboards_{:.breadcrumbs}.
2. Wähle aus dem Dropdown-Menü ein Dashboard aus.
3. Klicke rechts auf das {% icon ellipsis_v %} und wähle die Option **Bearbeiten**.
4. Klicke unten rechts auf _Löschen_{:.doc-button}.  
5. Klicke im Bestätigungsfenster auf _Dashboard löschen_{:.doc-button}.<br> Um den Löschvorgang abzubrechen, klicke auf _Dashboard behalten_{:.doc-button}.

Wenn du das letzte verbleibende Dashboard löschst, wird der Bearbeitungsmodus angezeigt, bis du [ein neues Dashboard erstellst](#dashboards-erstellen).
