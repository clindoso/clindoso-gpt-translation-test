---
title: Probleme beim Öffnen des Schicht Centers
product_label:
  - classic
  - on-premise
---

In diesen Artikel zeigen wir häufig gemeldete Probleme beim Öffnen des Schicht Centers und mögliche Lösungen.

<!-- ## Internet Explorer reagiert nicht mehr

Wenn das _Schicht Center_{:.menu-item} nicht reagiert bzw. sich nicht öffnet, kann das mit der Einstellung _48669_{:.id-label} _Anzeige speichern_ zusammenhängen. Setze den Wert für die Einstellung für den betroffenen oder alle User einmalig von 1 auf 0 zurück. Dann sollte sich das _Schicht Center_{:.menu-item} wieder öffnen. Danach kannst Du das Speichern der Anzeige wieder aktivieren, indem Du wieder den Wert 1 einträgst und speicherst. -->

## Anzeige eines X anstelle des gewünschten Moduls

In einem ActiveX Element, z.B. dem _Schicht Center_{:.menu-item}, erscheint ein X anstatt der Benutzeroberfläche. Das ActiveX-Element in Deinem Browser kann aufgrund von Sicherheitseinstellungen nicht geladen werden. Setze im Tab **Sicherheit** in den Einstellungen des Internet Explorers die Sicherheitsstufe für die Zone Vertrauenswürdige Seiten auf niedrig.

Prüfe die folgenden ActiveX-Einstellungen über den Button _Stufe anpassen_{:.doc-button}. Weitere Informationen findest Du im {% link_new Artikel zur Browser/Client Konfiguration | getting-started/browser-setup.md %} und in diesem Microsoft-Artikel zum Thema [Verwenden von ActiveX-Steuerelementen für Internet Explorer 11](https://support.microsoft.com/de-de/help/17469).

## Der Enterprise Server konnte nicht gefunden werden

Im _Schicht Center_{:.menu-item} erscheint die Meldung: _Der Enterprise Server konnte nicht gefunden werden_. Auf ActiveX basierende Module wie das Schicht Center benötigen eine direkte TCP-Verbindung. injixo Classic verwendet den Port 45054 (Port 80 für injixo Tenants von vor 2019) vom Client zu Deinem injixo-Host. Möglicherweise ist die direkte Verbindung ins Internet in der Firewall geblockt. Stelle sicher, dass Deine Firewall zumindest für die IP-Adressen der Planer-Clients aus- und eingehende TCP/IP-Verbindungen über den Port 45054 bzw. Port 80 zulässt.

## Das Schicht Center friert beim Öffnen ein

Wenn das Laden von Daten zu lange dauert, erscheint, wenn Du auf das _Schicht Center_{:.menu-item} klickst, nur ein weißes Fenster und möglicherweise der Hinweis _injixo.com reagiert nicht. Webseite wiederherstellen_. Beim Klick auf _Webseite wiederherstellen_{:.doc-button} wirst Du aus injixo ausgeloggt.

{{ 1 | image: 'Hinweisfenster injixo.com reagiert nicht'}}

Dieser Dialog kommt vom Internet Explorer und ist keine injixo Funktion. Warte, bis der Inhalt nach einigen Augenblicken geladen wird. Die Ladezeit hängt davon ab, wie schnell Deine Internet-Verbindung ist und wie viele Mitarbeiter im System vorhanden sind. Das Laden der Daten klappt besser, wenn Du den benötigten Anzeigezeitraum in den Einstellungen des Schicht Centers verkleinerst.
