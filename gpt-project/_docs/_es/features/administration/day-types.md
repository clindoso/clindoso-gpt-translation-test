---
title: Crear y usar tipos de día
description: Crea tipos de día para representar días festivos y otros días especiales que cambian tus horas laborales.
product_label:
  - advanced
  - enterprise
  - classic
related_articles:
  - overwrite_title: Crear y gestionar unidades de planificación
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Crear y usar calendarios de planificación
    filepath: features/administration/planning-calendar.md
  - overwrite_title: Planificar días festivos
    filepath: best-practices/scheduling-public-holidays.md
---

Los tipos de día definen los días con horarios de apertura estándar y los días con horarios diferentes.

Añade tipos de día a tu {% link_new unidad de planificación | features/administration/create-and-manage-planning-units.md | #añadir-horarios-de-apertura %} para establecer los horarios de apertura para los días estándar y para días especiales, p.&nbsp;ej., si tu organización abre los festivos. injixo tendrá en cuenta las horas de apertura definidas para esos días durante la planificación optimizada.

En _Plan > Configuración > Tipos de día_{:.breadcrumbs} puedes:

- ver los tipos de día predefinidos;
- crear, editar y eliminar los tipos de día personalizados.

## Crear un tipo de día personalizado

Puede ser que tu horario de apertura se desvíe del estándar algunos días, p.&nbsp;ej., cuando hay promociones especiales o en festivos. Para crear tipos de día personalizados para esos días, sigue estos pasos:

1. Haz clic en el icono Nuevo {% icon item-add | icon-only %} en la barra de acciones.
2. Introduce un **nombre** (máximo 50 caracteres).
3. Introduce una **abreviatura** (máximo 25 caracteres).  
   La abreviatura aparecerá en el calendario de planificación.
4. (Opcional) Marca la casilla **Modo de día festivo**.<br>[Aprende más](#modo-de-día-festivo) sobre cómo configurar los tipos de día para festivos.
5. Haz clic en _Aceptar_{:.doc-button}.

## Modo de día festivo

 Para marcar un tipo de día como festivo, activa la casilla **Modo de día festivo** en la ventana de configuración del tipo de día.

### Crear tipos de día para festivos nacionales

Hay dos opciones para crear tipos de día para festivos nacionales:

- Crear tipos de día con el modo de día festivo y {% link_new añadirlos a tu calendario de planificación | features/administration/planning-calendar.md | #configure-a-planning-calendar %}.

- Añadir una {% link_new plantilla de calendario | features/administration/planning-calendar.md |#configure-a-planning-calendar %} a tu calendario de planificación. Esta opción crea automáticamente todos los tipos de día para los festivos nacionales incluidos con el modo de día festivo activado.

El modo de día festivo reduce las horas laborales de los empleados como corresponde. Si decides planificar el día como un día laboral estándar, siempre puedes [editar el tipo de día](#editar-un-tipo-de-día) y desactivar el modo de día festivo.

## Editar un tipo de día

> Advertencia
>
> Si desactivas el modo de día festivo de un modelo de día que está actualmente en uso, tendrás que volver a calcular las cuentas de horas o las {% link_new cuentas de horas previstas | features/scheduling/planning-periods/target-work-accounts.md %}.
   
1. Selecciona un tipo de día de la lista.
2. Edita los datos que quieres modificar.
3. Haz clic en _Aceptar_{:.doc-button}.

## Eliminar un tipo de día

> Atención
> 
> Antes de eliminar un tipo de día, {% link_new elimínalo de todos los calendarios de planificación | features/administration/planning-calendar.md | #remove-day-types-from-the-planning-calendar %}. No puedes eliminar los tipos de día predefinidos.

1. Selecciona un tipo de día de la lista.
2. En la barra de acciones, haz clic en el icono Eliminar {% icon item-delete | icon-only %} en la barra de acciones.

## Tipos de día en la planificación

injixo tiene en cuenta los tipos de día durante la planificación. 
- Si tu unidad de planificación abre regularmente un festivo, solo tienes que {% link_new añadir el horario de apertura a la unidad de planificación | features/administration/create-and-manage-planning-units.md | #añadir-horarios-de-apertura %}.  
- Si tu unidad de planificación cierra un día festivo, o si abre con horarios de apertura especiales, lee el artículo {% link_new Planificar días festivos | best-practices/scheduling-public-holidays.md %}.
