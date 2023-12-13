---
title: Xlink Agenten-Aktivitätsdaten mappen
product_label:
  - on-premise
redirect_from: /de/xlink-mapping-activities/
redirect_reason: renamed file in September 2021
---

In diesem Artikel lernst Du, wie Du die externen Aktivitäts- und Anmelde-IDs aus externen Systemen mit Mitarbeitern und Aktivitäten in injixo verknüpfst. Wir nennen diesen Prozess Mapping.

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

> Dieser Artikel bezieht sich auf Xlink. Lies den Artikel {% link_new Agentenstatus-Daten importieren | features/acd-integration/cloud/import-agent-status-data.md %}, wenn Du eine Integration konfigurieren möchtest.

Eine Aktivität in einem externen System stellt eine Tätigkeit oder einen Skill dar, auf die sich ein Mitarbeiter, z.B. per Eingabe eines Codes im externen System, anmeldet. Je nach Schnittstelle stehen unterschiedliche Aktivitäten aus dem externen System zur Verfügung. Die jeweilige Schnittstellen-Dokumentation mit weiteren Informationen ist unter [downloads.injixo.com](https://downloads.injixo.com) verfügbar.

## Externe Aktivitäten den Aktivitäten in injixo zuordnen

Standardmäßig speichert eine Xlink alle importierten externen Aktivitäten Deines Systems in der Aktivität _Anwesend_, der die ID 1 zugeordnet ist. Daher wird der Agentenstatus für alle Aktivitäten ebenfalls als _Anwesend_ angezeigt. Um stattdessen die tatsächlichen Aktivitäten angezeigt zu bekommen, gehst Du folgendermaßen vor:

Erstelle für jede Aktivität, die in _Anwesend_ gespeichert ist, eine neue Aktivität.

1. Gehe zu _WFM > Administration > Scheduling > Aktivitäten_{:.breadcrumbs}.
2. Klicke auf **Anwesend** in der Liste der Aktivitäten, dann auf **Externes System**. Du siehst nun eine Liste aller Aktivitäten, die vom Xlink importiert wurden.
3. Für jede dieser Aktivitäten, {% link_new erstelle eine neue Aktivität | features/administration/activities.md | #aktivität-erstellen %}, falls sie nicht bereits existiert.
4. Klicke dann erneut auf die Aktivität **Anwesend** und auf **Externes System**.
5. Klicke bei jeder **Aktivität** auf _![remove button](/assets/img/common/item-delete.gif)_{:.doc-button-icon}, um sie aus der Aktivität **Anwesend** zu entfernen.
6. Klicke auf _OK_{:.doc-button}.

Nun ordnest Du die Aktivitäten aus dem externen System den neu erstellten Aktivitäten zu:

1. Klicke auf eine der **Aktivitäten**, die Du gerade erstellt hast und dann auf **Externes System**.
2. Klicke auf das {% icon item-add %}.
3. Wähle unter **Externes System** Dein externes System aus.
4. Für **Externe Aktivität**, wähle die externe Aktivität aus, die Du mit der aktuellen Aktivität verbinden möchtest.
5. Wähle _1_ für **Klassifizierung**.
6. Klicke auf _OK_{:.doc-button}.
7. Ändere alle Aktivitäten, die Du erstellt hast, auf die gleiche Weise.

> Damit Deine neu erstellten Aktivitäten korrekt angezeigt werden, füge sie Deiner {% link_new Planungseinheit | features/administration/create-and-manage-planning-units.md | #aktivitäten-hinzufügen %} unter _WFM > Administration > Scheduling > Planungseinheiten_{:.breadcrumbs} hinzu.

Einer WFM-Aktivität können mehrere externe Aktivitäten zugeordnet werden. Umgekehrt kann einer externen Aktivität aber nur genau eine WFM-Aktivität zugeordnet werden.

## Mitarbeitern Externe Login-IDs zuordnen

Deine Mitarbeiter haben im externen System eine eindeutige ID, mit welcher sie sich anmelden. Gehe zu _WFM > Administration > Scheduling > Mitarbeiter_{:.breadcrumbs} und weise jedem Mitarbeiter die richtige externe Benutzerkennung zu.

1. Klicke auf einen **Mitarbeiter**.
2. Suche oben den Link **Externes System** und klicke ihn an. Die Seite scrollt nach unten zum Abschnitt Externes System.
3. Klicke auf das {% icon item-add %}, um ein externes System hinzuzufügen. Es öffnet sich ein neues Fenster.
4. Wähle das **Externe System** aus.
5. Füge bei **Mitarbeiter-ID im externen System** die ID aus der ACD für den Mitarbeiter hinzu. Die ID darf nur Zahlen enthalten.
6. Klicke auf _OK_{:.doc-button}.

Wiederhole den Vorgang für alle Mitarbeiter. Eine fehlende oder falsche Benutzerkennung bewirkt, dass kein Daten-Import durchgeführt wird. Nachdem Du die externe Benutzerkennung für alle Mitarbeiter hinzugefügt hast, kannst Du Daten importieren.

{{ 1 | image: 'Mitarbeiter Externe Systeme', '75%' }}

{{ 2 | image: 'Externe Systeme Dialog', '75%' }}

Du kannst einem Mitarbeiter im WFM mehrere externe Mitarbeiter-IDs zuordnen, allerdings kannst Du umgekehrt eine externe Mitarbeiter-ID höchstens einem WFM-Mitarbeiter zuordnen.
