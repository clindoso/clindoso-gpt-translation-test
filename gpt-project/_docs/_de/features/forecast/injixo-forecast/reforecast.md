---
title: Reforecast
---

Damit Du auf unvorhergesehene Ereignisse reagieren kannst, zum Beispiel wenn Deine historischen Daten stark von Deinen Prognosedaten abweichen, bieten wir Dir die Möglichkeit, Deinen Auto-Forecast anhand eines Reforecasts anzupassen.

Dieses Feature ist in injixo Advanced WFM oder höher verfügbar. <!-- currently not live, beta was canceled some years ago  -->

## Wie funktioniert der Reforecast?

Der Reforecast adaptiert Deine Prognosedaten basierend auf den Abweichungen zwischen der **operativen** oder **strategischen** {% link_new Version | features/forecast/injixo-forecast/store-forecast-versions.md %} und den historischen Daten. Die adaptierten Prognosedaten werden Dir als manuelle Anpassungen im Graphen angezeigt.

## Reforecast durchführen 

Folgende Schritte sind notwendig, um einen Reforecast des Auto-Forecasts durchzuführen:

1. Öffne den gewünschten Workload.
2. Wähle in der Zeitnavigation die Tagesansicht aus und klicke auf _Heute_{:.doc-button-icon}.
3. Klick auf den Button _{{ 1 | image: "Context Menu in injixo Forecast", '100%', 'svg'}}_{:.doc-button-icon} innerhalb der Volumen und AHT Sektion.
4. Wähle _Reforecast durchführen_{:.doc-button} aus.
5. Lege fest, ob der Reforecast basierend auf den Daten der **operativen** oder **strategischen** Version berechnet werden soll. Der Reforecast wird Dir als manuelle Anpassung im Graphen angezeigt.
6. a) Wenn Du mit dem angezeigten Reforecast zufrieden bist, bestätige Deine Auswahl mit _Speichern_{:.doc-button}.
6. b) Möchtest Du noch manuelle Anpassungen am Forecast vornehmen, bestätige Deine Auswahl mit _Speichern und anpassen_{:.doc-button}.

> Hinweis
>
> Bereits bestehende manuelle Anpassungen für den ausgewählten Zeitraum werden überschrieben.  

## Reforecast anzeigen

Der Reforecast wird automatisch im Volumen-Graph als manuelle Anpassung angezeigt. Du hast die Möglichkeit den Reforecast über manuellen Anpassungen zu überarbeiten oder zu entfernen. Außerdem kannst Du wie gewohnt den, aus dem Reforecast überarbeiteten, Auto-Forecast in einer Version ablegen.

{{ 2 | image: 'Überarbeiteter Forecast nach dem Anwenden des Reforecasts'}}
