---
title: ¿Qué es la funcionalidad Reuniones?
product_label:
  - advanced
  - enterprise
permalink: /es/meetings-overview/
permalink_reason: Used in the Intercom message managed by i18n.
description: Programa reuniones individuales, grupales y sesiones de aprendizaje para tus empleados automáticamente con la funcionalidad Reuniones.
related_articles:
  - overwrite_title: Revisar y aceptar sugerencias para reuniones
    filepath: features/scheduling/meetings/scheduling-suggestions.md
---

En este artículo aprenderás:

- cómo planificar reuniones 1 a 1, reuniones de grupo y sesiones de auto-aprendizaje con la funcionalidad **Reuniones**;
- qué prerrequisitos debes cumplir;
- las limitaciones a la hora de planificar reuniones.

## ¿Qué es la funcionalidad Reuniones?

En _Plan > Reuniones_{:.breadcrumbs} puedes planificar tres tipos de reuniones para tus empleados:

- {% link_new reuniones 1 a 1 | features/scheduling/meetings/one-on-ones.md %}: planifica reuniones individuales entre empleados y sus coordinadores;
- {% link_new reuniones de grupo | features/scheduling/meetings/group-meetings.md %}: planifica reuniones para grupos de empleados, con o sin organizador;
- {% link_new sesiones de auto-aprendizaje | features/scheduling/meetings/self-learning-sessions.md %}: planifica sesiones de formación individuales para tus empleados.

La funcionalidad **Reuniones** te ahorra tiempo, ya que no tienes que reorganizar las reuniones manualmente para encontrar el momento que mejor se ajuste a tu planificación. La funcionalidad de optimización matemática garantiza que el impacto de las reuniones en cobertura de las actividades planificadas sea mínimo.

## Prerrequisitos y limitaciones

Antes de que empieces a usarla, estos son algunos aspectos importantes de la funcionalidad **Reuniones**:

- requiere un calendario existente en el nivel Plan;
- solo puede sustituir las {% link_new actividades | features/administration/activities.md %} de tipo Presente configuradas como sustituibles;
  - no modifica las actividades no sustituibles;
  - no modifica actividades que no sean de tipo Presente, aunque sean sustituibles;
- no genera sugerencias de reuniones para empleados que no pertenezcan a la unidad de planificación seleccionada durante la configuración de la reunión;
- usa la zona horaria de la unidad de planificación.
- se ejecuta durante un máximo de 10 minutos y ofrece la mejor solución encontrada durante este tiempo.

## Generar sugerencias de horas para las reuniones

1. Ve a _Plan > Reuniones_{:.breadcrumbs}.
2. Decide qué tipo de reunión quieres planificar. Puedes elegir entre {% link_new reuniones 1 a 1 | features/scheduling/meetings/one-on-ones.md %},  {% link_new reuniones de grupo | features/scheduling/meetings/group-meetings.md %} y {% link_new sesiones de auto-aprendizaje | features/scheduling/meetings/self-learning-sessions.md %}. Haz clic en _Configuración_{:.doc-button} en el recuadro correspondiente.
3. Configura los parámetros necesarios para el tipo de reunión elegido.
4. Haz clic en _Generar sugerencias_{:.doc-button}.

## Revisar las sugerencias e incluirlas en la planificación

Una vez hayas iniciado el proceso de generar sugerencias para las reuniones, aparece una entrada en la tabla **Sugerencias generadas**. La entrada muestra cuándo se inició el proceso, el tipo de reunión y la unidad de planificación seleccionada. El proceso puede tardar un tiempo en completarse. Una vez completado, puedes:

1. {% link_new comprobar si el proceso se realizó correctamente | features/scheduling/meetings/scheduling-suggestions.md | #check-if-the-process-was-successful %};
2. {% link_new revisar las sugerencias de horas para las reuniones | features/scheduling/meetings/scheduling-suggestions.md | #review-and-apply-the-suggestions %}, incluir las sugerencias (todas o solo las seleccionadas) en la planificación;
3. {% link_new revisar los resultados de la planificación | features/scheduling/meetings/scheduling-suggestions.md | #review-the-scheduling-results %}.