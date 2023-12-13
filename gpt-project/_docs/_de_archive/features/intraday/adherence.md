---
title: Adherence
description: Verschaffe Dir in Echtzeit einen Überblick über die geplanten und tatsächlich ausgeführten Aktivitäten Deiner Mitarbeiter.
archived_date: 2021-04-22
archive_ref: 20210422-de-adherence
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

_Adherence_{:.menu-item} stellt die geplanten und laut ACD-Daten tatsächlich ausgeführten Aktivitäten Deiner Mitarbeiter in Echtzeit gegenüber. Damit hast Du die Auslastung Deiner Mitarbeiter im Blick und trägst zur Effizienzsteigerung in Deinem Unternehmen bei.

Das Modul ist in der Hauptnavigation unterhalb von _Intraday_{:.menu-item} zu finden. Zugriff haben Benutzer mit _Admin-Zugriff_ oder der Rolle _Supervisor_ bzw. _Supervisor Basic_.

> Für die Nutzung ist ein Import von Aktivitätsdaten aus einem externen System notwendig.

## Mitarbeiterübersicht

Die Tabelle zeigt alle Mitarbeiter, die den Schichtplan einhalten oder davon abweichen. Hält der Mitarbeiter den Schichtplan ein, erfolgt keine besondere Hervorhebung. Klicke auf eine Spaltenüberschrift, um nach einer beliebigen Spalte zu sortieren.

Verfügbare Spalten:

| Name | Namen der Mitarbeiter |
| Geplante Aktivität | Geplante Aktivitäten aus der Ebene _Plan_ |
| Status | Durch Farbcodes hervorgehobene Status für Abweichungen.
| Tatsächliche Aktivität | Alle Aktivitäten aus der der Ebene _Externes System_ oder _Zeiterfassung_. |
| Aktuelle Abweichungsdauer | Dauer der Abweichung, wenn die aktuelle Aktivität von der geplanten Aktivität abweicht. |
| Tatsächliche Aktivität Dauer | Dauer der momentan ausgeführten Aktivität (vom Beginn der Aktivität bis zum jetzigen Zeitpunkt). |

Nicht angezeigt werden Mitarbeiter die für eine Abwesenheit oder einen Urlaub geplant und nicht eingeloggt sind.

## Adherence Score

{{ 1 | image: 'Adherence Score','50%' }}

Der _Adherence Score in %_ zeigt auf einen Blick den Anteil der Mitarbeiter, die zum aktuellen Zeitpunkt den Schichtplan einhalten oder noch nicht die [Toleranzzeit](#toleranzzeit-für-abweichungen) überschritten haben. An der farbigen Legende darunter erkennst Du, wie viele Mitarbeiter welchen Abweichungsstatus über die Toleranzzeit hinaus haben.

Wenn für einen Mitarbeiter geplante und tatsächliche Aktivität voneinander abweichen, ist der Agent entweder _in der Toleranzzeit_ (falls konfiguriert) oder _in Planabweichung_. Folgende drei Status für eine Planabweichung sind dabei möglich:

- **Nicht Anwesend**: Gemäß des externen Systems arbeitet der Mitarbeiter nicht, der Mitarbeiter soll laut Schichtplan aber eine bestimmte Aktivität ausüben.
- **Falsche Aktivität**: Gemäß des externen Systems arbeitet der Mitarbeiter auf einem anderen Aktivitätstypen, als es die Planung vorsieht.\*
- **Nicht Geplant**: Gemäß des externen Systems arbeitet der Mitarbeiter, der Mitarbeiter soll laut Schichtplan aber nicht arbeiten. Agenten mit diesem Status haben keinen negativen Einfluss auf den _Adherence Score in %_.

Darunter gibt es einen groben Überblick, wie viele Agenten im Moment als Anwesend geplant und auch in der ACD angemeldet sind, wie viele Agenten für eine Pause geplant sind und wie viele eine Pause machen sowie die Abweichungen für beide Werte.

Definiere mit Hilfe von {% link_new Matches | features/intraday/adherence-matches.md %}, welche Kombinationen von Aktivitäten als plankonform gelten.

## Toleranzzeit für Abweichungen

Für Mitarbeiter ist es nahezu unmöglich, die Planung sekundengenau einzuhalten. Dies kann zu einer sehr unruhigen Übersicht mit ständigen Veränderungen führen, welche es erschwert, die Mitarbeiter zu identifizieren, die Aufmerksamkeit benötigen.

Du hast deshalb die Möglichkeit in den Einstellungen eine _Toleranzzeit_ festzulegen. Diese kann für jeden der drei Planabweichungs-Status einzeln konfiguriert werden. Nur Nutzer mit der Rolle _Administrator_ können die Einstellung ändern und diese gilt dann für alle Nutzer des Adherence Moduls.

Innerhalb der Toleranzzeit

- wird die Zeile des Agenten nicht besonders hervorgehoben.
- hat der Agent keinen negativen Einfluss auf den Adherene Score.
- wird der Agent nicht angezeigt, wenn der _Nur Planabweichungen_ Filter aktiv ist.

Die aktuelle Abweichungsdauer wird ab Beginn der Toleranzzeit gemessen.

## Aktivitätsübersicht

{{ 2 | image: 'Aktivitätsübersicht','50%' }}

Die Aktivitätsübersicht hilft Dir, bestimmte Aktivitäten im Blick zu behalten und zeigt folgende Informationen:

| Aktivität | Namen der Aktivitäten. |
| Geplant | Die Anzahl der geplanten Mitarbeiter. |
| Aktuell | Die Anzahl der Mitarbeiter, die laut ACD-Daten an dieser Aktivität arbeiten. |

## Filtere Datensätze mit Hilfe der Omnisuche

Über der Mitarbeiterübersicht befindet sich eine Omnisuche. Suche nach Mitarbeiternamen, Personalnummern, Aktivitäten und Mitarbeiterstatus (auch über Teilbegriffe). Trenne verschiedene Suchbegriffe mit Komma. Ergebnisse werden für jeden Suchbegriff angezeigt.

Du kannst Status oder Aktivitäten durch einen Klick auf die Einträge der Aktivitätsübersicht oder Mitarbeiterübersicht hinzufügen. Ein weiterer Klick entfernt den Suchbegriff wieder.

> Weiteres Kontrollinstrument
>
> Nutze auch die Reports _Planeinhaltung (Aktivität)_ und _Planeinhaltung (Arbeitszeit)_ in _WFM > Controlling > Reports_{:.breadcrumbs}.
