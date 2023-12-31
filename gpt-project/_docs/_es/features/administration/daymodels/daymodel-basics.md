---
title: Entender los modelos de horario
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Aprende qué tipos de modelos de horario existen, qué debes considerar antes de crear un modelo de horario y cómo los cambios en un modelo de horario impactan la planificación.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/daymodels/daymodel-creation.md
---

Los modelos de horario son plantillas para turnos. Representan el día laboral para los empleados que planificas, y definen cuándo los empleados están disponibles para trabajar, las horas de inicio y finalización de los turnos, así como el número de horas diarias que un empleado trabaja. injixo se basa en tus modelos de horario para crear planificaciones.

Por defecto, los modelos de horario que creas son asignados automáticamente a todas las unidades de planificación de tu organización. Para cambiar esta configuración predeterminada, {% link_new edita la unidad de planificación | features/administration/create-and-manage-planning-units.md | #limitar-los-modelos-de-horario %}. Durante la planificación optimizada, injixo solo usará los modelos de horario asignados a la unidad de planificación.

Si los modelos de horario configurados para tu unidad de planificación no cubren algunos acuerdos de trabajo, también puedes asignar modelos de horario personales a empleados particulares. Durante la planificación optimizada, injixo solo utilizará los modelos de horario personales para ese empleado.

Los modelos de horario incluyen las actividades de presencia, ausencia y pausa de un turno. Por ello, tienes que {% link_new añadir las actividades relevantes | features/administration/daymodels/daymodel-creation.md | #añadir-actividades-a-modelos-de-horario %} a los modelos de horario.

Los modelos de horario se añaden a las {% link_new rotaciones de turnos | features/administration/shift-sequences.md %} y pueden ser agrupados en {% link_new modelos semanales | features/administration/work-time-pattern-models.md | #crear-modelos-semanales %}.


## Tipos de modelos de horario

Hay tres tipos de modelos de horario. 

> Atención
> 
> - A los modelos de horario de tipo turno fijo también se les llama modelos de horario fijos.<br> 
> - A los modelos de horario de tipo turno variable también se les llama modelos de horario variables.


| Tipo                | Descripción                                                                                                                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Turno fijo         | Los turnos con un modelo de horario fijo tienen horas de inicio y finalización fijas que no pueden ser modificadas. Un modelo de horario fijo solo puede resultar en un único turno. Los modelos de horario fijos se suelen añadir a las {% link_new rotaciones de turnos | features/administration/shift-sequences.md %}.                                      |
| Turno variable      | Los turnos con un modelo de horario variable tienen una hora de inicio flexible dentro de un marco de tiempo definido. Por ello, distintos turnos pueden resultar de modelos de este tipo. Los modelos de horario variables que se añaden a rotaciones de turnos se convierten automáticamente en modelos de horario fijos, ya que se colocan en la primera posición de inicio posible de un turno. |
| Margen de disponibilidad | Este tipo de modelo de horario se usa para definir un rango de tiempo más corto que las horas de apertura de la unidad de planificación. Cuando insertes rotaciones de turnos que incluyan este tipo de modelo de horario, injixo seleccionará los modelos de horario compatibles con este margen de disponibilidad durante el proceso de optimización y en la oferta de turnos. También puedes usar este tipo para configurar la disponibilidad de varios empleados a la vez.          |

## Cuándo usar qué modelo de horario en la planificación

No hay un único escenario de uso para cada tipo de modelo de horario, pero la siguiente lista ofrece una orientación general:

- Turno fijo: usa modelos de horario fijos para planificar a los empleados con horarios de trabajo fijos. Estos turnos siempre empiezan y acaban a una hora fija y no pueden ser movidos en la planificación.
Puedes utilizar modelos de horario fijos en los modelos de planificación para {% link_new crear una planificación optimizada | features/scheduling/scheduling-optimization.md %}, definir patrones semanales repetitivos en las {% link_new rotaciones de turnos | features/scheduling/capacity/capacity-insert-shift-sequences.md %}, o si usas la {% link_new oferta de turnos | features/scheduling/schedules/schedules-shift-bidding.md %}.
- Turno variable: usa modelos de horario variables para planificar a empleados con horarios de trabajo flexibles. injixo puede planificar a un empleado para diferentes turnos con un único modelo de horario de este tipo. Este modelo de día se utiliza habitualmente al {% link_new crear planificaciones optimizadas | features/scheduling/scheduling-optimization.md %} o en la {% link_new oferta de turnos | features/scheduling/schedules/schedules-shift-bidding.md %}.
- Margen de disponibilidad: si las horas de apertura de tu unidad de planificación abarcan un período de tiempo más amplio que un día laboral, puedes limitar las opciones de injixo a la hora de planificar empleados. Para limitar la disponibilidad de varias personas a la vez, usa modelos de horario de tipo Margen de disponibilidad y añádelos a las rotaciones de turnos. De forma alternativa, puedes {% link_new configurar la disponibilidad de empleados específicos | features/administration/availabilities.md %} en la configuración de los empleados. Ambas opciones son tomadas en cuenta durante la planificación optimizada si la regla de planificación 2611 está activada.

Como alternativa a las disponibilidades puedes usar {% link_new rotaciones de turnos | features/administration/shift-sequences.md %} o modelos semanales en los {% link_new modelos de planificación | features/administration/work-time-pattern-models.md | #crear-modelos-semanales %}. También puedes usar ambos para rotar turnos tempranos y tardíos, por ejemplo.

Recomendamos crear un conjunto limitado de modelos de horario variables (combinados con las {% link_new disponibilidades de tus empleados | features/administration/availabilities.md | #create-employee-availabilities %}) en lugar de crear una gran cantidad de modelos de horario fijos.

## Actividad base y duración del turno

Es obligatorio establecer una actividad base para todos los modelos de horario fijos y variables para definir la duración total del turno. En ambos tipos de modelos de horario puedes añadir más actividades que se superpongan a la actividad base. La duración de las otras actividades no puede exceder la duración de la actividad base.

La actividad base cubre el tiempo total que un empleado planificado está presente durante un turno, incluidas las pausas y otras actividades no remuneradas. Es la primera actividad que seleccionas al crear un nuevo modelo de horario, y no puedes eliminarla ni editarla después de guardar el modelo de horario.

El tiempo total de un turno planificado, pausas incluidas, es la duración bruta del turno. Después de deducir las actividades no remuneradas, como pausas o tiempos de preparación, el tiempo de trabajo resultante es la duración neta del turno. Puedes ver la duración neta del turno bajo el nombre Horario real en Planificar y en el Centro de planificación. Ten en cuenta que los contratos también especifican tiempos netos. 

La duración de un modelo de horario debe respetar las horas laborales establecidas en tus {% link_new contratos | features/administration/create-contracts.md %}.
Por ejemplo, un contrato con 40 horas laborales distribuidas en 5 días a la semana requiere un modelo de horario con un tiempo laboral neto de 8 horas diarias. Un contrato de 37,5 horas semanales requiere un modelo de horario con 7,5 horas diarias.

Usa la actividad Presente como actividad base y asegúrate de que esté configurada como Reemplazable. De este modo, las funcionalidades Optimización de tareas y Crear planificación optimizada pueden reemplazar la actividad Presente con otras actividades, siempre y cuando estas tengan {% link_new requisitos de personal calculados | features/forecast/injixo-forecast/staff-requirement.md %} y estén configuradas como planificables.

### Elementos fijos vs. pasillos

Puedes crear un elemento de pasillo si añades una actividad con una duración más corta que el tiempo entre el inicio y fin del elemento. Los elementos de pasillo se superponen a todos los elementos fijos de un turno. La planificación optimizada moverá los elementos de pasillo para optimizar la cobertura. Los pasillos pueden superponerse entre sí, pero no las actividades dentro de dos pasillos.

Cuando insertas manualmente un modelo de horario en la planificación, los elementos de pasillo se colocan a la hora más temprana posible del pasillo. Puedes mover manualmente los pasillos dentro de sus intervalos definidos.

Cuando la duración de un elemento de pasillo coincide exactamente con el elemento de tiempo de inicio y fin configurado, se crea un elemento fijo en su lugar.

