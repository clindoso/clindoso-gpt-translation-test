---
title: Añadir una integración de Freshdesk Contact Center
description: Conecta tu CRM de Freshdesk Contact Center a injixo y utiliza los datos importados en injixo Forecast.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-five9-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

La integración de Freshdesk Contact Center importa historiales de llamadas y datos de adherencia en tiempo teal.

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Añadir una integración de Freshdesk Contact Center

Para añadir una integración de Freshdesk Contact Center en injixo, necesitas una cuenta de Freshdesk Contact Center Pro o Enterprise. Sigue el proceso descrito en {% link_new Añadir una integración cloud | features/acd-integration/cloud/add-cloud-integration.md %}: 

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Freshworks**, haz clic en _Selecciona el modelo_{:.doc-button}.
4. En la sección **Freshdesk Contact Center**, haz clic en _Añadir integración_{:.doc-button}.

## Configurar tu integración de Freshdesk Contact Center

1. Introduce un nombre inequívoco para la integración que identifique el origen de los datos.
2. En la sección **Credenciales**, introduce el nombre completo de tu dominio de Freshdesk Contact Center, incluido el subdominio, p.&nbsp;ej., ejemplo.freshcaller.com.
3. Inicia sesión en Freshdesk Contact Center y copia una clave de API válida.
4. Vuelve a injixo y copia la clave de la API en el campo **Clave de la API**.
5. Selecciona un [método de agrupación para las colas importadas](#nombres-de-las-colas-según-el-método-de-agrupamiento).
6. Haz clic en _Guardar integración_{:.doc-button}. 

Cuando hayas guardado tu configuración, podrás acceder a la sección **Instalar la aplicación injixo**.

## Instalar la aplicación injixo

1. En la sección **Instalar la aplicación injixo**, genera y copia la **clave de la API de injixo**.
2. Configura la aplicación injixo en tu cuenta de Freshdesk en [Freshworks Marketplace](https://www.freshworks.com/apps/freshcaller/injixo_1/).
3. En la página de instalación de la aplicación injixo, pega la clave de la API que habías copiado antes.
4. Para importar datos en tiempo real, marca la casilla **Export real-time agent status data** en la página de instalación de la aplicación injixo en Freshworks Marketplace.

### Nombres de las colas según el método de agrupamiento

Cuando se importan los datos, el método de agrupamiento determina el nombre de las colas que se crean en injixo.

| Método de agrupamiento   | Nombre de la cola                               | Ejemplo           |
| ------------------- | ---------------------------------------- | ----------------- |
| Número de teléfono        | Número de teléfono                             | +49123456789      |
| Enrutamiento(equipo/agente) | Nombre del equipo                                | Equipo de asistencia técnico |
| Enrutamiento(equipo/agente) | Nombre del agente (si no hay ningún nombre de equipo asignado) | Agente 1           |

Si las llamadas no pertenecen a ningún grupo en Freshdesk Contact Center, el nombre de la cola será Undefined_Queue.
