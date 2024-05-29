---
title: Deactivate, reactivate, and delete employees
product_label:
  - essential
  - advanced
  - enterprise
  - classic
description: Learn when and how to deactivate, reactivate or delete employees.
related_articles:
  - overwrite_title: Add title for untranslated source
    filepath: getting-started/how-does-billing-work.md
---

If you have employees who you no longer schedule or who no longer need access to injixo, you can deactivate or delete them. This has two effects:

- Deactivated employees lose access to injixo.
- Your organization will not be {% link_new billed | getting-started/how-does-billing-work.md %} for these employees anymore (starting the following month).

## Deactivate employees

If employees are not available for work for an extended period of time, e.g. when they take a sabbatical or maternity leave, you can temporarily deactivate them. Your organization will not be billed for deactivated employees. You can reactivate employees when they return. In some cases, the European General Data Protection Regulation (GDPR) may require you to delete an employee's data. If this is the case, [delete](#delete-employees) the employee.

To deactivate an employee, follow these steps:

1. Go to _Plan > Configuration > Employees_{:.breadcrumbs}.
2. In the employee list, click the employee you want to deactivate.
3. In the **Staff Membership** section of the employee configuration dialog, click the {% icon item-edit %}.
4. Enter a leave date.<br>A leave date in the past will immediately deactivate the employee. A future leave date will deactivate the employee on the specified date.
5. Click _OK_{:.doc-button}.<br>A confirmation message appears.
6. To delete future schedules but keep historical scheduling data, click _Yes_{:.doc-button}. To keep all scheduling data of the deactivated employee, click _No_{:.doc-button}.

### List deactivated employees

1. Go to _Account > Users_{:.breadcrumbs}.
2. Click the **Unbilled Users** tab.<br>The table shows all deactivated users for whom your organization is not billed.

### Reactivate employees

To reactivate an employee, e.g. when they return after a long absence, follow these steps:

1. Go to _Plan > Configuration > Employees_{:.breadcrumbs}.
2. Use the search field in the top left corner to find the employee you want to reactivate.<br>A window opens. If you have entered the employee's full name and the search returns only one result, the window shows the employee's configuration dialog. If the search returns several results, the window shows a list of employees.
3. If the window shows a list, click the employee you want to reactivate.
4. In the **Staff Membership** section of the employee configuration dialog, click the {% icon item-add %}.
5. Enter a join date.
6. Click _OK_{:.doc-button}.

## Delete employees

> Warning
>
> You cannot reactivate a deleted employee. The employee will be deleted from all current and future schedules they were scheduled for. Deleting an employee does not affect historical adherence data in {% link_new Intraday | features/intraday/adherence-intraday.md %}.

Delete employees only when their staff membership has ended permanently. When employees are absent for a longer time, e.g. when they take a sabbatical or maternity leave, you can [deactivate](#deactivate-employees) them instead.

To delete an employee, follow these steps:

1. Go to _Plan > Configuration > Employees_{:.breadcrumbs}.
2. In the employee list, click the employee you want to delete.
3. In the action bar, click the {% icon item-delete %}.<br>A confirmation message appears.
4. Click _Yes_{:.doc-button}.<br>The employee and all their current and future schedules are deleted from injixo.

When you delete an employee in injixo, their personal data is anonymized for privacy protection. injixo retains the employee's ID but marks it as deleted, and replaces their name with asterisks. injixo also modifies personal details to remove any identifiable information, such as names, personnel number, addresses, phone numbers, and email addresses. If the employee configuration included ID card numbers, injixo completely deletes them.
