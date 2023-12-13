---
title: Mitarbeiterbedarf berechnen
product_label:
  - advanced
  - enterprise
  - classic
description: Lerne, wie Du Mitarbeiterbedarf für Anrufe, Chats, E-Mails und mehr berechnest.
redirect_from:
  - /de/mitarbeiterbedarf/
  - /de/staff-requirement-parameter/
redirect_reason: Article used in intercom forecast tour, staff-requirement-parameter removed in April 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-backoffice-linear.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-asa.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-abandoned-calls.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-multiactivity.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-outbound.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-constant.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/employee-requirement.md
---

In diesem Artikel lernst Du:
* wie Du eine integrierte Methode zur Berechnung des Mitarbeiterbedarfs konfigurierst.
* wie Du den berechneten Mitarbeiterbedarf ansiehst.
* wie Du den Mitarbeiterbedarf für die Planung überträgst.
* andere verfügbare Methoden zur Berechnung des Mitarbeiterbedarfs kennen.

Berechne den Mitarbeiterbedarf für Deine Workloads auf Grundlage des erstellten Forecasts mit verschiedenen Berechnungsmethoden.

Neu bei injixo Forecast? Lerne zuerst {% link_new die Grundlagen | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Integrierte Methoden konfigurieren

1. Gehe zu **Forecast**.
2. Wähle einen **Workload**.
3. Gehe zum Abschnitt *Mitarbeiterbedarf* und klicke auf *Berechnungsparameter konfigurieren*{:.doc-button} für einen neuen Workload. Um eine bestehende Berechnungsmethode zu ändern, klicke auf *Berechnungsmethode bearbeiten*{:.doc-button}.
4. Wähle eine **Methode** aus dem Dropdown-Menü *Berechnungsmethode*.
   - Nutze **Erlang C** (für Anrufe), **Chat** oder **Linear** (für Backoffice-Volumina). Diese Methoden sind vollständig integriert; ihre Berechnungsergebnisse werden auf der Grundlage neuer Datenimporte, geänderter Berechnungsparameter oder {% link_new manueller Anpassungen | features/forecast/injixo-forecast/manual-adjustments.md %} aktualisiert.
   - Nutze **Andere** für andere nicht-automatisierte Skripte für verschiedene Anwendungsfälle. Lerne [wie Du die Berechnungsmethoden konfigurierst und verwendest](#weitere-berechnungsmethoden). <!-- EN header fixed in DE -->

5. Konfiguriere für *Erlang C* (für Anrufe), *Chat* oder *Linear* die erforderlichen und optionalen **Berechnungsparameter**. Die Berechnungsparameter hängen von der gewählten Berechnungsmethode ab.

    {{ 2 | image: "Berechnungsparameter Erlang C", '75%' }}

    Parameter | Details
    ---------------------- | ----------
    *Ziel-Servicelevel* | Prozentsatz der eingehenden Anrufe oder Chats, die innerhalb der *Ziel-Wartezeit* bearbeitet werden sollen
    *Ziel-Wartezeit* | Zeit, in der der im Parameter *Ziel-Servicelevel* angegebene Prozentsatz der Anrufe bzw. Chats bearbeitet werden soll, z. B. 80% der Anrufe in 20 Sekunden.
    *Shrinkage (Schwund) | Der Prozentsatz der ungeplanten Abwesenheiten, z. B. für Toiletten- und Trinkpausen, verspätet eintreffende Mitarbeitende, unerwartete Krankmeldungen oder technische Probleme. Um die Gesamtzahl der benötigten Mitarbeitenden einschließlich Schwund (s%) zu ermitteln, teile die Anzahl der Mitarbeitenden durch *(1 - s%)*. Wenn Du 70 Mitarbeitende benötigst und der Schwund 10% beträgt, benötigst Du insgesamt 78 Mitarbeitende.
    *Mindestbesetzung* | Gib einen Wert ein, um Intervalle mit niedrigeren Werten zu überschreiben. Wird in der Tagesansicht als horizontale Linie angezeigt.
    *Maximalbesetzung* | Gib einen Wert ein, um Intervalle mit höheren Werten zu überschreiben. Wird in der Tagesansicht als horizontale Linie angezeigt. Hinweis: Die eingegebenen Werte können die ursprünglich berechneten Mitarbeiterbedarfswerte überschreiben.  
    *Konstante durchschnittliche Vorgangsdauer (AHT)* | Gib einen Wert ein, um die prognostizierte AHT mit einem festen Wert zu überschreiben. Wähle **Die konstante AHT nur anwenden, wenn kein AHT-Wert verfügbar ist**, um den festen AHT-Wert nur für Zeiträume zu verwenden, in denen kein AHT-Wert als Ausweichmöglichkeit verfügbar ist. Standardmäßig verwendet die Mitarbeiterbedarfsberechnung die AHT-Werte aus dem Forecast.
    *Maximale Sitzungen* | Maximale Anzahl von parallelen Chat-Sitzungen, die Mitarbeitende gleichzeitig bearbeiten können.
    *Overhead* | Prozentsatz der AHT, den Mitarbeitende für Aufgaben aufwenden müssen, die nicht parallel erledigt werden können, z. B. das Hinzufügen von Notizen im CRM-System nach dem Anruf. Dieser Parameter hat keine Auswirkungen, wenn Du *1* für *Maximale Sitzungen* eingibst.

6. Wähle im Abschnitt *Speicherort* eine **Planungseinheit** und eine **Aktivität**. injixo speichert dort den berechneten Mitarbeiterbedarf, wenn Du [Mitarbeiterbedarf für die Planung verwendest](#mitarbeiterbedarf-für-die-planung-übertragen).
    {{ 3 | image: "Planungseinheit und Aktivität", '65%' }}
7. Klicke auf *Konfiguration speichern*{:.doc-button}.

### Berechneten Mitarbeiterbedarf ansehen

Der Abschnitt *Mitarbeiterbedarf* am unteren Rand zeigt ein Diagramm mit dem berechneten Mitarbeiterbedarf an. Der Bereich oberhalb des Diagramms zeigt die Berechnungsparameter sowie die daraus resultierenden insgesamt benötigten Personenstunden für den ausgewählten Zeitraum an.

Bewege den Mauszeiger über das Diagramm, um einen Tooltip anzuzeigen, der das Volumen und die AHT sowie die erforderlichen Mitarbeitenden für das Intervall (in der Tagesansicht) oder die Personenstunden für den Tag (Wochen- und Monatsansicht) anzeigt. Hinweis: Wenn Du eine feste durchschnittliche Bearbeitungszeit konfiguriert hast, zeigt der Tooltip den festen Wert anstelle der prognostizierten AHT an.

{{ 1 | image: 'Diagramm für Mitarbeiterbedarf'}}

### Mitarbeiterbedarf für die Planung übertragen

Übertrage den Mitarbeiterbedarf für einen bestimmten Zeitraum, um optimierte Zeitpläne zu erstellen oder eine Auftragsoptimierung durchzuführen.

1. Gehe auf *Forecast*{:.doc-button}.
2. Wähle einen **Workload**.
3. Wähle einen **Zeitraum**, für den Du den Bedarf verwenden möchtest. Hinweis: In der Jahresansicht kannst Du keine Mitarbeiterbedarfe übertragen.
4. Optional: Wähle im Abschnitt *Mitarbeiterbedarf* den **Forecast** oder die **Forecastversion** aus dem ersten Dropdown-Menü auf der rechten Seite für die Berechnung des Mitarbeiterbedarfs. Der ausgewählte Wert ist standardmäßig *Auto-Forecast*.

    > Um Forecastversionen oder einen importierten Forecast zu verwenden, musst Du zuvor für den ausgewählten Zeitraum {% link_new eine Forecastversion gespeichert | features/forecast/injixo-forecast/store-forecast-versions.md %} oder {% link_new einen Forecast importiert | features/forecast/injixo-forecast/import-forecast.md %} haben.

5. Klicke auf *Bedarf verwenden*{:.doc-button} im Bereich Mitarbeiterbedarf. Du siehst den ausgewählten Zeitraum, die Planungseinheit und die Aktivität in einem neuen Fenster. Wenn Du keine Planungseinheit und Aktivität in Deinem Workload konfiguriert hast, wird die Meldung *Nicht zugewiesen* angezeigt.
Um dies zu beheben, schließe das Fenster und klicke auf *Berechnungsmethode bearbeiten*{:.doc-button}, um eine Planungseinheit und eine Aktivität in Deiner Workload-Konfiguration hinzuzufügen.
6. Klicke auf *Speichern*{:.doc-button}, um den Mitarbeiterbedarf zu übertragen. Fahre mit dem Planungsprozess fort.

<!-- Überschrift in der Intercom-Forecasttour verwendet -->
## Weitere Berechnungsmethoden

Du kannst einen Mitarbeiterbedarf auch per Skript erstellen. Du musst das Skript in einem separaten Fenster konfigurieren und ausführen.

Methode | Verwendung
------------ | --------
Andere | Berechnungsmethoden für Backoffice, Berechnungen auf Basis der durchschnittlichen Antwortgeschwindigkeit und Abbruchraten.
Zusätzliche Skripte | Berechnungsmethoden für Multiaktivitäten und Outbound sowie ein Skript zum Schreiben eines konstanten Mitarbeiterbedarfs ohne Forecast. |  

### Die Berechnungsmethode *Andere* einrichten

1. Gehe zu **Forecast**.
2. Wähle einen **Workload**.
3. Klicke im Abschnitt *Mitarbeiterbedarf* auf *Berechnungsmethode bearbeiten*{:.doc-button}.
4. Wähle **Andere** als **Berechnungsmethode**.
5. Klicke auf *Speichern*{:.doc-button}.

So führst Du die Skripte aus:

1. Wähle den **Zeitraum**, für den Du den Mitarbeiterbedarf speichern möchtest.
2. Klicke auf _Forecast verwenden_{:.doc-button}, um den Forecast für den ausgewählten Zeitraum in die *Auto-Forecast*-Version im WFM-Teil von injixo zu übertragen.
3. Wähle das **Skript** aus dem Dropdown-Menü im Abschnitt *Mitarbeiterbedarf*. Es öffnet sich ein neues Fenster oder ein neuer Browser-Tab.
4. Wähle **Auto-Forecast** als **Version**, um das Skript auf der Grundlage des berechneten Forecasts auszuführen. Konfiguriere die anderen Berechnungsparameter.
5. Klicke auf _OK_{:.doc-button}, um das Skript auszuführen.

Ein neues Fenster zeigt die Berechnungsergebnisse. Die Werte werden gespeichert.

### Bedarf für Multiaktivitäten oder Outbound-Kampagnen berechnen

1. Gehe zu *Forecast*{:.doc-button}.
2. Wähle einen **Workload**.
3. Wähle den **Zeitraum**, für den Du den Mitarbeiterbedarf speichern möchtest.
4. Klicke auf _Forecast verwenden_{:.doc-button}, um den Forecast für den gewünschten Zeitraum in die Version *Auto-Forecast* zu übertragen.
    > Bevor Du das Skript für Multiaktivitäten startest, klicke in jedem Workload für die Teilaktivitäten auf _Forecast verwenden_{:.doc-button}.  

3. Klicke oben rechts auf **Berechnungen für Multiaktivitäten, konstanten Bedarf und Outbound**.
4. Wähle ein **Bedarfsskript** aus dem **Dropdown-Menü**. Es öffnet sich ein neues Fenster oder ein neuer Browser-Tab.
5. Konfiguriere die Berechnungsparameter. Wähle **Auto-Forecast** als **Version**, um das Skript auf der Grundlage des berechneten Forecasts auszuführen.
6. Klicke auf _OK_{:.doc-button}, um das Skript auszuführen.

Ein neues Fenster zeigt die Berechnungsergebnisse. Die Werte werden gespeichert.

### Konstante Bedarfe schreiben

1. Gehe zu *Forecast*{:.doc-button}.
1. Klicke auf **Berechnungen für Multiaktivität, konstanten Bedarf und Outbound**.
4. Wähle das Skript **Konstanter Bedarf** aus dem **Dropdown-Menü**. Es öffnet sich ein neues Fenster oder ein neuer Browser-Tab.
5. Konfiguriere die Skriptparameter.
6. Klicke auf _OK_{:.doc-button}, um das Skript auszuführen.

Ein neues Fenster zeigt die Berechnungsergebnisse. Die Werte werden gespeichert.
