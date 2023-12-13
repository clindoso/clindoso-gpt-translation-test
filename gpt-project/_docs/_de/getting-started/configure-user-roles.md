---
title: Benutzerrollen konfigurieren
redirect_from:
  - /de/user-and-role-authorization/
redirect_reason: renamed file in June 2021
description: Erfahre, welche Benutzerrollen es gibt, wie du ihre Berechtigungen änderst, neue Benutzerrollen erstellst und Benutzern Rollen zuweist.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-user-accounts.md
---

## Was sind Benutzerrollen?

In einer Benutzerrolle werden Zugriffsrechte für Benutzer zusammengefasst. Diese beziehen sich auf:

- die Produkte und Features in injixo, z.&nbsp;B. _Forecast_{:.menu-item}.
- die Features in WFM, z.&nbsp;B. _WFM > Administration_{:.breadcrumbs}.

In injixo gibt es Rollenkategorien. In jeder ist eine {% link_new Standard-Benutzerrolle | getting-started/default-user-roles.md | #standard-benutzerrollen %} angelegt, die voreingestellte Zugriffsrechte, d.&nbsp;h. Berechtigungen, enthält. Wenn du eine neue Benutzerrolle innerhalb einer Rollenkategorie anlegst, erhält sie automatisch dieselben Zugriffsrechte auf Produkte und Features wie die Standard-Benutzerrolle.<br>
Die Rollenkategorie Sonstige hat keine Standard-Benutzerrolle.

### Benutzerrollen anzeigen und verwalten

Gehe zu _Account > Rollen_{:.breadcrumbs}.  
   Benutzerrollen werden in bereits bestehenden Rollenkategorien zusammengefasst (z.&nbsp;B. in der Rollenkategorie Planer). Die Rollenkategorien können dabei helfen, einen Überblick über die Zugriffsrechte zu behalten und diese leichter zu verwalten. Du kannst eine Benutzerrolle per Drag-and-Drop von einer Rollenkategorie in eine andere verschieben oder einzelne Benutzerrollen über die Suchfunktion finden.
   
   > Berechtigungen für neue Funktionalitäten werden auf Basis der Rollenkategorie vergeben  
   >   
   > Berechtigungen für neue injixo-Funktionalitäten werden den Benutzerrollen automatisch zugewiesen. Welche Berechtigungen sie erhalten, hängt von ihrer Rollenkategorie ab. Wenn es beispielsweise eine neue Funktionalität für Planer gibt, erhalten alle Benutzerrollen in der Rollenkategorie Planer die entsprechenden Zugriffsrechte. Wenn du eine Benutzerrolle aus der Rollenkategorie Planer in eine andere Rollenkategorie verschoben hast, erhält diese Benutzerrolle keine automatischen Berechtigungen mehr für neue Planer-Funktionalitäten. Bei Bedarf kann ein Benutzer mit Admin-Zugriff die Berechtigungen manuell zur Benutzerrolle hinzufügen. Das gleiche gilt für Benutzerrollen in der Rollenkategorie Sonstige. Ihre Berechtigungen müssen immer manuell hinzugefügt werden.

   {{ 1 | image: "Überblick über Rollenkategorien", '80%' }}

### Neue Benutzerrolle erstellen

1. Klicke auf das blaue {% icon blue_plus %} in einer Rollenkategorie.<br>Um mehr über eine Rollenkategorie zu erfahren, bewege den Mauszeiger über das jeweilige Informations-Icon {% icon info_circle | icon-only %}.

   - Rollenkategorie Sonstige: Erstellt eine leere Benutzerrolle. Es sind keine Standardberechtigungen festgelegt.
   - Rollenkategorien der {% link_new Standard-Benutzerrollen | getting-started/default-user-roles.md %}: Standardberechtigungen für injixo-Komponenten sind vorausgewählt. Die Zugriffsrechte für WFM-Features sind nicht festgelegt. 
  > Hinweis
  >
  > Wenn du eine neue Benutzerrolle erstellst, musst du die [Zugriffsrechte für die Features in WFM manuell festlegen](#berechtigungen-für-wfm-konfigurieren).

2. So konfigurierst du die Benutzerrolle auf der Seite **Benutzerrolle erstellen**:

   - **Allgemeine Informationen**: Gib einen **Namen**, eine **Abkürzung** und optional eine **Beschreibung** ein.
   - **Rollenkategorie**: Zeigt die vorausgewählte **Rollenkategorie** an.

3. (Optional) Bearbeite die Standardberechtigungen.<br>Im Abschnitt **Berechtigungen** zeigt ein graues Häkchen-Icon neben dem Komponentennamen an, dass alle Berechtigungen für diese Komponente standardmäßig vergeben sind. Ein graues Minus-Icon zeigt an, dass einige Berechtigungen für diese Komponente nicht standardmäßig vergeben werden.  
   - Produkt: Um Berechtigungen für alle Features innerhalb eines Produkts zu vergeben, aktiviere die Checkbox neben dem Produktnamen.
   - Feature: Um Berechtigungen für einzelne Features zu vergeben, klicke auf den nach unten zeigenden Pfeil neben einem Produktnamen. Aktiviere die Checkbox(en) neben den Features.
   - Um alle Unterkategorien anzuzeigen, klicke auf **Alle ausklappen**. Um alle Unterkategorien zu schließen, klicke auf **Alle einklappen**.
   - Um bereits ausgewählte Berechtigungen auf die Standard-Benutzerrolle zurückzusetzen, klicke auf **Auf Standardeinstellungen zurücksetzen**.
4. Um die neue Benutzerrolle zu speichern, klicke auf _Benutzerrolle erstellen_{:.doc-button}.<br>Um die [WFM-Berechtigungen](#berechtigungen-für-wfm-konfigurieren) für die neue Benutzerrolle festzulegen, gehe zu _Erstellen und zu Benutzerrollenrechte gehen_{:.doc-button}.

   {{ 2 | image: "Ansicht Benutzerrolle erstellen", '80%' }}

### Benutzerrolle einem Benutzer zuweisen

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Klicke auf einen Namen.
3. Aktiviere eine oder mehrere Checkboxen unter **Benutzerrolle(n) zuweisen**. Um die angezeigten Benutzerrollen zu filtern, verwende das Eingabefeld **Suche Benutzerrollen**.
4. Klicke auf _Speichern_{:.doc-button}.

   {{ 6 | image: 'Benutzerrollen zuweisen', '80%'}}

## Berechtigungen für WFM konfigurieren

1. Wähle unter _Account > Rollen_{:.breadcrumbs} eine Benutzerrolle aus.
2. Klicke im Abschnitt **Berechtigungen** auf _Gehe zu Benutzerrollenrechte_{:.doc-button}.  
   Du wirst zu _WFM > Administration > System > Benutzerrollenrechte_{:.breadcrumbs} weitergeleitet.
3. Aktiviere oder deaktiviere die Checkboxen im Abschnitt **Navigator** auf der rechten Seite, um Berechtigungen hinzuzufügen oder zu entfernen.

{{ 4 | image: "Abschnitt Navigator in WFM Benutzerrollenrechte", '60%' }}

Wir empfehlen, nur rollenbasierte Berechtigungen zu verwenden. Du kannst bei Bedarf Berechtigungen für einzelne Benutzer anpassen. Um individuelle Berechtigungen zu ändern, gehe zu _WFM > Administration > System > Benutzerrechte_{:.breadcrumbs}.

## Teamzugriff verwalten: Zugriff auf Stammdaten einschränken

Wenn es in deinem Unternehmen mehrere Teams gibt und du den Zugriff auf die Daten der Teams einschränken möchtest, kannst du einem Benutzer mehr als eine Benutzerrolle zuweisen. injixo kombiniert dann die Berechtigungen, die in den verschiedenen Benutzerrollen festgelegt sind. Du kannst den Zugriff auf Elemente wie Planungseinheiten, Tagesmodelle, Aktivitäten oder Reports einschränken.

**Beispiel**

Wenn alle deine Planer auf den Schichtplan zugreifen können sollen, aber jeder Planer nur die Daten seiner eigenen Planungseinheit bearbeiten können soll, kannst du jedem Planer zwei Benutzerrollen zuweisen.

Du kannst eine neue Benutzerrolle erstellen, die keinen Zugriff auf bestimmte Planungseinheiten hat oder einer bestehenden Benutzerrolle den Zugriff auf alle Planungseinheiten entziehen. Um einer bestehenden Benutzerrolle den Zugriff auf alle Planungseinheiten zu entziehen, gehe wie folgt vor:

1. Gehe zu _Account > Rollen_{:.breadcrumbs}.
2. Klicke auf die Benutzerrolle.
3. Klicke auf _Gehe zu Benutzerrollenrechte_{:.doc-button}.
4. Scrolle rechts zum Abschnitt **Planungseinheiten** (oder nutze den Quick-Link oben).
5. Klicke auf das {% icon item-delete %} neben dem Eintrag [Alle], um den Zugriff auf alle Planungseinheiten zu entziehen.
6. Klicke auf _OK_{:.doc-button}.

Füge wie folgt Zugriff auf bestimmte Planungseinheiten hinzu:

1. Wähle die zweite Benutzerrolle aus.
2. Klicke im Abschnitt **Planungseinheiten** auf das {% icon item-add %}.
3. Wähle die Planungseinheit(en) aus der Liste aus. Drücke **STRG** oder **Shift**, während du klickst, um mehrere Planungseinheiten auszuwählen.
4. Aktiviere eine oder mehrere Checkboxen unter **Zugriffsrechte**, um Rechte zum Lesen, Bearbeiten und Löschen festzulegen.
5. Klicke auf _OK_{:.doc-button}.

Um die Konfiguration abzuschließen, gehe zu _Account > Benutzer_{:.breadcrumbs} und [weise Benutzern die Benutzerrollen zu](#benutzerrolle-einem-benutzer-zuweisen).


## Benutzerdefinierte oder Standard-Benutzerrolle bearbeiten

1. Gehe zu _Account > Rollen_{:.breadcrumbs}.
2. Klicke auf den Benutzerrollen-Eintrag, den du ändern möchtest.
3. Führe die gewünschten Änderungen an der Benutzerrolle durch und klicke auf _Änderungen speichern_{:.doc-button}.

## Benutzerdefinierte Benutzerrolle löschen

1. Gehe zu _Account > Rollen_{:.breadcrumbs}.
2. Klicke auf den Benutzerrollen-Eintrag.
3. Klicke unten rechts auf _Benutzerrolle löschen_{:.doc-button}. Die Standard-Benutzerrollen sind nicht löschbar.
