---
title: Gestionar empleados
product_label:
  - advanced
  - enterprise
description: Aprende a crear, consultar, editar y eliminar empleados.
beta-feature: true
redirect_from: /people-overview/
redirect_reason: Renamed from /people-overview/ to /manage-people/ in Jan 2023
---

Con People puedes gestionar los datos más importantes de todos los empleados de tu organización:

- Crear, editar y eliminar perfiles de empleados.
- Invitar a un empleado nuevo a injixo (enviar correo de bienvenida).
- Acceder a los ajustes de la cuenta de usuario de un empleado.
- Acceder a los datos de configuración del empleado en WFM.

> Los usuarios con acceso de administrador tienen por defecto acceso a People.
>
> Para {% link_new otorgar acceso a People a otros usuarios | getting-started/configure-user-roles.md %} ve a _Account > Roles de usuario_{:.breadcrumbs}.

## Crear un empleado

1. Ve a _People_{:.breadcrumbs}.
2. Haz clic en _+ Nuevo empleado_{:.doc-button}.
3. Introduce la información básica obligatoria para el empleado:
   - **Nombre** y **Apellidos**, y opcionalmente, **segundo nombre**.
   - **Identificador personal**: identificador único para el empleado en tu organización.
   - **Correo electrónico (para iniciar sesión en injixo)**: introduce la dirección de correo que el empleado usará para iniciar sesión en injixo.
4. Para invitar al empleado a que inicie sesión en injixo, marca la casilla **Enviar correo de bienvenida**.  
   Solo puedes enviar el correo de bienvenida cuando creas un empleado. El correo incluye instrucciones para crear una contraseña y un enlace a la página de inicio de sesión de injixo.
5. (Opcional) Puedes introducir información adicional del empleado, como su número de teléfono u otros datos de contacto.
La información introducida en el campo **Título** no se utiliza en injixo. Puedes usar esta información para dirigirte a los empleados, p.&nbsp;ej., cuando envíes boletines informativos.
6. Haz clic en _Crear empleado_{:.doc-button}.  
   Si has marcado la casilla **Enviar correo de bienvenida**, injixo le enviará un correo de bienvenida al empleado.

## Invitar a un empleado a iniciar sesión en injixo

Solo puedes {% link_new enviar un correo con una invitación para iniciar sesión en injixo | features/people/manage-people.md | #crear-un-empleado %} cuando creas un empleado.

## Consultar o editar un empleado

1. Ve a _People_{:.breadcrumbs}.
2. (Opcional) Para buscar a un empleado, usa el campo **Búsqueda**.
3. Haz clic en un empleado en la lista.  
   Los detalles del empleado se muestran a la derecha. Para cerrar los detalles, haz clic en _Cancelar_{:.doc-button} o pulsa **Esc** en el teclado.
4. Edita los detalles del empleado.

   > Atención:
   >
   > Si modificas la dirección de correo, el empleado ya no podrá iniciar sesión en injixo con la dirección de correo antigua. Asegúrate de comunicarle a la persona su nueva dirección de correo. injixo no informará al empleado del cambio de la dirección de correo.

5. Haz clic en _Guardar cambios_{:.doc-button}.

## Eliminar un empleado

> Advertencia
>
> No puedes reactivar a un empleado eliminado. El empleado será de todas las planificaciones, actuales y futuras, en las que estuviera incluido. Eliminar un empleado no afecta a los datos históricos de adherencia en {% link_new Intraday | features/intraday/adherence-intraday.md %}.

1. Ve a _People_{:.breadcrumbs}.
2. Haz clic en un empleado en la lista.  
   Se muestran los datos del empleado.
3. Haz clic en _Eliminar empleado_{:.doc-button}.
4. En la ventana de confirmación, haz clic en _Eliminar empleado_{:.doc-button}.

Para asegurarte de que tus planificaciones han sido actualizadas tras eliminar un empleado, usa la optimización de tareas.
