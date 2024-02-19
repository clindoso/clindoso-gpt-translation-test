---
title: Understand valuation
description: Learn how injixo valuates time in time-off requests.
product_label:
  - essential
  - advanced
  - enterprise
---

When people request time off, injixo differentiates between the following:
- The actual time off, i.e. the time range that a person is absent from work
- The valuated time off, i.e. the time that will be deducted from a person's entitlement, and that they will be compensated for if they requested paid time off.<br>
Valuated time off can be quantified in hours or days, depending on the [time unit of the time-off type](https://help.injixo.com/time-off-types#create-a-time-off-type).

For example, when a person with a full-time contract is absent for one day, which would result in an actual absence of 24&nbsp;hours, injixo valuates 8&nbsp;hours that need to be deducted from the person's vacation entitlement. This equals the paid time off that the person will be compensated for.

Note that all valuation-related settings apply to your entire organization by default. It is possible to [set up time-off valuation per planning unit](#time-off-valuation-per-planning-unit).

injixo can valuate time off based on either or both of the following items:
- A person's contract
- A person's schedule

The valuation can be further influenced by the following factors:
- Selected time-off unit (days or hours)
- Public holidays
- Multiple time-off requests of one person within one week
- Rounding functionality

To view how injixo valuates individual days in a multi-day time-off request, go to _Plan > Time Off_{:.breadcrumbs} <span class="beta-icon">Beta</span> and hover over an entry in the **To be booked** column. Depending on the time unit of the [time-off type](https://help.injixo.com/time-off-types#create-a-time-off-type), a pop-up displays the number of hours or the fraction of a day to be booked for each day, including days with 0&nbsp;hours. For full-day time-off requests with the time unit days, injixo will display 1&nbsp;day.

## Time-off valuation based on a person's schedule

There are two options for time-off valuation based on the schedule:
- Option 1: injixo only uses the schedule as a basis for valuation if there is a published scheduling period. If there is no published scheduling period, injixo uses the contract as a basis for valuation by default.
- Option 2: injixo always uses the schedule as a basis for valuation. This also applies if there is no published scheduling period. If you want to use this option, contact your consultant.

When the valuation is based on the schedule, injixo compares the requested time off with the person's scheduled paid activities for the same time frame. When a time-off request is approved, the time scheduled for paid activities will be deducted from the person's entitlement and the person will receive compensation for that time.

The following table provides several examples with different parameters of a time-off request:

| Time unit | Scheduled |  Requested time off | Valuated time | 
|--------------------|--------------------|--------------------|--------------------|
| hours | four hours of paid activities | one day | four hours |
| days | four hours of paid activities | one day | one day |
| hours | from 9&nbsp;AM to 5&nbsp;PM with a 30-minute unpaid break starting at 12&nbsp;PM (7.5h) | from 9&nbsp;AM to 12&nbsp;PM (3h) | three hours |
| days | from 9&nbsp;AM to 5&nbsp;PM with a 30-minute unpaid break starting at 12&nbsp;PM (7.5h) | from 9&nbsp;AM to 12&nbsp;PM (3h) | 0.4 days |
| hours/days| no scheduled activities | one day | zero hours/days |

If your organization schedules people using shift sequences only, e.g. because you cannot represent people's individual working agreements with contracts in injixo, the valuation always needs to use the schedule as a basis. If this is the case, contact your consultant to have that option activated for you.

## Time-off valuation based on a person's contract

There are two types of contracts the valuation can be based on:<br>
- Standard: The contract states how many days in a week are working days. These days are defined once and they never change.
- Flexible: The contract states how many days in a week are working days. It does not specify on which days the person is working. The days do not need to be consecutive and they can change from one week to the next.

In Time Off <span class="beta-icon">Beta</span>, by default, contracts are used as a fall-back option for valuation if there is no published scheduling period. If you want to exclude contracts from the time-off valuation, e.g. because you only schedule people with shift sequences, contact your consultant. When contracts are excluded from the time-off valuation, injixo will always use people's schedules as a basis, regardless of whether it is published or not.

Optionally, for valuation based on contracts, injixo can consider public holidays if the contract is flexible. When a person with a flexible contract requests time off for a time frame that includes a public holiday, injixo will not deduct the public holiday from the person's entitlement when the option is activated. Instead, the number of working days per week will be reduced by the amount of public holidays during the time frame of a person's requested time off. If you want to use this functionality, contact your consultant.
Make sure to add the public holidays you want injixo to consider to your planning calendar.

The following table provides several examples with different parameters of a time-off request:

| Time unit | Target working time |  Requested time off | Valuated time | 
|--------------------|--------------------|--------------------|--------------------|
| hours | four hours | one day | four hours |
| days | four hours | one day | one day |
| hours | from 9&nbsp;AM to 5&nbsp;PM with a 30-minute unpaid break starting at 12&nbsp;PM (7.5h) | from 9&nbsp;AM to 12&nbsp;PM (3h) | three hours |
| days | from 9&nbsp;AM to 5&nbsp;PM with a 30-minute unpaid break starting at 12&nbsp;PM (7.5h) | from 9&nbsp;AM to 12&nbsp;PM (3h) | 0.4 days |
| hours/days| no scheduled activities | one day | zero hours/days |

### Standard contracts

In standard contracts, the daily target working time determines the time that is deducted from a person's entitlement and that they are compensated for. 
- If the unit of the time-off type is hours, the corresponding amount of hours is deducted.
- If the unit of the time-off type is days, either a full day or a fraction of a day is deducted, depending on whether the time-off request is for a full day or a partial day.
Depending on the defined working days in a person's contract, injixo starts the time-off valuation on the first day of the time-off request and continues from there, valuating only regular working days and dismissing regular days off. For example, if a part-time person works from Monday until Thursday and requests two weeks off, eight days or the corresponding amount of hours will be deducted from their entitlement.

### Flexible contracts

For part-time people, a flexible contract may be the preferred option because they want to work on varying days. When a person with a flexible contract requests time off, injixo starts the time-off valuation on the first day of the time-off request and valuates the consecutive days as working days up to the total number of weekly working days. For example, when a person who works three days per week requests time off from Wednesday-Saturday, injixo valuates Wednesday-Friday as working days that are deducted from the person's entitlement and for which the person will receive compensation.

When the time-off valuation is based on a person's contract, injixo does not consider the person's schedule for time-off valuation. However, for flexible contracts, injixo will consider already approved paid time off in the person's schedule if it falls into the same week as the new time-off request. The amount of approved time off is then valuated as the corresponding number of working days or hours. For example, a person who only works three days per week requests two days off. After you have [approved their time-off request](https://help.injixo.com/time-off#approve-or-reject-time-off-requests), they submit another time-off request for two more days within the same week. injixo will then consider that there is already a paid absence for two days in the person's schedule and will only deduct one more day from their entitlement. If a person submits several time-off requests for one week and you haven't approved any of them yet, you need to handle them one at a time. You cannot approve them in bulk.

## Time-off valuation in days versus hours  

Depending on your national legislation or organizational preferences, you can choose whether you want injixo to valuate time off in days or in hours when you create a new time-off type.

If you choose valuation in hours, make sure you have configured all of your people's daily target working hours (according to their contract) or the duration of their daily paid activities (according to their schedule) so that injixo can use those for the valuation.

If you choose valuation in days, every working day that is requested as a day off is valuated as one entire day (according to contract or schedule). This applies to both full-time and part-time people.
For example, a part-time person with a flexible contract has different working hours throughout the week. On some days, they only work three hours, on others, five. If they request one day off on a day on which they only work three hours, their entitlement will be reduced by a full day but they will also be compensated for a full day. How much that is, depends on the basis for valuation, i.e. the number of scheduled paid activities for the day or the contractual target working time. People can also request partial days off.

### Valuation for partial-day time-off requests

If the valuation is based on the schedule, the number of paid hours in a shift is used as a basis for valuation.
For example, if a part-time person was scheduled for two paid hours on a specific day and they request two hours of time off for that day instead of submitting a full-day time-off request, a full day will still be deducted because it equals all of their working hours on that day. If they were scheduled for four hours on that day and they request two hours of time off, only half a day will be deducted.

If the valuation is based on the contract, the target working time per day equals the number of paid time. If a person requests a partial day off, injixo displays a decimal value by default. For example, if a full-time person working 8&nbsp;hours per day requests two hours off, injixo displays 0.25 days in the **To be booked** column. This can be avoided with the rounding functionality.

### Rounding

Rounding can be helpful if your organization uses valuation in days. This functionality works for valuation based on either contracts or schedules. When people request partial days off, injixo displays a decimal number. For easier processing of time-off requests, the valuated time can be rounded, so you only need to decide on full-day or half-day time-off requests.

- Partial-day time-off requests with a time range of up to half a working day (according to contract or schedule) will be rounded to a half working day. The person's entitlement will be reduced by a half day and they will receive compensation for a half day.
- Partial-day time-off requests with a time range exceeding half a working day will be rounded to a full working day. The person's entitlement will be reduced by one day and they will receive compensation for a full day.

If you want to use this option, contact your consultant.

## Time-off valuation for night shifts

If a person is scheduled to work a night shift that starts before midnight of one day and ends after midnight of the following day, and they request a day off, injixo handles their time-off request differently than the [default setting](https://help.injixo.com/time-off#time-off-requests-for-night-shifts). 

The following table provides several examples for requested time off:

| Scheduled night shift | Time-off request |   Time off in schedule | Valuated time (hours/days) | 
|--------------------|--------------------|--------------------|--------------------|
| 25&nbsp;June, 10&nbsp;PM until 26&nbsp;June, 6&nbsp;AM | 26&nbsp;June | 26&nbsp;June, 6&nbsp;AM until 27&nbsp;June midnight (18&nbsp;hours) | eight&nbsp;hours (one&nbsp;day) |
| 25&nbsp;June, 10&nbsp;PM until 26&nbsp;June, 6&nbsp;AM | 25&nbsp;June | 25&nbsp;June, midnight until 26&nbsp;June 6&nbsp;AM (30&nbsp;hours) | eight&nbsp;hours (one&nbsp;day) |
| 25&nbsp;June, 10&nbsp;PM until 26&nbsp;June, 6&nbsp;AM and 28&nbsp;June, 10&nbsp;PM until 29&nbsp;June, 6&nbsp;AM | 25&nbsp;June until 29&nbsp;June | 25&nbsp;June, midnight until 29&nbsp;June 6&nbsp;AM | 16&nbsp;hours (two&nbsp;days) |
| no scheduled night shift but scheduled during the day | 26&nbsp;June |  26&nbsp;June, midnight until 27&nbsp;June, midnight | eight&nbsp;hours (one&nbsp;day) |


## Time-off valuation per planning unit

By default, the time-off valuation settings apply to your entire organization. If your organizational setup requires a different time-off valuation per planning unit, e.g. due to different time zones or labor laws, the following options can be activated for each planning unit individually:
- The option to only consider the schedule for valuation, e.g. if you work with shift sequences
- The rounding option if you work with days as the time unit of the time-off type
- The option to consider public holidays if you work with contracts as a basis for valuation

Note: If a person is assigned to several planning units, their time-off request will be valuated based on their primary planning unit, i.e. the planning unit with the highest priority. The priority is set when you {% link_new assign the planning unit to the person | features/administration/employee-overview.md | #mandatory-scheduling-settings %}.

## Your optimal setup

Your consultant will help you with the optimal time-off valuation setup for your organization. To help them better understand your needs, look at the following questions: 

- What do you want to use as a basis for valuation?
- Do you schedule people with shift sequences only?
- Do you publish scheduling periods?
- Do you use days or hours as the unit for time-off types?
- Do you have several planning units with different time-off valuation needs?

## Frequently asked questions

### Why do I not see a valuation for a time-off request?

There are several possible scenarios:
- Scenario&nbsp;1: The valuation is [based on the contract](#time-off-valuation-based-on-a-persons-contract). The person who requested time off has multiple contracts that apply during the requested time off.<br>
- Scenario&nbsp;2: Part of the requested time off falls into a period with a published scheduling period and another part is not covered by a published scheduling period. By default, injixo uses the person's contract as a basis for valuation for time ranges without a published scheduling period. This can cause a conflict.<br>
- Scenario&nbsp;3: The valuation is [based on schedules](#time-off-valuation-based-on-a-persons-schedule) only. A person requests time off for a period during which they are not scheduled for any paid activities.<br>
- Scenario&nbsp;4: A person requests one day off and the valuation is based on their contract. Their contract does not specify a target working time for the day for which they requested time off.<br>
- Scenario&nbsp;5: The time-off valuation is based on schedules only. The published schedules do not cover the entire [time-off period](https://help.injixo.com/time-off-types#time-off-period). People request time off for days for which there is no schedule.<br>
- Scenario&nbsp;6: A person requests time off of a time-off type that does not have a [time unit](https://help.injixo.com/time-off-types#create-a-time-off-type).

### Why can the hours/days to be booked change until the time-off request has been approved?

- Scenario&nbsp;1: If you haven't published the schedule before a person requests time off (e.g. before a weekend), the basis for valuation is the contract, unless the option to always use the schedule is activated. If you publish the schedule while the time-off request is pending, the basis for valuation automatically changes from contract to schedule. As a result, the hours/days to be booked can change.<br>
- Scenario&nbsp;2: If the basis for valuation is the schedule, changes to the schedule can affect the time to be booked, e.g. if you delete a shift or change an unpaid activity to a paid one.

### Why is the valuation different for agents than for planners?

Currently, planners see the valuated time off while agents see the actual time off, i.e. the time range of the time off. These views are not aligned yet.
