---
title: Importar datos con la API de injixo
navigation_title: injixo API
product_label:
  - advanced
  - enterprise
description: Añade una integración con la API de injixo para importar datos de contactos y datos de los estados de los agentes de tu sistema externo.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/manage-workloads.md
  - overwrite_title: Gestionar Dashboards
    filepath: features/monitoring/dashboards/dashboards-overview.md
---

injixo usa integraciones universales y de proveedor específico para importar datos de contactos y datos de los estados de los agentes de sistemas externos.

## ¿Qué es una integración con la API de injixo?

En injixo Advanced y Enterprise, las integraciones con la API de injixo permiten enviar consultas vía API para importar datos (p.&nbsp;ej., si no existe una integración estándar para tu sistema externo). Con este fin, la API de injixo ofrece los siguientes recursos:

- [Recurso para eventos de contacto](https://api.injixo.com/resources/integration_contact_event/): los eventos de contacto se registran cuando los clientes contactan con tu organización por teléfono, correo electrónico o chat. injixo agrupa estos datos en colas organizadas por nombre de cola y por canal.
- [Recurso para los estados de los agentes](https://api.injixo.com/resources/integration_agent_status/): los datos de los estados de los agentes se registran cuando los empleados cambian de una actividad a otra, p.&nbsp;ej. inicio de sesión, trabajo tras llamada o cierre de sesión.

## Añadir una integración con la API de injixo

Los usuarios con acceso de administrador pueden seguir los siguientes pasos para añadir una integración con la API de injixo:

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Universal Interfaces**, haz clic en _Selecciona el modelo_{:.doc-button}.
4. En la sección **injixo API**, haz clic en **Añadir integración**.
5. Introduce un nombre inequívoco para la nueva integración.
6. Haz clic en **Guardar integración**.<br>Ahora puedes acceder a la sección **Acceder a la API de injixo**.
7. Para generar la clave de la API de injixo, haz clic en _Generar_{:.doc-button}.

La autenticación también funciona con tokens de acceso personal creados en la sección {% link_new **Tokens de acceso personal** | features/reporting/injixo-api/injixo-api.md | #authorization-personal-access-token %} en los perfiles de usuario.

> No podrás acceder a la clave de la API más adelante. 
>
> - Guarda la clave de la API en un lugar seguro, como tu gestor de contraseñas.
> - La clave actual de la API expirará si otro usuario genera una clave nueva para la integración o si se elimina la integración.

## Importar datos <a id="import-contact-or-agent-status-data">

Para identificar y autenticar la integración con la API, incluye la clave de la API de injixo y el identificador de la configuración de la integración en las solicitudes de la API:

1. Añade tu clave de la API de injixo al encabezado de la solicitud de autorización.
2. Encuentra o copia tu ID de configuración de la integración:
    - Ve a _Account > Integraciones_{:.breadcrumbs}.
    - En tu sección de la integración con la API, haz clic en el {% icon pencil %}.
    - En la sección **Acceder a la API de injixo**, haz clic en _{% icon clone | icon-only %}Copiar_{:.doc-button}.
3. Añade tu ID de configuración de la integración al objeto **meta** en el cuerpo de la solicitud.

Para importar regularmente datos de tu sistema externo a injixo, tienes que ejecutar tu propia aplicación. Puedes encontrar ejemplos de scripts en Ruby y Python en las guías del usuario en la [documentación de la API de injixo](https://api.injixo.com) (en inglés).

## Testar la importación de datos

Para realizar pruebas, puedes enviar solicitudes POST únicas a la API. La estructura de los datos en los siguientes ejemplos incluye un único punto de datos, pero puedes modificarlo si lo necesitas. Sustituye al menos la clave API de muestra (abc123456=) y el valor de integrationConfigurationId (1234) con tus propios datos.

La API solo es compatible con HTTPS. Envía tus solicitudes a https://api.injixo.com para evitar los errores `not_found`.

### cURL en la línea de comandos

Los siguientes ejemplos muestran cómo enviar datos a la API con [cURL](https://curl.se/). cURL es una herramienta de línea de comandos que intercambia datos con un servidor a través de una consola.

Eventos de contacto:

```
curl -X POST \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer abc123456=" \
 -d '{"data":[{"properties":{"offered":true,"handled":false,"duration":124.6},"queueName":"Level 1 support","queueIdentifier":"1337_99","timestamp":"2021-12-06T10:34:22Z","channel":"calls"}],"meta":{"integrationConfigurationId":1234}}' \
 https://api.injixo.com/external-systems/contact-events
```

Ten en cuenta que  cada nueva combinación de `queueIdentifier`, `queueName`, y `integrationConfigurationId`creará una cola nueva. Para evitar nombres de cola duplicados, asegúrate de añadir el mismo queueIdentifier o el mismo integrationConfigurationId a cada solicitud con el mismo nombre de cola. 

Estados de los agentes:

```
curl -X POST \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer abc123456==" \
 -d '{"data":[{"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2021-12-06T10:00:00Z","endTime":"2021-12-06T15:00:00Z"}],"meta":{"integrationConfigurationId":8431,"externalSystem":"My ACD"}}' \
 https://api.injixo.com/external-systems/agent-statuses
```

### Clientes REST

Los siguientes ejemplos muestran cómo enviar datos a la API con un cliente REST, como [Postman](https://www.postman.com/downloads/).

1. Incluye un encabezado de solicitud JSON:

   ```
   {
  "Content-type": "application/json",
  "Authorization": "Bearer abc123456="
}
   ```

2. Incluye un cuerpo de solicitud JSON distinto para eventos de contacto y para datos de los estados de los agentes.<br><br>

   Ejemplo de cuerpo de solicitud para eventos de contacto: `/external-systems/contact-events`:

   ```
   {
  "data": [
    {
      "properties": { "offered": true, "handled": false, "duration": 124.6 },
      "queueName": "Level 1 support",
      "queueIdentifier": "1337_99",
      "timestamp": "2021-12-06T10:34:22Z",
      "channel": "calls"
    },
    {
      "properties": { "offered": true, "handled": true, "duration": 200.1 },
      "queueName": "Level 1 support",
      "queueIdentifier": "1337_99",
      "timestamp": "2021-12-06T10:46:22Z",
      "channel": "calls"
    }
  ],
  "meta": { "integrationConfigurationId": 1234 }
}
   ```

   Ejemplo de cuerpo de solicitud para eventos de contacto: `/external-systems/agent-statuses`:

   ```
   {
  "data": [
    {"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2022-12-06T08:00:00Z","endTime":"2022-12-06T13:00:00Z"},
    {"agentIdentifier":"bob@mycompany.com","activityIdentifier":"Test","startTime":"2022-12-07T09:00:00Z","endTime":"2022-12-07T10:00:00Z"}
  ],
  "meta": {
    "integrationConfigurationId": 1234,
    "externalSystem": "My ACD"
  }
}
   ```

## Tu primera solicitud API: ¿y ahora qué?

Una vez hayas enviado correctamente una solicitud API, tienes que esperar para ver los datos en injixo. Hay dos formas de trabajar con los datos importados:

- Solicitudes de eventos de contacto: en Forecast, las páginas Nueva carga de trabajo y Editar carga de trabajo mostrarán las colas importadas una vez los datos hayan sido procesados.
- Solicitudes de datos de los estados de los agentes: la primera solicitud con nuevos ID de agentes no dará como resultado datos reales de los estados de los agentes en Shift Center. Para ver los datos, {% link_new asigna al menos un identificador externo | features/acd-integration/cloud/import-agent-status-data.md | #asignar-identificadores-de-usuarios-externos-a-los-empleados-en-injixo %} (enviado como agentIdentifier) a un empleado. Tendrás que enviar otra solicitud para poder ver los datos.
