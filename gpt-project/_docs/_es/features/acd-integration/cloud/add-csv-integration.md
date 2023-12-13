---
title: Añadir una integración de archivos CSV
navigation_title: CSV
description: Importa datos históricos de archivos CSV a injixo.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
---

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Qué es una integración de archivos CSV

Una integración de archivos CSV importa datos históricos de contactos o de los estados de los agentes desde archivos CSV. Usa una integración de archivos CSV si tu sistema no puede conectarse con ninguna otra integración.

Para configurar una integración de archivos CSV, sigue estos pasos:

- Crea una integración de archivos CSV en injixo
- Crea un esquema CSV
- Asigna las columnas (usa los menús desplegables o una consulta SQL)
- Importa tus archivos CSV de forma automática o manual

## Añadir una integración de archivos CSV

Para importar diferentes formatos de archivo CSV (p.&nbsp;ej., con separadores, formatos de fecha o nombres de columna distintos), configura una integración para cada formato. Dependiendo del tipo de archivo CSV que genere tu sistema externo, puede que injixo espere columnas distintas a las que incluye tu CSV. [Aprende más](#asignar-las-columnas) sobre las columnas que injixo espera y cómo asignarlas si tu archivo CSV contiene columnas o nombres de columnas diferentes.

Para añadir una integración de archivos CSV en injixo, sigue estos pasos:

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En el recuadro **Universal Interfaces**, haz clic en _Selecciona el modelo_{:.doc-button}.
4. En la sección **CSV**, haz clic en _Añadir integración_{:.doc-button}.

## Configurar una nueva integración de archivos CSV

1. Introduce un nombre inequívoco para la nueva integración que identifique el origen de los datos.
2. En la sección **injixo Cloud Link**, instala y conecta {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md | #instalar-injixo-cloud-link %}. Si prefieres [importar los datos manualmente](#importación-manual-de-archivos), puedes saltarte este paso.
3. En la sección **Configuración**, selecciona el tipo de datos a importar:
   - **Datos de contacto**: los datos subidos incluyen todos los volúmenes ofrecidos y gestionados registrados en tu sistema externo, como llamadas, chats, redes sociales, tickets, correos electrónicos o documentos.
   - **Estados de los agentes**: los datos subidos incluyen todas las actividades de agentes registradas en su sistema externo, como inicio de sesión, cierre de sesión, en llamada, trabajo tras llamada, descanso, preparado, etc.
4. Haz clic en _Crear un nuevo esquema CSV_{:.doc-button}.
5. Configurar el esquema CSV. Esto incluye:
   - Opciones de configuración y preprocesamiento
   - Asignación de columnas (por defecto mediante [menús desplegables](#asignar-las-columnas); alternativamente mediante una [consulta SQL](#asignar-las-columnas-consulta-sql))  
      Aprende cómo [crear un esquema CSV](#crear-un-esquema-csv) que incluya las opciones de configuración anteriores.
6. Haz clic en _Guardar integración_{:.doc-button} para crear la integración.

Una vez hayas guardado la integración podrás usar la [importación manual de datos](#importación-manual-de-archivos) o configurar la [importación automática de datos](#importación-automática-de-archivos).

## Crear un esquema CSV

Cada integración de archivos CSV tiene su propio esquema CSV. El esquema CSV describe el formato del archivo CSV y la asignación de las columnas. Si tu sistema externo genera un archivo CSV que no incluye exactamente los nombres de columna que se muestran en injixo, puedes usar los [menús desplegables (por defecto)](#asignar-las-columnas) o una [consulta SQL](#asignar-las-columnas-consulta-sql) para asignarlos en injixo.   
[Aprende más](#asignar-las-columnas) sobre las columnas que injixo espera y cómo asignarlas si tu archivo CSV contiene columnas o nombres de columnas diferentes.

Para poder crear un esquema CSV, primero tienes que [añadir una integración de archivos CSV](#añadir-una-integración-de-archivos-csv) y seleccionar el tipo de datos a importar. Los parámetros que configures para el esquema CSV dependerán del tipo de datos a importar que selecciones (datos de contacto o estados de los agentes).

### Opciones de configuración y preprocesamiento

1. En la sección **Configuración**, sube un archivo CSV de muestra generado por tu sistema externo. Así podrás ver cómo maneja injixo los archivos de tu sistema durante la importación.
2. Configura los siguientes parámetros. Dependiendo del tipo de datos a importar, los parámetros variarán:<br><br>

   | Parámetro                                                     | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Separador de columna del archivo CSV**                              | Carácter separador utilizado en el archivo CSV que has subido, p.&nbsp;ej., punto y coma.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | **Zona horaria**                                                 | Zona horaria en la que tu sistema externo registra los datos, p.&nbsp;ej., Europe/Madrid (UTC+01:00).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | **Disposición de los datos**<br>(Solo para datos de contacto)                     | La disposición de los datos depende de cómo se generó tu archivo CSV:<br>**Basado en contactos**: para archivos que contienen una línea por contacto. Dado que los datos importados basados en contactos se agregan en intervalos de 15 minutos, el intervalo de la unidad de planificación debe ser de 15 minutos. Nuevas importaciones de datos sobrescribirán los datos importados previamente para el intervalo. Si tu archivo contiene la misma marca de tiempo varias veces, estos datos se sumarán por intervalo.<br><br>**Basado en intervalos**: para datos agregados que contienen una línea con toda la información de contacto por intervalo. Selecciona la longitud de intervalo que coincida con la de tu archivo CSV. Si seleccionas un intervalo más largo que el de los archivos subidos, verás un mensaje de error. Si seleccionas un intervalo más corto que el de los archivos, p.&nbsp;ej., un intervalo de de 15 minutos para un archivo con intervalos de 30 minutos, cada intervalo faltante (en este caso, cada segundo intervalo) será completado con un 0 o el texto no data, según lo que hayas configurado en la opción **Gestión de los valores faltantes en los intervalos**. |
   | **Gestión de los valores faltantes en los intervalos**<br>(Solo para datos de contacto) | Define cómo mostrar los valores que faltan en la cola objetivo en otras partes en injixo:<br>**Rellenar con cero**: los valores que falten se reemplazarán con un cero.<br>**Dejar vacío**: los valores que falten se reemplazarán con el texto: no data.<br>**Dejar vacío** se ajusta a la mayoría de los escenarios. La importación sobrescribe los datos existentes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

3. (Opcional) En la sección **Opciones de preprocesamiento**, selecciona una o varias opciones relevantes para tu formato de archivo CSV:<br><br>

   | Opción de preprocesamiento       | Descripción                                                                                                                                                                                             |
   | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Añadir fila de encabezado**         | En los archivos sin fila de encabezado, injixo etiquetará las columnas como A, B, C, etc. en la página [Asignar columnas](#asignar-las-columnas).                                                                        |
   | **Omitir filas vacías**        | injixo ignorará las filas que solo incluyan separadores.                                                                                                                                                  |
   | **Omitir la(s) primera(s) X fila(s)**        | injixo eliminará las filas adicionales al principio del archivo. Introduce el número de filas que deben ser eliminadas.                                                                                               |
   | **Omitir la(s) filas()) que contengan** | injixo ignorará las filas que incluyan ciertos caracteres. Introduce un texto (distingue entre mayúsculas y minúsculas). injixo ignorará las filas que incluyan este texto. Para añadir múltiples textos, haz clic en _Añadir texto_{:.doc-button}. |

4. Para continuar con la asignación de columnas, haz clic en _Asignar las columnas_{:.doc-button}.

### Asignar las columnas

Por defecto, puedes utilizar los menús desplegables en la sección **Asignar columnas** para definir cómo emparejar las columnas de tus archivos CSV con las columnas requeridas por injixo. Antes de asignar las columnas, tienes que completar la [configuración](#opciones-de-configuración-y-preprocesamiento).
Si tu sistema externo genera archivos CSV que no incluyen las columnas esperadas, puede [asignarlas mediante una consulta SQL](#asignar-las-columnas-consulta-sql).

La página Asignar columnas muestra una vista previa del archivo CSV que has subido.

1. Usa los menús desplegables para asignar las columnas y formatos del archivo CSV.

2. Rellena todos los campos.  
   Aprende más sobre las opciones para [datos de contacto](#desplegables-para-datos-de-contacto) y [datos de los estados de los agentes](#desplegables-para-estados-de-los-agentes) en la tabla a continuación.

3. Para guardar tu configuración, haz clic en _Guardar esquema_{:.doc-button}.

#### Desplegables para datos de contacto

Si has seleccionado **Datos de contacto** como tipo de datos a importar, la página de asignación muestra los siguientes elementos:

| Campo          | Descripción                                                                                                                                                                                                                                          | Necesario para datos basados en intervalos | Necesario para datos basados en contactos |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------: | :-----------------------------: |
| **Nombre de la cola** | Nombre de la cola de la que se importan los datos.                                                                                                                                                                                                        |               Sí                |               Sí               |
| **Formato de fecha**       | Formato y valores de fecha.<br>Por defecto, puedes seleccionar un formato de fecha en el menú desplegable que corresponda al formato de tu archivo CSV. Para [personalizar un formato de fecha](#formato-de-fecha-personalizado), haz clic en el {% icon gear %} e introduce tu formato en el campo de texto. |               Sí                |               Sí               |
| **Hora**       | Formato y valores de hora.                                                                                                                                                                                                                          |               Sí                |               Sí               |
| **Marca de tiempo**  | Valores de marca de tiempo con un [formato personalizado de marca de tiempo](#formato-personalizado-de-marca-de-tiempo-con-fecha-y-hora).<br>Esta columna aparece si activas **Fecha y hora en una columna**.                                                                              |               Sí                |               Sí               |
| **Entrantes**    | Contactos entrantes (por intervalo para datos basados en intervalos).<br>Acepta números enteros y decimales con punto.                                                                                                                                            |               Sí                |               Sí               |
| **Atendidos**    | Contactos atendidos (por intervalo para datos basados en intervalos).<br>Acepta números enteros y decimales con punto.<br>Para datos basados en contactos, el valor para los contactos respondidos solo puede ser 0 o 1 (o decimales).                                              |               Sí                |               Sí               |
| **TMO**        | Tiempo medio de operación en el intervalo.<br> Formatos aceptados: segundos (números enteros) o hh:mm:ss (p.&nbsp;ej., 00:05:00).<br>Si no hay columna TMO, selecciona **Sin columna**.<br>Este campo solo está disponible para datos basados en intervalos.                           |                No                |               No                |
| **Duración**   | Duración del registro en segundos (número entero).<br>Este campo solo aparece para datos basados en contactos.                                                                                                                                                                        |                No                |               Sí               |
| **Canal**    | Nombre fijo del canal (primer menú desplegable) o columna seleccionable que contiene el nombre del canal (segundo menú desplegable).<br>Valores aceptados: calls, emails, chats, documents, cases, social_media.                                                           |               Sí                |               Sí               |

#### Desplegables para estados de los agentes

Si has seleccionado **Estados de los agentes** como tipo de datos a importar, la página de asignación muestra los siguientes elementos:

| Campo                   | Descripción                                                                                                                                                                                                                                                                          | Obligatorio |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| **Identificador de agente**    | Identificador único para el agente, p.&nbsp;ej., DNI o nombre.                                                                                                                                                                                                                                     | Sí      |
| **Identificador de actividad** | Actividad que el agente lleva a cabo.                                                                                                                                                                                                                                                     | Sí      |
| **Fecha de inicio**          | Fecha en la que el agente inició la actividad.<br>Por defecto, puedes seleccionar un formato en el menú desplegable que corresponda al formato de tu archivo CSV. Para [personalizar un formato de fecha](#formato-de-fecha-personalizado), haz clic en el {% icon gear %} e introduce tu formato en el campo de texto.   | Sí      |
| **Hora de inicio**          | Hora a la que el agente inició la actividad.                                                                                                                                                                                                                                         | Sí      |
| **Marca de tiempo de inicio**     | [Formato personalizado de marca de tiempo](#formato-personalizado-de-marca-de-tiempo-con-fecha-y-hora) que incluye la fecha y hora a las que el agente inició la actividad.<br>Esta columna aparece si activas **Fecha y hora en una columna**.                                                                 | Sí      |
| **Fecha de finalización**            | Fecha en la que el agente finalizó la actividad.<br>Por defecto, puedes seleccionar un formato de fecha en el menú desplegable que corresponda al formato de tu archivo CSV. Para [personalizar un formato de fecha](#formato-de-fecha-personalizado), haz clic en el {% icon gear %} e introduce tu formato en el campo de texto. | No       |
| **Hora de finalización**            | Hora a la que el agente finalizó la actividad.                                                                                                                                                                                                                                         | No       |
| **Marca de tiempo de finalización**       | [Formato personalizado de marca de tiempo](#formato-personalizado-de-marca-de-tiempo-con-fecha-y-hora) que incluye la fecha y hora a las que el agente interrumpió la actividad.<br>Esta columna aparece si activas **Fecha y hora en una columna**.                                                                 | No       |

#### Formato de fecha personalizado

Puedes configurar un formato de fecha personalizado que corresponda al formato de tu archivo CSV. Añade los siguientes caracteres en el campo **Formato de fecha personalizado**:

- Para el día: **D** (cifra única del 1 al 9) o **DD** (para cifra precedida de 0)
- Para el mes: **M** (cifra única del 1 al 9) o **MM** (para cifra precedida de 0)
- Para el año: **YY**o **YYYY**

Los demás caracteres se interpretan como separadores.

Ejemplos:

| Fecha     | Formato de fecha personalizado |
| -------- | ------------------ |
| 13/1,22  | D/M,YY             |
| 010122   | DDMMYY             |
| 13012022 | DDMMYYYY           |

#### Formato personalizado de marca de tiempo con fecha y hora

Para añadir un formato personalizado de marca de tiempo, activa la opción **Fecha y hora en una columna**.
Además del [formato de fecha personalizado](#formato-de-fecha-personalizado), debes configurar el formato de hora con minúsculas:

- Para la hora: **h** (cifra única del 1 al 9) o **hh** (para cifra precedida de 0)
- Para los minutos: **m** (cifra única del 1 al 9) o **mm** (para cifra precedida de 0)
- (Opcional) Para los segundos: **s** (cifra única del 1 al 9) o **ss** (para cifra precedida de 0)

Ejemplos:

| Fecha y hora  | Formato de marca de tiempo |
| -------------- | ---------------- |
| 13/1,22 9:15:8 | D/M,YY h:m:s     |
| 010122 09-15   | DDMMYY hh-mm     |

### Asignar las columnas (consulta SQL)

Para la mayoría de los archivos CSV puedes utilizar la asignación predeterminada mediante los menús desplegables. Si tu sistema externo genera archivos CSV que no contienen ciertas columnas requeridas para la asignación predeterminada (p.&nbsp;ej., si requieren cálculos adicionales) o si contienen formatos no compatibles, puede ser que el [método de asignación predeterminado](#asignar-las-columnas) no sea el adecuado para ti. En este caso, puedes usar una solicitud SQL (SQLite) para asignar las columnas. Esto te permite convertir valores totales en promedios, o calcular un volumen de llamadas a partir de varias columnas, entre otras opciones. Este método de asignación solo está disponible para datos de contacto. No se puede utilizar para datos de los estados de los agentes.

#### Requisitos

Ten en cuenta los siguientes requisitos a la hora de escribir una consulta SQL para la asignación de columnas:

- Usa `uploaded_file` como nombre de la tabla.
- Usa minúsculas para los nombres de las columnas.
- Usa el tipo de datos datetime para la columna timestamp (en formato `YYYY-MM-DD hh:mm:ss`).
- Utiliza la sintaxis de consulta de [SQLite](https://www.sqlite.org).

La consulta SQL de [SQLite](https://www.sqlite.org) admite operaciones matemáticas, conversiones de datos y alias de columnas (para asignar diferentes nombres de columna). Puede leer más sobre las limitaciones con respecto a los siguientes elementos en sqlite.org:

- [precisión numérica](https://www.sqlite.org/datatype3.html)
- [funciones matemáticas](https://www.sqlite.org/lang_mathfunc.html)
- [conversiones de datos implícitas](https://www.sqlite.org/datatype3.html#affinity)
- [funciones de fecha y hora](https://www.sqlite.org/lang_datefunc.html)
- [manipulación de cadenas](https://www.sqlite.org/lang_corefunc.html#string_functions)

Para asignar las columnas mediante una consulta SQL, sigue estos pasos:

> Cambiar el método de asignación sobrescribirá el esquema CSV existente
>
> Si ya has creado un esquema CSV, cambiar el método de asignación y guardar el nuevo esquema sobrescribirá el anterior. No se puede restaurar un esquema de CSV una vez que ha sido sobrescrito.

1. Activa el interruptor **Usar una consulta SQL para asignar las columnas** en la parte superior derecha de la página de asignación de columnas.
2. Introduce una consulta SQL (SQLite) en el campo de texto. Sugerencia: copia y pega las siguientes consultas de muestra según las necesites.

Si quieres subir datos de contacto basados tanto en intervalos como en contactos, necesitas crear una integración y escribir una consulta SQL para cada tipo de datos.

### Columnas requeridas en la consulta SQL

La siguiente tabla ofrece un resumen de las columnas requeridas en la consulta SQL:

> Dependiendo de tu [plan de WFM](https://www.injixo.com/pricing/), puede ser que no todos los canales de la cola de origen de injixo estén disponibles para ti.

| Nombre de la columna | Tipo de datos | Requerido | Detalles                                                                                                                                                                                                  |
| ----------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| queue       | Cadena    | Sí      | Identificador para la cola                                                                                                                                                                                 |
| timestamp   | Datetime  | Sí      | Inicio del intervalo en formato YYYY-MM-DD hh:mm:ss                                                                                                                                                  |
| offered     | Número entero   | Sí      | Número de contactos (como llamadas o correos) en el intervalo                                                                                                                                                 |
| answered    | Número entero   | Sí      | Basado en intervalos: número de contactos gestionados en el intervalo<br>Basado en contactos: el valor 1 indica que se ha gestionado el contacto. El valor 0 indica que no se ha gestionado el contacto. |
| aht         | Float     | No       | Tiempo medio de operación de todos los contactos en el intervalo                                                                                                                                                   |
| duration    | Número entero   | Sí      | Tiempo total de operación de un contacto concreto                                                                                                                                                                  |
| channel     | Cadena    | Sí      | Identificador del canal de la cola origen de injixo<br>Valores aceptados: calls, chats, emails, social_media, documents, cases                                                                            |

#### Consultas de muestra básicas

Datos de contacto basados en intervalos:

```sql
SELECT
   queue, timestamp,
   offered, handled, aht,
   channel
FROM uploaded_file
```

Datos de contacto basados en intervalos:

```sql
SELECT
   queue, timestamp,
   offered, handled, duration,
   channel
FROM uploaded_file
```

Los siguientes ejemplos avanzados muestran cómo aplicar operaciones matemáticas y funciones de SQLite.

#### Consulta de muestra avanzada 1

- Divide HandleTime por HandledCalls para obtener el tiempo medio de operación (TMO) requerido.
- Combina Date y Time usando SUBSTR para obtener el formato de marca de tiempo requerido YYYYY-MM-DD HH:MM:SS.

|   Queue    |    Date    | Time  | Received | HandledCalls | Aband | HandleTime | HoldTime |
| :--------: | :--------: | :---: | :------: | :----------: | :---: | :--------: | :------: |
| test queue | 06/03/2023 | 07:30 |    5     |      5       |   -   |   1324.6   |    -     |
| test queue | 06/03/2023 | 08:00 |    2     |      2       |   -   |    1548    |    -     |

```
SELECT
  Queue as queue,
  SUBSTR(Date, 7, 4) || '-'|| SUBSTR(Date, 1, 2) || '-' || SUBSTR(Date, 4,2) || ' ' || Time || ':00' as timestamp,
  Received as offered,
  HandledCalls as handled,
  HandleTime/HandledCalls as aht,
  'chats' as channel
FROM uploaded_file
```

#### Consulta de muestra avanzada 2

- Usa el `date('now')` de SQLite para obtener la fecha actual y combínala con la hora del archivo.
- Elimina los decimales y conviértelos en números enteros.
- Combina Date y Time usando SUBSTR para obtener el formato de marca de tiempo requerido YYYYY-MM-DD HH:MM:SS.

En este ejemplo, los encabezados de columna contienen caracteres en blanco. 

| Queue Name | Hour in hh:mm | Offered Calls | Handled Calls | Average Handling Time       |
| :--------: | :-----------: | :-----------: | :-----------: | :-------------------------: |
| demo queue |     07:00     |      3.4      |      2.9      |          00:05:30           |
| demo queue |     08:30     |      5.7      |      5.2      |          00:10:15           |

Puedes reemplazar la fila de encabezado utilizando las opciones de preprocesamiento de la integración:

- Omitir la(s) primera(s) 1 fila(s): elimina el encabezado original.
- Añadir fila de encabezado: añade encabezados de columna con letras

```
 SELECT
   A as queue,
   DATE('now')||' '|| "B"||':00' as timestamp,
   FLOOR(C) as offered,
   FLOOR (D) as handled,
   (CAST(substr(E, 1, 1) AS INTEGER) * 3600) +
   (CAST(substr(E, 3, 2) AS INTEGER) * 60) +
   CAST(substr(E, 6, 2) AS INTEGER) as aht,
   'calls' as channel
FROM uploaded_file
```

Si no reemplazas la fila de encabezado, usa comillas dobles para referirte a los nombres de columna reales: 

```
 SELECT
   "Queue Name" as queue,
   DATE('now')||' '|| "Hour in hh:mm"||':00' as timestamp,
   FLOOR("Offered Calls") as offered,
   FLOOR ("Handled Calls") as handled,
   (CAST(substr("Average Handling Time", 1, 1) AS INTEGER) * 3600) +
   (CAST(substr("Average Handling Time", 3, 2) AS INTEGER) * 60) +
   CAST(substr("Average Handling Time", 6, 2) AS INTEGER) as aht,
   'calls' as channel
FROM uploaded_file
```

#### Consulta de muestra avanzada 3

- Resta AbandonedCalls a OfferedCalls para obtener las llamadas atendidas.
- Transforma la cadena de inicio con formato especial en el formato de marca de tiempo requerido YYYY-MM-DD HH:MM:SS.

|  Name  |       Start       | OfferedCalls | AbandonedCalls | AverageHandlingTime |
| :----: | :---------------: | :----------: | :------------: | :-----------------: |
| queue1 | 20230613 15:30:00 |      10      |       2        |         300         |
| queue2 | 20230613 15:35:00 |      15      |       3        |         450         |
| queue3 | 20230613 15:40:00 |      12      |       2        |         350         |

<!-- notes for database integrations -->
<!-- In this example, the date time format in the Start column is not supported by built-in SQLite `datetime()` and `strftime()` functions. You need to change the string first. -->
<!-- changed the example from datetime(substr(Start, 1, 4) || '-' || to substr(Start, 1, 4) || '-' || -->
<!-- `datetime` is not required here, but in database integrations it would be needed due to the reqiured datetime datatype in the table around line 210 -->

```
SELECT
  Name as queue,
    substr(Start, 1, 4) || '-' ||
    substr(Start, 5, 2) || '-' ||
    substr(Start, 7, 2) || ' ' ||
    substr(Start, 10, 8) as timestamp,
  Offered as offered,
  (Offered - Abandoned) as handled,
  AverageHandlingTime as aht,
  'calls' as channel
FROM uploaded_file
```

<!-- do not change the heading, used in the integrations UI -->

## Editar un esquema CSV

Cuando cambia la estructura del archivo CSV, tienes que modificar el el esquema CSV de la integración.

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Haz clic en el {% icon pencil %} junto a la integración que quieras modificar.
3. Haz clic en _Editar el esquema CSV_{:.doc-button}.
   Puedes modificar las opciones en la sección **Configuración**. Para modificar las opciones de preprocesamiento, haz clic en _Volver a cargar el fichero_{:.doc-button} y carga un archivo CSV modificado o el original.
4. Haz clic en _Asignar las columnas_{:.doc-button}. Si es necesario, puedes modificar cómo se asignan las columnas.
5. Haz clic en _Guardar esquema_{:.doc-button}.

> La disposición de los datos no puede ser modificada
>
> Cuando editas un esquema CSV no puedes modificar la disposición de los datos configurada anteriormente (basados en contactos o basados en intervalos).

## Ejemplos de asignación de columnas

En esta sección encontrarás ejemplos de archivos CSV y las asignaciones correspondientes. Puedes usar estos ejemplos como plantillas para tus propios archivos CSV.

### Datos de contacto (basados en intervalos)

Archivo CSV

```

Queue;Date;Time;IncomingCalls;AnsweredCalls;AHT
My Inbound Queue;25/05/2020;08:00;15;14;230
My Inbound Queue;25/05/2020;08:15;16;15;210
My Inbound Queue;25/05/2020;08:30;20;18;235
My Inbound Queue;25/05/2020;08:45;18;15;215

```

<!-- left-align all tables -->
<style>
table {
   margin-left: 0px;
}
</style>

Asignación de columnas

| Columna      | Columna asignada/valor |
| ----------- | ------------------- |
| Nombre de la cola  | Queue               |
| Date        | Date                |
| Formato de fecha | dd/mm/yyyy          |
| Time        | Time                |
| Formato de hora |    hh:mm           |
| Offered     | IncomingCalls       |
| Atendidos     | AnsweredCalls       |
| AHT         | AHT                 |
| Formato de TMO  | Seconds             |

Este ejemplo no incluye columna para el canal. En la configuración del esquema CSV, selecciona la opción **Canal**. Para configurar el canal para, p.&nbsp;ej., llamadas, selecciona **Llamadas** en el menú desplegable.

### Datos de contacto (basados en contactos)

Archivo CSV

```

Queue;Date;Time;Offered;Answered;Duration
My Inbound Queue;25/05/2020;08:00;1;1;100
My Inbound Queue;25/05/2020;08:03;1;0;0
My Inbound Queue;25/05/2020;08:04;1;1;120
My Inbound Queue;25/05/2020;08:07;1;0;0

```

Asignación de columnas

| Columna      | Columna asignada/valor |
| ----------- | ------------------- |
| Nombre de la cola  | Queue               |
| Fecha        | Date                |
| Formato de fecha | dd/mm/yyyy          |
| Hora        | Time                |
| Formato de hora | hh:mm               |
| Entrantes     | Offered             |
| Atendidos    | Answered            |
| Duración    | Duration            |

Este ejemplo no incluye columna para el canal. En la configuración del esquema CSV, selecciona la opción **Canal**. Para configurar el canal para, p.&nbsp;ej., llamadas, selecciona **Llamadas** en el menú desplegable.

### Estados de los agentes

Archivo CSV

```

StartDate;StartTime;AgentID;AgentActivityID
2022-04-22;08:34:29;816;1013;
2022-04-22;08:34:42;816;1015;
2022-04-22;08:34:48;816;1015;
2022-04-22;08:39:11;816;1015;

```

Asignación de columnas

| Columna              | Columna asignada/valor |
| ------------------- | ------------------- |
| Identificador de agente    | AgentID             |
| Identificador de actividad | AgentActivityID     |
| Fecha de inicio          | StartDate           |
| Formato de fecha         | yyyy-mm-dd          |
| Hora de inicio          | StartTime           |
| Formato de hora         | hh:mm:ss            |

## Importar archivos CSV

Una vez hayas guardado tu integración de archivos CSV, puedes empezar a importar archivos CSV.
injixo acepta los siguientes formatos de codificación de archivos:

- UTF-8
- ISO-8859-1/Latin-1
- ISO-8859-9
- Windows-1252

Usa UTF-8 para evitar mensajes de error genéricos.

### Importación automática de archivos

[Configura una integración de archivos CSV](#configurar-una-nueva-integración-de-archivos-csv) y conecta injixo Cloud Link. injixo Cloud Link subirá nuevos datos a injixo. Por defecto, cada vez que guardas un nuevo archivo CSV en la carpeta de instalación de injixo Cloud Link, comienza una nueva importación. El directorio por defecto es C:\\Program Files\\injixo Cloud Link, pero puedes modificarlo durante la instalación de injixo Cloud Link. 

También puedes configurar una {% link_new carpeta de importación | features/acd-integration/cloud/install-cloud-link.md | #configurar-la-carpeta-de-importaciones %} específicamente para subir archivos. En ese caso, guarda los archivos nuevos en la carpeta de importación.

Una vez los datos hayan sido importados, podrás {% link_new añadir nuevas colas a una carga de trabajo | features/forecast/injixo-forecast/manage-workloads.md %} en Forecast, o verás datos actualizados en tus cargas de trabajo existentes. Si los datos no son importados, usa la importación manual de archivos descrita a continuación para verificar si el formato de tu archivo es válido.

### Importación manual de archivos

Puedes importar datos a injixo manualmente usando una página web.

Una vez hayas [configurado la integración de archivos CSV](#configurar-una-nueva-integración-de-archivos-csv), podrás importar datos manualmente (puedes saltarte la instalación de injixo Cloud Link).

1. Ve a [https://www.injixo.com/csv-importer](https://www.injixo.com/csv-importer).
2. Haz clic en **abre el explorador de archivos** y selecciona un archivo CSV para importarlo (o arrástralo al navegador).
3. En el menú desplegable abajo a la izquierda, selecciona tu integración de archivos CSV.
4. Haz clic en _Importar fichero_{:.doc-button}.
   El formato del archivo debe coincidir con el esquema CSV.
5. Para importar los datos, haz clic en _Aplicar datos_{:.doc-button}.

Una vez tus datos hayan sido procesados, podrás {% link_new añadir colas a una carga de trabajo | features/forecast/injixo-forecast/manage-workloads.md %} en injixo Forecast. El archivo no puede exceder los 7 MB.

## Preguntas frecuentes

| Pregunta                                                                  | Respuesta                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ¿Puedo importar dos veces el mismo archivo?                                         | Sí, si importas los datos manualmente. No, si usas injixo Cloud Link.<br>Para eliminar archivos duplicados, injixo calcula sumas de comprobación durante la importación. Los archivos importados con la misma suma de comprobación no volverán a ser importados. Si el archivo tiene el mismo nombre, pero distinto contenido, será importado. |
| ¿Borra injixo los archivos CSV importados automáticamente tras la importación? | No. Los archivos importados se guardan en la carpeta del cliente injixo Cloud Link. Puedes borrarlos manualmente o configurar un borrado regular.                                                                                                                                              |
| ¿Puedo importar un archivo CSV que incluya datos futuros?                        | Sí, es posible. Sin embargo, ten en cuenta que injixo no ignorará los datos futuros, sino que los almacenará como datos históricos. Esto no impide calcular una previsión, pero los gráficos históricos y de previsión se solaparán.                                               |
