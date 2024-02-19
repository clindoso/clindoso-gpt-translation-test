---
title: IP-Filterung
product_label:
  - enterprise
  - advanced
description: Erfahre, wie du die IP-Filterung für deinen injixo-Tenant einrichten kannst.
toc: true
---

Das Feature zur IP-Filterung muss separat kostenpflichtig gebucht werden. Es ist nicht automatisch in deinem Enterprise oder Advanced WFM-Plan enthalten.
Falls dein Unternehmen Interesse an diesem Feature hat, kontaktiere deinen Consultant.

Die IP-Filterung sorgt dafür, dass deine Benutzer nur von bestimmten IP-Adressbereichen auf deinen injixo-Tenant zugreifen können. Benutzer mit anderen IP-Adressen haben keinen Zugriff auf injixo. injixo bietet eine [Network Access Control List](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) (NACL). Mit dieser Liste kann gesteuert werden, welche IP-Adressen Zugriff auf injixo haben. Wenn du möchtest, dass nur von bestimmten Netzwerken auf injixo zugegriffen werden kann (z.&nbsp;B. aus deinem Unternehmensnetzwerk), aktiviere die NACL.

## IP-Filterung aktivieren

Nur Benutzer mit Admin-Zugriff können die IP-Filterung aktivieren.

> Hinweis
> 
> Wenn du die IP-Filterung aktivierst, werden alle aktiven Benutzer abgemeldet. Je nachdem, in welchem Produktbereich Benutzer arbeiten, erfolgt die Abmeldung zu unterschiedlichen Zeitpunkten:
> - Sofortige Abmeldung
> - Abmeldung, wenn Daten das nächste Mal geladen oder gespeichert werden
> - Zeitgesteuerte Abmeldung (nur, wenn du über _Plan > Schicht Center_{:.breadcrumbs} auf Schicht Center zugreifst)
> 
> Um weiterhin mit injixo arbeiten zu können, müssen die Benutzer sich erneut anmelden.

1. Gehe zu _Account > Sicherheit_{:.breadcrumbs} und scrolle zum Abschnitt **IP-Filterung**.
2. Gib in den **IP-Adressbereich**-Feldern die IP-Adressbereiche im [CIDR-Format](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#:~:text=CIDR%20notation%20specifies%20an%20IP,bits) ein. Du kannst bis zu drei IP-Adressbereiche hinzufügen.
3. Klicke auf _IP-Filterung aktivieren_{:.doc-button}.

Die IP-Filterung betrifft nur Interaktionen auf der Benutzeroberfläche. Wenn du über eine Direkt-URL auf das optional verfügbare Schicht Center zugreifst, ist die IP-Filterung nicht aktiv.
 
## IP-Adressbereiche bearbeiten

> Hinweis
> 
> Wenn du die IP-Adressbereiche bearbeitest, werden alle Benutzer abgemeldet, wenn sie das nächste Mal injixo nutzen. Um weiterhin mit injixo arbeiten zu können, müssen die Benutzer sich erneut anmelden.

1. Gehe zu _Account > Sicherheit_{:.breadcrumbs} und scrolle zum Abschnitt **IP-Filterung**.
2. Bearbeite die IP-Adressbereiche.
3. Klicke auf _Speichern_{:.doc-button}.

## IP-Filterung deaktivieren

1. Gehe zu _Account > Sicherheit_{:.breadcrumbs} und scrolle zum Abschnitt **IP-Filterung**.
2. Lösche die IP-Adressbereiche.
3. Klicke auf _IP-Filterung deaktivieren_{:.doc-button}.

Nach der Deaktivierung der IP-Filterung können Benutzer wieder von jeder IP-Adresse aus auf injixo zugreifen.

> Hinweis
> 
> Wenn du die IP-Filterung deaktivierst, werden alle Benutzer abgemeldet. Um weiterhin mit injixo arbeiten zu können, müssen die Benutzer sich erneut anmelden.
