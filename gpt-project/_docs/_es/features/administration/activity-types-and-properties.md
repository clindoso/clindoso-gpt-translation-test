---
title: Tipos y propiedades de las actividades
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Conoce los distintos tipos de actividades y las funciones de las distintas opciones de configuración.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-examples.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/create-and-manage-planning-units.md
  - overwrite_title: Add title for untranslated source
    filepath: best-practices/how-to-schedule-multiskill-agents.md
redirect_from:
  - /es/activity-properties/
redirect_reason: Updated filename on 11 October 2023
---

Cuando {% link_new creas y editas actividades | features/administration/activities.md %}, las diferentes opciones de configuración determinan cómo se usarán y mostrarán las actividades en tus planificaciones e informes.

## Tipos de actividades

El tipo de una actividad influencia la planificación y determina:
- cómo se gestiona la actividad en la planificación optimizada;
- dónde puedes usar la actividad;
- cómo se muestra la actividad en las planificaciones y en el Centro de planificación;
- si los informes incluyen la actividad. <!-- illness, absences, vacation -->

La tabla a continuación ofrece más detalles sobre cada tipo de actividad.

| Tipo     | Descripción                                                                                                                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Presencia | Todas las actividades en las que las personas trabajan.<br>injixo planifica las actividades de tipo Presencia de acuerdo con los requisitos de personal.                                    |
| Pausa    | Pausas remuneradas o no remuneradas durante un turno.<br>Solo las actividades de tipo Pausa pueden ser configuradas en los modelos de horario como pausas. Puedes usar la {% link_new optimización de pausas | features/scheduling/schedules/break-optimization.md %} para distribuir las pausas en la planificación de manera que las actividades con requisitos de personal tengan una cobertura óptima. |
| Enfermedad  | Ausencia remunerada o no remunerada, como un día de enfermedad o una cita médica.<br>Las actividades de tipo Enfermedad son las únicas que se incluyen en los informes de enfermedad.                             |
| Vacaciones | Vacaciones remuneradas o no remuneradas, otros permisos, etc. <br> Las actividades de tipo Vacaciones son las únicas que se incluyen en los informes de vacaciones.                                                 |
| Ausencia  | Otras ausencias que afectan a la planificación, como formación externa, permiso por horas extra, etc.<br>Las actividades de tipo Ausencia son las únicas que se incluyen en los informes de ausencias.              |
| Reunión  | Las actividades de este tipo se usan para {% link_new planificar reuniones | features/scheduling/meetings/meetings-overview.md %}. |

## Propiedades de las actividades

Las propiedades de una actividad afectan a tu planificación y a cómo puedes usar la actividad.
Para establecer las propiedades de una actividad, usa las casillas explicadas a continuación.

| Propiedad                                    | Efecto                 |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Remunerada                                        | Activa el cálculo de horas laborables para las actividades planificadas. Si las pausas o ausencias son remuneradas, serán incluidas en el cálculo de horas laborables. Si no son remuneradas, no serán incluidas en el cálculo de horas laborables.                                                                                                                                       |
| Respetar tiempo de descanso                     | Previene que se incumpla el período de descanso configurado en el contrato. injixo solo verifica el período de descanso si la regla de planificación _2601_{:.id-label} está activada.   |
| Planificable                                   | injixo puede planificar la actividad si usas la funcionalidad Crear planificación optimizada, o puede optimizarla con la optimización de tareas. Recomendamos usar esta propiedad para actividades con requisitos de personal. No se suele activar para actividades de tipo Ausencia, Vacaciones y Enfermedad.                                                                               |
| Se puede solicitar en Me                           | Permite a los empleados solicitar permisos (ausencias, vacaciones o baja por enfermedad) en injixo Me (tiene que existir un {% link_new período de disfrute | features/scheduling/time-off/time-off-periods.md %} con el estado Publicado). En Oferta de turnos, los turnos con actividades de tipo Presencia y Pausa se pueden solicitar de forma automática. |
| Intercambiable en intercambio de turnos              | Permite a los empleados {% link_new intercambiar la actividad entre sí | features/scheduling/schedules/scheduling-periods/schedules-enable-employees-to-swap-shifts.md %} en injixo Me. Para ello, todas las actividades (también las pausas) incluidas en los modelos de horario deben estar configuradas como Intercambiable en intercambio de turnos.                                                                                                                          |
| Permitir sobrecobertura cuando el requisito de personal sea cero | Permite a injixo planificar la actividad incluso en intervalos sin requisitos de personal. Por defecto no se cubren los intervalos con requisitos de personal 0.
|
| Sustituible                               | Permite a injixo sustituir la actividad por otras actividades planificables que tengan requisitos de personal. Esta casilla debe estar marcada para poder {% link_new planificar reuniones | features/scheduling/meetings/meetings-overview.md %} en esta actividad.                                                                                                               |
| Actividad de jornada completa                | Puedes planificar la actividad para una jornada completa en Planificar o en la pestaña Actividades de jornada completa en la vista diaria en el Centro de planificación. Si la actividad también es remunerada, al empleado al que se le asigne se le contabilizará el número de horas laborables diarias definidas como objetivo en su contrato.<br>Esta opción debe estar activada para permitir a los empleados solicitar la actividad como actividad de jornada completa en injixo Me.    |
| Modo de día completo                                | Sólo disponible para actividades de jornada completa. El modo de día completo te permite planificar manualmente la actividad en el Centro de planificación con estado de jornada completa en la pestaña Actividades de jornada completa. Esta acción guarda la entrada sustituida en la planificación para consultas futuras. En consecuencia, injixo excluye a estos empleados del cálculo de la cobertura, pero la entrada de la planificación continúa siendo visible. |
| Trato especial en la planificación optimizada | Solo disponible para actividades de tipo Presencia. Las actividades con esta propiedad solo pueden ser planificadas respetando estrictamente su configuración. Las actividades no pueden ser reemplazadas y su duración no es flexible.<br>Aprende más en [la sección específica](#trato-especial-en-la-planificación-optimizada) a continuación. |

## Trato especial en la planificación optimizada

Esta propiedad significa que la funcionalidad Planificación optimizada solo puede planificar la actividad estrictamente como está configurada. Esta propiedad se utiliza a menudo para programar horas extras o actividades de back-office.<br>
Hay dos escenarios de uso para esta propiedad:

Opción 1: La actividad es parte de un modelo de horario. En este caso, la actividad solo puede ser planificada con la duración que has configurado, y en el marco de tiempo definido en el modelo de horario. La actividad no puede ser usada para sustituir otras actividades sustituibles. Cómo la planificación optimizada usa la actividad depende también de {% link_new  la configuración de la actividad dentro del modelo de horario | features/administration/daymodels/daymodel-creation.md | #añadir-una-actividad-de-presencia-o-ausencia %}:
- Configurada como elemento fijo: la planificación optimizada solo planificará la actividad a la hora exacta para la que ha sido configurada.
- Configurada como elemento de pasillo: la planificación optimizada puede mover la actividad dentro del pasillo (intervalo de tiempo) definido para optimizar la cobertura de otras actividades.

Ejemplo de uso:

- Añade una actividad de back-office sin requisitos de personal y con una duración de una hora a tu modelo de horario. La funcionalidad Planificación optimizada planificará la actividad con una duración de exactamente una hora. Si la actividad está configurada en el modelo de horario como elemento de pasillo, la actividad será movida  dentro del pasillo al intervalo de tiempo donde tenga el menor impacto en la cobertura de otras actividades.

Opción 2: La actividad no es parte de un modelo de horario. En este caso, la funcionalidad Planificación optimizada no puede planificar la actividad automáticamente, y tampoco puede usarla para reemplazar otras actividades sustituibles. La actividad solo puede ser planificada manualmente.

Ejemplo de uso:

- Crea una actividad de horas extra que no esté incluida en ningún modelo de horario. La funcionalidad Planificación optimizada no planificará la actividad y no la usará para reemplazar actividades sustituibles. Añade la actividad a la planificación manualmente cuando sea necesario. En este escenario, siempre tienes control completo sobre cuándo la actividad es planificada, durante cuánto tiempo, y a quién se le asigna.

> Atención
>
> Esta propiedad solo está disponible una vez hayas creado la actividad.

## Subactividades

Puedes asignar actividades a otras actividades. La actividad a la que se le asignan actividades se convierte en una multiactividad. Las actividades asignadas son las subactividades de la multiactividad. Las multiactividades te permiten planificar a empleados con múltiples cualificaciones cuando se requiera una de sus cualificaciones. En la lista de las actividades, las multiactividades están marcadas con el icono <em class="multiactivity-icon"></em>.

La funcionalidad Crear planificación optimizada puede planificar multiactividades si te aseguras de cumplir lo siguiente:

- Selecciona el tipo Presencia para las multiactividades y todas las subactividades.
- Configura tanto las multiactividades como las subactividades como remuneradas y planificables.
- Asigna todas las subactividades (y después la multiactividad) a tu unidad de planificación.
- Para controlar quién puede ser incluido en la planificación, asigna una cualificación distinta a cada subactividad.
- (Opcional) Asigna una cualificación a la multiactividad. En este caso, los empleados deberán tener esta cualificación particular para que se les asigne la multiactividad. Por defecto, la multiactividad no requiere cualificaciones.

> Atención
>
> Si no usas Crear planificación optimizada, sino la optimización de tareas, injixo puede sustituir las actividades sustituibles por multiactividades. Esto solo es posible si el empleado está cualificado para realizar al menos una subactividad de la multiactividad.
