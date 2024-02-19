---
title: Tagesmodelle im Überblick
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, welche Tagesmodelltypen es gibt, was du beachten musst, bevor du ein Tagesmodell erstellen kannst und welche Auswirkungen es auf den Schichtplan hat, wenn du ein Tagesmodell änderst.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
---

Tagesmodelle sind Vorlagen für Schichten. Sie umfassen den Arbeitstag für deine geplanten Mitarbeiter und legen die Start- und Endzeiten von Schichten fest. Außerdem bestimmen sie pro Mitarbeiter die Anzahl der Arbeitsstunden pro Tag und wann die Mitarbeiter arbeiten können. injixo erstellt Schichtpläne auf Grundlage deiner Tagesmodelle.

Wenn du Tagesmodelle erstellst, werden diese standardmäßig automatisch allen Planungseinheiten deines Unternehmens zugewiesen. Um diese Standardeinstellung zu ändern, {% link_new bearbeite die Planungseinheit | features/administration/create-and-manage-planning-units.md | #tagesmodelle-verwalten %}. Während der Schichtplanoptimierung berücksichtigt injixo nur die Tagesmodelle, die der Planungseinheit zugewiesen sind.

Wenn die Tagesmodelle in deiner Planungseinheit nicht alle Arbeitsverträge abdecken, kannst du für einzelne Mitarbeiter auch individuelle Tagesmodelle anlegen. Während der Schichtplanoptimierung verwendet injixo nur diese individuellen Tagesmodelle für diese Mitarbeiter.

Tagesmodelle enthalten die Anwesenheits-, Abwesenheits- und Pausenaktivitäten einer Schicht. Deshalb musst du {% link_new relevante Aktivitäten zu Tagesmodellen hinzufügen | features/administration/daymodels/daymodel-creation.md %}.

Tagesmodelle werden zu {% link_new Schichtfolgen | features/administration/shift-sequences.md %} hinzugefügt und können in {% link_new Wochenmodellen | features/administration/work-time-pattern-models.md | #wochenmodelle-erstellen %} gruppiert werden.


## Tagesmodelltypen

Es gibt drei verschiedene Typen von Tagesmodellen. 

> Hinweis
> 
> - Tagesmodelle vom Typ Zeitlich fixierte Schicht werden auch fixe Tagesmodelle genannt.<br> 
> - Tagesmodelle vom Typ Variable Schicht werden auch variable Tagesmodelle genannt.


| Typ                | Beschreibung                                                                                                                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zeitlich fixierte Schicht         | Schichten mit einem fixen Tagesmodell haben feste Start- und Endzeiten, die nicht verschoben werden können. Aus einem fixen Tagesmodell kann sich immer nur eine Schicht ergeben. Fixe Tagesmodelle werden in der Regel zu {% link_new Schichtfolgen | features/administration/shift-sequences.md %} hinzugefügt.                                      |
| Variable Schicht      | Schichten mit einem variablen Tagesmodell haben flexible Startzeiten innerhalb eines festgelegten Zeitraums. Daraus ergeben sich mehrere mögliche Schichten. Variable Tagesmodelle, die zu Schichtfolgen hinzugefügt werden, werden automatisch zu fixen Tagesmodellen, weil sie fest an die erste mögliche Startposition einer Schicht gesetzt werden. |
| Verfügbarkeitsrahmen | Dieser Tagesmodelltyp wird verwendet, um einen Zeitraum festzulegen, der kürzer ist als die Geschäftszeiten der Planungseinheit. Wenn du Schichtfolgen mit diesem Tagesmodelltyp eingefügt hast, wählt injixo während der Optimierung und beim Schichtwunsch-Verfahren Tagesmodelle aus, die mit der festgelegten Verfügbarkeit übereinstimmen. Du kannst diesen Typ auch verwenden, um für mehrere Mitarbeiter auf einmal Verfügbarkeiten zu konfigurieren.          |

## Wann verwende ich welches Tagesmodell?

Es gibt nicht den einen allgemeingültigen Anwendungsfall pro Tagesmodell, aber in der folgenden Liste findest du Richtlinien zur Orientierung:

- Zeitlich fixierte Schicht: Verwende fixe Tagesmodelle, um Mitarbeiter mit festen Arbeitszeiten zu planen. Ihre Schichten beginnen und enden immer zu einer festen Zeit und können im Schichtplan nicht verschoben werden.
Du kannst fixe Tagesmodelle in Planungsmodellen verwenden, um {% link_new optimierte Schichtpläne | features/scheduling/scheduling-optimization.md %} zu erstellen, mit denen du wöchentlich wiederkehrende Muster in {% link_new Schichtfolgen | features/scheduling/schedules/schedules-insert-shift-sequences.md %} definierst oder wenn du mit dem {% link_new Schichtwunsch-Verfahren | features/scheduling/schedules/schedules-shift-bidding.md %} arbeitest.
- Variable Schicht:  Verwende variable Tagesmodelle, um Mitarbeiter mit flexiblen Arbeitszeiten zu planen. injixo kann mit nur einem Tagesmodell dieses Typs einen Mitarbeiter für verschiedene Schichten planen. Dieses Tagesmodell wird typischerweise verwendet, um {% link_new optimierte Schichtpläne | features/scheduling/scheduling-optimization.md %} zu erstellen oder wenn du mit dem {% link_new Schichtwunsch-Verfahren | features/scheduling/schedules/schedules-shift-bidding.md %} arbeitest.
- Verfügbarkeitsrahmen: Wenn die Geschäftszeiten deiner Planungseinheit länger sind als die Dauer eines üblichen Arbeitstages, kannst du für injixo die Planungsoptionen einschränken. Wenn du die Verfügbarkeit für mehrere Mitarbeiter auf einmal einschränken möchtest, verwende Tagesmodelle vom Typ Verfügbarkeitsrahmen und füge diese zu Schichtfolgen hinzu. Alternativ kannst du in den Mitarbeitereinstellungen {% link_new Verfügbarkeiten für einzelne Mitarbeiter konfigurieren | features/administration/availabilities.md %}. Beide werden bei der Schichtplanoptimierung berücksichtigt, wenn die Planungsregel&nbsp;2611 aktiviert ist.

Als Alternative zu Verfügbarkeiten kannst du auch {% link_new Schichtfolgen | features/administration/shift-sequences.md %} Wochenmodelle in {% link_new Planungsmodellen | features/administration/work-time-pattern-models.md | #wochenmodelle-erstellen %} verwenden. Du kannst auch beides verwenden, zum Beispiel, wenn du Früh- und Spätschichten rotieren möchtest.

Wir empfehlen, eine limitierte Anzahl an variablen Tagesmodellen zu erstellen (in Kombination mit den {% link_new Verfügbarkeiten deiner Mitarbeiter | features/administration/availabilities.md | #mitarbeiter-verfügbarkeiten-erstellen %}) anstatt eine große Anzahl fixer Tagesmodelle zu erstellen.

## Basisaktivität und Schichtdauer

Für jedes fixe oder variable Tagesmodell musst du immer eine Basisaktivität einrichten, um die Gesamtschichtdauer festzulegen. Du kannst in beiden Tagesmodelltypen weitere Aktivitäten hinzufügen, die die Basisaktivität überlagern. Die Dauer der anderen Aktivitäten darf die Dauer der Basisaktivität nicht überschreiten.

Die Basisaktivität deckt die gesamte Zeit ab, die ein geplanter Mitarbeiter während seiner Schicht anwesend ist, einschließlich Pausen und anderen unbezahlten Aktivitäten. Sie ist die erste Aktivität, die du auswählst, wenn du ein neues Tagesmodell erstellst und du kannst sie nicht mehr löschen oder bearbeiten, nachdem du das Tagesmodell gespeichert hast.

Die Gesamtdauer einer geplanten Schicht einschließlich Pausen entspricht der Brutto-Schichtdauer. Nach Abzug der unbezahlten Aktivitäten, wie z.&nbsp;B. Pausen oder Rüstzeiten, ergibt sich aus der übrigen Arbeitszeit die Netto-Schichtdauer. Die Netto-Schichtdauer wird in Schedules und im Schicht Center unter dem Namen Ist-Zeit angezeigt. Beachte, dass in Verträgen ebenfalls Netto-Zeiten festgelegt sind. 

Die Länge eines Tagesmodells muss zu den Arbeitszeiten in deinen {% link_new Verträgen | features/administration/create-contracts.md %} passen.
Wenn ein Vertrag eine wöchentliche Arbeitszeit von 40&nbsp;Stunden aufgeteilt auf 5&nbsp;Tage vorsieht, benötigst du ein Tagesmodell mit einer Netto-Arbeitszeit von 8&nbsp;Stunden pro Tag. Bei einem Vertrag mit 37,5&nbsp;Stunden pro Woche benötigst du ein Tagesmodell mit 7,5&nbsp;Stunden pro Tag.

Verwende die Aktivität Anwesend als Basisaktivität und vergewissere dich, dass sie als Ersetzbar konfiguriert ist. Dann können die Funktionalitäten Joboptimierung und Optimierten Plan erstellen die Aktivität Anwesend durch andere Aktivitäten ersetzen, solange diese einen {% link_new berechneten Mitarbeiterbedarf | features/forecast/injixo-forecast/staff-requirement.md %} haben und als Planbar konfiguriert sind.

### Feste Elemente vs. Korridore

Du kannst ein Korridorelement erstellen, indem du eine Aktivität hinzufügst, deren Dauer kürzer ist als die Zeit vom Start bis zum Ende des Elements. Korridorelemente überlagern in einer Schicht alle festen Elemente. Bei der optimierten Planung werden Korridorelemente zugunsten der Deckung verschoben. Korridore können sich überlappen, aber Aktivitäten innerhalb von zwei Korridoren können dies nicht.

Wenn du ein Tagesmodell manuell in den Schichtplan einfügst, werden Korridorelemente an der frühestmöglichen Stelle innerhalb des Korridors platziert. Du kannst Korridore innerhalb der festgelegten Intervalle manuell verschieben.

Wenn die Dauer eines Korridorelements exakt mit der konfigurierten Start- und Endzeit des Elements übereinstimmt, wird stattdessen ein festes Element erstellt.

