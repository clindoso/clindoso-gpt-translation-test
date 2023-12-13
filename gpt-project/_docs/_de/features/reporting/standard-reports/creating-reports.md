---
title: Reports erstellen
redirect_from:
  - /de/available-reports/
redirect_reason: article deleted April 2022
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erzeuge Standard-Reports im HTML- oder PDF-Format mit unterschiedlichen Parametern.
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

In diesem Artikel lernst Du:
- wie Du Reports auf Basis verschiedener Parameter und Filter erstellst.
- wie die Reports Zeitzonen anzeigen.

Reports enthalten Plandaten aus verschiedenen Ebenen oder statistische und administrative Informationen. Lerne mehr über {% link_new Reports zu Planungseinheiten | features/reporting/standard-reports/planning-unit-reports.md %} und {% link_new Reports zu Mitarbeitern | features/reporting/standard-reports/employee-reports.md %}.

Du kannst Reports im HTML- oder PDF-Format erstellen. Installiere Adobe Acrobat Reader auf Deinem Computer, um PDF-Reports in Deinem Browser anzuzeigen.

> Auswahl-basierte Reports zeigen nur Inhalte an, wenn Du den ausgewählten Mitarbeitern mindestens eine {% link_new Auswahl | features/administration/selections.md %} zugewiesen hast.  

## Reports erstellen

1. Gehe zu *WFM > Controlling > Reports*{:.breadcrumbs}.
2. Wähle das **Startdatum** und **Enddatum**.


3. Nutze den Abschnitt *Filter*, um auszuwählen, was in Deinem Report angezeigt wird:

    - **Standardfilter:** Klicke auf eine **Planungseinheit**, einen **Vertrag** oder eine **Auswahl**, um die Mitarbeiterliste einzuschränken. Um mehrere Einträge auszuwählen, halte beim Klicken die **STRG**- oder **Shift-Taste**.

        {{ 2 | image: 'Standardfilter', '80%' }}

    - **Mitarbeiterfilter**: Wähle einen {% link_new Mitarbeiterfilter | features/administration/employee-filter.md %}, um eine eine benutzerdefinierte Mitarbeiterliste, z. B. basierend auf Qualifikationen, zu erstellen. Um einen neuen Filter zu erstellen, klicke auf **Filter-Editor**.

      <br>Aktiviere die Checkbox **Filterzeitraum entspricht Reportzeitraum**, um das in der Report-Benutzeroberfläche ausgewählte Start- und Enddatum zu überschreiben.

      {{ 3 | image: 'Mitarbeiterfilter', '60%' }}  

      Mitarbeiterfilter sind in injixo Essential WFM nicht verfügbar.

4. Klicke *Anwenden*{:.doc-button}.

5. Optional: Wähle im Abschnitt *Mitarbeiter* einzelne ***Mitarbeiter*** aus.

    {{ 5 | image: 'Abschnitt Mitarbeiter', '60%' }}

6. Im Abschnitt *Parameter* kannst Du:
    - die **Ebene** auswählen, aus der Du die Daten lesen möchtest.
    - das **Format** für die Datenausgabe festlegen (PDF oder HTML).
    - die Optionen zum {% link_new Versenden von Reports per E-Mail | features/reporting/standard-reports/email-reports.md %} an bestimmte Benutzer wählen.
    - definieren, ob Du Mitarbeiternamen und Personennummern anonymisieren möchtest.

    {{ 4 | image: 'Report-Parameter', '30%' }}

7. Klicke rechts im Abschnitt *Reports zu Planungseinheiten* oder *Reports zu Mitarbeitern* auf einen **Reportnamen**.

    {{ 6 | image: 'Liste der Reports mit Abschnitten', '50%' }}

    <br>
    Die Dokumenten-Symbole neben den Reportnamen zeigen, für welchen Zeitraum Du einen Report erzeugen kannst. Du kannst z. B. Tages- und Pausenpläne für maximal einen Monat erzeugen, andere Reports für maximal ein Jahr. 

Ein JobProcessor-Fenster öffnet sich. Der gewünschte Report wird erstellt und angezeigt.

Du kannst mehrere Reports mit denselben Parametern erstellen. Wenn Du einen Filter oder ein Datum änderst, musst Du erneut auf *Anwenden*{:.doc-button} klicken.

## Zeitzonen in Reports

Die Zeiten im Report beziehen sich auf die lokale Zeit der Planungseinheit. Im Kopf des Reports wird die Zeitdifferenz zwischen der Zeitzone der Planungseinheit und UTC sowie zwischen der Zeitzone der Planungseinheit und der lokalen Benutzerzeit angezeigt.

Beispiel: Ein Mitarbeiter in New York beginnt seine Schicht um 8:30 Uhr. Ein Report verwendet die Ortszeit von Manchester (UK), dem Standort der Planungseinheit. Die Zeitdifferenz beträgt +05:00. Der Mitarbeiter muss diese Zeitdifferenz von der angezeigten Zeit abziehen, um zu wissen, wann die Schicht beginnt. Die Schicht würde um 3:30 Uhr Ortszeit in New York beginnen.
