---
title: Nichtverfügbarkeiten deiner Mitarbeiter verwalten
description: Erfahre, wie deine Mitarbeiter mit einer Aktivität vom Typ Abwesenheit Nichtverfügbarkeiten festlegen können.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: true
---

Erstelle eine wünschbare Aktivität vom Typ Abwesenheit, mit der deine Mitarbeiter Zeiten angeben können, zu denen sie nicht verfügbar sind.

Verwalte die Nichtverfügbarkeiten deiner Mitarbeiter mit Abwesenheitsanträgen, wenn du folgendes erreichen möchtest:

- Zeiträume festlegen, innerhalb derer Mitarbeiter Nichtverfügbarkeiten hinzufügen können.
- Eine Frist für Anträge auf Nichtverfügbarkeit festlegen, und die Anträge genehmigen bzw. ablehnen.
- Einen Überblick über die Anträge deiner Mitarbeiter über einen längeren Zeitraum behalten.
- Feststellen, ob die Verträge der Mitarbeiter mit ihrem Bedarf für Abwesenheiten übereinstimmen.
- Mitarbeitern erlauben, eine unbegrenzte Anzahl von Nichtverfügbarkeiten einzutragen.
- Mitarbeitern erlauben, untertägige Nichtverfügbarkeiten einzutragen.

Dieser Artikel zeigt den Prozess im Überblick. Du kannst ihn als Checkliste verwenden.

## 1\. Die Aktivität Nicht verfügbar erstellen

1. Erstelle unter _Plan > Konfiguration_{:.breadcrumbs} eine {% link_new neue Aktivität | features/administration/activities.md | #aktivität-erstellen %}.
2. Konfiguriere deine Aktivität wie folgt:
   - **Name**: Trage Nicht verfügbar ein. Eine Kurzbezeichnung wird automatisch erzeugt.
   - **Typ**: Wähle **Abwesenheit** aus.
   - Aktiviere die Checkbox **Wünschbar in Me**.
   - (Optional) Aktiviere die Checkbox **Ganztägig erlauben**.
3. Klicke auf _Aktivität erstellen_{:.doc-button}.

## 2\. Abwesenheitsperiode erstellen

1. Erstelle unter _Plan > Urlaub/Abwesenheiten_{:.breadcrumbs} eine {% link_new Abwesenheitsperiode | features/scheduling/time-off/time-off-periods.md | #abwesenheitsperiode-anlegen %}.
2. Gib die allgemeinen Informationen für deine Abwesenheitsperiode ein:
   - **Planungseinheit**
   - (Optional) **Auswahl**
   - **Aktivität**: Wähle **Nicht verfügbar**.
   - (Optional): **Stichtag**
   - **Status**: Wähle **Veröffentlicht**.
3. Klicke auf _Abwesenheitsperiode erstellen_{:.doc-button}.

## 3\. Mitarbeiter stellen Anträge

Unter _Me > Abwesenheit_{:.breadcrumbs} können Mitarbeiter Abwesenheiten mit der Aktivität Nicht verfügbar {% link_new beantragen | features/injixo-me/use-injixo-me/explore-injixo-me.md | #abwesenheiten-beantragen %}.

## 4\. Anträge genehmigen oder ablehnen

Anträge für die Aktivität Nicht verfügbar kannst du unter _Plan > Urlaub/Abwesenheiten_{:.breadcrumbs} {% link_new genehmigen bzw. ablehnen | features/scheduling/time-off/vacation-absences-management.md %}.<br>
Wenn du einen Antrag eines Mitarbeiters genehmigst, zeigt das Schichtplanfenster oben im Schicht Center eine rote Zelle mit der Kurzbezeichnung der Aktivität Nicht verfügbar für den genehmigten Zeitraum an. Wenn du die Funktionalitäten **Optimierten Plan erstellen** bzw. **Joboptimierung** verwendest, plant injixo den Mitarbeiter nicht während des blockierten Zeitraums.

## Überblick über Anträge behalten

Unter _Plan > Schicht Center_{:.breadcrumbs} kannst du die Details der genehmigten Abwesenheitsanträge für die Aktivität Nicht verfügbar einsehen.

1. Klicke auf den Tab **Aktivitäten - Bedarf** unter der Tabelle. Wähle oben einen Datumsbereich aus der Datumsauswahl und klicke auf _Anwenden_{:.doc-button}.
2. Klappe die entsprechende Planungseinheit in der oberen Tabelle aus.
3. Klicke doppelt auf eine rote Zelle mit dem Namen Nicht verfügbar.
4. Klicke auf den Tab **Verlauf**.  
   Du siehst die Details des genehmigten Abwesenheitsantrags.
   - Datum/Uhrzeit: Datum und Uhrzeit der Genehmigung.
   - Aktion: Die ausgeführte Aktion. Hier: Wunsch genehmigen.
   - Benutzer: Der Mitarbeiter, der den Antrag genehmigt hat.
5. Klicke auf _OK_{:.doc-button}.

Gehe zu _Plan > Urlaub/Abwesenheiten_{:.breadcrumbs}, um {% link_new genehmigte, ausstehende und abgelehnte Anträge einzusehen | features/scheduling/time-off/vacation-absences-management.md %}.
