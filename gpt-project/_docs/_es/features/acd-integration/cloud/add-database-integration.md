---
title: Añadir una integración de base de datos
navigation_title: Database
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Conecta tu base de datos a injixo para importar datos
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/how-integrations-work.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/install-cloud-link.md
  - overwrite_title: Add title for untranslated source
    filepath: features/acd-integration/cloud/import-agent-status-data.md
---

¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.

## Qué es una integración de base de datos

Una integración de base de datos es un tipo especial de integración on-premise. Usa una integración de base de datos si tu sistema no se puede conectar a una integración cloud o a las otras integraciones on-premise.

Puedes definir una consulta SQL para leer la información en la base de datos. Las integraciones de base de datos usan {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.

## Añadir una integración de base de datos

1. Ve a _Account > Integraciones_{:.breadcrumbs}.
2. Si ya existe una integración, haz clic en _Añadir integración_{:.doc-button}.
3. En la sección **Universal Interfaces**, haz clic en _Selecciona el modelo_{:.doc-button}.
4. En la sección **Base de datos**, haz clic en _Añadir integración_{:.doc-button}.

## Configurar una integración de base de datos

1. Introduce un nombre inequívoco para la nueva integración que identifique el origen de los datos.
2. Instala y conecta {% link_new injixo Cloud Link | features/acd-integration/cloud/install-cloud-link.md %}.
3. Selecciona tu **tipo de base de datos**.
4. Introduce las credenciales requeridas, que dependerán de tu selección.

   | Tipo de base de datos                                  | Credenciales                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | MS SQL Server<br>MySQL<br>PostgreSQL | **Nombre de la base de datos**<br>**Host**<br>**Puerto**: si usas una instancia nombrada en la conexión con MS SQL Server, no introduzcas el puerto. En su lugar, abre el puerto UDP 1434 en tu cortafuegos para asegurarte de que el servicio SQL Server Browser puede determinar el puerto para injixo Cloud Link.<br>**Usuario**<br>**Contraseña**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | Otros (ODBC)                                   | **Cadena de conexión**: la cadena de conexión contiene los parámetros que la integración necesita para conectarse al servidor de tu base de datos. Consulta [//www.connectionstrings.com](https://www.connectionstrings.com) para encontrar una cadena de conexión apropiada para tu tipo de base de datos y de driver ODBC.<br><br>Ejemplos para una base de datos InterSystem Caché:<br>`DRIVER={InterSystemsODBC};SERVER=myServerAddress;` `PORT=12345;DATABASE=myDataBase;UID=myUsername;PWD=myPassword;` <br><br>El identificador SQL en consultas debe estar delimitado por comillas altas. Añade opciones adicionales a la cadena de conexión si tu driver ODBC no lo soporta de forma predefinida, p. ej., para Informix.<br><br>Ejemplo para una base de datos IBM Informix:<br>`DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=myServerAddress;DATABASE=myDatabase;HOST=myHost;SERVICE=myService;UID=myUsername;PWD=myPassword;PROTOCOL=onsoctcp;DELIMIDENT=y;`<br><br>También puedes crear una fuente de datos ODBC en la que configures el controlador, el servidor, la base de datos, etc. Esto te permite añadir la opción DSN que ves a continuación como cadena de conexión en lugar de incluir los detalles de conexión en la cadena de conexión. Adicionalmente tendrás que añadir las opciones que no se pueden configurar en la fuente de datos ODBC, p.&nbsp;ej., `DELIMIDENT=y`.<br><br>Ejemplos de DSN:<br> `DSN=myODBCDatasourceName;`<br>`DSN=myODBCDatasourceName;DELIMIDENT=y;` |

## Configurar los datos de la importación

1. En la sección **Configuración**, selecciona el tipo de datos que quieres importar de tu base de datos:
   - **En base a contactos** para datos históricos de contacto con una fila por contacto.
   - **En base a intervalos** para datos históricos de contacto agrupados en intervalos.
   - **Estados de los agentes** para datos sobre los estados de los agentes.  
    Por defecto, los datos se importan cada 15 minutos. Puedes controlar la importación con dos casillas adicionales:
        - **Importar datos en tiempo real**: los datos se importan cada 10 segundos. Disponible solamente en injixo Advanced e injixo Enterprise WFM.
        - **Reconciliación de datos**: define el período de tiempo para el cual se importan datos sobre los estados de los agentes cada 15 minutos. La opción predefinida considera los datos de las últimas 24 horas (es la opción recomendada).  

2. Selecciona la **zona horaria de la base de datos** en el menú desplegable.
3. Introduce la **consulta SQL** que se usará para importar información de tu base de datos. Aprende más sobre la [consulta SQL](#consulta-sql).
4. Para crear la integración, haz clic en _Guardar integración_{:.doc-button}.  
   La integración empezará a importar datos a injixo. La importación inicial puede tardar cierto tiempo.  
   Todas las colas importadas de la base de datos conectada estarán automáticamente disponibles en la {% link_new página de configuración de las cargas de trabajo | features/forecast/injixo-forecast/manage-workloads.md | #crear-cargas-de-trabajo %} en injixo Forecast.  
   Las actividades externas estarán disponibles en la actividad Presente (ID 1). Para importar datos de los estados de los agentes, tienes que {% link_new asignar los identificadores externos de usuario a las actividades | features/acd-integration/cloud/import-agent-status-data.md %}.

### Reconciliación de datos

En ocasiones, será necesario corregir manualmente datos de los estados de los agentes ya importados. Por ejemplo, si un empleado olvidó registrar su hora de salida y corriges los datos en la base de datos para reflejar correctamente las horas trabajadas.

La casilla **Reconciliación de datos** está marcada por defecto. injixo reimportará todos los datos

- de las últimas 24 horas
- cada 15 minutos.

De este modo, siempre tendrás acceso a la versión más actualizada de los datos de las últimas 24 horas. Las modificaciones de datos más antiguos que 24 horas no se incluirán en la reimportación.

Tu base de datos puede tener dificultades con la reimportación continua de datos. Si necesitas desactivar la reconciliación de datos, injixo solo importará los datos más recientes desde la última importación exitosa (por norma general, los datos de los últimos 15 minutos). En este caso, puede que tengas que actualizar manualmente en injixo los datos importados hace más de 15 minutos. Mantén la casilla marcada siempre que sea posible, puesto que las actualizaciones manuales requieren un significante esfuerzo adicional y son propensas a errores.

Si suspendes tu integración durante menos de 24 horas, injixo reimporta todos los datos en cuanto reanudes la integración. Esto ocurre independientemente de si la casilla está marcada o desmarcada.  
Si suspendes la integración durante un período de tiempo superior a 24 horas, no se reimportarán los datos más antiguos de 24 horas.

## Consulta SQL

La consulta SQL para una integración de base de datos debe contener nombres de columna específicos. El tipo de datos seleccionado para la importación determina qué columnas son necesarias. Puedes definir el nombre de la tabla. A continuación tienes las consultas SQL más simples que puedes ejecutar:

<style>
table th:first-of-type {
   width: 20%;
}
table th:nth-of-type(4) {
   width: 50%;
}
</style>

| Tipo de datos a importar | Ejemplo de consulta                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------- |
| En base a intervalos   | SELECT queueidentifier, queuename, timestamp, offered, answered, handlingtime, channel FROM testTable |
| En base a contactos    | SELECT queueidentifier, queuename, timestamp, answered, duration, channel FROM testTable              |
| Estados de los agentes     | SELECT agentidentifier, starttime, endtime, activity FROM testTable                                   |

> Atención 
> 
> En la mayoría de los casos, tu base de datos no coincidirá con los nombres de columna esperados. Para solucionarlo, usa los nombres de columna requeridos como alias de columna o crea una vista en tu base de datos.

Amplía las consultas de muestra para obtener y filtrar datos de tu tabla personalizada:

```
SELECT
  Start as "timestamp",
  Id as queueidentifier,
  Name as queuename,
  SUM(CASE countId WHEN 1000 THEN val ELSE 0 END) as offered,
  SUM(CASE countId WHEN 1001 THEN val ELSE 0 END) as answered,
  SUM(CASE countId WHEN 1002 THEN val ELSE 0 END) as handlingtime,
  calls as channel
FROM table
WHERE countId IN (1000, 1001, 1002)
GROUP BY Start, Name
```

## Detalles de las columnas

Las tablas a continuación muestran los detalles de las columnas esperadas organizadas por tipo de importación.

### Estados de los agentes

<style>

table {
   width: 100%;
}  
table th:first-of-type {
   width: 20%;
}
table th:nth-of-type(4) {
   width: 50%;
}
</style>

| Columna                    | Tipo de datos | Requerido | Detalles                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| agentidentifier           | Cadena    | Sí      | Identificador único para el agente                                                                                                                                          |
| starttime                 | Datetime  | Sí      | Inicio de la actividad del estado del agente                                                                                                                                       |
| endtime                   | Datetime  | No       | Fin de la actividad del estado del agente<br>No usar si la actividad está en proceso.                                                                                               |
| activity                  | Cadena    | Sí      | Identificador de la actividad externa                                                                                                                                     |

### En base a intervalos

| Columna                    | Tipo de datos | Requerido | Detalles                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| queueidentifier           | Cadena    | Sí      | Identificador único para la cola<br>Puedes renombrar la cola modificando el queuename, pero mantendrá el mismo queueidentifier.                                        |
| queuename                 | Cadena    | Sí      | Identificador para la cola                                                                                                                                                 |
| timestamp                 | Datetime  | Sí      | Inicio del intervalo                                                                                                                                                    |
| offered                   | Número entero   | Sí      | Número de contactos (p.&nbsp;ej., llamadas o correos) en el intervalo                                                                                                                 |
| answered                  | Número entero   | Sí      | Número de contactos gestionados en el intervalo                                                                                                                |
| handlingtime              | Número entero   | Sí      | Tiempo total de operación para todos los contactos en el intervalo                                                                                                                       |
| channel                   | Cadena    | No       | Identificador para el canal de la cola origen de injixo<br>Si está vacío, el valor por defecto será calls<br>Valores válidos: calls, chats, emails, social_media, documents, cases. |

### En base a contactos

| Columna                    | Tipo de datos | Requerido | Detalles                                                                                                                                                                  |
| ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| queueidentifier           | Cadena    | Sí      | Identificador inequívoco para la cola<br>Puedes renombrar la cola modificando el queuename, pero mantendrá el mismo queueidentifier.                                        |
| queuename                 | Cadena    | Sí      | Identificador para la cola                                                                                                                                                 |
| timestamp                 | Datetime  | Sí      | Inicio del intervalo                                                                                                                                                    |
| offered                   | Número entero   | Sí      | Contacto ofrecido (valor 1)<br>Ningún contacto ofrecido (valor 0)                                                                                                                |
| answered                  | Número entero   | Sí      | Contacto gestionado (valor 1)<br>Ningún contacto gestionado (valor 0)                                                                                                                |
| duration                  | Número entero   | Sí      | Tiempo total de operación para un contacto concreto                                                                                                                                    |
| channel                   | Cadena    | No       | Identificador para el canal de la cola origen de injixo<br>Si está vacío, el valor por defecto será calls<br>Valores válidos: calls, chats, emails, social_media, documents, cases. |

## Editar una integración de base de datos

Si los detalles o la estructura de los datos de tu base de datos cambian, puedes editar la configuración de la integración. La importación sucesiva de datos se realizará como previamente. Si necesitas volver a importar todos los datos disponibles del pasado, crea una nueva integración.

## Problemas conocidos con el controlador ODBC

Para evitar aumentar las conexiones TCP en Cloud Link al consultar datos de Amazon Athena, asegúrate de usar [el controlador ODBC 2.x de Amazon Athena](https://docs.aws.amazon.com/es_es/athena/latest/ug/odbc-v2-driver.html).
