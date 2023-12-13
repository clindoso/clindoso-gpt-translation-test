---
title: Aktivitäten erstellen
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
beta-feature: false
description: Erstelle Aktivitäten, um geplante und ungeplante Tätigkeiten in deinem Unternehmen abzubilden.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

Um Aktivitäten zu erstellen, zu bearbeiten und zu löschen, gehe zu _Plan > Konfiguration > Aktivitäten_{:.breadcrumbs}.

Über Aktivitäten werden alle Tätigkeiten abgebildet, die in deinem Unternehmen geplant werden und zu denen du Reports erstellst, z.&nbsp;B. Telefonie, Pausen, Abwesenheiten oder Meetings. Du kannst beliebig viele Aktivitäten erstellen. Die Anzahl der Aktivitäten hängt nur davon ab, zwischen wie vielen Tätigkeiten du unterscheiden und welchen Detailgrad du erreichen möchtest.

Aktivitäten sind ein wesentlicher Bestandteil der Schichtplanung mit injixo. Sie hängen mit anderen Konfigurationselementen zusammen, z.&nbsp;B. mit {% link_new Planungseinheiten | features/administration/create-and-manage-planning-units.md | #aktivitäten-hinzufügen %} und {% link_new Tagesmodellen | features/administration/daymodels/daymodel-basics.md %}. Sie sind auch Teil der Schichtpläne, die im {% link_new Schicht Center | features/scheduling/shiftcenter/add-and-delete-items.md %} oder in {% link_new Schedules | features/scheduling/schedules/schedules-edit.md %} verwaltet werden.

In injixo gibt es zwei vorkonfigurierte (nicht löschbare) Aktivitäten:

- Anwesend: Diese Aktivität wird als Platzhalteraktivität in Tagesmodellen verwendet. Bei der Schichtplanung ersetzt injixo diese Aktivität durch andere Aktivitäten, die als Planbar konfiguriert sind.
- Urlaub: Diese Aktivität wird verwendet, um bezahlten Urlaub basierend auf dem Urlaubsanspruch eines Mitarbeiters zu planen. Erstelle eine separate Aktivität für unbezahlte Abwesenheit.

## Aktivität erstellen

1. Klicke auf _Neue Aktivität_{:.doc-button}.
2. Gib die allgemeinen Informationen zu deiner Aktivität ein:
   - **Name**: Eindeutiger Name, der deine Aktivität beschreibt. Die Kurzbezeichnung wird automatisch erstellt.
   - **Typ**: Der Aktivitätstyp bestimmt, wie injixo Aktivitäten bei der Schichtplanung behandelt und wie diese im Reporting und in anderen Funktionalitäten angezeigt werden. Erfahre mehr über die verschiedenen {% link_new Aktivitätstypen | features/administration/activity-types-and-properties.md | #aktivitätstypen %}.
   - **Farbe**: Die Farbe wird im Schichtplan und bei anderen Konfigurationselementen angezeigt. Sie kann dir dabei helfen, verschiedene Aktivitäten auf einen Blick zu unterscheiden.
   - **Shortcut**: Optionales Tastaturkürzel, mit dem du die Aktivität schneller im Schicht Center einfügen kannst. Erfahre mehr über {% link_new Shortcuts | best-practices/tips-on-shift-center-usage.md | #tipp-2-shortcuts-für-die-schnelle-zuweisung-von-aktivitäten %}.
   - **Offizieller Name und Kurzbezeichnung**: Alternativer Name, der für internes Reporting und Integrationen verwendet werden kann. injixo Me zeigt immer den Namen an, der unter **Name** eingegeben wurde.
3. Aktiviere eine oder mehrere Checkboxen, um die {% link_new Eigenschaften der Aktivität | features/administration/activity-types-and-properties.md | #aktivitätseigenschaften %} zu konfigurieren.
  Wenn du die Eigenschaft Planbar auswählst, kannst du den {% link_new Stellenwert | best-practices/importance-for-activities.md %} bearbeiten.
  Wenn du die Eigenschaft Ersetzbar auswählst, kannst du den Wert für die {% link_new Priorität | best-practices/priority-for-activities.md %} bearbeiten.
4. (Optional) Weise der Aktivität {% link_new Qualifikationen | features/administration/work-with-skills.md | #aktivitäten-qualifikationen-zuweisen %} hinzu.
5. Klicke auf _Aktivität erstellen_{:.doc-button}.

Erfahre mehr über {% link_new Aktivitätstypen und -eigenschaften | features/administration/activity-types-and-properties.md %}.

### Aktivitätskennung

Um die Kennung einer Aktivität zu sehen, kannst du:

- in der **Aktivitäten**-Liste auf eine Aktivität klicken. Die URL in der Browserleiste zeigt die Kennung der ausgewählten Aktivität an (z.&nbsp;B. https://www.injixo.com/plan/configuration/activities/1234).
- die injixo-API verwenden. Erfahre, wie du [Aktivitäten mit der injixo-API verwalten](https://api.injixo.com/resources/activities/) kannst.

## Multiaktivitäten und Teilaktivitäten 

Mit Multiaktivitäten kannst du Personen mit mehreren Qualifikationen planen, wenn eine ihrer Qualifikationen benötigt wird. Du kannst eine Aktivität in eine Multiaktivität umwandeln, indem du ihr {% link_new andere Aktivitäten zuweist | features/administration/activity-types-and-properties.md | #teilaktivitäten %}. Die zugewiesenen Aktivitäten werden dann zu Teilaktivitäten. In der Aktivitätenliste sind Multiaktivitäten mit einem <em class="multiactivity-icon"></em> markiert.

Wenn du auf eine Aktivität klickst, die eine Teilaktivität ist, siehst du den Abschnitt **Multiaktivitäten**. Dort werden alle Multiaktivitäten angezeigt, denen die Aktivität zugewiesen ist.

Wenn du auf eine Aktivität klickst, die keine Teilaktivität ist, siehst du den Abschnitt **Teilaktivitäten**. Dort kannst du andere Aktivitäten auswählen, damit sie zu Teilaktivitäten der Aktivität werden, die du gerade bearbeitest. Die Aktivität selbst wird dadurch zu einer Multiaktivität.
Du kannst einer Aktivität erst dann Teilaktivitäten hinzufügen, nachdem du sie erstellt hast.

## Externe Systeme

<!-- will be made obsolete by the new activity mapping page. Will require a separate article -->

Du kannst Aktivitäten aus externen Systemen einer Aktivität in injixo zuordnen.

1. Wähle eine Aktivität aus der Liste aus, scrolle bis zum Abschnitt **Externe Systeme** und klicke auf _In WFM bearbeiten_{:.doc-button}.
2. Navigiere zum Abschnitt **Externe Systeme**.
3. Klicke auf das {% icon item-add %}.
4. Wähle ein **Externes System**, eine **Bezeichnung im externen System** und eine **Klassifikation** aus den Dropdown-Menüs aus.
5. Klicke auf _OK_{:.doc-button}.

> Du kannst eine Aktivität aus einem externen System nur einmal zu einer Einzelaktivität in injixo hinzufügen.

## Aktivität kopieren

Um eine neue Aktivität mit denselben allgemeinen Eigenschaften wie eine bestehende Aktivität zu erstellen, gehe wie folgt vor:

1. Klicke in der **Aktivitäten**-Liste auf eine Aktivität.
2. Klicke unter dem Namen der Aktivität auf **Aktivität kopieren**.  
   Ein Fenster **Neue Aktivität erstellen** mit bereits ausgewählten Checkboxen öffnet sich. Zugewiesene Qualifikationen und Teilaktivitäten werden nicht kopiert.
3. Gib einen **Namen** für die neue Aktivität ein.
4. (Optional) Ändere die Farbe und andere Eigenschaften.
5. Klicke auf _Aktivität erstellen_{:.doc-button}.

## Aktivität bearbeiten oder löschen

1. Klicke in der **Aktivitäten**-Liste auf eine Aktivität.

- Um die Aktivität zu bearbeiten, passe die Informationen an, die du ändern möchtest und klicke auf _Änderungen speichern_{:.doc-button}.
- Um die Aktivität zu löschen, klicke unten rechts auf _Aktivität löschen_{:.doc-button}.

Wenn die gelöschte Aktivität anderen Konfigurationselementen zugewiesen war (z.&nbsp;B. Planungseinheiten oder Tagesmodelle), wird der Name der Aktivität bei diesen Elementen kursiv angezeigt. Eine gelöschte Aktivität verliert ihre Zuweisungen zu anderen Konfigurationselementen, bleibt jedoch in den Konfigurationsdaten sichtbar. Möglicherweise musst du bestehende Tagesmodelle neu erstellen, wenn diese die gelöschte Aktivität enthalten.

Im Schicht Center werden gelöschte Aktivitäten als {% link_new Balken mit einer gestrichelten Umrandung | features/scheduling/shiftcenter/shift-center-overview.md | #wie-werden-elemente-angezeigt %} angezeigt. In Schedules werden gelöschte Aktivitäten in grau und ohne den Namen angezeigt. Die ursprünglichen Zeitinformationen bleiben mit Ausnahme der Tagesansicht weiterhin sichtbar.
