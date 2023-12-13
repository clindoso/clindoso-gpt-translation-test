---
title: Planungsmodelle
redirect_from:
  - /de/work-time-pattern-models/
product_label:
  - advanced
  - enterprise
  - classic
description: Nutze Planungsmodelle, um Startzeit-Korridore und wöchentliche Rotationen für vollständig optimierte Schichtpläne zu erstellen.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/reference-date.md
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

Benötigst Du Hilfe bei der Erstellung vollständig optimierter Schichtpläne mit wöchentlichen Rotationen oder einer gerechteren Verteilung von Spät- und Nachtschichten oder freien Tagen?

Ohne Einschränkungen steht es der volloptimierten Planung (AutoScheduler) frei, jedes Tagesmodell zuzuweisen, das der Planungseinheit zugeordnet ist und dem Vertrag des Mitarbeiters entspricht. Planungsmodelle stellen sicher, dass die Mitarbeiter nicht einfach zufällige Schichten erhalten.

Planungsmodelle sind so aufgebaut, dass sie aus einem oder mehreren Wochenmodellen bestehen. Wochenmodelle wiederum enthalten mindestens ein Tagesmodell.

## Wochenmodelle

Wochenmodelle gruppieren Schichten nach Startzeit, Schichtdauer, Aktivitäten oder was immer Du Dir vorstellen kannst. Typische Beispiele sind:

 - Früh-, Mittel-, Spät- und Nachtschichten. Für Fairness durch wechselnde Nachtschichten oder andere unbeliebte Schichten.
 - Schichten gruppiert nach Schichtdauer. Um wechselnd mehr oder weniger Stunden in einer Woche zu planen.
 - Schichten mit unterschiedlichen Aktivitäten. Um verschiedene Aktivitäten wechselweise zu planen oder besser zu verteilen.

Wochenmodelle werden den Planungsmodellen zugeordnet.

### Erstellen eines Wochenmodells

{{ 4 | image: 'Dialog zum Erstellen eines Wochenmodells', '50%' }}

Erstelle Wochenmodelle in *WFM > Administration > Scheduling > Wochenmodelle*{:.breadcrumbs}.

1. Klicke auf das grüne *+*{:.doc-button} in der Aktionsleiste.
2. Vergib einen **Namen**.
3. Vergib eine **Kurzbezeichnung**.
4. Wähle eine **Farbe**.
5. Gib die **Maximale Anzahl von [Ausnahmetagen](#ausnahmetage) pro Woche** ein, falls erforderlich.
6. Klicke *OK*{:.doc-button}.

Füge anschließend ein oder mehrere Tagesmodelle hinzu.

### Hinzufügen von Tagesmodellen zu einem Wochenmodell

1. Klicke auf das grüne *+*{:.doc-button} in der Kategorie Tagesmodelle des Wochenmodells.
2. Wähle ein oder mehrere **Tagesmodelle** aus der Liste.
3. Klicke *OK*{:.doc-button}.

Wochenmodelle erlauben die Verwendung von {% link_new zeitlich fixierten | features/administration/daymodels/daymodel-creation.md | #zeitlich-fixierte-schicht %} und {% link_new variablen | features/administration/daymodels/daymodel-creation.md | #variable-schicht %} Tagesmodellen. Verwende aber, wann immer möglich, variable Tagesmodelle. Dadurch wird der Aufwand für die Verwaltung Deiner Tagesmodelle minimiert.

> Tipps  
> - Die volloptimierte Planung (AutoScheduler) plant nur Tagesmodelle, die der Planungseinheit zugeordnet sind. Wenn Du die Tagesmodelle der Planungseinheit eingeschränkt hast, werden u.U. nicht alle Mitarbeiter mit dem Planungsmodell geplant.
> - Die volloptimierte Planung (AutoScheduler) ersetzt innerhalb von Tagesmodellen ersetzbare durch planbare Aktivitäten. Hinterlege, wenn möglich, nicht jede Aktivität einzeln in Deinen Tagesmodellen, sondern verwende die Systemaktivität *Anwesend* (ID 1) als Basisaktivität.

## Planungsmodelle

Jedes Planungsmodell ist eine Sammlung von einem oder mehreren Wochenmodellen. Über das Planungsmodell definierst Du außerdem Regeln für die Abfolge der Wochenmodelle und für die Startzeit der Schichten.

<!-- correct setting text -->
Nutze *48402*{:.id-label} *Berücksichtigung von Mitarbeitern mit Planungsmodellen*, um nur Mitarbeiter mit einem zugewiesenen Planungsmodell zu planen. Standardmäßig plant die volloptimierte Planung (AutoScheduler) Mitarbeiter unabhängig von der Zuordnung eines Planungsmodells. Ist die Einstellung aktiv, müssen alle Mitarbeiter ein Planungsmodell haben.

### Erstellen von Planungsmodellen

{{ 5 | image: 'Anlegen eines Planungsmodells', '50%' }}

Erstelle Planungsmodelle in *WFM > Administration > Scheduling > Planungsmodelle*{:.breadcrumbs}:

1. Klicke auf das grüne *+*{:.doc-button} in der Aktionsleiste.
2. Vergib einen **Namen**.
3. Vergib eine **Kurzbezeichnung**.
4. Wähle eine **Farbe**.
5. Definiere einen [Typ](#vier-verschiedene-typen).
6. Wähle das **Wochenmodell** für [Ausnahmetage](#ausnahmetage), falls notwendig.
7. Klicke *OK*{:.doc-button}.

Füge anschließend ein oder mehrere Wochenmodelle hinzu.

### Hinzufügen eines Wochenmodells zu einem Planungsmodell

<!-- screenshot? -->

1. Klicke auf *+*{:.doc-button} in der Unterkategorie Wochenmodelle innerhalb des Planungsmodells.
2. Wähle ein **Wochenmodell**.
3. Setze eine **Position**.
4. Klicke *OK*{:.doc-button}.

#### Position

Ändere die Reihenfolge der Wochenmodelle mithilfe der blauen Pfeile ↑ ↓. Das Verschieben nach oben und unten spielt eine wichtige Rolle für die Planungsmodelle Typ B (starre Rotation) und D (Kombi-Rotation). Diese beiden Typen befolgen strikt die Reihenfolge der Wochenmodelle bei der Auswahl von Tagesmodellen.

### Vier verschiedene Typen

Typ     | Name                            | Beschreibung
------- | ------------------------------- | --------------------------------------------------------------------------------------------
A       | Flexible Auswahl                | Typ A erlaubt jedes Tagesmodell aus allen zugewiesenen Wochenmodellen für jeden Tag in jeder Woche. Ein Mitarbeiter kann am Montag früh, am Dienstag nachts und am Mittwoch spät arbeiten, usw. <sup>1</sup>
B       | Starre Rotation                  | Typ B verwendet die Abfolge der Wochenmodelle. <sup>2</sup> Ein Mitarbeiter erhält das gleiche Tagesmodell für die gesamte Woche, z. B. ab 9 Uhr von Montag bis Freitag. Die Regel kann nur durch die Definition von Ausnahmetagen gebrochen werden.
C        | Variable Rotation              | Typ C ignoriert die Abfolge der Wochenmodelle. <sup>2</sup> Schichten müssen während einer Woche die gleiche Startzeit haben. Die Rotation startet neu, wenn jedes Wochenmodell verwendet wurde.
D        | Kombi-Rotation (A/B) | Typ D verwendet die Abfolge der Wochenmodelle. <sup>2</sup> und kombiniert Typ A und B. Die Schichten können während der Woche unterschiedliche Startzeiten haben.

<sup>1</sup> Füge Einschränkungen bei Verfügbarkeiten oder Verträgen hinzu, damit der Schichtplan für die Mitarbeiter angemessen bleibt.  
<sup>2</sup> Abfolge der Wochenmodelle: Verwendung des ersten Wochenmodells für Woche 1, des zweiten für Woche 2, usw. Woche 1 wird durch das {% link_new Referenzdatum | features/administration/reference-date.md %} definiert, das Du bei der Zuordnung des Planungsmodells zum Mitarbeiter festlegst.

Dein Planungsmodell kann ein oder mehrere Wochenmodelle enthalten. Wähle Typ A oder D für flexible Startzeiten und Typ B oder C für feste Startzeiten.

Das Planungsmodell im folgenden Beispiel enthält vier Wochenmodelle mit jeweils drei Tagesmodellen, die durch unterschiedliche Farben gekennzeichnet sind.

{{ 1 | image: 'Beispiel für unterschiedliche Typen' }}

## Ausnahmetage

Ausnahmetage erlauben es, die Regeln zu brechen, die der [Typ des Planungsmodells](#vier-verschiedene-typen) definiert.

Ein Anwendungsbeispiel könnte ein Muster mit zwei Spät- oder einer Nachtschicht pro Woche sein.

Mit Ausnahmetagen arbeiten:

1. Erstelle ein separates Wochenmodell. Es enthält die als Ausnahmen zu verwendenden Tagesmodelle.
2. Definiere in einem oder mehreren der anderen Wochenmodellen die Anzahl der zulässigen Ausnahmen pro Woche.
3. Wähle das Wochenmodell mit den Ausnahmen in einem Planungsmodell aus.

Die volloptimierte Planung (AutoScheduler) plant nur eine Woche unter Verwendung der verfügbaren Tagesmodelle, ohne diejenigen für die Ausnahmetage. Stelle sicher, dass die normalen Tagesmodelle in die Arbeitswoche passen, die {% link_new im Vertrag definiert ist | features/administration/create-contracts.md %}. Wenn die Konfiguration mit dem Vertrag zusammenpasst, darf die Optimierung ein gewöhnliches Tagesmodell gegen eines für Ausnahmetage austauschen, wenn dies eine bessere Deckung bedeutet.

### Einem Mitarbeiter ein Planungsmodell zuweisen

{{ 2 | image: 'Mitarbeiter ein Planungsmodell zuweisen', '50%' }}

Weise Mitarbeitern ein Planungsmodell in *WFM > Administration > Scheduling > Mitarbeiter*{:.breadcrumbs} zu.

1. Wähle einen **Mitarbeiter**.
2. Klicke *+*{:.doc-button} in der Unterkategorie Planungsmodelle.
3. Wähle ein **Planungsmodell**.
4. Setze ein {% link_new Referenzdatum | features/administration/reference-date.md %}. Wähle hierbei immer den ersten Tag der Woche.
5. Klicke *Ok*{:.doc-button}.

Verwende die Massenbearbeitung, um ein Planungsmodell mehreren Mitarbeitern gleichzeitig zuzuweisen. Verwende nicht den gleichen Montag als Referenzdatum für alle Mitarbeiter, falls Du eine fixe Rotation (Typ B) verwendest.
 <!-- only B or also C ? -->  

## Zusammenfassung: Drei Schritte, um Rotationen zu definieren

1. **Erstelle ein Wochenmodell**.
   - Füge Tagesmodelle hinzu (vorher separat erstellt).
   - Definiere die Anzahl von [Ausnahmetagen](#ausnahmetage).
2. **Erstelle ein Planungsmodell**.
   - Wähle einen [Typ](#vier-verschiedene-typen).
   - Wähle bei Bedarf ein Wochenmodell für Ausnahmetage aus.
   - Füge ein oder mehrere Wochenmodelle hinzu.
   - Passe die Position der Wochenmodelle an (falls notwendig).
3. **Füge das Planungsmodell einem Mitarbeiter hinzu**.
   - Setze ein Referenzdatum.

## Beispiele

Hier sind einige Beispiele für die Verwendung von Planungsmodellen. Planungsmodelle sind ziemlich mächtig und es sind viele Konfigurationen möglich, daher ist eine gute Planung vorab entscheidend.  
Verträge und Tagesmodelle sowie die Zuordnungen von Tagesmodellen zu Planungseinheiten müssen korrekt sein, ebenso wie die Konfiguration des Planungsmodells und der Wochenmodelle selbst.

### Fixe Rotation mit Früh-, Mittel- und Spätschichten

Nutze ein Planungsmodell vom Typ B (starre Rotation) und weise diesem drei verschiedene Wochenmodelle zu:

* Wochenmodell 1 (Position 1) enthält Frühschichten.
* Wochenmodell 2 (Position 2) enthält Mittelschichten.
* Wochenmodell 3 (Position 3) enthält Spätschichten.

Die Position gibt die Reihenfolge des Wochenmodells im Planungsmodell an.

Ordne dieses Planungsmodell Deinen Mitarbeitern zu, indem Du ein {% link_new Referenzdatum | features/administration/reference-date.md %} festlegst.

### Ausnahmetage für Nachtschichten

<!-- type suggestions missing, maybe it doesn't matter -->

Ein Planungsmodell hat drei verschiedene Wochenmodelle mit

* Tagesmodellen für Frühschichten
* Tagesmodellen für Spätschichten
* Tagesmodellen für Nachtschichten (dies ist das Wochenmodell für Ausnahmetage)

Du möchtest, dass jeder Mitarbeiter zwischen der Frühschicht in der ersten Woche und der Spätschicht in der folgenden Woche wechselt.  
Wenn Du für jede Woche maximal 2 Ausnahmetage festlegst und ein Mitarbeiterbedarf für Nachtschichten besteht, kann jeder Mitarbeiter, der dieses Planungsmodell hat, eine Nachtschicht für maximal zwei Tage (Nächte) pro Woche erhalten.
