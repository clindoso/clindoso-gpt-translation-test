---
title: Configurar filtros avanzados de empleados
description: Usa el editor de filtros de empleados para filtrar empleados siguiendo una combinación de criterios.
product_label:
  - advanced
  - enterprise
  - classic
---

Con los filtros avanzados puedes crear listas de empleados que cumplan varios criterios. Las opciones de edición dependen de tus derechos de usuario.

Los filtros avanzados funcionan de manera similar a los {% link_new grupos | features/administration/selections.md %}. Se diferencian en lo siguiente:

- En los filtros avanzados los criterios de agrupación se basan en elementos de configuración, como unidad de planificación, cualificaciones y contrato.
- En los grupos puedes crear tus propios criterios de agrupación.

Los filtros avanzados solo están disponibles en injixo Classic, Advanced y Enterprise.
  
1. Para acceder al editor de filtros, ve a _Plan > Centro de planificación_{:.breadcrumbs}.
2. Si el mosaico de grupo {% icon selection-filter-s | icon-only %} está seleccionado: selecciona el mosaico empleado {% icon schedules-filter-employees-u | icon-only %}.
3. Haz clic en el enlace **Editor del filtro avanzado**.

## Crear un filtro avanzado

1. En la sección **Filtro avanzado**, haz clic en el icono Crear filtro {% icon item-add | icon-only %}.
2. Selecciona un tipo de **período**:<br>
    - **Personalizado**: establece manualmente el período de tiempo con el selector de fechas. Selecciona una fecha de inicio y una fecha de fin.<br>
    - **Fijo**: establece un período para la semana, mes o año previo, actual o próximo.<br>
    - **Predefinido**: se establece automáticamente el día actual como periodo.
3. [**Define el filtro**](#definir-un-filtro).
4. Para ver los resultados del filtro, haz clic en _Filtrar_{:.doc-button}.
5. Para añadir el filtro al filtro avanzado, haz clic en _Aplicar_{:.doc-button}.
6. Para guardar el filtro, haz clic en el icono Guardar filtro {% icon save | icon-only %}.<br>Para guardar un filtro existente con un nombre diferente, haz clic en el icono Guardar filtro como...{% icon saveas | icon-only %}.

## Definir un filtro

Un filtro es un conjunto de condiciones para cribar y extraer datos de un conjunto de datos mayor. Puedes definir criterios y obtener una lista de empleados que cumplan con esos criterios.

1. En la sección **Definición del filtro**, haz clic en el {% icon item-add %}.
2. En el primer menú desplegable, selecciona un tipo de datos de configuración.
3. En el segundo menú desplegable, selecciona una condición.
4. (Opcional) Selecciona una [prioridad y operadores relacionales](#usar-operadores-relacionales-y-la-prioridad) para unidades de planificación, categorías de empleados o cualificaciones.
5. Haz clic en _Aplicar_{:.doc-button}.

Para editar un filtro, haz clic en el {% icon item-edit %}.

## Usar condiciones

### IS IN

La condición **IS IN** muestra resultados que coinciden exactamente con el filtro.
 
1. Selecciona un tipo de datos de configuración en el primer menú desplegable.
2. Selecciona **IS IN** en el segundo menú desplegable.
3. Haz clic en _Criterios_{:.doc-button} para ver los criterios disponibles y selecciona uno de la lista.
4. Para añadir criterios a tu selección, haz clic en la {% icon right-arrow-blue %}.
5. En la ventana **Seleccionar criterios**, haz clic en _Aplicar_{:.doc-button}.
6. (Opcional) Selecciona [opciones y operadores relacionales](#usar-operadores-relacionales-y-la-prioridad) para unidades de planificación, categorías de empleados o cualificaciones.
7. Haz clic en _Aplicar_{:.doc-button}.

### IS LIKE

La condición **IS LIKE** muestra resultados que coinciden parcialmente con el filtro.

1. Selecciona un tipo de datos de configuración en el primer menú desplegable.
2. Selecciona **IS LIKE** en el segundo menú desplegable.
3. Introduce el texto por el que quieres filtrar.
    - Para reemplazar varios caracteres, usa el marcador *.
    - Para reemplazar exactamente un carácter, usa el marcador ?.
4. (Opcional) Selecciona [opciones y operadores relacionales](#usar-operadores-relacionales-y-la-prioridad) para unidades de planificación, categorías de empleados o cualificaciones.
5. Haz clic en _Aplicar_{:.doc-button}.

## Usar operadores relacionales y la prioridad

Con la casilla Prioridad y los operadores relacionales puedes incluir en tu filtro empleados según su prioridad y asignación a la unidad de planificación o categoría de empleados seleccionada:  

1. Selecciona la **unidad de planificación** o la **categoría de empleado** en el primer menú desplegable.
2. Marca la casilla **Prioridad**.
3. Selecciona un operador relacional de la lista.
4. Introduce un valor de prioridad.

Con el elemento de configuración Cualificación puedes usar operadores relacionales para incluir solo empleados con un cierto nivel de cualificación:  

1. Selecciona **Cualificación** en el primer menú desplegable.
2. Marca la casilla **Grado de cualificación**.
3. Selecciona un operador relacional de la lista.
4. Introduce el valor del nivel de cualificación.

## Vincular filtros

Puedes vincular filtros individuales entre sí:

1. Crea o selecciona un [filtro avanzado](#crear-un-filtro-avanzado).
2. Define un [filtro](#definir-un-filtro).
3. Selecciona un operador condicional:<br>
  - **AND**: incluye los empleados que cumplan todas las condiciones.  
  - **OR**: incluye los empleados que cumplan al menos una condición.  
  - **NOT**: Excluye a los empleados que cumplan la condición que sigue al operador NOT.
4. Crea un segundo filtro.
5. Haz clic en _Aplicar_{:.doc-button}.

Para crear un grupo, abre un paréntesis. Para cerrarlo, cierra el paréntesis. Usa las flechas hacia arriba y hacia abajo para mover y ordenar los filtros individuales en cualquier momento.

## Ejemplo de filtro

Para filtrar empleados de la unidad de planificación Nueva York que no tienen un contrato de jornada completa de 40 horas y no son parte del grupo Horas extra, el filtro debe seguir esta estructura:


```
Unidad de planificación IS IN "Nueva York"
AND
NOT
(
Contrato IS IN " Jornada completa 40h"
AND
Grupo IS IN "Horas extra"
)
```

Este filtro selecciona a todos los empleados de la unidad de planificación Nueva York y luego excluye a las personas que tienen un contrato de jornada completa de 40 horas y forman parte del grupo Horas extra:

- **IS IN** define la condición para la unidad de planificación.
- **AND** combina las condiciones del filtro.
- **NOT** excluye las condiciones que le siguen.
- Los paréntesis abren y cierran el grupo de condiciones a excluir.
- **IS IN** selecciona los empleados que tienen un contrato de jornada completa de 40 horas.
- **AND** combina las condiciones dentro de los paréntesis.
- **IS IN** selecciona los empleados que forman parte del grupo Horas extra.

## Editar filtros

1. En el menú desplegable **Filtro avanzado**, selecciona un filtro.
2. Edita la información que deseas modificar.
3. (Opcional) Para cambiar el nombre de tu filtro, haz clic en el {% icon item-edit %}.
4. Para guardar, haz clic en el {% icon save %}.<br>Para guardar un filtro existente con un nombre diferente, haz clic en el {% icon saveas %}.
