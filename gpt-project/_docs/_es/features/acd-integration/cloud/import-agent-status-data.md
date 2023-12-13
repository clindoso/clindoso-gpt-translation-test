---
title: Importar datos de los estados de los agentes
product_label:
  - advanced
  - enterprise
  - classic
description: Configura injixo para importar correctamente datos de los estados de los agentes.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-cloud-integration.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/add-five9-integration.md
---

Los sistemas externos, como los ACD, registran cuándo las personas cambian de una actividad a otra. injixo puede usar estos datos para la gestión intradiaria.

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Prerrequisitos

Para importar datos de los estados de los agentes, primero tienes que {% link_new añadir una integración | features/acd-integration/cloud/how-integrations-work.md %}. La integración debe poder importar datos de los estados de los agentes.

Para ver si tu integración puede importar este tipo de datos, ve a _Account > Integraciones_{:.breadcrumbs}. Si ya existe una integración, haz clic en Añadir integración. En los recuadros de cada integración verás el texto Estados de los agentes (datos históricos) o RTA (datos en tiempo real).

Una vez hayas añadido la integración, tendrás que asignar los identificadores de usuarios externos a tus empleados en injixo. También puedes reasignar los estados externos a las actividades de injixo.

## Identificadores de usuarios externos

Los identificadores de usuarios externos son específicos de cada sistema externo. Usan una dirección de correo, nombre de usuario o código de agente para identificar a los usuarios en el sistema externo.

Para evitar fallos en la importación, comprueba que la ortografía, las mayúsculas y minúsculas y los espacios sean correctos.

| Sistema externo                 | Identificador de usuario requerido              |
| ---------------------- | ------------------------------------- |
| Five9                  | Nombre de usuario de Five9                  |
| Genesys Cloud          | Nombre de usuario de PureCloud              |
| Genesys Engage         | Nombre de usuario de PureEngage             |
| Talkdesk               | Correo electrónico usado en Talkdesk        |
| UJET                   | Correo electrónico usado en UJET            |
| Sikom                  | Nombre de usuario de Sikom                  |
| Mitel MiVoice Business | Nombre de usuario de Mitel MiVoice Business |
| Vonage                 | Código de agente de Vonage                  |
| Avaya CMS              | Nombre de usuario de Avaya CMS              |

## Asignar identificadores de usuarios externos a los empleados en injixo

Para importar datos, tienes que asignar los identificadores de usuarios externos a los empleados en injixo. Puedes asignárselos a todos los empleados o solo a aquellos cuyos datos quieras importar.

1. Ve a _WFM > Gestión > Planificación > Empleados_{:.breadcrumbs} y selecciona un empleado.
2. En la parte superior, haz clic en **Sistemas externos** o desplázate hasta la sección **Sistemas externos**.
3. Haz clic en el icono Insertar {% icon item-add | icon-only %} para añadir un sistema externo.  
   Se abre una ventana.
4. En el menú desplegable **Sistema externo**, selecciona la integración que acabas de configurar.
5. En el campo **ID del empleado en el sistema externo**, introduce el código del empleado, p.&nbsp;ej., su identificador personal.
6. En el campo **Ampliación**, introduce el identificador de usuario del sistema externo para el empleado, p.&nbsp;ej., su dirección de correo electrónico.
7. Haz clic en _Aceptar_{:.doc-button}.

Una vez hayas actualizado las secciones de los empleados, la próxima importación incluirá los datos de los estados de los agentes.


## Reasignar actividades externas

Las actividades externas son aquellas que el sistema externo registra cuando las personas inician o cierran sesión, o cuando cambian de una actividad a otra, p.&nbsp;ej., de responder correos electrónicos a llamadas.

Puedes reasignar actividades externas a actividades existentes en injixo. Si por lo contrario decides {% link_new crear nuevas actividades | features/administration/activities.md | #crear-una-actividad %}, asegúrate de añadirlas a tu {% link_new unidad de planificación | features/administration/create-and-manage-planning-units.md | #añadir-actividades %} para que puedan ser mostradas correctamente.

Por defecto, las integraciones registran estas actividades en la actividad Presente (ID 1) y muestran el estado del agente Presente para todas las actividades. injixo puede mostrar las mismas actividades que tu sistema externo. Para ello, tienes que reasignar las actividades externas a otras actividades de injixo.


Para poder reasignar actividades, primero debes pausar la integración:

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. En la lista de integraciones, haz clic en el icono Suspender la importación {% icon pause_circle | icon-only %} junto a la integración cuyas actividades quieres reasignar.

Una vez hayas pausado tu integración, sigue estos pasos:

1. Ve a _Plan > Configuración > Actividades_{:.breadcrumbs}.
2. Selecciona la actividad que quieres reasignar.
3. En la sección **Sistemas Externos**, haz clic en _Editar en WFM_{:.doc-button}. 
4. Navega hasta la sección **Sistemas externos**.
5. Haz clic en el icono Insertar {% icon item-add | icon-only %} .
6. En la ventana **Sistemas externos**:<br>
   - En el menú desplegable **Sistema externo**, selecciona tu integración.
   - En el menú desplegable **Nombre de la actividad en el sistema externo**, selecciona la actividad externa que quieres asignar a la actividad de injixo que estás editando.
   - En el menú desplegable **Clasificación**, selecciona el valor 1.
7. Haz clic en _Aceptar_{:.doc-button}.

Para reasignar más actividades, haz clic en la siguiente actividad y repite el proceso en el menú de configuración a la derecha.


Cuando hayas terminado de asignar actividades, ve a _Account > Integraciones_{:.breadcrumbs} y haz clic en el icono Reanudar la integración {% icon play_circle | icon-only %} junto a la integración.
