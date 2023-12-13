---
title: Desactivar, reactivar y eliminar empleados
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Aprende cuándo y cómo desactivar, reactivar o eliminar empleados.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/how-does-billing-work.md
---

Si tienes empleados que ya no incluyes en la planificación o que ya no necesitan acceso a injixo, puedes desactivarlos o eliminarlos. Estas acciones tienen dos efectos:

- los empleados desactivados ya no pueden acceder a injixo;
- a tu organización ya no se le {% link_new facturarán | getting-started/how-does-billing-work.md %} estos empleados (a partir del mes siguiente).

## Desactivar empleados

Si un empleado no está disponible para trabajar durante un período prolongado de tiempo, p.&nbsp;ej., porque ha tomado un año sabático o un permiso de maternidad o paternidad, puedes desactivarlo temporalmente. A tu organización no se le facturarán los empleados desactivados. Puedes reactivar a los empleados cuando vuelvan al trabajo. En algunos casos, el Reglamento General de Protección de Datos (GDPR) de la Unión Europea puede exigir que elimines los datos de un empleado. Si este es el caso, [elimina el empleado](#eliminar-empleados).

Para desactivar un empleado, sigue estos pasos:

1. Ve a _Plan > Configuración > Empleados_{:.breadcrumbs}.
2. En la lista de empleados, haz clic en el empleado que quieres desactivar.
3. En la sección **Pertenencia a la empresa** en la ventana de configuración, haz clic en el {% icon item-edit %}.
4. Introduce una fecha de salida.<br>Una fecha de salida pasada desactivará inmediatamente el empleado. Una fecha de salida futura desactivará al empleado en la fecha especificada.
5. Haz clic en _Aceptar_{:.doc-button}.<br>Aparece un mensaje de confirmación.
6. Para eliminar planificaciones futuras pero al mismo tiempo mantener los datos históricos de planificación, haz clic en _Sí_{:.doc-button}. Para mantener todos los datos de planificación del empleado desactivado, haz clic en _No_{:.doc-button}.

### Lista de empleados desactivados

1. Ve a _Account > Usuarios_{:.breadcrumbs}.
2. Haz clic en la pestaña **Usuarios no facturados**.<br>La tabla muestra todos los usuarios desactivados que no son incluidos en las facturas de tu organización.

### Reactivar empleados

Para reactivar a un empleado, p.&nbsp;ej., cuando este regresa tras una larga ausencia, sigue estos pasos:

1. Ve a _Plan > Configuración > Empleados_{:.breadcrumbs}.
2. Use el campo de búsqueda en la esquina superior izquierda para encontrar al empleado que quieres reactivar.<br>Se abre una ventana. Si has introducido el nombre completo del empleado y la búsqueda devuelve solo un resultado, la ventana muestra el diálogo de configuración del empleado. Si la búsqueda devuelve varios resultados, la ventana muestra una lista de empleados.
3. Si la ventana muestra una lista, haz clic en el empleado que quieres reactivar.
4. En la sección **Pertenencia a la empresa** en la ventana de configuración, haz clic en el icono Insertar {% icon item-add | icon-only %}.
5. Introduce una fecha de entrada. 
6. Haz clic en _Aceptar_{:.doc-button}.

## Eliminar empleados

> Advertencia
>
> No puedes reactivar un empleado eliminado. El empleado será eliminado de todas las planificaciones, actuales y futuras, en las que estuviera incluido. Eliminar un empleado no afecta a los datos históricos de adherencia {% link_new Intraday | features/intraday/adherence-intraday.md %}.

Elimina empleados solo cuando su pertenencia a la empresa haya terminado de forma permanente. Cuando los empleados estén ausentes por un período más largo,p.&nbsp;ej., cuando toman un año sabático o un permiso de maternidad o paternidad, [desactívalos](#desactivar-empleados).

Para eliminar un empleado, sigue estos pasos:

1. Ve a _Plan > Configuración > Empleados_{:.breadcrumbs}.
2. En la lista de empleados, haz clic en el empleado que quieres eliminar.
3. En la barra de acciones, haz clic en el icono Eliminar {% icon item-delete | icon-only %}.<br>Aparece un mensaje de confirmación.
4. Haz clic en _Sí_{:.doc-button}.<br>El empleado y todas sus planificaciones presentes y futuras serán eliminadas de injixo.

Cuando eliminas a un empleado en injixo, sus datos personales se anonimizan para proteger su privacidad. injixo retiene el ID del empleado, pero lo marca como eliminado y sustituye su nombre por asteriscos. injixo también modifica los detalles personales para eliminar cualquier información identificable, como nombres, identificador personal, direcciones, números de teléfono y direcciones de correo electrónico. Si la configuración del empleado incluye números de documentos de identificación, injixo los elimina por completo.
