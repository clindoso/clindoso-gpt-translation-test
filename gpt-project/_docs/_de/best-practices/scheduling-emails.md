---
title: E-Mails planen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie Du E-Mails planst.
promote-service: what-if-scenario
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

Du möchtest mit injixo zusätzlich E-Mails planen und fragst Dich, wie das funktioniert? Hier erklären wir Dir, was Du beachten musst.

## Separate Aktivität

1. Erstelle unter *WFM > Administration > Scheduling > Aktivitäten*{:.breadcrumbs} eine {% link_new Aktivität | features/administration/activity-examples.md %} E-Mail vom Typ *Anwesenheit*.
2. Setze die Häkchen für *Planbar*, *Bezahlt* und *Ruhezeit einhalten*.
3. Ordne diese Aktivität der Planungseinheit zu, in welcher Du E-Mails planen möchtest.

Wenn nicht alle Mitarbeiter E-Mails bearbeiten können oder sollen, benötigst Du eine {% link_new Qualifikation | features/administration/work-with-skills.md %} für die E-Mail-Aktivität.

Erstelle einen separaten Forecast für das E-Mail-Aufkommen. Dazu sollten die ankommenden E-Mails idealerweise auf Intervall-Basis aus Deiner Telefonanlage oder Deinem E-Mail-Tool importiert werden.
Nutze wie auch schon beim Telefonie-Forecast die prognostizierten Werte für das E-Mail-Aufkommen, um einen separaten Mitarbeiterbedarf für die Aktivität E-Mail zu erhalten.

Hinterlege einen konstanten Bedarf für E-Mails, beispielsweise zwei Mitarbeiter pro Intervall am Morgen und drei Mitarbeiter pro Intervall am Nachmittag.

Nutze für die Planung Tagesmodelle mit Anwesend-Aktivitäten, sodass die Optimierung diese Basis-Aktivität entweder mit Telefonie oder E-Mail ersetzen kann. Möglich sind aber auch feste E-Mail-Blöcke im Tagesmodell für die Bearbeitung von E-Mails ohne Mitarbeiterbedarf oder in bestimmten Zeiträumen.  

## Multiaktivität

Mitarbeiter mit beiden Qualifikationen für E-Mails und Telefon, kannst Du mit einer Multiaktivität planen, die sowohl Telefonie als auch E-Mail als Teilaktivitäten hat.

1. Erstelle unter *WFM > Administration > Scheduling > Aktivitäten*{:.breadcrumbs} eine Aktivität vom Typ *Anwesenheit* und nenne diese z.B. Multi-Phone-Mail.
2. Setze die Häkchen für *Planbar*, *Bezahlt* und *Ruhezeit einhalten*.
3. Erstelle eine E-Mail-Aktivität (falls noch nicht vorhanden eine zusätzliche Aktivität Telefonie).
4. Ordne diese Aktivitäten der Planungseinheit zu, in welcher Du E-Mails planen möchtest.
5. Füge E-Mail und Telefonie der Multi-Phone-Mail Aktivität hinzu, um eine Multiaktivität zu erzeugen.

Dieser Planungsansatz funktioniert nur mit der volloptimierten Planung (AutoScheduler). Achte bei der Bedarfsberechnung darauf, für die E-Mail-Aktivität andere Erlang-C Service Level Parameter zu verwenden als für die Telefonie, z.B. 80% in 14400 Sekunden im Gegensatz zu 80% in 20 Sekunden.
