---
title: Benutzerrollen konfigurieren
redirect_from:
  - de/user-and-role-authorization/
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

Eine Benutzerrolle fasst eine Gruppe von Benutzern zusammen, die dieselben Berechtigungen und Zugriffsrechte auf die Produkte und Features in injixo haben, z.&nbsp;B. _Forecast_{:.menu-item} bzw. auf Features in WFM, z.&nbsp;B. _WFM > Administration_{:.breadcrumbs}.

In injixo gibt es Rollenkategorien. In jeder Rollenkategorie ist eine {% link_new Standard-Benutzerrolle | getting-started/default-user-roles.md | #standard-benutzerrollen %} angelegt, die voreingestellte Berechtigungen enthält. Wenn du eine neue Benutzerrolle innerhalb einer Rollenkategorie anlegst, erhält sie automatisch dieselben Berechtigungen für Produkte und Features wie die Standard-Benutzerrolle in dieser Rollenkategorie.<br>
Die Rollenkategorie **Sonstige** hat keine Standard-Benutzerrolle.

### Benutzerrollen anzeigen und verwalten

Gehe zu _Account > Rollen_{:.breadcrumbs}.

   Benutzerrollen werden in Rollenkategorien zusammengefasst (z.&nbsp;B. in der Rollenkategorie **Planer**). Die Rollenkategorien können dabei helfen, einen Überblick über die Berechtigungen zu behalten und diese leichter zu verwalten. Du kannst eine Benutzerrolle per Drag-and-Drop von einer Rollenkategorie in eine andere verschieben oder einzelne Benutzerrollen über die Suchfunktion finden.
   
   > Berechtigungen für neue Funktionalitäten 
   >   
   > Berechtigungen für neue injixo-Funktionalitäten werden den Benutzerrollen automatisch zugewiesen. Welche Berechtigungen sie erhalten, hängt von ihrer Rollenkategorie ab. Wenn es beispielsweise eine neue Funktionalität für Planer gibt, erhalten alle Benutzerrollen in der Rollenkategorie **Planer** die entsprechenden Berechtigungen. Wenn du eine Benutzerrolle aus der Rollenkategorie **Planer** in eine andere Rollenkategorie verschoben hast, erhält diese Benutzerrolle keine automatischen Berechtigungen mehr für neue **Planer**-Funktionalitäten. Bei Bedarf kann ein Benutzer mit Admin-Zugriff die Berechtigungen manuell zur Benutzerrolle hinzufügen.<br> Das Gleiche gilt für Benutzerrollen in der Rollenkategorie **Sonstige**: Ihre Berechtigungen müssen immer manuell hinzugefügt werden.

### Neue Benutzerrolle erstellen

1. Klicke auf das blaue {% icon blue_plus %} in einer Rollenkategorie.

   - Rollenkategorie **Sonstige**: Erstellt eine leere Benutzerrolle. Es sind keine Standardberechtigungen festgelegt.
   - Rollenkategorien der {% link_new Standard-Benutzerrollen | getting-started/default-user-roles.md %}: Standardberechtigungen für injixo-Komponenten sind vorausgewählt. Die Berechtigungen für WFM-Features sind nicht festgelegt.
  > Hinweis
  >
  > Wenn du eine neue Benutzerrolle erstellst, musst du die [Berechtigungen für die Features in WFM manuell festlegen](#berechtigungen-für-wfm-konfigurieren).

2. So konfigurierst du die Benutzerrolle auf der Seite **Benutzerrolle erstellen**:

   - **Allgemeine Informationen**: Gib einen **Namen**, eine **Abkürzung** und optional eine **Beschreibung** ein.
   - **Rollenkategorie**: Zeigt die vorausgewählte **Rollenkategorie** an.

3. (Optional) Bearbeite die Standardberechtigungen. Im Abschnitt **Berechtigungen** zeigt ein graues Häkchen-Icon neben dem Komponentennamen an, dass alle Berechtigungen für diese Komponente standardmäßig vergeben sind. Ein graues Minus-Icon zeigt an, dass einige Berechtigungen für diese Komponente nicht standardmäßig vergeben werden.
   - Komponente: Um Berechtigungen für alle Features innerhalb einer Komponente zu vergeben, aktiviere die Checkbox neben dem Komponentennamen.
   - Feature: Um Berechtigungen für einzelne Features zu vergeben, klicke auf den nach unten zeigenden Pfeil neben einem Komponentennamen. Aktiviere die Checkbox(en) neben den Features.
   - Um alle Unterkategorien anzuzeigen, klicke auf **Alle ausklappen**. Um alle Unterkategorien zu schließen, klicke auf **Alle einklappen**.
   - Um bereits ausgewählte Berechtigungen auf die Standard-Benutzerrolle zurückzusetzen, klicke auf **Auf Standardeinstellungen zurücksetzen**.
4. Um die neue Benutzerrolle zu speichern, klicke auf _Benutzerrolle erstellen_{:.doc-button}. Um die [WFM-Berechtigungen für die neue Benutzerrolle festzulegen](#berechtigungen-für-wfm-konfigurieren), klicke auf _Erstellen und zu Benutzerrollenrechte gehen_{:.doc-button}.

### Benutzerrolle einem Benutzer zuweisen

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Klicke auf einen Namen.
3. Aktiviere eine oder mehrere Checkboxen unter **Benutzerrolle(n) zuweisen**. Um die angezeigten Benutzerrollen zu filtern, verwende das Eingabefeld **Suche Benutzerrollen**.
4. Klicke auf _Speichern_{:.doc-button}.

## Berechtigungen für WFM konfigurieren

1. Wähle unter _Account > Rollen_{:.breadcrumbs} eine Benutzerrolle aus.
2. Klicke im Abschnitt **Berechtigungen** auf **Gehe zu Benutzerrollenrechte**.  
   Du wirst zu _WFM > Administration > System > Benutzerrollenrechte_{:.breadcrumbs} weitergeleitet.
3. Aktiviere oder deaktiviere die Checkboxen im Abschnitt **Navigator** auf der rechten Seite, um Berechtigungen hinzuzufügen oder zu entfernen.

{{ 4 | image: "Abschnitt Navigator in WFM Benutzerrollenrechte", '60%' }}

> Hinweis
>
> Individuelle Berechtigungen für einzelne Benutzer können rollenbasierte Berechtigungen überschreiben. Dies trifft auch auf Benutzer mit Admin-Zugriff zu.
>
> Verwende nach Möglichkeit immer nur die rollenbasierten Berechtigungen. Du kannst die Berechtigungen für einzelne Benutzer unter _WFM > Administration > System > Benutzerrechte_{:.breadcrumbs} anpassen. Beachte, dass diese Änderungen die rollenbasierten Berechtigungen überschreiben. 
>
> Um bestimmte Benutzerberechtigungen zurückzusetzen, musst du möglicherweise vorübergehend den Admin-Zugriff entfernen, um die ausgegrauten Checkboxen auf der Seite **Benutzerrechte** zu aktivieren. Klicke auf das Zurücksetzen-Icon {% icon asterisk | icon-only %}, um die Rolle auf die Standardeinstellungen zurückzusetzen.

## Teamzugriff verwalten: Zugriff auf Stammdaten einschränken

Wenn es in deinem Unternehmen mehrere Teams gibt und du den Zugriff auf die Daten der Teams einschränken möchtest, kannst du einem Benutzer mehr als eine Benutzerrolle zuweisen. injixo kombiniert dann die Berechtigungen, die in den verschiedenen Benutzerrollen festgelegt sind. Du kannst den Zugriff auf Elemente wie Planungseinheiten, Tagesmodelle, Aktivitäten oder Reports einschränken.

**Beispiel**

Wenn alle deine Planer auf den Schichtplan zugreifen können sollen, aber jeder Planer nur die Daten seiner eigenen Planungseinheit bearbeiten können soll, kannst du jedem Planer zwei Benutzerrollen zuweisen.

Du kannst eine neue Benutzerrolle erstellen, die keinen Zugriff auf bestimmte Planungseinheiten hat oder einer bestehenden Benutzerrolle den Zugriff auf alle Planungseinheiten entziehen. Um einer bestehenden Benutzerrolle den Zugriff auf alle Planungseinheiten zu entziehen, gehe wie folgt vor:

1. Gehe zu _Account > Rollen_{:.breadcrumbs}.
2. Klicke auf die Benutzerrolle.
3. Klicke auf **Gehe zu Benutzerrollenrechte**.
4. Scrolle rechts zum Abschnitt **Planungseinheiten** (oder nutze den Quick-Link oben).
5. Klicke auf das {% icon item-delete %} neben dem Eintrag [Alle], um den Zugriff auf alle Planungseinheiten zu entziehen.
6. Klicke auf _OK_{:.doc-button}.

Um Zugriff auf bestimmte Planungseinheiten hinzuzufügen, gehe wie folgt vor:

1. Wähle die zweite Benutzerrolle aus.
2. Klicke im Abschnitt **Planungseinheiten** auf das {% icon item-add %}.
3. Wähle die Planungseinheit(en) aus der Liste aus. Drücke **STRG** oder **Shift**, während du klickst, um mehrere Planungseinheiten auszuwählen.
4. Aktiviere eine oder mehrere Checkboxen unter **Zugriffsrechte**, um Rechte zum Lesen, Bearbeiten und Löschen festzulegen.
5. Klicke auf _OK_{:.doc-button}.

Um die Konfiguration abzuschließen, gehe zu _Account > Benutzer_{:.breadcrumbs} und [weise Benutzern die Benutzerrollen zu](#benutzerrolle-einem-benutzer-zuweisen).

## Benutzerdefinierte oder Standard-Benutzerrollen bearbeiten

1. Gehe zu _Account > Rollen_{:.breadcrumbs}.
2. Wähle die Benutzerrolle aus, die du ändern möchtest.
3. Führe die Änderungen an der Benutzerrolle durch und klicke auf _Änderungen speichern_{:.doc-button}.

## Benutzerdefinierte Benutzerrollen löschen

1. Gehe zu _Account > Rollen_{:.breadcrumbs}.
2. Klicke auf die Benutzerrolle.
3. Klicke unten rechts auf _Benutzerrolle löschen_{:.doc-button}. Du kannst keine Standard-Benutzerrollen löschen.
