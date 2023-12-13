---
title: Mit Workloads arbeiten
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du die Graphen für Volumen und durchschnittliche Bearbeitungszeit in Workloads bearbeitest und darin navigierst.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/forecast-activate-business-hours.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/events-and-holidays.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manual-adjustments.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/store-forecast-versions.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/download-forecast.md
---

In diesem Artikel lernst du, wie du in den Graphen für Volumen und durchschnittliche Bearbeitungszeit in Workloads arbeitest und darin navigierst.

Neu in injixo Forecast? Lerne zuerst {% link_new die Grundlagen | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}. Wenn du noch keine Workloads hast, lerne wie du {% link_new deinen ersten Workload erstellst | features/forecast/injixo-forecast/manage-workloads.md %}.

## Workload-Details anzeigen

1. Gehe zu _Forecast_{:.menu-item}.
2. Wähle einen Workload mit einer der folgenden Optionen:
   - Wähle einen Workload aus dem Dropdown-Menü am oberen Bildschirmrand.
   - Gib den Workload-Namen in das Suchfeld ein.
   - Klicke auf einen Workload in der Liste

{{ 3 | image: 'Auswahlfeld für Workloads' }}

### In Workloads navigieren

- Verwende die **Zeitnavigation**, um eine Tages-, Wochen-, Monats- oder Jahresansicht auszuwählen.
- Klicke auf den **Datumsbereich**, um einen Zeitraum aus dem Kalender auszuwählen.
- Verwende _<_{:.doc-button} und _>_{:.doc-button}, um im ausgewählten Datumsbereich zu navigieren.
- Um zum aktuellen Zeitraum zurückzukehren, klicke auf die erste Schaltfläche auf der linken Seite, z. B. **Diese Woche** (je nach gewählter Ansicht beschriftet).

  {{ 1 | image: 'Workload-Zeitnavigation', '80%' }}

### Diagramme zu Volumen und durchschnittlicher Bearbeitungszeit

Das Diagramm zeigt das Volumen und die durchschnittliche Bearbeitungszeit (AHT) für historische Daten, importierte Forecasts und erzeugte Forecasts an. Oben siehst du das Gesamtvolumen und die AHT (gewichteter Gesamtdurchschnitt) für den ausgewählten Zeitraum.

Eine Legende hilft dir, die verschiedenen Diagramme und {% link_new manuelle Anpassungen | features/forecast/injixo-forecast/manual-adjustments.md %} zu unterscheiden; blende die Graphen aus, indem du auf das {% icon eye %} klickst.

Hinweis: Das AHT-Diagramm ist nicht verfügbar für Workloads, deren Queues keine AHT-Daten liefern.

{{ 4 | image: 'Volumen und AHT Graphen', '80%' }}

### Graph für den Mitarbeiterbedarf

Im Abschnitt _Mitarbeiterbedarf_ konfigurierst/bearbeitest du die Bedarfsberechnungsmethode.

Der Bereich zeigt die Berechnungsergebnisse für automatische Berechnungsmethoden an. Oben siehst du die konfigurierten Parameter und die daraus resultierenden Gesamt-Personenstunden für den ausgewählten Zeitraum.

{{ 5 | image: 'Graph für den Mitarbeiterbedarf', '80%' }}

Um den Mitarbeiterbedarf für die Schichtplanung zu nutzen, wähle den Forecast oder die Forecast-Version aus dem Dropdown-Menü im Abschnitt **Mitarbeiterbedarf** (_Auto-Forecast_ ist vorausgewählt) und klicke auf _Bedarf verwenden_{:.doc-button}.

Um die Werte für andere Berechnungsmethoden zu übernehmen, klicke auf _Forecast verwenden_{:.doc-button} oben rechts neben den Diagrammen. Der Workload ist jetzt als Queue in WFM verfügbar. Der Queue-Name beginnt mit einem Sternchen (*). Wähle als nächstes dein {% link_new Bedarfsskript | features/forecast/injixo-forecast/staff-requirement.md %} aus, wähle die Queue und die _Auto-Forecast_-Option, konfiguriere die Parameter und klicke auf _OK_{:.doc-button}, um das Skript auszuführen.
