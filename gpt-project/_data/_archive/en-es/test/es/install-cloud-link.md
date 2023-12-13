EN,DE,File
---,---,install-cloud-link.md
title: Instalar injixo Cloud Link,title: Instalar injixo Cloud Link,install-cloud-link.md
product_label:,product_label:,install-cloud-link.md
- essential,- essential,install-cloud-link.md
- advanced,- advanced,install-cloud-link.md
- enterprise,- enterprise,install-cloud-link.md
- classic,- classic,install-cloud-link.md
description: Instala el cliente de injixo Cloud Link para importar datos a injixo.,description: Instala el cliente de injixo Cloud Link para importar datos a injixo.,install-cloud-link.md
related_articles:,related_articles:,install-cloud-link.md
- overwrite_title: Add title for untranslated source,- overwrite_title: Add title for untranslated source,install-cloud-link.md
filepath: features/acd-integration/cloud/how-integrations-work.md,filepath: features/acd-integration/cloud/how-integrations-work.md,install-cloud-link.md
- overwrite_title: Importar datos sobre los estados de los agentes,- overwrite_title: Importar datos sobre los estados de los agentes,install-cloud-link.md
filepath: features/acd-integration/cloud/import-agent-status-data.md,filepath: features/acd-integration/cloud/import-agent-status-data.md,install-cloud-link.md
---,---,install-cloud-link.md
¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.,¿Las integraciones son nuevas para ti? Consulta primero {% link_new la información básica | features/acd-integration/cloud/how-integrations-work.md %}.,install-cloud-link.md
## Qué es injixo Cloud Link,## Qué es injixo Cloud Link,install-cloud-link.md
injixo Cloud Link es un cliente de software que necesitas instalar para configurar una integración on-premise. injixo Cloud Link importa datos a injixo con regularidad. También puedes instalar injixo Cloud Link cuando configures integraciones de CSV para importar regularmente nuevos archivos CSV de una carpeta.,injixo Cloud Link es un cliente de software que necesitas instalar para configurar una integración on-premise. injixo Cloud Link importa datos a injixo con regularidad. También puedes instalar injixo Cloud Link cuando configures integraciones de CSV para importar regularmente nuevos archivos CSV de una carpeta.,install-cloud-link.md
El directorio de instalación del cliente contiene:,El directorio de instalación del cliente contiene:,install-cloud-link.md
- el archivo ejecutable injixo-cloud-link;,- el archivo ejecutable injixo-cloud-link;,install-cloud-link.md
- uno o varios archivos injixo-cloud-link.*.log;,- uno o varios archivos injixo-cloud-link.*.log;,install-cloud-link.md
- el archivo de configuración injixo-cloud-link.toml;,- el archivo de configuración injixo-cloud-link.toml;,install-cloud-link.md
- una carpeta de licencias con licencias para bibliotecas de código abierto (open source).,- una carpeta de licencias con licencias para bibliotecas de código abierto (open source).,install-cloud-link.md
## Prerrequisitos,## Prerrequisitos,install-cloud-link.md
- Windows: injixo Cloud Link es compatible con Windows 10 y superior y con Windows Server 2016 y superior. <!-- what about Linux -->,- Windows: injixo Cloud Link es compatible con Windows 10 y superior y con Windows Server 2016 y superior. <!-- what about Linux -->,install-cloud-link.md
- Linux: el paquete unixODBC tiene que estar instalado.,- Linux: el paquete unixODBC tiene que estar instalado.,install-cloud-link.md
- Cortafuegos/proxy: el puerto 443 tiene que estar abierto para tráfico saliente. injixo Cloud Link usa encriptación TLS con TCP a través del puerto 443.,- Cortafuegos/proxy: el puerto 443 tiene que estar abierto para tráfico saliente. injixo Cloud Link usa encriptación TLS con TCP a través del puerto 443.,install-cloud-link.md
"Atención: las integraciones on-premise acceden a un sistema local, como un ACD o CRM, para extraer datos. Según el tipo de base de datos, tendrás que instalar un controlador (driver) de base de datos.","Atención: las integraciones on-premise acceden a un sistema local, como un ACD o CRM, para extraer datos. Según el tipo de base de datos, tendrás que instalar un controlador (driver) de base de datos.",install-cloud-link.md
## Instalar injixo Cloud Link,## Instalar injixo Cloud Link,install-cloud-link.md
"Cuando añades una {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %} o una {% link_new integración de CSV | features/acd-integration/cloud/add-csv-integration.md %}, en la sección **injixo Cloud Link** encontrarás enlaces para descargar el instalador del cliente (para Windows) o los archivos del cliente (para Linux).","Cuando añades una {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %} o una {% link_new integración de CSV | features/acd-integration/cloud/add-csv-integration.md %}, en la sección **injixo Cloud Link** encontrarás enlaces para descargar el instalador del cliente (para Windows) o los archivos del cliente (para Linux).",install-cloud-link.md
### Instalación del servicio de Windows,### Instalación del servicio de Windows,install-cloud-link.md
Instala el primer servicio con el instalador del cliente de Windows:,Instala el primer servicio con el instalador del cliente de Windows:,install-cloud-link.md
1. Haz clic en **Descargar para Windows 64-bit** y ejecuta el archivo.,1. Haz clic en **Descargar para Windows 64-bit** y ejecuta el archivo.,install-cloud-link.md
2. Haz clic en **Next**.,2. Haz clic en **Next**.,install-cloud-link.md
3. (Opcional) Modifica el directorio de instalación.,3. (Opcional) Modifica el directorio de instalación.,install-cloud-link.md
4. Haz clic en **Next** y después en **Install**.,4. Haz clic en **Next** y después en **Install**.,install-cloud-link.md
Una ventana de la consola te muestra un PIN que es válido durante cinco minutos.,Una ventana de la consola te muestra un PIN que es válido durante cinco minutos.,install-cloud-link.md
"Para [conectar injixo Cloud Link a tu integración](#conectar-injixo-cloud-link-a-tu-integración), sigue las instrucciones de la consola.","Para [conectar injixo Cloud Link a tu integración](#conectar-injixo-cloud-link-a-tu-integración), sigue las instrucciones de la consola.",install-cloud-link.md
5. Haz clic en **Finish** en el instalador.,5. Haz clic en **Finish** en el instalador.,install-cloud-link.md
El instalador crea el servicio de Windows **injixo Cloud Link**.,El instalador crea el servicio de Windows **injixo Cloud Link**.,install-cloud-link.md
"### <a name=""install-multiple-cloud-link-services-windows"">Instalar múltiples servicios de Windows","### <a name=""install-multiple-cloud-link-services-windows"">Instalar múltiples servicios de Windows",install-cloud-link.md
"Puedes instalar hasta ocho servicios adicionales para gestionar distintas integraciones. Para evitar sobrescribir servicios instalados previamente, recomendamos usar directorios separados.","Puedes instalar hasta ocho servicios adicionales para gestionar distintas integraciones. Para evitar sobrescribir servicios instalados previamente, recomendamos usar directorios separados.",install-cloud-link.md
"Para instalar más servicios, sigue estos pasos:","Para instalar más servicios, sigue estos pasos:",install-cloud-link.md
1. Crea un nuevo directorio y copia los archivos del directorio de instalación original.,1. Crea un nuevo directorio y copia los archivos del directorio de instalación original.,install-cloud-link.md
2. Modifica el parámetro TRANSFORMS en el siguiente comando:,2. Modifica el parámetro TRANSFORMS en el siguiente comando:,install-cloud-link.md
```,```,install-cloud-link.md
"msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS="":instance.1""","msiexec /i injixo-cloud-link.msi MSINEWINSTANCE=1 TRANSFORMS="":instance.1""",install-cloud-link.md
```,```,install-cloud-link.md
Numera el valor del parámetro TRANSFORMS en este orden:,Numera el valor del parámetro TRANSFORMS en este orden:,install-cloud-link.md
"- `"":instance.1""` <!-- the docs say :instance.mst https://learn.microsoft.com/en-us/windows/win32/msi/installing-multiple-instances-with-instance-transforms -->","- `"":instance.1""` <!-- the docs say :instance.mst https://learn.microsoft.com/en-us/windows/win32/msi/installing-multiple-instances-with-instance-transforms -->",install-cloud-link.md
"- `"":instance.2""`","- `"":instance.2""`",install-cloud-link.md
3. Abre el símbolo del sistema de Windows (cmd).,3. Abre el símbolo del sistema de Windows (cmd).,install-cloud-link.md
4. Ejecuta el comando msiexec partiendo del nuevo directorio de instalación.,4. Ejecuta el comando msiexec partiendo del nuevo directorio de instalación.,install-cloud-link.md
"Cuando se complete la instalación, verás un servicio de Windows con el nombre _injixo Cloud Link (Instance {id})_.","Cuando se complete la instalación, verás un servicio de Windows con el nombre _injixo Cloud Link (Instance {id})_.",install-cloud-link.md
### Instalación del servicio de Linux,### Instalación del servicio de Linux,install-cloud-link.md
Instala el primer servicio basado en el siguiente ejemplo:,Instala el primer servicio basado en el siguiente ejemplo:,install-cloud-link.md
1. Haz clic en **Descargar para Linux 64-bit** y extrae el archivo al directorio de instalación que prefieras.,1. Haz clic en **Descargar para Linux 64-bit** y extrae el archivo al directorio de instalación que prefieras.,install-cloud-link.md
2. Abre un terminal.,2. Abre un terminal.,install-cloud-link.md
3. Instala el servicio injixo Cloud Link:,3. Instala el servicio injixo Cloud Link:,install-cloud-link.md
`sudo ./injixo-cloud-link service install`,`sudo ./injixo-cloud-link service install`,install-cloud-link.md
4. Lanza el servicio instalado:,4. Lanza el servicio instalado:,install-cloud-link.md
`sudo ./injixo-cloud-link service start`,`sudo ./injixo-cloud-link service start`,install-cloud-link.md
5. Muestra un PIN usando el comando:,5. Muestra un PIN usando el comando:,install-cloud-link.md
`sudo ./injixo-cloud-link pin`,`sudo ./injixo-cloud-link pin`,install-cloud-link.md
Una ventana de la consola te muestra un PIN que es válido durante cinco minutos.,Una ventana de la consola te muestra un PIN que es válido durante cinco minutos.,install-cloud-link.md
"Para [conectar injixo Cloud Link a tu integración](#conectar-injixo-cloud-link-a-tu-integración), sigue las instrucciones de la consola.","Para [conectar injixo Cloud Link a tu integración](#conectar-injixo-cloud-link-a-tu-integración), sigue las instrucciones de la consola.",install-cloud-link.md
"### <a name=""install-multiple-cloud-link-services-linux"">Instalar múltiples servicios de Linux","### <a name=""install-multiple-cloud-link-services-linux"">Instalar múltiples servicios de Linux",install-cloud-link.md
"Puedes instalar múltiples servicios para gestionar distintas integraciones. Para evitar sobrescribir servicios instalados previamente, recomendamos usar directorios separados.","Puedes instalar múltiples servicios para gestionar distintas integraciones. Para evitar sobrescribir servicios instalados previamente, recomendamos usar directorios separados.",install-cloud-link.md
"Para instalar más servicios, sigue estos pasos:","Para instalar más servicios, sigue estos pasos:",install-cloud-link.md
1. Crea un nuevo directorio y copia los archivos del directorio de instalación original.,1. Crea un nuevo directorio y copia los archivos del directorio de instalación original.,install-cloud-link.md
2. Abre el archivo injixo-cloud-link.toml.,2. Abre el archivo injixo-cloud-link.toml.,install-cloud-link.md
3. Modifica el valor de **name** en la sección **[app]** con un nuevo ID:,3. Modifica el valor de **name** en la sección **[app]** con un nuevo ID:,install-cloud-link.md
```,```,install-cloud-link.md
[app],[app],install-cloud-link.md
"name = ""com.injixo.cloud-link.instance.1""","name = ""com.injixo.cloud-link.instance.1""",install-cloud-link.md
```,```,install-cloud-link.md
"4. Instala e inicia el nuevo servicio desde el nuevo directorio, como se ha descrito anteriormente.","4. Instala e inicia el nuevo servicio desde el nuevo directorio, como se ha descrito anteriormente.",install-cloud-link.md
## Conectar injixo Cloud Link a tu integración,## Conectar injixo Cloud Link a tu integración,install-cloud-link.md
"La instalación de injixo Cloud Link muestra el siguiente mensaje, que incluye un PIN:","La instalación de injixo Cloud Link muestra el siguiente mensaje, que incluye un PIN:",install-cloud-link.md
```,```,install-cloud-link.md
"** Before you are able to run the client,","** Before you are able to run the client,",install-cloud-link.md
** link it to your injixo account:,** link it to your injixo account:,install-cloud-link.md
**  1) Log in to injixo.com,**  1) Log in to injixo.com,install-cloud-link.md
**  2) Visit https://www.injixo.com/account/integrations,**  2) Visit https://www.injixo.com/account/integrations,install-cloud-link.md
**  3) Select an integration you want to connect the client to,**  3) Select an integration you want to connect the client to,install-cloud-link.md
**  4) Enter your pin: 424242 (expires in 5 minutes),**  4) Enter your pin: 424242 (expires in 5 minutes),install-cloud-link.md
```,```,install-cloud-link.md
1. Vuelve a la página **Añadir una nueva integración** en tu navegador.,1. Vuelve a la página **Añadir una nueva integración** en tu navegador.,install-cloud-link.md
"2. En la sección **injixo Cloud Link**, introduce el PIN en el campo **PIN mostrado durante la instalación**.","2. En la sección **injixo Cloud Link**, introduce el PIN en el campo **PIN mostrado durante la instalación**.",install-cloud-link.md
3. Haz clic en _Conectar_{:.doc-button}.,3. Haz clic en _Conectar_{:.doc-button}.,install-cloud-link.md
Cloud Link se conecta a injixo. Ya puedes continuar configurando tu {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %} o {% link_new integración de CSV | features/acd-integration/cloud/add-csv-integration.md %}.,Cloud Link se conecta a injixo. Ya puedes continuar configurando tu {% link_new integración on-premise | features/acd-integration/cloud/add-on-premise-integration.md %} o {% link_new integración de CSV | features/acd-integration/cloud/add-csv-integration.md %}.,install-cloud-link.md
## Conectarse vía un servidor proxy,## Conectarse vía un servidor proxy,install-cloud-link.md
"Para conectarte vía servidor proxy, añade el nombre del host del proxy o su dirección IP a la variable de entorno **https_proxy**:","Para conectarte vía servidor proxy, añade el nombre del host del proxy o su dirección IP a la variable de entorno **https_proxy**:",install-cloud-link.md
"- Windows: añade la variable de entorno en la sección **Variables del sistema**. Si los servicios no funcionan con la cuenta de LocalSystem, configura una variable de usuario.","- Windows: añade la variable de entorno en la sección **Variables del sistema**. Si los servicios no funcionan con la cuenta de LocalSystem, configura una variable de usuario.",install-cloud-link.md
- Linux: configura la variable de entorno en /etc/environment o en /etc/profile.d.,- Linux: configura la variable de entorno en /etc/environment o en /etc/profile.d.,install-cloud-link.md
Ejemplo: https_proxy=http://your.proxy.example,Ejemplo: https_proxy=http://your.proxy.example,install-cloud-link.md
"Si es necesario, puedes añadir el número de puerto (si no es el puerto 80) y el nombre de usuario y contraseña para la autenticación:","Si es necesario, puedes añadir el número de puerto (si no es el puerto 80) y el nombre de usuario y contraseña para la autenticación:",install-cloud-link.md
Ejemplo: https_proxy=http://username:password@your.proxy.example:8080,Ejemplo: https_proxy=http://username:password@your.proxy.example:8080,install-cloud-link.md
## Compartir las direcciones IP de destino de injixo <!-- rethink the name -->,## Compartir las direcciones IP de destino de injixo <!-- rethink the name -->,install-cloud-link.md
"Para permitir que injixo Cloud Link se conecte a los servidores en la nube de injixo, comparte las siguientes URL:","Para permitir que injixo Cloud Link se conecte a los servidores en la nube de injixo, comparte las siguientes URL:",install-cloud-link.md
- injixo-*.s3-eu-west-1.amazonaws.com,- injixo-*.s3-eu-west-1.amazonaws.com,install-cloud-link.md
- www.injixo.com,- www.injixo.com,install-cloud-link.md
"No puedes compartir solo una dirección IP. Los procesos de distribución y actualización modifican con regularidad las direcciones IP de un servidor. Valora si instalar injixo Cloud Link en el DMZ. Si la conexión al servidor falla, verás [códigos de error de sockets de Windows](https://learn.microsoft.com/es-es/windows/win32/winsock/windows-sockets-error-codes-2) en el archivo de registro.","No puedes compartir solo una dirección IP. Los procesos de distribución y actualización modifican con regularidad las direcciones IP de un servidor. Valora si instalar injixo Cloud Link en el DMZ. Si la conexión al servidor falla, verás [códigos de error de sockets de Windows](https://learn.microsoft.com/es-es/windows/win32/winsock/windows-sockets-error-codes-2) en el archivo de registro.",install-cloud-link.md
## Registro,## Registro,install-cloud-link.md
"injixo Cloud Link rota los archivos de registro diariamente y tras cada reinicio, pero no los borra. Los archivos actuales se encuentran en injixo-cloud-link.log. Los archivos de registro rotados incluyen la fecha de rotación en el nombre del archivo. Para borrarlos, tienes que configurar un borrado regular o borrarlos manualmente.","injixo Cloud Link rota los archivos de registro diariamente y tras cada reinicio, pero no los borra. Los archivos actuales se encuentran en injixo-cloud-link.log. Los archivos de registro rotados incluyen la fecha de rotación en el nombre del archivo. Para borrarlos, tienes que configurar un borrado regular o borrarlos manualmente.",install-cloud-link.md
### Activar el registro detallado,### Activar el registro detallado,install-cloud-link.md
"Para las integraciones de base de datos, injixo Cloud Link ofrece un modo de registro detallado. Con él activado, el archivo de registro muestra el número total de filas recuperadas y las primeras diez filas de datos para cada demanda.","Para las integraciones de base de datos, injixo Cloud Link ofrece un modo de registro detallado. Con él activado, el archivo de registro muestra el número total de filas recuperadas y las primeras diez filas de datos para cada demanda.",install-cloud-link.md
"Para activar el registro detallado, sigue estos pasos:","Para activar el registro detallado, sigue estos pasos:",install-cloud-link.md
1. Pausa injixo Cloud Link.,1. Pausa injixo Cloud Link.,install-cloud-link.md
"2. En el directorio de instalación, abre el archivo injixo-cloud-link.toml.","2. En el directorio de instalación, abre el archivo injixo-cloud-link.toml.",install-cloud-link.md
"3. En la sección **[app]**, define **verbose** como true:","3. En la sección **[app]**, define **verbose** como true:",install-cloud-link.md
```,```,install-cloud-link.md
[app],[app],install-cloud-link.md
verbose = true,verbose = true,install-cloud-link.md
```,```,install-cloud-link.md
4. Guarda el archivo y reinicia injixo Cloud Link.,4. Guarda el archivo y reinicia injixo Cloud Link.,install-cloud-link.md
## Configurar la carpeta de importaciones,## Configurar la carpeta de importaciones,install-cloud-link.md
"Por defecto, injixo Cloud Link sube los archivos guardados en su carpeta de instalación. Para las integraciones de CSV, puedes configurar una carpeta de importaciones personalizada. Para ello, sigue estos pasos:","Por defecto, injixo Cloud Link sube los archivos guardados en su carpeta de instalación. Para las integraciones de CSV, puedes configurar una carpeta de importaciones personalizada. Para ello, sigue estos pasos:",install-cloud-link.md
1. Pausa injixo Cloud Link.,1. Pausa injixo Cloud Link.,install-cloud-link.md
"2. En el directorio de instalación, abre el archivo injixo-cloud-link.toml.","2. En el directorio de instalación, abre el archivo injixo-cloud-link.toml.",install-cloud-link.md
"3. En la sección **[app]**, define tu carpeta de importaciones como valor de **importDirectory**.","3. En la sección **[app]**, define tu carpeta de importaciones como valor de **importDirectory**.",install-cloud-link.md
- Usa rutas relativas o absolutas.,- Usa rutas relativas o absolutas.,install-cloud-link.md
- Usa una segunda barra invertida como secuencia de escape para la barra invertida.,- Usa una segunda barra invertida como secuencia de escape para la barra invertida.,install-cloud-link.md
4. Guarda el archivo y reinicia injixo Cloud Link.,4. Guarda el archivo y reinicia injixo Cloud Link.,install-cloud-link.md
## Preguntas frecuentes,## Preguntas frecuentes,install-cloud-link.md
<style>,<style>,install-cloud-link.md
table th:first-of-type {,table th:first-of-type {,install-cloud-link.md
width: 25%;,width: 25%;,install-cloud-link.md
},},install-cloud-link.md
table th:nth-of-type(2) {,table th:nth-of-type(2) {,install-cloud-link.md
width: 75%;,width: 75%;,install-cloud-link.md
},},install-cloud-link.md
</style>,</style>,install-cloud-link.md
| Pregunta                                                                        | Respuesta                                                                                                                                                                                                                                                                                                                                                                                                           |,| Pregunta                                                                        | Respuesta                                                                                                                                                                                                                                                                                                                                                                                                           |,install-cloud-link.md
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |,| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |,install-cloud-link.md
| ¿Cómo puedo obtener un nuevo PIN si el antiguo ha expirado?                              | Reinicia injixo Cloud Link. Introduce el nuevo PIN del archivo de registro en el campo con seis dígitos en la sección **injixo Cloud Link** de la página de configuración.                                                                                                                                                                                                                                                      |,| ¿Cómo puedo obtener un nuevo PIN si el antiguo ha expirado?                              | Reinicia injixo Cloud Link. Introduce el nuevo PIN del archivo de registro en el campo con seis dígitos en la sección **injixo Cloud Link** de la página de configuración.                                                                                                                                                                                                                                                      |,install-cloud-link.md
"| ¿Cómo puedo eliminar Cloud Link de mi sistema?                                      | 1\. Vuelve a ejecutar el instalar de injixo Cloud Link o ve a _Programas > Programas y características_{:.breadcrumbs} en Windows.<br>2\. Haz clic con la tecla derecha en **injixo Cloud Link** en la lista y selecciona **Desinstalar** o **Desinstalar o cambiar**.<br>3\. Sigue las instrucciones en la pantalla.<br><br>Para desinstalar otras instancias, ve a _Programas > Programas y características_{:.breadcrumbs} en Windows y sigue los pasos 2 y 3. |","| ¿Cómo puedo eliminar Cloud Link de mi sistema?                                      | 1\. Vuelve a ejecutar el instalar de injixo Cloud Link o ve a _Programas > Programas y características_{:.breadcrumbs} en Windows.<br>2\. Haz clic con la tecla derecha en **injixo Cloud Link** en la lista y selecciona **Desinstalar** o **Desinstalar o cambiar**.<br>3\. Sigue las instrucciones en la pantalla.<br><br>Para desinstalar otras instancias, ve a _Programas > Programas y características_{:.breadcrumbs} en Windows y sigue los pasos 2 y 3. |",install-cloud-link.md
"| ¿Cómo puedo mover injixo Cloud Link a un servidor nuevo?                                | 1\. Haz clic en {% icon pencil %} junto a una integración.<br>2\. Haz clic en **Conectar una nueva instalación de injixo Cloud Link**.<br>3\. Si es necesario, vuelve a descargar injixo Cloud Link e instálalo en el servidor nuevo.                                                                                                                                                                          |","| ¿Cómo puedo mover injixo Cloud Link a un servidor nuevo?                                | 1\. Haz clic en {% icon pencil %} junto a una integración.<br>2\. Haz clic en **Conectar una nueva instalación de injixo Cloud Link**.<br>3\. Si es necesario, vuelve a descargar injixo Cloud Link e instálalo en el servidor nuevo.                                                                                                                                                                          |",install-cloud-link.md
"| ¿Cómo modifico mi integración para una instalación de injixo Cloud Link que ya existe? | 1\. Ve al directorio de instalación y copia el PIN del archivo de registro.<br>2\. Borra la integración existente y crea una nueva.<br>3\. Conecta el injixo Cloud Link en curso con la integración nueva. Para ello, introduce el PIN durante la configuración de la integración nueva.                                                                                                               |","| ¿Cómo modifico mi integración para una instalación de injixo Cloud Link que ya existe? | 1\. Ve al directorio de instalación y copia el PIN del archivo de registro.<br>2\. Borra la integración existente y crea una nueva.<br>3\. Conecta el injixo Cloud Link en curso con la integración nueva. Para ello, introduce el PIN durante la configuración de la integración nueva.                                                                                                               |",install-cloud-link.md
