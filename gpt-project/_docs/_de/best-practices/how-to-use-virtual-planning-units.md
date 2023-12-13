---
title: Mitarbeiter an mehreren Standorten gemeinsam planen
redirect_from:
  - /de/best-practice-planung-ueber-vituelle-planungseinheiten/
description: Mit virtuellen Planungseinheiten kannst Du mehrere Planungseinheiten in einem Schritt planen und die damit verbundenen Synergie-Effekte nutzen.
product_label:
  - advanced
  - enterprise
  - classic
---

## Szenario

Du betreibst zwei Contact Center für Dein Unternehmen; eins in New York und eins in Berlin. Die Anrufe werden an jeden Agenten mit den entsprechenden Qualifikationen weitergeleitet, unabhängig vom Standort des Agenten. Du möchtest Agenten an beiden Standorten beschäftigen, um dieses Anrufvolumen zu bewältigen.

In injixo Enterprise on-premise musst Du die folgenden Einstellungen aktivieren, um die Funktionalität wie beschrieben nutzen zu können:  
- *48103*{:.id-label} *Kennzahlen für übergeordnete Planungseinheiten konsolidieren*  
- *48399*{:.id-label} *Planbarkeit virtueller Planungseinheiten im AutoScheduler*  

## Repräsentation in injixo

Jeder Standort ist als eigene {% link_new Planungseinheit | features/administration/create-and-manage-planning-units.md %} angelegt.

Darüber hinaus benötigst Du zwei zusätzliche Planungseinheiten:
1. Eine Planungseinheit, der keine Mitarbeiter zugeordnet sind, in welcher aber die Zahlen für die benötigten Agenten gespeichert werden, um Dein Anrufaufkommen zu bewältigen.
<!-- oder: in welcher aber die Zahlen für den  Mitarbeiterbedarf gespeichert werden. -->
2. Eine Planungseinheit, die Dein gesamtes Unternehmen repräsentiert, verteilt auf mehrere Standorte. Diese wird als übergeordnete oder virtuelle Planungseinheit bezeichnet.

Am Ende hast Du eine solche Struktur:
- Motibot Technology Co.
  - Berlin
  - New York
  - Mitarbeiterbedarfe

## Empfohlener Ansatz

### Erzeuge eine Planungseinheit für den Mitarbeiterbedarf

Erstelle dazu unter *WFM > Administration > Scheduling > Planungseinheiten*{:.breadcrumbs} eine neue Planungseinheit mit dem gleichen Intervall wie Deine bestehenden Planungseinheiten. Lege die Öffnungszeiten so fest, dass sie die Öffnungszeiten aller anderen Planungseinheiten umfassen. Füge alle Aktivitäten hinzu, die in mindestens einer Planungseinheit ausgeführt werden.

Zum Beispiel:
- Berlin: Mo-Fr von 08:00-18:00
- München: Mo-So von 09:00-18:00 Uhr
- Mitarbeiterbedarfe: Mo-So von 08:00-18:00 Uhr

Füge der Planungseinheit **nichts** anderes hinzu, keine Mitarbeiter, Tagesmodelle oder Planungskalender.

### Erstelle die übergeordnete Planungseinheit

Diese wird auf die gleiche Weise wie die Bedarfsplanungseinheit erstellt, jedoch musst Du Dich nicht um die Betriebszeiten kümmern; bei der Planung werden die Öffnungszeiten jeder untergeordneten Planungseinheit individuell berücksichtigt.

### Aufbau und Zuordnung der Planungseinheiten

Während der Einrichtung legen wir die virtuelle Planungseinheit als übergeordnete Einheit der standortbezogenen Planung fest. Öffne dazu die untergeordneten Planungseinheiten und wähle in *Allgemein*{:.menu-item} die virtuelle Planungseinheit als **Übergeordnete Planungseinheit** aus.

{{ 1 | image: 'Create virtual planning unit'}}

### Forecast und Planung

Den errechneten Mitarbeiterbedarf für Deine Aktivitäten hinterlegst Du in der Planungseinheit Mitarbeiterbedarfe. Nachdem Du den Bedarf für alle Aktivitäten berechnet hast, kannst Du einen Schichtplan erstellen, indem Du eine vollständige Optimierung auf der übergeordneten Planungseinheit durchführst. Beachte bitte, dass dadurch immer die Schichtpläne für alle Mitarbeiter in jeder untergeordneten Planungseinheit optimiert werden.

> Verfügbare Planungsmethoden
>
> Virtuelle Planungseinheiten können nur mithilfe einer volloptimierten Planung geplant werden. Schichterzeugung oder Job- und Pausenoptimierung sind nicht möglich.

## Planungsergebnis

Für die Planung der Mitarbeiter in jeder untergeordneten Planungseinheit werden die Bedarfe aus der Bedarfsplanungseinheit genutzt, so wird die Deckung über alle Standorte hinweg optimiert. Die daraus resultierende Deckung kannst Du wie gewohnt im Kennzahlenfenster für die übergeordnete Planungseinheit sehen. Diese aggregierte Ansicht betrifft nur die Kennzahlen; Du erhältst keine Komplettübersicht über Deine Mitarbeiter und ihre Schichtpläne.

> Hinweis
>
> Wenn Du einen Überlauf planen möchtest, benötigst Du nur eine zusätzliche übergeordnete Planungseinheit und keine für die Mitarbeiterbedarfe. Speichere wie gewohnt die Bedarfe der einzelnen Planungseinheiten.
>
> Mit der Planung der übergeordneten Planungseinheit stellst Du sicher, dass die Anrufe primär in der eigenen Planungseinheit beantwortet werden. Sind nicht genug Mitarbeiter vorhanden, werden zusätzlich entsprechend qualifizierte Agenten aus anderen Planungseinheiten für die Aktivität berücksichtigt.
