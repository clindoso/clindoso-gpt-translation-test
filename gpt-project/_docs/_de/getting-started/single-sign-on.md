---
title: Single Sign-On (SSO)
product_label:
  - advanced
  - enterprise
description: Erfahre, wie du Single Sign-On (SSO) in injixo einrichtest und verwendest.
---

Single Sign-on (SSO) ist ein Authentifizierungsmechanismus, mit dem sich ein Benutzer mit denselben Zugangsdaten bei mehreren Webseiten und Anwendungen anmelden kann. Dafür wird eine Vertrauensbeziehung zwischen einem zentralen Identitätsmanagementdienst (Identity Provider/IdP) und einer Anwendung (Service Provider/SP) eingerichtet, in diesem Fall injixo.

Der IdP ist ein Drittanbieter wie OneLogin, Microsoft Azure AD, Okta oder Google. Wenn dein Unternehmen SSO verwendet, profitiert es von einheitlichen Sicherheitsrichtlinien, wie Zwei-Faktor-Authentifizierung und Passwortrotation, die in Übereinstimmung miteinander konsistent eingesetzt werden. Benutzer authentifizieren sich gegen den IdP, der wieder zu injixo weiterleitet.

Die IdP-Konfiguration wurde mit den zuvor genannten IdP getestet. Wenn du deinen spezifischen IdP nicht integrieren kannst, wende dich an uns.

## Voraussetzungen

Die folgenden Voraussetzungen müssen für eine erfolgreiche Integration von injixo in den jeweiligen IdP erfüllt sein:

- SAML 2.0 Protokollunterstützung
- Zugriff auf die Föderationsmetadaten-URL über das Internet
- Die bei injixo und dem IdP registrierten E-Mail-Adressen müssen mit einem Postfach verbunden sein

> Um die Sicherheit zu erhöhen, aktiviere verschlüsselte Assertions/Tokenverschlüsselung (dringend empfohlen).

## SSO für dein Konto aktivieren

Nur Benutzer mit Admin-Zugriff können SSO aktivieren.

1. Registriere injixo als neue SAML-/SSO-Anwendung bei deinem IdP.  
   Du kannst [dieses injixo-Logo](/assets/img/common/injixo-logo.png) herunterladen, um es auf der Webseite der Anwendung zu verwenden.

2. Gehe in injixo zu _Account > Sicherheit_{:.breadcrumbs} und konfiguriere SSO unter **Single Sign-On**.

3. Im Abschnitt **injixo SAML Metadaten** stehen dir zwei Optionen zur Verfügung, je nachdem, ob dein IdP Dateiuploads unterstützt:

   - Dateiuploads unterstützt: Klicke auf _{% icon download | icon-only %}Herunterladen_{:.doc-button} und schließe die IdP-Konfiguration mit der heruntergeladenen XML-Datei ab.
   - Dateiuploads nicht unterstützt: Klicke auf **Service Provider Details** und füge die angezeigte URL deiner IdP-Konfiguration hinzu.

4. (Optional) Wenn du verschlüsselte SAML-Assertions verwendest, klicke im Abschnitt **Tokenverschlüsselung** auf _{% icon download | icon-only %}Herunterladen_{:.doc-button}. Füge die heruntergeladenen Zertifikate deiner IdP-Konfiguration hinzu.
5. Je nachdem, ob dein IdP eine Föderationsmetadaten-URL bereitstellt, schließe die Konfiguration wie folgt ab:

   - IdP stellt Föderationsmetadaten-URL bereit: Kopiere deine Föderationsmetadaten-URL für die registrierte Anwendung von deinem IdP. Füge die URL im Abschnitt **Identity Provider** in das Feld **Föderationsmetadaten-URL** ein.
   - IdP stellt keine Föderationsmetadaten-URL bereit: Lade die XML-Datei für die Föderationsmetadaten herunter und hoste sie selbst. Erfahre zum Beispiel, wie du deine eigene benutzerdefinierte [SAML-Applikation mit Google](https://support.google.com/a/answer/6087519?hl=en) einrichten kannst.

6. Klicke auf _Konfiguration speichern_{:.doc-button}.  
   > SSO ist nun aktiv
   >
   > Alle Benutzer können sich weiterhin mit ihrem Benutzernamen und ihrem Passwort anmelden. Um SSO erneut zu deaktivieren, klicke auf _Deaktivieren_{:.doc-button}.  
   > Um die Sicherheit noch weiter zu erhöhen, kannst du [SSO für alle Benutzer erzwingen](#sso-für-alle-benutzer-erzwingen).

## SSO-Konfiguration testen

Klicke auf _Konfiguration testen_{:.doc-button}, um die Anmeldung über den IdP zu testen. Der IdP erzeugt eine SAML-Antwort, die an injixo gesendet wird. Du wirst zur Anmeldeseite des IdP weitergeleitet. Dort gibst du die IdP-Anmeldedaten ein. Wenn die IdP-Konfiguration korrekt ist und die Authentifizierung erfolgreich, wirst du bei injixo angemeldet.

{{ 4 | image: 'Testen der SSO-Konfiguration mit dem aktuellen Benutzer', '80%' }}

### Test fehlgeschlagen? Konfiguriere die SAML-Antwort
<!-- A valid SubjectConfirmation was not found on this Response in our internal server logs -->

Die SAML-Antwort des IdP enthält die Assertion des authentifizierten Benutzers mit Attributen und Profilinformationen. Wenn der Vorgang nicht erfolgreich war und du eine Fehlermeldung siehst, überprüfe die Anwendungs- und Benutzerkonfiguration sowie die beim IdP festgelegten Attribute Recipient, InResponseTo, NotBefore und NotOnOrAfter. 

Du kannst das SubjectConfirmation XML-Element in der SAML-Antwort in den Entwicklertools deines Browsers oder in externen SAML-Tools debuggen. Um die unverschlüsselte Antwort im Klartext zu sehen, deaktiviere verschlüsselte Assertions.

Beispiel für das SubjectConfirmation XML-Element in einer SAML-Antwort:

```
<saml:Subject>
    <saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">email@company.org</saml:NameID>
    <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
        <saml:SubjectConfirmationData NotOnOrAfter="2022-08-11T08:25:25Z"
            Recipient="https://www.injixo.com/sso/saml/acs"
            InResponseTo="_abcdefgh-0444-4567-abcd-abcdabcdabcd"
    />
    </saml:SubjectConfirmation>
</saml:Subject>
```

## SSO für alle Benutzer erzwingen

Wenn du testen möchtest, ob die Konfiguration erfolgreich war, kannst du alle Anmeldungen mit Benutzername und Passwort deaktivieren, indem du SSO für alle Benutzer erzwingst. Dafür musst du folgendes sicherstellen:

- Alle injixo-Benutzer sind in injixo und beim IdP angelegt.
- Die injixo-E-Mail-Adresse entspricht der zugehörigen IdP-Kennung.
- Alle injixo-Benutzer wurden der Applikation beim IdP zugeordnet.

Sobald du SSO erzwungen hast, ist folgendes nicht mehr möglich:

- Anmeldung über Benutzername und Passwort (alle existierenden Passwörter werden ungültig)
- Passwort zurücksetzen in injixo (weder durch Benutzer noch durch Administratoren)
- Zugangsverwaltung zu injixo außerhalb des IdP

Erzwinge SSO im Abschnitt **3\. Anmeldung ausschließlich via SSO**. Der Button _Erzwingen_{:.doc-button} wird auswählbar, wenn du die SSO-Konfiguration erfolgreich getestet hast.

{{ 5 | image: 'Button zum Erzwingen von SSO für alle Benutzer', '80%' }}

## E-Mail-Adressen ändern, wenn SSO erzwungen wird

Erzwingst du SSO, können Benutzer ihre E-Mail-Adressen nicht mehr selbst ändern, da die injixo E-Mail-Adresse mit der entsprechenden IdP-Kennung übereinstimmen muss.

Nur Benutzer mit Admin-Zugriff können E-Mail-Adressen in injixo ändern.

## Über SSO anmelden

Wenn SSO erfolgreich eingerichtet wurde, können sich Benutzer über [https://www.injixo.com/login/sso](https://www.injixo.com/login/sso) bei injixo anmelden. Sie müssen ihre E-Mail-Adresse eingeben und werden zum Anmeldebildschirm des IdP weitergeleitet. Wenn die Benutzer bereits angemeldet sind, werden sie automatisch wieder zu injixo weitergeleitet. Andernfalls müssen sie das IdP-Passwort eingeben.

## Zugriff auf injixo entziehen

Um einem Benutzer den Zugang zu injixo über SSO zu entziehen, musst du die Benutzerzuordnung zu injixo im IdP löschen. Hinweis: Wenn der Benutzer noch in injixo angelegt ist, wird er weiterhin abgerechnet. Um Kosten zu vermeiden, musst du den Benutzer {% link_new deaktivieren bzw. löschen | features/administration/deactivate-employees.md %}.

## SSO deaktivieren

Um Anmeldungen mit Benutzernamen und Passwort wieder zuzulassen, können Benutzer mit Admin-Zugriff SSO deaktivieren. Dadurch werden die IdP-Verbindung und alle eingegebenen Konfigurationsdetails gelöscht. Nach der Deaktivierung erhalten alle aktiven Benutzer eine E-Mail, um ein neues injixo-Passwort zu setzen. Danach ist die Anmeldung mit Benutzernamen und Passwort über [https://www.injixo.com/login](https://www.injixo.com/login) wieder möglich.

## SSO für mehrere Tenants verwenden

Wenn dein Unternehmen mit mehreren injixo-Tenants arbeitet und du einigen oder allen Benutzern Zugriff auf mehr als einen Tenant gewähren möchtest, funktioniert die Standardkonfiguration für SSO nicht. Wende dich an deinen Consultant, um eine Konfiguration für diesen speziellen Anwendungsfall aufzusetzen.

<!-- SSO for multiple tenants can be activated by the feature flag multi_tenant_sso, see also https://github.com/ivx/internal-support-documentation/tree/main/Cortex-->
