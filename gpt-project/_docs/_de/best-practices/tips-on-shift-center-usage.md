---
title: Tipps zur Nutzung von Schicht Center
product_label:
  - advanced
  - enterprise
  - classic
description: Erfahre, wie du im Arbeitsalltag das Schicht Center effizient nutzen kannst.
redirect_from:
  - /de/best-practice-tips-on-shift-center-usuage/
---

In diesem Artikel erhältst du nützliche Tipps, um im Arbeitsalltag das Schicht Center effizient zu nutzen.

## Tipp 1: Ansicht der Stundenskala anpassen

Begrenze die Stundenskala auf die Öffnungszeiten deiner Planungseinheit, indem du nicht relevante Zeiträume ausblendest:

1. Gehe zu _Administration > System > Einstellungen_{:.breadcrumbs}.
2. Scrolle zum Abschnitt _SchedulePro_ (oder nutze die Suche).
3. Passe den Standardwert für die Einstellungen unterhalb nach deinen Bedürfnissen an:
   - _48077_{:.id-label}_Beginn der Stundenskala im Schicht Center_
   - _48078_{:.id-label}_Ende der Stundenskala im Schicht Center_

## Tipp 2: Shortcuts für die schnelle Zuweisung von Aktivitäten

Shortcuts bieten eine einfache und schnelle Möglichkeit, Mitarbeitern ganztägige Aktivitäten oder feste Tagesmodelle manuell zuzuordnen. Es ist nicht nötig, die entsprechende Aktivität erst in einem Dialogfenster auszuwählen. Dies ist besonders nützlich, wenn du Abwesenheiten im Rahmen der Tagessteuerung verwaltest.

Die beiden verfügbaren Arten von Shortcuts erlauben Buchstaben, Zahlen und Leerzeichen (max. 5 Zeichen):

- Standard-Shortcut: Drücke die _Enter_-Taste, nachdem du die definierte Abfolge auf deiner Tastatur eingegeben hast, um das entsprechende Tagesmodell oder die Aktivität einzufügen.
- Sofort-Shortcut: Du musst nicht die _Enter_-Taste drücken. Füge beim Anlegen der Shortcut-Definition am Ende ein _#_-Zeichen hinzu.

### Shortcuts erstellen

1. Gehe zu _Plan > Konfiguration_{:.breadcrumbs} und wähle **Aktivitäten**. Gehe für Tagesmodelle zu _WFM > Administration > Scheduling > Tagesmodelle_{:.breadcrumbs}.
2. Wähle eine **Aktivität** oder ein **Tagesmodell**.
3. Gib den Shortcut in das Feld **Shortcut** ein, z.&nbsp;B. **k** für _Krankheit_ (Standard-Shortcut) oder **k#** (Sofort-Shortcut).
4. Speichere den Shortcut mit _OK_{:.doc-button}.

Hinweis: Shortcuts setzen voraus, dass Aktivitäten und Tagesmodelle der Planungseinheit zugeordnet sind.

### Einen Standard-Shortcut verwenden

1. Wähle eine oder mehrere **Tageszellen** für einen Mitarbeiter im Planfenster aus.
2. Drücke **k**. Das neue Element wird direkt hinzugefügt. Um ein Element für mehrere aufeinanderfolgende Tage einzugeben, markiere **mehrere Zellen auf einmal**, bevor du **k** drückst. Diese Aktion überschreibt bestehende Elemente im Schichtplan.

### Einen Sofort-Shortcut verwenden

1. Wähle eine **Tageszelle** für einen Mitarbeiter im Planfenster aus.
2. Drücke **k**, dann die **Eingabetaste**. Um das Element für mehrere aufeinanderfolgende Tage einzugeben, drücke eine **Zahlentaste** nach dem Shortcut, z.&nbsp;B. **k** + **3** + **Enter**. Diese Aktion überschreibt bestehende Elemente im Schichtplan.

Tipp: Die Leertaste eignet sich hervorragend als Sofort-Shortcut (z.B. für die Aktivität Krankheit), da diese Taste am schnellsten erreichbar ist. Drücke einfach die Leertaste gefolgt von #.

{{ 1 | image: 'Sofort-Shortcut', '50%' }}

## Tipp 3: Ursprünglichen Plan als Referenz kopieren

Der beste Plan hat auch nur Bestand bis zur ersten notwendigen Änderung im Tagesgeschäft. Um einen Überblick über die notwendigen Planabweichungen zu behalten und gegebenenfalls Rückschlüsse für die nächste Planperiode ziehen zu können, bietet es sich an, den ursprünglichen Plan vor dem Ändern zu sichern.

Zu diesem Zweck bietet injixo verschiedene [Planungsebenen](#tipp-9-arbeiten-mit-verschiedenen-ebenen) und du kannst deinen endgültigen Schichtplan von der Ebene _Plan_ auf die Ebene _Aktueller Stand_ kopieren, indem du die Funktion {% link_new | features/scheduling/schedules/schedules-copy-level-content.md %} nutzt, um eine Referenz zu erhalten.

Verwende die Ebenen im Widerspruch zu ihren Namen:

- _Plan_: für alle Änderungen bei kurzfristigen Krankheiten, Urlauben, Verspätungen, unerwarteten Teambesprechungen etc. Optimiere Jobs und Pausen jederzeit, wenn du auf veränderte Bedarfe reagieren musst.
- _Aktueller Stand_: Verwende die Ebene für Vergleichszwecke. Sie dient als eine Referenz zur ursprünglichen Planung.

## Tipp 4: Sortierung in der Tagesansicht nutzen

Wenn du das _Schicht Center_{:.menu-item} öffnest, ist die Tagesansicht immer alphabetisch nach Mitarbeiternamen sortiert. Du kannst {% link_new die Sortierung ändern | features/scheduling/shiftcenter/sort-and-filter-items.md | #elemente-einer-ebene-sortieren %}, z.&nbsp;B. aufsteigend oder absteigend nach Startzeit der Schichten. Wenn du das _Schicht Center_{:.menu-item} erneut öffnest, klicke auf den **Pfeil nach unten**, um die zuvor verwendete Sortierung wieder aufzurufen.

## Tipp 5: Anzeige der Tageszelle ändern

Die Tageszelle bietet bei geschlossener wie offener Tagesansicht eine Kurzinformation zum Tag. Standardmäßig wird hier die Kurzbezeichnung der ersten Aktivität des Tages angezeigt, aber je nach Arbeitsweise kann es sinnvoll sein, die Ansicht anzupassen.

Um die tatsächlichen Arbeitsstunden (Bruttoarbeitszeit) oder die Zeiten für Schichtbeginn und -ende anstelle der Abkürzung des ersten Elements anzuzeigen, klicke mit der rechten Maustaste auf eine **Tageszelle**, wähle **Anzeigen**, und wähle dann eine der **Optionen**.

{{ 4 | image: 'Einstellen der Tageszellen-Anzeige', '50%'}}

## Tipp 6: Änderungshistorie für einen Tag anzeigen

Der Tab _Verlauf_ zeigt die aktuellen und früheren Mitarbeiterzuweisungen für den ausgewählten Tag an. Du kannst sehen, wer die jeweilige Änderung vorgenommen hat, was hilfreich sein kann, wenn du mit mehreren Personen an einem Schichtplan zusammenarbeitest. Erfahre, wie du {% link_new Aktionen anzeigst und rückgängig machst | features/scheduling/shiftcenter/modify-items.md | #vorherige-aktionen-anzeigen-und-rückgängig-machen %}.

## Tipp 7: Aktivitäten für mehrere Mitarbeiter auf einmal hinzufügen

Wenn du schnell dieselbe (Meeting-)Aktivität für mehrere Mitarbeiter einfügen musst, kann das manuelle Hinzufügen über das Schicht Center wesentlich schneller sein als ein automatisierter Prozess. Du hast den Schichtplan und das Kennzahlenfenster weiterhin direkt im Blick. Erfahre, wie du {% link_new Aktivitäten für mehrere Mitarbeiter auf einmal einfügst | features/scheduling/shiftcenter/add-and-delete-items.md | #elemente-für-mehrere-mitarbeiter-auf-einmal-hinzufügen %}.

## Tipp 8: Kennzahlenfenster anpassen

Auf dem Tab _Aktivitäten_ im Kennzahlenfenster kannst du durch Farben gekennzeichnete über- oder unterbesetzte Aktivitäten erkennen.

Um einen besseren Überblick zu erhalten, kannst du verschiedene Aktivitäten aus der Ansicht entfernen und nur {% link_new bestimmte Aktivitätstypen anzeigen | features/scheduling/shiftcenter/analyze-coverage-staffing-requirement.md | #aktivitäten-bestimmter-typen-ausblenden %}. Wenn du nur den Typ _Anwesenheit_ auswählst, ist es einfacher, Anpassungen vorzunehmen und deren direkte Auswirkungen im Schichtplan zu sehen, z. B. bei der Tagessteuerung, wenn du Krankmeldungen eingibst, um so ggf. bedarfsorientierte Gegenmaßnahmen einleiten zu können.

## Tipp 9: Arbeiten mit verschiedenen Ebenen

Zeige verschiedene Ebenen an und verwende diese, um deine Planung noch präziser durchzuführen:

- _Plan_{:.menu-item} zeigt manuell oder automatisch geplante Aktivitäten und Schichten an. Zuteilungen/Verlosungen des {% link_new Schichtwunsch-Verfahrens | features/scheduling/schedules/schedules-shift-bidding.md %} und {% link_new Optimierte Schichtpläne | features/scheduling/schedules/schedules-optimized-schedules.md %} schreiben auf diese Ebene. Job- und Pausenoptimierungen ändern den Ebeneninhalt, Mitarbeiter sehen diesen in injixo Me.
- _Aktueller Stand_{:.menu-item} enthält den tatsächlichen Schichtplan. [Kopiere deinen endgültigen Schichtplan](#tipp-3-ursprünglichen-plan-als-referenz-kopieren) in diese Ebene und nimm hier alle kurzfristigen Änderungen des Tages vor.
- _Externes System_{:.menu-item} zeigt {% link_new Agentenstatus-Daten | features/acd-integration/cloud/import-agent-status-data.md %} an, die über eine Integration importiert wurden (falls konfiguriert). Du kannst Einträge bei Bedarf manuell hinzufügen/bearbeiten.
- _Wunsch_{:.menu-item} zeigt alle Erstwünsche, die Mitarbeiter in injixo Me eingeben. Du kannst Tagesmodelle manuell hinzufügen, aber keine einzelnen Aktivitäten.
- _Ausweichwunsch_{:.menu-item} zeigt alle Ausweichwünsche, die Mitarbeiter in injixo Me eingeben. Du kannst Tagesmodelle manuell hinzufügen, aber keine einzelnen Aktivitäten.
- _Urlaubs-/Abwesenheitswunsch_{:.menu-item} zeigt alle Urlaubs- und Abwesenheitsanträge an, die Mitarbeiter in injixo Me eingeben. Du kannst Tagesmodelle manuell hinzufügen, aber keine einzelnen Aktivitäten.
- _Verfügbarkeit_{:.menu-item} zeigt die Verfügbarkeiten der Mitarbeiter an. Du kannst sie auch manuell hinzufügen.
- _Version 1_{:.menu-item} und _Version 2_{:.menu-item} kann Backups der Planung oder genehmigte Urlaubs- und Abwesenheitsanträge enthalten. Verwende diese Ebene zu Vergleichszwecken, z.&nbsp;B. für Pläne im Vergleich zum tatsächlichen Tag oder zum Testen/Vergleichen verschiedener Planungsszenarien.

Hinweis: injixo Advanced und Enterprise WFM enthalten alle Ebenen. Du kannst den Ebenen-Zugriff über {% link_new Benutzerrollen | getting-started/configure-user-roles.md %} konfigurieren. injixo Essential WFM bietet nur Zugriff auf die Ebene _Plan_.
