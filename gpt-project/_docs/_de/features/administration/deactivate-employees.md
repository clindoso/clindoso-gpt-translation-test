---
title: Mitarbeiter deaktivieren, reaktivieren und löschen
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Lerne, wann und wie Du Mitarbeiter deaktivieren, reaktivieren oder löschen kannst.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/how-does-billing-work.md
---

Wenn du in deinem Unternehmen Mitarbeiter hast, die du nicht mehr planst und die keinen Zugang zu injixo mehr benötigen, kannst du sie deaktivieren oder löschen. Dies hat folgende Auswirkungen:

- Deaktivierte Mitarbeiter verlieren den Zugang zu injixo.
- Deinem Unternehmen werden diese Mitarbeiter ab dem folgenden Monat nicht mehr {% link_new in Rechnung gestellt | getting-started/how-does-billing-work.md %}.

## Mitarbeiter deaktivieren

Wenn Mitarbeiter für einen längeren Zeitraum nicht arbeiten können, zum Beispiel, wenn sie ein Sabbatical oder Elternzeit nehmen, kannst du sie vorübergehend deaktivieren. Deinem Unternehmen werden deaktivierte Mitarbeiter nicht in Rechnung gestellt. Du kannst Mitarbeiter reaktivieren, wenn sie wieder zurück zur Arbeit kommen. Es kann Fälle geben, in denen du gemäß der Europäischen Datenschutz-Grundverordnung (DSGVO) die Daten eines Mitarbeiters löschen musst. Falls solch ein Fall eintritt, [lösche](#mitarbeiter-löschen) den Mitarbeiter.

Um einen Mitarbeiter zu deaktivieren, gehe wie folgt vor:

1. Gehe zu _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs}.
2. Klicke in der Mitarbeiterliste auf den Mitarbeiter, den du deaktivieren möchtest.
3. Klicke im Mitarbeiterkonfigurationsdialog im Abschnitt **Betriebszugehörigkeit** auf das {% icon item-edit %}.
4. Gib ein Austrittsdatum ein.<br>Ein Austrittsdatum in der Vergangenheit sorgt dafür, dass der Mitarbeiter sofort deaktiviert wird. Wenn das Austrittsdatum in der Zukunft liegt, wird der Mitarbeiter zum festgelegten Datum deaktiviert.
5. Klicke auf _OK_{:.doc-button}.<br>Eine Bestätigungsnachricht erscheint.
6. Um zukünftige Schichtpläne zu löschen, aber historische Planungsdaten zu behalten, klicke auf _Ja_{:.doc-button}. Um alle Planungsdaten des deaktivierten Mitarbeiters zu behalten, klicke auf _Nein_{:.doc-button}.

### Deaktivierte Mitarbeiter anzeigen

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Klicke auf den Tab **Nicht abgerechnete Benutzer**.<br>Die Tabelle zeigt alle deaktivierten Benutzer, die deinem Unternehmen nicht mehr in Rechnung gestellt werden.

### Mitarbeiter reaktivieren

Um einen Mitarbeiter erneut zu aktivieren, z.&nbsp;B. nach einer langen Abwesenheit, gehe wie folgt vor:

1. Gehe zu _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs}.
2. Verwende das Suchfeld oben links, um den Mitarbeiter zu finden, den du reaktivieren möchtest.<br>Ein Fenster öffnet sich. Wenn du den vollständigen Namen des Mitarbeiters eingegeben hast und die Suche nur einen Treffer hat, zeigt das Fenster direkt den Konfigurationsdialog des betreffenden Mitarbeiters an. Wenn die Suche mehrere Treffer hat, zeigt das Fenster eine Liste von Mitarbeitern an.
3. Wenn das Fenster eine Liste anzeigt, klicke auf den Mitarbeiter, den du reaktivieren möchtest.
4. Klicke im Mitarbeiterkonfigurationsdialog im Abschnitt **Betriebszugehörigkeit** auf das {% icon item-add %}.
5. Gib ein Eintrittsdatum ein.
6. Klicke auf _OK_{:.doc-button}.

## Mitarbeiter löschen

> Achtung
>
> Gelöschte Mitarbeiter können nicht wiederhergestellt werden. Wenn du einen Mitarbeiter löschst, wird er aus allen aktuellen und zukünftigen Schichtplänen entfernt, in denen er geplant war. Das Löschen eines Mitarbeiters hat keinen Einfluss auf die historischen Daten zur Planeinhaltung in {% link_new Intraday | features/intraday/adherence-intraday.md %}.

Wir empfehlen, Mitarbeiter nur dann zu löschen, wenn ihre Betriebszugehörigkeit dauerhaft beendet ist. Wenn Mitarbeiter für einen längeren Zeitraum abwesend sind, zum Beispiel, wenn sie ein Sabbatical oder Elternzeit nehmen, empfehlen wir, sie stattdessen zu [deaktivieren](#mitarbeiter-deaktivieren).

Um einen Mitarbeiter zu löschen, gehe wie folgt vor:

1. Gehe zu _Plan > Konfiguration > Mitarbeiter_{:.breadcrumbs}.
2. Klicke in der Mitarbeiterliste auf den Mitarbeiter, den du löschen möchtest.
3. Klicke in der Aktionsleiste auf das {% icon item-delete %}.<br>Eine Bestätigungsnachricht erscheint.
4. Klicke auf _Ja_{:.doc-button}.<br>Der Mitarbeiter und alle seine aktuellen und zukünftigen Schichtpläne werden aus injixo gelöscht.

Wenn du einen Mitarbeiter in injixo löschst, werden seine persönlichen Daten aus Datenschutzgründen anonymisiert. injixo hält die ID des Mitarbeiters vor, markiert sie jedoch als gelöscht und ersetzt den Namen durch Sternchen. injixo ändert auch persönliche Angaben, um alle identifizierbaren Informationen zu entfernen, wie Namen, Personalnummer, Adressen, Telefonnummern und E-Mail-Adressen. Wenn in der Mitarbeiterkonfiguration Ausweisnummern enthalten waren, löscht injixo diese vollständig.
