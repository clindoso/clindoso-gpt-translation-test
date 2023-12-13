---
title: Verfügbarkeiten
product_label:
  - advanced
  - enterprise
  - classic
description: Erstelle wiederverwendbare Verfügbarkeiten, um Zeiträume zu definieren, in denen Mitarbeiter geplant werden können.
redirect_from:
  - /de/availabilities/
redirect_reason: rename article September 2022
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/shift-sequences.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/scheduling-methods.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/employee-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/shiftcenter/shift-center-overview.md
---

In diesem Artikel lernst Du: 
- was Verfügbarkeiten sind.
- wie Du Verfügbarkeiten einrichtest.

## Was sind Verfügbarkeiten?

Verwende Verfügbarkeiten, wenn ein Mitarbeiter an einem Tag nicht (oder nur teilweise) verfügbar ist. Mit Verfügbarkeiten kannst Du die Einschränkungen noch weiter eingrenzen, die durch die Öffnungszeiten Deiner Planungseinheit und vertragliche Vorgaben definiert sind.

Nur wenn eine Schicht oder Aktivität in den konfigurierten Zeitraum passt, kann sie in den Schichtplan eingefügt werden. Mitarbeiter ohne Verfügbarkeit gelten innerhalb Deiner Öffnungszeiten als jederzeit verfügbar.  

## Anwendungsfälle

Du kannst Verfügbarkeiten für verschiedene Zwecke nutzen. Die folgenden Anwendungsfälle sind nur Beispiele.

Anwendungsfall                              | Beispiel
------------------------------------- | ----------
Feste Arbeitstage/Zeiten in jeder Woche | Die Mitarbeiter werden aufgrund von Kinderbetreuung nur für Morgenschichten oder früher endende Schichten geplant.
Wochenenden blocken                        | Mitarbeiter werden an Wochenenden nicht geplant. Verfügbarkeiten von einer Minute verhindern die Planung.
Verfügbarkeiten über Wochen hinweg wechseln    | 50 % des Teams arbeiten nur bis 14.00 Uhr, der Rest arbeitet aufgrund des erweiterten telefonischen Supports länger.
Kernarbeitszeiten visualisieren          | Mitarbeiter haben basierend auf ihrem Vertrag eine Verfügbarkeit, die von einer Schichtfolge überschrieben werden kann. 
Zeitweise (nicht) verfügbare Mitarbeiter     | Wenn sich die Verfügbarkeiten der Mitarbeiter vorübergehend ändern, kannst Du diese mit Schichtfolgen überschreiben.  

<!-- just a test if people read carefully :) What do you think? -->
Hast Du andere Anwendungsfälle? Füge einen Kommentar in der Umfrage zu diesem Artikel ein. 

## Auswirkungen auf die Planung

Standardmäßig berücksichtigt injixo Verfügbarkeiten bei der Erstellung von optimierten Schichtplänen. Verfügbarkeiten werden nicht bei der Schichterzeugung geprüft, sondern beim Speichern des Plans während der Verlosung/Zuweisung.

Wenn die Planungsregel *2611*{:.id-label} *Verfügbarkeit des Mitarbeiters* deaktiviert ist, prüft injixo die Verfügbarkeiten nicht.

Tipp: Wenn Du willst, dass Deine Mitarbeiter Schichten wünschen und erhalten können, die länger sind als ihre Verfügbarkeit, kannst Du die Planungsregel deaktivieren.

## Verfügbarkeiten einrichten

Es gibt zwei Wege, Verfügbarkeiten einzurichten: 

Name                     | Details
------------------------ | -------
Mitarbeiter-Verfügbarkeiten  | Konfiguriere in der Mitarbeiterkonfiguration temporäre oder permanente Verfügbarkeiten für einzelne Mitarbeiter.
Tagesmodell-Verfügbarkeiten | Füge Verfügbarkeiten zu Schichtfolgen hinzu, um mehreren Mitarbeitern die gleiche Verfügbarkeit zu geben. 

Hinweis: Tagesmodell-Verfügbarkeiten überschreiben sowohl Mitarbeiter-Verfügbarkeiten als auch manuell eingefügte Verfügbarkeiten. 

Wenn Du es erlaubst, können Mitarbeiter im Mitarbeiterportal {% link_new ihre eigenen Verfügbarkeiten eintragen | features/injixo-me/use-injixo-me/explore-injixo-me.md | #verfügbarkeit-einrichten %}. Die Verfügbarkeiten werden als Mitarbeiter-Verfügbarkeiten hinzugefügt (maximal 14). Mitarbeiter oder Planer müssen regelmäßig alle veralteten Einträge aus der Liste löschen. Da diese Funktion keinen automatischen Überprüfungsprozess beinhaltet, solltest Du diese Verfügbarkeiten vor der Erstellung des Schichtplans manuell prüfen, um Planungsfehler zu vermeiden.  

### Tipps zum Einrichten von Zeiträumen

Du kannst die genauen Arbeitszeiten Deiner Mitarbeiter abbilden, zum Beispiel von 8 bis 17 Uhr. 

Um flexibler zu sein, kannst Du den Zeitraum der Verfügbarkeiten (Anfangs- oder Endzeit), z. B. auf die Öffnungszeiten Deiner Planungseinheit erweitern:
- 0 Uhr - 20 Uhr: Mitarbeiter können bis 20 Uhr arbeiten.
- 16 Uhr - 0 Uhr Mitarbeiter können nicht vor 16 Uhr beginnen.

Um Mitarbeiter an bestimmten Wochentagen von der Planung auszuschließen, plane für sie Verfügbarkeiten von einer Minute, z. B. in der Zeit von 00:00 bis 00:01 Uhr. 

### Mitarbeiter-Verfügbarkeiten erstellen

In der Mitarbeiterkonfiguration kannst Du temporäre oder dauerhafte Verfügbarkeiten für einzelne Mitarbeiter hinzufügen. Es gibt keine Möglichkeit, Mitarbeiter-Verfügbarkeiten mehreren Mitarbeitern gleichzeitig zuzuweisen. Verwende stattdessen Tagesmodell-Verfügbarkeiten in Schichtfolgen.

1. Gehe zu *WFM > Administration > Scheduling > Mitarbeiter*{:.breadcrumbs}.
2. Klicke auf einen **Mitarbeiter** in der Liste. 
3. Scrolle zum Abschnitt *Verfügbarkeit* auf der rechten Seite (oder verwende den Quicklink *Verfügbarkeit* oben).
4. Klicke _![Plus-Button](/assets/img/common/item-add.gif)_{:.doc-button-icon}, um eine neue Verfügbarkeit hinzuzufügen.
5. (Optional) Füge ein **Gültig von** und **Gültig bis** Datum hinzu. Wenn die Verfügbarkeit nur für einen bestimmten Zeitraum gilt, schränkt dies den {% link_new Gültigkeitszeitraum | features/administration/set-a-validity-period.md %} ein.
6. Um den Wochentag zu definieren, wähle einen oder mehrere **Tagestypen** aus. Halte STRG gedrückt, um mehrere Einträge auszuwählen.  
7. Gib eine Startzeit in das **Von** Feld und eine Endzeit in das **Bis** Feld ein. Die Zeiten sind für alle ausgewählten Tage gültig.
8. (Optional) Wenn der Zeitraum über Mitternacht hinausgeht, z. B. bei Nachtschichten, aktiviere **Verfügbarkeitsrahmen endet am nächsten Tag**.
9. Klicke *OK*{:.doc-button}.

Die neue Mitarbeiter-Verfügbarkeit ist nun aktiv.  


### Tagesmodell-Verfügbarkeiten erstellen

Du kannst Tagesmodell-Verfügbarkeiten erstellen und diese manuell oder in Schichtfolgen einfügen:

1. Gehe zu *WFM > Administration > Scheduling > Tagesmodelle*{:.breadcrumbs}.
2. Wähle den Typ *Verfügbarkeitsrahmen*.
3. Gib einen eindeutigen **Namen** und eine **Kurzbezeichnung**, z. B. *Verfügbarkeit 8:30 - 19:00* und *Verfügbar 830-1900*.
4. (Optional) Wähle eine **Farbe**. Die Farbe kann hilfreich sein, z. B. beim Einrichten von Schichtfolgen.
5. Gib den **Verfügbarkeitsrahmen Beginn** ein. Dies ist der frühestmögliche Zeitpunkt für die Schicht.
6. Gib das **Verfügbarkeitsrahmen Ende** ein. Dies ist der letztmögliche Zeitpunkt für die Schicht. Lege alternativ eine **Verfügbarkeitsrahmen Dauer** fest. Der Maximalwert ist 48 Stunden.
7. Klicke *OK*{:.doc-button}.  

Du kannst das neue Tagesmodell nun manuell im Schicht Center oder in {% link_new Schichtfolgen | features/administration/shift-sequences.md | #tagesmodelle-einfügen %} einfügen. 

## Verfügbarkeiten im Schicht Center/Schedules

Das Schicht Center zeigt Verfügbarkeiten in jeder Ebene als `<>` Symbol an. Bewege den Mauszeiger über das Symbol, um einen Tooltip mit den Details anzuzeigen.

In der Ebene *Verfügbarkeit* kannst Du {% link_new Verfügbarkeiten hinzufügen | features/scheduling/shiftcenter/add-and-delete-items.md | #verfügbarkeit-hinzufügen %}. In den Tageszellen siehst Du alle Verfügbarkeiten als orangefarbene Elemente. In ausgeklappten Tageszellen erscheinen Mitarbeiter-Verfügbarkeiten als weiße Balken, die orange unterstrichen sind.

Hinweis: Um die `<>` Symbole in injixo Enterprise WFM on-premise anzuzeigen, aktiviere Einstellung *48188*{:.id-label} *Anzeige von Verfügbarkeitsinformationen im Schicht Center*. 

Das Schedules Feature kann Verfügbarkeiten nur als Aktivität *Anwesend* anzeigen. Es gibt keine Option zum Bearbeiten.

## Verfügbarkeiten bearbeiten und löschen

Du kannst die Startzeit, die Endzeit oder die Position von manuell eingefügten Verfügbarkeiten in der Ebene *Verfügbarkeit* im Schicht Center ändern (oder sie löschen). Um das Dialogfenster zu öffnen, doppelklicke auf eine **Tageszelle**. Du kannst auch die Maus verwenden, um einen Eintrag zu ändern. 

Erfahre mehr darüber {% link_new wie Du Elemente im Schicht Center änderst | features/scheduling/shiftcenter/modify-items.md %}.

Tipp: Für temporäre Änderungen kannst Du Mitarbeiter- und Tagesmodell-Verfügbarkeiten in eine andere (oder dieselbe) Zelle kopieren, um sie in manuell eingefügte Verfügbarkeiten umzuwandeln. 

Für dauerhafte Änderungen bearbeite die Schichtfolge. Um Tagesmodell-Verfügbarkeiten aus Schichtfolgen zu löschen, kannst Du auch das Feature {% link_new Ebenen leeren | features/scheduling/schedules/schedules-empty-levels.md %}verwenden. Mitarbeiter-Verfügbarkeiten findest Du in der {% link_new Mitarbeiterkonfiguration | features/administration/employee-overview.md | #mitarbeitereinstellungen-konfigurieren %} im Abschnitt *Verfügbarkeit*. Anstatt den Verfügbarkeitseintrag zu löschen, kannst Du die Zuordnung auch durch Hinzufügen eines Gültig-bis-Datums beenden.
