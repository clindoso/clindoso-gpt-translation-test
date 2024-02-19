---
title: Was ist Schedules?
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Schichten, Aktivitäten und andere Planungselemente wie Urlaubsanträge anzeigen und bearbeiten.
promote-service: team-leader-training
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-activity-coverage.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/schedules/schedules-edit.md
---

Schedules ermöglicht es Dir, Schichten, Aktivitäten und andere Elemente wie z.&nbsp;B. Urlaubswünsche anzuzeigen und zu bearbeiten. Rufe Schedules_ unter _Plan > Schedules_{:.breadcrumbs} auf. Es besteht aus einer Filterleiste, dem Planungsbereich und dem  _Aktivitäten-Panel.

### Filterleiste

In der Filterleiste kannst Du:

* die Planungseinheit(en) und Mitarbeiter auswählen, für die Du den Schichtplan anzeigen möchtest.
* in den *Vollbildmodus* wechseln. <sup>1</sup>
* verschiedene *Planungsaktionen* über das Dropdown-Menü auf der rechten Seite starten.

{{ 2 | image: 'Filterleiste' }}

<sup>1</sup> Klicke auf das _![Vollbildmodus Symbol](/assets/img/common/full-screen-mode.png)_{:.doc-button-icon}-Icon. Wenn Du Dich im Vollbildmodus befindest, bewege den Cursor auf das Pfeil-Symbol am oberen Bildschirmrand, um die Filterleiste erneut anzuzeigen. So kannst Du dann die Planungseinheit, die Auswahl oder den Mitarbeiterfilter ändern, während Du im Vollbildmodus bleibst. Klicke erneut auf das Symbol oder drücke **ESC**, um den Vollbildmodus zu verlassen.

### Planungsaktionen

  - {% link_new Schichtfolgen einfügen | features/scheduling/schedules/schedules-insert-shift-sequences.md %}: füge feste, sich wiederholende Abfolgen von Schichten, Aktivitäten oder Verfügbarkeien in Deinen Schichtplan ein
  - {% link_new Joboptimierung | features/scheduling/schedules/schedules-job-optimization.md %}: ersetze Aktivitäten, um die Deckung zu verbessern
  - {% link_new Pausen optimieren | features/scheduling/schedules/break-optimization.md %}: ordne die Pausenpositionen im Schichtplan neu an, um die Deckung zu verbessern
  - {% link_new Ebenen leeren | features/scheduling/schedules/schedules-empty-levels.md %}: lösche den Inhalt einer Ebene
  - {% link_new Ebeneninhalte kopieren | features/scheduling/schedules/schedules-copy-level-content.md %}: kopiere oder sichere Deinen Schichtplan und anderer Elemente in einer Ebene
  - {% link_new Aktivitäten ersetzen | features/scheduling/schedules/schedules-replace-activities.md %}: ersetze eine Aktivität durch eine andere Aktivität in einem bestehenden Schichtplan

Einige *Planungsaktionen* sind nur in injixo Advanced WFM und Enterprise WFM verfügbar:

  - {% link_new Optimierten Plan erstellen | features/scheduling/schedules/schedules-optimized-schedules.md %}: erstelle automatisch einen Schichtplan mit der bestmöglichen Deckung für alle Aktivitäten
  - {% link_new Extra-Aktivitäten planen | features/scheduling/schedules/schedules-extra-activities.md %}: plane „lagerfähige“ Aktivitäten wie E-Mail und Backoffice, indem Du bestehende Aktivitäten ersetzt

### Planungsbereich

Im Planungsbereich siehst Du Deine Planungseinheiten. Klicke auf eine **Planungseinheit**, um sie aufzuklappen. In der ersten Spalte erscheinen die zugeordneten Mitarbeiter, in der zweiten Spalte die Ebene(n), in der/denen die Planungselemente gespeichert wurden, und in der dritten Spalte die Arbeitszeiten der Mitarbeiter. Klicke auf die **Pfeilsymbole** in den Spaltenüberschriften, um die Spalten auf- oder zuzuklappen.

{{ 8 | image: 'Planungsbereich' }}

Die Arbeitszeiten zeigen die Werte für die *Soll*- und die *Ist*-Arbeitszeit, sowie die *Differenz* zwischen beiden. Ein Farbschema hilft Dir zu erkennen, ob ein Mitarbeiter seine vertraglichen Stunden erreicht hat: Rot (zu wenige Stunden), blau (zu viele Stunden) und grau (korrekte Stundenzahl).

Rechts neben der Spalte Arbeitszeiten befindet sich der Schichtplan der Mitarbeiter:innen. Jede Tageszelle zeigt einen Balken mit der Start- und Endzeit der Schicht. Die Tageszelle hat die Farbe der ersten Tagesaktivität (z. B. Pink für die *Coaching*-Aktivität im Screenshot)

Um einen Schichtplan zu kommentieren, siehe {% link_new Mit Kommentaren arbeiten | features/scheduling/schedules/schedules-comments.md %}

{{ 10 | image: "Wochenansicht mit Popover für Schicht" }}

Ein Klick auf einen **Mitarbeiternamen** öffnet ein Popover mit Vertrags- und Qualifikationsinformationen für diesen Mitarbeiter. Klicke auf den **blauen Mitarbeiternamen** innerhalb des Popovers, um die Mitarbeiterdetails in einem neuen Fenster zu öffnen.

### Aktivitäten-Panel

Die Leiste ganz unten ermöglicht die {% link_new Analyse der Besetzung, der Deckung und des Bedarfs | features/scheduling/schedules/schedules-activity-coverage.md %} für den angezeigten Zeitraum.

{{ 7 | image: 'Aktivitäten-Panel', '80%' }}

## Daten filtern

Das Schedules-Modul erlaubt Dir die Datenfilterung an verschiedenen Stellen. Erfahre unterhalb mehr dazu.

Hinweis: Du kannst einfach die *Zurück*-Funktion des Browsers verwenden, um zur letzten Filterauswahl oder Sortierung zurückzukehren, da das Schedules-Modul mit URL-Parametern zum Filtern und Sortieren arbeitet.

### Nach Planungseinheit

1. Klicke auf *Planungseinheit*{:.doc-button} in der Filterleiste.
2. Aktiviere die **Checkboxen**, um eine oder mehrere **Planungseinheiten** auszuwählen. Du kannst auch im Suchfeld nach einer Planungseinheit filtern oder **Alle Planungseinheiten** ankreuzen.

    {{ 6 | image: 'Filter für Planungseinheiten und Auswahlen', '40%' }}

### Nach Mitarbeitern

* Wähle in der Filterleiste eine **Auswahl**. In injixo Advanced WFM und Enterprise WFM kannst Du auch einen {% link_new Mitarbeiter-Filter | features/administration/employee-filter.md %} auswählen.
* Verwende oben links im Planungsbereich das Feld **Mitarbeiter suchen**, um nach einzelnen Mitarbeitern zu filtern. Du kannst auch nur Teile des Namens eingeben. Trenne mehrere Namen durch Kommas.

### Nach Ebene

In der zweiten Spalte des Planungsbereichs (*Ebene*) ist standardmäßig die Ebene *Plan* ausgewählt. In injixo Advanced WFM und injixo Enterprise WFM kannst Du weitere Ebenen anzeigen, indem Du auf das **Filtersymbol** klickst und **Checkboxen** aktivierst.

{{ 12 | image: 'Filter für Ebenen', '20%' }}

## Daten sortieren

Im Planungsbereich kannst Du nach folgenden Kriterien sortieren:

- *Mitarbeitername*: Sortiere nach dem Mitarbeiternamen in aufsteigender oder absteigender Reihenfolge, indem Du auf die **Spaltenüberschrift** klickst.
- *Arbeitszeiten*: Sortiere nach *Differenz*, *Ist-Zeit* und *Soll-Zeit*, indem Du auf die **Spaltenüberschriften** klickst.
- *Startzeit der Schichten*: Klicke auf die **drei Punkte** in der Spaltenüberschrift eines einzelnen Tages. Die Punkte werden nur angezeigt, wenn Du die Ansicht auf einen Zeitbereich von sieben Tagen oder weniger eingestellt hast. Wähle dann die **Ebene**, innerhalb derer Du sortieren möchtest. In injixo Essential WFM ist nur die Ebene *Plan* verfügbar.  

Um die Sortierung umzukehren, führe die oben beschriebenen Schritte erneut aus.

Hinweis: Wenn Du in der Spalte *Ebene* mehr als eine Ebene ausgewählt hast, wirst Du beim Filtern nach Arbeitszeiten dazu aufgefordert, die **Ebene** nach der Du sortieren möchtest in einem zusätzlichen Schritt anzuklicken.

## Zeitbereich und Zoom-Level anpassen

Im Planungsbereich kannst Du maximal 32 Tage anzeigen und maximal bis auf die 15-Minuten-Intervalle eines Tages hineinzoomen.

### Zeitbereich auswählen

Die Kopfzeile des Planungsbereichs zeigt den ausgewählten Zeitbereich an. Verwende die **Pfeilfelder** rechts und links, um zum vorherigen oder nächsten Zeitraum zu springen.

So wählst Du einen neuen Zeitbereich aus:

1. Klicke in der Mitte auf den **aktuellen Zeitbereich**. Dies öffnet die Zeitbereichsauswahl.
2. Gehe zum Datumsbereich, aus dem Du das Startdatum auswählen möchtest. Klicke auf die **Pfeilsymbole**, die nach links und rechts zeigen oder klicke auf den aktuell **gewählten Monat** bzw. das **gewählte Jahr** und triff eine neue Auswahl.
3. Klicke auf einen Tag, um das **Startdatum** festzulegen.
4. Navigiere zum **Enddatum** und klicke es an.

Um den aktuellen Zeitbereich zu verkürzen oder zu verlängern, klicke auf das aktuelle **Startdatum** oder **Enddatum**, um es abzuwählen. Klicke dann auf ein **anderes Datum**, um dieses auszuwählen.

Um vordefinierte Tages-, Wochen- oder Monatsansichten auszuwählen, nutze die **Quick-Links** auf der linken Seite.

  {{ 4 | image: "Zeitbereichsauswahl mit Quick-Links", '50%' }}

### In die Tagesansicht wechseln

Klicke auf ein beliebiges **Datum** im oberen Teil des Planungsbereichs, um die Details zu einem bestimmten Tag anzuzeigen.

{{ 11 | image: "In die Tagesansicht wechseln", '100%', 'gif' }}

### Hinein- und Herauszoomen in der Tagesansicht

Standardmäßig werden die Daten eines Tages in Ein-Stunden-Intervallen angezeigt. So änderst Du das Intervall in der Zeitleiste:  

1. Fahre in der Kopfzeile der Zeitleiste mit der Maus über den Zwischenraum zwischen den Stunden, bis eine **Lupe** erscheint. Klicke darauf, um hineinzuzoomen und 30-Minuten-Intervalle anzuzeigen.
2. Bewege den Mauszeiger über eine **30** in der Zeitleiste. Es erscheint eine Lupe. Klicke, um weiter hineinzuzoomen und 15-Minuten-Intervalle anzuzeigen.
3. Um wieder eine Ebene herauszuzoomen, klicke auf eine **15**, **30** oder **45**.
4. Um direkt zurück zur Ansicht mit Ein-Stunden-Intervallen zu springen, klicke auf eine **volle Stunde**.

{{ 3 | image: 'Zeitleiste mit angezeigten 30-Minuten-Intervallen' }}

Die gewählte Intervallgröße wird gespeichert und bei der nächsten Anmeldung wiederhergestellt.
