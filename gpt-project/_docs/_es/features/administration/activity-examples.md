---
title: Ejemplos de actividades
product_label:
  - essential
  - advanced
  - enterprise
  - classic
toc: false
description: Configura actividades estándar con la ayuda de ejemplos.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activities.md
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/work-with-skills.md
---

Para configurar cómo injixo maneja las actividades durante la planificación y en los informes, usa los {% link_new tipos y propiedas de las actividades| features/administration/activity-types-and-properties.md %} en _Plan > Configuración > Actividades_{:.breadcrumbs}.

A continuación encontrarás ejemplos de configuración para actividades usadas frecuentemente y sus tipos y actividades correspondientes.

## Presencia, pausa, enfermedad y vacaciones

Esta tabla incluye ejemplos de configuración para los tipos de actividad presencia, pausa, enfermedad y vacaciones.
La actividad Presente es una actividad estándar preconfigurada en injixo. Puedes usarla para todas las actividades en las que tus empleados trabajen y que estén basadas en los requisitos de personal, p.&nbsp;ej., Llamadas. 

<div class="table__wrapper" markdown="1">

<style>
table {
   width: 100%;
}
</style>

|                                        |  Presente  | Pausa para comer |         Enfermedad         |  Vacaciones |
| ------------------------------------------- | :---------------------: | :----------------------: | :---------------------: | :---------------------: |
| **Tipo**                                        |         Presencia         |          Pausa           |         Enfermedad         |        Vacaciones         |
| Remunerada                                        | <i class="fa fa-check"> |                          | <i class="fa fa-check"> | <i class="fa fa-check"> |
| Respetar tiempo de descanso                     | <i class="fa fa-check"> |                          |                         |
| Planificable                                   | <i class="fa fa-check"> |                          |                         |
| Se puede solicitar en Me                                 |                         | <i class="fa fa-check">  |                         | <i class="fa fa-check"> |
| Sustituible                                 | <i class="fa fa-check"> |                          |                         |
| Intercambiable en intercambio de turnos            | <i class="fa fa-check"> | <i class="fa fa-check">  |                         |
| Actividad de jornada completa                  |                         |                          | <i class="fa fa-check"> | <i class="fa fa-check"> |

</div>

Dependiendo de las normativas de tu organización, los contratos o las regulaciones laborales, algunas pausas pueden ser no remuneradas. En este caso, desmarca la casilla Remunerada.

## Ausencias y reuniones

Esta tabla incluye ejemplos de configuración para los tipos de actividad ausencia y reunión.
Las ausencias pagadas se usan por regla general para compensar horas extraordinarias o como un bloqueador para {% link_new planificar días festivos | best-practices/scheduling-public-holidays.md %}.
Si hay días en los que un empleado no puede trabajar bajo ninguna circunstancia, puedes bloquearlos con la configuración detallada aquí para Ausencia no remunerada.

<div class="table__wrapper" markdown="1">

|                                          | Ausencia remunerada | Ausencia no remunerada |    Reunión de jornada completa     |  Formación  |
| --------------------------------------------- | :-----------------------: | :-------------------------: | :---------------------: | :---------------------: |
| **Tipo**                                          |          Ausencia          |           Ausencia           |         Reunión         |         Reunión         |
| Remunerada                                          |  <i class="fa fa-check">  |                             | <i class="fa fa-check"> | <i class="fa fa-check"> |
| Respetar tiempo de descanso                       |                           |                             | <i class="fa fa-check"> |
| Planificable                                     |                           |                             |                         |
| Se puede solicitar en Me                                   |  <i class="fa fa-check">  |   <i class="fa fa-check">   |                         |
| Sustituible                                   |                           |                             |                         |
| Intercambiable en intercambio de turnos              |                           |                             |                         |
| Actividad de jornada completa                    |  <i class="fa fa-check">  |   <i class="fa fa-check">   |                         | <i class="fa fa-check"> |

</div>

También puedes utilizar las ausencias remuneradas como días de compensación por horas extraordinarias o como bloqueo pagado cuando {% link_new planifiques días festivos| best-practices/scheduling-public-holidays.md %}.<br>
La actividad de ausencia no remunerada también se puede utilizar para determinar de manera flexible qué días un empleado no trabajará bajo ninguna circunstancia.