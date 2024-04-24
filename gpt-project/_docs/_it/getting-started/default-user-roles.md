---
title: I ruoli utente prestabiliti
description: Scopri i diritti di accesso dei ruoli utente prestabiliti in injixo.
toc: true
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from:
  - /it/user-roles-in-detail/
redirect_reason: Updated filename on 05 December 2022
---

## I ruoli utente prestabiliti

Ogni categoria di ruoli in injixo include un ruolo utente prestabilito con diritti di accesso predefiniti. In injixo Advanced ed Enterprise WFM, puoi personalizzare i ruoli utente di default e/o {% link_new aggiungere nuovi ruoli utente | getting-started/configure-user-roles.md %}. Nota: la categoria di ruoli Altro non prevede un ruolo utente prestabilito.

| **Categoria di ruoli**     | **Diritti di accesso predefiniti**                                                                                                                                                                    |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Agente                 | Accesso a injixo Me: visualizzazione dei turni, richiesta di permessi, offerta turni, scambio turni.                                                                                                        |
| Pianificatore               | Accesso completo a tutte le funzioni relative al processo di previsione, alla pianificazione, alla gestione intraday e ai dati di configurazione.                                                                         |
| Supervisore (base)    | Accesso di sola lettura al livello Piano in {% link_new Schedules                                                                                                                              | features/scheduling/schedules/schedules-overview.md %} e nel {% link_new Centro dei turni | features/scheduling/shiftcenter/shift-center-overview.md %}. Accesso alla {% link_new panoramica degli scambi | features/scheduling/view-approve-shift-swap-requests.md %} e a {% link_new Ferie/Assenze | features/scheduling/time-off/vacation-absences-management.md %} per gestire gli scambi di turni e le richieste di permesso. Nessun tipo di accesso ai dati di configurazione. |
| Supervisore (avanzato) | Tutte le funzionalità del ruolo Supervisore (base), accesso completo al Centro dei turni e a Schedules, modifica delle pianificazioni nella gestione intraday e accesso completo a dati di configurazione specifici. |
| Finanza               | Accesso alle informazioni sugli utenti e sulla fatturazione e alle fatture per i servizi injixo.                                                                                                             |
| Formatore | Nessun diritto di accesso prestabilito. |

Per assegnare a un utente l’accesso come amministratore, {% link_new modifica l’utente | getting-started/manage-user-accounts.md %} e spunta la casella **Concedi l’accesso come amministratore**. Questa azione sovrascriverà tutti gli altri ruoli, e permetterà un accesso completo.

Nota: la tabella in questo articolo elenca i componenti e le funzionalità per i relativi ruoli utenti prestabiliti. L’icona con la spunta verde <i class="fa fa-check" style="color:#1cb396"></i> segnala l’accesso completo (lettura e scrittura). I diritti di accesso dipendono dal tuo piano WFM: per questo motivo, potresti non avere accesso a tutte le voci incluse nella tabella.

## Accesso ai componenti e alle funzionalità

Puoi accedere ai moduli della navigazione principale e ai componenti con relative funzionalità sotto ogni elemento, indicati in grassetto nella tabella qui sotto.

Attenzione: in injixo Classic tutti i componenti relativi alla pianificazione si trovano in _Scheduling > SchedulePro_{:.breadcrumbs}. Fai riferimento alla sezione [Accesso ai componenti del modulo WFM](#accesso-alle-funzionalità-in-wfm) per altri componenti di injixo Classic.

<div class="table__wrapper table__with-subsections" markdown="1">

|                                         |          Amministratore          |         Pianificatore         |  Supervisore (avanzato)  |   Supervisore (base)    |
| --------------------------------------- | :---------------------: | :---------------------: | :---------------------: | :---------------------: |
| **Forecast**                            |                         |                         |                         |                         |
| **Forecast**                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |        Solo lettura        |
| ------------------------------------    | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Intraday**                            |                         |                         |                         |                         |
| **Aderenza in Tempo Reale**                 | <i class="fa fa-check"> |        Solo lettura        |        Solo lettura        |        Solo lettura        |
| **Aderenza Intraday**                  | <i class="fa fa-check"> |        Solo lettura        |        Solo lettura        |        Solo lettura        |
| ------------------------------------    | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Plan**                                |                         |                         |                         |                         |
| **Schedules**                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |
| **Centro dei turni**                        | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |
| **Periodi di pianificazione**                  | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |                         |
| Genera turni                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Avvia la lotteria dei turni                     | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Assegna turni                           | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Regola la generazione dei turni                 | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| **Azioni di pianificazione**                  | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Inserire le rotazioni                  | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Crea una pianificazione ottimizzata               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Ottimizzazione delle mansioni                        | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Ottimizzare le pause                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Pianificare le attività extra               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Sostituisci le attività                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Svuotare i livelli                            | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Copiare il contenuto del livello                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Approvare scambi turno                     | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |        Solo lettura        |
| **Meetings**                            | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| **Ferie/Assenze**                            | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |
| Periodi di permesso                        | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |                         |
| Edita ferie spettanti <!--edit UI-->                        | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |                         |
| **Configurazione**                       |                         |                         |                         |                         |
| Qualifiche                                  | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |                         |
| --------------------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Analyze**                             |                         |                         |                         |                         |
| **Dashboards**                          | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |

</div>

## Accesso alle informazioni relative agli account, agli utenti e alle integrazioni

Clicca su _Account_{:.menu-item} nella navigazione principale per accedere ai componenti elencati di seguito.

<div class="table__wrapper table__with-subsections" markdown="1">

|                    |          Amministratore          |         Pianificatore         |         Finanza         |
| ------------------ | :---------------------: | :---------------------: | :---------------------: |
| **Account**        |                         |                         |                         |
| **Utenti**           | <i class="fa fa-check"> |                         |                         |
| **Ruoli utente**     | <i class="fa fa-check"> |                         |                         |
| **Fatturazione**        |                         |                         |                         |
| Abbonamento       | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Fatture           | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Contatti           | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| Dettagli            | <i class="fa fa-check"> |                         | <i class="fa fa-check"> |
| **Amministrazione** |                         |                         |                         |
| Dettagli azienda    | <i class="fa fa-check"> |                         |                         |
| **Integrazioni**   | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| **Sicurezza**       | <i class="fa fa-check"> |                         |                         |

</div>

## Accesso alle funzionalità in WFM

Clicca su _WFM_{:.menu-item} nella navigazione principale per accedere alle funzionalità elencate di seguito.

Nota: in injixo Advanced ed Enterprise WFM, sono disponibili **Monitoring** e **Administration**. Tutte le altre funzionalità relative alla pianificazione che prima si trovavano in _Scheduling > SchedulePro_{:.breadcrumbs} sono state spostate in _Plan > Schedules_{:.breadcrumbs} e in _Plan > Ferie/Assenze_{:.breadcrumbs}. Scopri di più sull’[accesso ai componenti e alle funzionalità](#accesso-ai-componenti-e-alle-funzionalità).

<div class="table__wrapper table__with-subsections" markdown="1">

|                                      |          Amministratore          |         Pianificatore         |  Supervisore (avanzato)  |   Supervisore (base)    |
| ------------------------------------ | :---------------------: | :---------------------: | :---------------------: | :---------------------: |
| **Scheduling**                       |                         |                         |                         |                         |
| **SchedulePro**                      |                         |                         |                         |                         |
| Centro dei turni                         | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |
| Ottimizzazione                         | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Periodi di pianificazione                     | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |                         |
| Pianificazione di meeting                      | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Inserire le rotazioni               | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Fabbisogno dei turni <!--edit UI-->                    | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Panoramica scambi <!--check UI-->                    | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |        Solo lettura        |
| **TimeManager**                        |                         |                         |                         |                         |
| Conti delle ore dovute                 | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Ferie spettanti                 | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |
| ------------------------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Monitoring**                       |                         |                         |                         |                         |
| Report                              | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |
| ------------------------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| **Administration**                   |                         |                         |                         |                         |
| **Scheduling**                       |                         |                         |                         |                         |
| Qualifiche                               | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |                         |
| Attività                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Modelli di orario                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Modelli settimanali                   | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |                         |
| Modelli di pianificazione             | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |                         |
| Rotazioni                      | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Tipi di giorno                            | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Unità di pianificazione                       | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Calendari pianificativi                    | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Gruppi di selezione                           | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |
| Contratti                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |                         |
| Dipendenti                            | <i class="fa fa-check"> | <i class="fa fa-check"> |        Solo lettura        |                         |
| **Forecasting**                      |                         |                         |                         |                         |
| Tipi di evento                          | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |                         |
| Code                               | <i class="fa fa-check"> |        Solo lettura        |                         |                         |
| **Sistema**                           |                         |                         |                         |                         |
| Regole di pianificazione                     | <i class="fa fa-check"> |        Solo lettura        |                         |                         |
| Impostazioni                             | <i class="fa fa-check"> |                         |                         |                         |
| Sistemi esterni                     | <i class="fa fa-check"> |                         |                         |                         |
| Diritti per ruoli di utenti                   | <i class="fa fa-check"> |                         |                         |                         |
| Diritti utenti                   | <i class="fa fa-check"> |                         |                         |                         |
| JobProcessor                         | <i class="fa fa-check"> | <i class="fa fa-check"> | <i class="fa fa-check"> |                         |

</div>

## Accesso a injixo Me

Gli utenti con il ruolo Agente possono cliccare su _Me_{:.menu-item} nella barra di navigazione principale per vedere la loro agenda, richiedere permessi e scambiare turni. Soltanto l’**Agenda personale** è accessibile per impostazione predefinita.

Gli utenti con accesso amministratore possono cliccare su _Me_{:.menu-item} e {% link_new configurare injixo Me| features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} per permettere agli utenti con ruolo Agente di avere accesso ad altri componenti.
