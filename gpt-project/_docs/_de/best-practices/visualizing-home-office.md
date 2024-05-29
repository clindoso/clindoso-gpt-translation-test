---
title: Umgang mit Homeoffice
redirect_from:
  - /de/options-for-home-office/
---

injixo bietet Dir eine Reihe von Möglichkeiten, mit denen Du Homeoffice-Tage im _Schicht Center_{:.menu-item} sichtbar machen kannst, ohne die eigentliche Planung zu beeinflussen.

## Homeoffice als Tagesstatus

Lege unter _WFM > Administration > Scheduling > Aktivitäten_{:.breadcrumbs} eine neue Aktivität vom Typ _Abwesenheit_ mit folgenden Parametern an:

{{ 1 | image: 'Parameter für die Aktivität Homeoffice', '60%' }}

Da die Aktivität nicht automatisch geplant werden soll, darf die Option _Planbar_ nicht aktiviert sein. Wenn sich Deine Agenten ihre Homeoffice-Tage selbst wünschen sollen, muss die Option **Wünschbar in Me** gesetzt sein.

Soll die Homeoffice-Aktivität auch zwischen den Mitarbeitern tauschbar sein, setze zusätzlich das Häkchen bei **Tauschbar beim Schichttausch**. Wenn Du Dich dafür entscheidest die Homeoffice-Aktivität nicht tauschbar zu machen, können Mitarbeiter trotzdem weiterhin ihre Schichten tauschen. Die Homeoffice-Aktivität wird dann nicht mitgetauscht.

Da Aktivitäten mit dem _Tagesstatus_ immer _Ganztägig erlauben_ erfordern, müssen beide Optionen ausgewählt sein.

Zur einfacheren Planung im _Schicht Center_{:.menu-item} solltest Du, wie in diesem Beispiel, einen Shortcut zuweisen.

Den Tagesstatus fügst Du durch {% link_new Zuordnung per Shortcut | best-practices/tips-on-shift-center-usage.md | #tipp-2-shortcuts-für-die-schnelle-zuweisung-von-aktivitäten %} direkt im _Schicht Center_{:.menu-item} ein. Die eigentlichen Aktivitäten Deiner Agenten bleiben erhalten und die Homeoffice-Aktivität wird im Hintergrund eingefügt:

{{ 2 | image: "Homeoffice im Schicht Center", "75%" }}

> Hinweis
>
> Durch den Tagesstatus ist keine Sortierung nach der Startzeit der Agenten möglich. Wenn die Sortierung für Dich wichtig ist, solltest Du eine der anderen beiden Lösungen nutzen.

## Homeoffice über eine zweite Schicht Center Ebene

Diese Variante erfordert keine Aktivität mit der Option _Tagesstatus_. Lege einfach eine unbezahlte _Abwesenheit_ mit der Option _Ganztägig erlauben_ an. Im _Schicht Center_{:.menu-item} blendest Du Dir eine ungenutzte Ebene ein (z.B. Ebene _Version 1_). Wir empfehlen, dass Du diese Ebene der Übersicht halber über Deine eigentliche Planebene einblendest. Hier kannst Du die Aktivität {% link_new mittels Shortcut | best-practices/tips-on-shift-center-usage.md | #tipp-2-shortcuts-für-die-schnelle-zuweisung-von-aktivitäten %} einfügen. Die Homeoffice-Aktivität ist damit immer sichtbar:

{{ 3 | image: 'Homeoffice in eigener Schicht Center Ebene', '75%' }}

## Homeoffice als Kommentar im Schicht Center

In dieser Variante trägst Du Homeoffice einfach als Kommentar ins _Schicht Center_{:.menu-item} ein. Der Kommentar-Indikator hilft Dir dabei zu erkennen, dass dort ein Eintrag vorhanden ist. Dieses Vorgehen ist nur empfehlenswert, wenn Du die Kommentare nicht noch für etwas anderes verwendest. Wenn Du mit der Maus über den Tag gehst, wird Dir die Homeoffice-Information angezeigt:

{{ 4 | image: 'Homeoffice als Kommentar im Schicht Center', '75%' }}
