---
title: Variierende Anzahl Arbeitstage bei gleichen Wochenarbeitszeiten
redirect_from:
  - /de/best-practice-planning-with-different-wtm/
---

In diesem Artikel lernst Du, wie Du über ein Planungsmodell vom Typ B und zwei Wochenmodelle eine zwei-Wochen-Rotation mit 40h pro Woche planst, jeweils eine Woche mit 5 Tagen à 8 Stunden und eine Woche mit 4 Tage à 10 Stunden. Erforderlich zum Verständnis sind die Grundlagen zu Planungsmodellen <!-- link de/work-time-pattern-models once merged -->.

Der Artikel beschränkt sich auf ein einfaches Beispiel für Vollzeit-Verträge; die Stundenwerte sind beispielhaft und können bei Dir abweichen. Natürlich kannst Du auch Teilzeit-Verträge entsprechend abbilden.

## Erzeuge Tagesmodelle, Wochenmodelle und ein Planungsmodell

Erzeuge **zwei Tagesmodelle** mit 8 Stunden und 10 Stunden Arbeitszeit:

{{ 2 | image: 'Tagesmodell für 10 Stunden-Schicht', '75%' }}
{{ 3 | image: 'Tagesmodell für 8 Stunden-Schicht', '50%' }}

Erstelle für beide Wochen jeweils ein **Wochenmodell** und ordne das entsprechende Tagesmodell zu:

{{ 4 | image: 'Beispiel Wochenmodell 4x10h inkl. Tagesmodell', '75%' }}

Lege ein **Planungsmodell** an. Wähle **Typ B - Starre Rotation** für eine feste Rotation der Schichten (eine Woche 4x10h, eine Woche 5x8h):

{{ 5 | image: 'Planungsmodell mit Wochenmodell für 8 und 10 Stunden-Schichten', '75%' }}

## Erstelle einen Vertrag für die Rotation

- **Arbeitszeitvorgaben**

  - 5 Arbeitstage pro Woche
  - 40 Stunden als Minimum, Soll und Maximum pro Woche
  - 8 Stunden als Minimum, 10 Stunden als Maximum für den Tag.
    Die Arbeitszeitvorgaben müssen als Maximum pro Tag die längste der geplanten Schichten (Netto-Zeit) erlauben.

  {{ 6 | image: 'Vertrag mit angepassten Arbeitszeitvorgaben', '50%' }}

- **AutoScheduler-Parameter**  
   Passe den Parameter **Mindestanzahl Arbeitstage pro Woche** auf 4 Tage an. So kann der Mitarbeiter an weniger Tagen eingesetzt werden, als grundsätzlich über die Anzahl Arbeitstage im Vertrag festgelegt.

  {{ 7 | image: 'AutoScheduler-Parameter mit Mindestanzahl 4 Arbeitstage pro Woche', '50%' }}

- **Planungsparameter**  
   Ändere _2602_{:.id-label} _Maximale Dauer einer Aktivität_ auf 10 Stunden ab. Dieser Wert erlaubt eine höhere Arbeitszeit als die im Vertrag voreingestellten 8 Stunden.

{{ 8 | image: 'Planungsparameter Maximale Dauer einer Aktivität', '50%' }}

## Ordne Mitarbeitern Vertrag und Planungsmodell zu

Ordne Mitarbeitern einzeln oder per Massenbearbeitung (über Auswahlen) den Vertrag und das Planungsmodell zu.
Nutze unterschiedliche Montage als Referenzdatum für das Planungsmodell für bestimmte Mitarbeitergruppen<!-- link /de/reference-date/ if translated -->, um eine gleichmäßige Verteilung von Mitarbeitern mit vier und fünf Arbeitstagen pro Woche zu haben.

## Ergebnis der volloptimierten Planung

Das Planungsergebnis für zwei Wochen sieht dann wie folgt aus:

**Woche 1: 4 Schichten à 10 Stunden:**

{{ 9 | image: 'Planungswoche mit vier Arbeitstagen à zehn Stunden', '75%' }}

**Woche 2: 5 Tagesschichten à 8 Stunden:**

{{ 10 | image: 'Planungswoche mit fünf Arbeitstagen à acht Stunden', '75%' }}
