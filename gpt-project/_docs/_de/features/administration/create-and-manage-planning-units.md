---
title: Planungseinheiten anlegen und verwalten
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Erfahre, wie Du Planungseinheiten erstellst, konfigurierst und löschst.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/planning-calendar.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/how-to-use-virtual-planning-units.md
redirect_from:
  - /de/planning-unit-configuration/
redirect_reason: Updated filename on 21 August 2023
---

In diesem Artikel lernst Du:

- was Planungseinheiten sind.
- wie Du sie erstellst, bearbeitest und löschst.
- wie Du Öffnungszeiten, Aktivitäten, Multiaktivitäten und Tagesmodelle zu einer Planungseinheit hinzufügst.

## Was sind Planungseinheiten?

Planungseinheiten fassen Mitarbeiter für die Planung zusammen. Normalerweise gehören alle Mitarbeiter zur gleichen Planungseinheit, es sei denn:

- die Mitarbeiter befinden sich in unterschiedlichen Zeitzonen. Nutze in diesem Fall eine Planungseinheit pro Zeitzone.
- die Planer oder Supervisor in Deinem Betrieb sind jeweils nur für eine Untergruppe von Mitarbeitern zuständig, z.B. je nach Geschäftsbereich. In diesem Fall sollte für jeden Planer eine separate Planungseinheit zur Verfügung stehen (nur möglich mit injixo Advanced und Enterprise).

## Eine Planungseinheit anlegen

1. Gehe zu _WFM > Administration > Scheduling > Planungseinheiten_{:.breadcrumbs}.
2. Klicke auf das {% icon item-add %} in der Aktionsleiste. Der folgende Dialog erscheint:

   {{ 1 | image: "Planungseinheit", '60%' }}

3. Vergib einen **Namen** (max. 50 Zeichen)
4. Gib eine **Kurzbezeichnung** (max. 25 Zeichen) ein. Die Kurzbezeichnung wird in einigen Modulen von injixo anstelle des Namens verwendet. Wenn der Name der Planungseinheit kurz ist, verwende ihn einfach auch hier.
5. Wähle eine **Farbe** (optional). injixo wird die Planungseinheit in dieser Farbe anzeigen.
6. Wähle ein **Intervall**. Es sollte dem Intervall entsprechen, dass die {% link_new Integration(en) | features/acd-integration/cloud/how-integrations-work.md %} nutzen, die die für die Planungseinheit relevanten Daten importieren. Stelle das Intervall auf 15, 30 oder 60 Minuten ein. Du kannst das Intervall nach dem Speichern nicht mehr ändern.
7. Wähle eine **Übergeordnete Planungseinheit** (optional), zu der die Planungseinheit gehören soll. Eine übergeordnete Planungseinheit ermöglicht es, mehrere Planungseinheiten in einem Schritt zu planen. Dies kann hilfreich sein, um den Mitarbeiterbedarf über mehrere Planungseinheiten hinweg besser abzudecken. Eine übergeordnete Planungseinheit kann auch verwendet werden, um einen Überlauf abzubilden, d.&nbsp;h. sicherzustellen, dass eine Planungseinheit einen Teil des Kontaktvolumens einer anderen Planungseinheit übernimmt, wenn diese überlastet ist.
8. Wähle für die Planungseinheit die lokale {% link_new **Zeitzone** | best-practices/working-with-timezones.md %} aus. Diese kann nach dem Speichern nicht mehr geändert werden. Wenn Du Mitarbeiter so planen willst, dass sie über verschiedene Standorte oder Zeitzonen hinweg an einem gemeinsamen Pool von Kontaktvolumen arbeiten, lies den Artikel zur Planung von Mitarbeitern an {% link_new verschiedenen Standorten | best-practices/how-to-use-virtual-planning-units.md %}.
9. Klicke auf _Ok_{:.doc-button}.

Du hast nun eine Planungseinheit erstellt. Füge als nächstes Informationen in den Abschnitten **Öffnungszeiten**, **Aktivitäten** und **Tagesmodelle** hinzu. Bei Bedarf kannst Du auch einen {% link_new Planungskalender | features/administration/planning-calendar.md %} verknüpfen. Unterhalb erfährst Du mehr über jeden Abschnitt.

### Öffnungszeiten hinzufügen

Füge Deiner Planungseinheit immer Öffnungszeiten hinzu. Die Mitarbeiterbedarfsberechnung und die volloptimierte Planung berücksichtigen diese Öffnungszeiten.

1. Klicke links in der Liste auf die **Planungseinheit**, die Du gerade erstellt hast.
2. Scrolle zum Abschnitt _Öffnungszeiten_ und klicke auf das {% icon item-add %}, um Öffnungszeiten für bestimmte Tagestypen hinzuzufügen.
3. Wähle zunächst den {% link_new **Tagestyp** | features/administration/day-types.md %} aus. Halte während Du klickst _STRG_ oder _Shift_ gedrückt, um mehrere Elemente auf einmal auszuwählen.
4. Gib die Startzeit in das Feld **Von** ein.
5. Gib die Endzeit in das Feld **Bis** ein. Gib 00:00 bis 00:00 in die Felder _Von_ und _Bis_ ein, wenn Du 24 Stunden geöffnet hast.
6. **Gültig von** und **Gültig bis** werden nur verwendet, wenn Du festlegen willst, dass die gerade eingegebenen Öffnungszeiten nur für einen bestimmten Datumsbereich gelten. Wenn sie ohne Einschränkung gelten, lass die Felder einfach leer. Erfahre mehr über {% link_new Gültigkeitszeiträume | features/administration/set-a-validity-period.md %} in injixo.
7. Klicke auf _Ok_{:.doc-button}.

Du hast nun die Öffnungszeiten für den gewählten Tagestyp hinzugefügt. Füge jetzt die Öffnungszeiten für alle weiteren Tagestypen hinzu, die in der Planungseinheit geplant werden sollen.

Um die Öffnungszeiten zu ändern oder zu entfernen, klicke auf _![Bleistift-Symbol](/assets/img/common/item-edit.gif)_{:.doc-button-icon} oder _![rotes Kreuz](/assets/img/common/item-delete.gif)_{:.doc-button-icon}.

{{ 2 | image: "Öffnungszeiten der Planungseinheit", '60%' }}

### Aktivitäten hinzufügen

Mitarbeiter einer Planungseinheit können nur für Aktivitäten geplant werden, die dieser Planungseinheit zugewiesen sind. Das wird durch die standardmäßig aktivierte {% link_new Planungsregel | features/administration/create-contracts.md %} _2606_{:.id-label} sichergestellt.  
Die Standardaktivität mit der ID 1, in der Regel _Anwesend_ genannt, ist jeder Planungseinheit automatisch zugeordnet und kann nicht entfernt werden.

Füge der Planungseinheit alle Aktivitäten hinzu, die Deine Mitarbeiter normalerweise ausführen:

1. Scrolle zum Abschnitt _Aktivitäten_ und klicke auf das {% icon item-add %}.
2. Wähle mit einem Klick eine {% link_new **Aktivität** | features/administration/activities.md %} aus.
3. Belasse die Felder **Von** und **Bis** auf 00:00 bis 00:00. Standardmäßig berücksichtigt injixo nur die zuvor eingegebenen Öffnungszeiten der Planungseinheit. Ein Admin Benutzer kann über die Einstellung _48408_{:.id-label} _Berücksichtigung von Öffnungszeiten im AutoScheduler_ ein abweichendes Verhalten definieren.
4. Normalerweise lässt Du **Gültig von** und **Gültig bis** leer. Es sei denn, Du möchtest, dass eine Aktivität nur während eines bestimmten Datumsbereichs zur Planung zur Verfügung stehen soll.
5. Klicke auf _Ok_{:.doc-button}.

Um eine Aktivität zu ändern oder zu entfernen, klicke auf _![Bleistift-Symbol](/assets/img/common/item-edit.gif)_{:.doc-button-icon} oder _![rotes Kreuz](/assets/img/common/item-delete.gif)_{:.doc-button-icon}.

{{ 3 | image: "Aktivitäten der Planungseinheit", '60%' }}

### Multiaktivitäten hinzufügen

Um {% link_new Multiskill-Agenten | best-practices/how-to-schedule-multiskill-agents.md %} für mehrere Aktivitäten gleichzeitig zu planen, musst Du der Planungseinheit eine Multiaktivität wie oben beschrieben zuweisen. Gehe am besten wie folgt vor:

1. Erstelle eine {% link_new Multiaktivität | features/administration/activity-types-and-properties.md | #teilaktivitäten %}. Die Multiaktivität enthält die von den Multiskill-Mitarbeiter ausführbaren Aktivitäten als Teilaktivitäten.
2. Füge die Teilaktivitäten zur Planungseinheit hinzu.
3. Füge die Multiaktivität zur Planungseinheit hinzu. In der Aktivitäten-Liste wird sie fett hervorgehoben.

Multiaktivitäten sind nicht in injixo Essential verfügbar.

### Tagesmodelle verwalten

Standardmäßig sind alle vorhandenen Tagesmodelle automatisch der Planungseinheit zugewiesen. Normalerweise änderst Du diese Zuordnung nicht. Beachte, dass Du nur diejenigen Tagesmodelle, die der Planungseinheit zugewiesen sind, verwenden kannst, um Schichten anzulegen, Reports zu erstellen oder manuelle oder automatische Planungen durchzuführen.

Um ein Tagesmodell zu ändern oder zu entfernen, scrolle zum Abschnitt _Tagesmodelle_ und klicke auf das {% icon item-edit %} oder das {% icon item-delete %}. Um ein Tagesmodell hinzuzufügen, klicke auf das {% icon item-add %}. Wähle das Tagesmodell aus, das Du hinzufügen möchtest und klicke auf _Ok_{:.doc-button}.

{{ 4 | image: "Tagesmodelle der Planungseinheit", '60%' }}

## Eine Planungseinheit löschen

1. Klicke in der Liste auf die **Planungseinheit**, die Du entfernen möchtest.
2. Scrolle zu den Abschnitten _Aktivitäten_ und _Tagesmodelle_ und entferne alle zugewiesenen Aktivitäten und Tagesmodelle. Dadurch verhinderst Du, dass diese Tagesmodelle und Aktivitäten später einer gelöschten Planungseinheit zugeordnet sind. Klicke auf _![rotes Kreuz](/assets/img/common/item-delete.gif)_{:.doc-button-icon} neben jeder Aktivität und jedem Tagesmodell, um sie zu entfernen.
3. Stelle sicher, dass die **Planungseinheit**, die Du löschen willst, in der Liste markiert ist.
4. Klicke in der Aktionsleiste über der Liste der Planungseinheiten auf _![rotes Kreuz](/assets/img/common/item-delete.gif)_{:.doc-button-icon}.
5. Bestätige das Löschen mit _Ja_{:.doc-button}.