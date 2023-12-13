---
title: Añadir una integración de Cisco ICM
description: Aprende cómo conectar tu Cisco ICM a injixo para importar datos.
product_label:
  - advanced
  - enterprise
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-five9-integration.md
  - overwrite_title: Importar datos sobre los estados de los agentes
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

La integración de Cisco ICM importa datos de adherencia en tiempo real. La integración usa {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Añadir una integración de Cisco ICM

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Cisco ICM**, haz clic en _Añadir integración_{:.doc-button}.

## Configurar tu integración de Cisco ICM

1. Introduce un **nombre de la integración** inequívoco que identifique el origen de los datos.
2. En la sección **injixo Cloud Link**, haz clic en el **enlace de descarga** para tu sistema operativo.<br>
   > Atención
   >
   > Aunque ya hayas descargado Cloud Link para otra integración, también necesitas descargar la versión específica para Cisco en esta página.
3. Instala y conecta {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.<br>
4. En la sección **Configuración**, sigue los siguientes pasos:

   - Introduce una **cadena de conexión** con los parámetros requeridos para conectarse a tu base de datos de Cisco.   
   `DRIVER={MS SQL Server};Server=myServerAddress;Database=myDataBase;UserId=myUsername;Password=myPassword;`
   - Selecciona la **zona horaria de la base de datos** en el menú desplegable.
   - Introduce tu **ID del cliente** y **contraseña** de Cisco ICM.
   - Introduce tu **puerta de enlace periférica 1**.
   - (Opcional) Introduce tu **puerta de enlace periférica 2**.

4. Haz clic en _Guardar integración_{:.doc-button}.

injixo comenzará entonces a importar datos de adherencia en tiempo real, pero los datos solo serán visibles una vez hayas asignado los identificadores de usuarios externos a tus empleados en injixo.

## Asignar usuarios externos a tus empleados

1. Ve a _WFM > Gestión > Planificación > Empleados_{:.breadcrumbs}.
2. Asigna los identificadores de usuarios externos a tus empleados.
   > Atención
   >
   > Los identificadores de usuarios externos son los «Unified CCE Skill Target IDs» de Cisco.

Aprende cómo {% link_new asignar identificadores de usuarios externos | features/acd-integration/cloud/import-agent-status-data.md | #asignar-identificadores-de-usuarios-externos-a-los-empleados-en-injixo %} a tus empleados.

## Asignar estados de agentes a actividades de injixo

1. Ve a _WFM > Gestión > Planificación > Actividades_{:.breadcrumbs}.
2. Asigna los estados de Cisco ICM a las actividades de injixo.

Aprende cómo {% link_new asignar estados externos | features/acd-integration/cloud/import-agent-status-data.md | #reasignar-actividades-externas %} a actividades de injixo.
