---
title: Impostare un periodo di validità
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Utilizza i periodi di validità per definire i periodi in cui gli elementi della configurazione sono attivi.
redirect_from:
  - /it/valid-from-to-dates/
redirect_reason: Updated filename on 12 October 2023
---

Con i periodi di validità, puoi impostare una configurazione per un periodo di tempo delimitato. Puoi programmare delle modifiche alla configurazione in modo che avvengano automaticamente in futuro senza un ulteriore intervento manuale.

I periodi di validità sono sempre facoltativi. Se non specifichi un periodo di validità, la configurazione sarà effettiva immediatamente, e non cambierà fino a quando non la modificherai manualmente.

I periodi di validità sono disponibili in _WFM > Administration > Scheduling_{:.breadcrumbs}.

## Utilizzare i periodi di validità

Puoi impostare un periodo di validità durante la creazione dei dati di configurazione. 

Esempio: vuoi che una specifica unità di pianificazione si faccia carico temporaneamente dell’attività Chiamate per evitare di sovraccaricare le altre unità di pianificazione. Puoi aggiungere l’attività Chiamate a una seconda unità di pianificazione e definire il periodo di validità per questa configurazione:

1. Seleziona **Unità pianificative**.
2. Seleziona l’unità di pianificazione alla quale vuoi aggiungere l’attività.
3. Vai alla sezione **Attività** a destra.
4. Clicca sull’icona Aggiungi {% icon item-add | icon-only %}.
5. Inserisci delle date nei campi **Validità dal** e **fino al**. Questo è il periodo di validità.
6. Scegli un’attività e imposta le ore nei campi **dalle** e **alle**.
7. Clicca su _OK_{:.doc-button}.

## Modificare un periodo di validità

Puoi modificare il periodo di validità per i dati di configurazione esistenti. 

Esempio: vuoi prorogare il contratto di un dipendente. Puoi modificare il periodo di validità del contratto di questo dipendente.

1. Seleziona **Dipendenti**.
2. Seleziona il dipendente per il quale vuoi prorogare il contratto.
3. Vai alla sezione **Contratti** a destra.
4. Clicca sull’{% icon item-edit %} accanto al contratto che vuoi prorogare.
5. Modifica il campo **fino al**.
6. Clicca su _OK_{:.doc-button}.
