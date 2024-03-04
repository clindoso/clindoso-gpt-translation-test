---
title: Auswahlen erstellen und verwalten
description: Erstelle Auswahlen und füge Mitarbeiter hinzu.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from: /de/selections-overview/
redirect_reason: renamed file in April 2022
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/filter-with-selections.md
---

Mit Auswahlen kannst du Mitarbeiter nach bestimmten Kriterien gruppieren und filtern. Auswahlen funktionieren ähnlich wie {% link_new Mitarbeiterfilter | features/administration/employee-filter.md %}. So unterscheiden sie sich voneinander:

- Bei Auswahlen kannst du die Kriterien für die Gruppierung selbst festlegen.
- Mitarbeiterfilter gruppieren auf Grundlage der Stammdaten wie z.&nbsp;B. Planungseinheit, Qualifikation und Vertrag.

Zudem sind Mitarbeiterfilter nur in injixo Classic, Advanced und Enterprise verfügbar.

Auswahlen werden häufig verwendet, um Mitarbeiter zu gruppieren, die:

- einem bestimmten Vorgesetzten unterstellt sind.
- von zu Hause aus arbeiten.
- vor kurzem eingestellt wurden und zusätzliche Unterstützung oder Beaufsichtigung benötigen.
- kurzfristig für andere Mitarbeiter einspringen können.
- zusätzliche Verpflichtungen haben, die nicht planungsrelevant aber trotzdem wichtig sein können, z.&nbsp;B. Teilnahme an einem Erste-Hilfe-Training.

Wenn du injixo Essential verwendest, kannst du mit Auswahlen Mitarbeiter auf Grundlage von Stammdaten gruppieren, z.&nbsp;B. Planungseinheit, Qualifikation und Vertrag.

## Auswahlen erstellen

1. Gehe zu _Plan > Konfiguration > Auswahl_{:.breadcrumbs}.
2. Klicke oben links auf das {% icon item-add %}.  
    Ein Konfigurationsfenster öffnet sich auf der rechten Seite.
3. Fülle folgende Felder aus:
    - **Name**: Eindeutiger Name für die Auswahl (max. 50 Zeichen).
    - **Kurzbezeichnung**: Kurzbezeichnung für den Namen (max. 25 Zeichen).
    - **Beschreibung**: Optionale Beschreibung, damit andere Benutzer verstehen, was die Auswahl umfasst.
4. Klicke auf _OK_{:.doc-button}.

## Mitarbeiter zur Auswahl hinzufügen

Damit du Mitarbeiter zu einer Auswahl hinzufügen kannst, musst du zuerst {% link_new eine Auswahl erstellen | features/administration/selections.md | #auswahlen-erstellen %}.

1. Gehe zu _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs}.
2. Klicke auf den Mitarbeiter, den du zu einer Auswahl hinzufügen möchtest.  
   Ein Konfigurationsfenster öffnet sich auf der rechten Seite.
3. Klicke im Abschnitt **Auswahl** auf das {% icon item-add %}.
4. Fülle folgende Felder aus:  
   - **Auswahl**: Klicke auf die Auswahl, zu der du den Mitarbeiter hinzufügen möchtest.
   - (Optional) **Gültig vom/Gültig bis**: Datumsbereich, um den Gültigkeitszeitraum für die Auswahl einzuschränken. Wenn du diese Felder leer lässt, ist die Auswahl immer gültig. Erfahre mehr über {% link_new Gültigkeitszeiträume | features/administration/set-a-validity-period.md %}.
5. Klicke auf _OK_{:.doc-button}.

Um eine Auswahl zu bearbeiten, der ein Mitarbeiter zugewiesen ist, klicke auf das {% icon item-edit %}. Um die Zuweisung zu der Auswahl zu entfernen, klicke auf das {% icon item-delete %}.

## Mitarbeiter in einer Auswahl verwalten

In _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs} erhältst du einen Überblick darüber, welche Mitarbeiter einer Auswahl zugewiesen sind und kannst auf ihre Einstellungen zugreifen.

Mit den folgenden Dropdown-Menüs kannst du die Mitarbeiter in einer Auswahl filtern:

- **Planungseinheit**: Wähle die Option [Alle] aus.
- **Auswahl**: Wähle eine Auswahl aus.  
   Wenn das Dropdown-Menü **Auswahl** nicht angezeigt wird, klicke in der Aktionsleiste auf das Icon **Standardfilter aktivieren**{% icon selection | icon-only %}.

injixo zeigt alle Mitarbeiter in der Auswahl an. Um auf die Einstellungen eines Mitarbeiters zuzugreifen, klicke auf dessen Zeile in der Liste.

## Auswahlen einander zuweisen

In injixo Classic, Advanced und Enterprise kannst du einer bestehenden Auswahl weitere Auswahlen zuweisen. Die Auswahl, der andere Auswahlen zugewiesen werden, wird zur übergeordneten Auswahl. Die zugewiesenen Auswahlen sind die untergeordneten Auswahlen. Über die übergeordnete Auswahl kannst du gleichzeitig auch alle Mitarbeiter filtern, die einer der untergeordneten Auswahlen zugewiesen sind.

Um eine Hierarchie zwischen einer übergeordneten und mehreren untergeordneten Auswahlen zu erstellen, {% link_new erstelle zunächst die über- und untergeordneten Auswahlen | features/administration/selections.md | #auswahlen-erstellen %}.

Um eine Auswahl einer anderen Auswahl zuzuweisen, gehe wie folgt vor:

1. Gehe zu _Plan > Konfiguration > Auswahl_{:.breadcrumbs}.
2. Klicke in der Auswahlliste auf die Auswahl, die du als übergeordnete Auswahl verwenden möchtest.  
   Ein Konfigurationsfenster öffnet sich auf der rechten Seite.
3. Klicke im Abschnitt **Auswahl** auf das {% icon item-add %}.
4. Fülle folgende Felder aus:  
   - **Auswahlen**: Klicke auf die Auswahl, die du als untergeordnete Auswahl hinzufügen möchtest.
   - (Optional) **Gültig vom/Gültig bis**: Datumsbereich, um den Zeitraum einzuschränken, in dem die untergeordneten Auswahlen der übergeordneten Auswahl zugewiesen sind. Wenn du diese Felder leer lässt, ist die Zuweisung immer gültig.
5. Klicke auf _OK_{:.doc-button}.

Um eine untergeordnete Auswahl zu bearbeiten oder zu entfernen, klicke auf das {% icon item-edit %} oder das {% icon item-delete %}.

> Hierarchie der Auswahlen
>
> Die Hierarchie der übergeordneten und untergeordneten Auswahlen ist in _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs} nicht sichtbar. Um zu überprüfen, ob eine Auswahl eine übergeordnete Auswahl ist, gehe zu _Plan > Konfiguration > Auswahl_{:.breadcrumbs} und klicke im Abschnitt **Auswahl** auf eine Auswahl. Alternativ kannst du für die übergeordneten Auswahlen entsprechende Namen vergeben, um die Hierarchie auf einen Blick deutlich zu machen.

## Auswahl löschen

1. Gehe zu _Plan > Konfiguration > Auswahl_{:.breadcrumbs}.
2. Klicke auf die Auswahl, die du löschen möchtest.
3. Klicke oben links auf das {% icon item-delete %}.
4. Um zu bestätigen, klicke auf _Ja_{:.doc-button}.
