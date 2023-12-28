---
title: ¿Qué es la función Reuniones?
product_label:
  - advanced
  - enterprise
permalink: /es/meetings-overview/
permalink_reason: Used in the Intercom message managed by i18n.
description: Programa reuniones individuales, grupales y sesiones de aprendizaje para tus empleados automáticamente con la función Planificar reuniones.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/meetings/scheduling-suggestions.md
---

En este artículo aprenderás:

- cómo programar reuniones 1:1, grupales y sesiones de aprendizaje con la función _Reuniones_.
- qué requisitos previos debes cumplir.
- las limitaciones en la programación de reuniones.

## ¿Qué es la función Programar reuniones?

El menú _Plan > Reuniones_ permite programar tres tipos de reuniones para tus empleados:

- {% link_new reuniones 1:1 | features/scheduling/meetings/one-on-ones.md %}: programar reuniones individuales entre empleados y sus coordinadores
- {% link_new Reuniones grupales | features/scheduling/meetings/group-meetings.md %}: programa reuniones para grupos de empleados con o sin anfitriones
- {% link_new Sesiones de aprendizaje | features/scheduling/meetings/self-learning-sessions.md %}: programa invididuales sesiones de entrenamiento para tus empleados

La función _Reuniones_ te ayudará a ahorrar tiempo, ya que no tendrás que reorganizar las reuniones manualmente para encontrar el momento que mejor se ajuste a tu horario. La función de optimización matemática garantiza que el impacto de los espacios horarios para reuniones en la cobertura de las actividades existentes es mínimo.

{{ 1 | image: 'Página general' }}

## Requisitos previos y limitaciones

Algunos aspectos importantes sobre la función Reuniones:

- Requiere un calendario existente en el Level de planning.
- Solo puede reemplazar las {% link_new actividades | features/administration/activities.md %} de tipo Presente que se hayan configurado como Reemplazables.
  - No modifica las actividades no reemplazables: estas se mantienen como están.
  - No modifica actividades de tipos diferentes a Presente, incluso si están configuradas como Reemplazables.
- No genera sugerencias de reuniones para empleados que no formen parte de la unidad de planificación elegida durante el proceso de configuración de la reunión.
- Utiliza la zona horaria de la unidad de planificación.
- Se ejecuta durante un máximo de 10 minutos y ofrece la mejor solución encontrada durante este tiempo.

## Generar sugerencias para espacios en los que celebrar las reuniones

1. Ve a _Plan > Reuniones_{:.breadcrumbs}.
2. Decide qué tipo de reunión quieres programar. Puedes elegir entre {% link_new reuniones 1:1 | features/scheduling/meetings/one-on-ones.md %},  {% link_new reuniones grupales | features/scheduling/meetings/group-meetings.md %} y {% link_new sesiones de aprendizaje | features/scheduling/meetings/self-learning-sessions.md %}. Haz clic en el botón **Configuración** en la tarjeta correspondiente.
3. Configura los **parámetros** necesarios para el tipo de reunión elegido. Los parámetros varían en función del tipo de reunión. Haz clic en uno de los enlaces anteriores para aprender a configurar un tipo de reunión específico.
4. Haz clic en **Generar sugerencias**.

## Revisa las sugerencias y escríbelas en el planning

Cuando has empezado el proceso de generar sugerencias para las reuniones, aparece una entrada en la tabla _Sugerencias generadas_. Se muestra cuándo se inició el proceso, el tipo de reunión y la unidad de planificación seleccionada. El proceso puede tardar un tiempo en completarse. Una vez lo haya hecho, puedes

1. {% link_new comprobar si el proceso se realizó correctamente | features/scheduling/meetings/scheduling-suggestions.md | #comprobar-si-el-proceso-se-ha-realizado-correctamente%},
2. {% link_new revisar las sugerencias de espacios para reuniones | features/scheduling/meetings/scheduling-suggestions.md | #revisar-y-aplicar-las-sugerencias%}, escribir las sugerencias seleccionadas o todas en el planning, y
3. {% link_new revisar los resultados de la planificación | features/scheduling/meetings/scheduling-suggestions.md | #revisar-los-resultados-de-la-planificacion %}.
