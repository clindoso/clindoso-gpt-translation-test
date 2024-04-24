---
title: Valore d’importanza delle attività
product_label:
  - advanced
  - enterprise
  - classic
description: Utilizza il valore d’importanza per stabilire la rilevanza delle attività nella pianificazione ottimizzata.
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
---

Puoi stabilire un valore d’importanza per ogni attività in _Plan > Configurazione > Attività_{:.breadcrumbs}.

## Perché è necessario stabilire il valore d’importanza delle attività?

Per impostazione predefinita, l’ottimizzazione delle mansioni comincerà a pianificare dipendenti partendo dalle attività con un basso fabbisogno di personale. Pianificare personale in eccedenza per le attività con fabbisogno di personale più alto ha un impatto negativo minore rispetto alla pianificazione di personale insufficiente per le attività con fabbisogno di personale più basso.

Di conseguenza, se non sono disponibili abbastanza dipendenti, per le attività con fabbisogno di personale più alto potrebbe essere pianificato personale insufficiente. Puoi aggirare questa impostazione e dare precedenza alle attività con un fabbisogno di personale più elevato utilizzando il valore d’importanza (valore predefinito: 100%). Maggiore il valore d’importanza di un'attività, più l'ottimizzazione delle mansioni cercherà di aderire al fabbisogno di personale.
Per esempio, puoi usare questa funzionalità per dare precedenza a un’attività rispetto a un’altra, come nel caso della linea diretta B2B rispetto alla linea diretta B2C.

Se un’attività richiede cinque dipendenti, assegnarle cinque dipendenti risulterà in una copertura ottimale. Per dare precedenza a questa attività, imposta un valore d’importanza alto (100%). L’ottimizzazione delle mansioni cercherà quindi di pianificare i dipendenti in modo da aderire quanto più possibile al fabbisogno di personale. 

Le attività per le quali un’eccedenza di personale è accettabile dovrebbero avere un valore d’importanza più basso. Con un valore d’importanza del 20%, l’ottimizzazione delle mansioni pianificherà il numero esatto di persone necessarie, o ne pianificherà in eccesso, se sono disponibili.

## Prerequisiti

Per dare precedenza alle attività con il valore d’importanza, devono verificarsi le seguenti condizioni:
- Le attività che devono avere la precedenza sono pianificabili e sostituibili.
- Le persone che devono lavorare sulle attività che hanno la precedenza sono pianificate per l’attività Presente (ID 1).

Se i tuoi dipendenti sono pianificati per altre attività, che non sono sostituibili, o se nel modello di orario esiste un blocco di attività già pianificate, il valore d’importanza non ha nessun effetto. L’ottimizzazione delle mansioni quindi non può cambiare l’attività per il giorno o per certi intervalli.
Anche le qualifiche delle persone, o le proprietà dell’attività, come l’opzione Pianificabile, potrebbero impedire all’ottimizzazione delle mansioni di assegnare maggiori risorse all’attività.

## Esempio

- Ci sono due attività: A e B.
- 26 persone sono disponibili e qualificate a lavorare sulle attività A e B.
- Il fabbisogno di personale per ogni attività è di 10 persone.
- L’attività A ha un valore d’importanza del 20% e l’attività B ha un valore d’importanza del 100%.

L’ottimizzazione delle mansioni pianifica 10 dipendenti per ciascuna delle due attività A e B, aderendo perfettamente al fabbisogno di personale. Restano però ancora 6 persone da pianificare.
Il valore d’importanza dell’attività A è cinque volte inferiore rispetto a quello dell’attività B. Per questo motivo, l’ottimizzazione delle mansioni può assegnare all’attività A altre cinque persone prima che questo abbia lo stesso impatto negativo sulla copertura che avrebbe l’assegnazione all’attività B di una persona in più. injixo tende quindi ad assegnare all’attività A personale in eccesso.
