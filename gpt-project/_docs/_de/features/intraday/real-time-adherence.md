---
title: Echtzeit Adherence-Feature verwenden
toc: true
product_label:
  - advanced
  - enterprise
description: Verschaffe Dir in Echtzeit einen Überblick darüber, wie genau sich Deine Agenten an ihre Schichtpläne halten.
archive_ref: 20210422-de-adherence
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
redirect_from:
  - /de/adherence/
redirect_reason: Updated filename on 07 December 2022
---

In diesem Artikel lernst Du:

- was das Echtzeit Adherence-Feature ist und wie Du es verwendest.
- wie Du nach Agentenstatus, Planabweichungs-Typ, Aktivität, etc. filterst.
- wie Du die angezeigten Daten sortierst.

## Was ist das Echtzeit Adherence-Feature?

Mit dem _Echtzeit Adherence_{:.menu-item}-Feature, verfügbar unter _Intraday > Echtzeit Adherence_{:.breadcrumbs}, gleichst Du in Echtzeit die geplanten Aktivitäten Deiner Agenten mit den gerade tatsächlich ausgeführten Aktivitäten ab. So kannst Du Abweichungen vom Schichtplan rasch erkennen und falls nötig Maßnahmen ergreifen.

## Voraussetzungen

Das _Echtzeit Adherence_{:.menu-item}-Feature nutzt Informationen aus der ACD, die darüber Auskunft geben, an welchen Aktivitäten Mitarbeiter aktuell arbeiten. Das Feature zeigt Daten, nachdem Du den {% link_new Import von Agentenstatus-Daten | features/acd-integration/cloud/import-agent-status-data.md %} eingerichtet hast.

## Daten anzeigen

Wähle eine **Planungseinheit** und/oder **Auswahl**, um Mitarbeiterdaten anzuzeigen.

In den Bereichen oben sowie auf der linken Seite erhältst Du einen [allgemeinen Überblick](#einen-allgemeinen-überblick-erhalten) über die gewählte Planungseinheit und/oder Auswahl. Die Mitarbeitertabelle im unteren Bereich zeigt Dir Details zum [Status einzelner Mitarbeiter](#details-zu-mitarbeitern-prüfen).

> Begrenze die Ansicht für bestimmte Benutzer auf relevante Mitarbeiter
>
> Konfiguriere Berechtigungen auf bestimmte Planungseinheiten oder Auswahlen pro {% link_new Benutzer oder Benutzerrolle | getting-started/configure-user-roles.md | #berechtigungen-für-wfm-konfigurieren %}.

## Den Status verstehen

Jeder Agent hat einen Status, der auf dem Vergleich zwischen der geplanten Aktivität und der tatsächlichen Aktivität basiert:

- _Plankonform_: Die Aktivitätstypen der geplanten und der tatsächlichen Aktivität sind gleich. Der Status wird farblich nicht besonders hervorgehoben.
- _In Planabweichung_: Die Aktivitätstypen von geplanter und tatsächlicher Aktivität weichen voneinander ab.

Es gibt drei verschiedene Typen von _Planabweichungen_, die farblich unterschiedlich hervorgehoben werden:

- _Nicht Anwesend_ (rot): Der Agent ist für eine bestimmte Aktivität geplant, aber es gibt keine Informationen von der ACD oder dem externen System, dass der Agent tatsächlich etwas tut. Hervorgehoben in Rot.
- _Falsche Aktivität_ (gelb): Gemäß der ACD führt der Mitarbeiter eine Aktivität aus, die nicht der geplanten Aktivität entspricht.
- _Nicht Geplant_ (blau): Der Agent ist überhaupt nicht geplant, aber es gibt Aktivitätsdaten in der ACD oder im externen System, die zeigen, dass der Agent mit einem bestimmten Agentenstatus angemeldet ist. Agenten mit diesem Planabweichungs-Typ haben keinen negativen Einfluss auf den _Adherence Score_.

In injixo Advanced WFM und injixo Enterprise WFM kannst Du mithilfe von {% link_new Matches | features/intraday/adherence-matches.md %} wesentlich genauer festlegen, welche Kombinationen von Aktivitäten als _plankonform_ gelten.

## Einen allgemeinen Überblick erhalten

Die Bereiche oben und links geben Dir einen Überblick über den Status Deiner Mitarbeiter zum aktuellen Zeitpunkt. Unterhalb erfährst Du mehr über die einzelnen Bereiche.

> So überprüfst Du die historische Planeinhaltung
>
> Um nicht die aktuelle, sondern die historische Planeinhaltung zu überprüfen, verwende die Reports _Planeinhaltung (Aktivität)_ und _Planeinhaltung (Arbeitszeit)_ unter _WFM > Controlling > Reports_{:.breadcrumbs}.

### Echtzeit Adherence

Die Echtzeit-Planeinhaltung ist der Prozentsatz der Agenten, der sich in diesem Moment _in Planeinhaltung_ oder _in Toleranzzeit_ befindet.

{{ 4 | image: 'Echtzeit Adherence','40%' }}

### Intraday Adherence

Die Intraday-Planeinhaltung ist der aggregierte Wert für jedes vergangene Intervall des bisherigen Tages.

Das Diagramm darunter enthält zwei Graphen:

- In Grau: der Wert für jedes vergangene Intervall des bisherigen Tages. Dies hilft, Tageszeiten mit hoher oder niedriger Planeinhaltung zu identifizieren.
- In Blau: der Trend des Intraday Adherence-Scores. Damit erkennst Du den allgemeinen Trend über den bisherigen Tag.

Darüber hinaus wird der festgelegte Zielwert für die Planeinhaltung angezeigt.

Hinweis: Bewege die Maus über das Diagramm, um die Werte für die einzelnen Intervalle in einem Pop-up-Fenster zu sehen.

Alle Zeiten erscheinen in der Zeitzone der ausgewählten Planungseinheit. Wenn Du keine Planungseinheit, sondern nur eine Auswahl wählst, und Du mehrere Zeitzonen in injixo verwendest, wird die im Unternehmens-Account konfigurierte Zeitzone verwendet. Zusätzlich werden ggf. die Öffnungszeiten der ausgewählten Planungseinheit im Diagramm angezeigt.

{{ 3 | image: 'Intraday Adherence-Score','50%' }}

### Agentenübersicht, Pausen und Anwesenheit

Die Agentenübersicht auf der linken Seite ist zweigeteilt und zeigt:

- die Anzahl der Agenten für die drei unterschiedlichen _Typen der Planabweichung_.
- die Anzahl Deiner Mitarbeiter _in Planeinhaltung_, _in Toleranzzeit_ und _in Planabweichung_.

Unter _Anwesenheit_ siehst Du für alle Aktivitäten vom Typ _Anwesenheit_ die Anzahl der geplanten und der momentan tatsächlich angemeldeten Agenten sowie die Differenz zwischen beiden Werten. Unter _Pausen_ siehst Du dieselben Informationen, aber nur für Aktivitäten vom Typ _Pause_.

{{ 1 | image: 'Agentenübersicht','100%' }}

<!-- rework later, the feature will change soon -->

### Aktivitätsübersicht

Die _Aktivitätsübersicht_ unten links listet die geplanten und tatsächlich anwesenden Agenten für jede geplante Aktivität in der gewählten Planungseinheit und/oder Auswahl auf.

Die Tabelle enthält die folgenden Spalten:

| Aktivität | Name der geplanten Aktivität. |
| Geplant | Die Anzahl der für diese Aktivität geplanten Mitarbeiter. |
| Tatsächlich | Die Anzahl der Mitarbeiter, die laut ACD-Daten gerade an dieser Aktivität arbeiten. |

{{ 2 | image: 'Aktivitätsübersicht','40%' }}

## Details zu Mitarbeitern prüfen

Die _Mitarbeitertabelle_ unten rechts zeigt alle Mitarbeiter, die den Schichtplan einhalten oder davon abweichen. Sie zeigt keine Mitarbeiter, die für eine Aktivität vom Typ _Urlaub_ oder _Krankheit_ geplant sind und gleichzeitig nicht angemeldet sind.

{{ 5 | image: "Tabelle mit Details zu den Mitarbeitern", '75%' }}

Die Tabelle enthält folgende Spalten:

| Name | Die Namen der angezeigten Mitarbeiter |
| Tatsächliche Aktivität | Die Aktivität, die der Agent gerade ausführt (basierend auf den Daten aus der Ebene _Externes System_ oder _Zeiterfassung_). |
| Status | Wenn der Agent _Plankonform_ ist, ist die Statusfarbe grau. Wenn der Agent _in Planabweichung_ ist, können die folgenden drei Farben angezeigt werden: Rot, wenn der Agent _Nicht Anwesend_ ist, Gelb, wenn der Agent die _Falsche Aktivität_ ausführt, und Blau, wenn der Agent aktiv, aber _Nicht Geplant_ ist.
| Geplante Aktivität | Die Aktivitäten, für die die angezeigten Mitarbeiter zum aktuellen Zeitpunkt geplant sind (falls vorhanden). |
| Aktuelle Abweichungsdauer | Dies zeigt an, wie lange sich der Mitarbeiter schon _in Planabweichung_ befindet. |
| Aktuelle Aktivitätsdauer | Die Zeitspanne, die seit dem Beginn der aktuellen Aktivität vergangen ist. |

### Den Tagesverlauf eines Agenten prüfen

Klicke auf den **Namen eines Agenten**, um eine Detailansicht unterhalb der Tabelle zu öffnen. Hier siehst Du die geplanten Aktivitäten des Agenten für den heutigen Tag. Direkt darunter siehst Du die Zeiträume, in denen sich der Agent in Planabweichung befand.
Über der grafischen Anzeige siehst Du einige Statistiken über den Tagesverlauf des Agenten. Sie zeigen, für welchen Zeitraum der Agent geplant ist und die Gesamtzeit der Planabweichungen. Das Verhältnis aus beiden wird im Adherence Score ersichtlich.

{{ 6 | image: 'Agentendetails','60%' }}

Klicke auf einen **Abweichungszeitraum**, um die Details der tatsächlichen vom Agenten ausgeführten Aktivitäten anzuzeigen. Du siehst zusätzlich den Aktivitätstyp und die Dauer der Aktivität.

Wenn viele kurze Planabweichungen aufeinander folgen, werden diese in der Detailansicht zu einem Block zusammenfasst.

{{ 7 | image: 'in Planabweichung Detail-Ansicht','60%' }}

### Die Ansicht filtern und sortieren

Sortiere die angezeigten Daten in der Tabelle _Aktivitätsübersicht_ und in der _Mitarbeitertabelle_ mit einem Klick auf eine beliebige **Spaltenüberschrift**. Klicke nochmals, um die Sortierreihenfolge umzukehren.

Oberhalb der Liste der Agenten befindet sich eine Suchleiste. Aktiviere neben der Suchleiste die Checkbox **Nur Planabweichungen anzeigen**, um nur Agenten _in Planabweichung_ anzuzeigen.

Füge Elemente in der Suchleiste hinzu oder entferne sie, um die Mitarbeitertabelle zu filtern:

- Gib **(Teil-)Suchbegriffe** in die Suchleiste ein, z. B. Mitarbeiternamen, Aktivitäten oder einen Mitarbeiterstatus. Trenne verschiedene Suchbegriffe durchs Kommas. Die Suche zeigt Ergebnisse für jeden Deiner Suchbegriffe an.
- Klicke auf einen **Mitarbeiterstatus** in der _Agentenübersicht_. Das angeklickte Element wird der Suche hinzugefügt. Klicke erneut auf ein Element, um es wieder aus der Suche zu entfernen.
- Klicke in der _Aktivitätsübersicht_ auf die **Lupe** rechts neben einer Aktivität. Die angeklickte Aktivität wird der Suche hinzugefügt. Klicke erneut, um sie zu entfernen.

### Toleranzzeiten festlegen

In einer realen Arbeitsumgebung sind Agenten selten in der Lage, sich sekundengenau an ihren Schichtplan zu halten. Dies kann zu einer sehr unruhigen Darstellung im Echtzeit Adherence-Feature führen, vor allem bei einer großen Anzahl von Mitarbeitern. Damit Du Dich auf die Mitarbeiter konzentrieren kannst, die Deine Aufmerksamkeit erfordern, kannst Du eine bestimmte Dauer definieren, bevor ein _In Planabweichung_-Status wirksam wird. Dies wird als _Toleranzzeit_ bezeichnet.

Wenn sich ein Agent innerhalb der definierten Toleranzzeit befindet, zählt diese zwar schon zur aktuellen Abweichungsdauer, aber:

- die Zeile des Agenten wird noch nicht hervorgehoben und nur das Statussymbol ändert sich.
- der Agent hat keinen negativen Einfluss auf den Adherence Score.
- der Agent erscheint nicht, wenn der Filter _Nur Planabweichungen anzeigen_ aktiviert ist.

Als Benutzer mit der Rolle _Administrator_ kannst Du eine separate _Toleranzzeit_ für jeden der drei Planabweichungstypen festlegen:

1. Klicke auf das Kontextmenü-Icon _![Kontextmenü Icon](/assets/img/common/injixo-ui/context-menu.svg)_{:.doc-button-icon}.
2. Wähle **Toleranzzeiten anpassen**. Das _Toleranzzeiten anpassen_-Fenster öffnet sich.
3. Wähle die gleichen oder unterschiedliche Werte aus den Dropdown-Menüs **Nicht Anwesend**, **Falsche Aktivität** und **Nicht Geplant**.
4. Klicke _Anwenden_{:.doc-button}, um die Werte zu speichern.

> Die Einstellungen der Toleranzzeiten gelten für alle Benutzer des _Echtzeit Adherence_-Feature in Deinem Unternehmen.

### Zielwert für die Planeinhaltung festlegen

Du kannst den _Zielwert für die Planeinhaltung_ anpassen, der standardmäßig auf 90 % gesetzt ist. Alle Diagramme zeigen den Zielwert. Alle Einzelwerte unter dem Zielwert werden hervorgehoben.

Benutzer mit _Admin-Zugriff_ können Du den _Zielwert für die Planeinhaltung_ festlegen:

1. Klicke auf das Kontextmenü-Icon _![Kontextmenü Icon](/assets/img/common/injixo-ui/context-menu.svg)_{:.doc-button-icon}.
2. Wähle **Zielwert für die Planeinhaltung anpassen**.
3. Gib im Feld neben _Lege den Zielwert für die Planeinhaltung fest:_ einen neuen _Zielwert_ ein.
4. Klicke _Anwenden_{:.doc-button}, um den Wert zu speichern.

> Diese Einstellung ist ein globaler Wert und gilt für alle Agenten und injixo-Benutzer.
