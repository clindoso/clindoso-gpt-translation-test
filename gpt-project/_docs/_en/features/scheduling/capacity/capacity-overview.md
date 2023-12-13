---
title: What is the Capacity feature?
product_label:
  - advanced
  - enterprise
toc: false
description: Learn what the Capacity feature is and how to display the staff requirements, contracted capacity, and resulting coverage per calendar week for a planning unit.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/scheduling/capacity/capacity-insert-shift-sequences.md
---

_Plan > Capacity_{:.breadcrumbs} gives you insights into your future hiring and training needs. Soon, you'll do your long-term planning here.

> This is the very first version. Still pretty basic? Send an email with your feedback and ideas to *capacity-team@injixo.com*.

## Show the capacity per planning unit

Select a **Planning unit**. A table appears that shows the staff requirements, the contracted capacity, and the resulting coverage per calendar week for the whole year. All values are displayed in hours.

The table contains the following rows:

- Staff requirements: The sum of the staff requirements for all activities of the selected planning unit. Make sure to first {% link_new calculate and save | features/forecast/injixo-forecast/staff-requirement.md %} the staff requirements for all activities of the planning unit under Forecast. Otherwise, the staff requirements won't be displayed here.
- Contracted capacity: The sum of the contractual working time of all employees of the selected planning unit. All employees with an assigned contract are considered. Absences do not influence the numbers. The numbers are based on the target working time per week which is defined for each contract in the section {% link_new Work Time Guidelines | features/administration/create-contracts.md | #work-time-guidelines %}.
- Potential coverage: The difference between the Contracted capacity and Staff requirements values.

{{ 1 | image: "Capacity table", '100%' }}
