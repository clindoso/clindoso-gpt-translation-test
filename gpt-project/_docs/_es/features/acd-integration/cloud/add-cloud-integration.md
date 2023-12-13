---
title: Añadir una integración cloud
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: false
description: Conecta tu ACD en la nube a injixo para importar datos
---

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Qué son las integraciones cloud

Las integraciones cloud extraen datos directamente de un sistema en la nube. injixo soporta múltiples integraciones cloud.

## Añadir una integración cloud

1. Ve a *Account > Integraciones*{:.breadcrumbs}. La página muestra todas las integraciones disponibles.
2. Haz clic en _Añadir integración_{:.doc-button} e introduce la información necesaria. En este ejemplo, vamos a configurar la integración Five9, pero el proceso para configurar cualquier otra integración cloud es muy similar.
3. Escoge un nombre inequívoco para tu integración. El nombre debería reflejar el origen de los datos.
4. Introduce el nombre de usuario y contraseña de una persona con rol de administrador en tu cuenta de Five9.
5. Configura el resto de los detalles específicos de la integración (p.&nbsp;ej., la región de tu cuenta de Five9 y cómo quieres agrupar las colas).
6. Haz clic en _Guardar integración_{:.doc-button} para crear la integración con la información introducida.

{{ 1 | image: 'Integración con Five9', '80%' }}

 La importación inicial de datos puede tardar hasta 15 minutos. Todas las colas del sistema conectado aparecen automáticamente como disponibles para ser asignadas en la {% link_new página de configuración de cargas de trabajo | features/forecast/injixo-forecast/manage-workloads.md | #crear-cargas-de-trabajo %} en injixo Forecast.

Si tu integración soporta la importación de datos de los estados de los agentes, primero tienes que {% link_new asignar los identificadores de usuarios externos y las actividades externas | features/acd-integration/cloud/import-agent-status-data.md %} para poder importar datos de los estados de los agentes.
