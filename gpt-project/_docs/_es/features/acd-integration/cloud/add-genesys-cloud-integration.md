---
title: Añadir una integración de Genesys Cloud
description: Aprende cómo conectar tu sistema de Genesys Cloud a injixo para importar datos.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Una integración de Genesys Cloud es una integración cloud que importa historiales de llamadas, correos electrónicos y chats, así como estados de los agentes y datos de adherencia en tiempo real.

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Añadir una integración de Genesys Cloud

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Genesys**, haz clic en _Seleccionar modelo_{:.doc-button}.
4. En la sección **Genesys Cloud**, haz clic en _Añadir integración_{:.doc-button}.

## Configura tu integración de Genesys Cloud

1. Introduce un nombre inequívoco para la integración que identifique el origen de los datos.
2. En la sección de **Credenciales de API**, copia y pega tu clave de API y secreto de API de Genesys Cloud.
3. En la sección **Configuración**, selecciona tu región de acceso.
4. (Opcional) Marca la casilla **Importar estados detallados de agentes on-queue**.<br>El estado del agente «on-queue» en Genesys incluye varios estados, como «communication», «interacting», «idle» o «not responding». Cuando importes estados de los agentes, injixo diferenciará entre los distintos estados agrupados bajo «on-queue».
5. Haz clic en _Guardar integración_{:.doc-button}.

## Preguntas frecuentes

| Pregunta                            | Respuesta                                                                                                                                           |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------- |
| La integración importa datos de llamadas abandonadas, velocidad media de respuesta, y llamadas atendidas dentro del nivel de servicio. ¿Por qué no puedo mostrar estos datos en Dashboards? | Puedes mostrar estos datos en Dashboards si añades exclusivamente colas provenientes de tu integración de Genesys Cloud cuando configuras una carga de trabajo en Forecast. No puedes mostrar estos datos si incluyes colas provenientes de otras integraciones.
