---
title: Añadir una integración de Odigo
description: Aprende cómo conectar tu distribuidor de llamadas de Cisco a injixo para importar datos.
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

La integración de Odigo importa datos sobre los estados de los agentes y datos de adherencia en tiempo real.

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Añadir una integración de Odigo

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Odigo**, haz clic en _Añadir integración_{:.doc-button}.
4. Introduce un nombre inequívoco para la integración que identifique el origen de los datos.
5. (Opcional) Configura la importación de detalles de los estados de pausa de los agentes.
- Marca la casilla **Importar detalles de los estados de pausa de los agentes**.<br>Cuando se importan los estados de pausa, injixo incluirá información sobre el tipo de pausa.<br>Ten en cuenta que si marcas esta casilla, también necesitas actualizar la {% link_new asignación de actividades | features/acd-integration/cloud/import-agent-status-data.md | #reasignar-actividades-externas %}.
- Introduce tu URL de Odigo, incluida tu ID de cliente.
- Introduce el nombre de usuario y la contraseña para el servicio web.
6. Haz clic en _Guardar integración_{:.doc-button}.

## Configurar tu integración de Odigo

1. En la sección **Generar token de URL injixo**, haz clic en _Generar_{:.doc-button}.
2. Copia el token de URL injixo.<br>
El token de URL injixo solo aparece una vez. Si no puedes completar la configuración directamente, guárdalo en un lugar seguro, p.&nbsp;ej., en un gestor de contraseñas.
3. En la sección de administración de tu aplicación Odigo, activa el envío de notificaciones a servidores externos. Para ello, ponte en contacto con Odigo.
4. Pega el **token de URL injixo** en el campo para URL de notificación.
5. Guarda tu configuración en Odigo y regresa a injixo.

Para activar la integración, tendrás que reiniciar el servidor. Para ello, ponte en contacto con Odigo.<br>
injixo comenzará entonces a importar datos de adherencia en tiempo real, pero los datos solo serán visibles cuando hayas asignados los identificadores de usuarios externos a tus empleados en injixo.

## Asignar usuarios externos a tus empleados

1. Ve a _WFM > Gestión > Planificación > Empleados_{:.breadcrumbs}.
2. Asigna los identificadores de usuarios externos a tus empleados.

Aprende cómo {% link_new asignar identificadores de usuarios externos | features/acd-integration/cloud/import-agent-status-data.md | #asignar-identificadores-de-usuarios-externos-a-los-empleados-en-injixo %} a tus empleados.

## Asignar estados de agentes a actividades de injixo

1. Ve a _WFM > Gestión > Planificación > Actividades_{:.breadcrumbs}.
2. Asigna los estados de Odigo a las actividades de injixo.

Aprende cómo {% link_new asignar estados de agentes | features/acd-integration/cloud/import-agent-status-data.md | #reasignar-actividades-externas %} a actividades de injixo.
