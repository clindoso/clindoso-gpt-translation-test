---
title: Tagesmodelle konfigurieren
redirect_from:
  - /de/day-models-overview/
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du Tagesmodelle vom Typ Zeitlich fixierte Schicht, Variable Schicht und Verfügbarkeitsrahmen erstellst und wie du Aktivitäten zu Tagesmodellen hinzufügst.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-basics.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/set-a-validity-period.md
---

Neu bei Tagesmodellen? Lerne zuerst {% link_new die Grundlagen | features/administration/daymodels/daymodel-basics.md %}.

## Tagesmodelle erstellen

Unter _Plan > Konfiguration > Tagesmodelle_{:.breadcrumbs} kannst du Tagesmodelle erstellen und bearbeiten.

> Hinweis
> 
> - Tagesmodelle vom Typ Zeitlich fixierte Schicht werden auch fixe Tagesmodelle genannt.<br> 
> - Tagesmodelle vom Typ Variable Schicht werden auch variable Tagesmodelle genannt.

1. Um ein neues Tagesmodell hinzuzufügen, klicke auf das {% icon item-add %}.
2. Wähle aus dem Dropdown-Menü **Typ** den Tagesmodelltyp aus, den du konfigurieren möchtest.
3. Konfiguriere dein Tagesmodell.<br>Um mehr über die Konfigurationsoptionen für jeden Tagesmodelltyp zu erfahren, sieh dir die folgenden Abschnitte an.
4. Um das Tagesmodell zu speichern, klicke auf _OK_{:.doc-button}.

Als nächstes kannst du dem neuen Tagesmodell {% link_new Aktivitäten hinzufügen | features/administration/daymodels/daymodel-creation.md | #aktivitäten-zu-tagesmodellen-hinzufügen %}. 

> Hinweis
> 
> Wenn du in deiner Planungseinheit die {% link_new Anzahl der Tagesmodelle eingeschränkt | features/administration/create-and-manage-planning-units.md | #tagesmodelle-einschränken %} hast, musst du deiner Planungseinheit neue Tagesmodelle manuell zuweisen. Wenn du mit Planungsmodellen arbeitest, aktualisiere die Wochenmodelle.

### Zeitlich fixierte Schicht
   
| **Parameter** | **Beschreibung** |
|:-----|:-----|
| Name | Eindeutiger Name, der das Tagesmodell beschreibt. Wir empfehlen, den Tagesmodelltyp sowie die Start- und Endzeiten anzugeben, z.&nbsp;B. 8-16:30-fix. |
| Kurzbezeichnung | Diese Version des Namens wird in Reports und unter Schedules angezeigt. Wir empfehlen, den Namen des Tagesmodells auch für die Kurzbezeichnung zu verwenden oder eine verkürzte Variante des Namens. |
| Shortcut | Optionales Tastaturkürzel, mit dem du das Tagesmodell schneller im Schicht Center einfügen kannst. Erfahre mehr über {% link_new Shortcuts | best-practices/tips-on-shift-center-usage.md %}. |
| Farbe | Die Farbe wird im Schichtplan und bei anderen Konfigurationselementen angezeigt. Sie kann dir helfen, die Länge oder den Typ des Tagesmodells oder darin enthaltene Aktivitäten auf einen Blick zu erkennen. |
| Gültig vom/Gültig bis | Optionaler Zeitraum, in dem das Tagesmodell verwendet werden kann. Erfahre mehr über {% link_new Gültigkeitszeiträume | features/administration/set-a-validity-period.md %}. |
| Beginn | Zeit, zu der die fixe Schicht beginnt. |
| Ende | Zeit, zu der die fixe Schicht endet. |
| Brutto-Schichtdauer | Dauer der Schicht in Stunden.<br>Wenn du diesen Wert konfigurierst, wird damit der konfigurierte Wert für das Schichtende ersetzt.<br>Hinweis: Tagesmodelle vom Typ Fixe Schicht können eine Dauer von bis zu zwei Tagen haben. Um eine Nachtschicht zu erstellen, füge der Endzeit bis zu 24&nbsp;Stunden hinzu, wenn du das Tagesmodell erstellst, oder verwende die Brutto-Schichtdauer. Der Maximalwert ist 48:00. |
| Aktivität | Die erste Aktivität ist die {% link_new Basisaktivität | features/administration/daymodels/daymodel-basics.md | #basisaktivität-und-schichtdauer %}.<br>Hinweis: Nach dem Speichern des Tagesmodells kannst du die Basisaktivität nicht mehr ändern. |


### Variable Schicht
   
| **Parameter** | **Beschreibung** |
|:---------------------|:---------------------|
| Name | Eindeutiger Name, der das Tagesmodell beschreibt. Wir empfehlen, den Tagesmodelltyp sowie die Start- und Endzeiten anzugeben, z.&nbsp;B. var-8-20-8. |
| Kurzbezeichnung | Diese Version des Namens wird in Reports und unter Schedules angezeigt. Wir empfehlen, den Namen des Tagesmodells auch für die Kurzbezeichnung zu verwenden oder eine verkürzte Variante des Namens. |
| Farbe | Die Farbe wird im Schichtplan und bei anderen Konfigurationselementen angezeigt.<br>Sie kann dir helfen, die Länge oder den Typ des Tagesmodells oder darin enthaltene Aktivitäten auf einen Blick zu erkennen. |
| Gültig vom/Gültig bis | Optionaler Zeitraum, in dem das Tagesmodell verwendet werden kann.<br>Erfahre mehr über {% link_new Gültigkeitszeiträume | features/administration/set-a-validity-period.md %}. |
| Zeitrahmen Beginn | Frühestmögliche Zeit, zu der die Schicht beginnen kann. |
| Zeitrahmen Ende | Spätestmögliche Zeit, zu der die Schicht enden kann. |
| Zeitrahmen Dauer | Anzahl der Stunden zwischen dem frühesten Start und dem spätesten Ende der Schicht.<br>Wenn du hier einen Wert einträgst, ersetzt dies den Wert für Zeitrahmen Ende. |
| Brutto-Schichtdauer | Gesamtdauer der Schicht einschließlich Pausen. Die Dauer muss kürzer sein als die Dauer des Zeitrahmens. Wenn die Schichtdauer genauso lang ist wie der Zeitrahmen, wird das Tagesmodell automatisch ein Tagesmodell vom Typ Zeitlich fixierte Schicht. |
| Intervall | Intervall, in dem eine Schicht innerhalb des festgelegten Zeitrahmens beginnen kann. Beispielsweise kann eine Schicht mit einem Intervall von 30 alle 30&nbsp;Minuten innerhalb des festgelegten Zeitrahmens beginnen. |
| Aktivität | Die erste Aktivität ist die {% link_new Basisaktivität | features/administration/daymodels/daymodel-basics.md | #basisaktivität-und-schichtdauer %}.<br>Hinweis: Nach dem Speichern des Tagesmodells kannst du die Basisaktivität nicht mehr ändern. |

### Verfügbarkeitsrahmen

Nutze diesen Tagesmodelltyp z.&nbsp;B. in Schichtfolgen, um Verfügbarkeiten für mehrere Mitarbeiter auf einmal zu konfigurieren. Beachte, dass Verfügbarkeiten aus Tagesmodellen sowohl Verfügbarkeiten überschreiben, die Mitarbeiter in injixo Me eingetragen haben, als auch Verfügbarkeiten, die manuell im Schicht Center hinzugefügt wurden. Erfahre mehr über {% link_new Verfügbarkeiten | features/administration/availabilities.md %}.

| **Parameter** | **Beschreibung** |
|:---------------------|:---------------------|
| Name | Eindeutiger Name, der das Tagesmodell beschreibt. Wir empfehlen, den Tagesmodelltyp sowie die Start- und Endzeiten anzugeben, z.&nbsp;B. verf-8-16. |
| Kurzbezeichnung | Diese Version des Namens wird in Reports und unter Schedules angezeigt. Wir empfehlen, den Namen des Tagesmodells auch für die Kurzbezeichnung zu verwenden oder eine verkürzte Variante des Namens. |
| Farbe |  Die Farbe wird im Schichtplan und bei anderen Konfigurationselementen angezeigt. Die Farbe kann z.&nbsp;B. beim Einrichten von Schichtfolgen hilfreich sein. |
| Gültig vom/Gültig bis | Optionaler Zeitraum, in dem das Tagesmodell verwendet werden kann.<br>Erfahre mehr über {% link_new Gültigkeitszeiträume | features/administration/set-a-validity-period.md %}. |
| Verfügbarkeitsrahmen Beginn | Frühestmögliche Zeit, zu der die Schicht beginnen kann. |
| Verfügbarkeitsrahmen Ende | Spätestmögliche Zeit, zu der die Schicht enden kann. |
| Verfügbarkeitsrahmen Dauer | Anzahl der Stunden zwischen dem frühesten Start und dem spätesten Ende der Schicht. Der Maximalwert ist 48:00. Wenn du hier einen Wert einträgst, ersetzt dies den Wert für Verfügbarkeitsrahmen Ende. |

## Aktivitäten zu Tagesmodellen hinzufügen

Um ein bereits vorhandenes Tagesmodell weiter zu definieren, kannst du ihm Pausen oder weitere Aktivitäten hinzufügen. Konfiguriere weitere Aktivitäten, wenn du spezielle Aktivitäten definieren möchtest, an denen Mitarbeiter zu einer bestimmten Zeit während der Schicht arbeiten sollen. Diese speziellen Aktivitäten können zum Beispiel sein, die Social-Media-Kanäle des Unternehmens zu überprüfen oder Backoffice-Tätigkeiten zu erledigen. 

Um Aktivitäten hinzuzufügen, musst du zunächst {% link_new das Tagesmodell erstellen | features/administration/daymodels/daymodel-creation.md | #tagesmodelle-erstellen %}.

Die Schichtplanoptimierung kann Aktivitäten vom Typ Anwesenheit ersetzen, die als Ersetzbar konfiguriert sind. Wenn du keine Mitarbeiter für spezielle Aktivitäten planen möchtest, ist die Basisaktivität die einzige Aktivität vom Typ Anwesenheit in deinem Tagesmodell. Beachte, dass du mit der Konfiguration von Aktivitäten in Tagesmodellen die Flexibilität der Optimierungsfunktionen einschränkst (z.&nbsp;B. Optimierten Plan erstellen, Extra-Aktivitäten planen, Meetings). Um die Optimierung so flexibel wie möglich zu halten und um Planungsfehler zu vermeiden, empfehlen wir, die Anzahl der Aktivitäten vom Typ Anwesenheit, die du in Tagesmodellen konfigurierst, möglichst gering zu halten.

> Hinweis
> 
> Die erste Aktivität, die du zu einem Tagesmodell hinzufügst, ist automatisch die Basisaktivität. Nach dem Speichern des Tagesmodells kannst du die Basisaktivität nicht mehr bearbeiten oder löschen.
> Wir empfehlen, die Aktivität Anwesend als Basisaktivität zu verwenden. Erfahre mehr über die {% link_new Basisaktivität | features/administration/daymodels/daymodel-basics.md | #basisaktivität-und-schichtdauer %}.

### Anwesenheits- oder Abwesenheitsaktivität hinzufügen

Um eine Anwesenheits- oder Abwesenheitsaktivität zu einem bestehenden Tagesmodell hinzuzufügen, gehe wie folgt vor:

1. Wähle ein Tagesmodell aus.
2. Klicke im Abschnitt **An- und Abwesenheiten** auf das {% icon item-add %}.<br>Ein Dialogfenster öffnet sich.
3. Konfiguriere die Aktivität:
- **Beginn** und **Ende**:<br>Wenn die Checkbox **Relativ zum Beginn der Schicht** aktiviert ist: Lege die Anzahl der Stunden/Minuten nach Schichtbeginn fest, zu der die Aktivität starten bzw. enden soll (gib z.&nbsp;B. für 1,5 Stunden 1:30 ein).<br>Wenn die Checkbox **Relativ zum Beginn der Schicht** deaktiviert ist: Gib die genaue Zeit nach dem Schichtbeginn an, zu der die Aktivität starten bzw. enden soll (gib z.&nbsp;B. für 14&nbsp;Uhr 14:00 ein).
- **Dauer**: Wenn du eine Dauer festlegst, die länger ist als die Zeit zwischen dem konfigurierten Beginn und Ende, erstellst du damit einen {% link_new Korridor | features/administration/daymodels/daymodel-basics.md | #feste-elemente-vs-korridore %}. Aktivitäten können innerhalb eines Korridors verschoben werden.
- **Intervall**: Wir empfehlen, hier dasselbe Intervall zu verwenden wie deine ACD. Beachte, dass die Länge der Aktivität durch das gewählte Intervall teilbar sein muss. Wenn du den Wert 0 eingibst, steht die Zeit für den Beginn der Aktivität fest. Die Aktivität kann dann nicht innerhalb eines Korridors verschoben werden.
- **Relativ zum Beginn der Schicht**: Wenn die Checkbox aktiviert ist (Standardeinstellung), beginnt die Aktivität zu der festgelegten Anzahl an Stunden/Minuten nach dem Beginn der Schicht. Wenn die Schicht verschoben wird, wird auch die Aktivität verschoben.<br>Wenn die Checkbox deaktiviert ist, beginnt die Aktivität genau zu der konfigurierten Zeit. Wenn du eine variable Schicht verschiebst, werden dabei die Aktivitäten nicht verschoben. Dies kann nützlich sein, z.&nbsp;B. wenn Mitarbeiter mit unterschiedlichen Schichten zur selben Zeit an einem Teammeeting teilnehmen sollen.
4. Wähle aus dem Dropdown-Menü eine **Aktivität** aus.
5. Klicke auf _OK_{:.doc-button}.

### Pausenaktivität hinzufügen

Sowohl in variablen als auch in fixen Tagesmodellen kannst du Pausen für die optimierte Planung und das Schichtwunsch-Verfahren hinzufügen.  
Um eine Pausenaktivität zu einem bestehenden Tagesmodell hinzuzufügen, gehe wie folgt vor:

1. Wähle ein Tagesmodell aus.
2. Klicke im Abschnitt **Pausen (Schichterzeugung)** auf das {% icon item-add %}.<br>Ein Dialogfenster öffnet sich.
3. Konfiguriere die Pause:
- **Beginn** und **Ende**:<br>Wenn die Checkbox **Relativ zum Beginn der Schicht** aktiviert ist: Lege die Anzahl der Stunden/Minuten nach Schichtbeginn fest, zu der die Pause starten bzw. enden soll (gib z.&nbsp;B. für 4,5 Stunden 4:30 ein). Pausen werden standardmäßig relativ zum Beginn der Schicht eingetragen, da sie normalerweise erst nach einer bestimmten Zeit am Arbeitsplatz beginnen.<br>Wenn die Checkbox **Relativ zum Beginn der Schicht** deaktiviert ist: Gib die genaue Zeit nach dem Schichtbeginn an, zu der die Pause starten bzw. enden soll (gib z.&nbsp;B. für 13&nbsp;Uhr 13:00 ein).
- **Dauer**: Wenn du eine Dauer festlegst, die länger ist als die Zeit zwischen dem konfigurierten Beginn und Ende, erstellst du damit einen {% link_new Korridor | features/administration/daymodels/daymodel-basics.md | #feste-elemente-vs-korridore %}. Pausen können innerhalb eines Korridors verschoben werden.
- **Intervall**: Wir empfehlen, hier dasselbe Intervall zu verwenden wie deine ACD. Beachte, dass die Länge der Pause durch das gewählte Intervall teilbar sein muss.<br>Wenn du den Wert 0 eingibst, steht die Zeit für den Beginn der Pause fest. Die Pause kann dann nicht innerhalb eines Korridors verschoben werden.
- **Relativ zum Beginn der Schicht**: Wenn die Checkbox aktiviert ist (Standardeinstellung), beginnt die Pause zu der festgelegten Anzahl an Stunden/Minuten nach dem Beginn der Schicht. Wenn die Schicht verschoben wird, wird auch die Pause verschoben.<br>Wenn die Checkbox deaktiviert ist, beginnt die Pause genau zu der konfigurierten Zeit. Wenn du eine variable Schicht verschiebst, werden dabei die Pausen nicht verschoben. Das ist z.&nbsp;B. empfehlenswert, wenn die Kantine in deinem Contact Center nur begrenzt geöffnet hat.
4. Wähle aus dem Dropdown-Menü **Pause** eine Pausenoption.
5. Klicke auf _OK_{:.doc-button}.

Hinweis: In injixo Enterprise WFM On-premise bestimmt die Einstellung _48134_{:.id-label} _Behandlung von An- und Abwesenheiten oder Pausen in Zeitkorridoren beim Lösen des Schichtbezugs in Tagesmodellen_, ob Pausenkorridore beibehalten oder in feste Elemente umgewandelt werden.

## Was passiert, wenn ich Tagesmodelle ändere, die bereits verwendet werden?

Wenn du Tagesmodelle änderst, die bereits verwendet werden, kann das unterschiedliche Auswirkungen haben. Du kannst problemlos Konfigurationsdaten ändern, die nicht planungsbezogen sind, z.&nbsp;B. den Namen, die Kurzbezeichnung oder die Farbe.

Allerdings empfehlen wir dir, planungsrelevante Daten wie Start- und Endzeiten, Brutto-Schichtdauer, An- und Abwesenheiten oder Pausen nur zu ändern, bevor du deinen nächsten Schichtplan erstellst. Wenn du ein bestehendes Tagesmodell änderst, erstellt injixo automatisch eine interne Kopie des ursprünglichen Tagesmodells. Dadurch bleiben bereits geplante Schichten erhalten und werden weiterhin angezeigt.

Wenn du ein bestehendes Tagesmodell geändert oder ein neues hinzugefügt hast, empfehlen wir dir, den Planungsprozess von Anfang an erneut durchzuführen, um sicherzustellen, dass alle geänderten oder neuen Tagesmodelle korrekt verwendet werden.

Betroffene Tagesmodelle werden in Schichtfolgen und Wochenmodellen ersetzt. Bereits geplante Tagesmodelle werden im Schicht Center und in Schedules mit einer gepunkteten Linie am unteren Rand dargestellt. Schichten mit diesem Tagesmodell können nicht mehr geplant oder bearbeitet werden. Sie können nur aus dem Schichtplan gelöscht werden.

Wenn du Schichten aus einem Tagesmodell erstellt hast und Mitarbeiter auf diese Schichten im Zuge des Schichtwunsch-Verfahrens bereits einen Schichtwunsch abgegeben haben, können deine Mitarbeiter die Schichten mit diesem Tagesmodell nicht mehr sehen oder einen Schichtwunsch dafür abgeben.
Schichten, auf die bereits ein Schichtwunsch abgeben wurde, werden in der nachfolgenden Schichtverlosung oder bei den Schichtzuweisungen nicht mehr verwendet.

Hinweis: Die Minimal- und Maximalwerte für den Schichtbedarf gelten auch für das geänderte Tagesmodell.
