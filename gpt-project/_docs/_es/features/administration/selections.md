---
title: Crear y gestionar grupos
description: Crea grupos y asígnales personas.
product_label:
  - essential
  - advanced
  - enterprise
  - classic
redirect_from: /es/selections-overview/
redirect_reason: renamed file in April 2022
---

Los grupos se basan en criterios a los que asignas empleados y que puedes usar como filtro. Los grupos funcionan de manera similar a los {% link_new filtros avanzados | features/administration/employee-filter.md %}. Se diferencian en lo siguiente:

- En los grupos puedes crear tus propios criterios de agrupación.
- En los filtros avanzados los criterios de agrupación se basan en elementos de configuración, como unidad de planificación, cualificaciones y contrato.

Además, los filtros avanzados solo están disponibles en injixo Classic, Advanced y Enterprise.

Los grupos se utilizan por regla general para agrupar a empleados que:

- tienen el mismo supervisor;
- teletrabajan;
- han sido contratados recientemente y pueden necesitar apoyo o supervisión adicional;
- pueden sustituir a otras personas en caso de emergencia;
- tienen responsabilidades adicionales irrelevantes para la planificación pero que pueden ser importantes, p.&nbsp;ej., personas formadas en primeros auxilios.

Si usas injixo Essential, puedes usar los grupos para agrupar empleados de acuerdo con elementos de configuración como unidades de planificación, cualificaciones y contratos.

## Crear grupos

1. Ve a _Plan > Configuración > Grupos_{:.breadcrumbs}.
2. Haz clic en el icono Nuevo {% icon item-add | icon-only %} arriba a la izquierda.  
    Se abre un panel de configuración a la derecha.
3. Completa los siguientes campos:
    - **Nombre**: nombre único para el grupo (máximo 50 caracteres).
    - **Abreviatura**: abreviatura del nombre (máximo 25 caracteres).
    - **Descripción**: descripción opcional para que otros usuarios entiendan qué representa el grupo.
4. Haz clic en _Aceptar_{:.doc-button}.

## Asignar empleados a grupos

Para asignar empleados a grupos primero debes [crear un grupo](#crear-grupos).

1. Ve a _Plan > Configuración > Empleados_{:.breadcrumbs}.
2. Haz clic en el empleado que quieres asignar a un grupo.  
   Se abre un panel de configuración a la derecha.
3. En la sección **Grupos**, haz clic en el icono Insertar {% icon item-add | icon-only %}.
4. Haz clic en el grupo al que quieres asignar al empleado.
5. (Opcional) Introduce un rango de fechas en los campos **Válido desde** y **Válido hasta** para limitar el periodo de validez del grupo. Deja los campos **Válido desde** y **Válido hasta** en blanco si quieres que el grupo esté siempre disponible. Aprende más sobre los {% link_new períodos de validez | features/administration/set-a-validity-period.md %}.
6. Haz clic en _Aceptar_{:.doc-button}.

Para editar un grupo al que el empleado está asignado, haz clic en el icono Editar {% icon item-edit | icon-only %}. Para eliminar la asignación al grupo, haz clic en el icono Eliminar {% icon item-delete | icon-only %}.

## Combinar grupos

injixo Classic, Advanced y Enterprise permiten asignar grupos a otros grupos. El grupo al que se asignan otros grupos se convierte en un grupo principal. Los grupos asignados se convierten en grupos de nivel secundario. Esto te permite usar el grupo principal para filtrar empleados de todos los grupos secundarios.

Para crear una jerarquía de grupos entre grupos secundarios y un grupo principal, empieza por [crear los grupos principal y secundarios](#crear-grupos).

Para asignar un grupo a otro grupo, sigue estos pasos:

1. Haz clic en el grupo que quieres usar como grupo principal en la lista de grupos.  
   Se abre un panel de configuración a la derecha.
2. En la sección **Grupos**, haz clic en el icono Insertar {% icon item-add | icon-only %}.
3. Haz clic en el grupo al que quieres asignar un grupo secundario.
4. (Opcional) Introduce un rango de fechas en los campos **Válido desde** y **Válido hasta** para asignar los grupos secundarios al grupo principal durante un tiempo limitado. Deja los campos **Válido desde** y **Válido hasta** en blanco si quieres que la asignación esté activa sin límite temporal.
5. Haz clic en _Aceptar_{:.doc-button}.

Para editar o eliminar un grupo secundario, haz clic en el icono Editar {% icon item-edit | icon-only %} o en el icono Eliminar {% icon item-delete | icon-only %}.

> Jerarquía de grupos
>
> La jerarquía entre grupos principales y secundarios no es visible en _Plan > Configuración > Empleados_{:.breadcrumbs}. Para comprobar si un grupo es un grupo principal, ve a _Plan > Configuración > Grupos_{:.breadcrumbs} y haz clic en un grupo en la sección **Grupos**. Otra opción es otorgar nombres a los grupos que reflejen claramente la jerarquía.

## Eliminar un grupo

1. Ve a _Plan > Configuración > Grupos_{:.breadcrumbs}.
2. En la lista, haz clic en el grupo que quieres eliminar.
3. Haz clic en el icono Eliminar {% icon item-delete | icon-only %} arriba a la izquierda.
4. Para confirmar, haz clic en _Sí_{:.doc-button}.
