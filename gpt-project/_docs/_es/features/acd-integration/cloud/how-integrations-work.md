---
title: Cómo funcionan las integraciones
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Aprende qué integraciones existen, cómo funcionan y cómo añadirlas y eliminarlas.
promote-service: acd-integration-support
redirect_from: /es/cloud-overview/
redirect_reason: renamed file in Feb 2021
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

Para asistirte con el workforce management, injixo necesita datos de contacto y de los estados de los agentes. Estos datos se encuentran en sistemas externos, como distribuidores automático de llamadas (ACD, por sus siglas en inglés) o sistemas de gestión de relaciones con clientes (CRM, por sus siglas en inglés). Para que injixo reciba y procese tus datos, tienes que integrar tu ACD y/o tu CRM.

injixo ofrece integraciones universales e integraciones de proveedor específico tanto para sistemas cloud como on-premise. Según la integración, iniixo recibe los datos cada 15, 30 o 60 minutos (importe de datos históricos), o incluso en cuestión de segundos (importe de datos en tiempo real).


## Tipos de integración

El tipo de integración determina cómo injixo se conecta al sistema externo:

- Las integraciones cloud se conectan e importan datos directamente desde un sistema en la nube, como Five9 o Vonage.
- Las integraciones on-premise usan {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %} para conectarse a un sistema en tu red local, como Genesys Engage o Sikom. Una vez conectadas, las integraciones on-premise comenzarán a importar hasta tres años de datos históricos.

## Integraciones universales y de proveedor específico

Las integraciones de proveedor específico están adaptadas al sistema específico y deben ser siempre la opción preferida. Si no hay una integración de proveedor específico disponible, también puedes utilizar una de las opciones de integraciones universales:

- Base de datos: integración on-premise que usa una consulta SQL para leer información de una base de datos.
- CSV: integración basada en archivos para importar archivos CSV con injixo Cloud Link.
- injixo API: integración cloud necesaria para enviar consultas HTTP a la API de injixo.

## Qué datos se importan

Según la integración, injixo importa datos de contacto, datos de los estados de los agentes, o ambos.

- Los datos de contacto (llamadas, chats, redes sociales, tickets, correos, documentos) incluyen los volúmenes de llamadas ofrecidas y respondidas, así como el tiempo medio de operación, y se usan para calcular la previsión.
- Los datos de los estados de los agentes (inicio y cierre de sesión, trabajo tras llamada, descansos, etc.) incluyen información sobre las actividades de los empleados, p.&nbsp;ej., cuándo cambian de una actividad a la siguiente. Se usan en la gestión intradiaria.

## Añadir una integración

En los siguientes artículos encontrarás más detalles para configurar tu integración:

- {% link_new Añade una integración cloud | features/acd-integration/cloud/add-cloud-integration.md %}
- {% link_new Añade una integración on-premise  | features/acd-integration/cloud/add-on-premise-integration.md %} 
- {% link_new Añade una integración CSV  | features/acd-integration/cloud/add-csv-integration.md %}
- {% link_new Añade una integración de base de datos | features/acd-integration/cloud/add-database-integration.md %}
- {% link_new Importar datos con la API de injixo | features/acd-integration/cloud/import-data-with-injixo-api.md %}

Cuando hayas añadido una integración, esta empezará a enviar datos a injixo.

Los datos de contacto se importan automáticamente. Para trabajar con datos de contacto, añade colas importadas a una (nueva) carga de trabajo para {% link_new calcular una previsión | getting-started/calculate-a-forecast.md %}. Después, calcula los requisitos de personal y crea tu planificación.

> Prerrequisito para mostrar datos de los estados de los agentes
>
> Para ver datos de los estados de los agentes en Intraday, {% link_new asigna los identificadores de actividades y usuarios externos | features/acd-integration/cloud/import-agent-status-data.md %}. Para ello, suspende primero el importe de datos de tu integración.

<!-- add list of articles? or generic steps? -->

## Suspender el importe de datos

La asignación de actividades será sobrescrita si la integración está en funcionamiento. Para no perder la asignación y evitar duplicar actividades, debes suspender el importe de datos de la integración. Para ello, haz clic en el icono Suspender la importación {% icon pause_circle | icon-only %} junto a la integración en la vista general.

Para reanudar el importe de datos cuando hayas terminado la asignación, haz clic en el icono Reanudar la importación {% icon play_circle | icon-only %}. Se reimportarán los datos que falten.

## Eliminar una integración

Eliminar una integración no elimina los datos importados. Las colas siguen asignadas a tus cargas de trabajo. No puedes eliminar las colas creadas por una integración.

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Haz clic en el icono Editar {% icon pencil | icon-only %} junto a la integración que quieras eliminar.
3. Haz clic en _Eliminar integración_{:.doc-button} abajo a la derecha.
4. En la ventana de confirmación, haz clic en _Sí, eliminar_{:.doc-button}.
