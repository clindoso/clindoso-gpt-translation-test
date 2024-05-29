---
title: Verfügbarkeiten
product_label:
  - advanced
  - enterprise
  - classic
description: Erstelle wiederverwendbare Verfügbarkeiten, um Zeiträume zu definieren, in denen Mitarbeiter geplant werden können.
redirect_from:
  - /de/daymodel-availabilities/
redirect_reason: rename article September 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
toc: true
---

Mit Verfügbarkeiten kannst du festlegen, wenn ein Mitarbeiter an bestimmten Tagen oder zu bestimmten Zeiten nicht oder nur teilweise geplant werden kann. Du kannst zudem die Einschränkungen noch weiter eingrenzen, die die Öffnungszeiten deiner Planungseinheit und die Verträge deiner Mitarbeiter vorgeben.

Du kannst eine Schicht oder Aktivität nur dann in den Schichtplan einfügen, wenn sie in den konfigurierten Zeitraum passt. Mitarbeiter ohne konfigurierte Verfügbarkeit gelten innerhalb deiner Öffnungszeiten als jederzeit verfügbar.

Es gibt viele Anwendungsmöglichkeiten für Verfügbarkeiten, wie zum Beispiel:

- Feste Arbeitstage/Zeiten für jede Woche konfigurieren
- Verfügbarkeiten über Wochen hinweg wechseln
- Zeitweise verfügbare Mitarbeiter konfigurieren

Standardmäßig berücksichtigt injixo Verfügbarkeiten bei der Erstellung von optimierten Schichtplänen. Verfügbarkeiten werden nicht beim Erzeugen der Schichten berücksichtigt, sondern beim Zuteilen der Schichten.

injixo überprüft Verfügbarkeiten nur, wenn die Planungsregel _2611_{:.id-label} aktiviert ist. Deaktiviere diese Regel, damit deine Mitarbeiter auch Wünsche für Schichten abgeben und Schichten zugeteilt bekommen können, die länger sind als ihre Verfügbarkeiten.

## Verfügbarkeiten konfigurieren

Es gibt zwei Möglichkeiten, Verfügbarkeiten zu konfigurieren:

- Persönliche Verfügbarkeiten: Konfiguriere temporäre oder dauerhafte Verfügbarkeiten für einzelne Mitarbeiter unter _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs}.
- Tagesmodell-Verfügbarkeiten: Füge Verfügbarkeiten zu Schichtfolgen hinzu, um mehreren Mitarbeitern die gleiche Verfügbarkeit zuzuweisen.

Hinweis: Tagesmodell-Verfügbarkeiten überschreiben sowohl persönliche Verfügbarkeiten als auch manuell eingefügte Verfügbarkeiten.

## Feste Arbeitstage/Zeiten für jede Woche konfigurieren

Beispiel: Ein Mitarbeiter kann aufgrund von Kinderbetreuung nur mittwochs und freitags am Vormittag von 08:00&nbsp;Uhr bis 12:00&nbsp;Uhr arbeiten. Du kannst die Verfügbarkeit wie folgt konfigurieren:

1. Gehe zu _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs}.
2. Wähle den Mitarbeiter aus der Liste aus.
3. Klicke im Bereich **Verfügbarkeit** auf das Hinzufügen-Icon {% icon item-add | icon-only %}.
4. Konfiguriere die Verfügbarkeit:
   - (Optional) **Gültig vom** und **Gültig bis**: Wenn die Verfügbarkeit nur für einen bestimmten Zeitraum gilt, schränkt dies den {% link_new Gültigkeitszeitraum | features/administration/set-a-validity-period.md %} ein.
   - **Tagestypen**: Wähle Mittwoch und Freitag aus. Halte STRG gedrückt, um mehrere Einträge auszuwählen.
   - **Von**: Gib 8:00 ein.
   - **Bis**: Gib 12:00 ein.
5. Klicke auf _OK_{:.doc-button}.

## Verfügbarkeiten über Wochen hinweg wechseln

In den folgenden Abschnitten erfährst du, wie du mit Hilfe von Verfügbarkeiten wie im folgenden Beispiel oder vergleichbaren Anwendungsfällen deinen Schichtplan erstellen kannst:

- Dein Contact Center ist von 8:00&nbsp;Uhr bis 20:00&nbsp;Uhr geöffnet.
- In geraden Wochen übernimmt Planungseinheit&nbsp;A die Vormittagsschichten und Planungseinheit&nbsp;B die Abendschichten.
- In ungeraden Wochen ist es umgekehrt.
- Die Vormittagsschicht geht von 8:00&nbsp;Uhr bis 14:00&nbsp;Uhr.
- Die Abendschicht geht von 14:00&nbsp;Uhr bis 20:00&nbsp;Uhr.

### Tagesmodelle vom Typ Verfügbarkeitsrahmen erstellen

Um {% link_new Tagesmodelle zu erstellen | features/administration/daymodels/daymodel-creation.md %}, gehe zu _Plan > Konfiguration > Tagesmodelle_{:.breadcrumbs} und klicke auf das Neu-Icon {% icon item-add | icon-only %}.<br>Das folgende Beispiel zeigt, wie du zwei Tagesmodelle aufsetzt, damit sich eine Vormittagsschicht und eine Abendschicht abwechseln.

Um das Tagesmodell für die Vormittagsschicht zu konfigurieren, gehe wie folgt vor:

1. Erstelle ein neues Tagesmodell.
2. Konfiguriere das Tagesmodell:
   - **Typ**: Wähle die Option **Verfügbarkeitsrahmen**.
   - **Name** und **Kurzbezeichnung**: Gib einen eindeutigen Namen und eine Kurzbezeichnung ein, z.&nbsp;B. Verfügbarkeit 8:00-14:00 und Verf 8-14.
   - (Optional) **Farbe**: Wähle eine Farbe aus, um das Tagesmodell leichter wiederzuerkennen.
   - **Verfügbarkeitsrahmen Beginn**: Gib 8:00 ein.
   - **Verfügbarkeitsrahmen Ende**: Gib 14:00 ein.<br> Lege alternativ eine **Verfügbarkeitsrahmen Dauer** fest. Der Maximalwert ist 48 Stunden.
3. Klicke auf _OK_{:.doc-button}.

Um das Tagesmodell für die Abendschicht zu konfigurieren, gehe wie folgt vor:

1. Erstelle ein neues Tagesmodell.
2. Konfiguriere das Tagesmodell:
   - **Typ**: Wähle die Option **Verfügbarkeitsrahmen**.
   - **Name** und **Kurzbezeichnung**: Gib einen eindeutigen Namen und eine Kurzbezeichnung ein, z.&nbsp;B. Verfügbarkeit 14:00-20:00 und Verf 14-20.
   - (Optional) **Farbe**: Wähle eine Farbe aus, um das Tagesmodell leichter wiederzuerkennen.
   - **Verfügbarkeitsrahmen Beginn**: Gib 14:00 ein.
   - **Verfügbarkeitsrahmen Ende**: Gib 20:00 ein.<br> Lege alternativ eine **Verfügbarkeitsrahmen Dauer** fest. Der Maximalwert ist 48 Stunden.
3. Klicke auf _OK_{:.doc-button}.

### Schichtfolge erstellen und zuweisen

Um die beiden gerade erstellten Tagesmodelle für die Planung zu nutzen, gehe wie folgt vor:

1. {% link_new Erstelle eine Schichtfolge | features/administration/shift-sequences.md | #schichtfolgen-erstellen %} mit zwei **Mitarbeiterzeilen** und einer **Dauer** von 14&nbsp;Tagen.<br>
2. Füge die beiden Tagesmodelle in die Schichtfolge ein, die sich abwechseln sollen. Füge in Zeile&nbsp;1 das Vormittags-Tagesmodell in Woche&nbsp;1 und das Abend-Tagesmodell in Woche&nbsp;2 ein. Kehre in Zeile&nbsp;2 die Reihenfolge um.
3. {% link_new Weise | features/administration/employee-overview.md | #eine-schichtfolge-zuweisen %} deinen Mitarbeitern die Schichtfolge zu:
   - Wähle die erste Mitarbeiterzeile für Mitarbeiter in Planungseinheit&nbsp;A.
   - Wähle die zweite Mitarbeiterzeile für Mitarbeiter in Planungseinheit&nbsp;B.
   - Lege ein **Referenzdatum** fest, um festzulegen, ab wann die Schichtfolge in der Schichtplanung verwendet wird. Setze das Referenzdatum auf den Wochentag, an dem deine Planungswoche beginnt, z.&nbsp;B. Montag.
4. {% link_new Füge die Schichtfolge | features/scheduling/schedules/schedules-insert-shift-sequences.md | #schichtfolgen-einfügen %} in deinen Schichtplan ein.

## Zeitweise verfügbare Mitarbeiter konfigurieren

Beispiel: Einer deiner Mitarbeiter kann in einer bestimmten Woche nur von 9:00&nbsp;Uhr bis 12:00&nbsp;Uhr arbeiten.<br>Um dessen Verfügbarkeit entsprechend zu konfigurieren, befolge die Schritte zur [Konfiguration von festen Arbeitstagen/Zeiten pro Woche](#feste-arbeitstagezeiten-für-jede-woche-konfigurieren). Füge den entsprechenden {% link_new Gültigkeitszeitraum | features/administration/set-a-validity-period.md %} und die korrekten Werte für **Von** und **Bis** hinzu.

## Verfügbarkeiten bearbeiten

Du kannst Verfügbarkeiten bearbeiten, die du für einzelne Mitarbeiter konfiguriert hast:

1. Gehe zu _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs}.
2. Wähle den Mitarbeiter aus, dessen Verfügbarkeit du bearbeiten möchtest.
3. Klicke im Konfigurationsfenster auf der rechten Seite auf **Verfügbarkeiten**.
4. Klicke neben der Verfügbarkeit, die du bearbeiten möchtest, auf das {% icon pencil %}.
5. Bearbeite die Verfügbarkeit.
6. Klicke im Fenster **Verfügbarkeiten** auf _OK_{:.doc-button}.
7. Klicke unten im Konfigurationsfenster auf der rechten Seite auf _OK_{:.doc-button}.

Wenn du Verfügbarkeiten mit Tagesmodellen vom Typ **Verfügbarkeitsrahmen** konfiguriert hast, bearbeite das Tagesmodell:

1. Gehe zu _Plan > Konfiguration > Tagesmodelle_{:.breadcrumbs}.
2. Wähle das Tagesmodell aus, das du bearbeiten möchtest.
3. Bearbeite das Tagesmodell.
4. Klicke auf _OK_{:.doc-button}.

Du kannst Verfügbarkeiten auch im Schicht Center bearbeiten. Erfahre mehr darüber, wie du {% link_new Verfügbarkeiten im Schicht Center hinzufügen und löschen | features/scheduling/shiftcenter/add-and-delete-items.md | #verfügbarkeit-hinzufügen %} kannst. Für temporäre Änderungen kannst du persönliche Verfügbarkeiten und Verfügbarkeiten aus Tagesmodellen in eine Zelle kopieren, um sie in manuell eingefügte Verfügbarkeiten umzuwandeln.

Das Schicht Center zeigt Verfügbarkeiten in jeder Ebene mit dem Symbol `<>` an. Bewege den Mauszeiger über das Symbol, um einen Tooltip mit den Details anzuzeigen. In den Tageszellen werden alle Verfügbarkeiten als orangefarbene Elemente dargestellt. In ausgeklappten Tageszellen erscheinen die Verfügbarkeiten der Mitarbeiter als weiße Balken, die orange unterstrichen sind.

## Verfügbarkeiten löschen

Du kannst Verfügbarkeiten löschen, die du für einzelne Mitarbeiter konfiguriert hast:

1. Gehe zu _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs}.
2. Wähle den Mitarbeiter aus, dessen Verfügbarkeit du löschen möchtest.
3. Klicke im Konfigurationsfenster auf der rechten Seite auf **Verfügbarkeiten**.
4. Klicke neben der Verfügbarkeit, die du löschen möchtest, auf das {% icon item-delete %}.
5. Klicke im Fenster **Bestätigung** auf _Ja_{:.doc-button}.
6. Klicke auf _OK_{:.doc-button}.

Wenn du Verfügbarkeiten mit Tagesmodellen vom Typ **Verfügbarkeitsrahmen** konfiguriert hast, lösche das Tagesmodell:

1. Gehe zu _Plan > Konfiguration > Tagesmodelle_{:.breadcrumbs}.
2. Wähle das Tagesmodell aus, das du löschen möchtest.
3. Klicke in der Aktionsleiste auf das {% icon item-delete %}.
4. Klicke im Fenster **Bestätigung** auf _Ja_{:.doc-button}.

## Verfügbarkeiten in injixo Me

Du kannst Mitarbeitern erlauben, in injixo Me {% link_new eigene Verfügbarkeiten einzutragen | features/injixo-me/use-injixo-me/explore-injixo-me.md | #trage-deine-verfügbarkeiten-ein-verfügbarkeit %}. Mitarbeiter können bis zu 14&nbsp;Verfügbarkeiten hinzufügen. Lösche regelmäßig veraltete Einträge aus der Liste, bevor du einen Schichtplan erstellst, um potenzielle Planungsfehler zu vermeiden.

Damit deine Mitarbeiter ihre Verfügbarkeiten in injixo Me eintragen können, gehe wie folgt vor:

1. Gehe zu **Me**.
2. Aktiviere die Option **Verfügbarkeiten**.

Mitarbeiter können dann ihre wöchentlichen Verfügbarkeiten in injixo Me hinzufügen oder bearbeiten. Ihre Verfügbarkeiten werden in ihren Stammdaten angezeigt.
