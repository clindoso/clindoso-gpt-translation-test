---
title: Añadir una integración de Five9
description: Conecta tu ACD de Five9 a injixo y prepara un informe personalizado para utilizar la agrupación de colas por cualificaciones.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_reason: renamed file in Feb 2021
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
---

Five9 es una solución de software para centros de contacto basada en la nube. Incluye funcionalidades como distribución automática de llamadas, respuesta de voz interactiva y otras herramientas para workforce management. injixo soporta la integración de Five9 para importar historiales de llamadas, estados de los agentes y los datos de la aplicación en tiempo real.

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Prerrequisitos

Si agrupas tus colas por campaña, la integración lee el informe de registro de llamadas estándar de Five9.

Si agrupas tus colas por cualificación, la integración necesita un informe de registro de llamadas personalizado de Five9 que incluya las cualificaciones. Para importar datos de colas agrupadas por cualificación, sigue los pasos a continuación en Five9:

 1. Crea una nueva carpeta de informes compartidos.
 2. Personaliza el informe de registro de llamadas estándar incluyendo la columna "SKILL".
 3. Guarda el informe personalizado como "Call Log with Skills" en la carpeta compartida.

Para obtener información más detallada sobre cómo personalizar informes, consulta el Centro de Ayuda de Five9.

## Añadir una integración de Five9

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Five9**, haz clic en _Añadir integración_{:.doc-button}.
4. Introduce un nombre inequívoco para la nueva integración que identifique el origen de los datos.
5. Introduce el nombre de usuario y la contraseña de una persona con acceso de administrador en tu cuenta de Five9.
6. En la sección **Configuración**, selecciona la región de tu cuenta y el método de agrupamiento de colas.
7. Haz clic en _Guardar integración_{:.doc-button}.

La integración empezará a importar datos a injixo. La importación inicial de datos puede tardar hasta 15 minutos. Todas las colas del sistema conectado aparecen automáticamente como disponibles para ser asignadas en la {% link_new página de configuración de cargas de trabajo | features/forecast/injixo-forecast/manage-workloads.md | #crear-cargas-de-trabajo %} en injixo Forecast.

## ¿Qué sucede si hay estados de agentes paralelos?

En ocasiones, Five9 informa de múltiples estados para un agente al mismo tiempo, por ejemplo:

| Estado | Hora de inicio | Hora de fin |
| ------- | ------------ | -------- |
| Disponible | 13:00:00 | 13:00:05 |
| Entrante | 13:00:00 | 13:03:00 |

Para evitar que un estado sobrescriba el otro, la integración cambia el inicio del estado más largo. El inicio del estado más largo se convierte en el final del más corto:

| Estado | Hora de inicio | Hora de fin |
| ------- | ------------ | -------- |
| Disponible | 13:00:00 | 13:00:05 |
| Entrante | 13:00:05   | 13:03:00 |
