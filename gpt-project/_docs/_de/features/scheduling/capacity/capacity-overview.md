---
title: Was ist die Kapazitätsplanung?
product_label:
  - advanced
  - enterprise
toc: false
description: Lerne, was die Kapazitätsplanung ist und wie Du den Mitarbeiterbedarf, die Vertragskapazität und die resultierende Deckung für eine Planungseinheit anzeigst.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/capacity/capacity-insert-shift-sequences.md
---

*Plan > Kapazitätsplanung*{:.breadcrumbs} gibt Dir Einblicke in Deinen zukünftigen Einstellungs- und Schulungsbedarf. Bald führst Du hier Deine langfristige Planung durch.

> Das ist die allererste Version. Noch recht simpel? Schicke eine E-Mail mit Feedback und Ideen an *capacity-team@injixo.com*.

## Kapazität für eine Planungseinheit anzeigen

Wähle eine **Planungseinheit** aus,  um entsprechend den Mitarbeiterbedarf, die Vertragskapazität und die daraus resultierende Deckung je Kalenderwoche für das gesamte Jahr anzuzeigen. Alle Werte werden in Stunden angegeben.

Die Tabelle enthält die folgenden Zeilen:  

- *Mitarbeiterbedarf*: Die Summe aller Mitarbeiterbedarfe für alle Aktivitäten der ausgewählten Planungseinheit. Stelle sicher, dass Du zuerst die Mitarbeiterbedarfe für alle Aktivitäten der Planungseinheit im *Forecast-Modul* {% link_new berechnest und speicherst | features/forecast/injixo-forecast/staff-requirement.md %}. Ansonsten werden die Mitarbeiterbedarfe hier nicht angezeigt.
- *Vertragskapazität*: Die Summe der vertraglichen Soll-Arbeitsstunden aller Mitarbeiter der ausgewählten Planungseinheit. Es werden alle Mitarbeiter mit Vertrag berücksichtigt. Abwesenheiten haben keinen Einfluss auf die Zahlen. Die Zahlen basieren auf der Sollarbeitszeit pro Woche, die für jeden Vertrag im Abschnitt {% link_new Arbeitszeitvorgaben | features/administration/create-contracts.md | #arbeitszeitvorgaben %} definiert ist.
- *Potentielle Deckung*: Die Differenz der Werte für *Vertragskapazität* und *Mitarbeiterbedarf*.

{{ 1 | image: "Capacity Kapazitätstabelle", '100%' }}
