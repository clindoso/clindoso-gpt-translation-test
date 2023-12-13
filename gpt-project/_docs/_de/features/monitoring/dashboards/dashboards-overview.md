---
title: Dashboards verwalten
promote-service: team-leader-training
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Nutze Dashboards, um Dein Volumen und Deine Deckung zu analysieren.
related_articles:
  - filepath: features/monitoring/dashboards/work-with-charts.md
  - filepath: features/monitoring/dashboards/dashboards-examples.md
---

In diesem Artikel lernst Du, wie Du Dashboards erstellst, bearbeitest und löschst.

## Was ist das Dashboards-Modul?

Erstelle und speichere Dashboards mit jeweils bis zu vier verschiedene Diagrammen. Jedes Diagramm kann mehrere [Zeitreihen](https://help.injixo.com/de/glossary/overview/#zeitreihe)<!-- full url to glossary as exception --> als Graphen für verschiedene Zeiträume darstellen. Möglich sind Kennzahlen zu:
- Workloads (Historie, Forecasts und {% link_new Forecast-Versionen | features/forecast/injixo-forecast/store-forecast-versions.md %}).
- Planungseinheiten (Besetzung, Bedarf und Deckung für geplante Schichten und Aktivitäten sowie {% link_new in injixo Me gewünschte Schichten | features/scheduling/shift-bidding.md %}).

## Dashboards erstellen

1. Gehe zu *Analyze > Dashboards*{:.breadcrumbs}.
2. Klicke auf _![Kontextmenü](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon}.
3. Klicke **Erstellen**, um in den Bearbeitungsmodus zu gelangen.
4. Gib einen **Namen** für das neue Dashboard ein.
5. Wähle unter *Layout* auf der rechten Seite eines der **vordefinierten Layouts** aus, um die Anzahl der Diagramme festzulegen.
6. Optional: Gib einen **Namen** für jedes Diagramm in das Feld **Unbenanntes Diagramm** ein, um den Zweck/Inhalt des Diagramms zu beschreiben. Die Namen müssen nicht eindeutig sein.
7. Lege oben rechts in jedem Diagramm einen fixen **Zeitbereich** für die Anzeige fest oder aktiviere zusätzlich **Rollierender Zeitraum** (optional). In diesem Modus wird das Startdatum jeden Tag um einen Tag verschoben.

    {{ 3 | image: 'Auswahl des Zeitbereichs', '40%' }}

8. Ziehe Zeitreihen links aus der Baumstruktur in jedes Diagramm. Hinweis: Wenn für einen Zeitraum keine Daten für einen Workload verfügbar sind, zeigt die Legende ein Warnsymbol _![Warnung, dass keine Daten vorhanden sind](/assets/img/common/dashboards/no-data.png)_{:.doc-button-icon}.
9. Klicke *Speichern*{:.doc-button}. Klicke *Bearbeitungsmodus verlassen*{:.doc-button}, um in den Anzeigemodus zurückzukehren.

    <!-- remove left and top menu -->
    {{ 1 | image: 'Create a Dashboard', '75%', 'gif' }}

### Dashboards duplizieren

Für ein neues Dashboard, das einem bestehenden Dashboard ähnelt, kopiere Dein aktuelles Dashboard. Klicke auf _![Kontextmenü](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon}, dann klicke *Dashboard duplizieren*{:.doc-button}.

## Dashboards anzeigen

1. Gehe zu *Analyze > Dashboards*{:.breadcrumbs}.
2. Wähle ein **Dashboard** aus dem Dropdown-Menü **Dashboard auswählen** oder tippe, um zu filtern. Wenn Du noch kein Dashboard hast, zeigt der Bildschirm den Bearbeitungsmodus an und Du kannst [ein Dashboard erstellen](#dashboards-erstellen).
3. Optional: Klicke auf einen **Zeitbereich** in der oberen rechten Ecke jedes Diagramms, um den angezeigten Zeitraum zu ändern.

Tipp: Bewege den Mauszeiger über ein Diagramm, um einen Tooltip mit den Intervallwerten für jedes Diagramm anzuzeigen.

### Automatische Aktualisierung aktivieren

Wenn Du ein Dashboard ausgewählt hast, klicke oben rechts *Autom. Aktualisierung*{:.doc-button}, um das gewählte Dashboard automatisch alle 15 Minuten zu aktualisieren. Am unteren Bildschirmrand siehst Du, wann es zuletzt aktualisiert wurde.

### Vollbildmodus aktivieren

Für eine detailliertere Ansicht wechsele in den Vollbildmodus. Klicke _![Vollbildmodus](/assets/img/common/dashboards/fullscreen.png)_{:.doc-button-icon} in der oberen rechten Ecke.

## Dashboards bearbeiten

1. Klicke auf _![Kontextmenü](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon} neben dem Namen des aktuell ausgewählten Dashboards.
2. Klicke auf **Bearbeiten**, um den Bearbeitungsmodus für das Dashboard aufzurufen.
3. {% link_new Passe Zeitreihen an | features/monitoring/dashboards/work-with-charts.md | #zeitreihen-anpassen %} oder {% link_new lösche | features/monitoring/dashboards/work-with-charts.md | #zeitreihen-löschen %} sie.
4. Klicke auf *Speichern*{:.doc-button}, dann auf *Bearbeitungsmodus verlassen*{:.doc-button}, um zum Anzeigemodus zurückzukehren.

    {{ 2 | image: 'Bearbeitungsmodus', '75%' }}

## Dashboards löschen

1. Klicke auf _![Kontextmenü](/assets/img/common/dashboards/context-menu.png)_{:.doc-button-icon} neben dem Namen des aktuell ausgewählten Dashboards.
2. Klicke auf **Bearbeiten**, um den Bearbeitungsmodus zu öffnen.
3. Klicke unten rechts auf **Löschen**.
4. Bestätige die Meldung *Dieses Dashboard wird gelöscht. Bist Du sicher?*, indem Du auf *Dashboard löschen*{:.doc-button} klickst, um es zu löschen. Klicke auf *Dashboard behalten*{:.doc-button}, um den Löschvorgang abzubrechen.

Hinweis: Wenn Du das letzte verbleibende Dashboard löschst, wird der Bearbeitungsmodus angezeigt, bis Du [ein neues Dashboard erstellst](#dashboards-erstellen).
