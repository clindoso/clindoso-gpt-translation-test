---
title: Objektrechte konfigurieren
description: Der Zugriff auf bestimmte Objekte in injixo kann eingeschränkt werden, sodass Benutzer nur eine Teilmenge z. B. aller Dashboards sehen.
product_label:
  - advanced
  - enterprise
---

In diesem Artikel lernst Du:

- was _Objektrechte_ sind und wie Du sie anwendest.
- wie Du neue Objektberechtigungen erstellst und Benutzern zuweist.
- wie Du die Standardberechtigungen für z. B. Dashboards einschränkst.

## Was sind Objektrechte?

Mit _Objektrechten_ kannst Du den Zugriff auf gewisse Objekte, wie z. B. Dashboards, in injixo einschränken. Im Standard hat ein Benutzer keine Einschränkungen und hat somit Zugriff auf alle verfügbaren Objekte.

Als Benutzer mit _Admin-Zugriff_ kannst Du neue _Objektberechtigungen_ erstellen und diese einem Benutzer zuweisen, um dessen Zugriff auf bestimmte Objekte einzuschränken. Du kannst jedem Benutzer nur eine Berechtigungsgruppe zuweisen.

> Planungseinheiten und andere Objekte aus dem WFM-Bereich verwaltest Du unter in _WFM > Administration > System > Benutzerrollenrechte_{:.breadcrumbs}.

## Objektrechte verwalten

Navigiere zu _Account > Objektrechte_{:.breadcrumbs} für eine Übersicht aller Objektrechte, um diese zu bearbeiten oder neue zu erstellen.

### Neue Objektrechte erstellen

1. Gehe zu _Account > Objektrechte_{:.breadcrumbs}
2. Klicke auf _Objektberechtigung erstellen_{:.doc-button}. Die Seite _Neue Objektberechtigungen_ öffnet sich.
3. Gib einen **Namen** für die neue Gruppe ein.
4. Optional kannst Du eine **Beschreibung** hinzufügen. Diese erscheint in der Übersicht und erleichtert die Verwendung.

{{ 1 | image: 'Neue Objektrechte erstellen', '80%' }}

### Zugriff durch Objektrechte einschränken

Im Standard erlauben _Objektrechte_ den uneingeschränkten Zugriff auf z. B. Dashboards. Dies gilt auch für alle künftigen Objekte einer Kategorie. Um den Zugriff nur auf einige ausgewählte Dashboards zu ermöglichen, musst Du diese einzeln auswählen:

1. Aktiviere das Auswahlfeld **Zugriff einschränken** für z. B. Dashboards im Bereich _Berechtigte Objekte_. Dadurch öffnet sich die Liste aller verfügbaren Dashboards.
2. Aktiviere nun das Auswahlfeld für jedes Element, also Dashboard, welches im Rahmen der neuen Objektrechte verfügbar sein soll. Benutze die Suchfunktion um die Einträge leichter zu finden. Alle ausgewählten Dashboards werden für die Benutzer dieser Berechtigungsgruppe verfügbar sein.
<!-- not in yet --> <!-- Repeat step 1 and 2 for other object types if needed. -->
3. Klicke auf _Erstellen_{:.doc-button}, um die neuen Objektrechte zu speichern.

{{ 2 | image: 'Verfügbare Elemente für eingeschränkte Objektrechte ', '80%' }}

> Neue Objekte sind automatisch verfügbar
>
> Erstellt ein Benutzer z. B. ein neues Dashboard, wird dieses automatisch der Berechtigungsgruppe des aktuellen Benutzers hinzugefügt. Damit ist das neue Dashboard auch für alle anderen Benutzer mit denselben Objektrechten verfügbar.

### Objektrechte für einen Benutzer definieren

Unter _Account > Benutzer_{:.breadcrumbs} kannst Du _Objektrechte_ für alle Benutzer festlegen:

1. Gehe zu _Account > Benutzer_{:.breadcrumbs}.
2. Wähle einen **Benutzer** aus. Scrolle zum Bereich _Objektberechtigungen verwalten_ auf der Seite.
3. Wähle die gewünschten **Objektberechtigungen** aus der Liste aus.
4. Klicke _Speichern_{:.doc-button}, um den Benutzer zu speichern. Dessen Objektrechte sind nun gemäß der ausgewählten Gruppe eingeschränkt.
