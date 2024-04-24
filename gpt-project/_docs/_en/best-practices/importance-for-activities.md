---
title: Importance value for activities
product_label:
  - advanced
  - enterprise
  - classic
description: Use the importance value to prioritize activities during optimized scheduling.
toc: true
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: features/administration/activity-types-and-properties.md
---

<!-- Compare with https://update-importance-of-activities.help.injixo.com/importance-for-activities/ -->

You can define an importance value for each activity in _Plan > Configuration > Activities_{:.breadcrumbs}.

## Why do I need the importance value for activities?

By default, the job optimization will schedule employees for activities with lower staff requirements first. Overstaffing activities with higher staff requirements has less negative impact than understaffing activities with lower staff requirements.

As a consequence, activities with higher staff requirements might be understaffed if there are not enough employees available. You can bypass this setting and prioritize activities with higher staff requirements by using the importance value (default: 100%). The higher an activity's importance value is, the more the job optimization will attempt to match the staff requirements as closely as possible.
For example, you can use this functionality if you need to prioritize one activity over another, such as B2B hotline over B2C hotline.

If an activity requires five employees, scheduling five employees would result in the optimal coverage. To prioritize this activity, set a high importance value (100%). The job optimization will then try to schedule employees so that staff requirements are accurately met. 

Activities that can be overstaffed in your schedule should have a lower importance value. With an importance value of 20%, the job optimization would schedule the exact number of required employees or more, if they are available.

## Prerequisites

For prioritizing activities with the importance value, the following must be true:
- The activities that need to be prioritized are configured as **Plannable** and **Replaceable**.
- The employees who need to work on the prioritized activities are scheduled on the **Present** activity (ID 1).

If your employees are scheduled for other, non-replaceable activities or if there is a pre-scheduled activity block in their day model, the importance value has no effect. The job optimization then cannot change the activity for the day or certain intervals.
Also, your employees' skills or the activity's properties such as the **Plannable** option could prevent the job optimization from allocating more resources to this activity.

## Example

- There are two activities A and B.
- 26 employees are available and skilled to work on activities A and B.
- The staff requirements for each activity are 10 employees.
- Activity A has an importance value of 20% and activity B of 100%.

The job optimization schedules 10 employees each to activities A and B, exactly meeting the staff requirements. However, there are still 6 more employees that need to be scheduled.
Due to the five times lower importance value, the job optimization can assign five more employees to activity A before it has the same negative impact on the overall coverage as assigning one more employee to activity B. Thus, injixo tends to overstaff activity A over-proportionally.
