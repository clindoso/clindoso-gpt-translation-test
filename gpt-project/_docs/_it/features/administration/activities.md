---
title: Creare le attività
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
beta-feature: false
description: Crea attività per rappresentare i compiti pianificati e non pianificati nella tua organizzazione.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

Per creare, modificare ed eliminare le attività, vai su _Plan > Configurazione > Attività_{:.breadcrumbs}.

Le attività rappresentano i compiti che sono pianificati e inclusi nei report della tua organizzazione, come telefonate, chat, pause, permessi o riunioni. Puoi creare un numero di attività illimitato. Il numero di attività che creerai dipende dalla quantità di compiti che vuoi differenziare e dal livello di dettaglio desiderato.

Le attività sono una parte essenziale della programmazione e della pianificazione in injixo. Sono collegate ad altri elementi della configurazione come, per esempio, le {% link_new unità di pianificazione | features/administration/create-and-manage-planning-units.md | #aggiungere-le-attività %} e i {% link_new modelli di orario | features/administration/daymodels/daymodel-basics.md %}. Sono anche incluse nelle pianificazioni gestite nel {% link_new Centro dei turni | features/scheduling/shiftcenter/add-and-delete-items.md %} e in {% link_new Schedules | features/scheduling/schedules/schedules-edit.md %}.

injixo include due attività preconfigurate (non eliminabili):

- Presente: questa attività viene utilizzata come attività segnaposto all'interno dei modelli di orario. Durante la pianificazione, injixo sostituisce questa attività con altre attività che sono configurate come pianificabili.
- Ferie: questa attività viene utilizzata per pianificare permessi retribuiti in base ai permessi che spettano al dipendente. Per i permessi non retribuiti è necessario creare un’attività separata.

## Creare un’attività

1. Clicca su _Nuova attività_{:.doc-button}.
2. Inserisci alcune informazioni di base per l’attività:
   - **Nome**: un nome unico che descrive l’attività. L’abbreviazione verrà generata automaticamente.
   - **Tipo**: il tipo di attività determina il modo in cui injixo utilizza le attività nella pianificazione e il modo in cui vengono visualizzate in altri componenti e nei report. Scopri di più sui diversi {% link_new tipi di attività | features/administration/activity-types-and-properties.md | #tipi-di-attività %}.
   - **Colore**: colore che verrà visualizzato nella pianificazione e nelle pagine dei dati di configurazione. Il colore ti permette di identificare facilmente le diverse attività.
   - **Comando di scelta rapida**: scorciatoia facoltativa che ti permette di inserire più velocemente l’attività nel Centro dei turni. Scopri di più sui {% link_new comandi di scelta rapida | best-practices/tips-on-shift-center-usage.md | #tip-2-shortcuts-for-a-quick-assignment-of-activities %}.
   - **Nome ufficiale** e **Abbreviazione ufficiale**: Nome alternativo che può essere utilizzato per i report interni e per le integrazioni. injixo Me mostra sempre il nome che inserisci nel campo **Nome**.
3. Spunta una o più caselle per impostare le varie {% link_new proprietà delle attività | features/administration/activity-types-and-properties.md | #proprietà-delle-attività %}.
   Se selezioni Pianificabile, puoi modificare il {% link_new valore dell’importanza | best-practices/importance-for-activities.md %}.
   Se selezioni Sostituibile, puoi modificare il {% link_new valore della priorità | best-practices/priority-for-activities.md %}.
4. (Facoltativo) {% link_new Aggiungi qualifiche | features/administration/work-with-skills.md | #assegnare-le-qualifiche-alle-attività %} all’attività.
5. Clicca su _Crea attività_{:.doc-button}.

Scopri di più sui {% link_new tipi e le proprietà delle attività | features/administration/activity-types-and-properties.md %}.

### ID dell’attività

Per vedere l'ID di un'attività, puoi:

- Cliccare su un’attività nell’elenco delle **Attività**. L'URL nella barra del browser include l'ID dell'attività selezionata (per esempio: https://www.injixo.com/plan/configuration/activities/1234).
- Utilizzare l’API di injixo. Scopri come [gestire le attività tramite l’API di injixo](https://api.injixo.com/resources/schedules/activities).

## Multiattività e subattività

Le multiattività permettono di pianificare persone che hanno più di una qualifica quando una delle loro qualifiche è richiesta. È possibile trasformare un’attività in una multiattività {% link_new assegnandole altre attività | features/administration/activity-types-and-properties.md | #subattività %}. Le attività assegnate diventano le sue subattività. Nell’elenco delle attività, le multiattività sono contrassegnate da un’icona con la lettera M <em class="multiactivity-icon">.

Se un'attività è una subattività, quando la selezioni vedrai la sezione **Multiattività**, che comprende le multiattività alle quali è assegnata.

Se un’attività non è una subattività, quando la selezioni vedrai la sezione **Subattività**, dove puoi selezionare le attività da aggiungere come subattività all’attività che stai modificando. L'attività che stai modificando diventerà quindi una multiattività.
È possibile assegnare subattività a un’attività soltanto dopo averla creata.

## Sistemi esterni

<!-- will be made obsolete by the new activity mapping page. Will require a separate article -->

Puoi mappare le attività che provengono dai sistemi esterni a un'attività in injixo.

1. Seleziona un'attività dall'elenco, scorri fino alla sezione **Sistemi esterni** e clicca su _Modifica in WFM_{:.doc-button}.
2. Vai alla sezione **Sistemi esterni**.
3. Clicca sull’{% icon item-add %}.
4. Seleziona un **Sistema esterno**, una **Denominazione nel sistema esterno** e una **Classificazione** dai menu a tendina.
5. Clicca su _OK_{:.doc-button}.

> È possibile assegnare l'attività di un sistema esterno solo una volta a una singola attività singola in injixo.

## Duplicare un’attività

Per creare una nuova attività con le stesse proprietà generali di un’attività esistente, segui questi passaggi:

1. Nell’elenco delle **Attività**, seleziona un’attività.
2. Clicca su **Duplica attività** sotto il nome dell'attività.  
   Si aprirà la finestra **Crea nuova attività** con opzioni già selezionate. Le competenze assegnate e le subattività non vengono duplicate.
3. Inserisci un **Nome** per la nuova attività.
4. (Facoltativo) Modifica il colore e le altre proprietà.
5. Clicca su _Crea attività_{:.doc-button}.

## Modificare o eliminare un’attività

1. Nell’elenco delle **Attività**, seleziona un’attività.

- Per modificare l’attività, modifica le informazioni che vuoi e clicca su _Salva modifiche_{:.doc-button}.
- Per eliminare l’attività, clicca su _Elimina attività_{:.doc-button} in basso a destra.

Se l’attività eliminata era stata assegnata ad altri elementi della configurazione, come, per esempio, unità di pianificazione o modelli di orario, il nome dell’attività verrà visualizzato in corsivo in quegli elementi. Dopo l’eliminazione, l’attività non sarà più assegnata ad altri elementi, ma rimarrà visibile nei dati di configurazione. Potrebbe essere necessario creare di nuovo i modelli di orario che utilizzavano l’attività eliminata.

Nel Centro dei turni, le attività eliminate sono {% link_new circondate da bordi tratteggiati | features/scheduling/shiftcenter/shift-center-overview.md | #how-are-items-displayed %}. In Schedules, le attività eliminate sono visualizzate come uno spazio grigio senza il nome. Le informazioni originarie sull’orario restano visibili, tranne che nella visualizzazione giornaliera.
