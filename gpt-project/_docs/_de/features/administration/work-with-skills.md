---
title: Mit Qualifikationen arbeiten
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du mit Qualifikationen in injixo die Fähigkeiten deiner Mitarbeiter abbilden kannst. Erstelle, bearbeite und lösche Qualifikationen und Qualifikationsstufen.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/configure-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
redirect_from:
  - /de/skills/
redirect_reason: Updated filename on 24 July 2023
---

Mit Qualifikationen kannst du sicherstellen, dass deine Mitarbeiter nur für Aktivitäten geplant werden, für die sie aufgrund ihrer Fähigkeiten geeignet sind. Qualifikationen ordnen die Fähigkeiten deiner Mitarbeiter (z.&nbsp;B. Produktwissen, Sprachkenntnisse, Kommunikationskanäle etc.) Aktivitäten zu, an denen sie arbeiten können und die du in injixo planen kannst.

Um Qualifikationen zu konfigurieren, gehe zu _Plan > Konfiguration > Qualifikationen_{:.breadcrumbs}.

## Qualifikationen erstellen

Erstelle mindestens eine Qualifikation für jede Aktivität, die eine bestimmte Fähigkeit voraussetzt. Wenn du eine Qualifikation erstellst, setzt injixo die Qualifikationsstufe standardmäßig auf 100%. Qualifikationsstufen bilden ab, wie ausgeprägt die Fähigkeiten der Mitarbeiter sein müssen, um eine bestimmte Aktivität ausführen zu können, z.&nbsp;B. 100% für Englisch, aber nur 50% für Spanisch. Du kannst pro Qualifikation mehrere Qualifikationsstufen hinzufügen. 

> Wenn eine Aktivität keine besonderen Fähigkeiten der Mitarbeiter erfordert, musst du dafür keine Qualifikation erstellen.

1. Klicke auf _Neue Qualifikation_{:.doc-button}.
2. Gib einen Namen ein.
   Die Kurzbezeichnung wird automatisch erzeugt, du kannst sie aber bearbeiten.
3. (Optional) Passe die Standardeinstellungen der Qualifikationsstufe an.
4. (Optional) Klicke auf _Qualifikationsstufe hinzufügen_{:.doc-button}, um weitere Qualifikationsstufen hinzuzufügen, wenn du Mitarbeiter hast, die für die Aktivität weniger qualifiziert sind. Siehe auch: [Eignung mithilfe von Bewertung und Gewichtung berechnen](#eignung-mithilfe-von-bewertung-und-gewichtung-berechnen).
5. Klicke auf _Qualifikation anlegen_{:.doc-button}.  

 Als nächstes kannst du [einem Mitarbeiter eine Qualifikationsstufe zuweisen](#mitarbeitern-qualifikationsstufen-zuweisen) und [die Qualifikation einer Aktivität zuweisen](#aktivitäten-qualifikationen-zuweisen).

## Qualifikationen kopieren

Um eine neue Qualifikation mit denselben Qualifikationsstufen wie eine bereits bestehende Qualifikation zu erstellen, gehe wie folgt vor:

1. Klicke in der Qualifikationsliste auf die Qualifikation, die du kopieren möchtest.
2. Klicke unter dem Qualifikationsnamen auf **Qualifikation kopieren**.  
   Ein Fenster **Neue Qualifikation anlegen** öffnet sich. Die Qualifikationsstufen sind vorausgefüllt.
3. Gib einen Namen für die neue Qualifikation ein.
4. (Optional) Bearbeite die Qualifikationsstufen.
5. Klicke auf _Qualifikation anlegen_{:.doc-button}.

## Qualifikationen und Qualifikationsstufen bearbeiten

1. Wähle eine Qualifikation aus der Liste.
2. Bearbeite die Qualifikation oder Qualifikationsstufe(n).
   Um eine Qualifikationsstufe zu löschen, klicke daneben auf das {% icon trash %}.
3. Klicke auf _Änderungen speichern_{:.doc-button}.

## Qualifikationen löschen

1. Wähle eine Qualifikation aus der Liste.
2. Klicke auf _Qualifikation löschen_{:.doc-button} und bestätige den Dialog.

## Aktivitäten Qualifikationen zuweisen

1. Gehe zu _Plan > Konfiguration > Aktivitäten_{:.breadcrumbs}.
2. Wähle eine Aktivität aus der Liste aus und scrolle bis zum Abschnitt **Qualifikationen**.
3. Wähle eine Qualifikation aus dem Dropdown-Menü.
4. (Optional) Ändere die **Gewichtung**. Wenn du nur eine Qualifikation hinzufügst, behalte den Standardwert von 100% bei.  
   Für Aktivitäten, die mehr als eine Qualifikation erfordern, kannst du über die [Gewichtung](#eignung-mithilfe-von-bewertung-und-gewichtung-berechnen) bestimmen, welche Qualifikation wichtiger ist.
7. Klicke auf _Änderungen speichern_{:.doc-button}.

## Mitarbeitern Qualifikationsstufen zuweisen

1. Gehe zu _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs}.
2. Wähle einen Mitarbeiter aus der Liste aus und navigiere zum Abschnitt **Qualifikationsstufen**.
3. Klicke auf das {% icon item-add %} und wähle eine oder mehrere Qualifikationsstufen aus der Liste aus.
   Um mehrere Einträge auszuwählen, halte beim Klicken die **STRG**- oder **Shift**-Taste.
4. (Optional) Füge einen {% link_new Gültigkeitszeitraum | features/administration/set-a-validity-period.md %} für die Qualifikationsstufe hinzu, indem du Daten für **Gültig vom** und **Gültig bis** hinzufügst.
   Du kannst einem Mitarbeiter innerhalb eines Gültigkeitszeitraums nicht verschiedene Qualifikationsstufen derselben Qualifikation zuweisen.
 5. Klicke auf _OK_{:.doc-button}.  
   Die Aktivitäten, für die die Qualifikation erforderlich ist, erscheinen im Abschnitt **Aktivitäten** im Konfigurationsfenster des Mitarbeiters.

Für eine Aktivität können eine oder mehrere Qualifikation erforderlich sein. Um an einer Aktivität zu arbeiten, für die mehrere Qualifikationen nötig sind, müssen die entsprechenden Mitarbeiter alle Qualifikationen erfüllen.

Tipp: Um eine Qualifikation mehreren Mitarbeitern auf einmal zuzuweisen, kannst du die Funktionalität {% link_new Massenbearbeitung | features/administration/employee-overview.md | #massenbearbeitung-verwenden %}. 

## Eignung mithilfe von Bewertung und Gewichtung berechnen

injixo kann auf Grundlage folgender Daten einen Eignungsgrad berechnen:

- Die Bewertung der Qualifikationsstufe eines Mitarbeiters
- Die Werte für die Gewichtung, wenn eine Aktivität mehrere Qualifikationen erfordert

Beispiel: Du hast eine Aktivität Anrufe auf Spanisch, für die zwei Qualifikationen nötig sind: Spanisch und Anrufe. Die Qualifikation Spanisch ist doppelt so wichtig wie die Qualifikation Anrufe. Spanisch wird mit einem Wert von 100 gewichtet und Anrufe mit einem Wert von 50.

- Mitarbeiter&nbsp;1 hat die Qualifikationsstufen Spanisch 50% und Anrufe 100%.
- Mitarbeiter&nbsp;2 hat die Qualifikationsstufen Spanisch 100% und Anrufe 50%.

Dies ergibt einen Eignungsgrad von 66,66% für Mitarbeiter&nbsp;1 und 83,33% für Mitarbeiter&nbsp;2.

Der Eignungsgrad wird mit der folgenden Formel berechnet: `(Summe(Gewichtung jeder Qualifikation * Qualifikationsstufe des Mitarbeiters für diese Qualifikation)) / (Summe der Gewichtung aller Qualifikationen)`

Wenn eine Aktivität nur eine Qualifikation erfordert, entspricht der Eignungsgrad der Qualifikationsstufe des Mitarbeiters.

Damit der Eignungsgrad (anstatt der Anzahl der Mitarbeiter) in der {% link_new optimierten Planung | features/scheduling/schedules/schedules-optimized-schedules.md %} beachtet wird, konfiguriere die Einstellung _48069_{:.id-label} _Prozentwert der Eignung für Aktivitäten beachten_. Im {% link_new Schicht Center | features/scheduling/shiftcenter/analyze-coverage-staffing-requirement.md %} und in {% link_new Schedules | features/scheduling/schedules/schedules-activity-coverage.md %} können die Deckung und Besetzung nicht auf Basis der Eignung der Mitarbeiter angezeigt werden. In diesen Fällen werden die Deckung und Besetzung immer als 100% angezeigt, um die Anzahl der Mitarbeiter darzustellen.
