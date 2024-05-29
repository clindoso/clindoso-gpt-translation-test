---
title: Understand scheduling rules
product_label:
  - advanced
  - enterprise
  - classic
description: Understand what scheduling rules are and how they impact the scheduling process.
---

Scheduling rules are essential for the scheduling process in injixo. Contract-specific scheduling rules apply individual employee contracts. They ensure that the scheduling aligns with the constraints and parameters defined in contracts.

{% link_new Contract-specific scheduling rules | features/administration/create-contracts.md | #scheduling-rules %} ensure that the conditions of each contract are taken into account during scheduling. For example, if a contract specifies a certain rest period duration or a maximum number of working hours per day, scheduling rules ensure that these conditions are met. Breaching these rules can lead to scheduling conflicts, employee dissatisfaction, and potential contract violations. We highly recommend to talk to your consultant before making any changes to the scheduling rules.

To see a list of all available scheduling rules, go to _WFM > Administration > System > Scheduling rules_{:.breadcrumbs}. Click on a rule to see a description.

## Contract-specific scheduling rules examples

- _2601_{:.id-label} Rest Period Between Two Working Days: Activate this rule to ensure that assigned shifts comply with the rest period between two working days, as defined in the contract. This only applies to activities marked as Comply with Rest Period.
- _2614_{:.id-label} Maximum Number of Working Hours per Day: If you activate this rule, an employee’s working hours cannot exceed the daily maximum set in their contract. This includes hours from both day models and activities.
- _2620_{:.id-label} Check minimum number of weekends off per month as specified in the employee's contract: If you activate this rule, an employee must be assigned at least the number of free weekends per month specified in the contract.
- _2626_{:.id-label} Check maximum number of working hours within 24 hours as specified in the employee's contract: If you activate this rule, you can only assign an employee the number of hours for shifts and activities within 24 hours specified in the contract.

## Status Indicator

You can see the status of each rule in the list:

- Gray: The rule is deactivated and won't be considered during scheduling.
- Yellow: The rule is in soft mode. Breaching this rule will generate a warning during scheduling, but the action will still proceed.
- Red: The rule is fully activated. Any violation of the contract will result in an error message detailing the specific rule violation.

Users with Admin rights have the authority to modify each rule, set exceptions, and even revert user-specific values to default settings.

## Exceptions for contract-specific scheduling rules

- **Current**: Allows exceptions for specific users. Regular users can only make modifications within this section.
- **User**: Users with Admin rights can individually set the rule status for each user based on their contract.
- **User Groups**: Enforces rule status exceptions for designated user groups, ensuring that teams with similar contracts have consistent scheduling rules.
- **Program Components**: Set an exception for certain program components, such as Lottery, Assignment, Request Approval, Capacitor or Optimisation (not recommended).
