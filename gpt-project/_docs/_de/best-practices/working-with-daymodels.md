---
title: Passende Schichten für Deine Verträge
---

## Szenario

Du möchtest Schichten in injixo anlegen, die zu den Verträgen Deiner Vollzeit- und Teilzeit-Mitarbeiter passen, damit genügend Mitarbeiter zur richtigen Zeit verfügbar sind?

Dabei hast Du unterschiedliche Verträge, wie zum Beispiel:

  - 40 Stunden (5 x 8h)
  - 32 Stunden (4 x 8h)
  - 30 Stunden (5 x 6h)
  - 24 Stunden (4 x 6h)
  - 20 Stunden (5 x 4h)
  - 12 Stunden (3 x 4h oder 2 x 6h)

In unserem Beispiel ist Dein Contact Center zwischen 07:00-19:00 Uhr geöffnet. Für Dein Anrufaufkommen gehen wir von einer Verteilung mit zwei Spitzen im Vormittags- und Nachmittagsbereich aus.

> Hinweis
>
> Pausen haben wir der Einfachheit halber aus diesem Beispiel ausgeklammert. Beim Anlegen von Tagesmodellen sind diese natürlich zu beachten und müssen entsprechend zur Brutto-Arbeitszeit hinzugefügt werden. So erhöht eine unbezahlte 30 Minuten Pause pro Tag die Brutto-Arbeitszeit für einen Vollzeit-Mitarbeiter auf 8,5 Stunden.

## Abbildung in injixo

Schichten werden in injixo über {% link_new Tagesmodelle | features/administration/daymodels/daymodel-creation.md %} abgebildet. Du kannst so pro {% link_new Vertrag | features/administration/create-contracts.md %} die möglichen Schichten für Deine Planung definieren. Tagesmodelle werden {% link_new Planungseinheiten | features/administration/create-and-manage-planning-units.md %} zugeordnet. In {% link_new Wochen- und Planungsmodellen | features/administration/work-time-pattern-models.md %} lassen sich Schichtmodelle wie Früh-, Mittel-, Spät-Rotationen für die {% link_new volloptimierte Planung | features/scheduling/scheduling-optimization.md %} abbilden. Ein anderer Ansatz für feste Rotationen sind {% link_new Schichtfolgen | features/administration/shift-sequences.md  %}).

## Empfohlener Ansatz

Als Ausgangsbasis musst Du nur wissen, welche Verträge Deine Mitarbeiter haben, dann beginne die Planung Deiner Tagesmodelle:

1.  Führe identische, tägliche Arbeitszeiten in einem Tagesmodell zusammen. Die Anzahl der Arbeitstage und die Wochenstunden werden über den Vertrag des einzelnen Mitarbeiters festgelegt.<br><br>

    So erfordern die 12h-, 24h- und 30h-Verträge theoretisch also nur ein 6 Stunden Tagesmodell, wenn die tägliche Arbeitszeit über die Woche gleich ist und die Tagesmodelle alle die gleichen Aktivitäten enthalten.<br><br>

    In der Realität sind Verträge oft flexibler. Mitarbeitern können täglich unterschiedliche Schichten, z.B. zwischen 6 und 8 Stunden erhalten, um das vertraglich definierte Wochensoll von beispielsweise 37,5 Stunden zu erreichen. So sind je nach gewünschter Flexibilität mehrere Tagesmodelle (auch pro Vertrag) notwendig.<br><br>

    Fest hinterlegte Sonderaufgaben innerhalb einer Schicht erfordern eventuell ein eigenes Tagesmodell, obwohl die tägliche Arbeitszeit mit anderen Verträgen übereinstimmt.

2. Definiere für alle Deine Tagesmodelle:
    - Brutto-Arbeitszeit
    - Pausenanzahl, -zeiten und -länge
    - Basisaktivität und ggf. feste Sonderaufgaben

3. Lege fest, ob und in welchem Rahmen Mitarbeiter flexible Start- und Endzeiten haben.

    In den Randzeiten benötigst Du häufig weniger Mitarbeiter. Durch variable Tagesmodelle mit unterschiedlichen Startzeiten wird Deine Planung flexibler.

    Nutze kurze Teilzeitschichten zur Abdeckung der Spitzen im Bereich des Vor- und Nachmittags, wenn Deine Vollzeitkräfte ausreichen, um das niedrige Volumen in der Mittagszeit zu bearbeiten. Die Tagesmodelle für die Teilzeit-Mitarbeiter werden somit am Morgen oder in den Nachmittagsbereich positioniert, sodass es eine möglichst geringe Überschneidung in der Mitte des Tages gibt.

## Planungsergebnis

Mit der Kombination aus Tagesmodellen für Vollzeit-Mitarbeiter und flexiblen Tagesmodellen im Vor- und Nachmittagsbereich für Teilzeit-Mitarbeiter haben wir alle Voraussetzungen für eine optimale Planung Deiner Mitarbeiter geschaffen.

{{ 1 | image: 'Deckung der Öffnungszeiten mit Schichten', '75%' }}
