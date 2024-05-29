---
title: Matches konfigurieren
product_label:
  - advanced
  - enterprise
description: Erstelle Regeln, welche Aktivitäten in der Echtzeit Adherence-Übersicht als plankonform gelten.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

In diesem Artikel lernst Du:

- was die _Matches_-Funktion ist und wie Du sie öffnest.
- wie Du Matches konfigurieren kannst.

Mit _Matches_{:.menu-item} kannst Du Deinen Adherence Score erheblich verbessern.

Neu bei Echtzeit Adherence? Lerne zuerst {% link_new die Grundlagen | features/intraday/real-time-adherence.md %}.

## Was ist die Matches-Funktion?

Wenn Dir die Standardeinstellung des Aktivitätstypen-Vergleichs nicht genügt oder Du Unzulänglichkeiten bei den ACD-Mappings ausgleichen musst, kannst Du mit _Matches_{:.menu-item}:

- Regeln erstellen, welche _ACD Aktivität_ mit welchen _geplanten Aktivitäten_ übereinstimmt.
- Ungenauigkeiten reduzieren, die durch falsche oder zu weit gefasste Mapping-Regeln entstehen.

Änderungen in Matches haben nur Auswirkungen auf das Echtzeit Adherence-Feature. injixo Standard-Reports sind davon nicht betroffen.

## Auf Matches zugreifen

Du hast verschiedene Möglichkeiten, die _Matches_-Funktion zu öffnen:

- klicke auf das Kontextmenü-Icon _![Kontextmenü Icon](/assets/img/common/injixo-ui/context-menu.svg)_{:.doc-button-icon} und wähle **Aktivitäts-Matches**.
- klicke auf den Namen der **aktuellen Aktivität**.
- bewege den Mauszeiger über eine Aktivität links in der Aktivitätsübersicht und klicke auf das **Matches Icon**.

Auf der linken Seite siehst Du eine Liste von Aktivitäten. Nutze das Suchfeld oberhalb, um die Liste zu filtern.

{{ 3 | image: 'Liste der Aktivitäten','40%' }}

## Matches-Konfiguration anzeigen

Um eine detaillierte Ansicht der aktuellen Matches-Konfiguration zu erhalten, klicke auf eine **Aktivität**:

Links unter _Tatsächliche Aktivität_ siehst Du die Mappings zwischen externen und injixo-Aktivitäten, gruppiert nach externen Systemen. Wenn noch keine Mappings existieren, wird die Meldung _Keine Mappings eingerichtet_ angezeigt. Klicke **Bearbeiten**, um {% link_new Mappings hinzuzufügen oder zu bearbeiten | features/acd-integration/cloud/import-agent-status-data.md | #aktivitäten-aus-externen-systemen-den-aktivitäten-in-injixo-zuordnen %}.

Rechts unter _Geplante Aktivität_ kannst Du sehen, welche Aktivitäten und Aktivitätstypen als _plankonform_ gelten.

Standardmäßig wird jede Aktivität mit sich selbst gematcht. Dieses Match kann nicht aufgehoben werden. Gleichzeitig wird eine Aktivität mit allen Aktivitäten ihres {% link_new Aktivitätstyps | features/administration/activity-types-and-properties.md %} gematcht.

Ausnahme: Wenn eine Aktivität zu einem der Aktivitätstypen _Urlaub_, _Krankheit_ oder _Abwesenheit_ gehört, wird sie automatisch mit allen anderen Aktivitäten dieser drei Typen gematcht. Du kannst dieses initiale Match bearbeiten.

{{ 5 | image: 'Matches Übersicht','100%' }}

## Matches bearbeiten

Du kannst die Zuordnung von geplanten Aktivitäten und Aktivitätstypen zu einer _ACD-Aktivität_ bearbeiten:

1. Klicke auf **Aktivitäts-Matches bearbeiten**.
2. Aktiviere eine oder mehrere **Checkboxen** neben den Aktivitäten oder Aktivitätstypen, die Du hinzufügen möchtest. Bereits bestehende Zuordnungen findest Du am Anfang der Liste. Verwende das Suchfeld oberhalb, um die Liste zu filtern.
   {{ 2 | image: 'Matches bearbeiten','40%' }}
3. Klicke auf _Anwenden_{:.doc-button}.
   {{ 1 | image: 'Matches Übersicht','100%' }}

## Matches für die _Offline_ Aktivität erstellen

Wenn Agenten mit einer geplanten Aktivität bei keinem Deiner externen Systeme angemeldet sind, werden sie normalerweise als _Planabweichend_ mit Status _Nicht anwesend_ angezeigt. Je nach System und Konfiguration ist es normal, dass sich Agenten für Pausen, Meetings oder Trainings bei dem externen System abmelden.

Für diesen Fall enthält die Liste der Aktivitäten einen speziellen Eintrag für diesen _Offline_ Status. Durch die Erstellung eines Matches zwischen dem _Offline_ Status und den jeweiligen Aktivitäten verhinderst Du, dass diese Agenten fälschlicherweise als _Planabweichend_ auftauchen. Dies verbessert auch Deinen Adherence-Score.
