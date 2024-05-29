---
title: Reports erstellen
redirect_from:
  - /reports/
  - de/available-reports/
redirect_reason: The first redirect is pretty old. The second is for an article deleted in April, 2022.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erstelle Standard-Reports mit verschiedenen Parametern im HTML- oder PDF-Format.
promote-service: enhanced-reporting
toc: false
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/reporting/standard-reports/email-reports.md
  - overwrite_title: Add title for untranslated source
    filepath: features/reporting/standard-reports/planning-unit-reports.md
  - overwrite_title: Add title for untranslated source
    filepath: features/reporting/standard-reports/employee-reports.md
---

Unter _WFM > Controlling > Reports_{:.breadcrumbs} kannst du Reports auf der Datengrundlage von {% link_new Planungseinheiten | features/reporting/standard-reports/planning-unit-reports.md %} bzw. {% link_new Mitarbeitern | features/reporting/standard-reports/employee-reports.md %} erstellen.

Je nachdem, welche Parameter und Filter du verwendest, zeigen die Reports verschiedene Informationen an, z.&nbsp;B. geplante Schichten aus verschiedenen Ebenen oder Stammdaten von Mitarbeitern. Du kannst Reports im HTML- oder PDF-Format erstellen.

> Hinweis
>
> Reports auf der Grundlage von Auswahlen zeigen nur dann Inhalte an, wenn du deine Mitarbeiter mindestens einer {% link_new Auswahl | features/administration/selections.md %} zugewiesen hast.

## Reports erstellen

1. Wähle ein **Startdatum** und ein **Enddatum** aus.
2. Wähle im Abschnitt **Filter** aus, was in deinem Report angezeigt wird:
   - Wenn **Standardfilter** aktiviert ist: In allen Kästen ist standardmäßig die Option **[Alle]** ausgewählt. Um die Liste der Mitarbeiter einzugrenzen, wähle aus den Planungseinheiten, Verträgen oder Auswahlen eine oder mehrere Optionen aus.
   - Wenn **Mitarbeiterfilter** aktiviert ist: Wähle einen {% link_new Mitarbeiterfilter| features/administration/employee-filter.md %} aus, um eine benutzerdefinierte Mitarbeiterliste, z.&nbsp;B. basierend auf Qualifikationen, zu erstellen. Um das oben auf der Reports-Seite ausgewählte Start- und Enddatum zu überschreiben, aktiviere die Checkbox **Filterzeitraum entspricht Reportzeitraum**.
3. Klicke im Abschnitt **Mitarbeiter** auf _Anwenden_{:.doc-button}.
4. (Optional) Wähle im Abschnitt **Mitarbeiter** einzelne Mitarbeiter aus, um speziell zu ihnen Reports zu erstellen.
5. Konfiguriere im Abschnitt **Parameter** deinen Report:
   - **Ebene**
   - **Format**
   - **Report als E-Mail verschicken an**: Wähle aus dem Dropdown-Menü aus, ob und wie {% link_new Reports per E-Mail | features/reporting/standard-reports/email-reports.md %} an bestimmte Benutzer versendet werden sollen.
   - **Anonyme Auswertung**: Um Mitarbeiternamen und Personalnummern zu anonymisieren, wähle die Option **Ja**.
6. Wähle einen Reporttyp aus:
   - Um einen Report zu Planungseinheiten zu erzeugen, wähle eine Option aus der Liste {% link_new **Reports zu Planungseinheiten** | features/reporting/standard-reports/planning-unit-reports.md %} aus.
   - Um einen Report zu Mitarbeitern zu erzeugen, klicke auf {% link_new **Reports zu Mitarbeitern** | features/reporting/standard-reports/employee-reports.md %} und wähle eine Option aus der Liste aus.<br>
     Reports mit dem Einzelne-Datei-Icon {% icon report-icon-single-file | icon-only %} vor dem Reportnamen decken einen Zeitraum von bis zu einem Monat ab.<br>
     Reports mit dem Mehrere-Dateien-Icon {% icon report-icon-multiple-files | icon-only %} decken einen Zeitraum von bis zu einem Jahr ab.

## Zeitzonen in Reports

In einem Report entsprechen die angezeigten Zeiten der für die Planungseinheit konfigurierten Zeitzone. Die Kopfzeile eines Reports zeigt sowohl Unterschiede zwischen der Zeitzone der Planungseinheit und der koordinierten Weltzeit (UTC) als auch zwischen der Zeitzone der Planungseinheit und der lokalen Zeit des Benutzers an, der den Report aufruft.
