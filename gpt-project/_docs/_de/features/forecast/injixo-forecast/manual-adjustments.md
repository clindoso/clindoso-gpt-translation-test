---
title: Forecast anpassen
product_label:
  - advanced
  - enterprise
  - classic
description: Passe die Forecast-Werte für das Kontaktvolumen und die AHT manuell an.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/calculate-staff-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/events-and-holidays.md
---

Du kannst einen erzeugten Forecast bearbeiten, um Unregelmäßigkeiten bei den Werten für das Kontaktvolumen oder die durchschnittliche Bearbeitungszeit (AHT) zu entfernen.

Passe den Forecast an, wenn mindestens eine der folgenden Bedingungen zutrifft:

- Du hast nicht genügend historische Daten oder deine Daten stimmen nicht.
- Deine Werte für das Kontaktvolumen oder die AHT weichen von aktuellen Trends ab und du gehst nicht davon aus, dass sie sich wieder ändern. Ein Grund für solche Abweichungen können beispielsweise strukturelle Änderungen in deinem Unternehmen sein.
- Die Werte für dein Kontaktvolumen sind während eines bestimmten Zeitraums ungewöhnlich hoch oder niedrig, zum Beispiel während einer Marketingkampagne.<br> Entferne in diesem Fall die Unregelmäßigkeiten oder {% link_new füge eine Störung hinzu | features/forecast/injixo-forecast/events-and-holidays.md  | #ereignis-oder-störung-zu-einem-workload-hinzufügen %}, um den Zeitraum aus der Forecastberechnung auszuschließen.

Neue Forecastberechnungen überschreiben keine manuell angepassten Werte.

## Volumen anpassen

1. Wähle in _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Wähle mit der Datumsauswahl einen Zeitraum aus. Klicke auf eine Kalenderwoche, um die ganze Woche auszuwählen oder auf einen beliebigen Tag und ziehe dann mit der Maustaste, um einen Zeitraum kürzer oder länger als eine Woche auszuwählen.<br>Der von dir ausgewählte Zeitraum bestimmt, welche Anpassungsoptionen angezeigt werden.
3. Klicke im Abschnitt Volumen auf _Volumen anpassen_{:.doc-button}.
4. Passe die Konfiguration im Konfigurationsfenster an:

   - **Zeitraum**: Verfügbar, wenn du in Schritt&nbsp;2 einen Zeitraum von mehreren Tagen ausgewählt hast.
   - **Startzeit** und **Endzeit**: Verfügbar, wenn du in Schritt&nbsp;2 einen Zeitraum von einem Tag ausgewählt hast.
   - **anpassen (%)**/**überschreiben**: Wähle eine Option aus dem Dropdown-Menü aus.<br>**anpassen (%)** passt den aktuellen Wert für das Volumen prozentual nach oben oder unten an.<br>**überschreiben** ersetzt den aktuellen Wert durch einen neuen Wert, der eine ganze Zahl größer Null sein muss.
   - **Wert**: Gib einen Wert ein, um das Volumen anzupassen oder zu überschreiben.<br>Erfahre, wie du die [Werte für Volumen und AHT anpasst](#wie-wirken-sich-zeiträume-auf-anpassungen-von-volumen-und-aht-aus).

5. Klicke auf _Anpassung anwenden_{:.doc-button}.<br>
   Änderungen werden im Graphen für das Volumen hervorgehoben. Bewege den Mauszeiger über den Graphen, um weitere Details zu Kontaktvolumen, AHT und Mitarbeiterbedarf sowie zu Ereignissen anzuzeigen.

## AHT anpassen

1. Wähle in _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Wähle mit der Datumsauswahl einen Zeitraum aus. Klicke auf eine Kalenderwoche, um die ganze Woche auszuwählen oder auf einen beliebigen Tag und ziehe dann mit der Maustaste, um einen Zeitraum kürzer oder länger als eine Woche auszuwählen.
3. Klicke neben **AHT** auf das {% icon eye_slash %}.
4. Klicke auf _AHT anpassen_{:.doc-button}.
5. Passe die Konfiguration im Konfigurationsfenster an:

   - **Zeitraum**: Verfügbar, wenn du in Schritt&nbsp;2 einen Zeitraum von mehreren Tagen ausgewählt hast.
   - **Startzeit** und **Endzeit**: Verfügbar, wenn du in Schritt&nbsp;2 einen Zeitraum von einem Tag ausgewählt hast.
   - **anpassen (%)**/**überschreiben**: Wähle eine Option aus dem Dropdown-Menü aus.<br>**anpassen (%)** passt den aktuellen AHT-Wert prozentual nach oben oder unten an.<br>**überschreiben** ersetzt den aktuellen AHT-Wert durch einen neuen Wert, der eine ganze Zahl größer Null sein muss.
   - **Wert**: Gib einen Wert ein, um die AHT anzupassen oder zu überschreiben.<br> Erfahre, wie du die [Werte für Volumen und AHT anpasst](#wie-wirken-sich-zeiträume-auf-anpassungen-von-volumen-und-aht-aus).

6. Klicke auf _Anpassung anwenden_{:.doc-button}.<br>
   Änderungen werden im Graphen für die AHT hervorgehoben. Bewege den Mauszeiger über den Graphen, um weitere Details zu Kontaktvolumen, AHT und Mitarbeiterbedarf sowie zu Ereignissen anzuzeigen.

Wiederhole diesen Vorgang, um Werte erneut anzupassen, wenn der erzeugte Forecast und deine manuellen Anpassungen zu stark voneinander abweichen.

> Hinweis
>
> Wenn du die Werte für das Volumen oder die AHT erneut anpasst, zeigt das Konfigurationsfenster nicht die zuvor von dir eingegebenen Werte an. Wenn du den Prozentsatz für einen Zeitraum erneut nach oben oder unten anpasst, wird nicht der ursprüngliche Wert aktualisiert, sondern der zuletzt angepasste Wert.

## Wie wirken sich Zeiträume auf Anpassungen von Volumen und AHT aus?

Anpassungen haben unterschiedliche Auswirkungen, je nachdem, welchen Zeitraum du mit der Datumsauswahl ausgewählt hast:

| Wert    | Zeitraum      | Auswirkungen der Anpassung                                                                                                                                                                                                                                                                                                                             |
| ------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Volumen | Einzelner Tag | Ein Prozentwert verringert oder erhöht die vorhandenen Werte für alle Intervalle zwischen **Startzeit** und **Endzeit**.<br> Ein absoluter Wert überschreibt die vorhandenen Werte für alle Intervalle zwischen **Startzeit** und **Endzeit**.                                                                                                         |
| Volumen | Mehrere Tage  | Sowohl ein Prozentwert als auch ein absoluter Wert erhöhen oder verringern das Gesamtvolumen. Die Verteilung erfolgt proportional über den ausgewählten Zeitraum, wobei die Trends und Verteilungsmuster für alle Intervalle erhalten bleiben.                                                                                                         |
| AHT     | Einzelner Tag | Ein Prozentwert verringert oder erhöht die vorhandenen Werte für die Intervalle zwischen **Startzeit** und **Endzeit**.<br> Ein absoluter Wert überschreibt die vorhandenen Werte für alle Intervalle zwischen **Startzeit** und **Endzeit**.                                                                                                          |
| AHT     | Mehrere Tage  | Sowohl ein Prozentwert als auch ein absoluter Wert erhöhen oder verringern den angezeigten gewichteten Gesamtdurchschnitt. Die AHT-Werte verteilen sich über den ausgewählten Zeitraum, wobei die Trends und Verteilungsmuster für alle Intervalle erhalten bleiben. Dies kann zu höheren oder niedrigeren Werten an einem oder mehreren Tagen führen. |

## Anpassungen löschen

Du kannst Anpassungen löschen, wenn diese nicht mehr relevant sind.

1. Wähle in _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Wähle die Anpassungen aus, die du löschen möchtest:

   - Klicke im Abschnitt Volumen auf _Volumen anpassen_{:.doc-button}.
   - Klicke im Abschnitt **AHT** auf _AHT anpassen_{:.doc-button}.

3. Wähle einen **Zeitraum**.
4. Klicke auf _Alle Anpassungen löschen_{:.doc-button}, um alle Anpassungen für den gewählten Zeitraum zu entfernen.<br>
   injixo zeigt die ursprünglichen Forecast-Werte für den ausgewählten Zeitraum an.

## Mitarbeiterbedarf für Schichtplanung verwenden

Durch manuelle Anpassungen wird der Mitarbeiterbedarf erneut berechnet.

Wenn du die {% link_new Berechnung des Mitarbeiterbedarfs| features/forecast/injixo-forecast/calculate-staff-requirements.md %} auf der Workloads-Seite konfiguriert hast, kannst du die neuen Werte für die Schichtplanung verwenden, indem du auf _Mitarbeiterbedarf speichern_{:.doc-button} klickst.<br>
Um die angepassten Werte für die Bedarfsskripte Anrufe - Multi-Activity, Anrufe - Outbound und Allgemein - Konstanter Bedarf zu verwenden, gehe wie folgt vor:

1. Klicke oben rechts auf das {% icon ellipsis_v %} und wähle die Option **Forecast verwenden**.
2. Klicke im Konfigurationsfenster auf _Forecast verwenden_{:.doc-button}.
3. Wähle unter _Forecast > Bedarfsskripte_{:.breadcrumbs} ein Skript aus.
4. Konfiguriere das Skript und führe es aus.<br>Erfahre, wie du die Skripte für {% link_new Multiaktivitäten| features/forecast/requirement-scripts/multiactivity-script.md %}, {% link_new Outbound| features/forecast/requirement-scripts/outbound-calls-script.md %} und {% link_new Konstanten Bedarf| features/forecast/requirement-scripts/requirement-constant.md %} konfigurierst.
