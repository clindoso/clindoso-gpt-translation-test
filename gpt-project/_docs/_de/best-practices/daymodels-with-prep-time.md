---
title: Planung von Rüstzeiten
description: Lege Rüstzeit als Aktivität für die Vor- und Nachbereitung Deiner Mitarbeiter an und verwende sie in Tagesmodellen.
product_label:
  - advanced
  - enterprise
  - classic
promote_service: general
---

In diesem Artikel lernst Du:

- was Rüstzeiten sind.
- warum Rüstzeiten für die Planung problematisch sein können.
- wie Du diese in injixo verwendest.

## Herausforderung

Rüstzeiten sind unproduktive Zeiten am Anfang und/oder am Ende einer Schicht. Diese sind typischerweise bezahlt, können aber auch unbezahlt sein. In der Rüstzeit am Anfang der Schicht richtet sich der Mitarbeiter an seinem Arbeitsplatz ein und benötigt einige Minuten zum Starten des Rechners, Anmelden und Starten von Programmen. Am Ende der Schicht dient die Rüstzeit zum Abmelden, Herunterfahren des Rechners, dem Aufräumen des Arbeitsplatzes und anderen Aufgaben.

Rüstzeiten werden vor allem zu Beginn der ersten Schicht des Tages eingesetzt, wenn mehrere Agenten gleichzeitig die Schicht beginnen, um die Deckung nicht zu gefährden. Verbringen mehrere Agenten den Großteil eines Intervalls einer Schicht mit der Arbeitsvorbereitung, können sie in dieser Zeit keine Anrufe annehmen.
Andere Szenarien sind Rüstzeiten für alle Schichten aus Fairness-Gründen, Rüstzeiten am Ende der Spätschicht, um noch die letzten Anrufer zu bedienen, oder aber auch Rüstzeiten am Anfang und am Ende einer Schicht.

Du kannst ganz auf Rüstzeiten verzichten, wenn die Auswirkung auf die Deckung aufgrund einer geringen Mitarbeiteranzahl oder eines niedrigen Anrufvolumens zu vernachlässigen ist.

## Lösung

Du benötigst eine separate Aktivität für die Rüstzeit in Deinen Tagesmodellen. Diese sorgt dafür, dass unproduktive Vor- und Nachbereitungszeiten keinen Einfluss auf die Deckung haben. Außerdem kannst Du die Rüstzeit separat im Reporting ausweisen.

### Aktivität erstellen

1. Erstelle eine {% link_new neue Aktivität | features/administration/activities.md %} **Rüstzeit** vom Typ _Anwesenheit_.
2. Setze **folgende Häkchen** in der neuen Aktivität:
   - Bezahlt (optional)
   - Ruhezeit einhalten
   - Planbar
   - Tauschbar beim Schichttausch
   - Überdeckung erlauben, wenn Mitarbeiterbedarf gleich null. Notwendig, da für Rüstzeit kein Mitarbeiterbedarf besteht.

Füge die neue Aktivität {% link_new zur Planungseinheit hinzu | features/administration/create-and-manage-planning-units.md | #aktivitäten-hinzufügen %}.

### Tagesmodelle anpassen

1. Verlängere den **Zeitrahmen des Tagesmodells**.

   - Passe dazu den Wert für **Zeitrahmen Beginn** und/oder **Zeitrahmen Ende** {% link_new im Tagesmodell | features/administration/daymodels/daymodel-creation.md %} an. Die Anpassung ist notwendig, wenn die Rüstzeit vor dem Schichtbeginn oder nach dem Schichtende platziert werden soll.
   - Der neue Wert ergibt sich aus `Zeitrahmen Beginn - Rüstzeit am Anfang der Schicht` und `Zeitrahmen Ende + Rüstzeit am Ende der Schicht`. Füge z.B. 10 Minuten hinzu, wenn Du vor der Schicht 10 Minuten Rüstzeit einfügen möchtest.

2. Verlängere die **Brutto-Schichtdauer**, wenn die Rüstzeit unbezahlt ist oder mit dem Hinzufügen der Rüstzeit die Arbeitszeit verlängert wird. Überspringe diesen Schritt, wenn die Rüstzeit innerhalb der Schicht liegen soll.

3. Füge die neue Aktivität unter **An- und Abwesenheiten** in Deine bestehenden Tagesmodelle ein. Platziere sie dabei absolut oder relativ am Anfang und/oder am Ende der Schicht.

   {{ 1 | image: 'Tagesmodell mit Rüstzeit', '50%' }}

> Hinweis
>
> Passe die Min/Max/Soll-Werte für vorhandene Verträge entsprechend an, wenn Du die Schichtzeit verlängerst **und** eine bezahlte Rüstzeit nutzt. Eine Vertragsanpassung kann auch nötig sein, wenn Schichten mit Rüstzeit gegen Schichten ohne Rüstzeit getauscht werden.

## Entfernen von Rüstzeiten

Tagesmodelle können nur verlängert werden. Beim Entfernen einer Rüstzeit musst Du unter Umständen das ganze Tagesmodell neu anlegen, da eine Verkürzung der Dauer bzw. des Zeitrahmens von bestehenden Tagesmodellen nicht möglich ist.

## Mitarbeiter ohne Schichten in Randzeiten

Durch die Verlängerung des Tagesmodell-Zeitrahmens kann es vorkommen, dass die Rüstzeit außerhalb der Öffnungszeit der Planungseinheit liegt. Überprüfe in diesem Fall den Wert der Einstellung _48408_{:.id-label} _Berücksichtigung von Öffnungszeiten im AutoScheduler_ und ändere ihn ggf. auf 0. Auf diese Weise musst Du die Öffnungszeiten Deiner Planungseinheit nicht anpassen.
