---
title: Gestionar las cuentas de los usuarios
description: Consulta los usuarios facturados y no facturados. Crea, modifica y elimina usuarios. Gestiona el acceso de los usuarios con roles de usuario.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/manage-2fa.md
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/default-user-roles.md
---

Configura cuentas de usuario en injixo para gestionar a los empleados de tu organización. 

En _Account > Usuarios_{:.breadcrumbs} tienes un resumen de todos los usuarios:
- Usuarios facturados: esta pestaña muestra todos los usuarios activos en tu tenant de injixo.
- Usuarios no facturados: esta pestaña muestra a todos los usuarios desactivados que ya no pueden iniciar sesión en injixo. A tu organización no se le {% link_new facturan | getting-started/how-does-billing-work.md %} los usuarios desactivados.

Para encontrar usuarios concretos, usa el campo de búsqueda arriba de la lista de usuarios. Usa comas para separar los términos de búsqueda.
Para filtrar usuarios por rol de usuario, haz clic en el encabezado de la columna **Roles de usuario**. Se abre un diálogo donde puedes seleccionar uno o varios roles. La lista muestra todos los usuarios que tengan asignados al menos uno de los roles seleccionados.

## Crear usuarios

Los usuarios también son llamados empleados. injixo ofrece tres lugares distintos para crear usuarios:
- _Account > Usuarios_{:.breadcrumbs}
- _WFM > Gestión > Planificación > Empleados_{:.breadcrumbs}
- {% link_new People | features/people/manage-people.md | #crear-un-empleado %}

> Atención
> 
> Solo necesitas crear un usuario una vez en uno de estos lugares. injixo sincronizará automáticamente los datos de este usuario en los otros dos lugares.

Para crear un usuario, sigue estos pasos:

1. Ve a _Account > Usuarios_{:.breadcrumbs}.
2. Haz clic en _Crear usuario_{:.doc-button}.
3. Introduce la información del usuario y haz clic en _Crear_{:.doc-button}.

## Editar una cuenta de usuario

injixo ofrece dos lugares donde puedes editar una cuenta de usuario, dependiendo de lo que quieras hacer. La tabla a continuación te brinda una visión general de las diferentes opciones de configuración y dónde encontrarlas en injixo. También puedes acceder a ambos lugares desde People.

| Qué quiero hacer                                          | A dónde ir en injixo                                                                             |
| -------------------------------------------------- | ------------------------------------------------------------------------------------- |
| {% link_new Configurar los ajustes de planificación de un usuario | features/administration/employee-overview.md | #panorámica-de-los-ajustes-de-empleado %} (p.&nbsp;ej., asignar actividades, añadir niveles de cualificación, definir disponibilidades) | _WFM > Gestión > Planificación > Empleados_{:.breadcrumbs} |
| {% link_new Editar información del periodo de permanencia | getting-started/manage-user-accounts.md | #desactivar-una-cuenta-de-usuario %} de un usuario       | _WFM > Gestión > Planificación > Empleados_{:.breadcrumbs} |   
| Editar la información de idioma y zona horaria de un usuario | _Account > Usuarios_{:.breadcrumbs} |
| {% link_new Asignar un rol de usuario a un usuario | getting-started/configure-user-roles.md | #asignar-roles-de-usuario-a-los-usuarios %} | _Account > Usuarios_{:.breadcrumbs} |
| {% link_new Activar la autenticación de dos factores (2FA) | getting-started/manage-2fa.md %}   | _Account > Usuarios_{:.breadcrumbs} |

Si quieres editar un usuario, p.&nbsp;ej., para cambiar su dirección de correo, sigue estos pasos:

1. Ve a _Account > Usuarios_{:.breadcrumbs}.
2. Haz clic en un nombre de usuario.
3. Modifica los ajustes del usuario.
4. Haz clic en _Guardar_{:.doc-button}.

### Conceder acceso de administrador a un usuario

1. Ve a _Account > Usuarios_{:.breadcrumbs}.
2. Haz clic en un nombre de usuario.
3. En la sección **Acceso de administrador**, marca la casilla **Conceder acceso de administrador**.
4. Haz clic en _Guardar_{:.doc-button}.

### Desbloquear usuarios

Las cuentas de usuario se bloquean tras tres intentos fallidos de iniciar sesión con una contraseña incorrecta. Para desbloquear usuarios bloqueados, sigue estos pasos:

1. Ve a _Account > Usuarios_{:.breadcrumbs}.<br>
La lista de usuarios muestra un {% icon lock %} en amarillo junto al nombre del usuario bloqueado.
2. Haz clic en el nombre del usuario bloqueado.
3. En la sección **Seguridad**, haz clic en _Desbloquear usuario_{:.doc-button}.

Cuando desbloquees un usuario, te recomendamos establecer una contraseña nueva para ese usuario. 

### Establecer una contraseña nueva para un usuario

Si un usuario olvida su contraseña, puede hacer clic en el enlace **¿Has olvidado la contraseña?** en la página de inicio de sesión para restablecerla. También puedes restablecerla en su lugar, p.&nbsp;ej., si su cuenta ha sido bloqueada.
Para establecer una contraseña nueva para un usuario, sigue estos pasos:

> Atención
>
> Los usuarios no reciben notificaciones sobre cambios de contraseña. Tienes que comunicarles que tienen una contraseña nueva.

1. Ve a _Account > Usuarios_{:.breadcrumbs}.
2. Haz clic en un nombre de usuario.
3. En la sección **Seguridad** a la derecha, haz clic en _Establecer contraseña nueva_{:.doc-button}.
4. Introduce una contraseña nueva para el usuario.
5. Haz clic en _Guardar_{:.doc-button}.

## Desactivar una cuenta de usuario

Para entender las consecuencias de desactivar usuarios, lee {% link_new este artículo | features/administration/deactivate-employees.md %}.

1. Ve a _Account > Usuarios_{:.breadcrumbs}.
2. Haz clic en un nombre de usuario.
3. Haz clic en _Eliminar_{:.doc-button} en la parte inferior derecha.  
   Se abre una ventana.
4. Para desactivar el usuario, haz clic en _Periodo de permanencia_{:.doc-button} y fija una fecha de salida. Se mantendrán todos los datos de planificación. Podrás reactivar el usuario más adelante.

Aprende cómo {% link_new reactivar usuarios | features/administration/deactivate-employees.md | #reactivar-empleados %}.

## Eliminar una cuenta de usuario

> Advertencia
>
> No puedes reactivar una cuenta de usuario eliminada. La cuenta de usuario será eliminada de todas las planificaciones, actuales y futuras, en las que estuviera incluida.

Para eliminar permanentemente una cuenta de usuario, sigue estos pasos:

1. Ve a _Account > Usuarios_{:.breadcrumbs}.
2. Haz clic en un nombre de usuario.
3. Haz clic en _Eliminar_{:.doc-button} en la parte inferior derecha.  
   Se abre una ventana.
4. Marca la casilla **Entiendo que todos los datos del usuario y todas las planificaciones de \<nombre de usuario\> se eliminarán.**
5. Haz clic en _Eliminar_{:.doc-button}. 

## Exportar la lista de usuarios en formato CSV

Puedes exportar la lista de usuarios completa o filtrada como archivo CSV. Por ejemplo, puedes importar el archivo CSV en bases de datos y herramientas externas, como bases de datos de Data Warehouse o sistemas SAP y de RR.HH.

1. Ve a _Account > Usuarios_{:.breadcrumbs}.
2. (Opcional) Para reducir la lista de usuarios, usa la búsqueda o el filtro de roles.
3. Haz clic en _Exportar a CSV_{:.doc-button} arriba a la derecha.  
   El archivo CSV se descarga a tu ordenador.

El archivo CSV está separado por comas y contiene apellidos, nombre y dirección de correo electrónico de los usuarios. El formato del archivo es permanente y no se puede cambiar.
