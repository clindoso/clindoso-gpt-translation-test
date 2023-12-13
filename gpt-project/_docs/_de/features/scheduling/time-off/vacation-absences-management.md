---
title: Urlaub- und Abwesenheiten genehmigen und ablehnen
redirect_from:
  - /de/scheduling-vacation-absences-management-new/
  - /de/scheduling-vacation-absences-management/
redirect_reason: Modules in WFM section link to the article
description: Genehmige ausstehende Urlaubs-/und Abwesenheitsanträge oder lehne sie ab. Lerne, wie injixo Dir vorschlägt, welche Anträge Du nach Deinen Vorgaben genehmigen kannst.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-entitlement.md
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md
---

In diesem Artikel lernst Du:
- wie Du Urlaubsanträge einsiehst, genehmigst und ablehnst.
- wie Du automatische Genehmigungsvorschläge erhältst.

Das Modul *Urlaub/Abwesenheiten* bietet einen Überblick über alle Abwesenheits- und Urlaubsanträge, die Mitarbeiter im Mitarbeiterportal eingeben.

Benutzer mit den Rollen *Planer* oder *Supervisor (erweitert)* können Anträge annehmen oder ablehnen und automatische Vorschläge für Genehmigungen auf Basis von Regeln und Quoten erhalten (nicht verfügbar für injixo Essential WFM). Benutzer mit der Rolle *Supervisor (eingeschränkt)* können nur Anträge einsehen.

## Die Ansicht filtern

Schränke die angezeigten Urlaubsanträge mithilfe der Filterleiste ein.

1. Gehe zu *Plan > Urlaub/Abwesenheiten*{:.breadcrumbs}
2. Wähle eine **Planungseinheit** und/oder eine **Auswahl**.
3. Wähle einen **Status**. Wähle zwischen *Alle*, *Offen*, *Abgelehnt*, *Genehmigt* und Kombinationen.
4. Klicke **Startdatum - Enddatum** und wähle einen oder mehrere Tage.
5. Klicke *Filter anwenden*{:.doc-button}, um die Urlaubs- und Abwesenheitsanträge für den gewählten Zeitraum zu laden.

{{ 1 | image: "Filter-Optionen",'80%' }}

## Die Mitarbeiterliste durchsuchen und sortieren

Um die Mitarbeiterliste zu filtern, gib eine Aktivität oder den Namen eines Mitarbeiters in das Feld **Suchen nach Name oder Aktivität** unterhalb der Filterleiste ein.

Um die Tabelle nach *Status*, *Erstellungszeitpunkt*, *Name*, *Start*, *Ende* oder *Aktivität* zu sortieren, klicke auf eine **Spaltenüberschrift**. Pfeile nach oben oder unten zeigen die Sortierreihenfolge an, ein weiterer Klick kehrt diese um.

Die nicht sortierbaren Spalten *Bewilligte Tage* (BT) und *Verfügbare Tage* (VT) zeigen die genommenen und verbleibenden Urlaubstage der Mitarbeiter basierend auf dem {% link_new Urlaubsanspruch | features/scheduling/time-off/vacation-entitlement.md %}.

{{ 2 | image: 'Mitarbeitertabelle mit genehmigten oder abgelehnten Anträgen' }}

### Wann wurde der Antrag erstellt?

Jeder Eintrag, der nach dem 2. November 14:30 Uhr (UTC) über injixo Me eingereicht wurde, hat einen Zeitstempel mit dem Zeitpunkt der Erstellung. Fahre mit der Maus über die Zelle, um nicht nur das Datum, sondern auch die Uhrzeit zu sehen.

Alle älteren (oder über das Schicht Center erstellten) Anträge, zeigen stattdessen *unbekannt* an. Intern ist die Spalte immer noch nach der Antrags-ID geordnet; fahre mit dem Mauszeiger über den Eintrag *unbekannt*, um die ID zu sehen.

## Anträge genehmigen oder ablehnen

Bevor Du Dich entscheidest, einen Antrag zu genehmigen oder abzulehnen, kannst Du auf die **Zelle** in der Spalte *Start* oder *Ende* eines Eintrags klicken, um die Quoten für diesen Tag unten rechts im Kalender zu prüfen.

1. Klicke auf **✓**, um den Eintrag zu genehmigen oder **✗**, um ihn abzulehnen. Klicke erneut, um die Auswahl des Eintrags wieder aufzuheben. Klicke oben auf _Alle als genehmigt markieren_{:.doc-button} oder _Alle als abgelehnt markieren_{:.doc-button}, um alle Einträge auf einmal auszuwählen.

    {{ 3 | image: 'An- und Abwählen von Anträgen', '200', 'gif' }}

2. Klicke auf *Änderungen anwenden*{:.doc-button}.
3. Optional: Gib einen **Kommentar für Genehmigungen** oder für **Kommentar für Ablehnung** ein. Hinweis: injixo benachrichtigt die Mitarbeiter per E-Mail und fügt den eingegebenen Kommentar hinzu. Wenn Du mehrere Anträge auf einmal bearbeitest, sieht jeder Mitarbeiter denselben Kommentar.
4. Klicke auf *Genehmige Anfrage*{:.doc-button} oder *Anfrage ablehnen*{:.doc-button}. Der Name des Buttons spiegelt die Anzahl der ausgewählten Einträge wider. Standardmäßig prüft injixo, ob der Antrag gegen Regeln verstößt, z.B. ob noch genügend Urlaubsanspruch vorhanden ist.

Hinweis: Schalte **Genehmigungsregeln umgehen** ein, um die Genehmigung/Ablehnung von Anträgen zu erzwingen. Bei einem Fehler wird ein roter Banner mit der Antrags-ID angezeigt; klicke erneut auf die Schaltfläche _Anträge ablehnen_{:.doc-button}, um alle noch ausgewählten Ablehnungen abzuwählen.

### Die Zeilen *Genutzte Quote* und die *Angestrebte Quote* verstehen

Die Fußzeile der Kalenderansicht zeigt zwei Zeilen mit wöchentlichen Kontingenten:

- **Genutzte Quote**: Anzahl oder Prozentsatz der Mitarbeiter mit genehmigtem Urlaub an diesem Tag. Die **Genutzte Quote** umfasst alle Aktivitäten des Typs Urlaub, Abwesenheit und Krankheit, die als **Wünschbar in Me** ausgezeichnet sind.
- **Angestrebte Quote**: In der {% link_new Basisquoten-Konfiguration | features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md | #3-basisquote %} konfiguriertes Zielkontingent für den Tag als Zahl oder Prozentwert.

Verwende die Optionsfelder auf der linken Seite, um zwischen *Prozentsatz* und *Anzahl der Vollzeitbeschäftigten*/*Anzahl der Beschäftigten* (je nach Konfiguration der Basisquote) zu wechseln und die Werte umzurechnen.
Wenn Du mit der Maus über eine Zelle fährst, wird ein Tooltip mit der Anzahl der Mitarbeiter und der Anzahl der ausstehenden Anträge angezeigt.

Wenn *Vollzeitäquivalent* konfiguriert ist, spiegeln die Werte die Dauer eines Antrags im Verhältnis zu einem Vollzeitmitarbeiter wider. Ohne *Vollzeitäquivalent* wird jeder Antrag gleich gezählt, unabhängig von seiner Länge.

## Genehmigungsvorschläge erhalten

injixo kann Anträge zur Genehmigung vorschlagen. Automatische Genehmigungen berücksichtigen die Anzahl der Mitarbeiter in der Planungseinheit, der Mitarbeiterbedarf, geplante Abwesenheiten und die angestrebte Quote. Lerne, wie Du {% link_new Genehmigungsregeln und Quoteneinstellungen konfigurierst | features/scheduling/time-off/vacation-approval-rules-and-quota-settings.md %}.

1. Klicke auf _Genehmigungen vorschlagen_{:.doc-button} um potenzielle Anträge für die Genehmigung anzuzeigen. Das Verfahren behandelt ältere Anträge mit einer höheren Priorität ("Wer zuerst kommt, mahlt zuerst"). Das Ergebnis siehst Du nach einer kurzen Ladezeit mit der Anzeige *Vorschläge laden*.
2. Vorgeschlagene Genehmigungen erscheinen in grün. Du kannst mit dem **✗** Symbol immer noch Einträge abwählen.
3. Klicke auf _Genehmige n Anträge_{:.doc-button}. Der Name des Buttons zeigt die Anzahl der ausgewählten Einträge (n).
4. Optional: Gib einen **Kommentar für Genehmigungen** oder **Kommentar für Ablehnung** ein.
5. Klicke auf _Genehmige n Anträge_{:.doc-button}.

Hinweis: Du kannst nicht auf _Genehmigungen vorschlagen_{:.doc-button} klicken, wenn Du:
- gerade in der Liste der Anträge suchst.
- keine Planungseinheit oder keine Anträge zur Genehmigung/Ablehnung ausgewählt hast.

> E-Mail-Benachrichtigungen  
>  
> injixo sendet immer E-Mail-Benachrichtigungen in allen Cloud-Versionen. Du kannst sie nicht deaktivieren. injixo Enterprise On-Premise sendet E-Mail-Benachrichtigungen, wenn das Feld *E-Mail 1* für den/die Mitarbeiter konfiguriert ist.  
