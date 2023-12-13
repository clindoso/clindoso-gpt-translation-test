---
title: Ereignisse und Feiertage hinzufügen
product_label:
  - advanced
  - enterprise
  - classic
description: Erstelle Ereignisse und Ereignistypen, um die Genauigkeit Deines Forecasts zu verbessern.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
---

In diesem Artikel lernst Du:

- was Ereignisse sind.
- wie Du Ereignistypen erstellst und löschst.
- wie Du einem Workload Ereignisse und Feiertage hinzufügst.
- wie Du Ereignisse entfernst.

Füge Ereignisse zu Deinen historischen Daten und dem erstellten Forecast hinzu, um Deine Forecasts zu verbessern. Neben Daten sind Ereignisse der zweitwichtigste Faktor für die Forecast-Qualität.

Neu in injixo Forecast? Lerne zuerst {% link_new die Grundlagen | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Was sind Ereignisse?

Ein Ereignis ist eine Markierung für einen Tag, die injixo Forecast sagt, dass dieser Tag hinsichtlich des Volumens oder seiner Verteilung speziell ist. Es gibt vordefinierte Kategorien, die ähnliche Ereignistypen gruppieren, z. B. Werbeaktionen oder Newsletter.

Mit Ereignissen kannst Du Tage in der Vergangenheit und in der Zukunft markieren, die:

- ungewöhnlich niedrige oder hohe Volumen oder durchschnittlichen Bearbeitungszeiten aufweisen.
- Tagesverteilungen zeigen, die von einem Standardtag abweichen.
- unvollständige, fehlerhafte oder fehlende Daten enthalten, z. B. aufgrund eines ACD-Ausfalls.

injixo Forecast analysiert die zum Workload hinzugefügten Ereignisse, um Trends, Volumenschwankungen und andere Muster zu erkennen, um den erzeugten Forecast verbessern.

## Einen Ereignistyp erstellen

Jeder erstellte Ereignistyp ist in jedem Workload verfügbar.

1. Gehe zu _Forecast_{:.menu-item}.
2. Wähle einen **Workload**.
3. Klicke auf _![Kontextmenü im injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} rechts im Abschnitt _Ereignisse_.
4. Klicke auf **Ereignistypen anpassen**.
5. Wähle eine **Kategorie** aus dem Dropdown.
6. Gib im Abschnitt _Neuen Ereignistyp hinzufügen_ einen **Namen** für den Ereignistyp ein.
7. Klicke auf _Ereignistyp hinzufügen_{:.doc-button}.
8. Klicke auf _Schließen_{:.doc-button}. Jetzt kannst Du den neuen Ereignistypen in allen Deinen Workloads verwenden.

   {{ 1 | image: "Konfigurieren von Ereignistypen", '40%' }}

## Einen Ereignistyp löschen

Lösche alte Ereignistypen oder ersetze einen Ereignistyp durch einen anderen, z. B. wenn Du das Limit von sieben Ereignistypen pro Kategorie erreicht hast.

> Durch das Löschen eines Ereignistyps werden auch alle entsprechenden Ereignisse aus allen Forecasts entfernt.

1. Gehe zu _Forecast_{:.menu-item}.
2. Wähle einen **Workload**.
3. Klicke auf _![Kontextmenü im injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} rechts im Abschnitt _Ereignisse_.
4. Klicke auf **Ereignistypen anpassen**.
5. Wähle eine **Kategorie** aus dem Dropdown.
6. Klicke auf das **Papierkorb-Symbol** neben dem **Ereignistyp**, den Du entfernen möchtest.
7. Klicke auf _Löschen_{:.doc-button} im Pop-up-Fenster, um das Löschen zu bestätigen, oder auf _Abbrechen_{:.doc-button}, um die Aktion nicht durchzuführen.
8. Klicke auf _Schließen_{:.doc-button}.

## Ein Ereignis zu einem Workload hinzufügen

Füge alle bekannten Ereignisse zu vergangenen und zukünftigen Tagen hinzu. Lasse längere Zeiträume mit ungewöhnlichen Mustern weg, da diese Zeiträume und Muster die Forecast-Qualität mit der Zeit verschlechtern.

Smart Workloads berücksichtigen bis zu zwei Tage vor und nach dem Datum des Ereignisses. Basic Workloads berücksichtigen nur die Auswirkungen am aktuellen Tag.

1. Gehe zu _Forecast_{:.menu-item}.
2. Wähle einen **Workload**.
3. Klicke auf _![Kontextmenü im injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} rechts im Abschnitt _Ereignisse_.
4. Klicke auf **Ereignisse zuweisen**.
   {{ 2 | image: "Ereignisse hinzufügen", '40%' }}
5. Wähle einen **Ereignistyp** aus dem Dropdown-Menü **Ereignistyp auswählen**.
6. Klicke in das **Wähle einen Tag** Feld und wähle einen **Tag** aus dem Kalender aus, um das Ereignis hinzuzufügen.
7. Klicke auf _Ereignis zuweisen_{:.doc-button}.
8. Klicke auf _Schließen_{:.doc-button}.

> Ein Ereignis vom Typ _Störung_ markiert einen Tag in der Vergangenheit als ungültig und schließt ihn von der Forecast-Berechnung aus.

## Deine Feiertagsregion hinzufügen

Füge Feiertage aus verschiedenen Feiertagskalendern hinzu. injixo Forecast behandelt Feiertage als Ereignisse, da sie das Volumen eines normalen Tages beeinflussen können. Normalerweise wählst Du die entsprechende Feiertagsregion beim {% link_new Erstellen eines Workloads | features/forecast/injixo-forecast/manage-workloads.md %}. So änderst Du die Feiertagsregion:

1. Gehe zu _Forecast_{:.menu-item}.
2. Wähle einen **Workload**.
3. Klicke auf _Workload bearbeiten_{:.doc-button}. Klicke alternativ rechts im Abschnitt _Ereignisse_ auf _![Kontextmenü im injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon}, dann auf **Feiertagsregion bearbeiten**.
4. Wähle eine **Feiertagsregion** aus dem Dropdown.
5. Klicke auf _Workload speichern_{:.doc-button}.

## Ereignisse und Feiertage anzeigen

1. Gehe zu _Forecast_{:.menu-item}.
2. Wähle einen **Workload**.
3. Gehe zum **Tag**, der **Woche** oder dem **Monat**, um Ereignisse für den ausgewählten Zeitraum zu sehen, oder wähle **Jahr**, um alle Ereignisse (gruppiert nach Monat) und Feiertage für dieses Jahr zu sehen. Die Diagramme markieren Ereignisse und Feiertage in Gelb und zeigen sie in einer Liste auf der rechten Seite an.

   {{ 3 | image: "Ereignisse anzeigen", '80%', 'gif' }}

## Ein Ereignis entfernen

Entferne irrelevante Ereignisse aus Deinen Workloads, wie z. B. ein storniertes Mailing oder eine dauerhaft verschobene Marketingaktivität.

1. Gehe zu _Forecast_{:.menu-item}.
2. Wähle einen **Workload**.
3. Gehe zum Ereignisdatum. Das Ereignis wird rechts unter _Ereignisse_ angezeigt.
4. Klicke auf _![Kontextmenü im injixo Forecast](/assets/img/common/forecast/context-menu.svg)_{:.doc-button-icon} rechts im Abschnitt _Ereignisse_.
5. Wähle **Ereignisse zuweisen** aus dem Dropdown.
6. Klicke auf das **Papierkorb-Symbol** neben dem **Ereignistyp**, den Du entfernen möchtest.
7. Klicke auf _Schließen_{:.doc-button}.
