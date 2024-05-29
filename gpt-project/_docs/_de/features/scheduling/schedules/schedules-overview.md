---
title: Was ist Schedules?
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Sieh dir Schichten, Aktivitäten und andere Planungselemente wie Abwesenheitsanträge an und bearbeite sie.
promote-service: team-leader-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-activity-coverage.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-edit.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-comments.md
---

Unter _Plan > Schedules_{:.breadcrumbs} kannst du die Schichten deiner Mitarbeiter einsehen und verwalten. Du kannst Mitarbeiter über Schichtplanänderungen informieren, Planperioden erstellen und verwalten und hast Zugriff auf alle verfügbaren Planungsaktionen.
Schedules besteht aus einer Aktionsleiste und jeweils einem Bereich für den Schichtplan und die Aktivitäten. In den verschiedenen Abschnitten dieses Artikels erfährst du, was du in jedem Seitenbereich tun kannst.

## Voraussetzungen

Um **Schedules** optimal nutzen zu können, stelle sicher, dass folgendes zutrifft:

- Du hast mindestens eine {% link_new Auswahl | features/administration/selections.md %} erstellt.
- Du hast deine Firewall so konfiguriert, dass sie {% link_new WebSocket-Verbindungen | getting-started/system-requirements.md | #urls-für-websockets-freigeben %} für injixo erlaubt. Dies ist für Echtzeit-Updates erforderlich. Wenn die erforderliche WebSocket-Verbindung aufgrund von Firewalls nicht geöffnet werden kann bzw. aufgrund einer instabilen Netzwerkverbindung geschlossen wird, wird dir eine Fehlermeldung angezeigt.

## Aktionsleiste

### Daten filtern

Auf der linken Seite der Aktionsleiste stehen dir folgende Filteroptionen zur Verfügung:

- Filtern nach Planungseinheit: Wähle eine oder mehrere Planungseinheiten aus dem linken Dropdown-Menü aus.
- Filtern nach Auswahl: Klicke auf das {% icon selection-filter-u %} und wähle eine Auswahl aus dem rechten Dropdown-Menü.
- Filtern nach {% link_new Mitarbeiterfilter | features/administration/employee-filter.md %}: Klicke auf das {% icon schedules-filter-employees-u %} und wähle einen vorab konfigurierten Mitarbeiterfilter aus dem rechten Dropdown-Menü.

### Mitarbeiter benachrichtigen

Klicke auf _Mitarbeiter benachrichtigen_{:.doc-button}, um Mitarbeiter per Push-Benachrichtigung oder E-Mail {% link_new über Änderungen an ihrem Schichtplan zu informieren | features/scheduling/schedules/schedules-notify-scheduling-changes.md %}.

### Planperioden

Klicke auf _Planperioden_{:.doc-button}, um {% link_new Planperioden zu konfigurieren | features/scheduling/schedules/scheduling-periods/what-are-scheduling-periods.md %}.

### Planungsaktionen

Wähle aus dem Dropdown-Menü ganz rechts in der Aktionsleiste eine der folgenden Planungsaktionen aus:

- {% link_new Schichtfolgen einfügen | features/scheduling/schedules/schedules-insert-shift-sequences.md %}: Füge feste, sich wiederholende Abfolgen von Schichten, Aktivitäten oder Verfügbarkeiten in deinen Schichtplan ein.
- {% link_new Joboptimierung | features/scheduling/schedules/schedules-job-optimization.md %}: Ersetze Aktivitäten, um die Deckung zu verbessern.
- {% link_new Pausen optimieren | features/scheduling/schedules/break-optimization.md %}: Ordne die Pausen im Schichtplan neu an, um die Deckung zu verbessern.
- {% link_new Aktivitäten ersetzen | features/scheduling/schedules/schedules-replace-activities.md %}: Ersetze eine Aktivität durch eine andere Aktivität in einem bestehenden Schichtplan, um auf Änderungen im Bedarf zu reagieren.
- {% link_new Ebenen leeren | features/scheduling/schedules/schedules-empty-levels.md %}: Lösche den Inhalt einer Ebene.
- {% link_new Ebeneninhalte kopieren | features/scheduling/schedules/schedules-copy-level-content.md %}: Kopiere und sichere deine Schichtpläne und andere Elemente in einer Ebene.
- {% link_new Tauschanfragen genehmigen | features/scheduling/view-approve-shift-swap-requests.md %}: Genehmige Schichttausch-Anfragen deiner Mitarbeiter oder lehne sie ab.

Die folgenden Planungsaktionen sind nur in injixo Advanced WFM und Enterprise WFM verfügbar:

- {% link_new Optimierten Plan erstellen | features/scheduling/schedules/schedules-optimized-schedules.md %}: Erstelle automatisch einen Schichtplan mit der bestmöglichen Deckung für alle Aktivitäten.
- {% link_new Extra-Aktivitäten planen | features/scheduling/schedules/schedules-extra-activities.md %}: Plane lagerfähige Aktivitäten wie E-Mail und Backoffice-Aufgaben, indem du bestehende Aktivitäten ersetzt.

### Vollbildmodus

Klicke auf das Vollbildmodus-Icon _![Vollbildmodus-Icon](/assets/img/common/full-screen-mode.png)_{:.doc-button-icon}, um in den Vollbildmodus zu wechseln. Um im Vollbildmodus die Aktionsleiste anzuzeigen, bewege den Mauszeiger zum Pfeil-Icon am oberen Bildschirmrand. Wenn du den Vollbildmodus verlassen möchtest, klicke auf das {% icon full_screen_exit %} oder drücke die Esc-Taste.

## Schichtplan-Bereich

Der Schichtplan-Bereich ist eine Tabelle, die geplante Schichten anzeigt. Je nachdem, was du in der Aktionsleiste gewählt hast, zeigt sie Schichten für die Mitarbeiter in den entsprechenden Planungseinheiten, Auswahlen bzw. gemäß der gewählten Mitarbeiterfilter an.<br>Bewege den Mauszeiger über eine Schicht, um weitere Details anzuzeigen. Wenn eine Schicht Korridore enthält, z.&nbsp;B. für Pausen, zeigt die Detailansicht den Korridor als letzten Eintrag in der Liste an, unabhängig von seiner tatsächlichen Position im Schichtplan.

### Spalte Mitarbeitername

Die Spalte **Mitarbeitername** ist die erste Spalte von links. Sie zeigt die Planungseinheiten gemäß deinem Filter an. Klicke links neben dem Namen einer Planungseinheit auf _>_{:.doc-button}, um die Planungseinheit auszuklappen.

Verwende das Suchfeld über der Spalte, um nach bestimmten Mitarbeitern zu suchen. Verwende Kommas, um die Namen voneinander zu trennen, wenn du nach mehreren Mitarbeitern gleichzeitig suchen möchtest. Um die Zeile des Mitarbeiters im Schichtplan anzuzeigen, klappe die Planungseinheit aus, der er zugewiesen ist.

Klicke auf die Spaltenüberschrift, um sie alphabetisch nach Nachnamen zu sortieren. Bewege den Mauszeiger über den Namen eines Mitarbeiters, um ein Popover mit Informationen zu dessen Vertrag und Qualifikationen anzuzeigen. Klicke im Popover auf den Namen des Mitarbeiters in Blau, um das Profil des Mitarbeiters im Bearbeitungsmodus in einem neuen Tab zu öffnen.

> Hinweis
>
> Wenn du ein Eintritts- und ein Austrittsdatum für einen Mitarbeiter konfiguriert hast, wird dieser nur innerhalb des konfigurierten Zeitraums angezeigt.
> Wenn die Planungseinheit eines Mitarbeiters einen konfigurierten Gültigkeitszeitraum hat und seine Zuweisung zur Planungseinheit am selben Tag endet, wird sein Schichtplan nach diesem Tag nicht mehr in Schedules angezeigt. Im Schicht Center kannst du auch nach diesem Tag noch Schichtpläne anzeigen. Die Zellen für Tage nach dem Austrittsdatum des Mitarbeiters sind dann ausgegraut.

### Spalte Ebene

Die Spalte **Ebene** ist die zweite Spalte von links. Um sie aus- oder einzublenden, verwende den Pfeil _<_{:.doc-button} bzw. _>_{:.doc-button} neben dem Suchfeld für den Mitarbeiternamen. Klicke auf das Filter-Icon {% icon filter | icon-only %}, um eine oder mehrere Ebenen auszuwählen und deren Daten in der Tabelle anzuzeigen. Die Ebene Plan ist standardmäßig ausgewählt. In injixo Essential WFM ist nur die Ebene Plan verfügbar.

Wenn du mehr als eine Ebene in der Spalte **Ebene** auswählst und in der Tabelle [zwischen zwei und sieben Tagen anzeigst](#mehrtagesansicht-mit-tagesspalten), zeigt der Spaltenkopf jeder Tagesspalte ein {% icon ellipsis_v %} an, das du anklicken kannst, um zwischen den verschiedenen Ebenen zu wechseln.

### Spalte mit Arbeitszeiten

Die Spalte mit den Arbeitszeiten ist die dritte Spalte von links. Um sie aus- oder einzublenden und zu erweitern, verwende den Pfeil _<_{:.doc-button} bzw. _>_{:.doc-button} rechts oberhalb der Ebenenspalte. Die Spalte mit den Arbeitszeiten setzt sich von links nach rechts aus drei Abschnitten zusammen: Differenz, Ist-Zeit und Soll-Zeit. Diese Abschnitte zeigen die vertraglich erforderlichen und tatsächlich geplanten Arbeitsstunden der Mitarbeiter sowie die Differenz zwischen den beiden Werten.<br>Die Differenz ist wie folgt farblich codiert:

- Rot: Weniger Stunden geplant als vertraglich erforderlich
- Blau: Mehr Stunden geplant als vertraglich erforderlich
- Grau: Genauso viele Stunden geplant wie vertraglich erforderlich

Um die Tabelle nach den Arbeitszeitdaten der Mitarbeiter zu sortieren, klicke im Spaltenkopf für die Arbeitszeiten auf **Differenz** bzw. **Ist-Zeit** oder **Soll-Zeit**.

### Mehrtagesansicht mit Tagesspalten

Verwende die Datumsauswahl rechts über der Tabelle, um den angezeigten Datumsbereich zu ändern. Wenn du mehr als einen einzelnen Tag auswählst, zeigt die Tabelle eine Spalte für jeden Tag im Datumsbereich an, bis zu 32 Tagen. Jede Tageszelle zeigt die Start- und Endzeiten der Schicht eines Mitarbeiters an. Die Farbe entspricht der ersten geplanten Aktivität für den jeweiligen Tag.

Du kannst die Tabellendaten nach der Startzeit der Schichten sortieren. Klicke dazu auf das {% icon ellipsis_v %} im Spaltenkopf einer Tagesspalte. Wähle ggf. die Ebene aus, deren Daten du anzeigen möchtest.

Klicke auf den Spaltenkopf einer Tagesspalte, um zur Tagesansicht mit Stundenspalten zu wechseln.

### Tagesansicht mit Stundenspalten

Wenn du in der Datumsauswahl einen einzelnen Tag auswählst oder auf den Spaltenkopf einer Tagesspalte klickst, zeigt die Tabelle Spalten für jede Stunde des ausgewählten Tages an. Um in dieser Ansicht zwischen mehreren Ebenen zu wechseln oder um die Daten nach der Startzeit der Schichten zu sortieren, klicke auf das {% icon ellipsis_v %} rechts neben der Datumsauswahl und wähle eine neue Ebene bzw. klicke erneut auf eine gewählte Ebene, um die Sortierreihenfolge umzukehren.

Um Daten in 30-Minuten-Intervallen anzuzeigen, bewege den Mauszeiger zwischen zwei Spalten. Wenn das {% icon magnifying_glass %} erscheint, klicke darauf. <br>Um 15-Minuten-Intervalle anzuzeigen, bewege den Mauszeiger auf die 30-Minuten-Marke und klicke auf das dann erscheinende {% icon magnifying_glass %}.<br>Um zur Ansicht mit den Stundenspalten zurückzukehren, klicke auf eine beliebige Stundenmarkierung.

## Aktivitäten-Bereich

Klicke unten links auf _^_{:.doc-button}, um eine Tabelle mit Daten zu Aktivitäten einzublenden. Mit diesen Daten kannst du {% link_new die Besetzung, die Deckung und den Mitarbeiterbedarf analysieren | features/scheduling/schedules/schedules-activity-coverage.md %}.<br>Klicke auf die verschiedenen Tabs, um zwischen ihnen zu wechseln. Klicke in der Spalte **Aktivität** auf das Filter-Icon {% icon filter | icon-only %}, um die Aktivitäten auszuwählen, die du anzeigen möchtest.
