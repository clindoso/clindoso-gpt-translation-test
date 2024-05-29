---
title: Mitarbeiterbedarf berechnen
redirect_from:
  - /de/mitarbeiterbedarf/
  - /de/staff-requirement-parameter/
  - /de/staff-requirement/
redirect_reason: Updated filename on 04 March 2024
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Ermittle den Mitarbeiterbedarf für Anrufe, Chat, E-Mail und weitere.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/multiactivity-script.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/outbound-calls-script.md
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/requirement-scripts/requirement-constant.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/edit-or-delete-staff-requirements.md
---

Wenn du einen Forecast erzeugt hast, kannst du den Mitarbeiterbedarf berechnen. Du kannst in injixo aus verschiedenen Bedarfsskripten und Berechnungsmethoden auswählen. Bei Bedarf kannst du auch ein Skript für konstanten Mitarbeiterbedarf ohne einen Forecast verwenden.

Neu in injixo Forecast? Lerne zuerst {% link_new die Grundlagen | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Berechnungsmethoden und Bedarfsskripte

injixo bietet verschiedene Berechnungsmethoden und Bedarfsskripte.
Erfahre, {% link_new welches Bedarfsskript bzw. welche Berechnungsmethode| best-practices/requirement-scripts.md %} am besten für deinen Anwendungsfall geeignet ist.<br>
Erfahre im folgenden Abschnitt, wie du die [Berechnungsmethoden](#berechnungsmethoden-konfigurieren) konfigurieren kannst.<br>
Um zu erfahren, wie du die Bedarfsskripte konfigurierst, klicke auf die folgenden Links:

- {% link_new Skript für Multiaktivitäten | features/forecast/requirement-scripts/multiactivity-script.md %}
- {% link_new Skript für Outbound | features/forecast/requirement-scripts/outbound-calls-script.md %}
- {% link_new Skript für Konstanten Bedarf| features/forecast/requirement-scripts/requirement-constant.md %}

## Berechnungsmethoden konfigurieren

Die Berechnungsmethode berechnet den Mitarbeiterbedarf auf der Grundlage von neuen Datenimporten, geänderten Berechnungsparametern oder {% link_new manuellen Anpassungen | features/forecast/injixo-forecast/manual-adjustments.md %}.
Du kannst deine Berechnungsmethode jederzeit ändern.

1. Wähle in _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Klicke im Abschnitt **Mitarbeiterbedarf** auf _Mitarbeiterbedarf bearbeiten_{:.doc-button}.
3. Wähle aus dem Dropdown-Menü **Berechnungsmethode** eine Option aus:
   - **Erlang-C**
   - **Chat**
   - **Linear**
4. Konfiguriere im Abschnitt **Berechnungsparameter** die [Berechnungsparameter](#berechnungsparameter).
5. Wähle im Abschnitt **Zugehörige Planungseinheit und Aktivität** die Planungseinheit und die Aktivität aus, für die du den Mitarbeiterbedarf verwenden möchtest.  
   Erfahre mehr darüber, wie du den [Mitarbeiterbedarf für die Schichtplanung verwendest](#mitarbeiterbedarf-für-schichtplanung-verwenden).
6. Klicke auf _Speichern_{:.doc-button}.

Der Graph im Abschnitt **Mitarbeiterbedarf** zeigt den berechneten Mitarbeiterbedarf an.<br> Unter dem Graphen kannst du die für die Parameter konfigurierten Werte und die Gesamtpersonenstunden einsehen, die für den ausgewählten Zeitraum nötig sind.<br> Bewege den Mauszeiger über dem Graphen, um pro Intervall detaillierte Informationen über das Volumen, die AHT, den Mitarbeiterbedarf, manuelle Anpassungen und hinzugefügte Ereignisse anzuzeigen.

### Berechnungsparameter

Die folgende Tabelle enthält die Parameter, die du je Berechnungsmethode konfigurieren kannst:

| Parameter                                   | Beschreibung                                                                                                                                                                                                                                                                                                                | Konfigurierbar in Erlang-C | Konfigurierbar in Chat | Konfigurierbar in Linear |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ---------------------- | ------------------------ |
| Angestrebtes Servicelevel                   | Prozentsatz der eingehenden Anrufe oder Chats, die innerhalb der angestrebten Antwortzeit bearbeitet werden sollen.                                                                                                                                                                                                         | Ja                         | Ja                     | Nein                     |
| Angestrebte Antwortzeit                     | Zeit, in der der im Parameter Angestrebtes Servicelevel angegebene Prozentsatz der Anrufe bzw. Chats bearbeitet werden soll.                                                                                                                                                                                                | Ja                         | Ja                     | Nein                     |
| Shrinkage (Schwund)                         | Der Prozentsatz der bezahlten Zeit, während der Mitarbeiter nicht arbeiten können, z.&nbsp;B. wegen Toilettenpausen, Zuspätkommen, ungeplanter Abwesenheit wegen Krankheit oder technischen Problemen.                                                                                                                      | Ja                         | Ja                     | Ja                       |
| Mindestbesetzung                            | Gib einen Wert ein, um Intervalle mit niedrigeren Werten für den Mitarbeiterbedarf zu überschreiben.                                                                                                                                                                                                                        | Ja                         | Ja                     | Ja                       |
| Maximalbesetzung                            | Gib einen Wert ein, um Intervalle mit höheren Werten für den Mitarbeiterbedarf zu überschreiben.                                                                                                                                                                                                                            | Ja                         | Ja                     | Ja                       |
| Feste durchschnittliche Vorgangsdauer (AHT) | Gib einen Wert ein, um die prognostizierte AHT zu überschreiben.<br>Aktiviere die Checkbox **Die feste AHT nur anwenden, wenn kein AHT-Wert verfügbar ist**, um den festen AHT-Wert nur für Zeiträume ohne AHT-Daten zu verwenden. Standardmäßig verwendet die Mitarbeiterbedarfsberechnung die AHT-Werte aus dem Forecast. | Ja                         | Ja                     | Ja                       |
| Maximale Sitzungen                          | Maximale Anzahl von parallelen Chat-Sitzungen, die Mitarbeiter gleichzeitig bearbeiten können.                                                                                                                                                                                                                              | Nein                       | Ja                     | Nein                     |
| Overhead                                    | Prozentsatz der AHT, den Mitarbeiter für Aufgaben aufwenden müssen, die nicht parallel erledigt werden können, z.&nbsp;B. das Hinzufügen von Notizen im CRM-System nach einem Anruf. Dieser Parameter wird nicht berücksichtigt, wenn du im Feld **Maximale Sitzungen** den Wert&nbsp;1 eingibst.                           | Nein                       | Ja                     | Nein                     |

## Mitarbeiterbedarf für Schichtplanung verwenden

Um einen Schichtplan auf Grundlage des Mitarbeiterbedarfs zu erstellen, musst du den Mitarbeiterbedarf zunächst speichern. Um den Mitarbeiterbedarf zu speichern, befolge die untenstehenden Schritte.

Du kannst nur Mitarbeiterbedarf verwenden, der für Forecast-Versionen berechnet wurde oder importierte Forecasts, die du für den Zeitraum deiner Wahl gespeichert hast.<br>
Erfahre mehr über {% link_new Forecast-Versionen | features/forecast/injixo-forecast/save-forecast-versions.md %} oder darüber, wie du {% link_new einen Forecast importierst | features/forecast/injixo-forecast/import-forecast.md %}.

1. Wähle in _Forecast > Workloads_{:.breadcrumbs} einen Workload aus.
2. Wähle den Zeitraum, für den du den Mitarbeiterbedarf verwenden möchtest.
3. Wähle im Abschnitt **Mitarbeiterbedarf** eine Forecast-Version aus dem Dropdown-Menü links aus.
4. Klicke auf _Mitarbeiterbedarf speichern_{:.doc-button}.
5. Klicke im Fenster **Mitarbeiterbedarf speichern** auf _Speichern_{:.doc-button}.

injixo speichert den Mitarbeiterbedarf für die Planungseinheit und die Aktivität, die du bei der Konfiguration der Berechnungsmethode ausgewählt hast.

> Hinweis
>
> Du kannst den Mitarbeiterbedarf auch für eine andere Planungseinheit oder Aktivität verwenden. <br> Um dies zu tun, wiederhole die Schritte zur [Konfiguration der Berechnungsmethode](#berechnungsmethoden-konfigurieren) und wähle eine andere Planungseinheit oder Aktivität aus. Führe anschließend die Schritte zum [Verwenden des Mitarbeiterbedarfs für die Schichtplanung](#mitarbeiterbedarf-für-schichtplanung-verwenden) aus.
