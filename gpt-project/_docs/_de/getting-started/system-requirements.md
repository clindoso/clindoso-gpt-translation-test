---
title: Systemanforderungen
description: Browser- und Desktop-Anforderungen für Integrationen und Arbeitsplätze von Agenten und Planern.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/browser-setup.md
---

injixo ist eine browserbasierte Workforce Management SaaS-Software, die in mehreren [WFM-Plänen](https://www.injixo.com/pricing) verfügbar ist: injixo Essential WFM, injixo Advanced WFM und injixo Enterprise WFM.

## Browser-Anforderungen

injixo unterstützt die neuesten beiden Versionen der folgenden Browser:

- Microsoft Edge
- Google Chrome
- Mozilla Firefox
- Apple Safari

## Pop-up-Blocker

injixo nutzt Pop-ups, um zusätzliche Dialogfenster anzuzeigen. Um Pop-ups für injixo zuzulassen, gehe wie folgt vor:

- Deaktiviere deinen Pop-up-Blocker in [Microsoft Edge](https://support.microsoft.com/de-de/microsoft-edge/blockieren-von-popups-in-microsoft-edge-1d8ba4f8-f385-9a0b-e944-aa47339b6bb5).
- Lege eine Ausnahme für den Pop-up-Blocker in [Google Chrome](https://support.google.com/chrome/answer/95472?hl=de&co=GENIE.Platform%3DDesktop#zippy=%2Callow-pop-ups-and-redirects-from-a-site),[ Mozilla Firefox](https://support.mozilla.org/de/kb/pop-blocker-einstellungen-ausnahmen-problemloesung) und [Apple Safari](https://support.apple.com/de-de/guide/safari/sfri40696/mac) fest.

## Microsoft Edge im Internet Explorer (IE)-Modus

ActiveX-basierte Funktionen in WFM erfordern {% link_new Microsoft Edge im IE-Modus | support/faq/configure-edge-internet-explorer-mode.md %}. Um den IE-Modus zu konfigurieren, benötigst du eine [XML-Datei mit der Site List](https://learn.microsoft.com/de-de/deployedge/edge-ie-mode-local-site-list).

<style>
table {
  width: 100%;
}
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

| WFM-Plan                               | Microsoft Edge in IE-Mode erforderlich         |
| -------------------------------------- | ------------------------------------------ |
| Essential WFM                          | Nein                                         |
| Advanced WFM                           | Nein                                         |
| Enterprise WFM                         | Nur bei Nutzung kundenspezifischer Features            |
| Classic <sup>1</sup>                   | Ja                                        |
| Enterprise WFM On-premise <sup>1</sup> | Ja. Wenn Microsoft Edge im IE-Modus nicht konfiguriert ist, kannst du dich nicht anmelden. |

<sup>1</sup> Legacy-Software (alte WFM-Pläne, die aktuell noch genutzt werden)

Verwendest du einen anderen Browser oder eine falsche IE-Modus-Konfiguration, zeigt das IE-Symbol in der WFM-Navigation an, welche Features den IE-Modus erfordern (Classic/Enterprise WFM).

{% link_new injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} funktioniert mit jedem aufgelisteten Browser auf Computern, Smartphones und Tablets.

## injixo Client Software

ActiveX-basierte Features WFM erfordern den {% link_new injixo Client | getting-started/browser-setup.md %}.

Die Betriebssystemanforderungen findest du in der Download-Beschreibung unter [downloads.injixo.com](https://downloads.injixo.com/de).

| WFM-Plan                      | injixo-Client erforderlich                |
| ------------------------- | ----------------------------------------- |
| Essential WFM             | Nein                                        |
| Advanced WFM              | Nein                                        |
| Enterprise WFM            | Nur bei Nutzung kundenspezifischer Features           |
| Classic                   | Ja                                       |
| Enterprise WFM On-premise | Ja. Wenn der injixo-Client nicht installiert ist, kannst du dich nicht anmelden. |

Wenn der injixo-Client nicht installiert ist, zeigt das IE-Symbol in der linken Navigation an, welche Features den IE-Modus erfordern (Classic/Enterprise WFM).

Für {% link_new injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} ist der injixo-Client nicht erforderlich.

## Firewall-Ausnahmen

Damit du auf die injixo-Webseiten zugreifen kannst, musst du Datenverkehr von und nach *.injixo.com über Port 443 zulassen.

Wenn du ActiveX-basierte Features, Xlink oder kundenspezifische SDK-Anwendungen verwendest, füge eine weitere Firewall-Ausnahme hinzu. Diese Anwendungen verwenden Port 45054 für ausgehenden Datenverkehr (Port 80 für injixo-Hosts vor 2019) und erfordern direkten Internetzugang über Transmission Control Protocol (TCP). Im Browser konfigurierte Proxy Server werden nicht unterstützt.

Um die Adresse für die Firewall-Ausnahme zu erhalten, klicke auf *WFM*{:.menu-item} und verwende den Namen deines injixo-Hosts, der in der Adressleiste des Browsers sichtbar ist, z.&nbsp;B. wfm-123abc.injixo.com.

Um mehr über Firewall-Ausnahmen in Windows zu erfahren, siehe die [Microsoft-Dokumentation](https://support.microsoft.com/de-de/windows/hinzuf%C3%BCgen-eines-ausschlusses-zu-windows-sicherheit-811816c0-4dfd-af4a-47e4-c301afe13b26#:~:text=Go%20to%20Start%20%3E%20Settings%20%3E%20Update,%2C%20file%20types%2C%20or%20process).

### URLs für WebSockets freigeben

Um Echtzeit-Updates an Benutzer zu senden, z.&nbsp;B. im {% link_new Schicht Center | features/scheduling/shiftcenter/shift-center-overview.md %} oder für Echtzeit Adherence, nutzt injixo das WebSocket-Protokoll (basierend auf TCP) über Port 443\. injixo öffnet eine Webseite, die eine WebSocket-Verbindung aufbaut. Füge die folgenden URLs zur Allowlist hinzu:

- https://shiftcenter.injixo.com
- wss://shiftcenter.injixo.com
- https://www.injixo.com
- wss://ws.injixo.com

In injixo Advanced und injixo Enterprise WFM benötigt das Schicht Center WebSockets, um optimal zu funktionieren. Die zugrundeliegende Technologie bietet einen langsameren Fallback-Mechanismus, wenn WebSockets nicht verfügbar sind. Andere injixo-Features bieten keinen Fallback-Mechanismus.

## Anforderungen an die Netzwerk-Bandbreite

injixo ist für hohe Leistung bei geringem Ressourcenverbrauch konzipiert und optimiert. Beim ersten Zugriff werden Grafiken heruntergeladen und lokal in temporären Dateien gespeichert. Danach werden nur grundlegende Informationen sicher auf den Desktop übertragen.

Ein Contact Center mit 200&nbsp;Arbeitsplätzen kann mit einem stündlichen Datentransfer von etwa 25-50&nbsp;MB rechnen, wenn alle Benutzer angemeldet sind.

## Integrationsanforderungen

Richte {% link_new Integrationen | features/acd-integration/cloud/how-integrations-work.md %} ein, damit injixo Kontakt- und Agentenstatus-Daten von externen Systemen importieren und verarbeiten kann, z.&nbsp;B. von einer Automatic Call Distribution (ACD) oder einem Customer Relationship Management-System (CRM).
injixo unterstützt eine Vielzahl von Cloud- und On-premise-Integrationen.

Installiere {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}, um regelmäßig Daten von On-premise- und CSV-Integrationen zu importieren.

Datenanfragen beeinträchtigen die Kernfunktionen der Kommunikationssoftware, wie Telefon- oder E-Mail-Plattformen nicht.

Anfragen nach (Echtzeit-)Agentenstatus-Daten (RTA) können einen direkten Socket-Feed verwenden. Diese Feeds übermitteln nur Aktivitätsänderungen von Agenten (einschließlich eines Zeitstempels, einer Agenten-ID und eines Statuscodes) und sind jeweils etwa 1&nbsp;kB groß.

## Rechenzentrum und Sicherheitsvorkehrungen

injixo verwendet Rechenzentren in der Amazon EC2-Infrastruktur. Daher gelten die [Sicherheitsrichtlinien von Amazon](https://aws.amazon.com/de/security/) für injixo, z. B. SOC 1 Typ 2, ISO 27001 und PCI DSS Level 1.

Alle Daten werden innerhalb der EU (europäische Kunden) und in den USA (Kunden mit Sitz in den USA) gespeichert. injixo erfüllt alle relevanten Datenschutzbestimmungen, einschließlich der DSGVO in Europa. Erfahre mehr über [das Cloud-Sicherheits- und Compliance-Konzept von injixo](https://www.injixo.com/de/security/).
