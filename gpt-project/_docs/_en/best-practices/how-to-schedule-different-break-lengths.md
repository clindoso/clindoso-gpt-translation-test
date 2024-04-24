---
title: Schedule with different break lengths
product_label:
  - advanced
  - enterprise
  - classic
description: Schedule shifts with breaks of different lengths.
---

Within your organization, you may have agreed to different break lengths with your employees to meet their individual needs. This means that employees with the same contractual working time could have shifts of different lengths. Regardless of this, you can create this with a single contract.

As you only enter the work time guidelines in the contract, you have to make some minor changes to ensure that the optimization takes into account which employee gets short and which gets long breaks.

## Two work time pattern models with different day models

You can restrict the available day models for long and short breaks used by the optimization via Work Time Pattern Models. The optimization takes the Work Time Pattern Model assignment into account and only schedules the day models it contains.

If you have been working with the optimization but without Work Time Pattern Models, the introduction of Work Time Pattern Models of type A (flexible selection) is most likely to be the easiest option.

How to use Work Time Pattern Models:

1. Assign all day models with short breaks to a Week Time Pattern named "short breaks".
2. Add all day models with long breaks to the Week Time Pattern named "long breaks".
3. Create two Work Time Pattern Models of type A (flexible selection).
4. Assign the corresponding Week Time Pattern to the Work Time Pattern Models.
5. Now assign the corresponding Work Time Pattern Models to all employees who only take short breaks (using mass update).
6. Assign the other Work Time Pattern Models to the remaining employees

If you are already working with Work Time Pattern Models, you will need to split your previous Work Time Pattern Model and create two new Work Time Pattern Models of the type you have used so far.

## Personal employee day models

You can also limit the available day models for optimization via personal day models with long and short breaks. The optimization takes into account the day model assignment to the employee and only schedules the assigned day models.

Assign personal day models to your employees. Make the necessary changes under _Administration > Scheduling > Employees_{:.breadcrumbs} in the section _Day Models_. Employees who you want to schedule for short breaks will receive day models with short breaks; the other employees will receive day models with long breaks.

The assignment of day models to an employee is applied system wide, i.e. also for manual scheduling or in the Infothek. The disadvantage is that the assignment process may be time-consuming, as unfortunately mass update does not support this.

Notes on the scheduling rule _2661_{:.id-label} _Check day model assignment to employee_:

- If the rule is activated, an employee is not scheduled if he or she does not have a personal day model.
- If the rule is deactivated, the optimization uses
  - All day models, if an employee does not have a personal day model
  - Only the assigned day model, if an employee has a personal day model.

## Using skills

Employees get their desired break length because the optimization checks the necessary skill for the activities of a day model.

The scheduling rule _2605_{:.id-label} _Check skill_ is always activated and works not only for activities of type present, but for all activities with a skill.

Follow these steps:

1. Define a skill for short breaks and one for long breaks.
2. Assign the appropriate skill to your different break activities.
3. Adjust your day models or create new ones so that there are different shifts with the activities for the short and long breaks.
4. Assign (by mass update) the skill for short breaks to the employees who should get short breaks; the others get the skill for long breaks.

You can also apply these steps if you are using shift bidding instead of optimized scheduling.
