---
title: Den Forecast manuell anpassen
product_label:
  - advanced
  - enterprise
  - classic
description: Passe das im Forecast prognostizierte Kontaktvolumen und die AHT manuell an.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/calculate-staff-requirements.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/events-and-holidays.md
---

In diesem Artikel lernst Du:

- - wann ein erzeugter Forecast manuell angepasst werden muss.
- - wie Du Werte für Volumen oder durchschnittliche Bearbeitungszeiten (AHT) anpasst.
- - die Unterschiede zwischen Volumen- und AHT-Anpassungen.
- - wie Du manuelle Anpassungen löschst oder änderst.
- - wie Du den geänderten Mitarbeiterbedarf für die Schichtplanung überträgst.

Neu in injixo Forecast? Lerne zuerst {% link_new die Grundlagen | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Wann muss ein erzeugter Forecast manuell angepasst werden?

Ändere einen erzeugten Forecast, um Anomalien in den Volumen- oder AHT-Werten zu entfernen.

Passe das Ergebnis der Forecast-Berechnung manuell an, wenn Du:

- einen zuverlässigen Forecast erstellen musst, aber über unzureichende oder falsche historische Daten verfügst.
- Volumen- oder AHT-Werte hast, die von den aktuellen Trends abweichen, z. B. aufgrund struktureller Veränderungen im Unternehmen, und Du nicht erwartest, dass diese sich wieder ändern.
- ungewöhnlich hohe oder niedrige Volumen in einem bestimmten Zeitraum hast, die durch einmalige Ereignisse wie eine Marketingkampagne bedingt sind. Entferne diese Anomalien oder füge ein {% link_new Ereignis | features/forecast/injixo-forecast/events-and-holidays.md %} _Störung_ hinzu, um den Zeitraum aus der Forecast-Berechnung auszuschließen.

Neue Forecast-Berechnungen überschreiben nicht die manuell angepassten Werte.

## Volumen oder AHT anpassen

1. Gehe zu _Forecast_{:.menu-item}.
2. Wähle einen **Workload**.
3. Wähle einen **Tag**, eine **Woche** oder einen **Monat**.
4. Klicke auf _![Kontextmenü in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} im Abschnitt _Volumen und AHT_.
5. Klicke auf **Volumen anpassen**. Um die AHT anzupassen, klicke auf **AHT anpassen**.
6. Unter dem Graphen erscheint der Bereich für **Manuelle Anpassungen**.

   {{ 1 | image: 'Dialog für manuelle Anpassungen' }}

7. Wähle den **Zeitraum**, den Du anpassen möchtest, indem Du auf das erste und letzte Datum im Kalender klickst. Wähle in der Tagesansicht eine **Startzeit** und **Endzeit** anstelle des Zeitraums, um einzelne Intervalle zu aktualisieren.
8. Gib das **Volumen**- oder den **AHT**-Wert ein, um den Du den Forecast erhöhen oder verringern möchtest. Um den Wert zu verringern, stelle ein Minuszeichen voran, z. B. -50. Lerne unterhalb, [wie Volumen und AHT-Werte im Detail angepasst werden](#unterschiede-zwischen-volumen--und-aht-anpassungen).
   - Wähle **anpassen (%)**, um das Volumen prozentual anzupassen.
   - Wähle **überschreiben**, um für das Volumen einen bestimmten Wert (positive ganze Zahl) für den **Datumsbereich** festzusetzen.
9. Wähle einen **Grund für die Anpassung** aus dem Dropdown-Menü.
10. Klicke auf _Speichern_{:.doc-button}, um die Änderungen zu übernehmen oder klicke auf _Abbrechen_{:.doc-button}, um die Änderungen zu verwerfen. Deine Änderungen werden im Volumen- oder AHT-Graph sofort schraffiert hervorgehoben.

{{ 2 | image: 'Manuelle Anpassungen in injixo Forecast' }}

## Unterschiede zwischen Volumen- und AHT-Anpassungen

| Wert  |      Ansicht      | Beschreibung                                                                                                                                                                                                                                                                   |
| :----: | :------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Volumen |     Tag      | Ein Prozentwert verringert oder erhöht die bestehenden Werte für die ausgewählten Intervalle. Ein absoluter Wert überschreibt die ausgewählten Intervalle mit dem definierten Wert für jedes Intervall.                                                                                       |
| Volumen | Woche/Monat | Ein Prozentwert und ein absoluter Wert erhöhen oder verringern das Gesamtvolumen. Der Wert verteilt sich proportional über den ausgewählten Zeitraum, wobei die Intervall-Trends und Verteilungsmuster erhalten bleiben.                                                                      |
|  AHT   |     Tag      | Ein Prozentwert verringert oder erhöht die bestehenden Werte für die ausgewählten Intervalle. Ein absoluter Wert überschreibt die ausgewählten Intervalle mit dem definierten Wert für jedes Intervall.                                                                                       |
|  AHT   | Woche/Monat | Ein Prozentwert und ein absoluter Wert erhöhen oder verringern den angezeigten gewichteten Gesamtdurchschnitt. Die Werte verteilen sich über den ausgewählten Zeitraum, wobei die Intervall-Trends und Verteilungsmuster erhalten bleiben. Dies kann an einem oder mehreren Tagen zu höheren oder niedrigeren Werten führen. |

> Keine AHT-Werte
>
> Wenn ein Tag keine AHT-Werte anzeigt, kannst du die AHT nicht in der wöchentlichen oder monatlichen Ansicht anpassen.  
> In der Tagesansicht kannst du die AHT durch Überschreiben von Intervallen mit absoluten Werten anpassen.  
> Um die geänderte AHT in der wöchentlichen oder monatlichen Ansicht zu sehen, gib ein Kontaktvolumen größer null ein.

## Manuelle Anpassungen ändern

Passe die Werte erneut an, wenn es einen signifikanten Unterschied zwischen dem erzeugten Forecast und Deiner manuellen Anpassung gibt. Führe die gleichen Schritte aus wie unter [Volumen oder AHT anpassen](#volumen-oder-aht-anpassen) beschrieben.

Hinweis: Die Felder zeigen nicht die zuvor eingegebenen Werte an, sondern bleiben leer. Eine weitere prozentuale Erhöhung/Verringerung für einen Zeitraum aktualisiert nicht den ursprünglichen Wert, sondern den zuvor geänderten Wert.

## Manuelle Anpassungen löschen

Lösche alte oder nicht mehr benötigte Anpassungen.

1. Gehe zu _Forecast_{:.menu-item}.
2. Wähle einen **Workload**.
3. Wähle einen **Tag**, eine **Woche** oder einen **Monat**.
4. Klicke auf _![Kontextmenü in injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} im Abschnitt _Volumen und AHT_.
5. Wähle **Volumen anpassen** oder **AHT anpassen** im angezeigten Kontextmenü.
6. Wähle den gewünschten **Tag** oder die **Intervalle** aus dem Dropdown-Menü.
7. Klicke auf _Ausgewählte Anpassungen löschen_{:.doc-button}, um die anzeigte Anpassung zu löschen. Klicke auf _Alle Anpassungen löschen_{:.doc-button}, um alle Anpassungen des ausgewählten Tages zu entfernen.

   {{ 4 | image: 'Dialog zum Löschen von Anpassungen' }}

## Geänderten Mitarbeiterbedarf für die Schichtplanung übertragen

Bei automatischen Berechnungsmethoden wird bei manuellen Anpassungen der Mitarbeiterbedarf automatisch neu berechnet. Um den geänderten Mitarbeiterbedarf für die Schichtplanung zu verwenden, klicke auf _Mitarbeiterbedarf verwenden_{:.doc-button}.

Um die angepassten Werte für andere Berechnungsmethoden zu übernehmen, klicke auf _Forecast verwenden_{:.doc-button}, wähle anschließend Dein {% link_new Mitarbeiterbedarfsskript | features/forecast/injixo-forecast/calculate-staff-requirements.md %}, konfiguriere die Parameter und klicke auf _OK_{:.doc-button}, um es auszuführen. Dadurch wird Dein Mitarbeiterbedarf auf Grundlage der angepassten Werte aktualisiert.
