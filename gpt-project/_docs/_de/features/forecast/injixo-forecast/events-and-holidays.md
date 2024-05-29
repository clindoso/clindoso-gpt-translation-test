---
title: Ereignisse und Feiertage hinzufügen
product_label:
  - advanced
  - enterprise
  - classic
description: Erstelle Ereignisse und Ereignistypen, um deine Forecast-Genauigkeit zu verbessern.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/create-workloads.md
---

Füge Ereignisse zu deinen historischen Daten und dem erstellten Forecast hinzu, um den Forecasts zu verbessern. Neben Daten sind Ereignisse der zweitwichtigste Faktor für die Forecast-Qualität.

Neu in injixo Forecast? Lerne zuerst {% link_new die Grundlagen | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Was sind Ereignisse?

Mit Ereignissen kannst du vergangene und zukünftige Tage kennzeichnen, die vom Standard abweichen. Dazu gehören zum Bespiel:

- Tage mit ungewöhnlich niedrigen bzw. hohen Werten für das Volumen oder die durchschnittliche Bearbeitungszeit (AHT).
- Tage mit einer abweichenden Volumenverteilung.
- Tage mit unvollständigen, fehlerhaften oder fehlenden Daten, z.&nbsp;B. aufgrund eines ACD-Ausfalls.

injixo Forecast analysiert die zum Workload hinzugefügten Ereignisse, um Trends, Volumenschwankungen und andere Muster zu erkennen, und damit den erzeugten Forecast zu verbessern.

## Ereignistyp erstellen

Vordefinierte Kategorien gruppieren ähnliche Ereignistypen, z.&nbsp;B. Werbeaktionen oder Newsletter.
Alle von dir erstellten Ereignistypen sind in allen Workloads verfügbar. Jede Kategorie kann bis zu sieben Ereignistypen enthalten.

1. Wähle unter _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Klicke oben rechts auf das {% icon ellipsis_v %} und wähle die Option **Ereignistypen anpassen**.
3. Wähle aus dem Dropdown-Menü eine **Kategorie** aus.
4. Klicke auf **\+ Ereignistyp hinzufügen** und gib einen Namen ein.
5. Klicke auf _Ereignistyp hinzufügen_{:.doc-button}.
6. Klicke auf _Schließen_{:.doc-button}.

## Ereignistyp löschen

Lösche alte Ereignistypen oder ersetze einen Ereignistyp durch einen anderen, z.&nbsp;B. wenn du die Obergrenze von sieben Ereignistypen pro Kategorie erreicht hast.

> Achtung
>
> Wenn du einen Ereignistyp löschst, werden damit auch alle dazugehörigen Ereignisse aus allen Workloads und allen erzeugten Forecasts entfernt.

1. Wähle unter _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Klicke oben rechts auf das {% icon ellipsis_v %} und wähle die Option **Ereignistypen anpassen**.
3. Wähle aus dem Dropdown-Menü eine **Kategorie** aus.
4. Klicke auf das {% icon trash %} neben dem Ereignistyp, den du löschen möchtest.
5. Klicke im Bestätigungsfenster auf _Löschen_{:.doc-button}.
6. Klicke auf _Schließen_{:.doc-button}.

## Ereignis oder Störung zu einem Workload hinzufügen

Füge alle bekannten Ereignisse zu vergangenen und zukünftigen Tagen hinzu. Lasse längere Zeiträume mit ungewöhnlichen Mustern weg, da diese Zeiträume und Muster die Forecast-Qualität mit der Zeit verschlechtern.

Smart Workloads berücksichtigen die Auswirkungen eines Ereignisses bis zu zwei Tage vor und nach dem Datum des Ereignisses. Basic Workloads berücksichtigen die Auswirkungen eines Ereignisses nur am Tag des Ereignisses selbst.

Um ein Ereignis oder eine Störung hinzuzufügen, gehe wie folgt vor:

1. Wähle unter _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Klicke oben rechts auf das {% icon ellipsis_v %} und wähle die Option **Ereignisse verwalten**.
3. Klicke im Fenster auf **\+ Ereignis hinzufügen** bzw. auf **\+ Störung hinzufügen** und gib die relevanten Daten ein:
   - **Datum**: Wähle das Datum aus, zu dem du das Ereignis hinzufügen möchtest.
   - **Kategorie**: Wähle aus dem Dropdown-Menü eine Kategorie aus.
   - **Ereignis**: Wähle aus dem Dropdown-Menü ein Ereignis aus.
4. Klicke auf _Ereignis erstellen_{:.doc-button} bzw. _Störung erstellen_{:.doc-button}.
5. Klicke auf _Schließen_{:.doc-button}.

> Hinweis
>
> Füge eine Störung hinzu, um einen vergangenen Tag aus der Forecast-Berechnung auszuschließen.

## Feiertagsregion bearbeiten

Füge Feiertage aus einem deiner verfügbaren Planungskalender hinzu. injixo Forecast behandelt Feiertage als Ereignisse, da sie das Tagesvolumen beeinflussen können. Du kannst die entsprechende Feiertagsregion auswählen, wenn du {% link_new einen Workload erstellst | features/forecast/injixo-forecast/create-workloads.md | #workloads-erstellen %}. Um die Feiertagsregion zu ändern, gehe wie folgt vor:

1. Wähle unter _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Klicke oben rechts auf _Bearbeiten_{:.doc-button}.
3. Wähle eine **Feiertagsregion** aus dem Dropdown-Menü aus.
4. Klicke auf _Workload speichern_{:.doc-button}.

## Ereignisse und Feiertage einsehen

In den Graphen kannst du Ereignisse und Feiertage einsehen. Ereignisse, Störungen und Feiertage werden in unterschiedlichen Farben dargestellt. Derselbe Ereignistyp wird immer in derselben Farbe angezeigt. Die Legende gibt an, welche Farbe für welchen Ereignistyp verwendet wird.

1. Wähle unter _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Wähle einen Zeitraum aus der Datumsauswahl aus. Klicke auf eine Kalenderwoche, um die ganze Woche auszuwählen oder auf einen beliebigen Tag und ziehe dann mit der Maustaste, um einen Zeitraum kürzer oder länger als eine Woche auszuwählen.
3. Bewege den Mauszeiger über die Graphen, um Ereignisse und Feiertage anzuzeigen.
<!-- {{ 3 | image: "Viewing Events", '80%', 'gif' }} -->

## Ereignis löschen

1. Wähle unter _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Wähle einen Zeitraum aus der Datumsauswahl aus. Klicke auf eine Kalenderwoche, um die ganze Woche auszuwählen oder auf einen beliebigen Tag und ziehe dann mit der Maustaste, um einen Zeitraum kürzer oder länger als eine Woche auszuwählen.
3. Klicke oben rechts auf das {% icon ellipsis_v %} und wähle die Option **Ereignisse verwalten**.
4. Klicke auf das {% icon trash %} neben dem Ereignis, das du löschen möchtest.
5. Klicke auf _Schließen_{:.doc-button}.
