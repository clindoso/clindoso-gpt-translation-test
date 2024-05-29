---
title: Planungsmodelle erstellen
redirect_from:
  - de/wtpm_creating/
  - de/week_time_patterns/
  - de/wtpm_overview.md/
  - de/understanding_wtpms/
product_label:
  - advanced
  - enterprise
  - classic
description: Verwende Planungsmodelle in deiner Schichtplanoptimierung, um sicherzustellen, dass deinen Mitarbeitern keine willkürlichen Schichten zugeteilt werden.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-optimization.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-contracts.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/scheduling-split-shifts.md
---

Ein Planungsmodell besteht aus [Wochenmodellen](#wochenmodelle-erstellen) und legt fest, wie deinen Mitarbeitern {% link_new Tagesmodelle | features/administration/daymodels/daymodel-basics.md %} zugewiesen werden.

Die folgende Grafik zeigt, wie Tagesmodelle und Wochenmodelle in einem Planungsmodell zusammenspielen.

{{ 1 | image: 'Aufbau eines Planungsmodells' }}

Mit Planungsmodellen kannst du wiederkehrende Schichtmuster anlegen und Einschränkungen für die Funktionalität **Optimierten Plan erstellen** festlegen.<br>
Planungsmodelle bieten folgende Vorteile:

- Sie legen fest, welche Tagesmodelle verwendet werden können, um einen Mitarbeiter zu planen.
- Mitarbeiter erhalten keine willkürlichen Schichtkombinationen.
- Sie legen Startzeiten für Schichten fest.
- Sie legen eine Reihenfolge fest, in der Tagesmodelle zugewiesen werden.

Als Alternative zu Planungsmodellen kannst du Schichtfolgen verwenden oder {% link_new Verfügbarkeiten | features/administration/availabilities.md %} für deine Mitarbeiter konfigurieren.

## Voraussetzungen

Um Planungsmodelle verwenden zu können, stelle sicher, dass folgendes zutrifft:

- Du hast {% link_new Tagesmodelle | features/administration/daymodels/daymodel-creation.md %} und [Wochenmodelle](#wochenmodelle-erstellen) erstellt und den Wochenmodellen Tagesmodelle zugewiesen.
- Planungsmodelle bestehen immer aus einem oder mehreren Wochenmodellen.
- Wochenmodelle enthalten immer mindestens ein {% link_new Tagesmodell | features/administration/daymodels/daymodel-basics.md %}.
- Du hast deinen Mitarbeitern Planungsmodelle zugewiesen.

## Wochenmodelle erstellen

Ein Wochenmodell ist eine Gruppe von Tagesmodellen. Du kannst Tagesmodelle nach beliebigen Kriterien gruppieren, z.&nbsp;B. Schichtlänge, geplante Aktivitäten, Startzeit usw.<br>

Du kannst Wochenmodelle nur innerhalb von Planungsmodellen verwenden. Für eine Arbeitswoche plant injixo Mitarbeiter entsprechend der im Wochenmodell enthaltenen Tagesmodelle. So kannst du dafür sorgen, dass deine Mitarbeiter gerechtere und möglichst gleichbleibende Arbeitszeiten haben.

Um ein Wochenmodell zu erstellen, gehe wie folgt vor:

1. Gehe zu _Plan > Konfiguration > Wochenmodelle_{:.breadcrumbs}.
2. Klicke oben links auf das Neu-Icon {% icon item-add | icon-only %}.
   Ein Konfigurationsfenster öffnet sich auf der rechten Seite.
3. Konfiguriere das Wochenmodell:<br>
   **Name**: Gib einen eindeutigen Namen ein (max. 50 Zeichen).<br>
   **Kurzbezeichnung**: Gib den Namen oder eine Kurzversion davon ein (max. 25 Zeichen).<br>
   **Farbe**: Die Farbe kann dir dabei helfen, das Wochenmodell in einer Liste zu identifizieren.<br>
   **Maximale Anzahl von Ausnahmetagen pro Woche**: [Ausnahmetage](#ausnahmetage) erlauben injixo, von den Vorgaben des Wochenmodells abzuweichen, um den Mitarbeiterbedarf besser decken zu können.
4. Klicke auf _OK_{:.doc-button}.

Du kannst deinem Wochenmodell jetzt Tagesmodelle hinzufügen.

### Tagesmodelle zu einem Wochenmodell hinzufügen

1. Gehe im Konfigurationsfenster des Wochenmodells zum Abschnitt **Tagesmodelle** und klicke auf das Hinzufügen-Icon {% icon item-add | icon-only %}.
2. Wähle ein oder mehrere Tagesmodelle aus der Liste.
3. Klicke auf _OK_{:.doc-button}.

Du kannst einem Wochenmodell sowohl {% link_new fixe als auch variable Tagesmodelle | features/administration/daymodels/daymodel-basics.md | #tagesmodelltypen %} hinzufügen. Wenn du variable Tagesmodelle verwendest, kann die Funktionalität **Optimierten Plan erstellen** die optimale Startzeit von Schichten innerhalb der Vorgaben des Tagesmodells festlegen.

> Hinweis
>
> injixo kann nur die Tagesmodelle planen, die der Planungseinheit zugewiesen sind, der der Mitarbeiter zugewiesen ist. Wenn du die {% link_new Zuweisung der Tagesmodelle zu deiner Planungseinheit eingeschränkt | features/administration/create-and-manage-planning-units.md | #tagesmodelle-einschränken %} hast, kann es sein, dass Tagesmodelle, die du aufgrund deines Planungsmodells erwartest, nicht verwendet werden.
>
> injixo kann ersetzbare Aktivitäten innerhalb einer Schicht mit planbaren Aktivitäten ersetzen. Damit dies funktioniert, verwende variable Tagesmodelle für jede laut Vertrag vorgegebene Schichtdauer und verwende die Systemaktivität Anwesend (ID: 1) als {% link_new Basisaktivität | features/administration/daymodels/daymodel-basics.md | #basisaktivität-und-schichtdauer %}. Lege nicht für jede einzelne Aktivität ein Tagesmodell an.

## Planungsmodelle erstellen

1. Gehe zu _Plan > Konfiguration > Planungsmodelle_{:.breadcrumbs}.
2. Klicke oben links auf das Neu-Icon {% icon item-add | icon-only %}.
3. Konfiguriere das Planungsmodell:<br>
   **Name**: Gib einen eindeutigen Namen ein (max. 50 Zeichen).<br>
   **Kurzbezeichnung**: Gib den Namen oder eine Kurzversion davon ein (max. 25 Zeichen).<br>
   **Farbe**: Die Farbe kann dir dabei helfen, das Planungsmodell in einer Liste zu identifizieren.<br>
   **Typ**: Der [Typ](#planungsmodelltypen) legt fest, wie injixo das Planungsmodell verwendet.<br>
   **Wochenmodell für Ausnahmetage**: Wähle das Wochenmodell, das für [Ausnahmetage](#ausnahmetage) geplant werden soll.
4. Klicke auf _OK_{:.doc-button}.

Du kannst deinem Planungsmodell jetzt Wochenmodelle hinzufügen.

### Wochenmodelle zu einem Planungsmodell hinzufügen

1. Klicke im Konfigurationsdialog des Planungsmodells im Abschnitt **Wochenmodelle** auf das Hinzufügen-Icon {% icon item-add | icon-only %}.
2. Wähle ein Wochenmodell aus der Liste aus.
3. Setze eine Position.<br>
   Wenn du mehrere Wochenmodelle hinzufügst, klicke auf das {% icon down-arrow-blue %} und das {% icon up-arrow-blue %}, um die Position zu ändern.
4. Klicke auf _OK_{:.doc-button}.

### Position

Die Position der Wochenmodelle in Planungsmodellen spielt eine Rolle, wenn du Planungsmodelle vom [Typ&nbsp;B oder&nbsp;D](#planungsmodelltypen) verwendest. injixo weist die Wochenmodelle in der hier konfigurierten Reihenfolge zu.

Verwende das {% icon down-arrow-blue %} und das {% icon up-arrow-blue %}, um die Position der Wochenmodelle festzulegen.

## Planungsmodelltypen

| Typ | Name                 | Verwendung des Wochenmodells                                                                             | Zuweisung von Tagesmodellen                                                                            | Startzeit der Schicht                  | Auswirkung                                                                                                                                                                                                                                                                                                                          |
| --- | -------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A   | Flexible Auswahl     | injixo kann jedes Tagesmodell aus jedem enthaltenen Wochenmodell für jeden Tag in jeder Woche auswählen. | injixo kann jedes Tagesmodell aus jedem Wochenmodell verwenden.                                        | Flexibel                               | Je nach den Öffnungszeiten deines Unternehmens kann Typ&nbsp;A zu einer Schichtverteilung führen, die deine Mitarbeiter als willkürlich oder stressig empfinden. Es kann beispielsweise vorkommen, dass ein Mitarbeiter die Frühschicht am Montag, die Nachtschicht am Dienstag und die Abendschicht am Mittwoch zugeteilt bekommt. |
| B   | Starre Rotation      | injixo plant die Reihenfolge der Wochenmodelle entsprechend ihren Positionen.                            | injixo wählt für jede Woche das Tagesmodell aus, mit dem der Mitarbeiterbedarf am besten gedeckt wird. | Fix                                    | Jedem Mitarbeiter wird für die gesamte Woche das gleiche Tagesmodell zugewiesen, z.&nbsp;B. Start um 9&nbsp;Uhr von Montag bis Freitag. Lege [Ausnahmetage](#ausnahmetage) fest, wenn du ein anderes Tagesmodell verwenden möchtest. Starre Rotation sorgt von allen vier Typen für die konstanteste Schichtzuteilung.              |
| C   | Variable Rotation    | injixo hält sich nicht an die festgelegte Position der Wochenmodelle.                                    | injixo wählt ein Tagesmodell für die gesamte Woche aus.                                                | Fix                                    | Mitarbeiter können jedes Wochenmodell zugewiesen bekommen, um den Mitarbeiterbedarf bestmöglich zu decken. Da die Schichten immer zur selben Zeit beginnen, haben die Mitarbeiter im Lauf der Woche gleichbleibende Arbeitszeiten.                                                                                                  |
| D   | Kombi-Rotation (A/B) | injixo hält sich an die für die Wochenmodelle festgelegte Position.                                      | injixo wählt ein Tagesmodell für die gesamte Woche aus.                                                | Flexibel (innerhalb eines Zeitrahmens) | Je nach Mitarbeiterbedarf kann injixo Mitarbeiter für Frühschichten planen, die zwischen 8&nbsp;Uhr und 10&nbsp;Uhr beginnen. Mit Typ&nbsp;D kann injixo flexibler planen, um den Mitarbeiterbedarf zu decken. Gleichzeitig erhalten deine Mitarbeiter relativ konsistente Schichtpläne.                                            |

Die folgende Grafik stellt dar, wie sich die verschiedenen Planungsmodelltypen auf deinen Schichtplan auswirken. Dieses Beispiel zeigt ein Planungsmodell mit vier Wochenmodellen und drei Tagesmodellen je Wochenmodell.

{{ 2 | image: 'Beispiel-Schichtplan mit den verschiedenen Planungsmodelltypen' }}

## Ausnahmetage

Ausnahmetage erlauben injixo, von den Vorgaben des verwendeten [Planungsmodelltypen](#planungsmodelltypen) abzuweichen. Zum Beispiel könntest du Ausnahmetage verwenden, um eine Nachtschicht in einer Woche zu planen, in der der Mitarbeiter normalerweise in der Morgenschicht arbeitet.<br>

Ausnahmetage priorisieren den Mitarbeiterbedarf und sorgen für eine bessere Deckung. Allerdings führen sie zu weniger konsistenten Schichtplänen für deine Mitarbeiter.

Um Ausnahmetage zu planen, gehe wie folgt vor:

1. [Erstelle ein separates Wochenmodell](#wochenmodelle-erstellen) und füge ihm die Tagesmodelle hinzu, die du als Ausnahmen verwenden möchtest.
2. Lege im Konfigurationsdialog des Wochenmodells, das du für die Standardschicht verwenden möchtest, die Anzahl der Ausnahmetage pro Woche fest.
3. Wähle im Konfigurationsdialog des Planungsmodells das Wochenmodell aus, das du für die Ausnahmetage verwenden möchtest.

injixo kann dann bei der Auswahl von Tagesmodellen für die Woche keine Tagesmodelle verwenden, die für Ausnahmetage verwendet werden. Stelle sicher, dass alle für die Planung nötigen Stammdaten (d.&nbsp;h. alle verwendeten Tagesmodelle und alle Planungsmodelle) mit den im Vertrag des Mitarbeiters festgehaltenen {% link_new Arbeitszeitvorgaben | features/administration/create-contracts.md | #arbeitszeitvorgaben %} übereinstimmen. Wenn das für die Woche verwendete Tagesmodell mit dem Vertrag übereinstimmt, kann injixo das ursprüngliche Tagesmodell mit einem ersetzen, das für Ausnahmetage bestimmt wurde, um den Mitarbeiterbedarf besser zu decken.

## Mitarbeitern Planungsmodelle zuweisen

1. Gehe zu _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs}.
2. Wähle einen Mitarbeiter aus der Liste.
3. Klicke im Abschnitt **Planungsmodelle** auf das Hinzufügen-Icon {% icon item-add | icon-only %}.<br>
   Ein Konfigurationsfenster öffnet sich auf der rechten Seite.
4. Konfiguriere die Einstellungen:<br>
   **Gültig vom/Gültig bis**: Lege einen {% link_new Gültigkeitszeitraum | features/administration/set-a-validity-period.md %} fest.<br>
   **Planungsmodell**<br>
   **Referenzdatum**: Setze ein Referenzdatum, um das Startdatum für das Planungsmodell festzulegen.
5. Klicke auf _OK_{:.doc-button}.

Verwende die Funktionalität {% link_new Massenbearbeitung | features/administration/mass-update.md %}, um ein Planungsmodell mehreren Mitarbeitern gleichzeitig zuzuweisen.

> Vorsicht bei der Verwendung der Massenbearbeitung, wenn du Planungsmodelle vom Typ B zuweist
>
> Wenn du die Funktionalität Massenbearbeitung verwendest und für alle dasselbe Referenzdatum setzt, werden alle Mitarbeiter mit demselben Wochenmodell zur selben Zeit geplant.
>
> Wähle stattdessen kleinere Gruppen für die Massenbearbeitung aus und setze für sie aufeinanderfolgende Montage als Referenzdatum. Auf diese Weise beginnt jede Gruppe ihre Rotation in einer anderen Woche.

## Beispiele

### Beispiel A: Starre Rotation mit Früh- und Spätschichten

Konfiguriere ein Planungsmodell vom Typ&nbsp;B (starre Rotation) und weise diesem drei verschiedene Wochenmodelle zu. Denke daran, die Position für die Wochenmodelle festzulegen.

- Wochenmodell&nbsp;1 (Position&nbsp;1) enthält Tagesmodelle für Morgenschichten (Schichtbeginn zwischen 7&nbsp;Uhr und 9&nbsp;Uhr).
- Wochenmodell&nbsp;2 (Position&nbsp;2) enthält Tagesmodelle für Abendschichten (Schichtende um 23&nbsp;Uhr).
- Wochenmodell&nbsp;3 (Position&nbsp;3) enthält Tagesmodelle für Nachmittagsschichten (Schichtbeginn zwischen 11&nbsp;Uhr und Mittag).

Mit diesem Planungsmodell rotieren die Mitarbeiter konsistent zwischen einer Woche mit Morgenschichten, einer mit Abendschichten und einer mit Nachmittagsschichten.

Dies setzt ein gewisses Maß an Flexibilität voraus, aber die Mitarbeiter erhalten dafür im Wochenverlauf gleichbleibende Arbeitszeiten.

### Beispiel B: Ausnahmetage für Nachtschichten

Konfiguriere ein Planungsmodell mit drei verschiedenen Wochenmodellen. Konfiguriere maximal zwei Ausnahmetage pro Woche.

- Wochenmodell&nbsp;1 enthält Tagesmodelle für Morgenschichten.
- Wochenmodell&nbsp;2 enthält Tagesmodelle für Abendschichten.
- Wochenmodell&nbsp;3 enthält Tagesmodelle für Nachtschichten (wähle dieses im Dropdown-Menü **Wochenmodell für Ausnahmetage** aus).

Mit diesem Planungsmodell wechseln die Mitarbeiter zwischen Morgenschichten in der ersten Woche und Abendschichten in der zweiten Woche. Da du zwei Ausnahmetage festgelegt hast, kann es auch vorkommen, dass den Mitarbeitern bis zu zwei Nachtschichten pro Woche zugewiesen werden, wenn dies die beste Option ist, um den Mitarbeiterbedarf zu decken.
