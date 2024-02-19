---
title: Crear cargas de trabajo
redirect_from:
  - /es/workloads/
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Crea cargas de trabajo para representar los volúmenes de contacto históricos, la previsión, y el TMO. Conoce los diferentes tipos de cargas de trabajo.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/forecast/injixo-forecast/what-is-the-injixo-forecast.md
  - overwrite_title: Activar horarios de apertura
    filepath: features/forecast/injixo-forecast/forecast-activate-business-hours.md
---

Para crear, editar o eliminar cargas de trabajo, ve a _Forecast_{:.breadcrumbs}.

Las cargas de trabajo mapean los canales de entrada de tu sistema externo con el que registras los detalles de las interacciones con los clientes. injixo Forecast se basa en los datos de contacto importados y almacenados en colas para calcular una previsión de la carga de trabajo futura. Los eventos configurables, los días festivos o los horarios de apertura influencian el resultado de la previsión. También puedes {% link_new importar tu previsión | features/forecast/injixo-forecast/import-forecast.md %} a las cargas de trabajo.

En las cargas de trabajo configuras el cálculo de los requisitos de personal. Los requisitos de personal son necesarios para la planificación.

¿Estás empezando con injixo Forecast? Consulta primero {% link_new la información básica | features/forecast/injixo-forecast/what-is-the-injixo-forecast.md %}.

## Prerrequisitos

- Añade {% link_new una integración nativa o de archivos CSV | features/acd-integration/cloud/how-integrations-work.md %} e importa datos históricos para al menos una cola.
- Importa contactos ofrecidos, tiempo medio de operación (TMO) y contactos atendidos. Las cargas de trabajo con múltiples colas necesitan los contactos atendidos para mostrar el TMO y calcular promedios ponderados.

injixo crea colas a partir de los datos importados por una integración. El intervalo de importación de datos determina el intervalo de las colas creadas a partir de esos datos. Solo puedes agregar colas con el mismo intervalo a una carga de trabajo.

## Colas y canales

Los datos de contacto importados por una integración se almacenan en colas. Estas colas siempre están asociadas a un canal. Cuando creas [cargas de trabajo](#crear-cargas-de-trabajo), puedes filtrar las colas por canal para asignarlas a la carga de trabajo. Las integraciones nativas establecen automáticamente el canal de las colas. No todas las integraciones soportan todos los canales.
Si usas una integración de archivos CSV tendrás que establecer el canal manualmente. Puedes añadir un canal por columna, o seleccionar un canal para todo el archivo cuando {% link_new asignes las columnas | features/acd-integration/cloud/add-csv-integration.md | #asignar-las-columnas %} de un archivo CSV.  

Las integraciones soportan los siguientes canales:

- Llamadas
- Chats
- Correos electrónicos
- Casos
- Documentos
- Redes sociales

injixo Forecast agrupa las colas por canal. Solo puedes añadir colas con el mismo canal a una carga de trabajo.

<!-- anchor for intercom forecast tour -->

## Crear cargas de trabajo

Recomendamos crear una carga de trabajo para cada actividad que quieras planificar con requisitos de personal. Las multiactividades requieren una carga de trabajo para la multiactividad y una carga de trabajo para cada subactividad.

1. Haz clic en _Nueva carga de trabajo_{:.doc-button} arriba de la lista.
2. Introduce la información general de tu carga de trabajo:
   - **Nombre**: nombre único para identificar tu carga de trabajo.
   - **Zona horaria**: la {% link_new zona horaria | best-practices/working-with-timezones.md %} de la carga de trabajo no se puede editar más adelante.

     > Atención
     >
     > - Para guardar los requisitos de personal para una unidad de planificación, la zona horaria de la carga de trabajo debe coincidir con la zona horaria de la unidad de planificación.
     > - Si seleccionas una zona horaria para la carga de trabajo distinta a la zona horaria de la integración con la que importas datos, los datos importados se mostrarán desplazados en la carga de trabajo. Por ejemplo, si una integración de archivos CSV está configurada con la zona horaria UTC, y tu carga de trabajo está configurada con la zona horaria CEST (UTC +2 horas), los datos importados marcados a las 08:00 aparecerán a las 10:00 en la carga de trabajo.

   - (Opcional) **Región para los festivos**: incluye días festivos nacionales que pueden afectar a la previsión.
   - (Opcional) **Unidad de planificación** y **Actividad**: requerido para {% link_new activar los horarios de apertura | features/forecast/injixo-forecast/forecast-activate-business-hours.md %} en la sección **Horarios de apertura**.

3. (Solo para injixo Classic) Selecciona una opción en la sección **Modelo de precios**:

   - **Modo activo** (de pago): se factura mensualmente. No se puede revertir al modo de prueba.
   - **Modo test** (gratuito): solo puedes ver la previsión, pero no puedes transferir requisitos de personal para la planificación.

4. En la sección **Asignar colas**, selecciona las colas para tu carga de trabajo.

   Para limitar las colas mostradas:

   - Filtra las colas por canal (Llamadas, Chats, etc.).
   - Usa las casillas para mostrar colas seleccionadas, no seleccionadas o inactivas. Las colas inactivas son las importadas por integraciones que han sido eliminadas.
   - Usa el campo de búsqueda arriba de la tabla. Puedes buscar nombres de colas, integraciones o cargas de trabajo.

   Ten en cuenta que si el intervalo o canal de una cola no coincide con el de las colas seleccionadas, todas las colas que no coincidan se mostrarán en gris.

5. Haz clic en _Crear carga de trabajo_{:.doc-button}.

   La página muestra los datos históricos y una versión preliminar de la previsión.  
   Cuando el cálculo se haya completado, actualiza la página para ver la versión final de la previsión.  
   La nueva carga de trabajo aparecerá en la lista de cargas de trabajo.

Si usas injixo Essential, puedes crear cargas de trabajo Basic. Las cargas de trabajo Basic requieren al menos dos semanas de datos históricos. Las cargas de trabajo Basic no permiten incluir horarios de apertura.

Si usas injixo Advanced o Enterprise WFM, puedes crear cargas de trabajo Smart. Las cargas de trabajo Smart generan una previsión basada en un solo día de datos históricos. Las cargas de trabajo Smart admiten horarios de apertura.

Si usas injixo Classic, tienes que seleccionar adicionalmente el modelo de previsión (Smart o Basic) para cada carga de trabajo. Para las cargas de trabajo Smart, tienes que elegir entre el modo activo y el modo test. El modo test es gratuito, pero solo te muestra la previsión, y no permite transferir requisitos de personal para usarlos durante la planificación. El modo activo ofrece la funcionalidad completa y se factura mensualmente. Las cargas de trabajo Smart en modo activo no se pueden revertir al modo test.

<!-- hidden: feature not live yet -->
<!-- ## Create workloads without historical data

You only need an integration and historical data import if you want injixo to create forecasts. To add forecast data by {% link_new importing a forecast | features/forecast/injixo-forecast/import-forecast.md %} that has been generated externally or to {% link_new create constant staff requirements | features/forecast/requirement-scripts/requirement-constant.md %}, you can create a workload using the tab *Forecast Import*:

1. Go to **Forecast**{:.breadcrumbs}.
2. Click _Create Workload_{:.doc-button} in the upper right corner of the forecast page.
3. In the *Basic configuration* section, enter a **Name** for your new workload.
4. Select the **Time zone** to display data. Note: The set time zone must match the planning unit to save staff requirements.
5. (Optional) Select the **Holiday region** to acknowledge all public holidays that affect your forecast for the year.
6. Select the **Planning unit** and the **Activity**. Note: You must select an option to calculate staff requirements.
    {{ 4 | image: 'Import Workload basic configuration section' }}
7. Click the tab **Forecast import**.
8. Select your **Interval length** and the **Channel** for the data import. Both must correspond with your import file.
    {{ 5 | image: 'Import Workload parameters' }}
9. Click *Create workload*{:.doc-button}. -->

## Editar cargas de trabajo

1. Selecciona una carga de trabajo de la lista, o introduce el nombre de la carga de trabajo en el campo de búsqueda.
2. Para modificar los detalles de la carga de trabajo, haz clic en el {% icon pencil %}.  
   Puedes añadir o eliminar colas sin tener que reimportar datos. Las colas listadas se mostrarán en gris si su intervalo o canal no coincide con el de las colas ya asignadas.
3. Haz clic en _Guardar carga de trabajo_{:.doc-button}.  
   Puede ser que la nueva configuración actualice la previsión.

## Eliminar cargas de trabajo

1. Haz clic en el {% icon trash %} junto a la carga de trabajo en la lista.
2. En la ventana de confirmación, haz clic en _Eliminar carga de trabajo_{:.doc-button}.  
    injixo almacena los datos históricos asociados. Para reutilizar los datos, añade la cola o colas a otra carga de trabajo.
