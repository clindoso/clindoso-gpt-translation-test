---
title: Schichtpläne kopieren oder sichern
toc: false
product_label:
  - advanced
  - enterprise
description: Kopiere oder sichere Schichtpläne und andere Elemente in den verschiedenen Planungsebenen von injixo (Schedules-Modul).
---

In diesem Artikel lernst Du, wie Du Schichtpläne und andere Elemente in den verschiedenen Planungsebenen von injixo kopierst oder sicherst. Die Anleitung bezieht sich auf *Plan > Schedules*{:.breadcrumbs}.

## Ebenen in injixo

In injixo kannst Du verschiedene Ebenen für Planungszwecke nutzen. Ebenen enthalten - unter anderem - Tagesmodelle oder Aktivitäten für die Schichtplanung, Schichtwünsche oder Daten zur Verfügbarkeit von Agenten. Du kannst die Daten einer Ebene innerhalb derselben Ebene oder in eine andere Ebene kopieren, z.B. Deinen kompletten Schichtplan oder Teile davon. Das kann hilfreich sein, um Deine Planung zu beschleunigen.

Du kannst ein Backup anlegen, indem Du den kompletten Schichtplan in eine neue Ebene kopierst. Backups sind vor allem dann empfehlenswert, wenn Du eine neue Planungsmethode ausprobierst.

## Inhalt einer Ebene kopieren

So kopierst Du den Inhalt einer Ebene unter *Plan > Schedules*{:.breadcrumbs}:

1. Klicke auf *Planungsaktionen*{:.doc-button}.
2. Wähle **Ebeneninhalte kopieren**.
3. Wähle eine **Planungseinheit** im Bereich *Einstellungen*.
4. Wähle als **Quellebene** die Ebene, von der Du Daten kopieren möchtest.
5. Wähle als **Zielebene** die Ebene, in die Du die Daten kopieren möchtest.
6. Ändere den **Zeitraum** (optional). Der Zeitraum ist auf den aktuell in *Schedules* ausgewählten Zeitraum voreingestellt.
7. Mit **Ziel-Startdatum** definierst Du das Datum, an dem der kopierte Zeitraum eingefügt werden soll. Du kannst zum Beispiel die Daten eines alten Schichtplans in einen zukünftigen Zeitraum auf derselben Ebene kopieren. In diesem Fall müssen *Quellebene* und *Zielebene* übereinstimmen.
8. Optional: Aktiviere **Quellebene nach dem Kopieren leeren**, um den bestehenden Inhalt der Quellebene nach dem Kopieren zu löschen.
9. Um das Kopieren von Ebeneninhalten zu starten, klicke auf *Ebeneninhalte kopieren*{:.doc-button}. Das Kopieren kann einige Zeit in Anspruch nehmen. Du kannst auf den Link **JobProcessor** unten rechts klicken, bevor Du den Job startest, um den Fortschritt zu verfolgen. Klicke oben auf _![Zurück-Schaltfläche](/assets/img/common/injixo-ui/back.png)_{:.doc-button-icon} oder unten auf *Abbrechen*{:.doc-button}, um zu *Schedules* zurückzukehren, ohne den Job auszuführen.

{{ 1 | image: 'Dialog Ebeneninhalte kopieren', '80%' }}

Nachdem Du den Kopier-Job gestartet hast, öffnet sich wieder das Schedules-Modul. Eine grüne oder rote Benachrichtigung am oberen Rand zeigt an, ob der Job erfolgreich gestartet werden konnte oder nicht.

