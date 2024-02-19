---
title: Modificación masiva
product_label:
  - advanced
  - enterprise
  - classic
---

Usa la modificación masiva para editar las asignaciones de datos de configuración de varios empleados al mismo tiempo.
Puedes usar la funcionalidad de modificación masiva para los siguientes elementos de configuración:

- Contratos
- Cualificaciones
- Unidades de planificación
- Grupos
- Rotaciones de turnos
- Modelos de planificación

## Prerrequisitos

Antes de poder usar la funcionalidad de modificación masiva, tienes que {% link_new definir la configuración de base| getting-started/set-up-base-configuration.md %}.

## Iniciar la modificación masiva

> Atención
>
> No puedes revertir o deshacer una modificación masiva. Inicia otra modificación masiva para sobrescribir los datos actualizados incorrectamente con una modificación masiva, o modifica los datos de cada empleado individualmente.  

Para iniciar una modificación masiva, sigue estos pasos: 

1. Ve a _Plan > Configuración > Empleados_{:.breadcrumbs}.
2. Para seleccionar a los empleados cuyos datos de configuración quieres editar, elige un grupo o haz clic en el icono de filtro avanzado {% icon employee-filter | icon-only %}.
3. En la barra de acciones, haz clic en el icono de modificación masiva {% icon mass-update | icon-only %}.<br>Se abre la página de modificación masiva. 
4. En la sección **Parámetros**, utiliza el menú desplegable **Datos fijos** para seleccionar el elemento de configuración que quieres editar para varios empleados a la vez.<br>(Opcional) Usa los campos **Del** y **Al** para limitar el tiempo en que la modificación masiva será efectiva.
5. Selecciona una opción del recuadro **Comandos**.
6. Dependiendo de tu grupo, las siguientes secciones aparecen a la derecha: **Asignaciones existentes**, **Nueva asignación** o **Nuevo período de validez**. En las secciones, selecciona los elementos que quieres añadir, eliminar o reemplazar.
7. Para iniciar la modificación masiva, haz clic en **Aceptar**.<br>Se abre la pantalla de procesamiento de trabajos.<br>Se abre una pantalla con los resultados de tu modificación masiva.

| Pregunta                                                                          | Respuesta                                                                                                                                                                                      |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------- |
| ¿Por qué tienen mis empleados contratos asignados durante un periodo de tiempo más corto que antes de usar la modificación masiva?                              | Si asignas a un empleado un elemento de configuración que excede el periodo de procesamiento, pueden surgir periodos sin asignación.<br>Pongamos el siguiente ejemplo: un empleado tiene un contrato asignado del 1 de marzo al 31 de mayo. Tú introduces un nuevo periodo de validez desde el 1 de marzo al 15 de abril. Tras la modificación masiva, no existe ninguna asignación entre el 16 de abril y el 31 de mayo.                                                                                                                                           |


