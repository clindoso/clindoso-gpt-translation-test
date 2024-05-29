---
title: Agentenstatus-Daten importieren
product_label:
  - advanced
  - enterprise
  - classic
description: Richte injixo korrekt ein, um Agentenstatus-Daten importieren zu können.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-on-premise-integration.md
---

Externe Systeme wie ACDs erfassen, wann Mitarbeiter von einer Aktivität zur nächsten wechseln. injixo kann mit diesen Daten die Tagessteuerung unterstützen.

Neu bei Integrationen? Lerne zuerst {% link_new die Grundlagen| features/acd-integration/cloud/how-integrations-work.md %}.

## Voraussetzungen

Um Agentenstatus-Daten zu importieren, musst du eine {% link_new Integration hinzufügen| features/acd-integration/cloud/how-integrations-work.md | #integration-hinzufügen %}. Die Integration muss den Import von Agentenstatus-Daten unterstützen.

Um herauszufinden, ob deine Integration den Import von Agentenstatus-Daten unterstützt, gehe zu _Account > Integrationen_{:.breadcrumbs}. Wenn verfügbar, zeigen die Integrationen das Label Agentenstatus an für historische Daten bzw. das Label RTA für Echtzeit-Daten.

Nachdem du die Integration hinzugefügt hast, musst du Mitarbeitern in injixo externe Benutzerkennungen hinzufügen. Optional kannst du Aktivitäten aus externen Systemen denselben Aktivitäten in injixo zuordnen.

## Externe Benutzerkennungen

Externe Benutzerkennungen sind herstellerspezifisch. Sie identifizieren die Benutzer im externen System anhand einer E-Mail-Adresse, eines Benutzernamens oder einer Agenten-ID.

Um fehlerhafte Importe zu vermeiden, achte auf die richtige Schreibweise, Groß- und Kleinschreibung und Leerzeichen.

| Anbieter               | Erforderliche Benutzerkennung          |
| ---------------------- | -------------------------------------- |
| Five9                  | Benutzername in Five9                  |
| Genesys Cloud          | Benutzername in PureCloud              |
| Genesys Engage         | Benutzername in PureEngage             |
| Talkdesk               | Verwendete E-Mail-Adresse in Talkdesk  |
| UJET                   | Verwendete E-Mail-Adresse in UJET      |
| Sikom                  | Benutzername in Sikom                  |
| Mitel MiVoice Business | Benutzername in Mitel MiVoice Business |
| Vonage                 | Agenten-ID in Vonage                   |
| Avaya CMS              | Benutzername in Avaya CMS              |

## Mitarbeitern externe Benutzerkennungen in injixo zuordnen

Um Daten importieren zu können, musst du Mitarbeitern externe Benutzerkennungen zuordnen. Du kannst sie allen Mitarbeitern zuordnen oder nur denjenigen, für die du Agentenstatus-Daten importieren möchtest.

1. Gehe zu _WFM > Administration > Scheduling > Mitarbeiter_{:.breadcrumbs} und wähle einen Mitarbeiter aus.
2. Klicke oben auf **Externe Systeme** oder scrolle bis zum Abschnitt **Externe Systeme**.
3. Klicke auf das Hinzufügen-Icon {% icon item-add | icon-only %}, um ein externes System hinzuzufügen.  
   Ein Fenster öffnet sich.
4. Wähle im Dropdown-Menü **Externes System** die Integration aus, die du zuvor eingerichtet hast.
5. Füge im Feld **Mitarbeiter-ID im externen System** eine eindeutige Nummer für den Mitarbeiter hinzu, z.&nbsp;B. die Personalnummer des Mitarbeiters.
6. Gib im Feld **Erweiterung** die Kennung für den Mitarbeiter im externen System ein, z.&nbsp;B. die E-Mail-Adresse des Mitarbeiters.
7. Klicke auf _OK_{:.doc-button}.

Sobald du die Mitarbeiterkonfiguration aktualisiert hast, werden mit dem nächsten Import Agentenstatus-Daten importiert.

## Aktivitäten aus externen Systemen den Aktivitäten in injixo zuordnen

Aktivitäten aus externen Systemen sind die Aktivitäten, die das externe System aufzeichnet, wenn Mitarbeiter sich anmelden, abmelden oder von einer Aktivität zu einer anderen wechseln, z.&nbsp;B. von E-Mails zu Anrufe.

Du kannst Aktivitäten aus externen Systemen bestehenden Aktivitäten zuordnen. Wenn du stattdessen {% link_new neue Aktivitäten erstellen | features/administration/activities.md | #aktivität-erstellen %} möchtest, denke daran, diese deiner {% link_new Planungseinheit | features/administration/create-and-manage-planning-units.md | #aktivitäten-hinzufügen %} hinzuzufügen, damit sie korrekt angezeigt werden können.

Standardmäßig speichern Integrationen solche Aktivitäten in der Aktivität Anwesend (ID 1) und der Agentenstatus wird für alle Aktivitäten als Anwesend angezeigt. injixo kann dieselben Aktivitäten anzeigen wie dein externes System. Dazu musst du wie folgt die Aktivitäten aus externen Systemen anderen Aktivitäten in injixo neu zuordnen.

Um Aktivitäten neu zuzuordnen, pausiere als erstes die Integration:

1. Gehe zu _Account > Integrationen_{:.breadcrumbs}.
2. Klicke in der Integrationsliste neben der Integration, für die du Aktivitäten neu zuordnen möchtest, auf das Icon Importieren pausieren {% icon pause_circle | icon-only %}.

Sobald du die Integration pausiert hast, gehe wie folgt vor:

1. Gehe zu _Plan > Konfiguration > Aktivitäten_{:.breadcrumbs}.
2. Wähle die Aktivität aus, die du neu zuordnen möchtest.
3. Klicke im Abschnitt **Externe Systeme** auf _In WFM bearbeiten_{:.doc-button}.
4. Gehe zum Abschnitt **Externe Systeme**.
5. Klicke auf das Hinzufügen-Icon {% icon item-add | icon-only %}.
6. Führe im Fenster **Externe Systeme** folgende Schritte aus:<br>
   - Wähle aus dem Dropdown-Menü **Externes System** deine Integration.
   - Wähle aus dem Dropdown-Menü **Bezeichnung im externen System** die Aktivität im externen System aus, die du der aktuell ausgewählten injixo-Aktivität zuordnen möchtest.
   - Wähle aus dem Dropdown-Menü **Klassifikation** den Wert 1.
7. Klicke auf _OK_{:.doc-button}.

Um weitere Aktivitäten neu zuzuordnen, klicke auf die nächste Aktivität und fahre im Konfigurationsmenü auf der rechten Seite fort.

Wenn du die Aktivitätenzuordnung abgeschlossen hast, gehe zu _Account > Integrationen_{:.breadcrumbs} und klicke auf das Icon Importieren wiederaufnehmen {% icon play_circle | icon-only %} neben der Integration, um den Import fortzusetzen.
