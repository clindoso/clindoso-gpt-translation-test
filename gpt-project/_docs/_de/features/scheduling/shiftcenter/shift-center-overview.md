---
title: Was ist das Schicht Center?
product_label:
  - advanced
  - enterprise
  - classic
description: Lerne, wofür Du das Schicht Center verwendest und wie Du die Darstellung von Daten anpassen kannst.
---

In diesem Artikel lernst Du:
- was das Schicht Center ist und wofür es verwendet wird.
- wie die drei Bereiche des Schicht Centers aufgebaut sind und wofür sie verwendet werden.
- wie Du die Darstellung von Daten anpasst.
- wie Du Schichtpläne als Excel-Datei herunterlädst.

## Was ist das Schicht Center?

Das Schicht Center ist der zentrale Ort, um die von den automatischen Planungsprozessen erzeugten Schichtpläne einzusehen und manuell zu bearbeiten.

Du kannst das Schicht Center verwenden, um:
- Aktivitäten, Tagesmodelle und Mitarbeiterverfügbarkeiten hinzuzufügen, zu bearbeiten und zu verschieben.
- Deckung, Bedarf und Besetzung basierend auf Aktivitäten und Tagesmodellen zu analysieren.
- Ersatzmitarbeiter für Aktivitäten und Schichten zu finden.
- Mitarbeiterbedarfe und erzeugte Schichten zu bearbeiten.

### Zwei Versionen des Schicht Centers

In injixo Advanced und injixo Enterprise WFM erreichst Du das Schicht Center unter *Plan > Schicht Center*{:.breadcrumbs}. Diese ActiveX-freie Version ist mit allen unterstützten Browsern nutzbar.

In injixo Classic und injixo Enterprise WFM on-premise ist das Schicht Center unter *WFM > Scheduling > SchedulePro > Schicht Center*{:.breadcrumbs} verfügbar. Diese ActiveX-basierte Version funktioniert nur im Microsoft Internet Explorer und Edge.

Die beiden Versionen des Schicht Centers unterscheiden sich. Die Artikel erläutern die kleinen Unterschiede für jeden Anwendungsfall.

> On-premise: injixo build 10995 führt das Schicht Center als Windows-Anwendung ein
>  
> Um die neue Version zu nutzen, installiere Build 10995 auf dem Server und allen Client-Workstations. injixo greift auf die eingebettete Version zurück, wenn entweder die Clients oder der Server nicht Build 10995 verwenden.
>
> Die Windows-Anwendung behebt Abstürze, die beim Kopieren und Einfügen von Elementen in Microsoft Edge auftreten. Lerne mehr über die [geänderte Handhabung](#on-premise-schicht-center-als-windows-anwendung).

## Zeitbereich und Ebene(n) auswählen

1. Klicke auf *Ebenen*{:.doc-button} in der Filterleiste.
2. Wähle eine oder mehrere **{% link_new Ebenen | best-practices/tips-on-shift-center-usage.md | #tipp-9-arbeiten-mit-verschiedenen-ebenen %}** aus, für die Du Daten anzeigen möchtest.
3. Klicke auf den **Datums-Button** und wähle das Datum aus, ab dem du Daten anzeigen lassen möchtest.
4. Wähle eine **Zeiteinheit**, indem Du *Tage*, *Wochen*, *Monate* oder *Jahre* aus dem Dropdown-Menü auswählst.
5. Wähle eine **Zahl**, um anzugeben, wie viele Tage, Wochen, Monate oder Jahre Du anzeigen möchtest. Du kannst Daten für bis zu 500 Tage, 105 Wochen, 24 Monate oder 2 Jahre anzeigen lassen. Wenn Du z. B. *Monate* als Zeiteinheit für den Zeitraum und *2* für die Dauer auswählst, zeigt der Schichtplan 2 Monate an, beginnend mit dem Startdatum, das Du zuvor definiert hast.
6. Klicke auf *Anwenden*{:.doc-button}.

    {{ 13 | image: 'Filterleiste im Schicht Center'}}

Wenn Du das {% link_new Schicht Center mit ActiveX | features/scheduling/shiftcenter/shift-center-overview.md | #zwei-versionen-des-schicht-centers %} unter *WFM > Scheduling > SchedulePro > Schicht Center*{:.breadcrumbs} verwendest, befolge diese Schritte:

1. Klicke auf {% icon shift-center-params | icon-only %} oben links in der Aktionsleiste.
2. Wähle für **Startdatum** das Datum aus, ab dem Du Daten anzeigen möchtest.
3. Bei **Zeiteinheit des Zeitraums** und **Dauer des Zeitraums** gibst Du den Datumsbereich an, den Du einblenden möchtest.
4. Wähle eine oder mehrere **{% link_new Ebenen | best-practices/tips-on-shift-center-usage.md | #tipp-9-arbeiten-mit-verschiedenen-ebenen %}** aus, von denen Du Daten anzeigen willst. Markiere dazu die Ebene(n) links und klicke auf die Pfeile, um sie nach rechts zu verschieben. Nutze alternativ einen **Doppelklick**.
5. Klicke auf *Ok*{:.doc-button}.

    {{ 14 | image: 'Aktionsleiste im Schicht Center'}}

## Planfenster

Das Planfenster ist der obere Teil des Bildschirms unterhalb der Aktionsleiste. Es zeigt (abhängig von Deinen Benutzerrechten) eine oder mehrere Planungseinheiten an. Klicke auf *+*{:.doc-button}, um eine Planungseinheit aufzuklappen.

Du siehst nun alle Mitarbeiter, die der Planungseinheit zugeordnet sind, ihre Personalnummern, die Ebene(n) und die Schichtpläne der Mitarbeiter. Du siehst außerdem weiter rechts die vertragliche Soll-Arbeitszeit, die tatsächlich geplante Ist-Zeit und die Zeitdifferenz zwischen beiden.

Wenn einem Mitarbeiter Elemente im Schichtplan zugeordnet sind, zeigt jede Tageszelle standardmäßig einen farbigen Balken mit der Abkürzung des ersten Elements des Tages.

Ein grauer Hintergrund ohne Daten markiert Tage, für die keine Öffnungszeiten konfiguriert wurden. Grau dargestellte Tagesmodelle oder Aktivitäten erscheinen, wenn Mitarbeitern eine zweite Planungseinheit haben, in der aber nicht die Planung stattfindet.

{{ 1 | image: 'Planfenster im Schicht Center'}}

> Arbeitszeitwerte aktualisieren (in oranger Farbe)
>
> Immer wenn sich Dein Schichtplan ändert, färbt sich die Ist-Zeit und die Differenz zwischen der Ist-Zeit und der vertraglichen Soll-Zeit orange. Dies zeigt an, dass eine manuelle Aktualisierung erforderlich ist:
> * Um eine einzelne Planungseinheit zu aktualisieren, klicke auf {% icon shift-center-update-working-times | icon-only %} neben dem Namen der Planungseinheit.
> * Um alle Planungseinheiten auf einmal zu aktualisieren, klicke auf die Spaltenüberschrift **Planungseinheiten**.

### Tatsächliche Arbeitszeiten, Start-/Endzeiten oder Zeitwirtschaftskonten anzeigen

Um statt der Abkürzung des ersten Elements die tatsächlichen Arbeitsstunden, die Start- oder Endzeit oder das Zeitkonto <!-- link --> anzuzeigen, klicke mit der rechten Maustaste auf die **Zelle eines Tages**, wähle **Darstellung** und dann eine der angezeigten **Optionen**.

{{ 5 | image: 'Kontextmenü mit Menüpunkt Darstellung', '50%' }}

In injixo Enterprise WFM kannst Du ein oder mehrere Zeitwirtschaftskonten anzeigen, indem Du Einstellung *48478*{:.id-label} *Anzeige der Spalten mit Zeitwirtschaftskonten* aktivierst.

Um bestimmte Zeitwirtschaftskonten auszuwählen, klicke auf *Kontensalden*{:.doc-button} in der Filterleiste von *Plan > Schicht Center*{:.breadcrumbs} oder auf _![Kontosalden](/assets/img/de/features/shift-center-overview/account-balances.png)_{:.doc-button-icon} in *WFM > Scheduling > SchedulePro > Schicht Center*{:.breadcrumbs}.

## Kennzahlenfenster

Das Kennzahlenfenster zeigt Kennzahlen wie Bedarf, Besetzung und Deckung an, basierend auf den Elementen im Planfenster. Du kannst aggregierte Werte für den Tag anzeigen lassen oder bis auf Intervall-Ebene hineinzoomen.

Die *Farbcodierung* der Werte zeigt an, wie gut der Mitarbeiterbedarf gedeckt ist. Rot zeigt eine Unterdeckung, blau eine Überdeckung und grün signalisiert eine ideale Deckung. Je intensiver die Farbe, desto größer ist die Abweichung von der idealen Besetzung.

Am unteren Bildschirmrand gibt es *drei Tabs*, die Kennzahlen zu den verschiedenen Elementen Deiner Planungseinheit zeigen:

- **Tagesmodelle**: Kennzahlen für alle Tagesmodelle
- **Aktivitäten**: Kennzahlen für alle Aktivitäten
- **Aktivitätsübersicht**: Vertikale Darstellung von Kennzahlen für eine Aktivität, Kennzahl und Ebene.

Im Kennzahlenfenster kannst Du (je nach Tab) über das Kontextmenü auch Deinen Mitarbeiterbedarf für einen einzelnen Tag oder die erzeugten Schichten bearbeiten und Ersatzmitarbeiter für eine Schicht finden.

{{ 2 | image: 'Kennzahlen Fenster im Schicht Center'}}

## Meldungsanzeige

Die Meldungsanzeige ist das Fenster am unteren Rand. Benutze das Tastaturkürzel **STRG + K** um die Meldungsanzeige ein- oder auszublenden. Sie zeigt Planungsregel-Verstöße für Regeln an, die als weiche Regeln konfiguriert sind (gelber Status).

{{ 6 | image: 'Meldungsanzeige im Schicht Center' }}

Um eine Nachricht zu löschen, klicke sie an und drücke **Entf** auf Deiner Tastatur. Um alle Nachrichten zu löschen, klicke auf einen Eintrag, drücke **STRG + A**, um alle Einträge auszuwählen, und drücke **Entf**.

## Die Darstellung von Daten anpassen

Im Planfenster, dem Kennzahlenfenster und der Meldungsanzeige ist es möglich, die Anzeige der Daten individuell anzupassen, um einen besseren Überblick zu bekommen oder um bestimmte Details genauer zu betrachten.

### Größe der Bereiche anpassen

Um die Größe eines Bereichs zu ändern, fahre mit der Maus über den grauen Balken, der das Plan- und das Kennzahlenfenster bzw. das Kennzahlenfenster und die Meldungsanzeige trennt. Der Mauszeiger ändert sich. Klicke und ziehe dann das Fenster nach oben oder unten.

{{ 7 | image: 'Demo Bereiche ändern', '85%', 'gif' }}

### Tagesdetails anzeigen

Klicke auf die **Spaltenüberschrift eines Tages**, um den Tag aufzuklappen und die Details des Tages anzuzeigen. Um den Tag wieder einzuklappen, klicke erneut auf die Spaltenüberschrift. Standardmäßig zeigt ein Tag 24 Stunden an.

{{ 3 | image: 'Ausgeklappter Tag im Schicht Center' }}

Um etwas Platz auf dem Bildschirm zu sparen, kannst Du den Zeitraum auf Deine Öffnungszeiten begrenzen. Gehe zu *WFM > Administration > System > Einstellungen*{:.breadcrumbs} und konfiguriere die Einstellungen *48077*{:.id-label} und *48078*{:.id-label} neu. Lege dort Werte für den Start und das Ende des Anzeige-Zeitraums fest.

### Ein- und Auszoomen

Sowohl im Planfenster als auch im Kennzahlenfenster kannst Du die Auflösung der Zeitskala verändern, um z.B. Werte bis hin zu 15 Minuten-Intervallen zu sehen. Zum Vergrößern und Verkleinern klickst Du auf die **kleinen Pfeiltasten**, die nach rechts und links zeigen.

{{ 4 | image: 'Zeitskala', '50%' }}

## Wie werden Elemente angezeigt?

Du kannst verschiedene Elemente und Zustände anhand von speziellen Markierungen erkennen, wie z. B. Punkten und (gestrichelten) Linien:

- **Aktivität**: Einfacher Balken mit einem oder mehreren Elementen

    {{ 8 | image: 'Aktivität im Planfenster', '50%' }}

- **Tagesmodell**: Balken mit einer schwarzen Linie am unteren Rand. Kleine Punkte am oberen Rand heben bewegliche Korridor-Elemente hervor.

    {{ 9 | image: 'Tagesmodell im Planfenster', '50%' }}

- **Variables Tagesmodell**: Balken mit Punkten am unteren Rand vor der Schicht. Die Punkte zeigen mögliche Schichtpositionen an.

    {{ 10 | image: 'Variables Tagesmodell im Planfenster', '50%' }}

- **Gelöschtes Tagesmodell**: Balken mit großen schwarzen Punkten am unteren Rand

    {{ 11 | image: 'Gelöschtes Tagesmodell im Planfenster', '50%' }}

- **Gelöschte Aktivität**: Balken mit einer gestrichelten Umrandung

    {{ 12 | image: 'Gelöschte Aktivität im Planfenster', '50%' }}

## Schichtpläne als Excel-Datei herunterladen

Das Schicht Center unter *Plan > Schicht Center*{:.breadcrumbs} unterstützt keinen Datenexport nach Excel.

Im {% link_new Schicht Center mit ActiveX | features/scheduling/shiftcenter/shift-center-overview.md | #zwei-versionen-des-schicht-centers %} unter *WFM > Scheduling > SchedulePro > Schicht Center*{:.breadcrumbs} kannst Du den Schichtplan für den aktuell angezeigten Zeitraum und die angezeigten Ebenen als Excel-Datei exportieren. Klicke hierfür auf {% icon shift-center-excel-export | icon-only %} in der Aktionsleiste.

## On-premise: Schicht Center als Windows-Anwendung

Die Schicht Center Windows-Anwendung ersetzt die bisherige eingebettete Version. Sie benötigt auch den Microsoft Internet Explorer oder Microsoft Edge; installiere Build 10995 auf Server und Clients, um sie zu aktivieren.

Klicke auf ein Symbol in der Aktionsleiste, um ein Schicht Center in einem neuen Fenster öffnen:

- {% icon item-add | icon-only %}: Starte eine neue Instanz des Schicht Centers mit Deiner bisher konfigurierten Ansicht (Startdatum, Ebenen, Zeitraum).
- {% icon shift-center-params | icon-only %}: Starte eine neue Instanz des Schicht Centers mit geänderten Parametern (Startdatum, Ebenen, Zeitraum). Dies setzt Deine bisher konfigurierte Ansicht im neuen Fenster zurück.

Abhängig von Deinen Benutzerrechten enthält die Aktionsleiste zusätzliche Symbole:
- {% icon shift-center-time-accounts-balances | icon-only %}: Starte eine neue Instanz, die Deine bisherige Ansicht zurücksetzt, mit der zusätzlichen Spalte *Kontosalden*, die bestimmte Zeitwirtschaftskonten anzeigt.
- {% icon shift-center-autoscheduler | icon-only %}: Starte den AutoScheduler in einem eigenen Fenster.
- {% icon shift-center-job-optimization | icon-only %}: Starte eine Joboptimierung in einem eigenen Fenster.
- {% icon shift-center-break-optimization | icon-only %}: Starte eine Pausenoptimierung in einem eigenen Fenster.

Hinweis: Die folgenden Symbole wurden von der Aktionsleiste in die Anwendung selbst verschoben:
- Das Symbol für den Export nach Excel
- Das Symbol zur Änderung einer Auswahl
- Das Symbol zum Ändern der Mitarbeiterfilter
- Das Dropdown-Menü zur Auswahl der Auswahl/Filter

Die Aktionsleiste verweist nicht mehr auf die Seite zur Erstellung von Mitarbeiterfiltern. Gehe zu *Administration > Scheduling > Mitarbeiter*{:.breadcrumbs}, um Mitarbeiterfilter zu erstellen oder zu bearbeiten.
