---
title: Genehmigungsregeln und Quoteneinstellungen
description: Richte Urlaubsquoten und Genehmigungsregeln ein, um Vorschläge für die Genehmigung von Urlaub und Abwesenheiten zu erzeugen.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-entitlement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-absences-management.md
---

Das Modul Urlaub/Abwesenheiten erlaubt dir, Genehmigungsregeln zu konfigurieren und Quoten festzulegen. injixo nutzt Genehmigungsregeln und Quoten, um damit Vorschläge für die Genehmigung von Urlaubs- und Abwesenheitsanträgen zu erzeugen.

Neu bei Urlaub/Abwesenheiten? Lerne zuerst die {% link_new Grundlagen | features/scheduling/time-off/vacation-absences-management.md %}).

## Einstellungen für Vorschläge konfigurieren

1. Gehe zu *Plan > Urlaub/Abwesenheiten*{:.breadcrumbs}. 
2. Klicke auf *Vorschläge konfigurieren*{:.doc-button}.
3. (Optional) Prüfe und ändere die vorausgewählte **Planungseinheit**.

### Genehmigungsregeln konfigurieren

Im Abschnitt **Genehmigungsregeln**, kannst Du bis zu drei Regeln für das Vorschlagsverfahren aktivieren:

- Urlaubsanspruch: Prüft, ob der Mitarbeiter noch genügend Urlaubstage hat. injixo kann eine Genehmigung vorschlagen, wenn der Mitarbeiter noch genügend {% link_new Urlaubsanspruch | features/scheduling/time-off/vacation-entitlement.md %} für das Jahr hat.
- Mitarbeiterbedarf: Prüft die Deckung des durchschnittlichen Tagesbedarfs einer Planungseinheit. Genehmigungen sind möglich, wenn genügend Personen arbeiten, um den {% link_new Mitarbeiterbedarf | features/scheduling/edit-or-delete-staff-requirements.md %} zu decken, basierend auf dem durchschnittlichen täglichen Mitarbeiterbedarf für alle Aktivitäten in der Planungseinheit.
- Abwesenheits-Quote: Überprüft das verfügbare Abwesenheitskontingent einer Planungseinheit. Genehmigungen sind möglich, wenn der konfigurierte Wert für die Abwesenheitsquote noch nicht erreicht ist.

{{ 1 | image: 'Genehmigungsregeln', '90%' }}

Um die Konfiguration zu speichern, klicke auf _Regeln speichern_{:.doc-button}.

## Quoteneinstellungen

Im Abschnitt **Quoteneinstellungen**, kannst Du allgemeine Quoteneinstellungen festlegen. Die Zielquote ist der Anteil an Mitarbeitern, die an einem bestimmten Tag abwesend sein dürfen.

 {{ 2 | image: 'Quoteneinstellungen', '75%' }}

### 1. Vollzeitäquivalent


Wenn die Option **Vollzeitäquivalent** deaktiviert ist, kann eine bestimmte Anzahl oder ein bestimmter Prozentsatz an Mitarbeitern abwesend sein - unabhängig davon, ob es sich um Vollzeit- oder Teilzeitbeschäftigte handelt.

Wenn die Option **Vollzeitäquivalent** aktiviert ist, wird die Dauer einer Anfrage im Verhältnis zum definierten Vollzeitäquivalent (z. B. acht Stunden) in das Kontingent einbezogen. Eine Anfrage mit einer Dauer von vier Stunden wird für Vollzeitbeschäftigte als halber Tag gezählt. Für einen Mitarbeiter mit einem Vier-Stunden-Äquivalent würde die gleiche Anfrage als ganzer Tag zählen.

### 2. Einheit der Quote

Wechsele zwischen **Anzahl an Mitarbeitern** und **Prozent** je nach Unternehmensanforderungen.

### 3. Basisquote

Wenn **Anzahl an Mitarbeitern** aktiviert ist, gib eine absolute Zahl in dieses Feld ein. Wenn die Option **Prozent** aktiviert ist, gib einen Wert in Prozent der Mitarbeiter ein.

Wenn Du **Anzahl der Mitarbeiter** auswählst, ist die Quote unabhängig von der Größe der Planungseinheit.

Bei einer prozentualen Einstellung führt eine 10% Quote bei einer Planungseinheit mit 50 Mitarbeitern zu maximal 5 abwesenden Mitarbeitern. Wenn die Anzahl der verfügbaren Mitarbeiter auf 55 steigt, würde der Wert bei einer Quote von 10% auf 5,5 Mitarbeiter erhöht. Im Gegensatz dazu würde bei der Option **Anzahl der Mitarbeiter** eine auf 5 festgelegte Quote unabhängig von der Gesamtzahl der Mitarbeiter gleich bleiben.

### 4. Zeiträume

Ein Zeitraum legt eine Quote für eine bestimmte Phase fest und kann individuell benannt werden. Zeiträume überschreiben die Basisquote. Außerdem bestimmt die Reihenfolge der Zeiträume, welche Quote bei überschneidenden Zeiträumen verwendet wird. Der oberste Zeitraum hat hierbei Vorrang.

1. Klicke auf *Zeitraum hinzufügen*{:.doc-button}.
2. Füge einen **Titel** hinzu (z.B. Weihnachten).
3. Wähle das **Start- und Enddatum** aus.
4. Gib den **Wert für die Quote** ein.
5. Setze die Option für die Anwendung der wöchentlichen Modifikatoren (wenn gewünscht).
6. Klicke auf *Quote speichern*{:.doc-button}.

> Hinweis
>
> Du kannst die Zeiträume per Drag & Drop neu anordnen. Um Zeiträume zu löschen, klicke auf das Symbol mit dem Papierkorb.

### 5. Wochentags-Modifikatoren

Ein Modifikator ist ein Prozentsatz. Dieser wird auf die finale Quote angewendet. Gib bei Bedarf auf der rechten Seite für jeden Wochentag einen Modifikator an. Dadurch wird die Quote um den eingegebenen Prozentwert erhöht oder verringert.

Ein Wert von 100% hat keine Auswirkung auf die Quote, während ein Wert von 120% die Quote um 20% erhöht. Als Beispiel legen wir eine **Basisquote** mit einem Vollzeitäquivalent (FTE) von 1 fest. Ein Modifikator von 120% am Montag führt zur Erhöhung der Quote auf 1,2 FTE; ein Modifikator von 80% reduziert die Quote auf 0,8 FTE.

## 6. Quotenkalender

Im unteren Teil zeigt ein Kalender die resultierende Quote für jeden Tag. Die Farbcodierung zeigt Anpassungen der **Wochentags-Modifikatoren** und der hinzugefügten **Zeiträume**. Klicke auf einen Tag, um den genauen Wert anzuzeigen. Die Tagesquoten werden oben rechts über dem Kalender angezeigt.

Klicke auf die Icons in der Abbildung, um mehr über die Felder zu erfahren:  

<iframe width="960" height="651" data-original-width="2242" data-original-height="1520" src="https://www.thinglink.com/card/1369603813740118018" type="text/html" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen scrolling="no"></iframe><script async src="https://cdn.thinglink.me/jse/responsive.js"></script>

Klick auf *Quote speichern*{:.doc-button}, wenn Du zufrieden mit Deinen Einstellungen bist.
