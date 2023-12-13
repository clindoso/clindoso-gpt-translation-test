---
title: Externes System definieren
toc: false
product_label:
  - on-premise
description: Lerne, was externe Systeme sind und wie Du sie erstellst.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-overview.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/xlink-configuration-import-odbc.md
---

<div markdown="1" class="hint-box-default hint-box-red">

Xlink-Integration ist veraltet

Falls Du in Deinem injixo Cloud WFM-Plan noch Xlink verwendest, aktualisiere Deine Integration bitte umgehend auf injixo Cloud Link oder eine Lösung, die den neuesten Integrationsstandards entspricht. Unsere Customer Experience-Experten können Dir dabei helfen. Kontaktiere sie [hier](https://www.injixo.com/contact/?message_type=support-enquiry&message=Ich%20m%C3%B6chte%20Unterst%C3%BCtzung%20beim%20Update%20meiner%20Integration.%20Mir%20ist%20bewusst,%20dass%20dies%20notwendig%20ist,%20um%20den%20Datenimport%20zu%20injixo%20auch%20nach%20dem%2030.%20Januar%202023%20ohne%20Unterbrechung%20zu%20gew%C3%A4hrleisten.).

</div>

In diesem Artikel lernst Du:

- was ein externes System ist und warum Du es benötigst.
- wie Du ein externes System erstellst.

## Was ist ein externes System?

Externe Systeme sind für den Datenimport mit Xlink erforderlich.

> Du benötigst kein externes System, um Daten mit einer {% link_new Integration | features/acd-integration/cloud/how-integrations-work.md %} hochzuladen.

Externe Systeme definieren, welche Xlink (Standard-)Schnittstelle verwendet wird, um Daten über ODBC- oder CSV-Dateien abzurufen. Die Schnittstellen hinter externen Systemen verwenden eine herstellerspezifische, starre Konfiguration und Import-Logik, um eine Verbindung herzustellen und Daten aus der ACD oder Datei zu lesen.

Die verfügbaren Universal- und CSV-Schnittstellen sind etwas flexibler, da sie ein Format für Dateien oder Tabellen definieren können, aus denen Xlink Daten liest. Die entsprechenden Handbücher für diese Schnittstellen sind auf [downloads.injixo.com](https://downloads.injixo.com) verfügbar.

## Ein externes System erstellen

1. Gehe zu _WFM > Administration > System > Externes System_{:.breadcrumbs}.
2. Klicke auf das {% icon item-add %}.
3. Wähle unter **Systembeschreibung** entweder **CSV Files**, **Universal** oder eine **spezifische Schnittstelle** für Deine ACD.
4. Gib einen **Namen** ein, um die Datenquelle später identifizieren zu können.
5. Aktiviere die Checkboxen **PhoneLink** (für Anrufdaten) und (**TimeLink**) (für Agentstatusdaten). Nicht alle Schnittstellen unterstützen beide Optionen.
6. Klicke auf _OK_{:.doc-button}.
