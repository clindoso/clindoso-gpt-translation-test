---
title: Requisitos del sistema
description: Requisitos de navegador y hardware para las integraciones y las estaciones de trabajo de agentes y planificadores.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/browser-setup.md
---

injixo es un sistema SaaS de workforce management basado en explorador. Está disponible en distintos [planes WFM](https://www.injixo.com/pricing): injixo Essential WFM, injixo Advanced WFM e injixo Enterprise WFM.

## Requisitos de navegador

injixo es compatible con las dos últimas versiones de los siguientes navegadores:

- Microsoft Edge
- Google Chrome
- Mozilla Firefox
- Apple Safari

## Bloqueador de ventanas emergentes

injixo utiliza ventanas emergentes para mostrar ventanas de diálogo adicionales. Para permitir a injixo mostrar ventanas emergentes, sigue los siguientes pasos:

- Desactiva el bloqueador de ventanas emergentes en [Microsoft Edge](https://support.microsoft.com/en-us/microsoft-edge/block-pop-ups-in-microsoft-edge-1d8ba4f8-f385-9a0b-e944-aa47339b6bb5).
- Configura una excepción para el bloqueador de ventanas emergentes en [Google Chrome](https://support.google.com/chrome/answer/95472?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Callow-pop-ups-and-redirects-from-a-site), [Mozilla Firefox](https://support.mozilla.org/en-US/kb/pop-blocker-settings-exceptions-troubleshooting) y [Apple Safari](https://support.apple.com/guide/safari/block-pop-ups-sfri40696/mac).

## Modo Internet Explorer (IE) en Microsoft Edge

Las funcionalidades basadas en ActiveX de WFM requieren el {% link_new modo IE en Microsoft Edge | support/faq/configure-edge-internet-explorer-mode.md %}. Para configurar el modo IE necesitar una [lista de sitios en un archivo XML](https://learn.microsoft.com/en-us/deployedge/edge-ie-mode-local-site-list).

<style>
table {
  width: 100%;
}
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

| Plan WFM                               | Requiere el modo IE en Microsoft Edge         |
| -------------------------------------- | ------------------------------------------ |
| Essential WFM                          | No                                         |
| Advanced WFM                           | No                                         |
| Enterprise WFM                         | Solo para las funcionalidades personalizadas            |
| Classic <sup>1</sup>                   | Sí                                        |
| Enterprise WFM on-premise <sup>1</sup> | Sí<br>No se puede iniciar sesión si no está configurado. |

<sup>1</sup> Versiones antiguas del sistema que aún utilizan algunos clientes.

Si utilizas un navegador incompatible o no has configurado correctamente el modo IE, el logo de IE en la navegación de WFM identifica las funcionalidades que requieren el modo IE (planes Classic/Enterprise WFM).

{% link_new injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} funciona en cualquier navegador de la lista, en ordenadores, smartphones y tablets. 

## Cliente injixo

Las funcionalidades basadas en ActiveX de WFM requieren {% link_new el cliente injixo | getting-started/browser-setup.md %}.

Puedes consultar los requisitos de sistema operativo en la descripción de la descarga en [downloads.injixo.com](https://downloads.injixo.com).

| Plan WFM                      | Requiere el cliente injixo                |
| ------------------------- | ----------------------------------------- |
| Essential WFM             | No                                        |
| Advanced WFM              | No                                        |
| Enterprise WFM            | Solo para las funcionalidades personalizadas           |
| Classic                   | Sí                                       |
| Enterprise WFM on-premise | Sí<br>No se puede iniciar sesión si no está instalado. |

Si el cliente no ha sido instalado, el logo de IE en la navegación izquierda identifica las funcionalidades que requieren el modo IE (Classic/Enterprise WFM).

{% link_new injixo Me | features/injixo-me/set-up-injixo-me/configure-injixo-me.md %} no requiere el cliente injixo.

## Excepciones del cortafuegos

Para acceder a los sitios web de injixo, autoriza el tráfico de red entrante y saliente para *.injixo.com a través del puerto 443.

Si utilizas funcionalidades basadas en ActiveX o aplicaciones SDK personalizadas, añade otra excepción al cortafuegos. Estas aplicaciones utilizan el puerto 45054 para el tráfico saliente (puerto 80 para los host injixo anteriores a 2019) y requieren acceso directo a internet por TCP (protocolo de control de transmisión, por sus siglas en inglés). Los servidores proxy configurados en el navegador no son compatibles.

Para obtener la dirección para configurar la excepción, haz clic en _WFM_{:.menu-item} y usa el nombre de tu espacio injixo que puedes ver en la barra de navegación, p.&nbsp;ej., wfm-123abc.injixo.com.

Si necesitas más información sobre las excepciones del cortafuegos en Windows, consulta la [documentación de Microsoft](https://support.microsoft.com/es-es/windows/agregar-una-exclusi%C3%B3n-a-seguridad-de-windows-811816c0-4dfd-af4a-47e4-c301afe13b26).

### Compartir las URL para WebSockets

Para enviar actualizaciones en tiempo real a los usuarios, p.&nbsp;ej., en el {% link_new Centro de planificación | features/scheduling/shiftcenter/shift-center-overview.md %} o en Adherencia en tiempo real, injixo utiliza el protocolo WebSocket (basado en TCP) mediante el puerto 443\. injixo abre una página web que establece una conexión WebSocket. Añade las siguientes direcciones a la lista de sitios de confianza:

- https://shiftcenter.injixo.com
- wss://shiftcenter.injixo.com
- https://www.injixo.com
- wss://ws.injixo.com

En injixo Advanced e injixo Enterprise WFM, el Centro de Planificación requiere WebSockets para poder funcionar a la máxima velocidad. La tecnología subyacente ofrece un mecanismo de reserva más lento en caso de que WebSockets no esté disponible. No todas las funcionalidades ofrecen mecanismos de reserva.

## Requisitos de ancho de banda

injixo está diseñado y optimizado para ofrecer un alto rendimiento y un bajo consumo de recursos. Durante el primer acceso, los gráficos se descargan y almacenan localmente en archivos temporales. A partir de entonces, solo se transfiere información básica de forma segura al dispositivo local.

Un centro de contactos con 200 empleados puede esperar una transferencia de datos de 25-50&nbsp;MB por hora si todos los usuarios están conectados.

## Requisitos para integraciones

Configura {% link_new integraciones | features/acd-integration/cloud/how-integrations-work.md %} para que injixo pueda importar y procesar datos de contacto y datos de los estados de los agentes. Estos datos se encuentran en sistemas externos, como distribuidores automático de llamadas (ACD, por sus siglas en inglés) o sistemas de gestión de relaciones con clientes (CRM, por sus siglas en inglés).
injixo soporta una gran variedad de integraciones en la nube y on-premise.

Instala el {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} para importar regularmente datos de integraciones on-premise o de archivos CSV.

Las solicitudes de datos no interfieren con las funciones principales de los programas de comunicación, como plataformas de telefonía o de email.

Las solicitudes de información en tiempo real sobre los estados de los agentes pueden usar una fuente directa. Estas fuentes solo transmiten los cambios de actividad de los agentes (incluyendo una marca de tiempo, un identificador del agente y un código de estado) y ocupan aproximadamente 1 kB cada una.

## Centro de datos y políticas de seguridad

injixo opera en centros de datos en la infraestructura de Amazon EC2. [Las políticas de seguridad de Amazon](https://aws.amazon.com/security/) son por lo tanto aplicables a injixo, p.&nbsp;ej., SOC 1 Type 2, ISO 27001 y PCI DSS Level 1.

Toda la información se almacena en la UE (para los clientes europeos) y en los EE.UU. (para los clientes estadounidenses). De este modo, injixo cumple con toda la legislación de protección de datos relevante, también con el RGPD en Europa. Puedes leer más sobre [la seguridad en la nube y el cumplimiento de normativas por parte de injixo](https://www.injixo.com/uk/security/).
