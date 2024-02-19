---
title: Elemente hinzufügen und löschen
product_label:
  - advanced
  - enterprise
  - classic
description: Füge manuell Aktivitäten, Tagesmodelle und andere Elemente in den Schichtplänen Deiner Mitarbeiter im Schicht Center hinzu oder lösche sie.
redirect_from:
  - /de/working-with-availabilities/
  - /de/creating-assignments/
redirect_reason: renamed file in March 2021
---

In diesem Artikel lernst Du:
- wie Du Aktivitäten, Multiaktivitäten, ganztägige Aktivitäten, Tagesmodelle, Verfügbarkeiten und Kommentare in Deinen Schichtplan einfügst.
- wie Du Elemente für mehrere Mitarbeiter auf einmal hinzufügst.
- wie Du Elemente löschst.

Normalerweise erstellst Du einen Schichtplan nicht komplett manuell, da die volloptimierte Planung dies für Dich übernimmt. Aber von Zeit zu Zeit kann es sein, dass Du Deinen Schichtplan bearbeiten musst. Das Schicht Center ermöglicht Dir genau das.

Neu im Schicht Center? Lerne zuerst {% link_new die Grundlagen | features/scheduling/shiftcenter/shift-center-overview.md %}.

## Aktivität hinzufügen

Du kannst eine oder mehrere Aktivitäten für einen Mitarbeiter an einem bestimmten Tag hinzufügen. Du hast folgende Optionen, um den Eingabedialog für Aktivitäten im Planfenster zu öffnen:

* Klicke mit der rechten Maustaste auf eine **Zelle** und klicke im Kontextmenü auf **Aktivität einfügen...**.
* Wähle eine **Zelle** aus und drücke **STRG + N** auf Deiner Tastatur.
* Doppelklicke auf eine **Zelle** und klicke auf den Tab **Aktivitäten**.

Wenn Du das {% link_new Schicht Center mit ActiveX | features/scheduling/shiftcenter/shift-center-overview.md | #zwei-versionen-des-schicht-centers %} unter *WFM > Scheduling > SchedulePro > Schicht Center*{:.breadcrumbs} verwendest, kannst Du zum Umschalten zwischen den Tabs im Eingabedialog auch die Tastenkombinationen **ALT + 1** bis **ALT + 8** verwenden.

Füge eine Aktivität wie folgt im Tab *Aktivitäten* hinzu:  

1. Wähle einen Aktivitätstyp über das Feld **Typ** unten links.
2. Klicke auf *Hinzufügen*{:.doc-button}, um eine neue Aktivität hinzuzufügen. Eine neue Zeile mit der Aktivität erscheint auf der linken Seite. Wenn Du sie wieder löschen möchtest, wähle sie aus und klicke *Löschen*{:.doc-button}.
3. Wähle in der Dropdown-Liste links eine **Aktivität** aus.
4. Definiere eine **Startzeit** und eine **Endzeit**. Klicke auf ein **Zeitfeld**, gib die Zeit ein oder ändere die Zeit mit den Pfeiltasten.
5. Klicke *OK*{:.doc-button}.

{{ 1 | image: 'Aktivitäten hinzufügen', '70%' }}

### Buchungsdatum und *-/0/+*-Spalten

Die Spalte *Buchungsdatum* kannst Du nicht ändern. Verwende **-/0/+**, um anzugeben, ob die Start- oder Endzeit an einem anderen Tag liegt. Behalte **0**, wenn die Start- oder Endzeit am ausgewählten Tag liegt. Klicke auf **-**, wenn die Start- oder Endzeit am vorherigen Tag liegt. Verwende **+**, wenn sie am folgenden Tag liegt.

## Multiaktivität hinzufügen

Du kannst eine Multiaktivität für einen Mitarbeiter an einem bestimmten Tag hinzufügen. Du hast folgende Optionen, um den Eingabedialog für Multiaktivitäten im Planfenster zu öffnen:

* Klicke mit der rechten Maustaste auf eine **Zelle** und klicke im Kontextmenü auf **Multiaktivität einfügen...**.
* Doppelklicke auf eine **Zelle** und klicke auf den Tab **Multiaktivitäten**.

Füge eine Multiaktivität wie folgt über den Tab *Multiaktivitäten* hinzu:  

1. Klicke auf *+*{:.doc-button}, um eine **Kategorie** auf der rechten Seite auszuklappen.
2. Doppelklicke auf eine **Multiaktivität**. Du kannst sie auch auswählen und auf den erscheinenden **kleinen schwarzen Pfeil** auf der rechten Seite klicken. Es erscheint eine neue Zeile mit der Multiaktivität auf der linken Seite. Wenn Du sie wieder löschen möchtest, wähle sie aus und klicke *Löschen*{:.doc-button}.
3. Klicke auf *+*{:.doc-button} in der neuen Zeile, um Details für die Multiaktivität anzuzeigen.
4. Lege eine **Startzeit** und eine **Endzeit** fest. Klicke auf ein **Zeitfeld**, gib die Zeit ein oder ändere die Zeit mit den Pfeiltasten. Verwende **-/0/+**, falls nötig ([siehe oben](#buchungsdatum-und--0-spalten)).
5. Klicke *OK*{:.doc-button}.

{{ 3 | image: 'Dialog: Multiaktivitität hinzufügen', '70%' }}

## Tagesmodell hinzufügen

Du kannst Tagesmodelle für einen Mitarbeiter an einem bestimmten Tag hinzufügen. Du hast folgende Optionen, um den Eingabedialog für Tagesmodelle im Planfenster zu öffnen:

* Klicke mit der rechten Maustaste auf eine **Zelle** und klicke im Kontextmenü auf **Tagesmodell einfügen...**.
* Doppelklicke auf eine **Zelle** und klicke auf den Tab **Tagesmodelle**.

Füge ein Tagesmodell wie folgt über den Tab *Tagesmodelle* hinzu:

1. Du kannst rechts zwischen den Tagesmodellen, die der Planungseinheit (PE) zugeordnet sind, und Tagesmodellen, die dem Mitarbeiter (MA) zugeordnet sind, wählen. Einige Filter wie z.B. *Sortiert nach Name* und *Sortiert nach Zeit* helfen Dir dabei, schnell das richtige Tagesmodell zu finden. Klicke auf *+*{:.doc-button}, um eine Kategorie zu **erweitern**. Die Filter *Unterbesetzte Schichten* und *Erzeugte Schichten* enthalten nur dann Tagesmodelle, wenn Du mit dem {% link_new Schichtwunsch-Verfahren | features/scheduling/shift-bidding.md %} arbeitest.
2. Klicke auf *+*{:.doc-button}, um ein bestimmtes Tagesmodell anzuzeigen.
3. Doppelklicke auf das **Tagesmodell**. Wähle es alternativ aus und klicke rechts daneben auf den erscheinenden **kleinen schwarzen Pfeil**. Eine neue Zeile erscheint auf der linken Seite. Wenn Du sie wieder löschen möchtest, wähle sie aus und klicke *Löschen*{:.doc-button}.
4. Klicke auf *+*{:.doc-button} in der neuen Zeile, um die Details des Tagesmodells anzuzeigen.
5. Wähle eine **Startzeit** (nur für variable Tagesmodelle). Verwende **-/0/+**, falls nötig ([siehe oben](#buchungsdatum-und--0-spalten)).
6. Klicke *OK*{:.doc-button}.

{{ 2 | image: 'Tagesmodell hinzufügen', '70%' }}

## Ganztägige Aktivität hinzufügen

Ganztägige Aktivitäten sind Aktivitäten, für die die Option *Ganztägig erlauben* aktiviert wurde. Du kannst eine ganztägige Aktivität für einen Mitarbeiter für einen oder mehrere Tage hinzufügen. Du hast folgende Optionen, um den Eingabedialog für ganztägige Aktivitäten im Planfenster zu öffnen:

* Klicke mit der rechten Maustaste auf eine **Zelle** und klicke im Kontextmenü auf **Ganztägige Aktivität einfügen...**.
* Doppelklicke auf eine **Zelle** und klicke auf den Tab **Ganztägige Aktivitäten**.

Füge eine ganztägige Aktivität wie folgt über den Tab *Ganztägige Aktivitäten* hinzu:

1. Klicke auf *Hinzufügen*{:.doc-button}. Eine neue Zeile mit der ganztägigen Aktivität erscheint auf der linken Seite. Wenn Du sie wieder löschen möchtest, wähle sie aus und klicke *Löschen*{:.doc-button}.
2. Wähle in der Dropdown-Liste links eine **Aktivität** aus.
3. Lege ein **Startdatum** und ein **Enddatum** fest (maximal ein Jahr).
4. Klicke *OK*{:.doc-button}.

{{ 4 | image: 'Ganztägige Aktivität hinzufügen', '75%'}}

Aktiviere **Alle ganztägigen Aktivitäten des Jahres anzeigen**, um alle ganztägigen Aktivitäten des ausgewählten Mitarbeiters für das Jahr anzuzeigen.

## Verfügbarkeit hinzufügen

Du kannst eine Verfügbarkeit für einen Mitarbeiter an einem bestimmten Tag einfügen. Eine Verfügbarkeit definiert bestimmte Zeitfenster innerhalb eines Tages, in denen ein Mitarbeiter für Schichten oder Aktivitäten zur Verfügung steht. Wenn keine spezifische Verfügbarkeit definiert wurde, wird der Mitarbeiter für den ganzen Tag als *verfügbar* betrachtet.

Da das Hinzufügen einer Verfügbarkeit nur in der Ebene *Verfügbarkeit* möglich ist, musst Du diese Ebene zuerst anzeigen. Klicke auf {% icon shift-center-params | icon-only %} oben links in der Aktionsleiste und wähle die Ebene *Verfügbarkeit*.

{{ 5 | image: 'Verfügbarkeiten im Schicht Center', '80%' }}

Du hast folgende Optionen, um den Eingabedialog für Verfügbarkeiten im Planfenster zu öffnen:

* Klicke mit der rechten Maustaste auf eine **Zelle** in der Ebene *Verfügbarkeit* und klicke auf **Verfügbarkeiten einfügen...** im Kontextmenü.
* Doppelklicke auf eine **Zelle** in der Ebene *Verfügbarkeit* und klicke auf den Tab **Verfügbarkeit**.

Du kannst eine Standard-Verfügbarkeit wie folgt über den Tab *Verfügbarkeit* hinzufügen:

1. Klicke *Hinzufügen*{:.doc-button} unten links, um einen Verfügbarkeitseintrag für diesen Tag zu erzeugen. 
2. Gib oben eine **Startzeit** und **Endzeit** ein und klicke *OK*{:.doc-button}, um diese zu speichern.

Du kannst auch Tagesmodell-Verfügbarkeiten einfügen:

1. Klicke *+*{:.doc-button} im Abschnitt *Sortiert nach Name* oder *Sortiert nach Zeit* auf der rechten Seite. Eine leere Liste bedeutet, dass es keine Tagesmodelle vom Typ *Verfügbarkeitsrahmen* gibt oder sie nicht Deiner Planungseinheit zugeordnet sind. Erfahre wie Du {% link_new Tagesmodell-Verfügbarkeiten erstellst | features/administration/availabilities.md | #tagesmodell-verfügbarkeiten-erstellen %}.
2. Doppelklicke auf ein **Tagesmodell**. Du kannst es auch auswählen und auf den erscheinenden **kleinen schwarzen Pfeil** rechts daneben klicken oder auf *Hinzufügen*{:.doc-button}. Eine neue Zeile erscheint auf der linken Seite. Wenn Du sie wieder löschen möchtest, wähle sie aus und klicke *Löschen*{:.doc-button}.
3. Klicke auf *+*{:.doc-button} in der neuen Zeile, um die Details der Verfügbarkeit anzuzeigen.

    {{ 7 | image: 'Schicht Center Verfügbarkeiten Eingabedialog', '70%' }}

4. Lege ein **Startdatum** und ein **Enddatum** fest. Verwende **-/0/+**, falls nötig ([siehe oben](#buchungsdatum-und--0-spalten)).
5. Klicke *OK*{:.doc-button}.

> Tagesmodelle vom Typ *Verfügbarkeitsrahmen* überschreiben andere Verfügbarkeiten
>  
> Wenn Du Tagesmodelle vom Typ *Verfügbarkeitsrahmen* im Schicht Center oder über die Funktion Schichtfolgen verwendest, überschreiben sie alle Verfügbarkeiten, die in der Mitarbeiterkonfiguration unter *WFM > Administration > Scheduling > Mitarbeiter*{:.breadcrumbs} zugewiesen wurden und auch Verfügbarkeiten, die vom Agenten im Mitarbeiterportal eingetragen wurden.

## Kommentare hinzufügen

Du kannst einen Kommentar mit einer maximalen Länge von 250 Zeichen für jede Tageszelle für jeden Mitarbeiter und in jeder Ebene hinzufügen. Tageszellen mit Kommentaren werden mit einem dicken schwarzen Rand hervorgehoben. Der Kommentar selbst erscheint im Tooltip, der angezeigt wird, wenn Du mit der Maus über die Tageszelle fährst.

Um einen Kommentar hinzuzufügen:

1. Doppelklicke auf eine **Zelle** und wechsle zum Tab **Kommentar**.
2. Gib einen **Kommentar** ein oder ändere einen bestehenden.
3. Klicke *OK*{:.doc-button}.

Hinweis: Du kannst Kommentare nicht kopieren. Aber Du kannst den Tab *Mitarbeiter* im Eingabedialog verwenden, um denselben Kommentar für mehrere Mitarbeiter gleichzeitig einzugeben ([siehe unten](#elemente-für-mehrere-mitarbeiter-auf-einmal-hinzufügen)).

> Kommentare auf der Ebene *Plan* sind für Deine Mitarbeiter innerhalb des Mitarbeiterportals injixo Me sichtbar.

## Elemente für mehrere Mitarbeiter auf einmal hinzufügen

Du kannst identische Elemente (Aktivitäten, Multiaktivitäten, ganztägige Aktivitäten, Tagesmodelle und sogar Kommentare) für mehrere Mitarbeiter gleichzeitig am selben Tag hinzufügen:

1. Doppelklicke auf eine **Tageszelle**.
2. Klicke auf den Tab **Mitarbeiter**.
3. Aktiviere die **Checkboxen** der Mitarbeiter, für die Du das Element hinzufügen möchtest. Wähle *Alle*{:.doc-button} oder *Keine*{:.doc-button}, um alle auszuwählen oder die Auswahl aufzuheben.  
    {{ 11 | image: 'Mitarbeiter auswählen', '75%' }}
4. Klicke auf den **Tab**, in dem Du Daten eingeben möchtest, d.&nbsp;h. auf *Aktivitäten*, *Multiaktivitäten*, *Tagesmodelle*, *Ganztägige Aktivitäten* oder *Kommentare*.
5. Füge die **Elemente** hinzu, die Du zuweisen möchtest.
6. Klicke *OK*{:.doc-button}. Die Elemente werden nun dem Schichtplan jedes ausgewählten Mitarbeiters hinzugefügt.
    {{ 12 | image: 'Vorherigen Planungsstand zurücksetzen', '75%' }}

Hinweis: Du kannst die Option nicht verwenden, um im Tab *Verlauf* frühere Planungsstände für mehrere Mitarbeiter gleichzeitig wiederherzustellen.

> Achte auf Verletzungen der Planungsregeln
>
> Für Benutzer mit *Admin-Zugriff* oder der Rolle *Planer* werden Schichtpläne unabhängig von etwaigen Planungsregelverletzungen aktualisiert. Überprüfe die {% link_new **Meldungsanzeige** | features/scheduling/shiftcenter/shift-center-overview.md | #meldungsanzeige %} am unteren Rand auf Fehler. Für andere Benutzerrollen werden Änderungen, die gegen die Regeln verstoßen, nicht übernommen.

## Elemente löschen

> Daten werden ohne vorherige Bestätigung sofort gelöscht. Den vorherigen Stand kannst Du nur einzeln je Mitarbeiter und Tag im Tab *Verlauf* wiederherstellen.

Um eine *einzelne Aktivität oder ein einzelnes Tagesmodell* zu löschen:

- Klicke mit der rechten Maustaste darauf und wähle **Eintrag löschen**. Du kannst auch auf das Element klicken und **STRG + E** drücken. Oder doppelklicke auf eine Zelle, um den Eingabedialog zu öffnen, wähle die Datenzeile des zu löschenden Eintrags aus und drücke *Löschen*{:.doc-button}.
- Klicke auf die **Tageszelle** und drücke **Entf** oder **STRG + L**.

Um alle Daten für einen *einzelnen Tag* zu löschen:
- Klicke mit der rechten Maustaste auf die Tageszelle und wähle **Alle Einträge löschen**.
- Klicke auf die **Tageszelle** und drücke **Entf** oder **STRG + L**.

Um alle Aktivitäten und Tagesmodelle für *mehrere Tage und Mitarbeiter* auf einmal zu löschen:
  1. Tipp: Konfiguriere die {% link_new Anzeigeparameter | features/scheduling/shiftcenter/shift-center-overview.md | #zeitbereich-und-ebenen-auswählen %} so, dass nur der Zeitraum und die Ebenen angezeigt werden, für die Du Daten löschen möchtest.
  2. Wähle die **Zellen** aus, die Du löschen möchtest.
  3. Klicke mit der rechten Maustaste auf die **ausgewählten Zellen** und wähle **Alle Einträge löschen**. Oder drücke **Entf** oder **STRG + L** auf Deiner Tastatur.
