---
title: Configuración de base
description: Los datos de configuración necesarios para crear una planificación.
redirect_from:
  - /es/configuration-hints/
  - /es/quickstart-base-configuration/
redirect_reason: Updated filename on 24 July 2023
product_label:
  - essential
  - advanced
  - enterprise
promote-service: new-planner-training
---

Antes de empezar a planificar, debes definir la configuración de base en injixo. Algunos de estos elementos de configuración son estrictamente necesarios para que injixo pueda crear planificaciones, mientras que otros son opcionales y dependerán de los {% link_new métodos de planificación | features/scheduling/scheduling-methods.md %} que quieras utilizar.

## Orden de configuración

Recomendamos configurar los elementos en el orden presentado en la siguiente sección. Los elementos de configuración tienen interdependencias y algunos pueden ser asignados a otros. Sigue los enlaces en la tabla para obtener más información sobre cada elemento de configuración y cómo configurarlos.
No hay dos configuraciones iguales, por lo que el orden óptimo para tu organización puede ser diferente al presentado aquí. <br>Usa este artículo como una lista de tareas para ayudarte durante el onboarding. Contacta con tu consultor si tienes cualquier duda.

### Elementos de configuración requeridos

La tabla a continuación ofrece una descripción general de los elementos de configuración requeridos que debes configurar en injixo, independientemente del método de planificación que quieras utilizar.

<table>
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 75%;">
  </colgroup>
  <thead>
    <tr>
      <th>Elemento de configuración</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{% link_new Cualificaciones | features/administration/work-with-skills.md %}</td>
      <td>Las cualificaciones representan las habilidades de tus empleados. Al asignar cualificaciones a los empleados, los marcas como capaces de trabajar en ciertas actividades. injixo requiere que asignes cualificaciones a actividades en las que solo ciertas personas pueden trabajar. No tienes que añadir cualificaciones a actividades en las que todos pueden trabajar.</td>
    </tr>
    <tr>
      <td>{% link_new Actividades | features/administration/activities.md %}</td>
      <td>Las actividades son tareas, reuniones y ausencias que tu organización planifica e incluye en informes.<br> Las actividades se añaden a los modelos de horario y las unidades de planificación.</td>
    </tr>
    <tr>
      <td>{% link_new Modelos de horario | features/administration/daymodels/daymodel-creation.md %}</td>
      <td>Los modelos de horario son plantillas de turno. Los modelos de horario definen la hora de inicio y finalización de un turno, así como las horas de trabajo diarias de una persona. Contienen todas las actividades de presencia, pausa y ausencia de un turno.<br>Los modelos de horario se asignan a unidades de planificación. También pueden ser agrupados en modelos semanales.</td>
    </tr>
    <tr>
      <td>{% link_new Unidades de planificación | features/administration/create-and-manage-planning-units.md %}</td>
      <td>Las unidades de planificación representan las ubicaciones, reales o virtuales, de tus empleados. Se utilizan para agrupar a los empleados para fines de planificación.</td>
    </tr>
    <tr>
      <td>{% link_new Contratos | features/administration/create-contracts.md %}</td>
      <td>Los contratos contienen información sobre los acuerdos de trabajo contractuales de tus empleados, incluidas las horas de trabajo mínimas, objetivo y máximas para cada día, semana y mes.<br>Los contratos se asignan a los empleados.</td>
    </tr>
    <tr>
      <td>{% link_new Empleados | features/administration/employee-overview.md %}</td>
      <td>En Empleados introduces información sobre cada empleado que incluyas en la planificación. injixo se basa en esas informaciones y en las asignaciones de los empleados (modelos de día, unidades de planificación, contratos, habilidades), para saber cuándo pueden trabajar y en qué actividades.</td>
    </tr>
  </tbody>
</table>


### Elementos de configuración opcionales

La tabla a continuación brinda una descripción general de los elementos de configuración opcionales que puedes configurar en injixo, dependiendo de la configuración de tu organización y del método de planificación que quieras usar.

<table>
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 75%;">
  </colgroup>
  <thead>
    <tr>
      <th>Elemento de configuración</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>{% link_new Rotaciones de turnos | features/administration/shift-sequences.md %} (requerido para planificación fija)</td>
      <td>Una rotación de turnos es un conjunto de modelos de horario o actividades con un patrón repetitivo.<br>Las rotaciones de turnos se asignan a las personas.</td>
    </tr>
    <tr>
      <td>{% link_new Grupos | features/administration/selections.md %}</td>
      <td>Los grupos te permiten filtrar y agrupar empleados, o planificarlos de acuerdo con cualquier criterio dado, p.&nbsp;ej., personas que pertenecen al mismo equipo o tienen el mismo tipo de contrato.<br> Los grupos se asignan a los empleados.</td>
    </tr>
    <tr>
      <td>{% link_new Modelos de planificación y modelos semanales | features/administration/work-time-pattern-models.md %}</td>
      <td>Los modelos de planificación y los modelos semanales te ayudan a organizar los turnos y a asegurar una distribución justa de los turnos y rotaciones entre los empleados planificados. Los modelos de planificación contienen al menos un modelo semanal. Los modelos semanales agrupan turnos por parámetros como la hora de inicio, duración del turno o actividades. Contienen conjuntos de modelos de horario.<br>Los modelos semanales se asignan a los modelos de planificación. Los modelos de planificación se asignan a los empleados.</td>
    </tr>
    <tr>
      <td>{% link_new Calendarios de planificación y tipos de día | features/administration/planning-calendar.md %}</td>
      <td>Los calendarios de planificación contienen días con horarios de apertura y requisitos de personal que se desvían del estándar (p.&nbsp;ej., días de campañas de marketing o festivos nacionales). Estos días especiales se configuran utilizando tipos de día. Esto ayuda a garantizar que se consideren automáticamente durante la planificación sin esfuerzo manual adicional.<br> Los calendarios de planificación se asignan a las unidades de planificación.</td>
    </tr>
  </tbody>
</table>


## ¿Y ahora?

¡Felicidades! Ya puedes {% link_new crear tu primera previsión | getting-started/calculate-a-forecast.md %}. ¡Qué te diviertas planificando!
